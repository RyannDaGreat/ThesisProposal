# MotionV2V: talk track + slide spec

Machine-readable spec (the source of truth for slide building): `presentation/agents/specs/motionv2v.json`. It has 6 slides (one 2-step build) and 624 spoken words.

## The paper in plain words

You have a video, and you want to change how something in it moves without changing anything else. The corgi should win the race. The ball should go through the hoop. The camera should zoom out. Motion-control models like Go-with-the-Flow (GWTF), ATI and ReVideo are image-to-video models. They keep only the first frame and generate the rest, so anything that was not in frame 1 (people walking in, parts of the scene the camera reveals later) gets made up. The usual editing trick of inverting the video and regenerating it also fails, because a motion edit means the output no longer lines up with the input frame by frame.

MotionV2V trains a model to do video-to-video motion edits directly. Real pairs (same content, different motion) do not exist, so we make them. We cut a real clip from a real video and use it as the target, so the model always learns to output real footage. Then we build a fake "motion counterfactual" of the same content. One way: a first/last-frame video diffusion model fills in between two real frames, with an LLM-written prompt like "make him twirl". The other way: temporal resampling (speed changes, shifts, reversal). After either one, we add crops, rotation and zoom. We track 1-64 points with TAPNext in both videos and draw the tracks as colored Gaussian dots on black. Training input: counterfactual video, counterfactual tracks, target tracks and text. Training output: the real clip. The model is a frozen CogVideoX-5B with a ControlNet-style trainable copy of its first 18 blocks (zero-init). At test time the user's real video takes the place of the counterfactual. The user clicks points, the tracker follows them, and the user drags them into target tracks in a GUI.

## Beats and why this order

1. **What the task is** (corgi race, before/after): the committee has to see the edit before anything else makes sense.
2. **Why GWTF can't** (first frame only): this connects to the previous paper and motivates training a new model.
3. **Counterfactual data** (2-step build): this is the real contribution. Step 1 shows that the target is real. Step 2 shows that the input is fake, which is the key idea, in red.
4. **The model at test time** (framework diagram): source tracks, target tracks, frozen model plus control branch. It ties back to the talk's theme, a new handle on a frozen model.
5. **Evidence + limits + status**: two results, the user study, L2 numbers, honest limits, CVPR, no code. Hands off to "any edit".

## Visuals (all opened and checked)

Workspace: `/Users/rburgert/Documents/ThesisProposal/presentation/agents/.scratchpad/explain_motionv2v/`. Crops were made by `presentation/agents/.scratchpad/scratchpad_agent_5.py` (earlier version). The pixel boxes below are in source-image pixels.

- `race_tied.png` (2392x582): from `source/src/5_MotionV2V/teaserv2.png`, box (4006,1343,6398,1925). The middle filmstrip of the teaser's "Alternate Outcomes" panel. It is the original tied race: bichon (pink track) and corgi (red track), 3 frames.
- `race_corgi.png` (2392x582): teaserv2.png box (4006,2015,6398,2597). The bottom strip, an edited output where the corgi ends up in front.
- `race_frame1.png` (794x582): teaserv2.png box (4006,1343,4800,1925). Frame 1 of the tied race.
- `dg_full_real.png` (3840x466): from `datagen.png` (datagen.pdf rendered at 200 dpi), box (152,217,6676,1009). The "Full Real Video" strip: a man walking on a NYC street, with blue and orange tracks.
- `dg_target.png` (3262x957): datagen.png box (0,2326,3262,3283). "(Real) Target Video Clip" strip with its label.
- `dg_counterfactual.png` (3262x974): datagen.png box (3653,4514,6915,5488). "Motion Counterfactual Video" strip: zoomed and cropped, with a different motion and an orange track on the bag.
- `framework.png` (3840x2317): teaserv2.png box (0,0,3883,2343). The "Motion Edits Framework" panel: marshmallow scene, input video + source tracks + target tracks (black panel) -> Diffusion Model -> output. The red box on the slide marks the Target Tracks column.
- `basketball.png` (1770x1688): teaserv2.png box (163,2408,1933,4096). Ball bounces off the rim, then goes through the hoop after the edit.
- `retiming.png` (2425x1311): teaserv2.png box (4006,2785,6431,4096). Taxi and truck retiming, before (top) and after (bottom).

Not used: `megacomparisonfigurev2.jpg` (8 comparison rows, too dense for one slide; good for backup), `JitterFigure.pdf`, `successive_edit_horz.pdf` (rendered in the workspace), `editor_gui.jpg` (only 512x358).

**motion_a/b/c.mp4 (from AutoplayAll) are NOT MotionV2V.** They show side-by-side appearance edits. motion_a: a gray untextured boat render turned into a photoreal boat in sunny water. motion_b: a Jack Russell running on a beach turned into the same dog running on snow, with the motion preserved. motion_c: a brown clay-like render of a fish monster turned into photoreal salmon chunks and teeth. motion_b and motion_c have a Gemini/Veo-style sparkle watermark in the corner. Frames are in `frames/motion_{a,b,c}_tile.png`. They might fit the future-work "any edit to any video" slide, but only if Ryan confirms they are his own (GenFlow?) and not Google's Veo output.

## Slides

The full speech and element rects are in the JSON. Summary:

1. **Motion Editing**: tied race strip, a red arrow down, the corgi-wins strip, and the red text "Make the corgi win". The speech opens from GWTF: "GWTF makes new videos. But what about the video you already have?"
2. **Why not GWTF?**: frame 1 in a red box, with the red text "Everything after frame 1 gets made up". Covers I2V hallucination and why inversion fails.
3. **Motion Counterfactuals (a)**: full real video, an arrow, the real target clip. "The target is always real."
4. **Motion Counterfactuals (b)**: adds a red arrow to the counterfactual strip and the red text "Fake in, real out". Covers interpolation with a prompt, temporal resampling, crop and zoom, tracks, and training I/O.
5. **The Model**: framework panel with a red box on the target tracks. Covers source/target tracks, dots on black, CogVideoX frozen + ControlNet-style copy of 18 blocks.
6. **Results**: basketball and retiming, with the red text "Picked about 70% of the time over 3 baselines". The speech covers the user study, L2, limits, CVPR 2026, no code, and the handoff to "any edit".

## Likely committee questions (answers verified in the chapter / impact_verified.md)

- **Why not just use GWTF or another I2V model with the first frame?** It is first-frame only, so content after frame 1 gets hallucinated. Slide 2.
- **Why not DDIM inversion plus editing?** A motion edit breaks pixel correspondence between input and output, and inversion-based editing depends on that correspondence. Slide 2.
- **Where do training pairs come from?** A real clip is the target. The counterfactual is made by first/last-frame interpolation with an LLM prompt or by temporal resampling, then crops, rotation and scale. Tracks come from TAPNext, N~U(1,64) points. Slides 3-4.
- **Doesn't training on generated video teach it to output generated-looking video?** No. The fake video is only ever the input. The target is always real. Slide 3 (said explicitly).
- **Architecture / compute?** Frozen CogVideoX-5B. The trainable copy of the first 18 blocks has zero-init MLPs (ControlNet-like, inspired by DiffusionAsShader). Inputs are patchified on 48 = 3x16 latent channels. 8 H100s for one week, 15k iterations, batch 32, 480x720, 100k videos. Slide 5 (the speech names the frozen model and the 18 blocks; the rest is for Q&A).
- **The input isn't aligned with the output. How does a ControlNet copy work?** It is empirically surprising, and the paper says so. The control branch takes the input video and both track videos as separate conditioning. Q&A only.
- **Numbers?** User study: 41 participants, 20 videos, a 4-way choice vs ATI (Wan2.1), ReVideo and GWTF (Wan2.2). Ours / ATI / ReVideo / GWTF, in %: content 70/24/1/5, motion 71/24/2/3, overall 69/25/1/5. On 100 test videos (split at the midpoint, second half reversed, so ground truth exists): L2 0.024 / ATI 0.038 / GWTF 0.067 / ReVideo 0.096. LPIPS 0.031 / 0.072 / 0.088 / 0.106. Slide 6 has the study and L2. LPIPS is for Q&A.
- **Limitations?** Past about 20 points it stops following them. Iterative edits drift (subject drift, blamed on base-model quality). Pixel-perfect anchors make it copy the original, fixed by adding U(-2,2) px jitter at inference (JitterFigure). Future work: synthetic 3D counterfactual data. Slide 6 has the first two. Jitter is for Q&A.
- **Is this the first motion editor?** No. MotionEditor (2023), MotionFollower and ReVideo (2024) came earlier. The scoped claim is the first video-to-video, general-object motion editor. Lee et al. (CVPR 2026, 3D point tracks, dense) is concurrent. The talk never says "first".
- **Does it build on GWTF?** No. GWTF is only a baseline. The connection is the motivation (first-frame limit), not shared code. Slide 2.
- **Impact?** CVPR 2026 (pp. 35988-35997), with Google. About 11 citations, all positioning cites. The GitHub repo (~58 stars) is a project page only, with no code or weights. Slide 6 says plainly that the code isn't out.
- **Camera control and time?** Camera edits use MonST3R point-map reprojection to make target tracks. It can also retime (duck appears later). Retiming is on slide 6. Camera control is Q&A (the swan example in teaserv2.png is available for backup).

## Handoff

The section ends with "motion is just one kind of edit. Next, I want any edit." The future-work section picks this up: "turn a general image-to-image editor into a general video-to-video editor, basically Nano Banana but for video" (`8_future_work.tex`), shown concretely as I2I2V2V plus LoraPlexer. Neither name appears in the thesis; they come from `presentation/scrapnotes.txt:35-42`.

## Uncertain

- Whether the race "bottom strip" is literally the corgi-wins output. The teaser caption says the edited strips are "one where the bichon wins and another where the corgi wins". In the bottom strip the corgi is clearly in front in the last frame, so I labeled it corgi-wins.
- Where motion_a/b/c come from (see above).
- The "about 70%" is the 4-way-choice share (69-71% across 3 questions). It is not a pairwise win rate.
