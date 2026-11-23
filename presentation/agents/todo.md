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

## One-hour iteration plan (started 18:43, deadline ~19:43; user asked to be notified when the hour is up)
- [x] 18:48 section specs: peekaboo, diffillusions, magick, gwtf, motionv2v written; exams for all 5 written
- [ ] frame spec (opener / problem / roadmap / close) — agent still writing
- [ ] Round 1 (18:50-19:08): user_study.py per section (Sonnet listener sees only slides+frames+speech; Opus examiner grades vs exam, defense, bullshit, 5 fixes)
- [ ] Round 2 (19:08-19:25): send examiner fixes to section agents, revise specs, re-test
- [ ] 19:25-19:35: full build into ai_presentation.pptx, render + look at every slide, whole-talk listener for story
- [ ] 19:35-19:43: commit, open in DeckCraft, notify user

## Rations (user, 18:54)
- Talk (macOS `say`): ONE left, use only when the hour's work is finished. Earlier ones are spent.
- Notification (`rp call ntfy_send`): due at ~19:43 (timer running).

## Running in parallel (18:54)
- Revising: peekaboo, magick, motionv2v, diffillusions, frame agents (deadline ~19:05-19:08)
- Done revising: gwtf (621 words) -> study r2 running
- Studies: diffillusions r1 rerun (first run hit build race), gwtf r2
- Whole-talk story listener (Sonnet) -> full_r1/story_listener.md
- Visual QA of all 47 slides at full scale -> full_r1/visual_qa.md
- Fixed: build_v2.py command file is now per-output (parallel builds clobbered each other)
