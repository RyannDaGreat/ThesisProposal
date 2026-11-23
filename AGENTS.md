# Thesis Proposal

Read before planning or changing files: `claude_instructions.md` (the manifest), `concerns.md`, and `agents/` (todo.md and anything else there).

## Presentation (`presentation/ThesisProposal.pptx`)

The user views the deck in Microsoft PowerPoint. Agents edit and look at it exclusively in DeckCraft.

- `presentation/ThesisProposal.pptx` and `presentation/ref_pptx/` are git-ignored, so git can't undo a bad edit. Before each editing session, copy the deck to `agents/.scratchpad/backups/ThesisProposal_<timestamp>.pptx`.
- `presentation/ref_pptx/` holds the user's past decks: read-only references for style and reusable figures.
- Tools: the DeckCraft app (`/Applications/DeckCraft.app`) and `deckcraft-cli` (on PATH, in `~/.local/bin`).
- Live editing (preferred): `open -n /Applications/DeckCraft.app --args --control 7979 "$PWD/presentation/ThesisProposal.pptx"`. The `deckcraft` MCP server in `.mcp.json` drives that window; without MCP, use `deckcraft-cli app COMMAND '{json}'` and `deckcraft-cli app --method ui.screenshot '{"path":"/abs/shot.png"}'`.
- Look at slides: `deckcraft-cli render presentation/ThesisProposal.pptx --all agents/.scratchpad/renders`.
- `deckcraft-cli commands` lists command ids and `deckcraft-cli describe COMMAND` explains one. The slide is 960×540 points, y down.
- After saving, run `python ~/.agents/external/anthropic/pptx/scripts/office/validate.py presentation/ThesisProposal.pptx` so it opens cleanly in PowerPoint.
- Don't save while the user has the deck open in PowerPoint. Ask them to close it first, or PowerPoint will overwrite the edits.
