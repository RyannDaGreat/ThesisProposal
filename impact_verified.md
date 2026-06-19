# Verified Research Impact — Fact-Check Consolidation

**Date:** 2026-06-19
**Method:** Five 10-agent research frenzies (50 agents total), one per paper, live WebSearch + WebFetch, mid-2026.
**Purpose:** Source-grounded ground truth for the thesis Research Impact chapter (`source/src/8_future_work.tex`).
Supersedes the unverified estimates in `impact.md`. Per-paper raw reports: `.frenzy/impact/F1`–`F5`.

**Legend:** ✅ verified · ⚠️ needs rewording/softening · ❌ refuted (your note was wrong)

---

## Five things that would have been WRONG in the thesis (read these first)

1. **Factorized Diffusion shirt = CVPR 2024, not 2025** (Seattle-skyline→"CVPR" hybrid, >10k shirts; ECCV 2024 paper).
2. **Illusion3D is NOT SIGGRAPH** — arXiv 2024 + CVPR 2025 Art Gallery exhibit.
3. **MotionMatcher does NOT use Go-with-the-Flow** — would have been a false citation. Drop it.
4. **MotionV2V "first motion edit" must be scoped** — bare "first" is refuted by MotionEditor (2023), MotionFollower / ReVideo (2024). Use "first video-to-video, general-object motion editor."
5. **ODISE / DiffuMask do NOT cite Peekaboo** — of 8 named candidates, only DiffCut actually does.

---

## 1. Peekaboo (arXiv 2022) — `.frenzy/impact/F1_peekaboo.md`

**Citations:** ~41 (Semantic Scholar, mid-2026) ✅. Google Scholar likely higher but blocked from fetch.

| Claim | Verdict | Verified finding | Source |
|---|---|---|---|
| Inspired "your diffusion model is secretly a classifier" | ⚠️ | Real paper: *Your Diffusion Model is Secretly a Zero-Shot Classifier*, Li/Prabhudesai/Duggal/Brown/Pathak, **CMU, ICCV 2023**, arXiv:2303.16203, **355 cites (S2)**. It **cites Peekaboo (ref [9])** — bibliography only, no body engagement. Say "cited by," not "inspired." (Your note guessed Thickstun — wrong.) A 2nd diffusion-classifier paper (Clark & Jaini, NeurIPS 2023) also cites Peekaboo. | arXiv:2303.16203 |
| First RGBA text-to-image | ⚠️ | Defensible as **"first to attempt transparent (RGBA) generation from an RGB-only model"** (the abstract literally says "to our knowledge we are the first to attempt"). Not a native RGBA generator; LayerDiffuse (Feb 2024) is first *trained/high-quality* RGBA, 15 months later. | Peekaboo abstract |
| Mechanism reused in Diffusion Illusions "immediately after" | ⚠️ | Reuse ✅ (both = Score Distillation loss on frozen SD; DI cites Peekaboo). But **~13 months apart** (Nov 2022 → Dec 2023 / SIGGRAPH 2024) — say "subsequently reused," not "immediately." SDS itself originates from **DreamFusion**, not Peekaboo. | — |
| Downstream segmentation papers cite it | ❌/⚠️ | Of 8 named (ODISE, DiffuMask, OVDiff, DiffSeg, DiffSegmenter, DiffCut, OVAM, Grounded Diffusion), **only DiffCut** verifiably cites Peekaboo. Confirmed citers: DiffCut, FreeSeg-Diff (benchmarks against & beats Peekaboo), SLiMe, SATR. | full-text grep |

**New / cross-domain:** DGMO (Interspeech 2025) ports Peekaboo's optimization to **audio source separation** — genuine cross-domain reach (classification, 3D, robotics, audio, matting). Venue was precisely the **O-DRUM workshop @ CVPR 2023** (poster, not main track — don't say "CVPR 2023" unqualified). GitHub: 31 stars.
**Watch out:** unrelated Microsoft "PEEKABOO" (arXiv:2312.07509, video gen) — do not conflate.

---

## 2. Diffusion Illusions (SIGGRAPH 2024) — `.frenzy/impact/F2_diffusion_illusions.md`

**Citations:** ~26 (Semantic Scholar) / 28 (Scholar) ✅ — the old "21" was stale.

| Claim | Verdict | Verified finding | Source |
|---|---|---|---|
| CVPR Demo Award year | ✅ **2023** | Official CVPR 2023 awards page (Demo Awards / Outstanding Demos) + project site ("best demo award in CVPR 2023") + SBU news Jun 2023. **NOT 2024** (CVPR 2024 best demo = Gaussian Splatting SLAM). | cvpr2023 awards; diffusionillusions.com |
| SIGGRAPH 2024 paper | ✅ | Confirmed. | — |
| Steve Mould video | ✅ | Real, Sep 14 2024, embedded on project site. | diffusionillusions.com |
| Matt Parker video | ✅ | Real, Sep 14 2024; description cites paper + all 5 authors verbatim. | YouTube |
| Visual Anagrams oral | ✅ | **CVPR 2024 Oral** (Geng, Park, Owens); cites DI as ref [2]. | — |
| LookingGlass (Pascal) CVPR oral | ✅ | **CVPR 2025 Oral**, Disney Research, lead Pascal Chang. Cites/extends DI to anamorphic 3D. | — |
| Factorized Diffusion = CVPR shirt | ❌ | **CVPR 2024 shirt** (Seattle-skyline→"CVPR" hybrid, >10k shirts), **NOT 2025**. ECCV 2024 paper (Geng/Park/Owens). Cites DI ref [5]. | — |
| Illusion3D = SIGGRAPH | ❌ | **Not SIGGRAPH** — arXiv 2024 preprint + **CVPR 2025 Art Gallery** exhibit. Yue Feng (UMD) lead. Cites DI. | arXiv:2412.09625 |
| Spawned its own subfield | ⚠️ | Founding/early work (demoed CVPR 2023), but **Visual Anagrams is a near-simultaneous progenitor** (arXiv ~1 week earlier, though it cites DI as prior). Soften to "among the first / helped establish an active line of research." | — |

**Full inspired-works list (FC-D9), 9 core generation papers:** Visual Anagrams, Factorized Diffusion, PTDiffusion (CVPR 2025), Anagram-MTL / "Diffusion-based Visual Anagram as Multi-task Learning" (WACV 2025), Illusion3D, LookingGlass, "Making Images from Images," "Stroke of Surprise," "The Art of Deception" (CVPR 2025) — + adjacent benchmarking (Illusory VQA) & 3D-art works. 6 confirmed to cite DI via bibliography check.
**Watch out:** do NOT conflate with the viral Reddit "Ugleh" spiral / "Illusion Diffusion" HF tool — a separate ControlNet hobbyist tool.

---

## 3. MAGICK (CVPR 2024) — `.frenzy/impact/F3_magick.md`

**Citations:** ~20 (Scholar) / 15 (S2; undercounts) — true ~20–22. **HF downloads: 6,448/month.** Both ~doubled vs old estimates. Size: ~150K (HF/GitHub say "140,000+"). GitHub: 11 stars.

| Claim | Verdict | Verified finding | Source |
|---|---|---|---|
| High impact? Who cited it & why? | ✅ | Moderately high, concentrated in transparent/RGBA/layered generation, where MAGICK is the de-facto reference 150K RGBA dataset. **6 papers materially USE it:** Trans-Adapter (ICCV 2025), TKG-DM (CVPR 2025, uses 3,000 MAGICK imgs), PrismLayers ("Inspired by MAGICK"), PSDiffusion (WACV 2026), LayeringDiff, a portrait-matte work. + ~6 cite as landmark (ART, Alfie, LayerDecomp, OmniPSD, TAUE). Multiple call it "the only dataset balancing both scale and quality." | huggingface.co/datasets/OneOverZero/MAGICK |
| Largest public general-domain RGBA dataset | ✅ | True — **"public" is load-bearing.** Next-largest public general-domain matting set = SIM (726 foregrounds); MAGICK ~15× bigger. The only larger general-domain RGBA set (LayerDiffuse, 1M) was **never released**. | — |
| PDF figures alone > prior largest matting set | ✅ | Paper itself prints: "the 1400 matted images exhibited in this document surpass... the previously largest general-purpose matting dataset, which contained 726 objects." | MAGICK paper |

**Refuted:** OmniAlpha and LayerDiffuse do NOT cite MAGICK; TransPixeler cites bib-only (shared co-author). No awards/media — standard CVPR poster. LayerBench (introduced by Trans-Adapter) is ~25% MAGICK images.

---

## 4. Go-with-the-Flow (CVPR 2025 Oral) — `.frenzy/impact/F4_gwtf.md`

**Citations:** ~107 (Semantic Scholar; was estimated 62). Repo under **Eyeline-Labs**.

| Claim | Verdict | Verified finding | Source |
|---|---|---|---|
| 1000+ GitHub stars | ✅ | **1,081** (UI "1.1k"). | github.com/Eyeline-Labs/Go-with-the-Flow |
| AnimateDiff + HunyuanVideo ports | ✅ | Both by dev **spacepxl**: AnimateDiff LoRA (2025-01-24, ~10 days post-release) + HunyuanVideo (2025-02-07). | README "Community Adoption" |
| ZeptaFrame + Kijai nodes | ✅ | ZeptaFrame (web editor, Pablerdo) + kijai's `ComfyUI-VideoNoiseWarp`. | README |
| Charles Herrmann physics paper | ✅ | **WonderPlay** (ICCV 2025 Highlight, Stanford/Utah, arXiv 2505.18151) — Herrmann co-author; uses GWTF as physics-renderer. | arXiv:2505.18151 |
| ~5 other papers built on it | ⚠️ | **4, not 5:** EquiVDM (NVIDIA, Liu & Vahdat), WonderPlay, HumANDiff, CameraNoise. **MotionMatcher does NOT use GWTF — drop it.** | — |
| Warped-noise extensions ("several") | ✅ | EquiVDM (proves equivariance *theory* of warped noise) + CameraNoise + HumANDiff. ⚠️ "Infinite-Resolution Integral Noise Warping" (Nov 2024) is prior/sibling (Burgert author), not a follow-up. | — |
| 3D extension | ✅ | **CameraNoise** (ICML 2026; 3D camera-geometry reprojection / GRFlow); HumANDiff (3D articulated). No true 3D-*volume* noise warping yet. | — |
| Yosun Chang CVPR 2025 demo honorable mention | ✅ | Demo **"AI3D Render"** won **Best Demo Honorable Mention** — official CVF awards page. | CVF awards |
| Citations + oral rate | ⚠️ | **~107 cites.** "Top 0.73%" = orals/submissions (95/13,008); orals were **3.3% of accepted**. Be precise. | — |
| SOTA by a long shot, stayed SOTA for months | ⚠️ | NOT independently verified — supported only indirectly (rivals use GWTF as baseline-to-beat). Cite paper's own benchmark tables or soften "for months." | — |

**Unresolved:** No Wan/LTX/Mochi ports found.

---

## 5. MotionV2V (CVPR 2026) — `.frenzy/impact/F5_motionv2v.md`

**Citations:** ~10 (Semantic Scholar, Jun 2026). GitHub `RyannDaGreat/MotionV2V`, 57 stars (project-page host, no code/weights released).

| Claim | Verdict | Verified finding | Source |
|---|---|---|---|
| Has anyone cited it yet? | ✅ **yes** | ~10 cites; one verified end-to-end: **TrajectoryMover** (arXiv 2603.29092, KTH/Adobe). "Likely zero" premise was wrong (~7 months post-release). | S2 |
| First to demonstrate motion edits | ❌ | Bare "first" REFUTED — MotionEditor (Nov 2023), MotionFollower (May 2024), ReVideo (May 2024) predate it. Use the paper's own scoped claim: **first video-to-video, general-object motion editor** (vs prior image-to-video / human-skeleton-specific). A bare "first" will not survive review. | — |
| CVPR 2026 | ✅ | Confirmed — CVF Open Access + IEEE/CVF proceedings **pp. 35988–35997**. arXiv carries no venue tag. Affiliation = **"Google"** (not necessarily DeepMind). | CVF Open Access |

**Other:** "Motion counterfactuals" is a genuine, as-yet-unadopted coinage. Does NOT build on Go-with-the-Flow (GWTF appears only as a baseline it beats). Minimal social/press traction. Don't confuse with "Generative Video Motion Editing with 3D Point Tracks" (Lee et al., also CVPR 2026).
