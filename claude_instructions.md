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

**Compilation status**: 228 pages, 0 errors, compiles clean with pdflatex+bibtex.

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

### Tone & Writing Style (REVISED based on forensic analysis of Kanchana's actual text)
- **CRITICAL: Synthesis paragraphs have ZERO \cite{} commands** — concepts named inline (e.g. "CLIP", "LLaVA") but never formally cited. This is intentional: it's a conceptual overview, not a cited literature review.
- Per-paper sections DO have dense citations (these come from the original papers verbatim)
- Formal academic prose but NOT stiff — flows naturally with narrative progression
- Historical/temporal framing: "Early methods... Recently... Building on this..."
- Heavy use of contrastive positioning: "While X, our approach Y" / "In contrast, we..."
- NO AI-sounding phrases: no "delve into", "it is worth noting", "in the realm of", "a testament to", "notably", "leveraging the power of"
- Must pass AI writing detectors — use varied sentence structure, specific technical claims, natural hedging
- Match Ryan's voice from the papers themselves (direct, technical, not overly formal)

### Content Rules (REVISED)
- Main chapter synthesis: BIRD'S EYE VIEW, zero citations, conceptual landscape only
- Per-paper sections: keep NEAR-VERBATIM from original papers (Kanchana changed <2% of his)
- Only cosmetic changes to per-paper sections: label prefixes, macro expansion, `\textbf{}` headers, path rebasing, `\vspace{0.5em}` spacing
- NO aggressive trimming or deduplication (Kanchana did none)
- Each per-paper section should end with clear positioning of that paper's contribution vs. prior work
- Self-citations across papers should read naturally, not self-promotional

### Length Target
- Main chapter: ~400 words (3-4 paragraphs)
- Per-paper sections: ~300-600 words each (matching Kanchana's)
- Total literature review: ~2000-2500 words

### Chapter Ordering for Related Works
Chronological: Diffusion Illusions → Peekaboo → MAGICK → GWTF → MotionV2V (may be removed)

## Ryan's Voice Notes — Abstract & Intro Direction (2026-02-21)

**NON-NEGOTIABLE REQUIREMENTS:**
- Be deeply familiar with ALL 5 papers, Kanchana's formatting/structure/tone, and Ryan's writing voice
- Use Ryan's vocabulary and writing style (direct, technical, not overly formal)
- SHORT text preferred — adding is easier than removing. Never pad with garbage.
- Will never be yelled at for being under-length, WILL be yelled at for adding filler

**Core Narrative: "Controlling Diffusion Models"**
- The difference between AI slop and useful AI output is the ratio of input to output dimensionality
- When artists can't control what they generate, they make slop
- Text-to-image is like tofu — needs flavoring, not good on its own
- Each paper = a new form of control over diffusion models, making them useful to artists

**Paper-by-Paper Narrative (Ryan's words, paraphrased):**

1. **Peekaboo** — "Where I learned to harness diffusion models." Used score distillation loss (Ryan calls it "dream loss") to do segmentation, which is actually a form of generation — generating the alpha mask. Cool because it made diffusion models generate alpha even though they were only ever trained on RGB. Controls foreground/background separation. The alpha rasterization trick actually connects to MAGICK later.

2. **Diffusion Illusions** — Controls not just the picture but the ANGLE at which you view it and what you see from that angle. Can turn a dog into a skull depending on viewing angle. Multiple types of illusions. Very similar background to Peekaboo (score distillation) but very different application. **HUGE IMPACT** — YouTube coverage, millions of views, tons of GitHub stars. MUST research and report impact.

3. **MAGICK** — Made with Adobe. "Bootstrapping a diffusion model to do something new." Lavishly simple trick: ask the model to generate a dog on a green screen, and "somehow that fucking works." Created alpha-controlled dataset — could give it an alpha mask and it generates RGB. New modality that couldn't have existed without tens/hundreds of thousands of samples. Largest matting dataset to date — the appendix had more pictures than the second-largest matting dataset before it. "That's a big deal."

4. **Go-with-the-Flow** — Controls MOTION in diffusion models. How we want things to move, not just how they look. Uses warped noise algorithm. Also has a motion illusion application: things visible only when they move (like a Rick Roll that disappears when paused). **BIG IMPACT** — 1000+ GitHub stars, tons of Twitter attention, CVPR Oral (less than 1% get that). MUST research and report impact.

5. **MotionV2V** — "Most recent work" / ongoing work. Not only controls motion but TRANSFERS content from one video to another. Editing is harder than generation because you must adhere to the original video's content. This is the proposed/future work direction.

**Structure Requirements:**
- Impact discussion at end of intro (or dedicated section)
- Check if Kanchana has an "ongoing work" section — MotionV2V would go there
- The intro should flow: motivation (control) → each paper as a step in the progression → impact → ongoing work

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
- `\modelname` in Peekaboo's `related_work_thesis.tex` was undefined when loaded from lit review chapter (outside the chapter that defines it) — replaced with literal "Peekaboo".

## File Change Log (append-only)

### Literature Review Session (2026-02-20)

**Created:**
- `source/src/2_DiffIllusions/history_thesis.tex` — Full "History of Illusions" section (classical, computational, diffusion-based illusions + figure) extracted from the original related_work and placed in the DiffIllusions chapter body.
- `.frenzy/litreview/agent{1-5}.tex` — 5 competing lit review drafts from Opus frenzy (kept for reference).

**Modified:**
- `source/src/2_literature.tex` — Replaced placeholder with 3-paragraph synthesis + 5 per-paper `\input{}` lines.
- `source/src/2_DiffIllusions/related_work_thesis.tex` — Condensed from 749 words (with figure + subsubsections) to 240 words (flat `\textbf{}` sections, no figure). Full history content moved to `history_thesis.tex`.
- `source/src/2_DiffIllusions/main_thesis.tex` — Changed `\input{related_work_thesis}` → `\input{history_thesis}` so the chapter body includes the full history section.
- `source/src/1_Peekaboo/related_work_thesis.tex` — Replaced `\modelname` → `Peekaboo` (4 occurrences).
- `source/src/3_MAGICK/sec/2_relatedwork_thesis.tex` — Trimmed from 558 to 268 words, flattened `\paragraph{}` → `\textbf{}` to match Kanchana's style.
- `source/src/4_GWTF/sec/2_related_work_thesis.tex` — Trimmed from 536 to 187 words, flattened `\subsection{}` → `\textbf{}` to match Kanchana's style.
- `source/src/5_MotionV2V/sec/relatedworks_thesis.tex` — Trimmed from 374 to 208 words, flattened `\subsection{}` → `\textbf{}` to match Kanchana's style.

**Split:**
- `related_work_thesis.tex` (DiffIllusions) was split into:
  - `history_thesis.tex` — Full history content (figure + subsections), included in chapter body
  - `related_work_thesis.tex` — Condensed related work for lit review chapter

**Word count comparison (lit review chapter total):**
- Kanchana: 2,177 words (synthesis + 4 per-paper sections)
- Ours: 1,640 words (synthesis + 5 per-paper sections)
- Compilation: 225 pages, 0 LaTeX errors

### Literature Review Revision — Kanchana Style Match (2026-02-20)

**Modified:**
- `source/src/2_literature.tex` — Rewrote 3 synthesis paragraphs with ZERO citations (matching Kanchana exactly). 416 words.
- `source/src/3_MAGICK/sec/2_relatedwork_thesis.tex` — Restored to near-verbatim from original paper (268 → 550 words). Full Synthetic segmentation, Alpha matting datasets, and Segmentation and Matting sections.
- `source/src/4_GWTF/sec/2_related_work_thesis.tex` — Restored to near-verbatim from original paper (187 → 521 words). Full Image/Video Diffusion Models and Motion Controllable Video Generation sections.
- `source/src/5_MotionV2V/sec/relatedworks_thesis.tex` — Restored to near-verbatim from original paper (208 → 337 words). Full Conditional Video Generation and Motion-Guided Video Generation sections.
- `source/src/2_DiffIllusions/related_work_thesis.tex` — Expanded with restored Diffusion-based Image Generation and Contemporary Work content (240 → 352 words).

**Word counts after revision:**
| Section | Words |
|---------|-------|
| Synthesis | 416 |
| DiffIllusions | 352 |
| Peekaboo | 294 |
| MAGICK | 550 |
| GWTF | 521 |
| MotionV2V | 337 |
| **Total** | **2,470** |

- Kanchana total: 2,177 words
- Zero citations verified in synthesis paragraphs
- Compilation: 228 pages, 0 LaTeX errors

### Abstract & Introduction Session (2026-02-21)

**Modified:**
- `source/src/0b_abstract.tex` — Replaced placeholder with abstract (281 words, Kanchana's: 372). Covers: control problem motivation, per-paper summary (1 paragraph each), no citations.
- `source/src/1_introduction.tex` — Replaced placeholder with full introduction (1,031 words, Kanchana's: 1,109). Structure: `\section{Overview}` (motivation + 5 `\textbf{}` contribution descriptions + impact paragraph) + `\section{Organization}` (7 `\paragraph{}` chapter descriptions).

**Impact data verified via online research:**
- Peekaboo: 41 Semantic Scholar citations, 106 HN points
- Diffusion Illusions: 21 citations, 251 GH stars, CVPR 2023 Best Demo, YouTube coverage (Steve Mould, Stand Up Maths, JacksFilms)
- MAGICK: 14 citations, 3,342 HF downloads/month, Adobe Research collab
- GWTF: 62 citations, 1,100 GH stars, CVPR 2025 Oral (95/13,008 = top 0.73%)
- MotionV2V: 54 GH stars in 3 months, Google collab

**Word count comparison:**
| Section | Ours | Kanchana's |
|---------|------|-----------|
| Abstract | 281 | 372 |
| Introduction | 1,031 | 1,109 |

- Intentionally shorter per Ryan's instruction ("adding is easier than removing")
- Compilation: 231 pages, 0 LaTeX errors
