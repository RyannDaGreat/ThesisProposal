# Ryan Burgert - First-Author Citation Impact Analysis

## Overview

This document traces the downstream research impact of first-author publications by Ryan Burgert, examining direct citations, second-order citations, and research directions that emerged from this work.

---

## 1. Go-with-the-Flow (CVPR 2025 Oral)

**Title:** Go-with-the-Flow:  Motion-Controllable Video Diffusion Models Using Real-Time Warped Noise
**Venue:** CVPR 2025 (Oral Presentation)
**arXiv:** 2501.08331 (January 2025)

### Citation Status

Due to recency (published January 2025), direct citation accumulation is limited. However, the work has generated immediate technical follow-up.

### Direct Technical Extensions

| Paper | Venue | Relationship |
|-------|-------|--------------|
| **EquiVDM** (Liu & Vahdat, NVIDIA) | arXiv 2504.09789 | Provides theoretical foundation for warped noise via equivariance analysis; validates and extends core innovation |
| **MotionMatcher** | arXiv 2502.13234 | Addresses same problem domain via feature-level motion alignment |

### Concurrent Research Landscape (CVPR 2025)

Go-with-the-Flow occupies the noise-space motion control niche among 2025 motion control papers:

| Approach | Paper | Method |
|----------|-------|--------|
| Noise warping | Go-with-the-Flow | Optical flow → warped noise |
| Trajectory control | Motion Prompting (Geng et al.) | Point trajectories → ControlNet |
| Region-wise control | MotionPro (Zhang et al.) | Region masks + trajectories |
| 3D-aware control | Diffusion as Shader | 3D tracking videos |

### Foundational Concepts Introduced

1. **Real-time noise warping** as motion control primitive
2. **Model-agnostic fine-tuning** demonstrated across CogVideoX, AnimateDiff
3. **Unified motion control paradigm** (local object, global camera, motion transfer)

### Assessment

The paper establishes noise warping as a viable alternative to trajectory conditioning. EquiVDM's theoretical extension within 3 months indicates technical traction. Citation impact will become measurable 6-12 months post-publication.

---

## 2. Diffusion Illusions (SIGGRAPH 2024)

**Title:** Diffusion Illusions: Hiding Images in Plain Sight
**Venue:** ACM SIGGRAPH 2024
**Award:** CVPR 2023 Demo Award
**Citations:** ~10 direct citations

### Direct Citations

| Paper | Venue | Usage |
|-------|-------|-------|
| **Visual Anagrams** (Geng, Park, Owens) | CVPR 2024 | Introduced simpler zero-shot alternative; explicitly cites as related work |
| **Factorized Diffusion** (Geng, Park, Owens) | ECCV 2024 | Extends to frequency decomposition for hybrid images |
| **Diffusion-based Visual Anagram as Multi-task Learning** (Xu et al.) | WACV 2025 | Addresses failure modes in visual anagram generation |
| **PTDiffusion** (Gao et al.) | CVPR 2025 | Training-free phase transfer for hidden images |
| **LookingGlass** (Disney Research) | CVPR 2025 Oral | Extends to anamorphic 3D illusions |
| **Illusion3D** (Feng et al.) | arXiv 2412.09625 | Extends to 3D multiview illusions |
| **The Art of Deception** (Gomez-Villa et al.) | CVPR 2025 | Studies color illusions in diffusion models |
| **Illusory VQA** (Rostamkhani et al.) | CVPR 2025 Workshops | Benchmarks VLMs on illusion recognition |

### Second-Order Citations

Visual Anagrams (itself citing Diffusion Illusions) is subsequently cited by:
- Factorized Diffusion
- Diffusion-based Visual Anagram as Multi-task Learning
- LookingGlass
- Illusion3D

### Research Directions Spawned

1. **Methodology simplification:** Visual Anagrams provided zero-shot alternative to SDS-based optimization
2. **Dimensional expansion:** 2D → 3D (Illusion3D, LookingGlass)
3. **Frequency decomposition:** Hybrid images via spatial frequency (Factorized Diffusion)
4. **Evaluation frameworks:** Illusory VQA benchmark

### Foundational Contributions

- First systematic pipeline for automated optical illusion generation using diffusion models
- Introduced "prime image" parameterization for multi-view generation
- Demonstrated physical fabrication of computationally generated illusions
- Established diffusion models as primary tool for optical illusion generation, displacing GAN-based approaches

### Assessment

Diffusion Illusions established a research subfield. The paper's methodological choices (SDS optimization, prime images) have been both adopted and improved upon. Visual Anagrams' simpler method became the baseline for many follow-ups, while Diffusion Illusions' optimization approach remains relevant for controlled generation. Citation trajectory shows accelerating impact (more 2025 citations than 2024).

---

## 3. MAGICK (CVPR 2024)

**Title:** MAGICK: A Large-scale Captioned Dataset from Matting Generated Images using Chroma Keying
**Venue:** CVPR 2024
**Dataset:** 150,000 RGBA images at 1024×1024
**Downloads:** 3,321/month (Hugging Face)

### Direct Usage in Research

| Paper | Venue | Usage |
|-------|-------|-------|
| **Trans-Adapter** (Dai et al.) | ICCV 2025 | 200 images for training; 400 images in LayerBench-Generated benchmark |
| **PSDiffusion** | arXiv 2505.11468 | MAGICK used for FID evaluation of RGBA layer quality |
| **Alfie** (Quattrini et al.) | ECCV 2024 Workshop | References MAGICK as "the biggest recently proposed dataset" |

### Benchmark Integration

**LayerBench** (introduced by Trans-Adapter, ICCV 2025):
- First high-quality benchmark for transparent image inpainting
- MAGICK images comprise 50% of the generated subset (200 of 400 images)
- Establishes MAGICK as standard evaluation resource

### Related Research Enabled

| Paper | Contribution |
|-------|--------------|
| **TransPixeler** (CVPR 2025) | Extends RGBA generation to video domain |
| **OmniAlpha** (arXiv 2511.20211) | First unified multi-task RGBA generation framework |
| **SDMatte** (ICCV 2025) | Diffusion-based interactive matting |
| **DRIP** (NeurIPS 2024) | Diffusion priors for image matting |

### Assessment

MAGICK has achieved benchmark status within 12 months of publication:
- Integrated into LayerBench as evaluation standard
- No competing large-scale RGBA datasets published post-MAGICK
- Monthly download rate indicates sustained practical utility
- Research extends from single-image RGBA to video transparency (TransPixeler) and multi-layer composition (OmniAlpha)

---

## 4. MotionV2V (arXiv 2025)

**Title:** MotionV2V: Editing Motion in a Video
**Status:** arXiv preprint (November 2025)
**Collaboration:** Google, Stony Brook University

### Citation Status

No direct citations indexed as of February 2026 (expected given November 2025 submission).

### Concurrent Research Landscape

MotionV2V appears within an active trajectory-based video editing ecosystem:

| Paper | Venue | Method | Distinction |
|-------|-------|--------|-------------|
| MotionV2V | arXiv 2511.20640 | Motion counterfactuals + sparse trajectories | Video editing focus |
| Motion Prompting | CVPR 2025 Oral | Track-conditioned ControlNet | Generation focus |
| Trajectory Attention | ICLR 2025 | Attention along trajectories | Auxiliary mechanism |
| VHOI | arXiv 2512.09646 | Motion densification | Human-object interactions |
| 3D Point Tracks | arXiv 2512.02015 | 3D track-conditioned V2V | 3D representation |
| MagicMotion | ICCV 2025 | Dense-to-sparse guidance | Multi-granularity |

### Novel Contributions

1. **Motion counterfactuals:** Video pairs with identical content but distinct motion
2. **Trajectory deviation formulation:** Direct editing via sparse trajectory manipulation
3. **Timestamp-flexible edits:** Modifications propagate naturally from any point

### Assessment

MotionV2V represents a methodologically sound contribution to trajectory-based video editing. The motion counterfactual concept, while not yet adopted, aligns with emerging interest in counterfactual video generation. Citation accumulation expected 3-6 months post-submission as indexing completes.

---

## 5. Peekaboo (arXiv 2022)

**Title:** Peekaboo: Text to Image Diffusion Models are Zero-Shot Segmentors
**Status:** arXiv preprint (November 2022)

### Research Impact

Peekaboo demonstrated that text-to-image diffusion models encode sufficient semantic-spatial information for zero-shot segmentation without task-specific training. This finding generated substantial follow-up research.

### Direct Follow-Up Work

| Paper | Venue | Relationship |
|-------|-------|--------------|
| **Grounded Diffusion** (Li et al.) | ICCV 2023 | Extended with learnable grounding module |
| **ODISE** (Xu et al.) | CVPR 2023 Highlight | Extended to panoptic segmentation; +8.3 PQ on ADE20K |
| **DiffuMask** (Wu et al.) | ICCV 2023 | Extracts cross-attention for synthetic mask generation |
| **OVDiff** (Oxford VGG) | ECCV 2024 | Pure inference-time method; +5% on PASCAL VOC |
| **DiffSegmenter** | IEEE TIP 2025 | Formalizes attention-based segmentation insight |
| **OVAM** (Marcos-Manchon et al.) | CVPR 2024 | Token optimization for attention maps |
| **DiffSeg** (Tian et al.) | CVPR 2024 | Self-attention merging; +26% pixel accuracy on COCO-Stuff-27 |
| **Diffusion-Guided WSSS** | ECCV 2024 | Fuses diffusion-CAMs with ViT; SOTA on VOC/COCO |
| **DiffCut** (Couairon et al.) | NeurIPS 2024 | Diffusion features + normalized cut |

### Research Directions Spawned

1. **Attention-map exploitation:** DiffSegmenter, OVAM, DiffSeg formalize cross/self-attention for segmentation
2. **Weakly-supervised extension:** Diffusion-Guided WSSS, IACD apply insight to image-level supervision
3. **Domain-specific applications:** RS-Dseg (remote sensing), biomedical segmentation
4. **Video extension:** Zero-shot video semantic segmentation (arXiv 2405.16947)
5. **Foundation model combinations:** Integration with CLIP, DINO, SAM

### Second-Order Impact

Papers citing Peekaboo follow-ups consistently note:
- Diffusion-based zero-shot segmentation as a "promising direction"
- Attention maps as the primary extraction mechanism
- Training-free inference as the standard approach
- Open-vocabulary capability as core requirement

### Assessment

Peekaboo established a research direction that remains active through 2025. The paper's core insight—diffusion models implicitly learn semantic localization—has been validated and extended across 20+ subsequent papers at CVPR, ICCV, ECCV, and NeurIPS. The field has moved from Peekaboo's gradient-based optimization toward attention-map extraction and combination with vision foundation models.

---

## 6. TRITON (CoRL 2023)

**Title:** Neural Neural Textures Make Sim2Real Consistent
**Venue:** 6th Conference on Robot Learning (CoRL)
**Publication:** PMLR Volume 205

### Citation Status

Limited explicit citations in subsequent published work through early 2025.

### Field Evolution

The problem TRITON addressed (temporal consistency in sim2real) has been pursued via alternative technical directions:

| Approach | Representative Work | Status |
|----------|---------------------|--------|
| Gaussian Splatting | SplatSim (2024), RoboGSim (2024) | Dominant current approach |
| Diffusion models | Crossway Diffusion (ICRA 2024) | Active research area |
| Vision foundation models | Theia (CoRL 2024) | Transfer learning advantages |
| Neural textures (TRITON) | — | Not widely adopted |

### Assessment

TRITON's specific approach of learnable neural textures for temporal consistency has not been widely replicated. The research community has converged on Gaussian Splatting and diffusion models as preferred alternatives for achieving photorealism and temporal consistency. The authors' subsequent work (LLaRA, Theia) has shifted toward vision-language models and foundation model approaches.

---

## Summary

### Impact by Paper

| Paper | Venue | Direct Citations | Research Directions | Field Status |
|-------|-------|------------------|---------------------|--------------|
| Go-with-the-Flow | CVPR 2025 Oral | Emerging | Noise warping for motion control | Active, theoretical extensions underway |
| Diffusion Illusions | SIGGRAPH 2024 | ~10 | Optical illusion generation via diffusion | Established subfield |
| MAGICK | CVPR 2024 | 3+ | RGBA generation, transparent image processing | Benchmark standard |
| MotionV2V | arXiv 2025 | — | Motion counterfactuals, trajectory editing | Too recent to assess |
| Peekaboo | arXiv 2022 | 20+ | Zero-shot diffusion segmentation | Mature, active research area |
| TRITON | CoRL 2023 | Limited | — | Superseded by alternative approaches |

### Aggregate Observations

1. **Peekaboo** generated the largest downstream research ecosystem, establishing zero-shot diffusion segmentation as an active subfield with 20+ follow-up papers at top venues.

2. **Diffusion Illusions** created a new research direction in optical illusion generation, with clear citation chains through Visual Anagrams to subsequent 2024-2025 work.

3. **MAGICK** achieved practical benchmark status, integrated into LayerBench and used for evaluation across multiple RGBA generation papers.

4. **Go-with-the-Flow** received CVPR Oral designation and immediate theoretical extension (EquiVDM), indicating strong initial reception pending citation accumulation.

5. **MotionV2V** and **TRITON** show limited citation impact—MotionV2V due to recency, TRITON due to field evolution toward alternative approaches.

---

*Analysis conducted: February 2026*
