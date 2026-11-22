# Concerns and history (append-only)

## 2026-11-22
- 18:14 Root `scrapnotes.txt` is 12 bytes of zlib data, not notes. The real notes are `presentation/scrapnotes.txt` (3.1 KB), which Ryan pointed to at 18:21.
- 18:16 Ryan named the target "AIPresentation.pptx". The file on disk is `presentation/ai_presentation.pptx` (0 bytes, empty). Using the file on disk.
- 18:20 Scope narrowed to `presentation/agents/` + `ai_presentation.pptx`. Before that, an earlier session had created root-level `AGENTS.md`, `.mcp.json`, `agents/` and a `.gitignore` line. Those are left untouched pending Ryan's call.
- Ref decks are 17 MB to 4.9 GB (embedded video). Read them with python-pptx (XML only); render with DeckCraft one slide at a time.
- Risk: DeckCraft is alpha. Validate every saved .pptx and render-check it before Ryan opens it in PowerPoint.
- Risk: talk is tomorrow; the user wants a 50-slide first draft and will review in timed rounds.

## 2026-11-22 18:41 — Draft v1 rejected: figures slapped on, papers not explained
- What happened: build_v1.py placed one thesis figure per slide with a one-line caption. 37 slides. I never worked out what each figure shows or how Ryan would explain the method.
- User verdict: "generic garbage", "beyond lazy", can't present it; no slide explains how any paper works or how they connect; dense LaTeX paper figures do not help.
- Root cause: started from the figure inventory, not from the explanation. Picked figures by filename. Paper figures are built for reading on a page, not for presenting.
- Lesson: write the talk track for each paper FIRST (what the audience must understand, step by step). Then design build sequences that show each step, with crops of single figure panels, result videos, and elements from Ryan's own talk slides. Look at every visual before using it. One idea per slide, and many slides are builds of the same image.
