"""
Command. Agentic user study for one section of the talk.

1. Renders the section's slides (build_v2 --only SECTION, then deckcraft-cli render).
2. Listener: a fresh `claude -p` that has never read the paper. It sees only the slide images and the
   spoken words, then answers the must_know questions in research/exam_<section>.json.
3. Examiner: a fresh `claude -p` that reads the chapter .tex and the exam. It grades the listener and
   grills the talk with the defense questions, saying which ones the talk leaves unanswered.
Writes .scratchpad/study/<section>/<run>/{listener.md, examiner.md}. Run: python user_study.py SECTION [--run NAME]
"""
import json
import subprocess
from pathlib import Path

import fire

AGENTS = Path(__file__).resolve().parents[1]
THESIS_SRC = AGENTS.parents[1] / "source" / "src"
STUDY = AGENTS / ".scratchpad" / "study"
CHAPTERS = {"peekaboo": "1_Peekaboo", "diffillusions": "2_DiffIllusions", "magick": "3_MAGICK",
            "gwtf": "4_GWTF", "motionv2v": "5_MotionV2V"}
LISTENER_MODEL = "sonnet"  # a smart outsider, like a committee member who never read the paper
EXAMINER_MODEL = "opus"
RENDER_SCALE = 1
VIDEO_FRAME_FRACTIONS = (0.1, 0.5, 0.9)  # the listener can't watch video, so it sees start, middle and end


def talk_transcript(slides, image_paths, video_frames):
    """
    Pure function. The listener's view: one block per slide with its image, video frames and spoken words.

    Args:
        video_frames (list[list[str]]): per slide, frame images of the videos playing on it

    Examples:
        >>> talk_transcript([{"speech": "Hi."}], ["/s/slide-01.png"], [[]])
        'SLIDE 1 (image: /s/slide-01.png)\\nRyan says: "Hi."'
        >>> talk_transcript([{"speech": "Hi."}], ["/s/1.png"], [["/f/a.png"]])
        'SLIDE 1 (image: /s/1.png)\\n  video on this slide plays; frames over time: /f/a.png\\nRyan says: "Hi."'
    """
    blocks = []
    for i, (s, p, frames) in enumerate(zip(slides, image_paths, video_frames)):
        video = "\n  video on this slide plays; frames over time: " + ", ".join(frames) if frames else ""
        blocks.append('SLIDE %d (image: %s)%s\nRyan says: "%s"' % (i + 1, p, video, s.get("speech", "")))
    return "\n\n".join(blocks)


def extract_frames(video, out_stem):
    """Command. Saves frames of video at VIDEO_FRAME_FRACTIONS of its length. Returns their paths."""
    probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video],
                           capture_output=True, text=True, check=True)
    duration = float(probe.stdout)
    paths = []
    for k, f in enumerate(VIDEO_FRAME_FRACTIONS):
        path = "%s_%d.png" % (out_stem, k)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(duration * f), "-i", video, "-frames:v", "1",
                        "-vf", "scale='min(1280,iw)':-2", path], check=True)
        paths.append(path)
    return paths


def slide_video_frames(slides, out_dir):
    """Command. Per slide, frame images of each video element (written under out_dir/frames)."""
    (out_dir / "frames").mkdir(exist_ok=True)
    return [[f for j, e in enumerate(s.get("elements", [])) if e["kind"] == "video"
             for f in extract_frames(e["path"], str(out_dir / "frames" / ("s%02d_e%d" % (i + 1, j))))]
            for i, s in enumerate(slides)]


def listener_prompt(transcript, questions):
    """Pure function. Prompt for the naive committee member. Example: listener_prompt('SLIDE 1...', ['Q?']) -> str"""
    qs = "\n".join("%d. %s" % (i + 1, q) for i, q in enumerate(questions))
    return f"""You are a computer-science professor on a PhD thesis committee. You know generative AI and diffusion
models in general, but you have NEVER read this student's papers. You are watching one section of the
student's talk. You only know what is on the slides and what the student says aloud.

Look at EVERY slide image (and every listed video frame) with the Read tool, in order, while reading
what the student says on it.
Use nothing else: do not open any other file, do not search the web.

{transcript}

Then write, in this order:
A. For each slide: one line saying what you understood from it, or exactly what confused you
   (something shown but not explained, a term not defined, a jump in logic).
B. Answer these questions from the talk alone. If the talk didn't tell you, say "NOT IN TALK" — do not guess.
{qs}
C. The 3 sharpest questions you would ask the student after this section."""


def examiner_prompt(chapter_dir, transcript, exam, listener_answers):
    """Pure function. Prompt for the paper-expert examiner. Example: examiner_prompt(Path('ch'), 'T', {}, 'A') -> str"""
    return f"""You are a tough thesis committee examiner who HAS read this paper closely. Read the chapter's .tex
files in {chapter_dir} first. Committee: Dimitris Samaras (vision/graphics), Michael Ryoo (video understanding,
robot learning; the advisor), Yifan Sun (ML/optimization). They are sharp and see through hand-waving.

Here is one section of the student's talk (slide images + spoken words). Look at every slide image with Read.

{transcript}

The exam (reference answers and defense questions), written independently from the paper:
{json.dumps(exam, indent=1)}

A listener who never read the paper watched the talk and answered:
{listener_answers}

Write:
1. SCORE: for each must_know question, CORRECT / PARTIAL / WRONG / NOT IN TALK, with one line why.
   Then a total like "5.5/8".
2. DEFENSE: for each defense question, does the talk already arm the student to answer it? ANSWERED / WEAK / MISSING.
3. BULLSHIT: anything on the slides or in the speech that is wrong, overclaimed, or vague enough to be attacked.
4. FIXES: the 5 most important concrete changes, each naming the slide number and the exact words or visual to change.
Be blunt and specific."""


def run_claude(prompt, model, cwd, log):
    """Command. Runs a fresh non-interactive claude session and tees its answer to log. Returns the answer."""
    out = subprocess.run(["claude", "-p", "--model", model, "--allowedTools", "Read",
                          "--dangerously-skip-permissions", prompt],
                         cwd=cwd, capture_output=True, text=True, check=True)
    log.write_text(out.stdout)
    print(out.stdout)
    return out.stdout


def render_section(section, out_dir):
    """Command. Builds SECTION alone into out_dir/section.pptx and renders slide PNGs. Returns (slides, pngs)."""
    pptx = out_dir / "section.pptx"
    subprocess.run(["python3", str(AGENTS / "build" / "build_v2.py"), "--out", str(pptx), "--only", section], check=True)
    subprocess.run(["deckcraft-cli", "render", str(pptx), "--all", "--scale", str(RENDER_SCALE), str(out_dir / "slides")], check=True)
    slides = json.loads((AGENTS / "specs" / (section + ".json")).read_text())["slides"]
    pngs = sorted((out_dir / "slides").glob("*.png"))
    assert len(pngs) == len(slides), "rendered %d slides but spec has %d" % (len(pngs), len(slides))
    return slides, pngs


def main(section, run="r1"):
    """Command. Runs listener then examiner for one section; writes their answers under .scratchpad/study."""
    out_dir = STUDY / section / run
    out_dir.mkdir(parents=True, exist_ok=True)
    slides, pngs = render_section(section, out_dir)
    exam = json.loads((AGENTS / "research" / ("exam_" + section + ".json")).read_text())
    transcript = talk_transcript(slides, [str(p) for p in pngs], slide_video_frames(slides, out_dir))
    listener = run_claude(listener_prompt(transcript, [m["q"] for m in exam["must_know"]]),
                          LISTENER_MODEL, out_dir, out_dir / "listener.md")
    run_claude(examiner_prompt(THESIS_SRC / CHAPTERS[section], transcript, exam, listener),
               EXAMINER_MODEL, out_dir, out_dir / "examiner.md")


if __name__ == "__main__":
    fire.Fire(main)
