"""
Command. Builds the talk from the JSON slide specs in agents/specs/ with DeckCraft.

frame.json gives the order; its {"insert_section": name} slides pull in specs/<name>.json,
and {"roadmap": true} repeats the frame's roadmap slide. Speech goes into the speaker notes.
Run: python build_v2.py [--out PATH] [--only SECTION]
"""
import json
import subprocess
from pathlib import Path

import fire

AGENTS = Path(__file__).resolve().parents[1]
SPECS = AGENTS / "specs"
OUT = AGENTS.parent / "ai_presentation.pptx"
CMD_FILE = AGENTS / ".scratchpad" / "build_v2_commands.txt"

FONT = "Futura"
TITLE_RECT = [40, 16, 880, 64]
TITLE_PT = 44
TEXT_PT = 28
LINE_PT = 4  # arrows and highlight boxes: thick enough to read from the back row
VIDEO_SUFFIXES = {".mp4", ".mov", ".m4v"}


def cmd(name, params):
    """
    Pure function. One DeckCraft --cmd-file line.

    Examples:
        >>> cmd('slide.new', {'layout': 'blank'})
        'slide.new={"layout": "blank"}'
    """
    return name + "=" + json.dumps(params)


def text_cmds(text, rect, size, color):
    """Pure function. Commands for a centered Futura text box. Example: text_cmds('Hi', [0,0,9,9], 28, '#000000')[0] -> 'insert.textBox={...}'"""
    return [cmd("insert.textBox", {"rect": rect, "text": text}),
            cmd("format.fontDialog", {"family": FONT, "size": size, "color": color}),
            cmd("format.align", {"align": "center"}),
            cmd("format.anchor", {"anchor": "middle"})]


def element_cmds(e):
    """
    Pure function. DeckCraft commands for one spec element (image, video, text, arrow, box).

    Examples:
        >>> element_cmds({"kind": "box", "rect": [1, 2, 3, 4], "color": "#C00000"})[1]
        'shape.fill={"none": true}'
    """
    kind = e["kind"]
    if kind == "image":
        return [cmd("insert.picture", {"path": e["path"], "rect": e["rect"]})]
    if kind == "video":
        return [cmd("insert.video", {"path": e["path"], "rect": e["rect"]}),
                cmd("media.options", {"autoplay": True, "loop": True})]
    if kind == "text":
        return text_cmds(e["text"], e["rect"], e.get("size", TEXT_PT), e.get("color", "#000000"))
    if kind == "arrow":
        return [cmd("shape.freeform", {"points": [e["from"], e["to"]]}),
                cmd("shape.line", {"color": e.get("color", "#C00000"), "width": LINE_PT, "tail": "triangle", "tailSize": "lg"})]
    if kind == "box":
        return [cmd("shape.insert", {"preset": "rect", "rect": e["rect"]}),
                cmd("shape.fill", {"none": True}),
                cmd("shape.line", {"color": e.get("color", "#C00000"), "width": LINE_PT})]
    raise ValueError("unknown element kind: " + kind)


def slide_cmds(s):
    """Pure function. All commands for one spec slide (title, elements, speaker notes)."""
    out = [cmd("slide.new", {"layout": "blank"})]
    if s.get("title"):
        out += text_cmds(s["title"], TITLE_RECT, TITLE_PT, "#000000")
    for e in s.get("elements", []):
        out += element_cmds(e)
    if s.get("speech"):
        out.append(cmd("slide.notes", {"text": s["speech"]}))
    return out


def load(name):
    """Query. Slides of specs/<name>.json."""
    return json.loads((SPECS / (name + ".json")).read_text())["slides"]


def talk_slides(only=None):
    """Query. The talk's slides in order, with sections spliced into the frame. only: one section alone."""
    if only:
        return load(only)
    frame = load("frame")
    roadmap = next(s for s in frame if s.get("is_roadmap"))
    out = []
    for s in frame:
        if "insert_section" in s:
            out += load(s["insert_section"])
        elif s.get("roadmap"):
            out.append(roadmap)
        else:
            out.append(s)
    return out


def check_paths(slides):
    """Query. Raises if any image/video path in slides is missing."""
    missing = [e["path"] for s in slides for e in s.get("elements", []) if "path" in e and not Path(e["path"]).exists()]
    if missing:
        raise FileNotFoundError("missing media:\n" + "\n".join(missing))


def main(out=str(OUT), only=None):
    """Command. Writes the command file and builds the deck at out."""
    slides = talk_slides(only)
    check_paths(slides)
    lines = [l for s in slides for l in slide_cmds(s)] + [cmd("slide.delete", {"index": 0})]
    CMD_FILE.write_text("\n".join(lines) + "\n")
    words = sum(len(s.get("speech", "").split()) for s in slides)
    print(len(slides), "slides,", words, "spoken words (~%.1f min at 135 wpm)" % (words / 135))
    subprocess.run(["deckcraft-cli", "run", "--cmd-file", str(CMD_FILE), "--save", out], check=True)
    print("saved", out)


if __name__ == "__main__":
    fire.Fire(main)
