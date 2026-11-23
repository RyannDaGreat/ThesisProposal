# Frame sections (opener, problem, primer, roadmap, closing)

Machine-readable spec: `presentation/agents/specs/frame.json` (generator: `presentation/agents/.scratchpad/scratchpad_agent_6.py`). Full speeches live in the JSON; this file is the human summary. 12 frame slides, 790 spoken words (+ roadmap repeats). All crops are in `presentation/agents/.scratchpad/explain_frame/`.

## The argument
1. A prompt is a few words, the output is millions of pixels, so the model fills in everything you didn't say (layout, transparency, motion) from its own prior, not from what the artist wanted.
2. Each paper adds one control handle the model never had (where, which angle, how see-through, how it moves, change the motion) to a pretrained model that stays frozen or is barely fine-tuned.
3. The claim: the knowledge needed for that control is already inside the frozen model; the work is building the handle that gets it out. The methods get stronger along the way: no training (Peekaboo, DI) -> synthetic data (MAGICK) -> noise-space hack + fine-tune (GWTF) -> trained control branch (MotionV2V).

**The one question:** How do you make a frozen diffusion model do what YOU want?

## Slides
| # | Title | Visual (file, crop source) | On-slide text | What it does |
|---|---|---|---|---|
| 1 | none | `assets/videos/gwtf_rickroll_warped_noise.mp4` full width (1046x284: noise left, RickRoll right) | none | Cold open, no explanation |
| 2 | none | `diffilu_hook1.mov` left + `explain_frame/magick_rgba.png` right (poster3.png crop 0,638,1122,1640: fire, parrot, W, cat, porcupine with white alpha mattes) | none | Cold open, "by the end you'll know how" |
| 3 | none | text title | "How to Control Your (Video) Diffusion Model" / "Ryan Burgert, Stony Brook University" | Title + who I am (folded in; Grade11 deck skipped, did not add anything in one beat) |
| 4 | Just ask? | `lion_fail.png` (SIGGRAPH_DiffiluPoster slide 3, crop 1432,495,2941,950): 5 models given "A lion isolated on a solid green background", none keyable | none | Concrete case where text fails to specify transparency |
| 5 | Just ask? | build: + red line | "The model decides everything you didn't say." | The problem in plain words |
| 6 | One question | text only | "How do you make a frozen diffusion model do what YOU want?" (red) | Thesis question + claim |
| 7 | Diffusion, fast | `sds_denoise.png` (DiffiluSigPresent slide 33, crop 790,270,1920,680): noisy puppy -> frozen model (prompt "A puppy") -> predicted noise | none | Denoising primer |
| 8 | Score Distillation | `sds_full.png` (DiffiluSigPresent slide 33, crop 0,280,1920,930): full SDS diagram with red arrows, Δimage = predicted − random noise | "The frozen model becomes a critic." | SDS / "dream loss" |
| 9 | Five handles (is_roadmap) | 5 tiles, h=160: Peekaboo (Vader+puppy alpha/foreground/castle), DI giraffe/penguin flip, MAGICK RGBA collage, GWTF cat-in-tree motion arrow, MotionV2V basketball before/after | handles in red: Where / From which angle / How see-through / How it moves / Change the motion; paper names below | Roadmap, repeated before each section via `{"roadmap": true}` |
| — | sections | `insert_section`: peekaboo, diffillusions, magick, gwtf, motionv2v | | |
| 10 | It kept going | Virtually Being, Vista4D, Go-with-the-Track teasers | 3 one-line captions (18pt) | Papers that build on the handles |
| 11 | What's next | MotionV2V tile -> red arrow | "Any edit, any video." | I2I2V2V + LoraPlexer |
| 12 | none | RickRoll video again | "Thanks!" | Callback |

## Likely committee questions
- **"Why is this one thesis and not five papers?"** (slides 5, 6, 9) Same problem in all five: text underspecifies the output, and each paper adds control on an existing pretrained model without training a new one. The handles cover space -> view -> transparency -> motion -> editing real motion, and the methods form a ladder from zero training to a trained control branch. Each paper's limit motivates the next (Peekaboo masks lack fine detail -> MAGICK; image control -> video motion in GWTF -> editing existing video in MotionV2V).
- **"Is SDS just DreamFusion?"** (slide 8) Yes, the loss is DreamFusion's. The contribution is what we optimize with it: an alpha mask over random backgrounds (Peekaboo) and printable arrangements viewed under transformations (DI).
- **"What exactly is next, how will you evaluate it, what's the risk?"** (slide 11) I2I2V2V: edit one frame with an image editor, propagate through the clip. LoraPlexer: combine several control LoRAs (Ryan's demo case: edges LoRA + 2-bit color LoRA, given edges and 2-bit of his dog, can it reproduce the dog?). Evaluation and risk are NOT in the thesis text; Ryan must supply them (suggest: reconstruction of held-out frames/videos from combined conditions, user study as in MAGICK/MotionV2V; risk = LoRAs interfering when combined, temporal drift in propagation).
- **"Frozen? GWTF and MotionV2V fine-tune."** (slide 6) Hence "frozen or barely fine-tuned"; GWTF changes only the noise and fine-tunes the existing model, it keeps the architecture.

## Uncertain
- "Five big models" names are read off poster labels (DeepFloyd, SDXL, Midjourney 5, DALL-E 3, SD 1.5); one-line failure descriptions are from looking at the crop.
- Presentation_New (4.9 GB) cannot be rendered by deckcraft-cli (2 GiB limit), so the primer reuses DiffiluSigPresent slide 33 instead of slides 121-132.
- Go-with-the-Track teaser is dense and small on slide 10; caption carries it.
- Next-project evaluation plan and risk need Ryan's own answer.

## Round 2 changes (frame.json edited in place; the table above is the v1 layout)
- 9 frame slides + 5 roadmap repeats, 780 spoken words in total (down from ~1130 counting the old repeats). The two "Just ask?" slides are merged; its speech leads straight into "One question" and says "we'll come back to this lion in MAGICK".
- One-question text now: "How do you control a pretrained diffusion model without building a new one?" Speech and roadmap state the honest arc: no training -> make the training data -> change the noise and fine-tune -> train a control branch, with the knowledge coming from the pretrained model every time.
- Opener names the RickRoll, avoids "dancing" over a still frame, and pays off with "in about twenty minutes". Slide 2 now uses the static giraffe/penguin flip crop (`explain_frame/tile_diffilu.png`) instead of a mid-flip video frame, and the MAGICK panel is bigger.
- Roadmap repeats are `{"roadmap": true, "speech": one line, "add_elements": [red box on the next tile]}`. The repeat before DI, MAGICK and GWTF gives the "because" that the listener found missing (soft masks -> make data; text can't describe motion -> the noise becomes the handle). The last repeat adds "Next: any edit, any video." and leads into `{"insert_section": "future"}`.
- "It kept going" and "What's next" removed. The close is a five-contribution summary with impact (Best Demo CVPR 2023, over 140,000 RGBA, CVPR 2025 Oral), one line on the three co-authored follow-ups, and the Rick callback (small video + "Thanks!").
- BUILDER NOTE: build_v2.py line ~100 appends the roadmap slide as-is. Repeats need `{**roadmap, "speech": s["speech"], "elements": roadmap["elements"] + s.get("add_elements", [])}`.
