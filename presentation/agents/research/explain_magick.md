# MAGICK — explanation, talk track, slide spec

Machine-readable spec: `presentation/agents/specs/magick.json` (7 slides, 649 spoken words; round 2 revision after examiner 5.5/8). All crops are in `presentation/agents/.scratchpad/explain_magick/crops/` and were made by `presentation/agents/.scratchpad/scratchpad_agent_3.py`.

## The paper in plain words

Diffusion models make RGB pictures. They can't make transparent cutouts with real alpha (the per-pixel see-through value), so hair, fur, smoke and glass come out as hard blobs. To train a model that does alpha you need lots of examples, but alpha is hard to get from real photos: the biggest matting dataset (Semantic Image Matting) has 726 objects, Adobe DIM has 431, alphamatting.com has 27. Segmentation datasets are big but their edges are hand-traced and hard.

MAGICK makes a 150,000-object RGBA dataset from RGB models alone. The idea is Hollywood's: ask the model for the object "isolated on a solid green background", then chroma key the screen out. Three problems and their fixes:
1. **Screen color.** A green object on green disappears. Generate the plain prompt once with SDXL, build a saturation-weighted hue histogram (Gaussian smoothed, sigma 10 degrees), pick the least-used named hue. Green or blue in over 90% of cases.
2. **Models can't make keyable screens.** SDXL/Midjourney/DALL-E give dark, gradient, or tinted screens; DeepFloyd gives flat screens but mushy edges. Fix: DeepFloyd image, cut out roughly with Photoshop Subject Select, paste onto a brighter saturated screen of the same hue, then SDXL img2img (SDEdit) at strength 0.95 with the screen color as a negative prompt. High strength repaints fine detail; the negative prompt removes color spill from the subject but can't touch the over-saturated screen.
3. **Keying is under-constrained.** Run three keyers that fail differently: a per-pixel color-difference keyer (Wright) with a per-pixel background estimated by deleting the foreground and inpainting (Telea) — this also gives decontaminated foreground colors; Adobe's internal learned chroma-key net; Photoshop Subject Select. Score = min over pairs of the mean MS-SSIM of the two cutouts composited on white and on black. Agreement means success. Median score 0.984; the top 50% (110k) are auto-accepted using the pixel-wise keyer; the other 40k (glass, water, smoke, fire) were chosen by humans in a web UI, one click among 7 alpha/foreground combinations (5 workers x 112 h, $0.30/sample).

Each sample: pure foreground colors F, alpha, caption (resolution not stated in the thesis text; don't say 1024). Prompts come from GPT-4/ChatGPT, procedural human templates, and an Adobe caption dataset with "clipping path"/"greenscreen" tags stripped.

Use: ControlNet (SD1.5) fine-tuned for alpha + prompt -> RGB. User study, 52 people, 27 alphamatting.com masks with GPT-4 prompts: preferred 82% vs SD1.5 Canny-edge ControlNet (16%), 77% vs Sketch-edge (23%). Each method made 3 images per mask; raters saw the prompt and two rows and picked the better row for appearance and prompt adherence. Baseline rationale (4_results_thesis.tex:17): no prior model takes alpha; ControlNet v1.1 seg is trained on ADE20K and ignores matted detail (it's the Fig. 1 comparison, not a study baseline). A MAGICK + DIM mix trains a better matting network (Dai et al. CVPR23, DIM test set, 6_appendix_thesis.tex:165-195): best SAD 33.03 / MSE .0104 for mixes vs 36.27 and 65.49 SAD for the two pure sets. Limits: synthetic, so it inherits diffusion flaws (misspelled stop sign), some shadows end up in the alpha, ~0.15% NSFW-flagged.

## Beats

1. Problem: real alpha (hair) exists; matting data is hand-made (few hundred objects, largest general-purpose 726), segmentation sets have hard edges. Hand-off from Peekaboo's blobby masks.
2. Key idea: prompt for a green screen + chroma key. Why keying, not a matting net on generated images: net errors would become ground truth; known flat B makes I = aF + (1-a)B nearly solvable and gives decontaminated F.
3. Screen choice: saturation-weighted hue histogram of a plain SDXL image, least-used hue (>90% green/blue).
4. Making screens keyable: DeepFloyd -> paste on brighter screen -> SDEdit (SDXL img2img) strength 0.95 + screen color as negative prompt.
5. Getting alpha: three keyers, agreement as proxy for correctness, top 50% auto (110k) + 40k human-picked.
6. Dataset + matting numbers + cost + limits.
7. Alpha-to-RGB, user study setup and numbers, hand-off to GWTF.

## Round 2 changes (examiner/listener flags in `.scratchpad/study/magick/r1/`)

- "726" now "largest general-purpose matting set" (P3M-10k portraits are bigger); "objects" not "images"; why matting data doesn't scale and why segmentation sets don't count.
- Added why keying beats matting-net-on-generated-images (compositing equation, known B).
- New slide "Pick the screen" with the actual hue histogram; "lavishly" cut.
- Slide "Keyable images": named SDEdit, explained the girl changes (DeepFloyd only gives layout + clean screen), why the negative prompt spares the screen; labels moved up and shortened so they don't clip.
- "When they agree, it worked" replaced by "Agreement is our proxy for correctness"; added threshold (top 50%, median 0.984), Telea-style inpainted per-pixel background, Adobe-internal learned keyer, humans *picked* (best of 7 alpha/F combos), not fixed.
- Cut overclaims: "the model made its own training data", "1024", "still the largest", "used to train layered generators". Added matting numbers, cost, limits.
- Transitions (story listener rated both WEAK, `.scratchpad/full_r1/story_listener.md`): opening now follows from Illusions ("Peekaboo and Illusions steer pixels the model already makes; transparency it can't make at all... here the handle is data"); doesn't rely on Peekaboo's bonus transparency slide. Closing: "now we control what's in a frame down to a single hair, but nothing yet controls how it moves over time. That's the next handle." Kept "down to a single hair" instead of "how see-through", because the examiner flagged see-through as an overclaim (outputs are shown on gray, not RGBA).
- Honest about training: the frozen RGB model makes the data, but the alpha-to-RGB ControlNet is trained ("With that data we fine-tuned..."), which answers the listener's "frozen vs trained" question for this section.
- Stock panel relabeled "ControlNet v1.1 seg" and separated from the user-study baselines; user-study setup stated; "how see-through" overclaim cut.

## Slides

Slide is 960x540 pt, title drawn at top. Speech is in the JSON verbatim; summaries here.

| # | Title | Visual (all in `.scratchpad/explain_magick/crops/`) | On-slide text | What it shows |
|---|---|---|---|---|
| 1 | Hair is hard | `s1_hair_alpha.jpg` — top-left panel of `source/src/3_MAGICK/figs/fig1.jpg`, frac box (0,0,0.333,0.496): white silhouette with hundreds of thin gray hair strands on black. rect [110,96,324,429] | red "Largest general-purpose matting set: 726 objects" | what an alpha matte is, why we lack data |
| 2 | The trick | `s2_pine_needles.jpg` — full `figs/GreenOnGreenBadGreenOnBlueGood.png` (Ryan's own: pine needles on green "maybe not the smartest idea..." vs on blue "much better!"). rect [100,88,760,390] | red prompt suffix | green screen + chroma key, why keying |
| 3 | Pick the screen | `s2b_hue_histogram.jpg` — full `figs/LeastCommonHueHistogram.png` (2934x1280): woman photo + prompt -> log-density hue histogram, dashed line at 100 deg, "Least Common Hue: green". rect [40,100,880,384] | none (figure has its own label) | least-common-hue choice |
| 4 | Keyable images | `s3_deepfloyd.jpg` and `s3_sdxl_img2img.jpg` — panels 2 and 5 of `figs/img2img_pipeline.pdf` rendered at 200 dpi (frac boxes (0.229,0.093,0.389,0.87) and (0.814,0.093,0.974,0.87)): screaming girl, DeepFloyd with mushy hair on dull green vs SDEdit result with crisp flyaway hair on bright green. Red arrow between. rects [50,92,370,373] / [540,92,370,373] | labels at y474; red "SDEdit (SDXL), strength 0.95" | two-model chain |
| 5 | Three keyers | `s4_disagree_low.jpg` (glass of water on violet, score .802, the three alphas disagree; Photoshop's is a solid block) and `s4_agree_high.jpg` (man with glasses on green, score .995, three identical silhouettes) — halves of `figs/sim_score_qualitative2.pdf` at 200 dpi, frac boxes (0.01,0,0.48,1) and (0.49,0,0.96,1). Red box on the agreeing one. | red "Agreement is our proxy for correctness." | selection by agreement |
| 6 | 150,000 cutouts | `s5_dataset_grid.jpg` — top-left 60% x 50% of `source/src/3_MAGICK/full_512.jpg`: 30 object/alpha pairs on gray (asparagus, lightbulb, fire, parrot, porcupine, basketball net, lightning, splash, wheelchair tennis player, flying hair). | small: "Matting error (SAD): best mix 33, either set alone 36 / 65"; red "3,700-6,400 downloads a month" | dataset, matting, cost, limits |
| 7 | Alpha in, image out | `s6_alpha_to_rgb.jpg` — full `figs/alpha2rgb.png`: inverted hair alpha / ours (strands follow the alpha) / ControlNet v1.1 seg (ignores it). rect [100,88,760,348] | column labels; red "52 raters preferred ours 82% vs Canny, 77% vs sketch" | application + user study, hand-off |

Possible build: slide 5 (Three keyers) can start with only the right image + red box, then add the left (glass) image; spoken order follows that. Slides 2-3 work as a build pair (pine needles -> histogram).

Rejected visuals: `figs/PipelineOverview.png` (5 steps + 6 images, too dense; slides 2-5 cover it step by step); `figs/priorcomparison.png` (5x2 grid, said in speech instead); `figs/MattingMethods.png` (redundant with slide 5); `figs/S3.png` letter-S glyphs (no budget, good backup slide); bottom half of `fig1.jpg` (purpose not stated in the text).

## Impact numbers used (from impact_verified.md)

~20 citations (Google Scholar). Hugging Face downloads 6,448/month (Jun 2026) and 3,773/month (Aug 2026), 158,640 all-time. Used by Trans-Adapter (ICCV 2025), TKG-DM (CVPR 2025), PSDiffusion (WACV 2026), PrismLayers, LayeringDiff. "Largest public general-domain RGBA dataset" — LayerDiffuse's 1M set was never released, so say "public".

## Likely committee questions

Slide numbers refer to the 7-slide section.

- **How is this ground truth? Isn't it just distilling your keyers?** It's alpha that three independent methods (color-difference keyer, Adobe's learned keyer, Photoshop Subject Select) agree on: min over pairs of the mean MS-SSIM of the cutouts composited on white and on black. Agreement is a proxy, said so on slide 5. Low-agreement cases go to humans or are dropped.
- **Why not run a matting network on ordinary generated images?** Its errors become the labels (2_relatedwork_thesis.tex:30). With a flat screen B is known per pixel, so I = aF + (1-a)B is nearly solved and F comes out decontaminated. Slide 2.
- **Why the 50% threshold?** The top half (above the 0.984 median) "yields decent results" (3_method_thesis.tex:164): chosen by inspection, not tuned. Appendix figure caption says the rest of the automatic pool is discarded. Slide 5.
- **Color spill / shadows?** Screen color as negative prompt removes spill from the subject (screen too saturated to be affected); pixel-wise keyer with inpainted background gives decontaminated F; some soft shadows stay in alpha. Slides 4, 6.
- **Bias?** Screens >90% green/blue; subjects limited to what DeepFloyd + SDXL draw well; synthetic text errors; ~0.15% NSFW-flagged. Slides 3, 6.
- **Is the user study fair?** No prior model takes alpha (4_results_thesis.tex:17); ControlNet v1.1 seg (ADE20K-trained) ignores matted detail (slide 7 right panel, Fig. 1, not a study baseline). Study baselines: SD1.5 Canny-edge and sketch-edge ControlNets on the same base. 27 unseen alphamatting.com masks, GPT-4 prompts, 3 images per method, 52 raters picked the better row for appearance and prompt adherence. 82% vs Canny, 77% vs sketch. Slide 7.
- **Does it help matting?** Dai et al. CVPR23 on DIM test: best mix SAD 33.03 (MSE .0104) vs 36.27 and 65.49 for the two pure sets. Don't say which pure set is which: the thesis text and old caption disagree on the ratio direction. Slide 6.
- **Cost?** 32 A100s for 3 weeks + 2 months annotation, $30,000; manual part: 5 workers x 112 h, $0.30/sample. Slide 6.
- **Frozen model? You trained a ControlNet.** The frozen RGB model (prompt suffix + least-common hue + SDEdit) makes the data with no retraining; the alpha-to-RGB ControlNet is then trained on it. The speech says this on slide 7. Slides 1-4, 7.

## Uncertain / not verified

- "726" is the largest *general-purpose* matting set per 6_appendix_thesis.tex:256 (SIM). Portrait sets such as P3M-10k are larger, hence "general-purpose".
- Matting mix ratio (see above) — kept vague on purpose.
- 150k (paper) vs "140,000+" (HF/GitHub page): used 150,000 as in the thesis.

## Round-3 changes (polish)
- Slide 2: equation `I = αF + (1−α)B` on slide with red "B = the screen color, known at every pixel"; speech uses "three equations for four unknowns... that's why we run three"; prompt caption "...isolated on a solid [color] background".
- Slide 4: images shrunk to 340 pt, label gets its own box at y448 (no more clipped wrap).
- Slide 5: numbers on slide (worst-pair MS-SSIM, median 0.984, auto 110k, human 1-of-7 40k); "proxy, not proof" in speech.
- Slide 6: SAD line and limits on slide; cost = $30k annotation plus 32 A100s for three weeks; open keyer for auto samples and 0.95 repaint stated (slide 4 and 6 speech).
- Slide 7: seg-ControlNet panel swapped for the alphamatting row of `alpha2rgbResults.png` (alpha | ours | sketch | Canny), crop `.scratchpad/explain_magick/crops/s7_alpha2rgb_study_row.jpg`; caption with 82/16 and 77/23; "edge accuracy is future work" said aloud.
- SAD DIRECTION: OPEN QUESTION FOR RYAN. Per the coordinator, the slide takes no side: "either dataset alone 36 / 65 → mix 33", and the speech says "mixing beats either alone". Ryan: which is MAGICK-only, 36 or 65? Fix 6_appendix_thesis.tex:166-168 so the definition and the table agree. Earlier analysis follows: the examiner wanted "DIM only 65 · MAGICK only 36". `6_appendix_thesis.tex:168` defines the ratio as the MAGICK fraction, but the same paragraph says the optimum is 1/5 MAGICK + 4/5 DIM (the best row is ratio 4/5), and the old caption in `6_appendix.tex:275` says a higher ratio means more DIM. Two of the three statements say the ratio is the DIM fraction, so ratio 0 = MAGICK only = 65.49 and ratio 1 = DIM only = 36.27. The slide says "MAGICK only 65 · DIM only 36 · mix 33". Ryan must confirm this; line 168 contradicts itself either way and needs fixing in the thesis.
- Small (~11 pt) labels remain baked into the figure images on slides 3 and 5 (axis ticks, keyer names); all added text is ≥18 pt.
