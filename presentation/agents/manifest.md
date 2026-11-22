# Thesis Proposal Talk — Manifest

## Goal
Ryan Burgert defends his PhD thesis proposal **tomorrow (2026-11-23)**. Title: **"How to Control Your (Video) Diffusion Model"**.
Build the talk deck in `presentation/ai_presentation.pptx`, about 50 slides for the first draft. It needs a real story: the committee cares about the overall arc, and the thesis itself is "a bunch of my papers duct-taped together sandwiched between the parts that they actually care about".
Ryan views the deck in PowerPoint. Agents edit and view it only in DeckCraft (`deckcraft-cli`, the DeckCraft app on control port 7979).

## Scope (hard rule)
- Agents may touch ONLY `presentation/agents/` (treated as a dump) and `presentation/ai_presentation.pptx`.
- Everything else is read-only: `presentation/ref_pptx/*` (past decks), `presentation/ThesisProposal.pptx`, the thesis `source/`, `scrapnotes.txt`.
- Commit as we go, never push. The big .pptx files are git-ignored.

## Style requirements (from Ryan)
- Inherit Ryan's own presentation style ("I have a very particular way of doing presentations"). Never a boring or AI-generated look.
- Write in Ryan's voice. He doesn't sound like an AI. No "not this, not that" constructions.
- Concrete style findings live in `research/style_A.md` and `research/style_B.md`, and get summarized here once confirmed.

## Inputs
- `../scrapnotes.txt`: Ryan's own outline and gather list. It is the primary source for structure.
- `../../source/`: thesis LaTeX. Chapters: Diffusion Illusions, Peekaboo, MAGICK, Go-with-the-Flow, MotionV2V.
- `../ref_pptx/`: past talks to reuse slides and media from. The MAGICK deck is missing (Ryan: "where is the MAGICK one?").
- `research/*.md`: swarm reports (thesis story, style, deck inventory).

## Workflow
- Back up `ai_presentation.pptx` to `.scratchpad/backups/` before each edit session.
- Edit live in DeckCraft (MCP or `deckcraft-cli app`) or headless (`deckcraft-cli run`), render with `deckcraft-cli render`, and look at every slide.
- Validate after each save: `python ~/.agents/external/anthropic/pptx/scripts/office/validate.py ai_presentation.pptx`.
- Use desktop mouse/screenshot control only when a headless route is stuck (e.g. permission dialogs).

## Session rules (from Ryan)
- Timed session with deadlines. Plan ahead to hit them.
- Notifications (`rp call ntfy_send`) and talking (`curl -s -d 'MSG' ntfy.sh/stark_comma`) are rationed. Use them only when granted. Talking is 1-2 plain-English sentences, read aloud.
- Sonnet subagents by default, medium/high effort. Opus for truly hard parts.

## Status
- Proposal: `proposal.md` (pending review).
