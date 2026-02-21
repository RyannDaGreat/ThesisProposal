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
