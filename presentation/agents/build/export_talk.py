"""
Command. Writes the whole talk (frame with sections spliced in, same order as build_v2.py) to one JSON file.

Other renderers (the PowerRP web version) read this so specs/*.json stay the single source.
Run: python export_talk.py OUT_JSON
"""
import json
from pathlib import Path

import fire

from build_v2 import check_paths, talk_slides


def main(out):
    """Command. Writes {"slides": [...]} to out, after checking every media path exists."""
    slides = talk_slides()
    check_paths(slides)
    Path(out).write_text(json.dumps({"slides": slides}, indent=1))
    print(len(slides), "slides ->", out)


if __name__ == "__main__":
    fire.Fire(main)
