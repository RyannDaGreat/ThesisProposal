# Thesis proposal talk: proposal v1 (2026-11-22 18:25)

Sources: `research/thesis_story.md`, `research/style_A.md`, `research/style_B.md`, `research/decks_C.md`, `../scrapnotes.txt` (used as a rough direction only).

## The story in one breath
Text is a tiny knob on a huge output. Type a sentence and the model fills in everything else from its own prior, so you get what the model wants, which is often not what you meant. Every paper in this thesis finds another handle that's already hiding inside a frozen model:
**where things are** (Peekaboo) → **what you see from each angle** (Diffusion Illusions) → **how transparent they are** (MAGICK) → **how they move** (Go-with-the-Flow) → **changing how they move in a video that already exists** (MotionV2V) → **any edit to any video** (next project).

Second thread for the committee, the methods ladder: no training (Peekaboo, DI) → synthetic data from the model itself (MAGICK) → change the noise (GWTF) → counterfactual training pairs (MotionV2V). Each rung spends more training to buy more control.

## Slide plan (50 + backup)
Each paper section uses the same template: roadmap slide → hook → the trick (2-3 build slides) → results → "what became of it" boast slide.

**Cold open (1-5)**
1. Title: *How to Control Your Diffusion Model*. Name, committee.
2. BANG: Warped-noise RickRoll video (InternPresentation 3). No explanation.
3. BANG: Diffusion Illusions flip/rotate results (DiffiluSigPresent 4, 6-13). No explanation.
4. BANG: MAGICK RGBA balls over backgrounds (SIGGRAPH_DiffiluPoster 3-4). No explanation.
5. "By the end of this talk you'll know how all three of those work."

**Who am I (6-8, quick)**
6. "I am Ryan Burgert" + TRITON photo with the ducks (TRITON Final Poster 4 "*Now with more ducks!").
7. Origin story: 2014, "Controlling Artificial Neural Networks With Genetic Algorithms" (Grade11 0, 4-6). "I've been trying to control neural networks since high school."
8. Contents: 5 papers, what became of them, 3 papers I helped on, what's next.

**The problem (9-12)**
9. "A sentence in, a whole image out." Low-dimensional input vs high-dimensional output.
10. "...so the model fills in the rest. With what IT wants." Slop example.
11. How diffusion models work, quick (Presentation_New 119-132).
12. The roadmap: 5 handles. This slide comes back at every section with the current one highlighted.

**Peekaboo + Diffusion Illusions: score distillation, flowing into each other (13-24)**
13. Roadmap: "Where things are."
14. Peekaboo hook: segmenting with a model that never saw a mask (Peekaboo intro1/intro2).
15. Score distillation, a.k.a. "dream loss" (DiffiluSigPresent 33).
16. Peekaboo trick: learn an alpha mask, composite on random backgrounds (Presentation_New 138-152 builds).
17. Results, honest version: beats GroupViT with zero segmentation training, loses to LSeg ("competitive, not SOTA").
18. Hand-off: "Same loss. What if we optimize SEVERAL images at once?"
19. Roadmap: "What you see from each angle."
20. Illusion definition: prime images + arrangements.
21. The trick, built step by step (DiffiluSigPresent method slides).
22. Dream target loss + printing them out (DiffiluSigPresent 47-52). Hand printouts to the committee.
23. Failure cases ("Dirty Laundry" style).
24. What became of it: CVPR 2023 Best Demo Award, Steve Mould + Matt Parker videos, follow-ups. Reviewer said "Not good, didn't like it". Well, other people did.

**MAGICK (25-31)**
25. Roadmap: "How transparent things are." Hand-off: Peekaboo's masks "lack fine detail".
26. Hook: RGBA from an RGB-only model. "But...how?"
27. The trick: ask for a green screen, chroma key, build the dataset (150,000+ RGBA images).
28. Training alpha-conditioned generation.
29. Live user study: before/after. "Let's do a user study right now lol."
30. Live MAGICK demo (or video fallback).
31. What became of it: ~20 citations, 3.7k-6.4k HF downloads a month.

**Go-with-the-Flow (32-39)**
32. Roadmap: "How things move." Video models arrive and text can't describe motion.
33. Hook: callback to the RickRoll from slide 2.
34. Warped noise explained. The notes ask for a better explainer video; Claude can try to make one.
35. Keeping noise Gaussian while warping it (the actual trick).
36. Fine-tune with no architecture changes.
37. Results grid (InternPresentation 4-5, AutoplayAll).
38. Live noise warp demo.
39. What became of it: CVPR 2025 Oral, ~117 citations, ~1.1k stars, used as a control signal in other people's work.

**MotionV2V (40-44)**
40. Roadmap: "Changing how things move in a video that already exists."
41. Why GWTF can't do it: first-frame conditioning hallucinates everything it can't see.
42. Motion counterfactual training pairs.
43. Results: edits trajectories and keeps the content; beats baselines including GWTF.
44. Status: CVPR 2026, ~11 citations, code not released yet (stated plainly).

**Papers I helped on, fast-forward (45-46)**
45. Vista4D (InternPresentation 16-25, 37).
46. Ziyu's paper + Koichi's paper. **Need slides/figures from Ryan.**

**What's next (47-50)**
47. "Nano Banana, but for video": image-to-image editor → video-to-video editor (I2I2V2V).
48. LoraPlexer: one model, many LoRAs/control signals (MAGICK, multi-noise-level, CFG).
49. Demo case: edges LoRA + 2-bit color LoRA on my dog. Can it reproduce my dog?
50. Timeline to defense + the opening roadmap again, all 5 lit up + "?" for the next one. Then questions.

**Backup:** 3D warped noise, other PhD papers, the full TRITON story, Peekaboo tables, the full MotionV2V eval.

## Style bible (what every builder must follow)
- 16:9 white background, black text. Futura Medium for everything; Bradley Hand for handwritten asides.
- No title placeholders. One centered free text box near the top: 40-54 pt, 1-4 words (up to 96 pt for a single word). Body text 28 pt.
- Media first: about 75% of slides are full-bleed autoplaying video with at most one caption line. 0-10 words on result slides, 15-30 on explanation slides.
- Red arrows and red text mark the key idea. Accents are yellow FFFF00, amber FFC000 and dark red 670706, used rarely.
- No cards, icons, footers, slide numbers or decorative transitions. Builds are done by duplicating the slide and repeating the title.
- Voice: casual, honest, short. "But...how?", "lol", "Believe it or not", CAPS for emphasis, trailing ellipses, failure slides kept in. Never "not X, but Y". No AI filler words.

## How the build gets parallelized (boss plan)
1. **Me first (~10 min):** lock the spine (this file), the style bible and one slide-spec format (`specs/NN_section.md`: per slide → title, on-slide text, media source as deck + slide index or thesis figure path, layout, speaker note). Build 3 reference slides in DeckCraft as the visual standard everyone copies.
2. **Section agents (Sonnet high, parallel):** cold open + me, problem, Peekaboo+DI, MAGICK, GWTF, MotionV2V + helpers, what's next. Each writes only its own spec file, using the shared roadmap and style bible.
3. **Reviewer (Opus, one pass):** reads all specs in order and fixes flow, hand-offs and voice ("does this sound like Ryan?").
4. **Builder agents:** one per section builds a section `.pptx` in `agents/.scratchpad/sections/`. They reuse old slides via DeckCraft `slide.reuse` (it copies slides with their videos out of the ref decks) and use thesis figures for the rest. Then one assembler merges the sections in order into `ai_presentation.pptx`, validates it, and renders every slide for a final visual pass.

## Questions for Ryan
1. Title: "How to Control Your Diffusion Model" (thesis) or "...Video Diffusion Model" (notes)?
2. Order: Peekaboo first (chronological and the thesis order), with Peekaboo flowing into Diffusion Illusions. OK?
3. Background: white (Diffilu talk) or one of your recent gradients (burnt orange from Intern, sky blue from HumanAnim)?
4. Where are the MAGICK talk deck, and the slides for Ziyu's / Koichi's papers and Vista4D?
5. Live demos (MAGICK, noise warp) and the live user study: keep, or video fallbacks only?
6. Facts to check before slides: the Steve Mould view count, Peekaboo's venue (workshop, arXiv-only).
