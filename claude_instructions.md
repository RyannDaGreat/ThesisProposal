# Thesis Proposal - Manifest

## Goal

Write Ryan Burgert's PhD thesis proposal document. The `source/` directory is where we write new LaTeX content. Everything else in this repo is **read-only reference material**.

## Thesis Theme

**"Controlling Diffusion Models"** (working title — stored as a variable for easy changing later). The unifying narrative is: how to make diffusion models do what you want.

## Chapter Ordering (chronological)

1. Introduction (placeholder)
2. Literature Review (unified, to be written)
3. **Diffusion Illusions** (SIGGRAPH 2024, arXiv Dec 2023) — currently Ch4 in source, needs reordering
4. **Peekaboo** (arXiv Nov 2022) — currently Ch3 in source, needs reordering
5. **MAGICK** (CVPR 2024) — currently Ch5 in source
6. **Go-with-the-Flow** (CVPR 2025 Oral, arXiv Jan 2025) — currently Ch6 in source
7. **MotionV2V** (arXiv Nov 2025) — currently Ch7 in source. **May be removed — Ryan hasn't decided yet.**
8. Future Work (placeholder)

**NOTE**: The source files currently have the OLD ordering (Peekaboo=Ch3, DiffIllusions=Ch4). Reordering main.tex `\input` lines will renumber chapters automatically since we use `\chapter{}` not `\chapter[N]{}`.

## Core Papers (first-author only, chosen by Ryan)

| Ch (new) | Paper | Venue | arXiv ID | Source |
|----|-------|-------|----------|----------------|
| 3 | **Diffusion Illusions** | SIGGRAPH 2024 | 2312.03817 | `Diffusion_Illusions_2312.03817_source.tar.gz` |
| 4 | **Peekaboo** | arXiv 2022 | 2211.13224 | `Peekaboo_2211.13224_source.tar.gz` |
| 5 | **MAGICK** | CVPR 2024 | — | Source from `/Users/ryan/CleanCode/Projects/Adobe2023/MAGICK_Paper` |
| 6 | **Go-with-the-Flow** | CVPR 2025 Oral | 2501.08331 | `Go-with-the-Flow_2501.08331_source.tar.gz` |
| 7 | **MotionV2V** | arXiv 2025 | 2511.20640 | `MotionV2V_2511.20640_source.tar.gz` (may be removed) |

## Actual source/ File Structure (as built)

```
source/
├── main.tex                      # Top-level document (report class, 88 lines)
├── preamble.tex                  # Unified preamble (245 lines, all packages + custom commands)
├── math_commands.tex              # Minimal placeholder
│
├── src/
│   ├── 0a_title_page.tex         # Title: "Creative Applications of Diffusion Models"
│   ├── 0b_abstract.tex           # PLACEHOLDER (red text)
│   ├── 0c_publications.tex       # Lists all 5 core papers
│   ├── 1_introduction.tex        # PLACEHOLDER (red text)
│   ├── 2_literature.tex          # Unified lit review (inputs per-paper related_work_thesis.tex)
│   │
│   ├── 3_peekaboo.tex            # Chapter stub → inputs from 1_Peekaboo/
│   ├── 1_Peekaboo/
│   │   ├── alltex_thesis.tex     # Main body (~630 lines), labels prefixed peekaboo_
│   │   ├── appendix_thesis.tex   # Supplementary demoted to subsections
│   │   ├── related_work_thesis.tex  # "Zero-Shot Segmentation with Diffusion Models"
│   │   ├── alltex.tex            # Original (reference only)
│   │   ├── appendix.tex          # Original (reference only)
│   │   ├── main.tex              # Original (reference only)
│   │   ├── egbib.bib
│   │   └── figures/              # Reorganized from flat naming to proper dirs
│   │
│   ├── 4_diffusion_illusions.tex # Chapter stub → inputs from 2_DiffIllusions/
│   ├── 2_DiffIllusions/
│   │   ├── main_thesis.tex       # Main body, labels prefixed diffill_
│   │   ├── X_suppl_thesis.tex    # Supplementary adapted
│   │   ├── related_work_thesis.tex  # Extracted related work
│   │   ├── main.tex              # Original (reference only)
│   │   ├── X_suppl.tex           # Original (reference only)
│   │   ├── preamble.tex          # Original (reference only)
│   │   ├── main.bib
│   │   └── figs/                 # Figures + tex subfigures
│   │
│   ├── 5_magick.tex              # Chapter stub → inputs from 3_MAGICK/sec/
│   ├── 3_MAGICK/
│   │   ├── sec/
│   │   │   ├── 1_intro_thesis.tex
│   │   │   ├── 2_relatedwork_thesis.tex   # "Alpha Matting and Synthetic Dataset Generation"
│   │   │   ├── 3_method_thesis.tex
│   │   │   ├── 4_results_thesis.tex
│   │   │   ├── 5_conclusion_thesis.tex
│   │   │   ├── 6_appendix_thesis.tex      # Demoted to subsections
│   │   │   └── [originals for reference]
│   │   ├── main.tex              # Original (reference only)
│   │   ├── preamble.tex          # Original (reference only)
│   │   ├── main.bib
│   │   └── figs/                 # Figures
│   │
│   ├── 6_gwtf.tex                # Chapter stub → inputs from 4_GWTF/sec/
│   ├── 4_GWTF/
│   │   ├── sec/
│   │   │   ├── 1_intro_thesis.tex
│   │   │   ├── 2_related_work_thesis.tex  # "Motion Control in Video Diffusion Models"
│   │   │   ├── 3_method_thesis.tex
│   │   │   ├── 4_experiments_thesis.tex
│   │   │   ├── 5_conclusion_thesis.tex
│   │   │   ├── X_suppl_thesis.tex         # Demoted to subsections
│   │   │   └── [originals for reference]
│   │   ├── main.tex              # Original (reference only)
│   │   ├── preamble.tex          # Original (reference only)
│   │   ├── main.bib
│   │   └── figures/
│   │
│   ├── 7_motionv2v.tex           # Chapter stub → inputs from 5_MotionV2V/sec/
│   ├── 5_MotionV2V/
│   │   ├── sec/
│   │   │   ├── 1_intro_thesis.tex
│   │   │   ├── notation_thesis.tex
│   │   │   ├── method_thesis.tex
│   │   │   ├── experiments_thesis.tex
│   │   │   ├── conclusion_thesis.tex
│   │   │   ├── relatedworks_thesis.tex    # "Video Motion Editing"
│   │   │   ├── X_suppl_thesis.tex
│   │   │   └── [originals for reference]
│   │   ├── main.tex              # Original (reference only)
│   │   ├── preamble.tex          # Original (reference only)
│   │   ├── main.bib
│   │   └── figures/
│   │
│   └── 8_future_work.tex         # PLACEHOLDER (red text)
```

**Compilation status**: 211 pages, 0 errors, compiles clean with pdflatex+bibtex.

## Adaptation Recipe (derived from diffing Kanchana's originals vs thesis)

For each paper → thesis chapter, apply these mechanical transformations:

### 1. Structural
- Remove `\documentclass`, `\usepackage` blocks, `\title`, `\author`, `\begin{document}`, `\maketitle`, `\end{document}`
- Create a chapter stub file: `\chapter{Paper Title}\label{chapter:shortname}` + `\input{src/N_Name/sections/intro}` etc.
- Keep the original `main.tex` in the paper folder (unused, for reference)
- Remove `\bibliography{...}` and `\bibliographystyle{...}` (thesis handles this globally)

### 2. Sections Removed/Relocated
- **Abstract**: Remove entirely (thesis has its own abstract)
- **Related Work**: Extract to a separate file, rename section title to be more descriptive, include from the unified literature review chapter (Ch2)
- **Acknowledgments/Contributions/Reproducibility Statement**: Remove entirely
- **Appendix**: Demote `\section` → `\subsection`, wrap under a new `\section{Additional Details}`, remove `\appendix` command and counter resets

### 3. Label Prefixing
- Prefix ALL `\label{...}` with a paper-specific prefix (e.g., `peekaboo_`, `diffill_`, `magick_`, `gwtf_`, `mv2v_`)
- Update ALL corresponding `\cref{...}`, `\Cref{...}`, `\ref{...}` to match
- Add `\label{chapter:shortname}` at the chapter level

### 4. Figure/Input Path Rebasing
- All `\input{figures/...}` → `\input{src/N_Name/figures/...}`
- All `\input{sections/...}` → `\input{src/N_Name/sections/...}`
- All `\includegraphics{figures/...}` → `\includegraphics{src/N_Name/figures/...}`
- All `\input{tables/...}` → `\input{src/N_Name/tables/...}`

### 5. Macro Replacement
- Replace paper-specific macros (`\modelname`, `\ours`, `\modelshort`, etc.) with literal text throughout
- Keep macros defined in the thesis preamble but don't use paper-local ones

### 6. Caption Updates
- Add short captions: `\caption{Long...}` → `\caption[Short Title]{Long...}` on every figure and table (for List of Figures/Tables)

### 7. Spacing Cleanup
- Remove ALL `\vspace{-X.Xem}` spacing hacks (conference paper micro-spacing not needed in thesis)
- Remove `\vspace` before/after captions, between figures
- Adjust `\scalebox` and `\tabcolsep` if tables are too wide/narrow for thesis page

### 8. Minor
- `\citep{...}` → `\cite{...}` if thesis uses natbib with numbers style
- Remove commented-out code, TODO markers, reviewer comments
- Change "Ours" → "Proposed" in comparison tables where appropriate
- Add figure placement specifiers `[t]` or `[h]` where missing

## Literature Review Style Requirements (derived from analyzing Kanchana's thesis)

### Structure
- **Two-level**: A synthesizing main chapter (~3-4 paragraphs, ~400 words) followed by per-paper related work sections via `\input{}`
- Main chapter establishes the unifying thread and positions the thesis, then `\input`s each paper's related work
- Per-paper sections are retitled with descriptive names (not just "Related Work")
- Per-paper sections use `\bhdr{}` or `\textbf{}` bold headers to chunk subtopics, with dense citation-laden paragraphs

### Tone & Writing Style
- Formal academic prose but NOT stiff — flows naturally with narrative progression
- Historical/temporal framing: "Early methods... Recently... Building on this..."
- Heavy use of contrastive positioning: "While X, our approach Y" / "In contrast, we..."
- Citations woven inline into sentences, not dumped as lists
- NO AI-sounding phrases: no "delve into", "it is worth noting", "in the realm of", "a testament to", "notably", "leveraging the power of"
- Must pass AI writing detectors — use varied sentence structure, specific technical claims, natural hedging
- Match Ryan's voice from the papers themselves (direct, technical, not overly formal)

### Content Rules
- Main chapter must have a BIRD'S EYE VIEW of all papers and how they connect to the "Controlling Diffusion Models" theme
- Deduplication: diffusion model foundations (DDPM, score distillation, etc.) appear in Peekaboo + DiffIllusions — cover once in main chapter or first occurrence
- GWTF + MotionV2V have strong topic overlap (video diffusion, motion control) but zero citation overlap — unify the narrative
- MAGICK is the most isolated (alpha matting) — needs clear connection to the control theme
- Each per-paper section should end with clear positioning of that paper's contribution vs. prior work
- Self-citations across papers (Peekaboo cited in DiffIllusions, MAGICK, GWTF; GWTF cited in MotionV2V) should read naturally, not self-promotional

### Length Target
- Main chapter: ~400 words (3-4 paragraphs)
- Per-paper sections: ~300-600 words each (matching Kanchana's)
- Total literature review: ~2000-2500 words

### Chapter Ordering for Related Works
Chronological: Diffusion Illusions → Peekaboo → MAGICK → GWTF → MotionV2V (may be removed)

## Critical Constraints

- `source/` is the ONLY writable directory for thesis content
- All other directories are read-only references
- Intro (Ch1), Abstract, Literature Review (Ch2), and Conclusion/Future Work (Ch8) need actual writing — PLACEHOLDER for now
- The mechanical part is: extract sources, apply recipe, create skeleton

## Lessons Learned

(append-only)

- Kanchana's proposal has 4 papers as core chapters. Ryan has 5.
- The `form.tex` is a committee signature form template.
- Some paper chapters are stubs with `\input{}`, others are large inline files. Stubs are cleaner.
- Kanchana kept original main.tex files in each paper folder as unused reference copies.
- The preamble needs to be a union of all packages from all papers. Conflicts must be resolved.
- Label prefixing is the most tedious but most critical step — namespace collisions break the build.
- Related work sections get extracted and retitled with more descriptive names for the unified lit review.
- `\modelname` and similar macros are always expanded to literals in the thesis version.
- MAGICK source was at an external path (`/Users/ryan/CleanCode/Projects/Adobe2023/MAGICK_Paper`), not in papers/ tarballs.
- MAGICK bib had unescaped `&` in publisher/booktitle fields — fixed to `\&`.
- MAGICK uses `\promptExampleSize` and `\promptstyle` macros — defined at top of `3_method_thesis.tex` rather than in thesis preamble (chapter-local).
- bibtex "Too many commas" warning for `zhou2017scene` is a malformed author field in the bib — cosmetic, doesn't break compilation.
