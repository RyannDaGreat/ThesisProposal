# Diffusion Illusions: talk section

Machine-readable spec (the source of truth for slides and full speech): `presentation/agents/specs/diffillusions.json`. 6 slides (one of them a build), 638 spoken words (about 4.7 min).

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

## Likely committee questions
- **Why not optimize pixels directly?** Pixel optimization hides each view's content in high-frequency patterns, which needs pixel-perfect alignment and breaks when printed. A Fourier feature network biases the primes toward printable frequencies. (Slide 3)
- **Do you backprop through the diffusion model?** No. SDS skips the U-Net Jacobian: (predicted − true noise) is used directly as the gradient on the derived image, then backpropped through the arrangement and the FFN. (Slide 3)
- **Why is multiplication a valid model of overlays?** Each transparency multiplies the transmitted light per channel. It commutes, so stack order doesn't matter. Output is scaled and tanh-normalized to keep dynamic range. The real prints show color shifts. (Slide 4, plus the limits on slide 6)
- **What do dream targets add over SDS?** SDS gradients are high-variance, so the images come out gritty. SDEdit targets give a cleaner regression signal. In the eval, method C (500 SDS steps, then 8 dream-target rounds) is best on aesthetics, and C/D are highest on the independence score. (Slide 5)
- **Quantitative evidence?** Hidden overlays, 19 PASCAL VOC subjects × 4 styles, against a baseline that runs SDXL score distillation on each image independently, with the same 15-minute budget on one A100. Ours beats it on CLIP similarity, aesthetics and independence, and loses on Vendi diversity (more constraints). The thesis reports this as score-distribution plots, not a single table of numbers, so there are no headline numbers to quote. (Slide 6)
- **What is the independence score?** A new metric: each derived image should match its own prompt AND not match the other prompts. (Slide 6, verbal)
- **How does this relate to Visual Anagrams?** Visual Anagrams (Geng et al., CVPR 2024) came out about the same time and says it was inspired by Diffusion Illusions. It handles single-image views (flips, permutations) by denoising directly, which is faster. It has no multi-prime overlays and no fabrication. (Slide 6)
- **Failure modes?** The hidden 5th image is hard to recognize, turns black, or leaks visibly into the primes. Biases from Stable Diffusion's training data carry over. (Slide 6)
- **Why so slow?** It is per-illusion optimization at inference time, with no amortized generator. Contemporary work has reduced this. (Slide 6)

## Uncertain / unverified
- The exact prompts for the three images in `diffilu_hook1.mov` are unknown, so the speech does not name them.
- The thesis gives no headline numbers for the evaluation (plots only), so none were invented. The sample count (N=64 in my earlier notes) is unconfirmed and left out of the speech.
- "Over a million views" for the YouTube videos is unverified and left out.
