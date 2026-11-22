# MAGICK — explanation, talk track, slide spec

Machine-readable spec: `presentation/agents/specs/magick.json` (6 slides, ~600 spoken words). All crops are in `presentation/agents/.scratchpad/explain_magick/crops/` and were made by `presentation/agents/.scratchpad/scratchpad_agent_3.py`.

## The paper in plain words

Diffusion models make RGB pictures. They can't make transparent cutouts with real alpha (the per-pixel see-through value), so hair, fur, smoke and glass come out as hard blobs. To train a model that does alpha you need lots of examples, but alpha is hard to get from real photos: the biggest matting dataset (Semantic Image Matting) has 726 objects, Adobe DIM has 431, alphamatting.com has 27. Segmentation datasets are big but their edges are hand-traced and hard.

MAGICK makes a 150,000-object RGBA dataset from RGB models alone. The idea is Hollywood's: ask the model for the object "isolated on a solid green background", then chroma key the screen out. Three problems and their fixes:
1. **Screen color.** A green object on green disappears. Generate the plain prompt once with SDXL, build a saturation-weighted hue histogram (Gaussian smoothed, sigma 10 degrees), pick the least-used named hue. Green or blue in over 90% of cases.
2. **Models can't make keyable screens.** SDXL/Midjourney/DALL-E give dark, gradient, or tinted screens; DeepFloyd gives flat screens but mushy edges. Fix: DeepFloyd image, cut out roughly with Photoshop Subject Select, paste onto a brighter saturated screen of the same hue, then SDXL img2img (SDEdit) at strength 0.95 with the screen color as a negative prompt. High strength repaints fine detail; the negative prompt removes color spill from the subject but can't touch the over-saturated screen.
3. **Keying is under-constrained.** Run three keyers that fail differently: a per-pixel color-difference keyer (Wright) with a per-pixel background estimated by deleting the foreground and inpainting (Telea) — this also gives decontaminated foreground colors; Adobe's internal learned chroma-key net; Photoshop Subject Select. Score = min over pairs of the mean MS-SSIM of the two cutouts composited on white and on black. Agreement means success. Median score 0.984; the top 50% (110k) are auto-accepted using the pixel-wise keyer; the other 40k (glass, water, smoke, fire) were chosen by humans in a web UI, one click among 7 alpha/foreground combinations (5 workers x 112 h, $0.30/sample).

Each sample: pure foreground colors F, alpha, caption, 1024 px. Prompts come from GPT-4/ChatGPT, procedural human templates, and an Adobe caption dataset with "clipping path"/"greenscreen" tags stripped.

Use: ControlNet (SD1.5) fine-tuned for alpha + prompt -> RGB. User study, 52 people, 27 alphamatting.com masks with GPT-4 prompts: preferred 82% vs SD1.5 Canny-edge ControlNet (16%), 77% vs Sketch-edge (23%). A MAGICK + DIM mix trains a better matting network (Dai et al. CVPR23) than either alone. Limits: synthetic, so it inherits diffusion flaws (misspelled stop sign), some shadows end up in the alpha, ~0.15% NSFW-flagged.

## Beats

1. Problem: real alpha (hair) exists; no big data to learn it (726 max). Hand-off from Peekaboo's blobby masks.
2. Key idea: prompt for a green screen + chroma key, with least-common-hue screen choice.
3. Making screens keyable: DeepFloyd -> paste -> SDXL img2img + negative prompt.
4. Getting alpha: three keyers, agreement = quality, 110k auto + 40k human.
5. The dataset + impact + limits.
6. What it enables: alpha-to-RGB, user study numbers, hand-off to GWTF.

## Slides

Slide is 960x540 pt, title drawn at top. Speech is in the JSON verbatim; summaries here.

| # | Title | Visual (all in `.scratchpad/explain_magick/crops/`) | On-slide text | What it shows |
|---|---|---|---|---|
| 1 | Hair is hard | `s1_hair_alpha.jpg` — top-left panel of `source/src/3_MAGICK/figs/fig1.jpg`, frac box (0,0,0.333,0.496): white silhouette with hundreds of thin gray hair strands on black. rect [110,96,324,429] | red "Biggest matting dataset: 726 objects" | what an alpha matte is, why we lack data |
| 2 | The trick | `s2_pine_needles.jpg` — full `figs/GreenOnGreenBadGreenOnBlueGood.png` (Ryan's own: pine needles on green "maybe not the smartest idea..." vs on blue "much better!"). rect [100,88,760,390] | red prompt suffix | green screen + least common hue |
| 3 | Keyable images | `s3_deepfloyd.jpg` and `s3_sdxl_img2img.jpg` — panels 2 and 5 of `figs/img2img_pipeline.pdf` rendered at 200 dpi (frac boxes (0.229,0.093,0.389,0.87) and (0.814,0.093,0.974,0.87)): same screaming girl, DeepFloyd with mushy hair on dull green vs SDXL img2img with crisp flyaway hair on bright green. Red arrow between. | labels; red "SDXL img2img, negative prompt "green"" | two-model chain |
| 4 | Three keyers | `s4_disagree_low.jpg` (glass of water on violet, score .802, the three alphas disagree; Photoshop's is a solid block) and `s4_agree_high.jpg` (man with glasses on green, score .995, three identical silhouettes) — halves of `figs/sim_score_qualitative2.pdf` at 200 dpi, frac boxes (0.01,0,0.48,1) and (0.49,0,0.96,1). Red box on the agreeing one. | red "When they agree, it worked." | selection by agreement |
| 5 | 150,000 cutouts | `s5_dataset_grid.jpg` — top-left 60% x 50% of `source/src/3_MAGICK/full_512.jpg`: 30 object/alpha pairs on gray (asparagus, lightbulb, fire, parrot, porcupine, basketball net, lightning, splash, wheelchair tennis player, flying hair). | red "3,700-6,400 downloads a month" | dataset, impact, limits |
| 6 | Alpha in, image out | `s6_alpha_to_rgb.jpg` — full `figs/alpha2rgb.png`: inverted hair alpha / ours (strands follow the alpha) / stock ControlNet (ignores it). | column labels, middle in red | application + user study, hand-off |

Possible build: slide 4 can start with only the right image + red box, then add the left (glass) image; spoken order already follows that (right first). Slide 2 could build from the green half to the full image but the PNG is one piece, so left as a single slide.

Rejected visuals: `figs/PipelineOverview.png` (good summary but 5 steps + 6 images, too dense for one slide; slides 2-4 cover it step by step); `figs/priorcomparison.png` (5x2 grid, said in speech instead); `figs/MattingMethods.png` (redundant with slide 4); `figs/S3.png` letter-S glyphs (fun, but no budget — good backup slide); bottom half of `fig1.jpg` (park composite with ellipses; purpose not stated in the text, so not used).

## Impact numbers used (from impact_verified.md)

~20 citations (Google Scholar). Hugging Face downloads 6,448/month (Jun 2026) and 3,773/month (Aug 2026), 158,640 all-time. Used by Trans-Adapter (ICCV 2025), TKG-DM (CVPR 2025), PSDiffusion (WACV 2026), PrismLayers, LayeringDiff. "Largest public general-domain RGBA dataset" — LayerDiffuse's 1M set was never released, so say "public".

## Likely committee questions

- **Isn't this just distilling Photoshop / your keyers? How is it ground truth?** It's not ground truth in the physical sense — it's alpha that three independent methods agree on (MS-SSIM on white and black composites, min over pairs). Disagreement cases went to humans. Slide 4.
- **Why not run a matting network on ordinary generated images?** Natural-background matting is far less constrained than keying a flat screen; existing matting nets are trained on <1k objects and fail on hair/transparency, so they can't produce training-grade labels. Slides 1, 4.
- **Why the 50% threshold?** Empirical: the top half (score above the 0.984 median) looked decent on inspection; the rest went to manual selection. Honest answer: chosen by eye, not tuned. Slide 4.
- **Does the dataset carry color spill / shadow artifacts?** Negative prompt + pixel-wise decontamination reduce spill; some soft shadows remain in alpha; it's synthetic so it inherits diffusion errors (misspelled text). Slides 3, 5.
- **Bias toward green/blue screens or toward what DeepFloyd can draw?** Screens are green/blue >90%; subject distribution is limited to what DeepFloyd+SDXL render well. Content is GPT-4 / procedural / caption-derived prompts, ~0.15% NSFW flagged. Slide 2.
- **Is the user study fair? Baselines weren't trained on alpha.** No prior model takes alpha as input; stock ControlNet seg conditioning ignores fine alpha (slide 6 right panel), so we compared against edge-conditioned ControlNets on the same SD1.5 base. 52 participants, 27 unseen alphamatting.com masks, 82% / 77% preference. Slide 6.
- **Does it help matting itself?** Yes, training Dai et al. (CVPR23) on a MAGICK + DIM mix beats either alone (mentioned on slide 5). Avoid quoting the exact ratio — the thesis text and table label disagree on which way the ratio goes.
- **Cost?** 32 A100s for 3 weeks + 2 months annotation, about $30k. Not on slides.
- **How does this connect to the thesis?** Another handle on a frozen model: the prompt suffix + least-common hue steers a frozen RGB model into producing keyable images, no retraining. Slides 2-3.

## Uncertain / not verified

- "Biggest matting dataset: 726" is per the thesis intro (SIM extends DIM to 726); larger private sets may exist.
- Matting mix ratio (see above) — kept vague on purpose.
- 150k (paper) vs "140,000+" (HF/GitHub page): used 150,000 as in the thesis.
