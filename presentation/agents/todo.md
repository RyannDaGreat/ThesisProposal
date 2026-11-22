# REVIEW CHECKLIST

No fork agents run. All work is done in the main session or by research subagents.

| # | Item | Product LOC | Status |
|---|---|---|---|
| 1 | Agent workspace: transcript, manifest, concerns | 0 (docs) | `13e47fa`, not pushed |
| 2 | Research reports: thesis story, style, decks | 0 (docs) | `7651eaf`, not pushed |
| 3 | Proposal v1 (50 slides) | 0 (docs) | `fcd0c24`, `4ab08d8`, not pushed. Replaced by item 5 after user feedback |
| 4 | Videos from ref decks + other-papers research | 0 (docs) | in `5997239`. Assets in .scratchpad (git-ignored) |
| 5 | Draft v1 deck: 37 slides from thesis figures | +262 (build_v1.py) | `5997239`, not pushed. ai_presentation.pptx is 140 MB, git-ignored. Not checked in PowerPoint. Known bugs: label/red-line overlap on roadmap slide 19 and on the other-papers slide 35. NOT ASKED: 2nd talk sent, and sent before the chat reply |
| 6 | Root-level ThesisProposal AGENTS.md, .mcp.json, agents/, .gitignore line | 0 | Waiting on user: keep, move, or delete? |

# TODO

- [x] Transcript, manifest, concerns in presentation/agents/
- [x] Research swarm: thesis story, style A/B, remaining decks (research/)
- [x] Presentation proposal → proposal.md
- [x] Notify sent (used up); talk sent twice
- [ ] Wait for answers to the 6 questions in proposal.md
- [x] Draft v1 built (37 slides)
- [ ] Fix v1 overlaps; review v1 with user; build draft in ai_presentation.pptx with DeckCraft (section agents + reviewer + assembler)
- [ ] Ask: earlier root-level AGENTS.md, .mcp.json, agents/, .gitignore line (made before the scope change) — keep, move here, or delete?
