# Style research B (agent 3): InternPresentation, HumanAnimDataFeb2026, Apr5_Vfx_5000iter_LTX23, AutoplayAll, TRITON Presentation
Method: python-pptx XML scan of all 5 decks + 7 deckcraft renders (renders in agents/.scratchpad/renders_agent_3/). Time-limited: only ~7 slides visually inspected; title-less slide stats are from XML.

## 1. Visual style
- Slide size: 13.333 x 7.5 in (16:9) in all five decks (TRITON also 16:9).
- Backgrounds: NOT dark. 2026 decks use PowerPoint built-in gradient backgrounds. InternPresentation = burnt-orange radial gradient (dark orange edges, lighter salmon glow bottom-center) with WHITE text; media slides have a plain white or black strip behind video. HumanAnimDataFeb2026 = light sky-blue gradient (all 19 slides use theme accent4 0F9ED5 background) with BLACK text. Apr5 = plain white, black text. TRITON (2022, grad-school poster-talk) = pure black background, glowing green/white handwritten-ish annotations, "TRITON" title in gradient-fill text over a trident image, QR code bottom right.
- Fonts: Futura Medium for essentially everything in 2026 decks (162 runs Intern, 116 Autoplay, 52 HumanAnim, 30 Apr5). Bradley Hand (handwritten) for scribbled asides in Intern + Autoplay (~37). Bauhaus 93 in 2 Apr5 runs (joke/emphasis). TRITON: Cambria / Cambria Math (equations), Consolas, Nerd fonts. Underlying theme is the default Office theme (Aptos Display) -- he overrides every run with Futura by hand.
- Palette (hex): theme only default Office (accent1 156082, accent2 E97132 orange, accent4 0F9ED5 blue, dk2 0E2841). Explicit run colors are rare: 000000, 670706 (dark red), FFFF00 (yellow highlight), FFC000 (amber). Gradient colors come from built-in PowerPoint backgrounds, not custom hex. So: palette = ONE saturated gradient background + white or black Futura text + occasional yellow/amber/dark-red highlight. No accent-color system, no icons, no cards, no footers, no slide numbers.
- Title placement/size: no real title placeholders (all "Title Slide" layout with free TextBoxes). Section/title text is centered, 40-54pt (48pt most common, 96/72pt for big single-word slides like "Dailies"), starting near the top edge (top 0.0-1.0 in) and often hugging it. Body text 28pt (most common), 36pt. Caption-style text on media slides is small (~28pt but sits in a top strip of one or two lines). Left half text/right half media split used on use-case slides (Intern 33: picture left 5.1in wide at x=1.3, text right at x=6.9).
- Text vs media: extremely media-heavy. Most slides (about 75%) are ONE embedded video (or two stacked/side-by-side videos) plus 0-2 lines of caption, many slides have NO text at all (Intern 8-14, 19-22; HumanAnim 1,6-8; Apr5 2,3,10,11). Videos are full-bleed or nearly so (e.g. Vista4D_A/B each 13.3in wide stacked, 'RickRollNoise' video 27.6in wide cropped by two white rectangles to show a window). Videos are real MP4 media shapes with autoplay animation (timing tag on ~75% of slides) -- that is why the files are 1GB+. Static pictures used for screenshots/diagrams (p1-p3 per slide).
- Animations/transitions: Intern 30 of 45 slides have <p:timing> (autoplay video triggers), 1 transition total. AutoplayAll: 30/37 timing, 0 transitions. Apr5 9/14, HumanAnim 14/19. TRITON: transitions on all 15 slides (morph-like, 2022 style) + builds. So: modern decks = autoplay only, no decorative transitions. Do not add fancy transitions.
- Recurring motifs: (a) "Source | Point cloud render | Vista4D" style labeled side-by-side comparison inside the video itself (labels baked into the video frame, tiny). (b) Hand-written Bradley Hand asides. (c) White block arrows over footage (Intern 27: two white arrows from "Different Roll" to two film frames). (d) Italic + underline emphasis inside centered text ("*very* high quality", underlined italic "they come in pairs!"). (e) Bracketed speaker stage directions typed on slide: "[Show dailies]", "[show DAG]", "[show busc dailies]", "[Label: Same scene, same take, different roll]". (f) Credit lines: "Credit: Tobias Gerts", "(Credit of Vidit)". (g) Cheap joke video titles ("RickRollNoise"). (h) Rounded-corner video frames with thin outline (HumanAnim, Apr5).
- Weaknesses worth knowing (not to inherit): captions tiny and cramped over videos, inconsistent title position slide to slide, no consistent layout.

## 2. Writing voice (VERBATIM)
Titles / snippets, in order of decks:
1. "I am Ryan Burgert" (appears as a joke label on slides 0,3,5 of Intern; the title slide literally says "I am Ryan Burgert" and below "Ryan Burgert")
2. "Go-with-the-Flow / CVPR 2026 Oral!"
3. "I worked on Go-with-the-Flow and other papers"
4. "GenFlow: A general purpose video editing AI"
5. "Credit: Tobias Gerts / Done in ComfyUI / Used latest 1080P GenFlow Ckpt"  (labels: "First Frame | Driving Video | Edited Video")
6. "Nanobananna Can Edit Many Frames at Once" / "TLDR: We used NanoBanana to create a video training dataset"
7. "Vista4D / CVPR 2026 Highlight! / Choose your camera angles in post!"
8. "Last CVPR we published Vista4D, a CVPR highlight"
9. "It can retarget camera angles… / But can keep parts of the scene the camera doesn't see!"
10. "Believe it or not, THIS was the data Vista4D trained on"
11. "However, it turns out that people that shoot movies have Dailies"
12. "Netflix has BETTER data: Dailies"
13. "Same Scene / Same Take / Different Roll / Synchronized in time / Differing in space"
14. "Dailies are very high quality / 4K+ / 16 Bit Depth / Very abundant / And mosty importantly, they come in pairs!"
15. "Over 300 productions, with thousands of hours of paired footage"
16. "From the dailies, we want this training data:"
17. "Many pairs can be >10 Minutes Long" / "But not all of each video is useful"
18. "Some issues with Dailies: The default proxies have color mismatches (We currently solve this by generating new proxies from EXR's)"
19. "We need actor ID's so we can train our model to memorize them"
20. "Turns out Busc did this too [show busc dailies]"
21. "We finished busc, now to move onto all dailies!" / "I am working on scaling this up beyond Busc!"
22. "WAN Animate Replace: The eye gaze direction does not match. Relative eye movement to first frame is ok though...which is to say, it doesn't lol but that's ok here..."
23. "WAN Animate: We can get away with a REALLY low number of diffusion steps"
24. "Prompt does not matter at all for WanAnimate"
25. "Janky animations at first...but synced nonetheless..."
26. "Facial animations are...not great. The jacket bends with the jaw..."
27. "Shocking result: i2v upscaling adds texture from the first frame really well??? Also...inference is being..." / "I wonder if we could use I2V guidance alone to get a giant boost…" / "(this is a failed attempt, it barely changed it...)"
28. "Accidental extrapolation – tried to do 2410 frames on a video that was shorter lol. It worked!"
29. "We have good results now..."
30. "Had FSDP Problems...inference FSDP not natively supported" -> "Solved: Uses nearly 1/5 the VRAM (this is just stage 1)" ; "Result: Added FSDP Inference Support / 1/5 The VRAM / 1.7x Inference speed"
31. "Doesn't (yet) work as well on non-VFX videos"; "FSDP Problems..."
32. TRITON (2022): "Better than CycleGAN!", "Simulations -> Photos!", "Totally unsupervised!", "Works with any 3D simulator!", "*Now with more ducks!"; "Neural Neural Textures / Make Sim2Real Consistent"
Voice summary: casual lab-meeting voice. Plain declarative sentences, trailing ellipses ("...but synced nonetheless..."), "lol", "Believe it or not", "Shocking result:...???", self-deprecating honesty about failures ("this is a failed attempt", "Janky", "FSDP Problems..."), typos left in ("mosty", "Nanobananna"), CAPS for emphasis (BETTER, REALLY, THIS), exclamation marks for wins ("CVPR 2026 Oral!"), few outright questions, lists of 2-4 very short items. Setup->reveal narrative pacing ("People that shoot movies have Dailies" -> "Netflix has BETTER data" -> "they come in pairs!"). Humor via meme/self-reference ("I am Ryan Burgert", RickRoll noise, ducks). NO "not X but Y" constructions found; no buzzwordy bullet language; no sentence-case corporate titles. Slides are written as captions to the video, spoken text carries the argument.
Words per slide: text slides 5-25 words (median ~10); title-only slides 3-8 words; ~25% of slides have zero words (pure video). Max seen ~45 words (Apr5 results slide / Autoplay CFG grid caption). Intern deck: 45 slides, roughly 220 words total on slides.

## 3. Talk structure
- InternPresentation (Netflix/Interpositive-style intern talk, 45 slides): opens with a joke self-intro ("I am Ryan Burgert" x3, RickRoll-noise video behind it, then Go-with-the-Flow figure), Contents slide (Go-with-the-Flow / Vista4D / GenFlow / Dailies Processing). Order of body: papers first (GWTF oral, GenFlow, Vista4D) then problem pivot "However... Dailies" then data pipeline issues and scaling plan. Transitions between sections are single big-text slides (e.g. "Vista4D / CVPR 2026 Highlight! / Choose your camera angles in post!", "Netflix has BETTER data: Dailies"). Ends on "Early model for Busc (Credit of Vidit)" -- two result videos, no thank-you/Q&A slide. Next-steps slide: "We finished busc, now to move onto all dailies!".
- Apr5 / AutoplayAll / HumanAnim = internal lab update decks (title with project + date -> "Updates:" bullet list -> result videos each with one caption -> problems). Open: title slide ("FlowGen LTX2 Updates, Feb 17, 2026, Ryan Burgert" / "GenFlow April"); then "We have good results now..." / "Updates:" list. End abruptly on last result video. Autoplay = HumanAnim + FlowGen update concatenated (slides 20-36 duplicate HumanAnim 2-18).
- TRITON: poster-style title with QR code (tritonpaper.github.io), then method built up via diagram animations; end on architecture diagram with no conclusion slide.
- None have an explicit overview/outline except Intern slide 1; none have a thank-you slide; no references slide.

## 4. Reusable slides for thesis papers (0-based indices)
Caveat: none of these five decks contain Peekaboo, Diffusion Illusions, or MAGICK. MotionV2V is not obviously present either (GenFlow in Intern/Apr5/Autoplay is an unreleased general video-editing model; check with Ryan if GenFlow == MotionV2V). Check the other decks (GenFlowMay4.pptx, DiffiluSigPresent.pptx, SIGGRAPH_DiffiluPoster.pptx, AdobeExitTalk.pptx, Presentation_New.pptx) -- not in my scope.
- Go-with-the-Flow (CVPR 2026 Oral): InternPresentation.pptx
  - 2: section title "Go-with-the-Flow / CVPR 2026 Oral!" (text only, orange)
  - 3: 'RickRollNoise' video ("Our Warped Noise", full-bleed noise) -- good visual hook for warped-noise explanation
  - 5: GWTF_Figure media (12.3in wide) with caption "I worked on Go-with-the-Flow and other papers" -- the main GWTF results/teaser video
  - 4: another video slide (no text), likely GWTF/noise result
- GenFlow (video-editing model results, if relevant): InternPresentation.pptx 6 (title "GenFlow: A general purpose video editing AI"), 7 (First Frame | Driving Video | Edited Video, ComfyUI, credit Tobias Gerts), 8-14 (full-screen video results, no text), 15 (NanoBanana-generated training dataset). Apr5_Vfx_5000iter_LTX23.pptx 2,3,10,11 (video-only result slides), 6 (FSDP: 1/5 VRAM, 1.7x speed; two rounded video frames side by side), 12/13 (ICLoRA stage 2 tiled ablation). AutoplayAll.pptx 2-8 (good results videos), 9-15 (keyframe count vs CFG/CDI ablation grids, 13 = "I2V CFG: 4 Passes" alpha/keyframe grid), 16-17 (accidental extrapolation, 2410-frame extension).
- Vista4D (CVPR 2026 Highlight, camera retargeting): InternPresentation.pptx 16 (section title), 17 (two stacked videos "Source video | Point cloud render | Vista4D"), 18-22 ("It can retarget camera angles... but can keep parts of the scene the camera doesn't see!"), 23 (mix and match subjects from different scenes), 24-25 ("THIS was the data Vista4D trained on"), 37 (reminder about Vista4D). Not one of the five named thesis papers, but a CVPR paper he may want.
- Dailies/Busc data pipeline (Netflix intern work; likely relevant if thesis includes data): InternPresentation.pptx 26-28 (same scene/take/different roll slides with clapperboard photo and arrows, very strong), 30 ("Dailies are very high quality"), 31 ("Over 300 productions, thousands of hours"), 32 (target training data), 40-41 (dynamic/static segmentation with SAM3), 42 (pipeline DAG + scaling plan), 43-44 (early Busc model results).
- Human animation: HumanAnimDataFeb2026.pptx 2-13 (WAN Animate Replace tests, steps/resolution/prompt ablations), 14-18 (Synbody 3D dataset). Probably not thesis material.
- TRITON (2022 Stony Brook sim2real; likely outside proposal): TRITON Presentation.pptx 0 (title with trident, black, QR), 3-5 inference black-box, 6 global temporal consistency, 9-14 neural texture pipeline diagram.

## Takeaways for the new deck (to inherit his style)
- 16:9 13.333x7.5, Futura (Medium) for all text, one big gradient background color per section (orange radial like Intern, or blue like HumanAnim), centered 40-54pt white/black text, very few words, big autoplaying video, captions that are one sentence, bracketed [show X] cues allowed, bold/italic/underline for emphasis, occasional handwritten aside, credit lines, a joke or two. Avoid cards, icons, footers, and any "not X but Y" phrasing.
