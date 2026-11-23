# Go-with-the-Flow: explanation + slide spec

Machine-readable spec (the source of truth for slides and full speech): `presentation/agents/specs/gwtf.json`. 6 slides, 593 spoken words (~4.4 min at 135 wpm).

Round 3 revision (examiner r2, 5/8, "right story, no mechanism"):
- **The thesis diagram's densities are wrong.** Under Algorithm 1 (`source/src/4_GWTF/sec/3_method_thesis.tex:26-37`, α = p(v)/deg(v)), q2 has degree 3: a contraction edge to q'2 and expansion edges to q'1 and q'3. So α = 1/3 and p' = (1, 1/3, 7/3, 1/3), which sums to 4 like the input. The figure's .5/1.5/.5 sums to 3.5. I redrew it with PIL as `.scratchpad/explain_gwtf/algo_graph_fixed.png` (780x518): density renamed p, holes ringed in orange, blue dashed backward arrows, green forward arrows. Ryan should know the thesis figure (`fig/algo_diagram_2_layers.png`, caption at `3_method_thesis.tex:73`) has this error.
- Slide 4 speech now says the key idea: every source splits into one independent piece per edge (contraction included), each piece is used exactly once, so no two output pixels share randomness. That is the Gaussianity argument.
- Slide 3: variance reason (average of 4 → variance 1/4 = gray; shared inputs = blurry), p = 0 vs p = 0.84, LPIPS labeled DeepFloyd SR, with SR LPIPS on the panel labels.
- Slide 5: windmill ablation (untuned CogVideoX roughly follows the motion but frames fall apart, `X_suppl_thesis.tex:78`) as the reason to fine-tune; "rank-2048 LoRA, 40 A100-days"; red on-screen "DAVIS image-to-video mIoU: 0.52 → 0.74" (0.52 = original CogVideoX, prompt only, `4_experiments_thesis.tex:195`). The user study is stated as "our own 40 examples".
- Slide 6: 4 limitations on screen, popularity cut to one dated line; "renderer" changed to "motion-to-video stage".

Round 2 revision (after examiner 5/8, speech-only critiques): slide 3 now gives benchmark Moran's I (nearest 0.26, bilinear 0.30, ours 0.0001 ~ fresh noise; the panel labels show these) and backs "it hurts" with DeepFloyd SR LPIPS 0.29 -> 0.6 instead of "garbage", plus "each frame i.i.d., only time correlated". Slide 4 states the density-weighted sum / divide by std, each piece to exactly one pixel, fresh noise for unreached pixels, and the per-frame i.i.d. guarantee. Slide 5 names gamma, its direction (lower = stricter) and defaults, the LoRA and 40 GPU-days, latent resolution (8x8 px, every 4th frame), the 3 user-study baselines, and DL3DV mIoU 0.83 vs 0.71 in place of FID. Slide 6 opens with where it loses (DMT, T2V DAVIS mIoU 0.85 vs 0.70) and limits, and names WonderPlay and NewtonGen as renderer users.

## Plain explanation

A video diffusion model starts from a block of random Gaussian noise (one frame of static per video frame) and denoises it. The prompt is a tiny input; the noise is the huge one and already decides a lot of the output, including how things move. Text can't say which way, how far, or how fast something moves, so Go-with-the-Flow puts the motion into the noise instead. Take a video, compute its optical flow (where each pixel moves between frames), and move the noise along that flow, so the noise "contains" the motion while each frame still looks like pure static.

You can't warp noise like an image. Nearest-neighbor copies noise pixels into smeared streaks; bilinear averages them into blurry gray. Both become spatially correlated (Moran's I ~0.24-0.30 vs 0.00014 for ours), and a diffusion model only knows uncorrelated static, so output quality collapses (DeepFloyd SR LPIPS 0.60 vs 0.29).

The algorithm treats noise pixels as particles. Frame by frame, each particle moves forward along the flow. Where several land on one pixel (contraction) they are summed and rescaled to unit variance, and a per-pixel density records how much noise got packed in. Where the scene stretches and leaves holes nobody landed on (expansion), the hole pulls from the previous frame along the backward flow, and the source pixel is split into independent pieces with conditional white-noise sampling (from How I Warped Your Noise, HIWYN). Proven: i.i.d. Gaussian in gives i.i.d. Gaussian out. Linear time, 2.14 ms/frame at 1024x1024, 26x faster than HIWYN (55.2 ms), faster than real time.

Training: warp noise for 4M videos from their RAFT flow and fine-tune CogVideoX-5B (T2V and I2V) with its own training pipeline; the only change is warped noise in place of Gaussian noise. No new parameters. Warped noise is randomly mixed with fresh noise (degradation gamma), which gives an inference knob for how strictly motion is followed (~0.5 default). At inference the flow can come from anywhere: dragged polygons (cut-and-drag), another video (motion/camera transfer), a crude 3D render, depth warping, or an edited first frame.

## Beats and why each visual

1. **What about motion?** Handoff from MAGICK. Cat input frame + quoted prompt, arrow to a Gaussian noise tile. Sets up "the noise is the big input." Cat frame is the same cat that appears in the results grid on slide 5, so the payoff is visible.
2. **Remember the RickRoll?** Pays off the cold open. Ryan's own 3-panel video (Input Video | Optical Flow | Our Warped Noise), labels baked in. One red line: each frame is still pure static.
3. **Just warp it?** Why a new algorithm. Four panels cropped from the thesis roller-coaster figure (nongauss_vis.png): input, nearest (streaks), bilinear (blur), ours (static), ours boxed in red. Moran's I numbers in speech.
4. **Noise as particles.** The mechanism. Thesis algorithm diagram with legend cut off, flattened onto white; speech walks through green forward arrows (contraction, density d sums), circled holes and blue dashed backward arrows (expansion, density split). Red line: Gaussian in, Gaussian out, 26x faster.
5. **Just swap the noise.** Training + applications. Ryan's results video (6 cells: 2 cut-and-drag, first-frame edit, I2V camera control, T2V motion transfer, turntable 3D-to-video). Speech names the cells and gives user study + FID.
6. **What became of it.** Impact + limits + handoff to MotionV2V.

## Assets (all checked by eye)

Workspace: `/Users/rburgert/Documents/ThesisProposal/presentation/agents/.scratchpad/explain_gwtf/`

| file | what it shows | source / crop |
|---|---|---|
| crop_cat_input.png (720x480) | two cats on windowsill, cut-and-drag input frame | `gwtf_results.mp4` frame at 1.5 s (`results_full.png`, 3430x2084), box (50,394,770,874) |
| crop_cat_output.png (720x480) | same, orange cat yawning (unused, spare) | same frame, box (970,394,1690,874) |
| crop_gaussian_noise.png (384x384) | RGB Gaussian static, std 0.25 around gray, seed 0 | generated |
| crop_coaster_{input,flow,ours,nearest,bilinear,hiwyn}.png (1152x590) | roller coaster, its flow, and 4 warping methods | `source/src/4_GWTF/fig/nongauss_vis.png` (3456x1272, 3x2 grid of 1152x636), label bar 46 px cut off. Bottom ~2 px has a thin dark line. |
| algo_graph_fixed.png (780x518), used on slide 4 | redrawn bipartite graph, correct densities p=1 -> p'=1, 1/3, 7/3, 1/3 | PIL, scratchpad_agent_4.py |
| crop_algo_graph.png (780x518), superseded | thesis graph with WRONG densities .5/1.5/.5 | `fig/algo_diagram_2_layers.png` composited on white, box (185,0,965,518) |
| assets/videos/gwtf_rickroll_warped_noise.mp4 | 40 s, 1046x284, Input Video / Optical Flow / Our Warped Noise (Rick shots incl. a shoe close-up and sunglasses shot) | InternPresentation index 3-4 |
| assets/videos/gwtf_results.mp4 | 3.3 s loop, 3430x2084, title + 6-cell results grid | InternPresentation index 5 |

**motion_a/b/c.mp4 (AutoplayAll) are NOT Go-with-the-Flow results and are not used.** Each is a side-by-side input|output: motion_a = dark crude CG boat render -> photoreal boat in rough sea; motion_b = stock dog running on a beach (iStock watermark) -> same dog running on snow; motion_c = crude CG chunks of salmon/fish flesh over blue water -> photoreal splashing salmon chunks. These look like render-to-photoreal / video-edit results, most likely GenFlow (Eyeline, "general purpose video editing AI" per InternPresentation index 6). Unverified, ask Ryan.

## Likely committee questions

| question | answer | slide |
|---|---|---|
| Why not bilinear-warp the noise? | Interpolation correlates neighboring noise: Moran's I 0.24-0.30 (p=0) vs ours 0.00014 (p=0.84); K-S 0.17-0.37 vs 0.060. Model sees out-of-distribution noise, quality drops (DeepFloyd SR LPIPS 0.55-0.62 vs 0.29). | 3 |
| What's new vs How I Warped Your Noise (HIWYN)? | HIWYN warps each frame from frame 0 by polygon rasterization and upsampling; cost grows with frame count. Ours warps frame to frame with pixel-level contraction/expansion + density, O(D) per frame (edges <= 2D). 2.14 ms vs 55.2 ms at 1024^2. Borrows HIWYN's conditional white-noise sampling for the split. That speed is what makes noise-for-4M-videos training feasible. | 4 |
| Is the output truly Gaussian? | Proposition: i.i.d. N(0,1) in -> i.i.d. N(0,1) out (proof in appendix). Contraction and expansion computed together to avoid cross-correlation; renormalize by sqrt of summed squared weights. | 4 |
| Why does fine-tuning on structured noise work at all? | The model learns that noise correlation over time = motion correspondence; frame-wise the noise is still standard Gaussian, so the base model's per-frame prior is kept. Original CogVideoX-5B with no warped noise: mIoU 0.52 vs ours 0.74 on DAVIS I2V. | 5 |
| How does it handle latent space? | Noise warped in pixel space, then downsampled to CogVideoX latents: 8x8 mean-pool x8 (keeps unit variance), 4x temporal nearest. | (not on slide; answer verbally) |
| What is the strictness knob? | Degradation gamma: Q <- ((1-g)Q + g*fresh)/sqrt((1-g)^2+g^2), random during training. Lower gamma = tighter motion. 0.5-0.7 for cut-and-drag, 0.2-0.5 for motion transfer. Careful: the paper's ablation sentence says "as gamma increases, control becomes tighter", which is backwards; the table (DAVIS I2V mIoU: g=0.9 0.50, 0.8 0.68, 0.5 0.74, 0.4 0.74, 0.2 0.74) shows lower = tighter, and the gain plateaus below 0.5. | 5 |
| Why not InfRes, which is also fast? | InfRes (concurrent, Ryan co-author) runs 2.61 ms vs our 2.14 ms with similar Gaussianity, but worse SR warping error (190.8 vs 152.0) and an unstable background. | (answer verbally) |
| Is it fair to compare a 40 GPU-day fine-tune to training-free baselines? | The trained baselines lose too: DragAnything (user-study set, FID 82.8 vs 74.3, flow err 0.62 vs 0.56), ImageConductor (DL3DV FID 89.2 vs 48.4, mIoU 0.61 vs 0.83), MotionCtrl (DAVIS T2V mIoU 0.47 vs 0.70). Data ablation: 33% / 12.5% of the data gives DAVIS I2V FID 100.1 / 105.2 vs 78.6. | 5 (baselines named) |
| Main numbers vs baselines? | User study (40 people): 82% win cut-and-drag, 90% turntable camera. VIPSeg object motion FID 41.1 vs SG-I2V 61.4 / MotionClone 85.2. DL3DV camera FID 48.4 vs MotionClone 82.7, ImageConductor 89.2. | 5 |
| Where does it lose? | DAVIS T2V motion transfer: DMT (training-free, per-video optimization) has better motion fidelity, mIoU 0.85 vs 0.70, flow err 0.28 vs 0.41. DAVIS I2V FID: original CogVideoX 76.6 vs ours 78.6 (motion control costs a little frame quality there). | not on slide; answer verbally |
| Limitations? | No limitations section in the paper; these are my reading: flow is 2D, so 3D/occlusion only comes through whatever the flow encodes; control is soft (a strong suggestion, not a hard constraint), set by gamma; small objects limited by 8x latent downsampling; needs one fine-tune per base model (40 A100-days for CogVideoX-5B). | 6 (spoken briefly) |
| Compute and data? | 4M videos, 8x A100 80GB, 40 GPU-days, 30k iters, rank-2048 LoRA, lr 1e-5, batch 8. Also works on AnimateDiff (2 days on 8x A100 40GB). | (answer verbally) |
| Relation to InfRes? | Concurrent sibling noise-warping paper (ICLR 2025, Ryan co-author), not a follow-up. Comparable Gaussianity, ours slightly faster (2.14 vs 2.61 ms) and better warping error in SR (152 vs 191). | (answer verbally) |

## Uncertainties

- Citation count 169 comes from `presentation/agents/research/other_papers.md:17` (Nov 2026); the thesis text says "over 115" and intro says 62 (stale). Use 169 only if Ryan confirms.
- InternPresentation index 1 says "CVPR 2026 Oral!"; that is a typo. It was CVPR 2025.
- The cat in the results video: I claim "drag a polygon over the cat's mouth and it yawns" from the input/output frames; I did not confirm the exact polygon. The input frame shows a smeared tail at the bottom (the drag preview), which may draw a question.
- EquiVDM is not mentioned (cut for length). Slide 6's on-slide line names WonderPlay and NewtonGen, and the speech covers both.
- Handoff to MotionV2V is the last sentence of slide 6.

## Round 4 + visual QA changes (final)

- Slide 2: the RickRoll video is re-encoded without its 8 pt burned-in label bar (`.scratchpad/explain_gwtf/rickroll_nolabels.mp4`, crop 1046x268 from y=16). Native 20 pt captions sit above it.
- Slide 3: captions are now 18 pt black text on white above each panel. That fixes the low-contrast "Nearest" label.
- Slide 4: the piece formula `X_i = q/d + (Z_i − S/d)/√d` is on screen. The red line now reads "Pieces are jointly Gaussian with zero covariance, so independent." The speech says density is not what makes the noise Gaussian; it keeps merged regions weighted correctly over long videos.
- Slide 5 layout: 3 video columns, input on top and output below (`cell_{cat,camera,turntable}_{in,out}.mp4`, 720x480 crops of gwtf_results.mp4). On the right are the γ formula and γ 0.9 → mIoU 0.50 / 0.5 → 0.74. Below is the baseline strip; every number is checked against `4_experiments_thesis.tex:173-176,195-209`:
  - VIPSeg FID 41.1 vs 61.4 / 85.2, mIoU 0.75 vs 0.63 / 0.71
  - DL3DV mIoU 0.83 vs 0.71
  - plain CogVideoX 0.52
- Slide 5 speech:
  - pixel-space warp then pool to the latent;
  - "no new modules: the LoRA merges back in, so zero extra inference cost". I used that wording instead of "no new parameters" because a LoRA does add trainable weights during training.
  - the user picks γ at inference;
  - a 40-person study: 82% on cut-and-drag, 90% on turntables.
- Slide 6: the limit now reads "Motion under 8 px or 4 frames is only approximated" instead of "lost".
- Not done (examiner r3 extras): the SR warping-error line (152 vs 164 HIWYN / 191 InfRes), the relighting trap (bilinear warping error 47.5 vs ours 85.8), and the untuned FID 76.6 vs 78.6 on screen. The first two are worth knowing for questions.

## Likely committee questions (final examiner leftovers, not on slides)

| Question | Answer |
|---|---|
| Is 0.52 a controlled ablation? | No. It is the original CogVideoX-5B, untuned, with the same prompt and first frame. The same-weights control is γ=0.9 → 0.50 vs γ=0.5 → 0.74: same LoRA, with the warp signal mostly gone. |
| Fair to compare against training-free baselines? | On DL3DV there is also the trained ImageConductor: FID 89.2 vs ours 48.4, mIoU 0.61 vs 0.83. MotionClone gets FID 82.7. SG-I2V was not evaluated on DL3DV. |
| Where do you lose? | T2V DAVIS mIoU: DMT 0.85, MotionClone 0.75, ours 0.70. Untuned FID is slightly better, 76.6 vs 78.6. SG-I2V has better VBench consistency. The user study used our own 40 samples. |
| What does your warp buy over InfRes / HIWYN? | All of them reach Moran's I ≈ 0 and LPIPS 0.28–0.29; InfRes gets 0.28. Ours has the lowest SR warping error: 152.0 vs 164.4 HIWYN and 190.8 InfRes (`4_experiments_thesis.tex:24`). Speed is 2.14 ms vs 2.61 InfRes and 55.2 HIWYN. Relighting is the trap: bilinear 47.5 vs ours 85.8. |
| Why is HIWYN slow? | It rasterizes polygons and re-warps from frame 0, so cost grows with the frame count. Ours stores only the previous frame. |
| Is the noise per frame? | Per latent frame. CogVideoX keeps 1 of every 4 frames (nearest in time) and mean-pools 8×8 then multiplies by 8 in space (`3_method_thesis.tex:106`). |
| Sub-pixel motion? | The pseudocode uses integer flow (f: D → ℕ²). Sub-pixel motion per frame is not addressed in the paper. Small motions accumulate through density/rounding only approximately; γ absorbs flow error. |
| Is the cat cut-and-drag top row the output? | No. The top row is the crude cut-and-paste input (cloned jaw); the bottom row is the model's yawn. |
