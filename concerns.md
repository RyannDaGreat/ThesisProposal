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

## Remaining work (requires actual writing, not mechanical)

- Abstract
- Introduction chapter
- Unified literature review (section stubs exist with inputs ready)
- Future work / conclusion
- MAGICK chapter (user will provide source)
- Committee form
