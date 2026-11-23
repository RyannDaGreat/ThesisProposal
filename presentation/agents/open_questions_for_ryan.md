# Open questions for Ryan (before the talk)

Things the agents could not settle from the thesis or the decks. Each one is on a slide or is likely to be asked about.

## Facts to confirm
1. **Future-work images (slides 48-50):** the internship/GenFlow images are on the slides. Is it OK to show them in public?
2. **LoRA-Mux = LoraPlexer?** Slide 49 assumes they're the same thing. Its six tile labels were guessed from how each tile looks (the speaker notes say [CONFIRM]).
3. **Rocket demo (slide 48):** Tobias Gerts is credited. What part is yours? The speech now says "on a video model from my internship".
4. **Future-work dates (slide 51):** the timeline Now–Feb / Feb–Apr / Apr–Jun / Summer is a guess.
5. **MotionV2V dog race:** the paper contradicts itself. The intro says the bichon wins, edit #4 says the corgi is slowed to reverse the race, and the teaser shows a tie. The slide uses the intended edit.
6. **MotionV2V SSIM ≈ 0.1 for every method** while LPIPS is 0.031. The examiner thinks it's probably a metric bug (data range or latents). Check the eval code.

## Contradictions inside the thesis (not edited, only noted)
- **MAGICK SAD mix:** `source/src/3_MAGICK/sec/6_appendix_thesis.tex:166` defines ratio = MAGICK fraction (so best = 2/3 MAGICK, SAD 33.03), but `:168` says best = 1/5 MAGICK. The slide stays neutral: "either alone 36 / 65 → mix 33".
- **Diffusion Illusions baseline:** `main_thesis.tex:279` (independent vanilla SDXL SDS, "one step") vs `X_suppl_thesis.tex:258` (baseline images leak). The examiner asks why an independent baseline scores low on independence.
- **GWTF density figure:** `algo_diagram_2_layers.png` densities 0.5/1.5/0.5 sum to 3.5, so they're not conserved. The slide uses a corrected figure (1, ⅓, 7/3, ⅓).
- **GWTF γ sentence:** the text says the opposite of the table (table: γ=0.9 → mIoU 0.50, γ=0.5 → 0.74).
- **Peekaboo Algorithm box:** it encodes `img`, not the composite, says MSE where the method uses L1, and `alltex_thesis.tex:188` has no λ.
- **MotionV2V eval protocol text:** `sec/experiments.tex` says it reverses V1, then says V0 is the input. Know which one was actually run.

## Hardest committee questions (from the listeners/examiners)
- Where does "control without building a new model" stop, given that GWTF trains a rank-2048 LoRA (40 A100-days) and MotionV2V trains a copy of 18 blocks?
- Diffusion Illusions: what's the Vendi/Independence Score exactly, and why optimization rather than Visual Anagrams-style sampling?
- MAGICK: $30k annotation, so how many were reviewed vs kept? Seed variance on 36 → 33?
- GWTF: what does your warp buy over InfRes (both have I≈0)? Answer: the lowest warping error at about the same speed.
- MotionV2V: baseline fairness (GWTF adapted via RAFT, ReVideo run with the whole frame editable), author-chosen edits, no error bars.

Full reports: `.scratchpad/study/<section>/final/{listener,examiner}.md`, `.scratchpad/full_r5/story_listener.md`.
