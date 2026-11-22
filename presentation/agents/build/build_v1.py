"""
Command. Builds draft v1 of the thesis proposal talk with DeckCraft.

Reads thesis figures from source/src and videos pulled from ref_pptx into
agents/.scratchpad/assets/videos, writes presentation/ai_presentation.pptx.
Run: python build_v1.py
"""
import json
import subprocess
from pathlib import Path

import fire
from PIL import Image

AGENTS = Path(__file__).resolve().parents[1]
PRESENTATION = AGENTS.parent
SRC = PRESENTATION.parent / "source" / "src"
VIDEOS = AGENTS / ".scratchpad" / "assets" / "videos"
OTHER_PAPERS = AGENTS / ".scratchpad" / "assets" / "other_papers"
FIG_CACHE = AGENTS / ".scratchpad" / "assets" / "figs"
OUT = PRESENTATION / "ai_presentation.pptx"

SLIDE_W, SLIDE_H = 960, 540
FONT = "Futura"
TITLE_PT = 44
CAPTION_PT = 26
STATEMENT_PT = 54
RED = "#C00000"
PDF_DPI = 200
MARGIN = 40
TITLE_BOX = [MARGIN, 16, SLIDE_W - 2 * MARGIN, 64]
CAPTION_BOX = [MARGIN, 468, SLIDE_W - 2 * MARGIN, 56]
MEDIA_BOX = [MARGIN, 86, SLIDE_W - 2 * MARGIN, 376]
VIDEO_SUFFIXES = {".mp4", ".mov", ".m4v"}
MAX_SIDE_PX = 3840  # 4K: sharp on any projector, small enough for DeckCraft to decode


def fit_rect(media_w, media_h, box):
    """
    Pure function. Largest rect with the media's aspect ratio, centered in box.

    Args:
        media_w, media_h (float): media size in any unit
        box (list): [x, y, w, h] in slide points

    Returns:
        list: [x, y, w, h]

    Examples:
        >>> fit_rect(1920, 1080, [0, 0, 960, 540])
        [0.0, 0.0, 960.0, 540.0]
        >>> fit_rect(100, 100, [0, 0, 960, 540])
        [210.0, 0.0, 540.0, 540.0]
    """
    x, y, w, h = box
    scale = min(w / media_w, h / media_h)
    fw, fh = media_w * scale, media_h * scale
    return [x + (w - fw) / 2, y + (h - fh) / 2, fw, fh]


def split_row(box, n, gap):
    """
    Pure function. Splits box into n equal side-by-side cells.

    Examples:
        >>> split_row([0, 0, 100, 50], 2, 10)
        [[0.0, 0, 45.0, 50], [55.0, 0, 45.0, 50]]
    """
    x, y, w, h = box
    cell_w = (w - gap * (n - 1)) / n
    return [[x + i * (cell_w + gap), y, cell_w, h] for i in range(n)]


def raster(path):
    """Command. Returns a PNG/JPG path for path, rendering page 1 of a PDF into FIG_CACHE."""
    path = SRC / path
    if path.suffix.lower() != ".pdf":
        return shrunk(path)
    FIG_CACHE.mkdir(parents=True, exist_ok=True)
    stem = FIG_CACHE / path.parent.parent.name / path.stem
    stem.parent.mkdir(parents=True, exist_ok=True)
    png = Path(str(stem) + ".png")
    if not png.exists():
        subprocess.run(["pdftoppm", "-png", "-r", str(PDF_DPI), "-singlefile", str(path), str(stem)], check=True)
    return png


def shrunk(path):
    """Command. Returns path, or a copy in FIG_CACHE downscaled so its long side is MAX_SIDE_PX."""
    Image.MAX_IMAGE_PIXELS = None  # our own thesis figures, not untrusted input
    with Image.open(path) as im:
        if max(im.size) <= MAX_SIDE_PX:
            return path
        small = FIG_CACHE / "shrunk" / path.name
        if not small.exists():
            small.parent.mkdir(parents=True, exist_ok=True)
            im.thumbnail((MAX_SIDE_PX, MAX_SIDE_PX))
            im.convert("RGB").save(small, quality=90)
        return small


def media_size(path):
    """Query. Pixel size of an image or video."""
    if path.suffix.lower() in VIDEO_SUFFIXES:
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                              "-of", "json", str(path)], capture_output=True, text=True, check=True)
        stream = json.loads(out.stdout)["streams"][0]
        return stream["width"], stream["height"]
    with Image.open(path) as im:
        return im.size


def cmd(name, params=None):
    """Pure function. One --cmd-file line. Example: cmd('slide.new', {'layout': 'blank'}) -> 'slide.new={"layout": "blank"}'"""
    return name if params is None else name + "=" + json.dumps(params)


def text_box(rect, text, size, color="#000000", align="center"):
    """Pure function. Commands for a Futura text box."""
    return [
        cmd("insert.textBox", {"rect": rect, "text": text}),
        cmd("format.fontDialog", {"family": FONT, "size": size, "color": color}),
        cmd("format.align", {"align": align}),
        cmd("format.anchor", {"anchor": "middle"}),
    ]


def media(path, box):
    """Command (may render a PDF). Commands that place one image or video fitted in box."""
    pulled = [d / path for d in (VIDEOS, OTHER_PAPERS) if (d / path).exists()]
    path = pulled[0] if pulled else raster(path)
    rect = fit_rect(*media_size(path), box)
    if path.suffix.lower() in VIDEO_SUFFIXES:
        return [cmd("insert.video", {"path": str(path), "rect": rect}),
                cmd("media.options", {"autoplay": True, "loop": True})]
    return [cmd("insert.picture", {"path": str(path), "rect": rect})]


def slide(title=None, items=(), caption=None, red=None, note=None, statement=None, labels=None):
    """
    Command (may render PDFs). Commands for one slide.

    items: media paths laid out in a row inside MEDIA_BOX (or the full area if no title/caption).
    labels: one short label under each item. red: a red key-idea line above the caption.
    """
    out = [cmd("slide.new", {"layout": "blank"})]
    top = TITLE_BOX[1] + TITLE_BOX[3] if title else MARGIN / 2
    red_y = CAPTION_BOX[1] - (CAPTION_BOX[3] if caption else 0)
    bottom = (red_y if red else CAPTION_BOX[1] if caption else SLIDE_H - MARGIN / 2) - (36 if labels else 0)
    box = [MARGIN, top, SLIDE_W - 2 * MARGIN, bottom - top]
    if title:
        out += text_box(TITLE_BOX, title, TITLE_PT)
    if statement:
        out += text_box([MARGIN * 2, 180, SLIDE_W - 4 * MARGIN, 180], statement, STATEMENT_PT)
    for i, cell in enumerate(split_row(box, len(items), 16) if items else []):
        out += media(items[i], cell)
        if labels:
            out += text_box([cell[0], bottom, cell[2], 36], labels[i], 22)
    if red:
        out += text_box([CAPTION_BOX[0], red_y, CAPTION_BOX[2], CAPTION_BOX[3]], red, CAPTION_PT, RED)
    if caption:
        out += text_box(CAPTION_BOX, caption, CAPTION_PT)
    if note:
        out.append(cmd("slide.notes", {"text": note}))
    return out


P, D, M, G, V = "1_Peekaboo/figures/", "2_DiffIllusions/figs/", "3_MAGICK/figs/", "4_GWTF/fig/", "5_MotionV2V/"
ROADMAP = [P + "peekaboo_grid.pdf", D + "FlipGallery.pdf", M + "fig1.jpg", G + "Teaser.pdf", V + "teaserv2.png"]
ROADMAP_LABELS = ["Where", "Views", "Transparency", "Motion", "Edit motion"]


def roadmap(highlight):
    """Command. Roadmap slide; highlight is the 0-based chapter now starting."""
    labels = [("▶ " + l) if i == highlight else l for i, l in enumerate(ROADMAP_LABELS)]
    return slide("Five handles", ROADMAP, labels=labels,
                 red="Next: " + ROADMAP_LABELS[highlight].lower(),
                 note="Roadmap. Each paper finds one more handle inside a frozen model.")


def deck():
    """Command. All slide commands for v1, in order."""
    s = []
    # Cold open: three results, no explanation.
    s += slide(items=["gwtf_rickroll_warped_noise.mp4"], note="No explanation yet. Just let it play.")
    s += slide(items=["diffilu_hook1.mov"], note="Flip illusion. Still no explanation.")
    s += slide(items=[M + "fig1.jpg"], caption="By the end of this talk you'll know how all three of these work.")
    s += slide(statement="How to Control Your Diffusion Model",
               caption="Ryan Burgert · Thesis Proposal · Stony Brook University",
               note="Advisor: Michael Ryoo.")
    # The problem.
    s += slide(statement="A few words in. A million pixels out.",
               note="Text is a tiny input for a huge output.")
    s += slide(statement="So who decides everything you didn't say?", red="The model does. With what IT wants.",
               note="Thesis claim: the prior reflects what the model wants to generate, not what the artist intended.")
    s += roadmap(0)
    # Peekaboo.
    s += slide("Peekaboo", [P + "intro1.png"], caption="A text-to-image model can segment, with zero segmentation training.")
    s += slide("How?", [P + "Newdia.pdf"], red="Learn an alpha mask that the diffusion model agrees with.",
               note="Score distillation: composite the masked image on random backgrounds and ask the model if it still matches the text.")
    s += slide("Peekaboo", [P + "peekaboo_grid.pdf"], caption="Referring segmentation from a model that never saw a mask.")
    s += slide(statement="Same loss. What if we optimize several images at once?")
    # Diffusion Illusions.
    s += roadmap(1)
    s += slide("Diffusion Illusions", [D + "FlipGallery.pdf"], caption="Flip it over and it's a different picture.")
    s += slide("Diffusion Illusions", [D + "hiddenGal.pdf"], caption="Stack four prints and a fifth image appears.")
    s += slide("But...how?", [D + "architecture.v3.drawio.pdf"],
               red="Every arrangement must look right to the model at the same time.")
    s += slide("It works on paper", [D + "SimRealRot.jpg"], caption="Printed, cut, and held up to a light.")
    s += slide("What became of it", [D + "website_figure_compressed.jpg"],
               red="CVPR 2023 Best Demo Award. Steve Mould and Matt Parker made videos on it.",
               note="Reviewer: 'Not good, didn't like it.' Well, other people did.")
    # MAGICK.
    s += slide("Peekaboo masks are blobby", [P + "vis_lim/im1_orig.png", P + "vis_lim/im1_seg.png"],
               caption="Fine detail gets lost. Hair and fur need real alpha.")
    s += roadmap(2)
    s += slide("MAGICK", [M + "GreenOnGreenBadGreenOnBlueGood.png"], red="Ask for a green screen. Then key it out.")
    s += slide("MAGICK", [M + "PipelineOverview.png"], caption="150,000+ captioned RGBA images, made by the model itself.")
    s += slide("MAGICK", ["3_MAGICK/ddpack0_q90.jpg"])
    s += slide("What became of it", [M + "alpha2rgbResults.png"],
               red="Thousands of Hugging Face downloads every month.",
               note="~20 citations; 3.7k to 6.4k HF downloads a month depending on the month.")
    # Go-with-the-Flow.
    s += slide(statement="Then video models arrived. Text can't describe motion.")
    s += roadmap(3)
    s += slide("Go-with-the-Flow", [G + "algo_diagram_2_layers.png"], red="Warp the noise. Keep it Gaussian.",
               note="Callback to the RickRoll from slide 1: that was warped noise.")
    s += slide("Go-with-the-Flow", [G + "framework_diagram.png"], caption="Fine-tune on warped noise. No architecture changes.")
    s += slide("Go-with-the-Flow", ["gwtf_results.mp4"])
    s += slide("What became of it", [G + "comparisons_video_diffusion_object_motions_new_compressed.pdf"],
               red="CVPR 2025 Oral · 169 citations · ~1.1k GitHub stars",
               note="Built on by EquiVDM (NVIDIA), WonderPlay, HumANDiff, CameraNoise. Follow-up: Infinite-Resolution Integral Noise Warping (ICLR 2025).")
    # MotionV2V.
    s += slide(statement="Go-with-the-Flow makes new videos. What about the video you already have?")
    s += roadmap(4)
    s += slide("MotionV2V", [V + "teaserv2.png"], caption="Change how things move. Keep everything else.")
    s += slide("How?", [V + "datagen.pdf"], red="Train on motion counterfactuals: same video, different motion.")
    s += slide("MotionV2V", [V + "megacomparisonfigurev2.jpg"], caption="CVPR 2026.")
    # Other papers.
    s += slide("I also helped on", ["vista4d_teaser.png", "virtually_being.png", "go_with_the_track.png"],
               labels=["Vista4D · CVPR 2026", "Virtually Being · SIGGRAPH Asia 2025", "Go-with-the-Track · SIGGRAPH 2026"],
               red="Two of them build on Go-with-the-Flow.",
               note="Vista4D: reshoot a video along a new camera path. Virtually Being: uses GWTF for motion. Go-with-the-Track (Koichi): point tracks for compositing and motion.")
    # Next.
    s += slide(statement="Next: any edit, to any video.",
               note="Image-to-image editor turned into a video-to-video editor. 'Nano Banana, but for video.'")
    s += slide("Five handles", ROADMAP, labels=ROADMAP_LABELS, red="...and a sixth?", note="Questions.")
    return s


def main(out=str(OUT)):
    """Command. Writes the command file to agents/.scratchpad and builds the deck at out."""
    lines = deck()
    cmd_file = AGENTS / ".scratchpad" / "build_v1_commands.txt"
    cmd_file.write_text("\n".join(lines + [cmd("slide.delete", {"index": 0})]) + "\n")
    print(len(lines), "commands ->", cmd_file)
    subprocess.run(["deckcraft-cli", "run", "--cmd-file", str(cmd_file), "--save", out], check=True)
    print("saved", out)


if __name__ == "__main__":
    fire.Fire(main)
