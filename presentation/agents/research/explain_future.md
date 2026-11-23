# What's next (future section)

Machine-readable spec: `presentation/agents/specs/future.json` (generator: `presentation/agents/.scratchpad/scratchpad_agent_7.py`). 4 slides, 425 spoken words. Slide 4 was redone as a 4-row left-aligned timeline (26 pt) plus one 20 pt metrics line and a small grey "PROPOSED" in the corner; edits applied by `scratchpad_agent_7b.py` on top of the generator output. Text elements on slide 4 carry `"align"` (left/right), a new key the builder may need to support. This section replaces frame slide 11 ("What's next"). Crops are in `presentation/agents/.scratchpad/explain_future/`.

## Sources and what they actually say
- `source/src/8_future_work.tex` (Future Work): the only thesis direction is "turn a general image-to-image editor into a general video-to-video editor, basically Nano Banana but for video", any edit (appearance, motion, or both) without disturbing what you didn't ask to change. MotionV2V is framed as the early step for motion.
- `scrapnotes.txt`: "Proposed next project: LoraPlexer + Vid2Vid Editing", "WHAT NEXT: I2I2V2V + MAGICK". LoraPlexer ingredients: 3D view change from synthetic + lighting changes, multi-distillation, MAGICK, multi noise levels, CFG (with and without model), demo case: To-Edges LoRA + 2-bit color LoRA on his dog, "can it reproduce my dog?".
- Visuals found in ref decks (these are the only grounded "what already works" claims):
  - `ref_pptx/InternPresentation.pptx` slide 8 (deckcraft index 7): GenFlow, driving video + edited first frame -> edited video (rocket launch). Credit Tobias Gerts, done in ComfyUI, "latest 1080P GenFlow Ckpt". -> `rocket_i2i2v2v.png` (full slide, 1920x1080).
  - `ref_pptx/GenFlowMay4.pptx` slide 16 (index 15): "Rank 32 LoRA-Mux (Merging 100 community LoRA's - no training involved)", "single Rank 32 Lora + 6 Different Modes", "Same Prompt + Same Seed for All of Them". -> `loramux_grid.png` (crop 0,120,1920,830).
  - `ref_pptx/InternPresentation.pptx` slide 16 (index 15): "Nanobananna Can Edit Many Frames at Once. TLDR: We used NanoBanana to create a video training dataset" (12 edits of one green-screen singer). -> `nb_multiframe.png` (crop 0,0,1920,802).
  - Also seen, not used: GenFlowMay4 slide 5 (LoRA A VFX Vid2Vid, LoRA B pulse mask, LoRA C Nano Banana data, "use Lora A + Lora C at inference"), slide 6 (list of controls incl. GWTF-based motion, edges, depth, relighting, "Unlike VACE, our performance will NOT degrade as we add more modalities"), slides 8-9 "EditAnything LTX2 LoRA (text+video->video)".

**Ryan must confirm before the talk:** GenFlow / LoRA-Mux / the Nano Banana dataset come from internship decks. Check that (a) you can show them publicly, (b) they count as your work toward the thesis, and (c) "LoRA-Mux" is the same thing as LoraPlexer. If any answer is no, drop slides 1-3's images and keep the speech as a plan.

## Talk track
1. **What's next** (rocket). Every handle so far was one specific thing. MotionV2V edits a real video without regenerating it, but only the motion. Next: one editor for any edit, Nano Banana for video. I2I2V2V = edit one frame with an image editor, a video model carries it through the clip. Early result: driving video + edited first frame -> edited video.
2. **One model, many handles** (LoRA-Mux grid). Every control signal is its own LoRA and stacking them fights. LoraPlexer packs many into one switchable adapter. Proof of concept: 100 community LoRAs merged into one rank-32 LoRA, no training, 6 modes, same prompt and seed. Next: distill properly across noise levels with CFG intact.
3. **Where the data comes from** (Nano Banana frames). Same trick as MAGICK: get the data out of models that already exist. Image editors edit many frames consistently -> paired before/after video. Dog test case: edges LoRA + 2-bit color LoRA, can the combined model rebuild the real dog.
4. **The plan** (timeline: Now–Feb data, Feb–Apr train, Apr–Jun evaluate, Summer paper + thesis + defense; dates PROPOSED BY AI). Data -> train -> evaluate -> paper -> thesis. Baselines, three metrics, user study, two risks with fallbacks.

### Why it's the natural next handle (the through-line)
- Each paper added one handle: where (Peekaboo), which angle (DI), how see-through (MAGICK), how it moves (GWTF), change the motion (MotionV2V). The last one moved from generating to editing real video, but for one edit type. The next step is every edit type.
- It reuses all five: MAGICK's idea of bootstrapping data from a model that can't do the task, GWTF's warped noise as the temporal-consistency fallback (GenFlowMay4 slide 6 already lists "Go-with-the-Flow Based" motion control), MotionV2V's paired-counterfactual training and user-study evaluation, and the SDS/distillation thread (Peekaboo, DI) shows up as multi-distillation in LoraPlexer.

## Plan details (PROPOSED BY AI, Ryan must confirm)
None of this is in the sources. It is a reasonable default, not a done plan.
- **Data:** multi-frame image-editor edits of real clips (as in the Nano Banana dataset slide) + MAGICK-style synthetic pairs: render a clip, apply a known edit (relight, recolor, view change from synthetic 3D, per scrapnotes), so ground truth exists.
- **Base model:** an open video model (GenFlowMay4 mentions LTX-2 / LTX2.3), so results can be released.
- **Baselines:** per-frame Nano Banana (flicker baseline), first-frame edit + image-to-video, VACE, AnyV2V. For LoraPlexer: each LoRA alone vs. merged vs. naive LoRA stacking.
- **Metrics:** edit match (VLM judge or CLIP text-image score on the instruction), preservation (LPIPS/PSNR outside the edit region on synthetic pairs, and against the original for unedited regions), temporal consistency (flow-warp error with RAFT), user study in the MotionV2V format. LoraPlexer: per-mode quality drop vs. the single LoRA; dog demo scored by LPIPS against held-out real frames.
- **Risks and fallbacks:**
  - Edit drifts or fades over long clips -> warped-noise init (GWTF), keyframe re-editing every N frames.
  - Merged LoRAs interfere -> keep separate LoRAs on a shared base, or a mode token / router trained jointly.
  - No ground truth for real edits -> rely on synthetic pairs for numbers, user study for real clips.
  - Industry code can't be released -> reimplement on an open model (needs Ryan's call on what's his).
- **Timeline (months from now):** 1-2 data, 2-4 training, 4-6 evaluation, 6-9 paper + thesis writing + defense. Ryan must put real dates and a target venue on it.

## Likely committee questions
- **Ryoo: "How is this different from VACE or existing video editors?"** Those take a fixed set of conditions and, per my own GenFlow notes, quality drops as you add modalities. I2I2V2V uses whatever image editor is best that month as the front end, so it gets better as image editors get better, and LoraPlexer is the answer to the "many modalities" problem. (Confirm you're OK citing the VACE claim.)
- **Ryoo: "How do you evaluate an edit when there's no ground truth?"** Synthetic pairs where I applied the edit myself give real numbers for preservation and consistency, same idea as MotionV2V's counterfactuals. Real clips get a user study and a VLM judge for "did it do what I asked".
- **Samaras: "Isn't this just propagating an edit with an I2V model? What's new?"** First-frame I2V regenerates everything after frame one, so you lose the original's motion and detail. Here the original video stays an input the whole time, which is the same argument I made for MotionV2V against inpainting and first-frame-to-video.
- **Samaras: "Why LoRAs instead of constrained sampling or guidance?"** Guidance needs a differentiable constraint per signal and per-sample cost. LoRAs are cheap, already exist by the thousands, and the proof of concept shows a hundred of them fit in one rank-32 adapter. Guidance stays a fallback for signals with no LoRA.
- **Sun: "When you merge 100 LoRAs into rank 32, what are you actually solving?"** A low-rank approximation of the summed weight deltas, so the interesting question is how much the modes overlap. If they don't fit, quality per mode drops and that's measurable. Distillation across several noise levels is the training version of the same thing. (Ryan: confirm how LoRA-Mux actually merges, e.g. SVD of stacked deltas, before claiming this.)
- **Sun: "Does distillation across noise levels converge, and does CFG survive?"** Honest answer: unknown yet. That's why the plan scores each mode against its original LoRA, with and without CFG.
- **Any: "What if it doesn't work in time?"** MotionV2V is already a complete V2V edit for motion. The fallback thesis chapter is I2I2V2V for appearance edits only, with LoraPlexer as a separate result.
- Slide 1 speech now says: "Tobias Gerts made this one in ComfyUI. The part I built is the GenFlow model underneath it: the training data and the LoRAs it runs on." The second sentence is inferred from GenFlowMay4 slide 5 (LoRA A/B/C training plan in Ryan's deck); **Ryan must confirm or correct it.**
- **Any: "Is the rocket result yours?"** It was made by Tobias Gerts in ComfyUI with the GenFlow checkpoint. Say exactly that, and say what part you built.

## Uncertain
- Exact meaning of LoraPlexer's notes items ("multi-distillation", "CFG with and without model") is interpreted, not stated.
- Whether GenFlow / LoRA-Mux / NB dataset are showable and count as thesis work.
- Speech is 399 words vs. the ~450 target, leaving room for the build on slide 4.
