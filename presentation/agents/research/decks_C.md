# decks_C: scan of 7 decks (python-pptx text scan; full per-slide dump in decks_C_raw.txt)

## Summary table
| Deck | Slides | Size (in) | About | Pics/Videos |
|---|---|---|---|---|
| AlphaGenFigures.pptx | 26 | 45.6x38.2 (poster-scale canvas) | MAGICK figure scratch: RGBA/alpha-matte generation, negative chromakey prompting, img2img refinement, similarity-score filtering, DF-XL noun stats | ~300 pics, 0 vid |
| AlphagenSelectionGuide.pptx | 7 | 13.33x7.5 | Annotator guide for picking best alpha/RGBA candidate (MAGICK dataset curation) + TODO notes | 20 pics, 0 vid |
| SIGGRAPH_DiffiluPoster.pptx | 9 | 43x24 | SIGGRAPH poster: Diffusion Illusions (flip illusion) + Peekaboo RGBA + MAGICK; authors Burgert, Li, Abe L..., Price, Kuen, Li, Ryoo | ~120 pics, 0 vid |
| Presentation_New.pptx | 156 | 13.33x7.5 | "Research Preliminary 2023" talk: TRITON + Peekaboo (committee Samaras, Hoai, Ryoo); big background sections | ~700 pics, ~55 vid slides |
| TRITON Final Poster.pptx | 20 | 13.33x7.5 | TRITON poster/slide material (sub-set of Presentation_New) | ~140 pics, ~14 vid |
| Grade11_Gen Alg and NN Presentation | 45 | 10x7.5 | 2014 Long Island Math Fair talk, Controlling Artificial Neural Networks With Genetic Algorithms | ~85 pics, 3 vid |
| ThesisProposal.pptx | 1 | 13.33x7.5 | empty | 0 |

## AlphaGenFigures.pptx (26 slides, 45.6x38.2 in)
Figure-assembly canvas for MAGICK (RGBA generation). Titles:
0-1 "BEST RGBA IMAGES FROM LAION: CHERRYPICKED TO BE GOOD" | 2 "Color Aversion" / "NEGATIVE CHROMAKEY PROMPTING WITHOUT IM2IM ON FIREFLY" | 3 empty | 4-9 chromakey pipeline (SDXL text-to-image, random subjects "lemon splashing in water", "robot exoskeleton", color "magenta") | 10 Prompt recipe: subject + "isolated on a solid" + least-common-hue + "background"; DeepFloyd output vs Photoshop Subject Selection | 11-12 model comparison: Deep Floyd / SDXL / Firefly 1.0 / Midjourney 5 / DALL-E 3 | 13,15 Before/After Img2Img | 14 RGB input; pixel-wise chromakey vs deep-learning chromakey vs Photoshop subject select | 16 Similarity score distribution (low .802 / high .995 examples) | 18 "Our Alpha-to-RGB" vs Sketch Edges vs Adobe Text Effects | 19-23 image grids | 24 "Most common DFXL nouns" ("Slightly Innacurate but whatever") | 25 empty.

## AlphagenSelectionGuide.pptx (7 slides, 13.33x7.5)
Annotator guide: "They all look the same from afar. Given multiple good options, try the one on the left...", "None are perfect. But some are good.", "Shadows are ok, as long as they look good!", "High detail is good!", "Be careful: watch out for greenspill on the hair!". Slide 6 = TODO notes (zoomable tiles on spacebar for Brian, multi-select examples). Not talk material.

## SIGGRAPH_DiffiluPoster.pptx (9 slides, 43x24)
0-1 Diffusion Illusions: Hiding Images in Plain Sight (diffusionillusions.com), "The Flip Illusion", leftover note "Label Peekaboo Loss Somewhere Here / Then Pseudocode (super duper short!!)" | 2 "Peekaboo can also generate images with transparency (An RGB image and mask are jointly optimized with Peekaboo loss)", Cropped Pascal-VOC | 3-4 MAGICK poster section (ryanndagreat.github.io/MAGICK; Burgert, Price, Kuen, Li, Ryoo): "MAGICK is a giant RGBA image dataset: over 150,000 images / complex alpha mattes and text captions at 1k..." | 5-8 mostly image-only/placeholder ("." text).

## Presentation_New.pptx (156 slides, 13.33x7.5) = "Research Preliminary 2023"
Slide 0 verbatim: "TRITON: Neural Neural Textures make Sim2Real Consistent / Peekaboo: Text to Image Diffusion Models are Zero Shot Segmentors / and / Ryan Burgert / Research Preliminary 2023 / Committee Members: Dimitris Samaras, Minh Hoai, Michael Ryoo". Slide 1 = agenda (TRITON Background / TRITON / Peekaboo Background / Peekaboo / Extras).
Sections:
- 2-17: TRITON overview, losses, outline stubs/notes (slides 8-16 are speaker-planning notes: "Only put in what I can explain well?", "[END TRITON]")
- 18-61: TRITON background: Pix2Pix, CycleGAN (works on stills, bad on video, "...but we'll revisit this issue later"), UNIT, MUNIT, CUT, RL-CycleGAN, RetinaGAN, SSIM/MSSSIM, Pfeiffer et al, Deferred Neural Rendering, UV maps, neural textures
- 62-66: Fourier Feature Networks, NeRF
- 67-102: TRITON method (Texture Recovering Image Translation Network, unprojection consistency loss, texture realism loss, adversarial losses)
- 103-116: experiments (reaching, pose prediction, deformable objects, shine/shadows; videos)
- 117-137: PEEKABOO background and notes
  - 119 "Diffusion Models / CLIP-based optimization / Score Distillation Loss"
  - 121-125 "How Diffusion Models Work" (They denoise images; training pairs by adding noise; one step is blurry; iterative DDPM sampling; credit Tom Goldstein tweet)
  - 126 Text-to-image diffusion (CLIP modulated; Dalle-2, GLIDE, Imagen, SD)
  - 127-128 VQGAN-CLIP "My point: sample generation via a loss"
  - 129 DreamFields (CLIP optimizes NeRF), 130-132 DreamFusion Score Distillation Loss ("= True noise - predicted noise")
  - 133-137 planning notes (referring seg, GroupViT, LSeg)
- 138-152: Peekaboo: zero-shot segmentation built on Stable Diffusion, "requires 0 training", Prompt "Harry Potter"; 140-144 "This is a picture of Harry Potter / ...and this one too! / ...they're ALL Harry Potter / ...the background doesn't matter"; 145-150 learned alpha = "neural neural texture", random-color composites, ScoreDistillationLoss("Harry Potter"), "Goal: find a minimal alpha map such that all composite images satisfy 'Harry Potter'", alpha penalty, "better! but why is it chopping up his shirt?", bilateral filter fix; 152 Peekaboo main diagram
- 153 "See more results at peekaboopaper.github.io" | 154 note "Briefly mention ClipPy, GroupVIT, Lseg" | 155 video slide

## TRITON Final Poster.pptx (20 slides)
Poster/figure slides from TRITON; duplicates of Presentation_New slides 4-6, 66, 69-82. Titles: Qualitative Comparisons, Full Training Pipeline, Dirty Laundry, "Better than CycleGAN!", Unpaired Image Translation Inference/Training (black-box), Global Temporal Consistency. Not relevant to thesis papers.

## Grade11 deck (45 slides, 10x7.5), 2014
Title: "Controlling Artificial Neural Networks With Genetic Algorithms", Ryan B., Port Jefferson 2014, Al Kalfus Long Island Math Fair. Slides: 1-6 what program does (Processing language, Magic Bullet Looks filter mimicry via NN trained on before/after pictures), 7 goal, 8-19 step-by-step genetic algorithm (random configs, test, parent/child), 20 watermelon/quadrilateral demo (40 quads, RGB+alpha) video, 21 ragdoll NN video, 22-23 pixel as function (x,y -> rgb), 24-31 NN intro (hidden layer 16 neurons, wX+wY+b, f), 32-40 program walkthrough, 41 "...fin", 44 "(fin)".

## Reusable for thesis talk
Deck / 0-based slide index / description
- **Presentation_New 0**: title slide format (name, "Research Preliminary 2023", committee list: Samaras, Hoai, Ryoo). Style template: same committee likely for proposal. Check if committee same.
- **Presentation_New 119-126**: diffusion intro sequence "How Diffusion Models Work" (noise -> denoise, training pairs, DDPM iterative sampling, text conditioning with CLIP). Direct reuse for the general diffusion intro (images from Tom Goldstein's explanation; credit kept).
- **Presentation_New 127-132**: VQGAN-CLIP "sample generation via a loss", DreamFields, DreamFusion/Score Distillation Loss. Reuse for "optimizing samples through a loss" arc leading to Peekaboo and Diffusion Illusions.
- **Presentation_New 138-152** (Peekaboo, ~15 slides): Peekaboo story; best reuse: 140-144 Harry Potter punchline sequence (140-144 pics: many composites "they're ALL Harry Potter"), 145-146 random-color composites + SDS goal, 147-150 optimization videos, alpha penalty/bilateral filter, 152 main diagram, 153 results URL. Peekaboo paper is covered end-to-end here.
- **Presentation_New 80-81, 4-6, 66-67, 72, 84-102, 104-116**: TRITON; not one of the 5 thesis papers, but "Neural Neural Textures" alpha-as-neural-texture ties to Peekaboo narrative (slide 147 "alpha is a neural neural texture"). Only for a brief "earlier work" mention.
- **SIGGRAPH_DiffiluPoster 0-1**: Diffusion Illusions poster (flip illusion figure, 16 pics each). Source images for the Diffusion Illusions section; images also on diffusionillusions.com. Note leftover to-do to label Peekaboo loss + pseudocode (a good idea for a slide).
- **SIGGRAPH_DiffiluPoster 2**: "Peekaboo can also generate images with transparency (RGB image and mask jointly optimized with Peekaboo loss)" - bridge from Peekaboo to RGBA/MAGICK; Pascal-VOC crops.
- **SIGGRAPH_DiffiluPoster 3-4**: MAGICK poster ("giant RGBA image dataset, over 150,000 images, complex alpha mattes + text captions at 1k"): MAGICK overview figures (29-31 pics each).
- **AlphaGenFigures 0-1, 10, 11-12, 14, 16, 18**: MAGICK figure sources: cherry-picked LAION RGBA, chromakey recipe, model comparison (DeepFloyd/SDXL/Firefly/MJ5/DALL-E 3), chromakey methods compare, similarity-score filtering, alpha-to-RGB vs sketch edges/Adobe Text Effects. Canvas is huge (45.6x38 in) so crop before use.
- **AlphagenSelectionGuide 0-5**: human-curation examples (good/bad alpha). Marginal; only for a data-quality slide.
- **Grade11 0**: personal origin story: 2014 math fair, "Controlling Artificial Neural Networks With Genetic Algorithms" (control theme!). **Grade11 4-6** (filter mimicry before/after), **20** (watermelon from 40 quadrilaterals GA demo video): usable for a short "I have been controlling generators since 2014" personal-intro/timeline beat. Strong personal style element.
- Nothing in these decks for Go-with-the-Flow or MotionV2V (video/motion work). ThesisProposal.pptx is empty.

## Writing voice (verbatim)
- "...er, kinda... L1 loss encourages blurryness"
- "...but we'll revisit this issue later"
- "My point: sample generation via a loss"
- "Don't panic! We'll break this down piece by piece"
- "better! but why is it chopping up his shirt?"
- "...they're ALL 'Harry Potter'" / "...the background doesn't matter."
- "It works well on still images" / "It works badly on videos" / "It's not temporally consistent" (one claim per slide, punchline build)
- "Dirty Laundry / Sometimes TRITON converges to the wrong object. You can usually fix that by re-running it though" (honest failure-case slide)
- "Brief tangent..." ; "Only put in what I can explain well?" ; "Peekaboo! [Follow notes]"
- "*Now with more ducks!" ; "Slightly Innacurate but whatever"
- Style traits: one idea per slide, incremental builds, conversational asides, named failure slides ("Dirty Laundry"), credit to sources on slides, paper URLs on slides (tritonpaper.github.io, peekaboopaper.github.io).

## PRIORITY FLAGS (from Ryan's notes)
1. **TRITON pictures + the ducks**
   - TRITON Final Poster.pptx slide 4: "Sim || Real || Better than CycleGAN! || Simulations -> Photos! || *Now with more ducks! || Works with any 3D simulator!" (3 pics, 2 videos). THE duck slide.
   - Presentation_New.pptx slide 66: same duck slide (2 pics, 2 vids).
   - Duck/rubik's cube/pepper pipeline builds (learned textures, projections): TRITON Poster 13-17 (duck, rubik's cube; 17 adds pepper); Presentation_New 75-79.
   - TRITON hero/qualitative: Poster 0 (17 pics, 3 vids), Poster 1 ("Consistent, reliable, photorealistic"), Poster 5 title ("Neural Neural Textures Make Sim2Real Consistent", Stony Brook CS); Presentation_New 4-6, 80-81.
   - Honest-failure slide "Dirty Laundry": Poster 3 and 19 (4 vids), Presentation_New 7, 82.
   - Temporal consistency demo: Poster 10 / Presentation_New 72 ("Global Temporal Consistency", video).
   - Robot experiments: Presentation_New 104-116.
2. **High school origin story (Grade11_Gen Alg and NN Presentation)**: slide 0 title ("Controlling Artificial Neural Networks With Genetic Algorithms", Ryan B., Port Jefferson 2014, Al Kalfus Long Island Math Fair); 1-6 what the program does (before/after filter mimicry, Example 1/2 NN output); 20 watermelon/quadrilateral GA demo (video, 40 quads with RGB+alpha); 21 ragdoll NN video (someone else's); 24-31 NN intro; 41/44 "fin". Best 4-6 slides: 0, 4 or 5, 20, 21.
3. **3D warped noise**: NOT found in any of my 7 decks (no Go-with-the-Flow content; searched titles/text). Closest idea: Peekaboo "alpha is a neural neural texture" (Presentation_New 147) and TRITON UV neural textures (unprojection consistency), conceptually adjacent (textures anchored to surfaces) but not warped noise.
4. **MAGICK content**: yes, in 3 of my decks, but none is a talk deck:
   - SIGGRAPH_DiffiluPoster.pptx slides 3-4 (MAGICK poster section: 150,000+ RGBA images, alpha mattes + captions at 1k; 31 and 29 pics) and slide 2 (Peekaboo RGBA bridge).
   - AlphaGenFigures.pptx (26 slides; all MAGICK figure material: chromakey prompting, model comparison, similarity filtering, alpha-to-RGB comparisons).
   - AlphagenSelectionGuide.pptx (7 slides; human curation guide).
   Best candidates for a MAGICK slide source: SIGGRAPH poster 3 and AlphaGenFigures 0, 10, 11, 14, 16, 18.
