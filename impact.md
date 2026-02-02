# Ryan Burgert - First-Author Academic Impact Report

> **Note:** Academic publications are under "Ryan Burgert" (with 'g').

---

## First-Author Publications

### 1. Go-with-the-Flow (CVPR 2025 - ORAL)

**Title:** Go-with-the-Flow: Motion-Controllable Video Diffusion Models Using Real-Time Warped Noise

| Detail | Value |
|--------|-------|
| **Venue** | CVPR 2025 (IEEE/CVF Conference on Computer Vision and Pattern Recognition) |
| **Status** | **Oral Presentation** (top ~2-3% of submissions) |
| **Pages** | 13-23 |

**Authors:** Ryan Burgert, Yuancheng Xu, Wenqi Xian, Oliver Pilarski, Pascal Clausen, Mingming He, Li Ma, Yitong Deng, Lingxiao Li, Mohsen Mousavi, Michael Ryoo, Paul Debevec, Ning Yu

**Affiliations:** Netflix Eyeline Studios, Netflix, Stony Brook University, University of Maryland, Stanford University

**Impact:**
- Enables motion control in video diffusion models via structured latent noise sampling
- Novel noise warping algorithm fast enough to run in real time
- One-stop solution for local object motion, global camera movement, and motion transfer
- Official implementation released: [GitHub](https://github.com/Eyeline-Labs/Go-with-the-Flow)

**Links:** [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Burgert_Go-with-the-Flow_Motion-Controllable_Video_Diffusion_Models_Using_Real-Time_Warped_Noise_CVPR_2025_paper.html) | [arXiv](https://arxiv.org/abs/2501.08331)

---

### 2. Diffusion Illusions (SIGGRAPH 2024)

**Title:** Diffusion Illusions: Hiding Images in Plain Sight

| Detail | Value |
|--------|-------|
| **Venue** | ACM SIGGRAPH 2024 Conference Papers |
| **Article** | No. 131, Pages 1-11 |
| **Citations** | 10 |
| **Downloads** | 534 |
| **Award** | **CVPR 2023 Demo Award** |

**Authors:** Ryan Burgert, Xiang Li, Abe Leite, Kanchana Ranasinghe, Michael Ryoo

**Impact:**
- First comprehensive pipeline to automatically generate optical illusions using diffusion models
- Creates "prime" images that produce multi-arrangement optical illusions when physically arranged
- Exhibited at **OpenSauce 2023 and 2024**
- Project website: [diffusionillusions.com](https://diffusionillusions.com/)

**Links:** [ACM DL](https://dl.acm.org/doi/10.1145/3641519.3657500) | [Project](https://diffusionillusions.com/)

---

### 3. MAGICK (CVPR 2024)

**Title:** MAGICK: A Large-scale Captioned Dataset from Matting Generated Images using Chroma Keying

| Detail | Value |
|--------|-------|
| **Venue** | CVPR 2024 |
| **Dataset Size** | 140,000+ high-quality RGBA images |
| **Resolution** | 1024×1024 |
| **License** | CC BY-NC 4.0 |

**Authors:** Ryan D. Burgert, Brian L. Price, Jason Kuen, Yijun Li, Michael S. Ryoo

**Affiliations:** Stony Brook University, Adobe Research

**Impact:**
- First large-scale captioned RGBA dataset for image matting/generation
- Scalable method for synthesizing images with high-quality alpha mattes
- Enables training alpha-to-RGB generation methods that outperform baselines
- Dataset released on [Hugging Face](https://huggingface.co/datasets/OneOverZero/MAGICK)
- [GitHub](https://github.com/RyannDaGreat/MAGICK)

**Links:** [CVF](https://openaccess.thecvf.com/content/CVPR2024/html/Burgert_MAGICK_A_Large-scale_Captioned_Dataset_from_Matting_Generated_Images_using_CVPR_2024_paper.html) | [Project](https://ryanndagreat.github.io/MAGICK/)

---

### 4. MotionV2V (2025)

**Title:** MotionV2V: Editing Motion in a Video

| Detail | Value |
|--------|-------|
| **Status** | arXiv preprint (2025) |
| **User Study** | 65%+ preference vs prior work |

**Authors:** Ryan Burgert, Charles Herrmann, Forrester Cole, Michael S. Ryoo, Neal Wadhwa, Andrey Voynov, Nataniel Ruiz

**Affiliations:** Google, Stony Brook University

**Impact:**
- Described as "first truly non-local video editor"
- Modifies video motion by editing sparse trajectories
- Introduces "motion counterfactuals" - video pairs with identical content but distinct motion
- Edits can start at any timestamp and propagate naturally
- [GitHub](https://github.com/RyannDaGreat/MotionV2V)

**Links:** [arXiv](https://arxiv.org/abs/2511.20640) | [Project](https://ryanndagreat.github.io/MotionV2V/)

---

### 5. Peekaboo (2022)

**Title:** Peekaboo: Text to Image Diffusion Models are Zero-Shot Segmentors

| Detail | Value |
|--------|-------|
| **Status** | arXiv preprint |
| **Year** | November 2022 |

**Authors:** Ryan Burgert, Kanchana Ranasinghe, Xiang Li, Michael S. Ryoo

**Impact:**
- **First-of-its-kind** zero-shot, open-vocabulary, unsupervised semantic grounding using diffusion models
- No segmentation-specific re-training required
- Evaluated on Pascal VOC (unsupervised semantic segmentation) and RefCOCO (referring segmentation)
- Can generate images with transparency even though underlying model trained on RGB only
- Cited by subsequent work in weakly supervised segmentation

**Links:** [arXiv](https://arxiv.org/abs/2211.13224) | [Project](https://ryanndagreat.github.io/peekaboo/)

---

### 6. TRITON (CoRL 2023)

**Title:** Neural Neural Textures Make Sim2Real Consistent

| Detail | Value |
|--------|-------|
| **Venue** | 6th Conference on Robot Learning (CoRL) |
| **Proceedings** | PMLR 205:2215-2225 |
| **Year** | 2023 |

**Authors:** Ryan D. Burgert, Jinghuan Shang, Xiang Li, Michael S. Ryoo

**Impact:**
- Unsupervised, end-to-end, stateless sim-to-real algorithm
- Combines differentiable rendering with image translation for temporal consistency
- Generates learnable neural textures for realistic simulation
- Handles object movement and deformation, not just camera movements
- Useful for downstream robotic manipulation tasks

**Links:** [PMLR](https://proceedings.mlr.press/v205/burgert23a.html) | [arXiv](https://arxiv.org/abs/2206.13500) | [OpenReview](https://openreview.net/forum?id=Go64YOmGwxM)

---

## First-Author Impact Summary

| Paper | Venue | Year | Type | Notable |
|-------|-------|------|------|---------|
| Go-with-the-Flow | CVPR | 2025 | **Oral** | Top-tier venue, oral presentation |
| Diffusion Illusions | SIGGRAPH | 2024 | Paper | CVPR 2023 Demo Award |
| MAGICK | CVPR | 2024 | Paper + Dataset | 140K image dataset release |
| MotionV2V | arXiv | 2025 | Preprint | Google collaboration |
| Peekaboo | arXiv | 2022 | Preprint | First zero-shot diffusion segmentor |
| TRITON | CoRL | 2023 | Paper | Robotics venue |

### Key Achievements as First Author

1. **CVPR 2025 Oral** - Highly selective (~2-3% acceptance for orals)
2. **SIGGRAPH 2024** - Premier graphics venue
3. **CVPR 2023 Demo Award** - Competitive demo track award
4. **2x CVPR papers** (2024, 2025) as first author
5. **Industry collaborations:** Netflix Eyeline Studios, Google, Adobe Research
6. **Open science:** Released datasets (MAGICK) and code for all projects

### Total First-Author Publications at Top Venues

- **CVPR:** 2 papers (1 oral)
- **SIGGRAPH:** 1 paper
- **CoRL:** 1 paper
- **arXiv/Under Review:** 2 papers

---

## Overall Metrics

| Metric | Value |
|--------|-------|
| **Google Scholar Citations** | 228+ |
| **First-Author Top Venue Papers** | 4 |
| **First-Author Preprints** | 2 |
| **Datasets Released** | 1 (MAGICK - 140K images) |
| **Code Releases** | 6+ repositories |

---

## Online Presence

| Platform | Link |
|----------|------|
| Personal Website | https://ryanndagreat.github.io/ |
| Google Scholar | https://scholar.google.com/citations?user=aGdF5D0AAAAJ |
| GitHub | https://github.com/RyannDaGreat |
| Twitter/X | https://x.com/ryanburgert |

---

*Report generated: February 2, 2026*
