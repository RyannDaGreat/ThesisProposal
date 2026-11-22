# Style research A (DiffiluSigPresent, GenFlowMay4, AdobeExitTalk, NetflixMar2026)
Method: raw XML text/media counts for every slide (zipfile, no media loaded) + deckcraft-cli renders of ~15 slides
(renders in presentation/agents/.scratchpad/renders_agent_2/). Deadline-limited: MAGICK material not found in these 4 decks.

## 1. Visual style
- Size: all four 16:9, 12192000x6858000 EMU (13.333in x 7.5in).
- Backgrounds: Diffusion Illusions = plain WHITE default Office theme, black text. Adobe talk = mixed: black/white
  default slides plus a few themed ones (dark purple gradient, hex 120027 / 150010, e.g. slide 45 Pixelwise-Keying;
  full-bleed black-hole image behind "Super Massive Matting Dataset", slide 12). GenFlow/Netflix = white with a
  pale yellow-to-white gradient on some; internal-update style, not polished.
- Fonts: titles/body are the Office default (renders as Calibri-ish) in Diffilu. Adobe uses Century Gothic for themed
  slides. Futura Medium and Andale Mono appear in all decks (code/labels). Diffilu also has Bodoni 72 Book, Consolas.
  No custom brand font. Mostly un-fancy sans; centered titles.
- Palette (hex by frequency): FFFFFF, 000000 text; FF0000 red (arrows, failure cases, emphasis, 13 uses in Diffilu);
  00B050 green and 0070C0 blue (labels, accents); FFFF00 yellow highlight (Adobe, Netflix); FFC000 orange; 7030A0/9A2AA0
  purple (Adobe theme). Diagram boxes: navy outline (about 1F4E9A) on light grey fill. Red arrow = "this is the key idea".
- Titles: centered top, ~40pt, short (1-4 words), plain black. Often the SAME title repeats across many consecutive
  slides while the content builds ("Score Distillation Loss" x13, "Pixelwise-Keying" step 1..4, "Phase 2: Dream Target Loss"
  x15). Subtitle line under it ~18-20pt ("Provides a gradient from a frozen diffusion model").
- Text vs media: media-dominant. Diffilu: 1-9 pictures/videos per slide, text 0-25 words. Typical slide = title + 1-3
  images side by side (e.g. 2 big squares for "Diffusion Illusions" slide 4, 7-square grid "Twisting Squares", slide 7).
  Adobe: slides with 14-95 pics (grids of generated images). Netflix/GenFlow: 1-6 videos per slide, text is a one-line
  caption, often handwritten-feeling lab-notes comments (italic gray 2nd line).
- Video/GIF: heavy. Videos per slide counted: Diffilu up to 14 (slides 7, 71), GenFlow up to 12 (slide 15), Netflix 2-6
  (side-by-side input vs output). Videos autoplay via <p:timing> (flag A below). Looping short clips are the primary result format.
- Layout patterns: (a) grid of N result clips with one caption line under; (b) pipeline diagram left-to-right with +, ->
  arrows between images (Score Distillation slides 29-37, 33 best example); (c) full-bleed photo with centered white text
  (takeaway slide 57: photo of fanned prints with "The takeaway:"); (d) before/after pairs ("Original Crude Video" / "Our Output");
  (e) QR code (diffusionillusions.com) top-right corner on many Diffilu slides.
- Animations: nearly every slide in Diffilu/Adobe has <p:transition> (T) , around 60-70 of 77 Diffilu slides; many video slides also
  have timing/autoplay (A). Use is mostly slide-to-slide fades/pushes, and builds by duplicating slides (title repeated,
  content added) rather than in-slide animations.
- Recurring motifs: emoji as icons (fire = trainable, snowflake = frozen); red arrows labeled with the update equation;
  "(that's me!)" next to own name; speaker notes embedded as slides (Diffilu 61-68 are draft/notes slides, e.g. "Then also
  show how we can make them and breif fabrication...").
- Internal updates (GenFlow, Netflix) = left-aligned plain lists, "Updates:" bullets, "[DONE]", "Currently Training" - NOT the style
  for a proposal talk. Style to inherit is Diffilu SIGGRAPH + Adobe talk.

## 2. Writing voice (verbatim)
Short, plain, conversational, a bit of humor, honest about failures. No marketing language. Question-driven.
Titles/headlines:
- "Diffusion Illusions: Hiding Images in Plain Sight"
- "We use Stable Diffusion to generate optical illusions with zero training"
- "Flip Illusions" / "Twisting Squares" / "Hidden Overlays" / "Rotation Overlays"
- "diffusionillusions.com + live demo after talk!"
- "How to Make Them: We optimize the prime images"
- "Score Distillation Loss: Provides a gradient from a frozen diffusion model"
- "What if we use two score-distillation losses at once, one for each prompt?"
- "What if we use four text prompts (four derived images)?"
- "Phase 2: Dream Target Loss: Score distillation loss alone does not create smooth images"
- "Using SDEdit makes them cleaner! We call these images 'Dream Targets'. But...it is no longer a valid illusion!"
- "Overlay illusions can be made on a regular laser printer. $$ They're very cheap to make! $$"
- "The takeaway: Diffusion models can generate optical illusions! We hope to inspire even more work in this area"
- (notes slide) "Hmm, they look messy...what if we use SDEdit to clean them up?" / "Cool, but now they're different" / "Hmm! They look better...let's do it again! And again! And again! That's dream target loss."
- Adobe: "But...how?" / "But... Firefly only does RGB! (no transparency)" / "Some are really good! Until you notice the white blob in her hair..."
- Adobe: "...the trick revealed: '... isolated on a solid greenscreen background'"
- Adobe: "Super Massive Matting Dataset 100k+ High Detail RGBA Images"
- Adobe: "'Pine needles on a greenscreen' maybe not the smartest idea..." -> "'Pine needles on a bluescreen' much better!"
- Adobe: "Cons: Color contamination, low-detail / Pros: Can separate a green apple from a greenscreen"
- Adobe: "Live Demo. Annotate up to 1000/hr. Currently 20,000 images (and counting!)"
- Netflix/GenFlow lab voice: "Shocking result: i2v upscaling adds texture from the first frame really well???"
- "Accidental extrapolation - tried to do 2410 frames on a video that was shorter lol. It worked!"
- "(this is a failed attempt, it barely changed it...yet the I2V Upscaling process ...)"
- "Why? Additional Control! ... Unlike VACE, our performance will NOT degrade as we add more modalities."
- "Rank 32 LoRA-Mux (Merging 100 community LoRA's - no training involved)"; "Proof of Concept: This is a single Rank 32 Lora + 6 Different Modes. Same Prompt + Same Seed for All of Them"
Words per slide: result slides 0-10 words; explanation slides 15-30; definition slides ("Our Illusion Definition") up to ~60 (the one dense outlier).
Patterns: ellipses ("...But working directly in pixel-space introduces heavy artifacts"), "!" and "?", "What if...", "But...",
self-aware asides ("lol", "(that's me!)"), uses "we" for the work. No "not X but Y" constructions found.

## 3. Talk structure
- Diffusion Illusions (SIGGRAPH): opens title + authors (with "(that's me!)"), repeats title over a pair of striking results
  (slides 2-4) then one-sentence claim "We use Stable Diffusion to generate optical illusions with zero training" (4-5).
  Demos first: Flip Illusions, Twisting Squares, Hidden Overlays, Rotation Overlays (6-13), plug website + live demo (14).
  THEN formal definition (15-26), THEN method in two phases: Score Distillation (28-43, long incremental build of one
  diagram), Dream Target Loss (44-49). Then fabrication, failure cases, quantitative eval (GPT4-V confusion matrix, 50-52),
  related work (Arcimboldo, Visual Anagrams, 53-56). Ends with takeaway on a photo (57), Thank-you/authors (58), "I hope this
  continues to encourage others in this field!" (59). Slides 61-76 are drafts/notes/backup.
  Pattern: results hook -> definition -> method built piece by piece -> evaluation/failures -> related work -> takeaway.
- Adobe exit talk: opens with title + authors ("Firefly-alpha"), poses the puzzle (How do you get alpha from RGB-only Firefly? "But...how?" x several)
  with RGBA diagram, shows failures of prior approach, reveals the trick (greenscreen), then a stack of "how it works" subquestions
  ("Where get prompts? How choose screen color? How do chromakeying?"), each answered by a section divider + 3-6 slides, live demo
  of annotation tool; ends on next project (Layer-Based Image Generation, Peekaboo losses 1-3 + Dream loss 4, slides 51-55).
- GenFlow/Netflix: not structured talks (update notes), skip for structure.

## 4. Reusable slides (0-based index in the .pptx slide order)
Peekaboo:
- AdobeExitTalk 51-55: "Layer-Based Image Generation" ("A cat on a bench in the park", Peekaboo Loss 1,2,3 + Dream Loss 4: composite vs per-layer losses).
- DiffiluSigPresent 75: draft slide "Label Peekaboo Loss Somewhere Here / Then Pseudocode (super duper short!!)" (16 pictures; check it).
Diffusion Illusions (best source: DiffiluSigPresent):
- 4: two giant illusion results (angel/penguin flip pair), 7: "Twisting Squares" 7-video grid, 6: "Flip Illusions" videos,
  8-13: Hidden Overlays + Rotation Overlays (video), 15/17-19: Illusion definition with prime/derived images,
  25: "How to Make Them: two phase process", 28-37: Score Distillation Loss build (33 = full diagram, cleanest),
  40-41: Fourier feature params + optimization-from-noise video, 42-43: two/four prompt videos,
  47-49: Dream Target Loss steps (SDEdit cleanup), 50: laser-printer fabrication, 51: failure cases, 52: GPT4-V quantitative confusion matrix,
  53-56: related work, 57: takeaway on photo, 69-76: extra video/result slides (71 has 14 videos, 7 pictures).
MAGICK: not found in these four decks (try other ref_pptx files, e.g. InternPresentation/AlphaGenFigures).
Go-with-the-Flow:
- GenFlowMay4 5: lists "Motion Control - Go-with-the-Flow Based" (just a bullet); GenFlowMay4 14: WanAnimate output = GenFlow control signal; 15: LoRA-Mux 6-mode video grid (6 results). No dedicated GWTF paper deck here: look at AutoplayAll.pptx / other refs.
- NetflixMar2026 7-9, 12-16 ("FlowGen LTX2"): pulse-mask keyframe results, 8 = 5/50%/100% keyframes comparison, 15-16 = extending a short input video (accidental 2410 frames).
MotionV2V (closest relevant): NetflixMar2026 10-11 ("Original Crude Video" vs "Our Output"), 13-14 CDI vs keyframes grids; GenFlowMay4 1-2,7-8 EditAnything LTX2 LoRA, 10 first/last frame conditioning. Not confirmed as MotionV2V paper material - treat as related.
Other: AdobeExitTalk 12 (full-bleed dataset slide) shows his best "big hero" slide; 33-35 Procedural human prompts, 41-45 Pixelwise-Keying 4-step build.
