# Concerns - Thesis Proposal

## 2026-02-20: Initial exploration complete

- Explored entire directory structure
- `source/` directory exists but is empty — ready for writing
- `kanchana_example/` contains a full Stony Brook PhD thesis proposal from Kanchana Ranasinghe (June 2025) — excellent template
- `kanchana_example/report_prev/` contains 6 additional thesis proposal PDFs from other students
- `papers/` contains 8 PDFs and 8 source tarballs for Ryan's publications
- `impact.md` contains detailed citation impact analysis for 6 of Ryan's first-author papers
- Ryan has ~9 papers; Kanchana had 5. Need to decide which papers form core chapters vs. supporting mentions.
- Key decision needed: What is the unifying thesis narrative? Ryan's work spans video generation, diffusion illusions, segmentation, datasets, sim2real. The thread seems to be "diffusion models for visual creation and understanding."
- The committee form template exists in kanchana_example but will need Ryan's info filled in.

## 2026-02-20: Kanchana diffing complete

- Downloaded 4 original arxiv sources (LSS, LocVLM, MVU, LTM) to `.frenzy/kanchana_originals/`
- Diffed all 4 originals against thesis-adapted versions using parallel agents
- Derived 8-category adaptation recipe (structural, sections, labels, paths, macros, captions, spacing, minor)

## 2026-02-20: Paper extraction and adaptation complete

- Extracted all 4 available paper sources (Peekaboo, DiffIllusions, GWTF, MotionV2V) into `source/src/`
- MAGICK has no source tarball in papers/ — user confirmed to skip and add manually later
- Peekaboo had flat `figures__X__Y` naming → reorganized into proper `figures/X/Y` dirs
- Created thesis skeleton: main.tex, preamble.tex, title page, abstract placeholder, publications, intro placeholder, lit review placeholder, MAGICK placeholder, future work placeholder
- Adapted all 4 papers in parallel using 5 agents (skeleton + 4 paper agents)

## 2026-02-20: Compilation fixes and verification

- Initial compile: 148 pages, multiple errors
  - Fix 1: Peekaboo had `\begin{figure}` commented out but `\end{figure}` active → uncommented
  - Fix 2: `subfig` package conflicts with `subcaption` → replaced with `subcaption`
  - Fix 3: `figure*`/`table*` → `figure`/`table` (single-column report class)
  - Fix 4: Undefined `\bb` macro in Peekaboo → added `\newcommand{\bb}{\mathbf{b}}`
- After fixes: 169 pages, 0 errors
- bibtex ran with 17 duplicate entry warnings (expected when combining 4 .bib files)
- Three pdflatex passes → all cross-references resolved
- Final: 169 pages, 0 errors, compiles clean

## 2026-02-20: MAGICK chapter adapted

- Source found at `/Users/ryan/CleanCode/Projects/Adobe2023/MAGICK_Paper` (not in papers/ tarballs)
- Created 6 thesis-adapted files: 1_intro, 2_relatedwork, 3_method, 4_results, 5_conclusion, 6_appendix
- All labels prefixed `magick_`, all figure paths rebased to `src/3_MAGICK/`
- Related work extracted: "Alpha Matting and Synthetic Dataset Generation"
- Fixed 2 unescaped `&` in main.bib (Taylor & Francis, Asilomar conference)
- Appendix demoted: sections → subsections, wrapped in "Additional Details"
- Compilation: 211 pages, 0 errors

## 2026-02-20: Thesis theme and ordering decided

- Theme: "Controlling Diffusion Models" / "How to make diffusion models do what you want" (working title, variable)
- Chronological chapter order: Diffusion Illusions → Peekaboo → MAGICK → GWTF → MotionV2V
- MotionV2V may be removed (Ryan undecided)
- Related works need deduplication and a unified summary — plan needed

## 2026-02-20: Literature review written

- Launched 5 Opus frenzy agents with diversified angles:
  1. "Control as a spectrum" (implicit to explicit)
  2. "Problem-driven" (concrete problems)
  3. "Technical mechanisms" (score distillation, noise shaping, conditioning)
  4. "Applications-first" (what users want to do)
  5. "Minimalist Kanchana-clone" (exact 3-paragraph mirror)
- All 5 wrote to `.frenzy/litreview/agent{1-5}.tex`
- Judged all 5 against Kanchana's original `2_literature.tex`:
  - Agent 5 (Kanchana clone) won at 8.5/10 — closest structural match
  - Agent 4 (Applications-first) was runner-up at 7/10 — best original phrasing
  - Agent 3 (Technical mechanisms) scored lowest — had math equations, wrong style
- Final version: blend of Agent 5's structure with Agent 4's phrasing, avoiding Agent 5's too-close opening sentence mimicry
- Fixed pre-existing bug: `\modelname` undefined in Peekaboo related_work_thesis.tex (replaced with literal "Peekaboo")
- Compilation: 230 pages, 0 LaTeX errors, 41 bibtex warnings (pre-existing duplicates)
- AI writing detector: web-based tools all require JavaScript/accounts, couldn't automate. User should manually verify at gptzero.me or quillbot.com/ai-content-detector

## 2026-02-20: Literature review revision — match Kanchana's style exactly

**Key findings from deep comparison with Kanchana's thesis:**
1. Kanchana's synthesis paragraphs have ZERO citations — pure conceptual narrative. Ours had ~25 `\cite{}` commands. Must rewrite citation-free.
2. Kanchana kept per-paper related works essentially VERBATIM from originals (only cosmetic label/macro changes). We over-trimmed ours (avg 249 words vs his 446). Must restore.
3. Kanchana's synthesis implicitly describes each paper's problem space in P1-P2 without naming papers, then P3 explicitly lists contributions.

**Plan:**
- Rewrite 3 synthesis paragraphs: zero citations, flowing narrative, ~400 words
- Restore all 4 trimmed per-paper sections to near-original content with cosmetic-only changes
- Target total: ~2,100-2,500 words (Kanchana: 2,177)

## 2026-02-20: Literature review revision completed — Kanchana style match

- Rewrote 3 synthesis paragraphs with ZERO citations (Kanchana-exact style)
- Restored 4 per-paper related work sections to near-original paper content:
  - MAGICK: 268 → 550 words
  - GWTF: 187 → 521 words
  - MotionV2V: 208 → 337 words
  - DiffIllusions: 240 → 352 words
  - Peekaboo: 294 words (kept as-is)
- Total lit review: 2,470 words (Kanchana: 2,177) — within range
- Verified zero `\cite{}` in synthesis paragraphs
- Full compile cycle: 228 pages, 0 LaTeX errors
- All per-paper sections use `\textbf{}` headers (matching Kanchana's format)

## 2026-02-21: Abstract and Introduction written

- Abstract: 281 words (Kanchana: 372). Intentionally shorter — Ryan said adding is easier than removing.
- Introduction: 1,031 words (Kanchana: 1,109). Structure matches Kanchana's: Overview section with motivation + per-paper contributions + impact paragraph, then Organization section with per-chapter paragraph descriptions.
- Impact data verified via 4 parallel research agents with online searches + impact.md
- Key verified numbers: Peekaboo 41 citations, DiffIllusions 21 citations + CVPR 2023 Demo Award + YouTube coverage, MAGICK 14 citations + 3,342 HF downloads/month, GWTF 62 citations + 1,100 GH stars + CVPR 2025 Oral (top 0.73%), MotionV2V 54 GH stars in 3 months
- Compilation: 231 pages, 0 LaTeX errors

## Remaining work (requires actual writing, not mechanical)

- Future work / conclusion
- Reorder chapters in main.tex to match chronological order
- Committee form
- Decide on MotionV2V inclusion

## 2026-06-19: MotionV2V inclusion RESOLVED — stays as full Ch7

- Long-open question (flagged "Ryan undecided / may be removed" since the early sessions) is now DECIDED: MotionV2V remains a full contribution chapter (Ch7).
- Rationale: the original reason to maybe-cut it ("unproven arXiv preprint") no longer holds. The 10-agent impact frenzy confirmed it is accepted to CVPR 2026 (CVF proceedings pp. 35988-35997) and already has ~10 citations at ~7 months post-release.
- No LaTeX change required (it was already Ch7). Cleared the "may be removed" flags in claude_instructions.md (3 places).
- Also corrected a long-standing manifest error while here: the chapter order note said "DiffIllusions → Peekaboo" but the true chronological (arXiv-v1) order is Peekaboo (Nov 2022) → DiffIllusions (Dec 2023). main.tex was already correct; only the note was wrong.

## 2026-08-03 — MAGICK impact fact-check (Ryan's in-text TODO), fresh frenzy of 10 agents
- Trigger: Ryan's commit d4f1af3 added `[TODO: Fact Check these claims. Do these papers actually use my dataset? ]` in the BODY TEXT of the MAGICK section of src/8_future_work.tex (it was printing into the PDF). Now moved into a %-comment with the verdict appended.
- Method: fresh frenzy (agents given no prior conclusions from the June impact frenzy). Reports: .frenzy/magick_factcheck/A1-A10.
- VERDICT: all three papers cited in the draft materially USE the dataset (verbatim quotes on file):
  Trans-Adapter (ICCV'25, trains on 90% MAGICK subset + "w/o MAGICK" ablation), TKG-DM (CVPR'25
  Highlight, 3,000-image MAGICK eval benchmark), PrismLayers (MSRA, trains transparency VAE
  decoder on MAGICK). Also PSDiffusion (WACV'26) and LayeringDiff (arXiv'25). LayerBench = 25%
  MAGICK (200/800, largest single source). "Largest public general-domain RGBA dataset, none
  bigger since" HOLDS through Aug 2026.
- CORRECTIONS vs June frenzy (impact_verified.md sec 3):
  1. The portrait-matte paper (Lu et al., Pattern Recognition 2026) replicates MAGICK's chroma-key
     METHOD as a baseline but never uses the data → material users = 5, not 6.
  2. HF downloads dropped 6,448 → 3,773/month. "Thousands a month" still true but barely plural;
     "over 150K all-time downloads" (158,640) is sturdier.
  3. LayeringDiff is arXiv-only (author's homepage confirms), despite one agent labeling it AAAI 2025.
- Bib repairs while verifying (bibtex error count 45 → 33; remaining 33 are benign cross-file
  duplicate keys from merging five papers' bibs):
  1. Stub authors "and others" filled with real lists: dai2025transadapter, tkgdm2025,
     prismlayers2025 (3_MAGICK), wonderplay2025, cameranoise2026, liu2025equivdm (4_GWTF).
  2. cameranoise2026 had a WRONG TITLE (real: "CameraNoise: Enabling Faithful Camera Control in
     Video Diffusion through Geometry-Flow-Guided Noise Warping", arXiv 2605.30774).
  3. EquiVDM was RETITLED on arXiv v2+ to "On Equivariance and Fast Sampling in Video Diffusion
     Models Trained with Warped Noise" — kept v1 title (prose says "EquiVDM"), flagged for Ryan.
  4. zhou2017scene in 2_DiffIllusions had corrupted author "olei Zhou, ..." (commas, truncated) — fixed.
  5. deepfloyd in 3_MAGICK had no author/year (bibtex warnings) — filled to match GWTF's entry.
- Lesson: bib stubs created during the June impact drafting ("and others") were never backfilled;
  when adding placeholder citations, log them in the TODO immediately so they don't reach a build.

## 2026-08-03 — Two frenzies: MAGICK largest-claim re-verify (10 Haiku, adversarial) + GWTF notes research (8 Sonnet)
- MAGICK "no bigger public general-domain RGBA dataset since" — FINAL: HOLDS, zero surviving
  counterexamples from 10 refutation-hunters. Two false refutations overturned by Claude's own
  audits: (1) PrismLayers "200K" = fragmented stylized repos (Plus 80.8K + MultiRes 91.4K
  resolution-variants + Pro 20K; anime/Pokemon/doodle styles; multi-layer comps ≠ individual
  RGBA images; no 200K repo exists); (2) nyuuzyou/openclipart "178K" ships NO images (metadata
  + SVG text + URLs only). Lesson: Haiku agents report paper/abstract claims as releases —
  always audit the actual repos before accepting a refutation or confirmation.
- Qualifiers are load-bearing: "public" + "general-domain" + "individual captioned RGBA
  images"; count phrased "over 140,000" (GitHub) not 150K (paper) to be bulletproof.
- GWTF research (Ryan's new bracketed notes in tex): 6 rendering-backbone papers pass the
  strict would-not-exist test (WonderPlay ICCV'25 HL, NewtonGen ICLR'26, VideoFrom3D SIGGRAPH
  Asia'25, VLIPP, PSIVG, FOFPred) + RealWonder technique-transfer. EquiVDM v1 said
  "concurrent", v2 recanted post-CVPR-acceptance. InfRes (ICLR'25, Burgert co-author, arXiv
  Nov'24) = concurrent sibling; GWTF calls it "the concurrent InfRes". Variants: CameraNoise/
  UniCam, HumANDiff, UniCaMo, Phi-Noise, IF-V2V. Cites 117 S2 / 120 GS. Virtually Being
  fine-tunes GWTF checkpoint but is own-group (Burgert co-author) - excluded from external
  adoption. Ecosystem: 1,090 stars flat; both official HF demo Spaces broken (action item).
- Full reports: .frenzy/magick_biggest_check/C1-C10, .frenzy/gwtf_impact2/D1-D8. Answers
  annotated as %-comments in src/8_future_work.tex (MAGICK + GWTF sections).

## 2026-08-03 — Findings folded into tex + manifest ("Modify the tex files accordingly")
- GWTF \AI{} prose now names the 6 rendering-backbone papers + RealWonder, the 3D-structure
  warped-noise variants (CameraNoise/HumANDiff/UniCaMo), InfRes as concurrent sibling, and
  115+ citations. Ryan's 4 bracketed questions were PRINTING in the PDF - converted to
  %-comments with answers adjacent.
- 9 new bib entries in 4_GWTF/main.bib (authors pulled from arXiv API same-day). bibtex
  error count unchanged (33 pre-existing duplicates) -> new entries parse clean.
- MAGICK section: Ryan had rewritten it in his voice meanwhile. Two interventions, flagged
  to him: (1) "presented and published at CVPR 2025" corrected to CVPR 2024 (proof:
  manifest Core Papers table + PSDiffusion's citation "CVPR 2024, pp. 22595-22604");
  (2) his commented-out "No bigger one has come out since" line restored as \AI{} with
  committee-proof qualifiers + "150,000 total downloads" phrasing, per his instruction
  "if it's true... we absolutely should claim it" (his commented line left untouched).
- Manifest: new section "Verified Impact Findings (2026-08-03) — with proof" + change log.
- MISTAKE LOG: two Edit calls failed because the MAGICK section changed on disk mid-session
  (Ryan's rewrite). Lesson: in an actively-co-edited file, re-read the target section
  immediately before every Edit, not just at session start.

## 2026-08-08 — MotionV2V developments check (5 Sonnet agents + batch-4 citer swarm)
- Ryan asked: any new developments, and are citers substantially based on it or citing for
  completeness? ANSWER: completeness — 0 of 11 citers build on it (all 11 full texts read).
- MISTAKE FOUND & LOGGED: June frenzy's "TrajectoryMover = verified end-to-end citer" was a
  conflation of two Burgert 2025 papers (its real baseline is GWTF 2025b; MotionV2V 2025a is
  a "concurrent work" related-work mention). Lesson: when an author has multiple same-year
  papers, always resolve 2025a/2025b keys before crediting a citation.
- Positives: "first V2V general-object motion editor" claim re-verified against ~40
  candidates and HOLDS; motion-editing subfield forming with MotionV2V + Lee et al.
  (2512.02015, 6 days later, calls us "concurrent work") as twin founding references.
- Negatives: no code released (58 stars flat; Motion4Motion cites the missing code as why
  it's absent from their baseline table; HF's Niels Rogge request unanswered since Dec 2025);
  CVPR 2026 standard poster, no award.
- Actions: MotionV2V \AI{} rewritten (subfield framing, honest citation
  characterization); FACT-CHECK comment block added; 2 verified bib entries
  (lee2026pointtracks, trajectorymover2026) appended to 5_MotionV2V/main.bib (bibtex error
  count unchanged = parse clean); manifest MotionV2V findings subsection added.
