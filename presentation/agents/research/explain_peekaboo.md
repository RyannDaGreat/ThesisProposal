# Peekaboo: explanation + slide spec

Machine-readable spec (layout + full speech): `presentation/agents/specs/peekaboo.json`. 7 slides (3 are one build), 650 spoken words.

## Plain explanation

Problem: segment "the thing the words describe" in a photo (e.g. "Harry Potter" in a photo with Hermione) without training any segmentation model. Peekaboo uses Stable Diffusion frozen, as downloaded.

Key idea: if you cut Harry out and paste him on any solid-color background, it is still a picture of Harry Potter. So the right mask is the one where every random-background composite still looks like "Harry Potter" to the diffusion model.

How it works, step by step:
1. A learnable mask alpha starts as noise.
2. Each step, blend the photo over a random solid color: composite = alpha * photo + (1 - alpha) * color.
3. Push the composite through score distillation (the DreamFusion loss, in latent space) with the prompt. The gradient goes only into alpha; Stable Diffusion never changes.
4. Alone, this keeps everything (the full photo is a fine "Harry Potter" picture). So add an alpha penalty (sum of alpha, coefficient 0.05): every kept pixel costs something. Pixels relevant to the prompt get strong gradients and stay; irrelevant ones get pulled to 0.
5. Pixel-wise masks come out chopped up, so alpha is parametrized through a bilateral filter guided by the photo's colors: similar colors get similar alpha, mask edges snap to image edges.
6. About 200 SGD steps per image.

Results: RefCOCO mIoU 0.204 (depth-bilateral) vs GroupViT 0.112 (trained 2 days on 16 V100s), LSeg 0.235 (trained for segmentation) still beats it. It "localizes the essence": "Emma Watson" grabs face and hair, not the dress. Making the RGB image learnable too generates transparent RGBA images from noise (first attempt at RGBA from an RGB-only model). Limits: hallucinates object shapes from background texture (worse with one-word prompts), sometimes adds extra parts, center bias from SD's training data.

## Beats
1. Problem: text-prompted mask, zero training, frozen SD.
2. Intuition: the background doesn't matter.
3. Mechanism (build of 3): optimize mask with SDS -> keeps everything -> + alpha penalty -> chopped shirt -> + bilateral filter.
4. What it finds (essence) + honest numbers and limits.
5. Bonus RGBA + impact + handoff.

## Slides (assets in presentation/agents/.scratchpad/explain_peekaboo/final/)

1. **Peekaboo**: `harry_input.png` (Hermione + Harry photo, 512x512) centered; red text "Harry Potter". Problem statement.
2. **Still Harry Potter**: input small at left, arrow, five composites of Harry alone on red / green / black / white / blue (`harry_composite_163..167.png`); red line "...the background doesn't matter."
3. **Let's optimize it!** (build 1/3): `vid_fourier_no_gravity.mp4` full width (1792x286 strip: Input Image | Alpha Map | Background #1-5; prompt line on top). Alpha starts as noise and ends keeping nearly everything, including Hermione.
4. Build 2/3: `vid_fourier_with_gravity.mp4` + red "+ alpha penalty". Hermione and background drop out; shirt gets chopped up.
5. Build 3/3: `vid_raster_bilateral.mp4` + red "+ bilateral filter". Clean Harry mask.
6. **Finds the essence**: `emma_watson_essence.png` (thesis vis_appendix/ew_01.png, 3x LANCZOS upscale): red outline around Emma Watson's face/hair only, Harry Styles beside her, caption "Emma Watson".
7. **Bonus: transparency**: `rgba_generation_timeline.png` (thesis PeekabooGenerativeTimeline.png): 4 rows noise -> avocado armchair / globe / Pikachu / cat in a box on checkerboard. Impact (~41 citations, CVPR 2023 O-DRUM workshop, cited by "Your Diffusion Model is Secretly a Zero-Shot Classifier") spoken only. Ends with handoff to Diffusion Illusions.

Full speech per slide is in the JSON.

## Sources and rationale
- Slides 2-5 reuse elements from Ryan's own Peekaboo explainer, `ref_pptx/Presentation_New.pptx` slides 141-151 (0-based): the Harry Potter photo, the random-color composites, and the three optimization videos (media21 "fourier_no_gravity", media22 "fourier", media20 "raster_bilateral"). Extracted with Python zipfile because deckcraft-cli refuses files over 2 GiB (this deck is 4.9 GB).
- Skipped the main architecture diagram (`Presentation_New` 152 / thesis Newdia): it carries equations and encoder boxes that would each need explaining; the build already shows the same pipeline with real data.
- Ryan's original slide used the alpha-penalty video with the line "better! but why is it chopping up his shirt?"; kept that beat in the speech.

## Likely committee questions
- **Why does the mask go to the object rather than to all ones?** Without a penalty it does stay near all ones (slide 3 shows it). The alpha penalty makes every kept pixel cost something, so only pixels whose removal hurts the SDS score survive (slides 3-4).
- **Why random solid backgrounds instead of one fixed color?** With one fixed color the mask could learn to use that color as part of the object. Random colors each step force the masked-in pixels alone to carry the prompt (slide 2, "background doesn't matter").
- **What exactly gets gradients? Is SD fine-tuned?** Only the mask parameters. SD (text encoder, VAE encoder, U-Net) is frozen. Loss = SDS (predicted noise minus true noise, latent space) + 0.05 * sum(alpha) (slides 3-4).
- **Numbers vs baselines?** RefCOCO mIoU: Peekaboo 0.204 (depth-bilateral) / 0.163 (RGB bilateral), GroupViT 0.112, LSeg 0.235, random 0.102. VOC-C: Peekaboo 0.551 / 0.520, GroupViT 0.578, Clippy 0.539, LSeg 0.678. So it beats GroupViT on referring segmentation but not on VOC-C, and it never beats LSeg, which trains for segmentation (slide 6 speech gives RefCOCO. Have VOC-C ready).
- **Cost?** 200 SGD steps (lr 1e-5) per image and prompt. Each step is one SD forward + backward, so it is much slower than a feed-forward segmenter (slide 5 says "two hundred steps").
- **Why the bilateral filter?** A per-pixel mask gets noisy and fragmented (the chopped shirt). Bilateral blur conditioned on image colors ties alpha to color-similar regions and aligns edges from early iterations. Ablation: raster 0.340 vs RGB bilateral 0.520 VOC-C mIoU; depth bilateral (MiDaS depth as the guide) 0.551 (slide 5).
- **Failure modes?** Hallucinates an object shape out of background texture (bird/cat/dog), especially with one-word prompts. Adds parts (a knife handle made from bread). Sometimes doesn't converge (eyes). Center bias inherited from SD's training images. Inherits SD's biases (slide 6 mentions the hallucination case).
- **"Essence": isn't that just a wrong segmentation?** It is a different definition: it finds the region the prompt depends on most, which can be smaller than the annotated object. That costs IoU on benchmarks that label the whole person (slide 6).
- **Relation to DreamFusion?** Same score distillation loss, adapted to the latent space and applied to a 2D mask instead of a NeRF (the primer, then slide 3).
- **Impact?** About 41 citations, CVPR 2023 O-DRUM workshop. Cited by "Your Diffusion Model is Secretly a Zero-Shot Classifier" (ICCV 2023). DGMO ported the idea to audio source separation. LayerDiffuse (2024) later trained RGBA generation directly (slide 7).

## Uncertainties
- The video strips have a burned-in prompt line "Harry Potter boy - daniel radcliffe - man with glasses", while Ryan's slides said prompt "Harry Potter". The speech reads out the real prompt. Could be cropped off with ffmpeg if Ryan prefers.
- The Harry composites and alpha are from Ryan's 2023 deck; I don't know which exact parametrization made them. The three videos are labeled by file name only (fourier_no_gravity, fourier, raster_bilateral). Calling the third "the bilateral filter fix" matches Ryan's own slide 149 ("solution: bilateral filtering").
- The thesis chapter says RGB Bilateral uses a raster mask (not the neural texture), and Ryan's old slides call alpha "a neural neural texture". The speech avoids the term.
- The GroupViT comparison holds on RefCOCO only. On VOC-C, GroupViT 0.578 beats Peekaboo 0.551, so the speech says "on referring segmentation".
