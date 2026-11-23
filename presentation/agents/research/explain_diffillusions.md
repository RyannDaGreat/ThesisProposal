# Diffusion Illusions: talk section

Machine-readable spec (the source of truth for slides and full speech): `presentation/agents/specs/diffillusions.json`. 8 slides, 647 spoken words. Round 3: rebuilt per r2 examiner (asymmetric flip hook, architecture diagram, formula, dream-target grid, baseline violin plot, sim-vs-print before awards).

## Plain explanation

An optical illusion like a flip picture is one physical object that looks like different things depending on how you look at it. Diffusion Illusions makes these automatically with a frozen text-to-image model and no training. The physical things you print are the **prime images**. A fixed, differentiable, physically real **arrangement** (leave it alone, rotate 180°, stack transparencies on a backlight) turns the primes into **derived images**, which are what the viewer sees, and each derived image gets its own prompt. Stacked transparencies are modeled by multiplying colors, because light passes through each sheet in turn (then scaled and tanh-normalized). Training has two phases. Phase 1 runs score distillation (DreamFusion's loss, the same one Peekaboo uses) on every derived image: add noise, let frozen Stable Diffusion predict it with that view's prompt, and use predicted minus actual noise as the gradient on that view. The gradients flow back through the arrangement into the shared primes, so one set of pixels gets pushed toward several prompts at once. Phase 2, **dream targets**: SDS images are noisy, so every so often each derived image is cleaned with SDEdit and the primes are regressed toward those cleaned targets (SSIM + L2). Primes are stored as Fourier feature networks rather than raw pixels, because raw pixels hide information in high frequencies that a printer destroys. Results: real printed flip, rotation-overlay and hidden-overlay illusions (four playground sheets that stack into a scannable QR code). Limits: slow, because it optimizes at inference time; printers shift colors; and the hidden 5th image sometimes turns black or shows through in the primes.

## Beats (in order)
1. Hook plus handoff from Peekaboo: same loss, now several images sharing pixels (video of spinning flip illusions).
2. Vocabulary from a real print: prime, arrangement, derived (dog/sloth photo).
3. Mechanism: score distillation on each view, gradients summed into one shared image (build: red arrows on the same photo). FFN detail.
4. Generalize the arrangement: overlays are color multiplication, which is differentiable (rotation overlay photos).
5. Push it further: hidden overlay to QR code; dream targets; printing.
6. Evidence, limits, impact, and the handoff to MAGICK.

## Slides (JSON has exact rects; full speech is in JSON)
| # | Title | Visual | Notes |
|---|---|---|---|
| 1 | Diffusion Illusions | `assets/videos/diffilu_hook1.mov` (1936x780, 9.25 s; three flip images rotating on a dark background, taken from DiffiluSigPresent slide 6, 0-based) | Opens from Peekaboo |
| 2 | One print, two pictures | `explain_diffillusions/crop_flip_photo.png`: photo of a printed page held in hands, dog right side up and sloth after a 180° rotation, with handwritten red labels. Cropped from thesis teaser `AlignedTeaser_Compressed-crop.pdf` (100 dpi render, display box 30,75,625,390 ×1.544) | Defines prime/arrangement/derived |
| 3 | But...how? | Same photo plus red text "Score distillation on EACH view, one shared image" and 2 red arrows | Build of slide 2 |
| 4 | Stack them | `crop_rotation_overlay.png`: base + rotator sheets, then "stack", then 4 photos at 0/90/180/270° labeled Cat/Man/Woman/Dog. Teaser box 668,40,1355,437 | Red line: light = multiply |
| 5 | Hidden overlays | `crop_hidden_qr_row.png`: 4 playground prints (p_i = d_i), a hand holding the stacked transparencies, and the scannable QR code d_5. Teaser box 20,970,2000,1380 | Dream targets + fabrication in speech |
| 6 | What became of it | Text only: grey reviewer quote, red "CVPR 2023 Best Demo Award", "Steve Mould and Matt Parker made videos about it" | Eval, limits, impact, MAGICK handoff |

Why these visuals: the teaser panels are **photos of real prints**, so they prove fabrication and teach the definitions at the same time. The SIGGRAPH deck's elements (sig_19 rotation diagram with green arrows, sig_21 puppies × = help!, sig_48 dream-target diagram) were viewed (renders in `explain_diffillusions/sig_*.png`). They are good alternatives, but they carry extra labels (prompt names, QR overlays, d_i/G(t,d) notation) that would cost words to explain. If Ryan wants a dream-target visual, crop `sig_48.png` (rows d_1..d_5 and their dream targets) and add it as a slide between 5 and 6.

Not used, on purpose: the SDS internals (noise → frozen model → predicted noise). They are assumed to be covered in the Peekaboo section. If Peekaboo does not cover them, reuse DiffiluSigPresent slides 29-37.

## Round-2 changes (graded against exam_diffillusions.json)
- The mechanism is now explicit on slide 3: encode into SD latent space, add noise, frozen U-Net predicts it, prediction error is the gradient on each view, backprop goes through the VAE encoder + arrangement + FFN (never the U-Net), and the per-view gradients sum on the shared primes. Only the primes are optimized.
- Arrangement definitions: slide 2 (identity/rot180, fixed + differentiable + physically doable), slide 4 (product, scaled by k and tanh), slide 5 (hidden: p_i = d_i, d_5 = product).
- Step counts match the paper: 500 SDS steps, then 8 dream-target rounds, each regressing for about 1000 steps toward an SDEdit target, with strength annealing 0.90 to 0.01 (strength "shrinking" in the speech).
- Evaluation is stated honestly: the baseline is unconstrained, independent SDXL; results are distribution plots only, with no tables and no Visual Anagrams comparison; and prompt/style matters more than the method variant.
- Limitations stated: slow, uncalibrated printer color shift, hidden image turning black.

## Likely committee questions (answer, and where it is covered)
- **Why not optimize pixels?** Pixel optimization hid views in high frequencies, which need pixel-perfect printing and alignment, and the physical prints broke. The FFN (an MLP from coordinates to RGB, per prime, 512x512, adapted from TRITON) is a smoothness prior. (Slide 3)
- **Backprop through the diffusion model? Through the VAE?** Not through the U-Net (DreamFusion drops its Jacobian), but yes through the VAE encoder, the arrangement and the FFN. SDS is a surrogate gradient, not a true loss. The paper uses an L1 noise residual normalized by timestep, which is a heuristic and not derived from a bound. Dream Target Loss, by contrast, is a well-defined regression (SSIM + MSE) toward a fixed target in each round. (Slide 3, details verbal)
- **Why multiplication, and what is k?** Transparencies multiply transmittance per channel, and multiplication commutes, so stack order doesn't matter. Products darken, so the result is scaled by k (2 for rotation, 3 for hidden) and passed through tanh, which models a brighter backlight. It is not calibrated to the printer; the paper's sim-vs-photo figures show color shifts. Measured ink transmission could be dropped into the arrangement op, since any differentiable arrangement works. (Slide 4, slide 6)
- **Does dream-target alternation converge? Does it drift?** There is no proof. Each round regresses to fixed targets for about 1000 steps, and the SDEdit strength anneals from 0.90 to 0.01, so the targets move less and less. It resembles alternating projection between "looks like the prompt" and "reachable by the arrangement". Evidence: the metrics rise monotonically with optimization time. Compromises (for example a hidden image that looks like "cow" instead of "bottle") are caught by low independence scores. w_5 = 3 prioritizes the hidden image. (Slide 5)
- **Baseline is a strawman? Why no Visual Anagrams?** Admit it: the baseline is SDXL generating each of the 5 targets independently with no constraint, so it measures what the illusion constraint costs, and it is not a competing method. Visual Anagrams is contemporary (it cites DI as inspiration) and handles only single-prime pixel-permutation views, so it cannot express multi-prime multiplicative overlays. There is no head-to-head comparison, even on flips. Every method got the same 15-minute budget on one A100. (Slide 6)
- **Evaluation details?** Hidden overlay, 4 styles x N=64 groups, each with 5 subjects drawn from 19 PASCAL VOC classes (person excluded). Metrics: CLIP cosine (controllability), Vendi with DINOv2/CLIP (diversity), LAION aesthetics, LLaVA-1.5, and the Independence Score. Distribution plots only, no significance tests. (Slide 6)
- **Independence score: saturating, gameable, validated?** It is the minimum diagonal entry of the row- and column-softmaxed 5x5 CLIP image-text matrix (tau = 0.05), so each image must match its own prompt better than the other four, and vice versa. It catches leakage that plain CLIP misses. Validation is qualitative only (ranked random examples), with no human study and CLIP's biases inherited. LLaVA was added as a second judge. (Slide 6)
- **What does the study say about your design choices?** C vs D: dream targets after SDS beat 4000 SDS steps alone on aesthetics. C vs B: weighting the hidden image 3x helps. C vs A: SDXL beats SD1.5. Rotation ablation: fewer derived images means better alignment. Differences between variants are modest next to style and prompt effects. (Slide 6 says "the prompt mattered most")
- **Why optimization when feed-forward samplers exist?** Optimization handles any differentiable arrangement, including multiplicative overlays across separate physical sheets, which noise-averaging samplers can't express. Speed is the main stated limitation. Thesis thread: frozen diffusion priors via score distillation over custom parameterizations (Peekaboo masks, FFN images). (Slides 1, 6)
- **Failure modes?** The hidden 5th image is hard to recognize, turns black, or shows through in the primes. SD/SDXL biases carry over. (Slide 6)

## Uncertain / unverified
- The prompts for the three images in `diffilu_hook1.mov` are unknown, so the speech doesn't name them.
- The evaluation has no headline numbers (plots only), so none are quoted.
- Checked in the source: N=64 groups (main_thesis.tex:252; the older main.tex:477 has an author comment "[xl: number by average, not true!]" next to it, so don't lean on N), the SDEdit strength schedule starting at 0.90 (X_suppl_thesis.tex:169), 500 SDS steps + 8 dream-target rounds, weights [1,1,1,1,3], the 15 min A100 budget, and the tanh scaling. Not re-checked: k=2/3 and the L1 residual, which come from the exam file.
- "Over a million views" is unverified and left out.

## Round-3 notes (r2 examiner)
- New visuals, all in `.scratchpad/explain_diffillusions/` and all checked in a render (`check/sheet.png`): `flip_giraffe*.png`/`flip_dogele*.png` (FlipGallery.pdf tiles, the second copy rotated 180), `arch.png` (architecture.v3.drawio.pdf), `hid_*.png` (teaser bottom row split into separate images, captions at 20 pt), `dreams_grid.png` (approaching_dreams.png without its legend), `base.png` (fig-overall-baseline.pdf, with our own 18 pt metric labels on top), `simreal.png` (SimRealHidAdjust.jpg without its tiny labels).
- Verified k: the commented-out table in figs/illusion_table.tex has `tanh(2 * p_1 * rot(p_2, 90j))` and `tanh(3 * p_1*p_2*p_3*p_4)`.
- **The baseline is unresolved. Ryan, check the code.** main_thesis.tex:279 calls it "vanilla SDXL ... independently for one step using score distillation loss". X_suppl_thesis.tex:258 says the baseline images are "heavily interfered with by others in the same group and the overlay image", which can't happen if the images were truly independent. The speech now says only "what the paper calls vanilla SDXL score distillation, read it as an ablation, not a rival method". It no longer claims the baseline is unconstrained.
- Step counts: method C in the eval is 500 SDS steps, then 8 dream-target rounds. The appendix pseudocode (X_suppl_thesis.tex:154, 171) shows `range(10000)` and a 90-step strength schedule from .90 to .01. If asked, the pseudocode is the general recipe and C is the evaluated budget. How the 8 rounds sample the .90 to .01 schedule is not stated.
- Dropped "the hidden image goes black" (it appears only in a commented-out line) and "the QR actually scans" (it isn't shown).
- Kept Ryan's reviewer joke. It now comes after the evidence and the limits.

## Final-round notes
- The Vendi plot on slide 7 is `vio_div_clip.png`. The raw eval data is not in the repo, so I couldn't re-run seaborn with cut=0. I cut the image at Vendi = 1, the metric's minimum, whitened everything below it, and closed each violin with a flat edge. If Ryan has the data, re-plot it with `cut=0`.
- Baseline speech now quotes the definition at main_thesis.tex:279 exactly ("vanilla SDXL ... independently for one step"). It drops "ablation", which the tex doesn't support. The independence contradiction with X_suppl_thesis.tex:258 is still open.
