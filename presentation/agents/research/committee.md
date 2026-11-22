# Committee prep: Samaras, Ryoo, Sun

Sources: SBU expert pages, Google Scholar and arXiv listings via web search. Paper lists are partial; check Scholar before the talk. Questions are predictions, not known facts.

## Dimitris Samaras (SUNY Empire Innovation Prof., directs the SBU Computer Vision Lab)

**Areas:** generative models for vision, digital pathology, gaze and scanpath modeling, face and head avatars, NeRF and inverse rendering, shadows.

**Recent work (2024-2025):**
- Fast constrained sampling in pre-trained diffusion models (NeurIPS 2025)
- Conditional generation from unconditional diffusion models using denoiser representations
- infinity-Brush (infinite-dimensional diffusion for large controllable images)
- ZoomLDM and PathLDM (multi-scale and text-conditioned latent diffusion)
- TopoCellGen and TopoDiffusionNet (topological constraints in diffusion)
- GriDiT (grid-factorized long sequence generation, TMLR 2025)
- PathSegDiff (segmentation from diffusion features)

**Knows deeply:** constraint-guided sampling, using diffusion as a prior for inverse problems, latent diffusion, denoiser features for downstream tasks, and 3D and face vision. He will see Peekaboo and Diffusion Illusions as constrained optimization through a frozen prior, close to his own work.

**Likely questions:**
1. Peekaboo and Diffusion Illusions optimize through a frozen prior. How is that different from constrained sampling that gets constraints in without per-sample optimization? What does it cost in time, and does it work at scale?
2. Peekaboo: score distillation is known to give mode-seeking, over-saturated gradients. How does that affect the alpha mask? Do you have failure cases or quantitative segmentation numbers (mIoU), or only qualitative?
3. Diffusion Illusions: the joint optimization has several images competing. Is there a guarantee of convergence? How does it scale with the number of arrangements?
4. MAGICK: keyed chroma-background data has fringe, spill and matting error. How did you measure label quality, and does a model trained on it inherit those artifacts?
5. Do the five projects share one principle (a frozen prior plus a differentiable constraint, or modified noise or data), or are they separate tricks? What is your unifying claim, and what experiment would falsify it?

## Michael Ryoo (advisor; SBU and Salesforce AI Research)

**Areas:** video understanding, video LLMs, robot learning and VLA policies, activity recognition, pixel and optical-flow motion as a representation.

**Recent work (2025-2026):**
- LLaRA (vision-language policy, ICLR 2025)
- Pixel motion as universal representation for robot control, and Pixel Motion Diffusion
- Robotic VLA with joint motion-image diffusion
- FOFPred: future optical flow prediction for robot control and video generation (CVPR 2026)
- MVU, Language Repository and BLIP-3-Video (long-video LLMs)
- Strefer and Active Video Perception
- Adaptive Caching for video DiTs (ICCV 2025)
- Co-author on Go-with-the-Flow and MotionV2V

**Knows deeply:** motion representations (flow, tracks), video transformers, VLMs and VLAs, efficient video models, and the robotics use of controllable video. He knows Go-with-the-Flow and MotionV2V from the inside, so expect sharp questions about them.

**Likely questions:**
1. Your thesis is "control." Define it. What is the control signal in each project (mask, noise, flow, motion), and which is most general? Where does the thesis stop?
2. Go-with-the-Flow: noise warping preserves marginal Gaussianity only approximately. When does it break, and what happens with occlusion, large motion, or flow errors?
3. MotionV2V: how well does it generalize beyond the counterfactuals you generate? What are the failure modes, and how do you evaluate motion fidelity versus appearance preservation?
4. Can flow-controlled video diffusion feed back into robot control or video understanding (my own work on flow as a representation)? Did you try it, and would you pitch it as future work?
5. What is the single remaining unsolved problem in controllable video generation, and what is the plan for the rest of the PhD?

## Yifan Sun (optimization; SBU CS, AI Institute and IACS)

**Areas:** first-order and large-scale optimization for ML, nonconvex and nonsmooth problems, convergence and ill-conditioning, implicit bias of optimizers, sparsity, stability and loss-landscape geometry in training. She has also collaborated on NLP. I found no diffusion papers by her. I did not confirm her latest 2024-2026 titles, so check her page.

**Knows deeply:** convex and semidefinite optimization, convergence theory, optimizer behavior, compression such as tensor-ring nets. She is the committee member most likely to ask optimization-theory questions about score distillation.

**Likely questions:**
1. Peekaboo and Diffusion Illusions run gradient descent on an SDS-like objective. Is it a true loss, or just a vector field with no objective? What does the optimizer converge to, if anything?
2. Which optimizer, learning rate and number of steps did you use, and how sensitive are results to them? Did you compare Adam against plain SGD, or try second-order information?
3. Joint optimization of many images in Diffusion Illusions: is the problem ill-conditioned? Are the gradients from different views conflicting, and did you check for local minima, seeds and variance?
4. Noise warping in Go-with-the-Flow: what does it do to the statistics the denoiser expects, and can you state it formally (independence, variance preservation)? What is the error bound?
5. Training on motion counterfactuals (MotionV2V) and a keyed synthetic dataset (MAGICK): what are the sources of bias, and how do you know the model learned the intended factor rather than a shortcut?

## Prep notes
- Have a one-slide answer for "what unifies the five papers" (Samaras, Ryoo).
- Have numbers ready: Peekaboo segmentation metrics, MAGICK size (150k RGBA) and quality checks, Go-with-the-Flow and MotionV2V benchmarks.
- Prepare an honest limitations slide on SDS behavior, noise-warp approximation, and synthetic-data bias.
