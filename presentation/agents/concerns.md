# Concerns and history (append-only)

## 2026-11-22
- 18:14 Root `scrapnotes.txt` is 12 bytes of zlib data, not notes. The real notes are `presentation/scrapnotes.txt` (3.1 KB), which Ryan pointed to at 18:21.
- 18:16 Ryan named the target "AIPresentation.pptx". The file on disk is `presentation/ai_presentation.pptx` (0 bytes, empty). Using the file on disk.
- 18:20 Scope narrowed to `presentation/agents/` + `ai_presentation.pptx`. Before that, an earlier session had created root-level `AGENTS.md`, `.mcp.json`, `agents/` and a `.gitignore` line. Those are left untouched pending Ryan's call.
- Ref decks are 17 MB to 4.9 GB (embedded video). Read them with python-pptx (XML only); render with DeckCraft one slide at a time.
- Risk: DeckCraft is alpha. Validate every saved .pptx and render-check it before Ryan opens it in PowerPoint.
- Risk: talk is tomorrow; the user wants a 50-slide first draft and will review in timed rounds.
