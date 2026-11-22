# Thesis story: "How to Control Your Diffusion Model" (Ryan Burgert, Stony Brook thesis proposal)

Sources read: `source/src/0b_abstract.tex`, `1_introduction.tex`, `2_literature.tex`, `0c_publications.tex`, `8_future_work.tex`, per-chapter intro/abstract/conclusion files, `claude_instructions.md`, `impact_verified.md`. All paths below are relative to `/Users/rburgert/Documents/ThesisProposal/source/src/` unless they start with `/`.

STATUS FLAG: the abstract (`0b_abstract.tex`), intro (`1_introduction.tex`), and Conclusion/Future Work (`8_future_work.tex`) are NO LONGER placeholders (manifest still says "PLACEHOLDER", which is stale). They are full drafts. Caveat: `8_future_work.tex` Research Impact chapter is explicitly "Claude's orange rough draft" (`\AI{...}` markers) over Ryan's original notes (kept as `%` comments). Its numbers are partly stale vs impact_verified.md (see section 4).

---

## 1. Unifying thesis argument (Ryan's wording)

Core claim, intro `1_introduction.tex` Overview:
- "text-to-image generation on its own is limited: the user provides a low-dimensional input (a sentence) and the model fills in everything else (composition, lighting, pose, transparency, motion) from its learned prior."
- "The result often looks impressive in isolation, but it reflects what the model wants to generate, not what the artist intended. For creative and professional applications, this gap between intent and output is the central obstacle."
- "None of these tasks can be addressed by text-to-image generation alone; they each require a different form of control over the generation process."
- "This thesis develops five methods that extend diffusion model control along different axes: spatial semantics, multi-view geometry, transparency, temporal motion, and video editing."
- Mechanism family: "Each method reuses frozen or minimally fine-tuned diffusion models and introduces control through inference-time optimization, dataset construction, noise-space manipulation, or targeted training."
- Payoff: "Together, they demonstrate that diffusion models contain far more structure than text-to-image generation exploits, and that this structure can be harnessed for creative applications that were previously impossible or impractical."

Abstract (`0b_abstract.tex`): "Without finer-grained control mechanisms, these models produce results that reflect the model's prior more than the artist's intent. Additionally, such vanilla usages expose only a fraction of what these base models are capable of - they can do more than just generate images and videos."

Conclusion (`8_future_work.tex`, Ryan's own phrasing): "Foundation models are extraordinarily powerful, but they are not actually useful if all we do with them is text-to-image or text-to-video." / "My argument throughout this thesis is that closing that gap is what makes these models useful, and that the structure you need to close it is already sitting inside the frozen model, waiting to be controlled." / "a frozen or lightly fine-tuned diffusion model can be steered toward things its training objective never had in mind."

Ryan's raw voice (manifest `claude_instructions.md`, "Ryan's Voice Notes", paraphrased by past sessions, not verbatim):
- "The difference between AI slop and useful AI output is the ratio of input to output dimensionality" (low-dim text in, high-dim image/video out). When artists can't control what they generate, they make slop.
- "Text-to-image is like tofu: needs flavoring, not good on its own."
- Each paper = a new form of control that makes diffusion models useful to artists.
- Ryan's description of the thesis as "a bunch of my papers duct-taped together sandwiched between the parts that they actually care about" means: the intro / lit review / conclusion carry the story, so spend slides on the arc, not per-paper detail.

Suggested 4-sentence version for the talk:
1. Text alone is a low-dimensional knob on a very high-dimensional output, so the model fills the gap with its own prior and you get slop, not intent.
2. The structure needed to close that gap is already inside the frozen model; each paper finds a different handle on it.
3. Handles, in order: score-distillation optimization (Peekaboo, Diffusion Illusions), synthetic data bootstrapped from the model itself (MAGICK), the noise itself (Go-with-the-Flow), and counterfactual training pairs (MotionV2V).
4. The axis moves from "what is where in one image" to "how things move in a whole video", ending at editing existing footage, the hardest form of control because the output must still honor what is already there.

---

## 2. The five papers

Chapter order in the document (main.tex, chronological by arXiv v1): Peekaboo (Ch3) -> Diffusion Illusions (Ch4) -> MAGICK (Ch5) -> GWTF (Ch6) -> MotionV2V (Ch7). The intro's contribution list and the abstract use this same order. (Manifest note: an earlier note said DI before Peekaboo; WRONG, Peekaboo predates DI by 13 months. The user's brief lists DI first; follow the document: Peekaboo first.)

Publications list (`0c_publications.tex`): Peekaboo arXiv 2022 (Burgert, Ranasinghe, Li, Ryoo); Diffusion Illusions SIGGRAPH 2024 (Burgert, Li, Leite, Ranasinghe, Ryoo); MAGICK CVPR 2024 (Burgert, Price, Kuen, Li, Ryoo; Adobe); GWTF CVPR 2025 Oral (Burgert, Xu, Xian, et al.); MotionV2V CVPR 2026 (Burgert, Herrmann, Cole, Ryoo, Wadhwa, Voynov, Ruiz; Google).

### 2.1 Peekaboo (arXiv Nov 2022, arXiv 2211.13224; Ch3)
- Axis: SPATIAL SEMANTICS (what is where / foreground vs background). Ryan: "Where I learned to harness diffusion models."
- Problem: referring / zero-shot segmentation from a text-to-image model that never saw localization labels.
- Trick: optimize an alpha mask by score distillation loss. Composite the text-described foreground over a randomized background, ask the frozen diffusion model to "score" it. Segmentation framed as generation of the alpha mask. Intro: "This was the first demonstration that text-to-image diffusion models can be repurposed for discriminative vision tasks, and established score distillation as a general-purpose tool for extracting structure from frozen generative models." Black-box noise predictor, no attention surgery, no retraining. Ryan calls SDS "dream loss".
- Headline results: Pascal VOC (unsupervised semantic seg.) and RefCOCO (referring seg.). RefCOCO table: Random mIoU .102, GroupViT .112, LSeg .235 (trained for seg.), Peekaboo Depth Bilateral .204, RGB Bilateral .163. Beats GroupViT (trained on 16 V100s for 2 days) with zero segmentation training; loses to LSeg, which was trained for segmentation. Also a first attempt at generating RGBA (transparency) from an RGB-only model. Be honest: the numbers are "competitive", not SOTA.
- Best figures (all in `1_Peekaboo/figures/`):
  - `/Users/rburgert/Documents/ThesisProposal/source/src/1_Peekaboo/figures/intro1.png` and `intro2.png` (intro teaser pair)
  - `.../1_Peekaboo/figures/vis/vis_cocoref.png` (RefCOCO qualitative grid) and `.../vis/baby.png`, `brown_cow.png`, `elephant_on_right.png`, `guy_in_red.png`, `red_jacket.png`, `the_front_horse.png` (referring examples)
  - `.../1_Peekaboo/figures/iterdiagram.pdf` and `Newdia.pdf` (method diagrams)
  - `.../1_Peekaboo/figures/PeekabooGenerativeTimeline.png` (generative timeline)
  - `.../1_Peekaboo/figures/MoreRGBAExamples.pdf` and `AlphaRegFries.pdf` (RGBA/alpha examples; bridge to MAGICK)
  - `.../1_Peekaboo/figures/vis_appendix/bilateral_overlay_timelapse.jpg` (optimization timelapse)
- Note: no `figures/` caveat. This chapter's dir is `figures/` (the others use `figs`, `fig`, or the chapter root).

### 2.2 Diffusion Illusions (SIGGRAPH 2024; arXiv 2312.03817, Dec 2023; CVPR 2023 Demo Award; Ch4)
- Axis: MULTI-VIEW GEOMETRY. Ryan: control "not just the picture but the ANGLE at which you view it and what you see from that angle." The dog that is a skull/sloth depending on viewpoint.
- Problem: generate optical illusions automatically. Prior art required "immense time and skill." No formal definition or general framework existed.
- Trick: optimize a group of "prime images" (parametrized by Fourier feature networks) so that differentiable transformations ("arrangements": flip, rotate, overlay, stack, hinged "mechanical squares") each produce a derived image matching a different prompt. Reuses SDS from Peekaboo plus a new "dream target loss". Same machinery as Peekaboo, different application.
- Headline: "first formalized, generic framework"; physically fabricated and photographed in the real world (real printed illusions). Example: four playground images that stack to a QR code. Three types: Flip Illusions, Rotation Overlay Illusions, Hidden Overlay Illusions. Quantitative: CLIP score, aesthetics, Vendi diversity, LLaVA controllability vs baselines (figs `final-*.png`).
- Best figures (in `2_DiffIllusions/figs/`):
  - `/Users/rburgert/Documents/ThesisProposal/source/src/2_DiffIllusions/figs/AlignedTeaser_Compressed-crop.pdf` (teaser, photographs of fabricated illusions; BEST single slide)
  - `.../2_DiffIllusions/figs/fig1.jpg` (paper hero figure)
  - `.../2_DiffIllusions/figs/architecture.v3.drawio.pdf` (method)
  - `.../2_DiffIllusions/figs/RotationPhoto.pdf`, `rotGal.pdf` / `RotGal.pdf`, `FlipGallery.pdf`, `hiddenGal.pdf` (galleries)
  - `.../2_DiffIllusions/figs/overlaydiagram.jpg`, `rearrangeFlipIllusion.pdf`, `approaching_dreams.png`, `sis_large_demo.jpg`, `website_figure_compressed.jpg`

### 2.3 MAGICK (CVPR 2024; with Adobe Research; Ch5)
- Axis: TRANSPARENCY (alpha / RGBA). Ryan: "Bootstrapping a diffusion model to do something new." "Lavishly simple trick": ask the model for a dog on a green screen, and "somehow that fucking works" (his words in the manifest notes; clean before putting on slides).
- Problem: no large alpha-matte data, so no way to train models that generate or condition on accurate alpha. Intro: "the largest existing matting dataset before our work contained only 726 objects" (alphamatting.com 27, DIM 431, Semantic Matting 726).
- Trick: generate objects on solid-color backgrounds and chroma-key them. (1) pick the background color least present in the object (generate sample first); (2) two-stage generation: DeepFloyd for clean solid backgrounds, then SDEdit img2img with SDXL for foreground detail; (3) combine chroma and deep keyers/segmenters to extract alpha.
- Headline: 150,000 captioned RGBA images at 1024x1024 ("over 140,000" on HF/GitHub). Demo: ControlNet fine-tuned on MAGICK for alpha-to-RGB generation; user study (52 participants) prefers it 0.82 vs 0.16 (vs Canny SD1.5) and 0.77 vs 0.23 (vs Sketch SD1.5). Paper's own line: the 1,400 matted images in the PDF exceed the previous largest matting set (726).
- Best figures (in `3_MAGICK/figs/`):
  - `/Users/rburgert/Documents/ThesisProposal/source/src/3_MAGICK/figs/PipelineOverview.png` (pipeline)
  - `.../3_MAGICK/figs/alpha2rgb.png` and `alpha2rgbResults.png` (alpha-conditioned generation vs ControlNet)
  - `.../3_MAGICK/figs/GreenOnGreenBadGreenOnBlueGood.png` (why background color matters)
  - `.../3_MAGICK/figs/fig1.jpg`, `ddpack0..3_q90.jpg` (also `.../3_MAGICK/ddpack0_q90.jpg`), `.../3_MAGICK/full_512.jpg` (dataset mosaic)
  - `.../3_MAGICK/figs/BeforeAfterImg2Img.pdf` (two-stage fix), `.../3_MAGICK/figs/priorcomparison.png`, `.../3_MAGICK/survey.png`

### 2.4 Go-with-the-Flow (CVPR 2025 ORAL; arXiv 2501.08331; Eyeline Labs/Netflix; Ch6)
- Axis: TEMPORAL MOTION (how things move, in generation from scratch). Ryan: control "how we want things to move, not just how they look." Also a motion illusion (content visible only while moving; the "Rick Roll that disappears when paused").
- Problem: motion control in video diffusion existed but needed architecture changes, parameterized signals (camera params), or per-application designs.
- Trick: warp the noise. Replace temporal-i.i.d. Gaussian noise with noise warped along optical flow (spatially still Gaussian, temporally correlated) via a new, faster-than-real-time algorithm (HIWYN was quadratic in frames). "Our approach requires only a change in data": pre-process training videos into warped noise, then fine-tune any video diffusion model as a black box (CogVideoX-5B T2V and I2V, 4M videos). Escher epigraph: "We adore chaos because we love to produce order." Intro framing: "producing order from chaos... proactively introducing partial order into the chaos of latent space sampling." Surprise: "removing temporal Gaussianity from the noise distribution does not deteriorate model fine-tuning."
- Headline: one-stop solution for (1) local object motion, (2) camera motion, (3) motion transfer; wins user studies on quality, motion control, text alignment, temporal consistency. Impact is the headline (see section 4): CVPR Oral (95 of 13,008 submissions), ~1.1k GitHub stars, 117+ citations.
- Best figures (in `4_GWTF/fig/`; note dir is `fig`):
  - `/Users/rburgert/Documents/ThesisProposal/source/src/4_GWTF/fig/Teaser.pdf` (teaser: object motion, camera motion, transfer)
  - `.../4_GWTF/fig/framework_diagram.png` (3-component pipeline)
  - `.../4_GWTF/fig/algo_diagram_2_layers.png` (noise-warping expansion/contraction)
  - `.../4_GWTF/fig/degradation_comparison.png` (noise degradation gamma knob 0.5-0.7)
  - `.../4_GWTF/fig/comparisons_video_diffusion_object_motions_new_compressed.pdf`, `comparisons_davis_i2v_new_compressed.pdf` (comparisons)
  - `.../4_GWTF/fig/wonderjourney_comparison.png`, `depthwarp.jpg`, `windmills.pdf`, `AnimateDiffAnimation.pdf`, `naz_diffrelight_grid11.jpg` (applications)

### 2.5 MotionV2V (CVPR 2026, standard poster; arXiv 2511.20640; with Google; Ch7)
- Axis: VIDEO EDITING (change motion of an EXISTING video, keep content). Ryan: "Most recent work"; "Not only controls motion but TRANSFERS content from one video to another"; "editing is harder than generation because you must adhere to the original video's content."
- Problem (intro hook): "Consider filming a climactic race between two dogs: your Corgi and a friend's Bichon. The original video sees the Bichon take the win... does the technology exist to modify this video such that your Corgi is victorious?" Prior I2V methods (ReVideo, GWTF) use only the first frame, so regions not in frame 1 are hallucinated; human-specific methods (MotionFollower, MotionEditor); camera-only (ReCapture, ReCamMaster). VFX answer today: reshoot, retiming, plate stitching, CGI.
- Trick: define a "motion edit" = delta between input and target sparse point trajectories. Train on synthetic "motion counterfactuals": video pairs with identical content but different motion, generated programmatically from real videos. Architecture: a T2V DiT with a control branch (duplicates first 18 transformer blocks) conditioned on counterfactual video + counterfactual tracks + target tracks. Edits can start at any timestamp, no masks, any object, successive edits possible.
- Headline: 4-way user study, 41 participants. Win rates Ours 70/71/69% (content/motion/overall) vs ATI ~24-25%, ReVideo 1-2%, GWTF 3-5%. Abstract: "over 65% preference". Claim scoped to "first video-to-video, general-object motion editor" (a bare "first" is refuted; see section 4).
- Best figures (in chapter ROOT, no figures/ subdir): 
  - `/Users/rburgert/Documents/ThesisProposal/source/src/5_MotionV2V/teaserv2.png` (teaser: input, source and target tracks, output)
  - `.../5_MotionV2V/three_strips_v2.jpg` (capabilities)
  - `.../5_MotionV2V/datagen.pdf` (counterfactual data generation)
  - `.../5_MotionV2V/architecturestacked.pdf` (architecture)
  - `.../5_MotionV2V/megacomparisonfigurev2.jpg` and `aticomparisonmegaphoneversion4.jpg` (comparisons)
  - `.../5_MotionV2V/successive_edit_horz.pdf` (successive edits), `editor_gui.jpg` (drag-point UI), `TestPrep.png`, `JitterFigure.pdf`, `UserStudyInterface.png`

---

## 3. Intro/motivation claims and future work

Intro motivating examples (from `1_introduction.tex`), good for a "why control" slide:
- "A graphic designer inserting an object into a composite needs accurate alpha boundaries, not a binary cutout." (MAGICK)
- "A visual effects artist editing a video needs to change how a character moves without regenerating the entire scene." (MotionV2V)
- "A researcher studying visual perception needs to construct precise optical illusions, not approximate ones." (Diffusion Illusions)
- Organization section maps Ch2 Literature, Ch3-7 papers, Ch8 Future Work. Ch8 is described as "3D generation, interactive editing, and unified spatial-temporal control frameworks" in intro, but the actual Future Work text is different (below). Mismatch to fix or avoid on slides.
- Lit review framing (`2_literature.tex`): "most control methods address either spatial or temporal domains but not both, and the field lacks a unified perspective on how different control mechanisms relate to one another." Pipeline of control: SDS (steer frozen models in arbitrary parameter spaces), ControlNet-style adapters, then video, where "controlling that motion remained largely unsolved."

Future work (actual text in `8_future_work.tex`, Section "Future Work", Ryan's note: "In the future, I'll be working on video editing tasks - such as proof that an image-to-image general editor can be turned into a video-to-video general editor (like nanobanana but for video)"):
- "I want to push this line of work from controlling video generation to controlling video editing in general."
- Image side exists (Nano Banana = Gemini 2.5 Flash Image: image + instruction -> targeted edit). "Nothing like that really exists for video yet; editing a clip still mostly means regenerating it, which throws away the temporal coherence and detail of the original."
- Goal: "what I want to prove is that you can turn a general image-to-image editor into a general video-to-video editor, basically Nano Banana but for video, that handles any edit, appearance, motion, or both, without disturbing what you did not ask it to change." MotionV2V "is an early step toward this for the specific case of motion."
- Only one future-work direction is written. The intro's "3D generation / interactive editing / unified spatial-temporal control" is not in the text.

---

## 4. Impact numbers (from `impact_verified.md`, mid-2026 frenzies, plus later updates in `claude_instructions.md` dated Aug 2026; prefer the later numbers)

Use the verified figures; the intro paragraph in `1_introduction.tex` has several STALE numbers (flagged below).

- Peekaboo: ~41 citations (Semantic Scholar). Cited by "Your Diffusion Model is Secretly a Zero-Shot Classifier" (CMU, ICCV 2023, 355 cites; bib-only citation, so say "cited by", not "inspired"). Confirmed citers: DiffCut, FreeSeg-Diff (benchmarks against Peekaboo), SLiMe, SATR. DGMO (Interspeech 2025) ports it to audio source separation. 31 GitHub stars. Venue precisely: O-DRUM workshop at CVPR 2023, plus arXiv Nov 2022. ODISE and DiffuMask do NOT cite it. INTRO CLAIM "over 40 follow-on papers at venues including CVPR, ICCV, ECCV, and NeurIPS" is NOT verified; the verified count is ~41 total citations, not 40 follow-ons.
- Diffusion Illusions: ~26 (S2) / 28 (Scholar) citations. CVPR 2023 Best Demo Award (verified; official awards page). Steve Mould video (Sep 14 2024) and Matt Parker / Stand Up Maths video (Sep 14 2024), both real. Cited by Visual Anagrams (CVPR 2024 Oral; near-simultaneous sibling), Factorized Diffusion (ECCV 2024; the CVPR 2024 "Seattle skyline -> CVPR" shirt, >10k shirts, NOT 2025), LookingGlass (CVPR 2025 Oral, Disney Research), Illusion3D (arXiv 2024 + CVPR 2025 Art Gallery; not SIGGRAPH). Soften claim to "among the first / helped establish an active line of research."
- MAGICK: ~20 citations (Scholar). HF downloads: 158,640 all-time / 3,773 per month (Aug 2026; earlier measure 6,448/month; the intro's "over 3,000 times per month" is consistent with the Aug figure). ~11 GitHub stars. "Largest PUBLIC general-domain RGBA dataset" holds (LayerDiffuse's 1M never released; "public" is load-bearing). 5 papers materially use it: Trans-Adapter (ICCV 2025), TKG-DM (CVPR 2025 Highlight, 3,000 MAGICK images), PrismLayers, LayeringDiff, PSDiffusion (WACV 2026). No awards or press; standard CVPR poster.
- Go-with-the-Flow: 117 citations (Semantic Scholar, 22 influential) / 120 Scholar (Aug 2026). STALE in intro: "62 citations". 1,081-1,090 GitHub stars (README says 1.1k; "over 1,100" in intro is slightly high, say "~1.1k"). CVPR 2025 Oral: 95 orals of 13,008 submissions (0.73% of submissions; 3.3% of accepted; be precise). Ecosystem: AnimateDiff and HunyuanVideo ports by spacepxl (HF), kijai's ComfyUI-VideoNoiseWarp (162 stars), ZeptaFrame. Load-bearing renderer in WonderPlay (ICCV 2025 Highlight), NewtonGen (ICLR'26), VideoFrom3D, VLIPP, PSIVG. Warped-noise follow-ups: EquiVDM (NVIDIA, theory), CameraNoise (ICML'26, 3D camera), HumANDiff, UniCaMo, Phi-Noise. Yosun Chang's "AI3D Render" won CVPR 2025 Best Demo Honorable Mention. Caveats: MotionMatcher does NOT use GWTF; no Wan/LTX/Mochi ports; both README HF demo Spaces broken (as of Aug 2026); Virtually Being is Ryan's own group (not external adoption).
- MotionV2V: CVPR 2026 poster (pp. 35988-35997). 11 citers (Aug 2026), NONE substantially built on it (all positioning cites). ~54-58 GitHub stars (intro says 54, latest 58) but the repo is a project page: NO CODE OR WEIGHTS RELEASED (issues requesting code are unanswered). "First video-to-video general-object motion editor" holds (Lee et al. CVPR 2026 independently converged; Point-to-Point does the inverse task). "Motion counterfactuals" coinage not yet adopted. TrajectoryMover is NOT an end-to-end MotionV2V citer.
- Honest framing for slides: strongest verified external impact = GWTF (oral, 117 cites, 6 papers using it as renderer, community ports) and Diffusion Illusions (demo award, YouTube coverage, 6+ illusion follow-ups). MAGICK = dataset adopted in the transparent-generation niche. Peekaboo = early, modestly cited, cross-domain. MotionV2V = too new, no code.

---

## 5. Connective thread: how each paper hands off to the next

(Intro states several of these explicitly; others inferred from Ryan's notes. "Source" marks which.)

1. Peekaboo -> Diffusion Illusions. Peekaboo showed a frozen text-to-image model, used as a black-box noise predictor with SDS, can be steered in a non-pixel parameter space (an alpha mask). Limit: one image, one prompt, one view. Handoff: same SDS plus differentiable parametrization, now optimizing several images jointly under geometric transformations, so one object has multiple readings (angle = control axis). (Source: abstract "Building on the same score distillation and image parametrization as Peekaboo"; intro "Building on the same score distillation framework, we extend control from single-image semantics to multi-view geometric structure." Note: 13 months apart, say "subsequently reused" not "immediately".)
2. Peekaboo (and DI) -> MAGICK. Peekaboo's masks "lack fine detail" (intro: "While Peekaboo showed that diffusion models can segment objects, the resulting alpha masks lack fine detail"). Optimization per-image is slow and imprecise, and training models for transparency needs scale data that doesn't exist (726 objects max). Handoff: stop optimizing per image; instead bootstrap a dataset from the model (green screen + chroma key), then train alpha-conditioned generation. Ryan: "The alpha rasterization trick actually connects to MAGICK later." Control axis moves from "extract structure at inference" to "train new conditioning from synthetic data".
3. MAGICK -> Go-with-the-Flow. Spatial control (where, what, how transparent) is solved per image; but video diffusion models then arrive and text can't specify motion, so "Moving from spatial to temporal control." Handoff: instead of data engineering for a conditioning channel, inject structure into the one thing every diffusion model consumes, the noise (warped by optical flow), with no architecture changes. Both are "change the data, not the model" style moves. Ryan's tie-in: GWTF also has an illusion application (visible only in motion), echoing DI.
4. Go-with-the-Flow -> MotionV2V. GWTF controls motion during generation from scratch. Intro: "While Go-with-the-Flow controls motion during generation from scratch, MotionV2V modifies object and camera trajectories in a given video while preserving its visual content." Limits GWTF/I2V methods share (MotionV2V intro): conditioned on a single first frame, so unseen regions are hallucinated, not preserved. Handoff: editing an existing video breaks the structural correspondence between input and output, so DDIM inversion and standard editing fail. Fix = train on synthetic motion counterfactual pairs. GWTF appears as a baseline MotionV2V beats (3-5% preference), not as a building block.
5. MotionV2V -> Future work. Motion editing is one special case of general video editing. Next: turn a general image-to-image editor (Nano Banana-style) into a general video-to-video editor (appearance, motion, or both).

Arc in one line for the opening slide: where things are (Peekaboo) -> from which angle you see them (Diffusion Illusions) -> how transparent they are (MAGICK) -> how they move (GWTF) -> changing how they move in a video that already exists (MotionV2V) -> any edit to any video (future).

Also useful for the committee: methods ladder from "no training" (Peekaboo, DI: inference-time optimization) to "synthetic data + fine-tune" (MAGICK) to "change the noise distribution, fine-tune black-box" (GWTF) to "full counterfactual training with control branch" (MotionV2V). Each rung spends more training to buy more control, ending at editing real videos.

## 6. Loose ends / risks to flag before tomorrow
- `claude_instructions.md` is stale in places: says abstract/intro/Ch8 are placeholders; title page says "Creative Applications of Diffusion Models" (actual `0a_title_page.tex` says "How to Control Your Diffusion Model").
- Intro `1_introduction.tex` impact paragraph has stale/unverified numbers (Peekaboo "over 40 follow-on papers", GWTF "62 citations", MotionV2V "54 stars" and no mention that no code is released).
- Intro says Ch8 covers "3D generation, interactive editing, and unified spatial-temporal control"; actual Future Work covers only video editing (Nano-Banana-for-video). Pick one story for the talk.
- Peekaboo is arXiv-only (workshop at CVPR 2023); do not label it "CVPR 2023" main track.
- Ryan's quote that includes profanity is from manifest notes, not the thesis; sanitize for slides.
- MotionV2V is the least proven: no released code, ~11 citations, "first" must be scoped.

---

## 7. Addendum: Ryan's talk outline (presentation/scrapnotes.txt) vs. what is in the thesis

Ryan's outline (verbatim fragments): title "How to Control your Video Diffusion Model" (thesis says "How to Control Your Diffusion Model", no "Video"). Index: "5 Main Papers" / "Impact of each 'This is part where I boast'" / "Ziyu, Vista4D, Koichi: 3 Extra Papers" / "Proposed next project: LoraPlexer + Vid2Vid Editing". Opener: "BANG BANG BANG [cool things - unexplained - warped noise rickroll, diffusion illusions, MAGICK (how to make an RGBA dataset from an RGB model alone)]". Also "Try to tie them into one question", "Intro: How to tie it together?", "Peekaboo with Diffilu: AIM FOR FLOW", live MAGICK demo ("let's do a user study right now lol [show before/after MAGICK's]"), live noise warp demo, extras (Triton + ducks photos, 3D warped noise, high-school project, unrelated papers).

### In the thesis vs NOT in the thesis
- Ziyu's paper, Vista4D, Koichi's paper: NOT in the thesis at all (grep of all source/src, manifest, concerns, impact files finds none). No chapter, no mention in intro/publications/future work. The thesis has exactly the 5 first-author papers. The only adjacent mention: "Virtually Being" (SIGGRAPH Asia 2025, fine-tunes the GWTF checkpoint, Burgert co-author) appears in `8_future_work.tex` comments and `impact_verified.md`/`claude_instructions.md` as an own-group paper that must NOT be counted as external GWTF adoption. Likely candidate to be one of the "extra papers" but Ryan's notes never name it. Extra-papers slides must be sourced from Ryan, not from the thesis. (TRITON, CoRL 2023, appears only in `/Users/rburgert/Documents/ThesisProposal/impact.md` sec 6 as an unrelated earlier paper: "limited" impact, superseded by Gaussian splatting/diffusion; it matches Ryan's "Triton pictures" extra, not a thesis chapter.)
- LoraPlexer, I2I2V2V: NOT in the thesis. Zero hits. The thesis's only future-work direction (`8_future_work.tex`) is "turn a general image-to-image editor into a general video-to-video editor, basically Nano Banana but for video". That is the same idea as the notes' "Vid2Vid Editing / I2I2V2V" (image-to-image-to-video-to-video), so the talk can present I2I2V2V as the concrete version of the thesis's future work. LoraPlexer's listed ingredients in the notes (3D view change from synthetic + lighting changes, multi-distillation, MAGICK, multi-noise-levels, CFG with/without model, demo: To-Edges LoRA + 2-bit color LoRA on his dog) have no thesis counterpart; "MAGICK" as part of the next project is a nice call-back (data bootstrapped from the model itself).
- Thesis intro claims future work on "3D generation, interactive editing, and unified spatial-temporal control" but Ch8 text only has the video-editing item. Notes' "3D Warped Noise" extra maps to CameraNoise/HumANDiff (others' 3D warped-noise follow-ups, see section 4), not to a thesis chapter.
- "Warped noise rickroll" opener and "things visible only when they move" ARE in the thesis (intro, GWTF: "content that is visible only during motion and vanishes when the video is paused").

### Diffusion Illusions follow-ups / awards / Steve Mould (as written in `8_future_work.tex` Research Impact chapter, Ryan's own prose, lines ~32-68)
- Ryan's voice: "Diffusion Illusions was one of the most well known works in my thesis. It was built on the technological foundations of Peekaboo: it parametrized images with Fourier feature networks, and used score distillation loss to optimize them. But it had a different goal, which was to create optical illusions, some of which humans would have little hope of designing by hand. In particular, the overlay illusions, which reveal hidden images when superimposed on each other and rotated, would be monstrously difficult for a human artist."
- "Diffusion Illusions ended up triggering its own small subfield of research... every one of the papers in this paragraph was directly inspired by and builds on our work." (Verified status: soften to "helped establish"; Visual Anagrams is a near-simultaneous sibling that cites DI.)
- Follow-ups listed in thesis: Visual Anagrams (CVPR 2024 Oral; invertible orthogonal transforms: rotations, puzzles with multiple solutions, color inversions); Factorized Diffusion (frequency-decomposed hybrid images; "used on the back of the official shirts for CVPR 2024"); PTDiffusion (training-free phase transfer; cliff face that is also a human face); Illusion3D and LookingGlass (CVPR 2025 Oral; 3D illusions via differentiable rendering: lenses/mirrors on one subject, e.g. a castle, reveal a hidden subject, e.g. a lion). Also: DI used "as a benchmark for SDS-alternative algorithms (mcallister2024sdsbridge), instead of just 3D reconstruction."
- Awards/media: "Best Demo Award at CVPR 2023" (verified, 2023 not 2024); SIGGRAPH 2024 paper, "presented, and given a demo session at SIGGRAPH 2024"; "two videos by the science-communication YouTubers Steve Mould and Matt Parker, amassing over a million views" (both videos Sep 14 2024; Parker's description cites the paper and all 5 authors; the intro's phrase "Stand Up Maths" = Matt Parker's channel; "over a million views" is Ryan's number; impact_verified.md verified that the videos exist but its listed claims do not independently confirm the view count, so check YouTube counts before saying "millions" on a slide). Note scrapnotes: 'SECTIONS: "Not Good, Didn't Like It" well, other people did' = rebuttal-slide idea (reviewers' pushback vs. later adoption); 'The awards that were won from Diffilu followups' = the Factorized Diffusion CVPR 2024 shirt, Visual Anagrams CVPR 2024 Oral, LookingGlass CVPR 2025 Oral.
- Slide-ready facts: Diffusion Illusions printouts for the live demo are on Ryan's gather list; best photos-of-fabricated-illusions figure = `/Users/rburgert/Documents/ThesisProposal/source/src/2_DiffIllusions/figs/AlignedTeaser_Compressed-crop.pdf`; Ryan's own SIGGRAPH deck at `/Users/ryan/DiffiluVideos/DiffiluSigPresent.pptx` and poster `/Users/ryan/CleanCode/Projects/Peekaboo/DiffusionIllusions/SIGGRAPH_DiffiluPoster.pptx` (paths from notes, not verified to exist on this machine).

### CORRECTIONS to sections above
- Section 4 note that the Research Impact chapter is wholly "Claude's orange rough draft" is only partly true: the Diffusion Illusions section (lines ~32-68) is already in Ryan's voice (plain text, not `\AI{}`), with older AI drafts commented out. Peekaboo section is a mix (AI text over Ryan notes).
- Intro paragraph's "Stand Up Maths" = Matt Parker.
