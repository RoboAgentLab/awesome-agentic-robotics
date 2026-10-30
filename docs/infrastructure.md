# Agent as Infrastructure

[Home](../README.md) · [Policy](policy.md) · [Self-Evolver](self-evolver.md)

Agents build and coordinate robotics development workflows across **collection, training, and inference**. Collection includes environment generation and dataset construction; inference includes evaluation and diagnosis. Inclusion requires agent decisions about the workflow, not simply running a fixed script.

Evaluation resource: [LADDER](https://ladderrobotics.ai/) ([paper](https://arxiv.org/abs/2610.18053), [code](https://github.com/insait-institute/ladder)) benchmarks long-horizon robot manipulation. Its PSP-Agent configurations are listed under [Policy](policy.md).

Evaluation resource: [EmbodiedLab](https://hexafuture.ai/benchmarks/embodiedlab/) ([paper](https://arxiv.org/abs/2610.35385), [code](https://github.com/HexaFuture/EmbodiedLab)) benchmarks acting-to-know science experiments in a simulated robot laboratory. Its T0/T1 agent configurations are listed under [Policy](policy.md).

Evaluation resource: [HandsOn](https://llltttwww.github.io/HandsOn-website/) ([paper](https://arxiv.org/abs/2610.26765), [code](https://github.com/TsinghuaC3I/HandsOn)) benchmarks dexterous manipulation. Its GPT-6 baseline is listed under [Policy](policy.md); the public code covers the benchmark and evaluation stack, with the exact GPT runner unverified.

## Browse

- [Infrastructure / Environment Generation](#infrastructure-environment-generation)
- [Infrastructure / Dataset Construction](#infrastructure-dataset-construction)
- [Infrastructure / Training](#infrastructure-training)
- [Infrastructure / Evaluation](#infrastructure-evaluation)
- [Infrastructure / Diagnosis](#infrastructure-diagnosis)

<a id="infrastructure-environment-generation"></a>

## Infrastructure / Environment Generation

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [3DCodeVerse: Exploring 3D Worlds as Code](https://arxiv.org/abs/2610.22341) | 2026 | Paper | <a href="https://github.com/gaoypeng/3dcodeverse"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Agentic Real2Sim: Physics-based World Modeling with Vision-Language Agents](https://arxiv.org/abs/2607.19190) | 2026 | Paper | <a href="https://github.com/agentic-real2sim/agentic_real2sim"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](https://arxiv.org/abs/2610.10479) | 2026 | Paper | — |
| [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | 2026 | Paper | — |
| [Articraft: An Agentic System for Scalable Articulated 3D Asset Generation](https://arxiv.org/abs/2605.15187) | 2026 | Paper | <a href="https://github.com/articraftresearch/Articraft"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Awomo-SimDataEngine: Agentic Simulation-ReadyWorld Generation](https://arxiv.org/abs/2610.02274) | 2026 | Paper | — |
| [ChronoAgentic: A Code-based Multi-Agent World Simulator for Physically Grounded Simulation Construction](https://arxiv.org/abs/2605.14398) | 2026 | Paper | — |
| [CoDimRecon: Agentic Reconstruction of Sim-Ready 3D Scenes with Deformable Curves, Surfaces, and Volumes](https://arxiv.org/abs/2609.36024) | 2026 | Paper | — |
| [D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control](https://arxiv.org/abs/2610.17114) | 2026 | Paper | — |
| [DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library](https://arxiv.org/abs/2609.35318) | 2026 | Paper | <a href="https://github.com/dexagent1/DexAgent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [DiagGen: Agentic Generation of Deformable Assets with Sim-based Diagnostics for Robotic Simulation](https://arxiv.org/abs/2609.23103) | 2026 | Paper | <a href="https://github.com/diaggen/diaggen"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction](https://arxiv.org/abs/2609.13082) | 2026 | Paper | — |
| [EmbodiedClaw: Conversational Workflow Execution for Embodied AI Development](https://arxiv.org/abs/2604.13800) | 2026 | Paper | — |
| [EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI](https://arxiv.org/abs/2607.07459) | 2026 | Paper | <a href="https://github.com/HorizonRobotics/EmbodiedGen"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation](https://arxiv.org/abs/2610.07969) | 2026 | Paper | — |
| [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | 2026 | Paper | <a href="https://github.com/EmbodiedSWE/EmbodiedSWE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation](https://arxiv.org/abs/2609.38905) | 2026 | Paper | — |
| [F4R: Failure-Driven Recognition, Reconstruction, Refinement, and Redeployment for Continual Robot Self-Improvement](https://arxiv.org/abs/2609.35575) | 2026 | Paper | — |
| [FATE: Closed-Loop Feasibility-Aware Task Generation with Active Repair for Physically Grounded Robotic Curricula](https://arxiv.org/abs/2603.01505) | 2026 | Paper | — |
| [Gemini 4 Argon: Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/) | 2026 | Project / report | — |
| [Genie Sim: Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078) | 2026 | Paper | <a href="https://github.com/AgibotTech/genie_sim"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GenPHRI: Agentic Generative Simulation for Physical Human-Robot Interaction](https://arxiv.org/abs/2604.08664) | 2026 | Paper | — |
| [GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning](https://arxiv.org/abs/2609.05927) | 2026 | Paper | — |
| [glm-skills-embodied: GLM-5.3-Flash Skills: Embodied Data Engine](https://github.com/hxwxss/glm-skills-embodied) | 2026 | Repository | <a href="https://github.com/hxwxss/glm-skills-embodied"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning](https://arxiv.org/abs/2606.08610) | 2026 | Paper | <a href="https://github.com/supersglzc/harbor-rl"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HomeBody: A Humanoid That Explores, Remembers, and Acts on Its Own](https://tml.stanford.edu/homebody/) | 2026 | Project / report | <a href="https://github.com/Stanford-TML/homebody"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Reflective Test-Time Planning: Learning from Trials and Errors: Reflective Test-Time Planning for Embodied LLMs](https://arxiv.org/html/2602.21198) | 2026 | Paper · [Project](https://reflective-test-time-planning.github.io) | — |
| [ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies](https://proceedings.iclr.cc/paper_files/paper/2026/file/8833c8aa10542d24d693bbaf6a4598f5-Paper-Conference.pdf) | 2026 | Paper | — |
| [PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement](https://arxiv.org/abs/2602.14968) | 2026 | Paper | — |
| [RAPID: Robot Agentic Programming from Demonstrations](https://arxiv.org/abs/2609.30249) | 2026 | Paper | — |
| [Real2Gym: Building Gyms from Videos, Bringing Skills to Robots](https://arxiv.org/abs/2609.37089) | 2026 | Paper | <a href="https://github.com/real2gym/R2G_Agent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Real2Sim Active Perception: Real2Sim via Active Perception with Behavior Trees Automatically Generated by VLMs](https://arxiv.org/abs/2601.08454) | 2026 | Paper | — |
| [RPG: Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204) | 2026 | Paper | — |
| [Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation](https://arxiv.org/abs/2610.01178) | 2026 | Paper | — |
| [RoboLab: A High-Fidelity Simulation Benchmark for Analysis of Task Generalist Policies](https://arxiv.org/abs/2604.09860) | 2026 | Paper | — |
| [RoboPlayground: Democratizing Robotic Evaluation through Structured Physical Domains](https://arxiv.org/abs/2604.05226) | 2026 | Paper | — |
| [RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks](https://arxiv.org/abs/2610.18835) | 2026 | Paper | <a href="https://github.com/robosimstudio/robosimstudio"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboWits: Unexpected Challenges for Robotic Creative Problem Solving](https://arxiv.org/abs/2605.30326) | 2026 | Paper | <a href="https://github.com/UMass-Embodied-AGI/RoboWits"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SAGE: Scalable Agentic 3D Scene Generation for Embodied AI](https://arxiv.org/abs/2602.10116) | 2026 | Paper | — |
| [ScaleVLA-RL: Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds](https://arxiv.org/abs/2603.18532) | 2026 | Paper · [Project](https://horizonrobotics.github.io/gail/scale-vla-rl/) | — |
| [Scene2Demo: Self-Evolving Embodied Data Generation via Object-Action Graph](https://arxiv.org/abs/2602.12065) | 2026 | Paper | — |
| [SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images](https://arxiv.org/abs/2610.28585) | 2026 | Paper · [Project](https://red-fairy.github.io/SceneRig/) | <a href="https://github.com/Red-Fairy/SceneRig"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://arxiv.org/abs/2602.09153) | 2026 | Paper | <a href="https://github.com/nepfaff/scenesmith"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation](https://arxiv.org/abs/2609.32698) | 2026 | Paper | — |
| [SimEX: Simulation-Integrated Robotics AutoResearch](https://arxiv.org/abs/2609.38982) | 2026 | Paper | — |
| [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](https://arxiv.org/abs/2606.28276) | 2026 | Paper | <a href="https://github.com/NVlabs/SimFoundry"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning](https://arxiv.org/abs/2605.09423) | 2026 | Paper | — |
| [SpatialHarness: Test-Time Spatial Scaffolding for Fine Robotic Manipulation](https://arxiv.org/abs/2610.12457v1) | 2026 | Paper · [Project](https://emilia113.github.io/SpatialHarness/) | — |
| [TacHarness: Agentic Infrastructure for Continually Improving Visuotactile Robot Policies](https://openreview.net/forum?id=V8hQBmyydD) | 2026 | Paper | — |
| [TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](https://arxiv.org/abs/2610.30043) | 2026 | Paper · [Project](https://xuyicheng-zju.github.io/TARSphere/) | <a href="https://github.com/xuyicheng-zju/TARSphere"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Text2MuJoCo](https://github.com/ShawnJoeng/Text2Mujoco) | 2026 | Repository | <a href="https://github.com/ShawnJoeng/Text2Mujoco"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Adaptive Environment Generation: Towards Adaptive Environment Generation for Training Embodied Agents](https://arxiv.org/abs/2602.06366) | 2026 | Paper | — |
| [Artisan: Towards Physically Grounded Articulated 3D Assets: A Multi-Agent Pipeline and Benchmark](https://arxiv.org/abs/2610.13947) | 2026 | Paper · [Project](https://physicalvision.github.io/artisan/) | <a href="https://github.com/physicalvision/artisan"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [USDCraft: Geometrically Grounded Programmatic Modeling of Articulated 3D Assets for Simulation](https://arxiv.org/abs/2610.11322) | 2026 | Paper · [Project](https://xingyoujun.github.io/usdcraft/) | — |
| [V-CAGE: Vision-Closed-Loop Agentic Generation Engine for Robotic Manipulation](https://arxiv.org/abs/2604.09036) | 2026 | Paper | — |
| [V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors](https://arxiv.org/abs/2603.18811) | 2026 | Paper | — |
| [Video2World: Benchmarking Coding Agents for Interactive World Modeling from Embodied Videos](https://arxiv.org/abs/2610.04432) | 2026 | Paper | <a href="https://github.com/AetherLabsAI/Video2World"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning](https://arxiv.org/abs/2512.17853) | 2025 | Paper | — |
| [Articulate AnyMesh: Open-Vocabulary 3D Articulated Objects Modeling](https://arxiv.org/abs/2502.02590) | 2025 | Paper · [Project](https://articulateanymesh.github.io/) | <a href="https://github.com/UMass-Embodied-AGI/Articulate-Anymesh"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Articulate-Anything: Automatic Modeling of Articulated Objects via a Vision-Language Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2025/hash/2c8047bf3ed8ef6905351608d641f02f-Abstract-Conference.html) | 2025 | Paper | <a href="https://github.com/vlongle/articulate-anything"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GenManip: LLM-driven Simulation for Generalizable Instruction-Following Manipulation](https://arxiv.org/abs/2506.10966) | 2025 | Paper · [Project](https://genmanip.com/) | <a href="https://github.com/InternRobotics/GenManip"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboSimGS: High-Fidelity Simulated Data Generation for Real-World Zero-Shot Robotic Manipulation Learning with Gaussian Splatting](https://arxiv.org/abs/2510.10637) | 2025 | Paper · [Project](https://robosimgs.github.io/) | <a href="https://github.com/Maxwell-Zhao/RoboSimGS"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ReGen: Generative Robot Simulation via Inverse Design](https://arxiv.org/abs/2511.04769) | 2025 | Paper · [Project](https://regen-sim.github.io/) | — |
| [RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation](https://arxiv.org/abs/2506.06677) | 2025 | Paper | <a href="https://github.com/buaa-colalab/RoboCerebra"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756) | 2025 | Paper · [Project](https://tangtaogo.github.io/RoboPearls/) | — |
| [SceneWeaver: All-in-One 3D Scene Synthesis with an Extensible and Self-Reflective Agent](https://arxiv.org/abs/2509.20414) | 2025 | Paper · [Project](https://scene-weaver.github.io/) | <a href="https://github.com/Scene-Weaver/SceneWeaver"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | 2025 | Paper | — |
| [Eurekaverse: Environment Curriculum Generation via Large Language Models](https://arxiv.org/abs/2411.01775) | 2024 | Paper | <a href="https://github.com/eureka-research/eurekaverse"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs](https://arxiv.org/abs/2410.03645) | 2024 | Paper | <a href="https://github.com/GenSim2/GenSim2"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GRS: Generating Robotic Simulation Tasks from Real-World Images](https://arxiv.org/abs/2410.15536) | 2024 | Paper | — |
| [OMNI-EPIC: Open-endedness via Models of human Notions of Interestingness with Environments Programmed in Code](https://arxiv.org/abs/2405.15568) | 2024 | Paper | <a href="https://github.com/maxencefaldor/omni-epic"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Gen2Sim: Scaling up Robot Learning in Simulation with Generative Models](https://arxiv.org/abs/2310.18308) | 2023 | Paper | <a href="https://github.com/pushkalkatara/Gen2Sim"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://arxiv.org/abs/2310.01361) | 2023 | Paper | <a href="https://github.com/liruiw/GenSim"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Holodeck: Language Guided Generation of 3D Embodied AI Environments](https://arxiv.org/abs/2312.09067) | 2023 | Paper · [Project](https://yueyang.ai/holodeck/) | <a href="https://github.com/allenai/Holodeck"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) | 2023 | Paper | <a href="https://github.com/Genesis-Embodied-AI/RoboGen"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="infrastructure-dataset-construction"></a>

## Infrastructure / Dataset Construction

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474) | 2026 | Paper | — |
| [Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation](https://arxiv.org/abs/2606.04172) | 2026 | Paper | <a href="https://github.com/arc-l/a2a"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AW-0: Agentic World Action Models](https://arxiv.org/abs/2610.30136) | 2026 | Paper | <a href="https://github.com/ZhuoyangLiu2005/agentic-wam"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589) | 2026 | Paper | <a href="https://github.com/xinxinliu-ai/AgenticRoboRL"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning](https://arxiv.org/abs/2606.10927) | 2026 | Paper | — |
| [ARS: Agentic Reward System for Robot Learning](https://arxiv.org/abs/2609.34484) | 2026 | Paper | <a href="https://github.com/midea-ai/ars"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | 2026 | Paper | — |
| [Awomo-SimDataEngine: Agentic Simulation-ReadyWorld Generation](https://arxiv.org/abs/2610.02274) | 2026 | Paper | — |
| [Robo-COP: Co-Evolving Robot Orchestrators and Policies through Deployment](https://arxiv.org/abs/2610.09228) | 2026 | Paper | — |
| [DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library](https://arxiv.org/abs/2609.35318) | 2026 | Paper | <a href="https://github.com/dexagent1/DexAgent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiedClaw: Conversational Workflow Execution for Embodied AI Development](https://arxiv.org/abs/2604.13800) | 2026 | Paper | — |
| [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | 2026 | Paper | <a href="https://github.com/EmbodiedSWE/EmbodiedSWE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation](https://arxiv.org/abs/2609.38905) | 2026 | Paper | — |
| [EndoRSI: Physical-Evidence-Driven Recursive Improvement of Endoscopic Robot Policies](https://arxiv.org/abs/2610.13376) | 2026 | Paper | — |
| [FLARE (2026): FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645v1) | 2026 | Paper | — |
| [AgentChord: From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation](https://arxiv.org/abs/2605.11951) | 2026 | Paper | <a href="https://github.com/EDEM-AI/AgentChord"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Gemini 4 Argon: Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/) | 2026 | Project / report | — |
| [Genie Sim: Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078) | 2026 | Paper | <a href="https://github.com/AgibotTech/genie_sim"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GenPHRI: Agentic Generative Simulation for Physical Human-Robot Interaction](https://arxiv.org/abs/2604.08664) | 2026 | Paper | — |
| [GIF: Agentic Generation of Interactive and Functional Object Compositions for Robot Learning](https://arxiv.org/abs/2609.05927) | 2026 | Paper | — |
| [glm-skills-embodied: GLM-5.3-Flash Skills: Embodied Data Engine](https://github.com/hxwxss/glm-skills-embodied) | 2026 | Repository | <a href="https://github.com/hxwxss/glm-skills-embodied"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884) | 2026 | Paper | <a href="https://github.com/insight-vla/insight"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Waddle: Introducing Waddle: Agents that Control Robots](https://waddlelabs.ai/research/introducing-waddle) | 2026 | Project / report | — |
| [GLIDE: Learning Beyond What Humans Can Demonstrate](https://arxiv.org/abs/2609.24996) | 2026 | Paper | — |
| [MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2610.03476) | 2026 | Paper | <a href="https://github.com/kaiknower/MobiAgent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [PlayWorld: Learning Robot World Models from Autonomous Play](https://arxiv.org/abs/2603.09030) | 2026 | Paper | <a href="https://github.com/irom-princeton/open-world"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HERO: Practice Makes Policies: Bootstrapping and Consolidating Robotic Capabilities from Zero Human Demonstrations](https://arxiv.org/abs/2607.26809) | 2026 | Paper | — |
| [RE-0: Verified Recursive Improvement of Embodied Code-as-Policy Agents through Local On-Policy Distillation](https://arxiv.org/abs/2609.32416) | 2026 | Paper | — |
| [Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation](https://arxiv.org/abs/2610.01178) | 2026 | Paper | — |
| [Local Recovery: Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision](https://arxiv.org/abs/2610.05151) | 2026 | Paper | — |
| [REVOLVE (2026): REVOLVE: An Automated Closed-Loop Framework for Evolving Robot Manipulation with Minimal Human Intervention](https://arxiv.org/abs/2609.14633) | 2026 | Paper | — |
| [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558) | 2026 | Paper | <a href="https://github.com/RoboClaw-Robotics/RoboClaw"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data](https://arxiv.org/abs/2605.13775) | 2026 | Paper | — |
| [RoboGene: Boosting VLA Pre-training via Diversity-Driven Agentic Framework for Real-World Task Generation](https://arxiv.org/abs/2602.16444) | 2026 | Paper | — |
| [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | 2026 | Paper | <a href="https://github.com/robolineage/robolineage"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboMemArena: A Comprehensive and Challenging Robotic Memory Benchmark](https://arxiv.org/abs/2605.10921) | 2026 | Paper | <a href="https://github.com/OpenHelix-Team/RoboMemArena"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [DGAC: Robot Self-Improvement via Human-Video Dynamics Models](https://arxiv.org/abs/2606.21406) | 2026 | Paper | — |
| [Scene2Demo: Self-Evolving Embodied Data Generation via Object-Action Graph](https://arxiv.org/abs/2602.12065) | 2026 | Paper | — |
| [SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792) | 2026 | Paper | [Code pending release](https://github.com/Self-Evolving-Agentic-Robotics/SEAR) |
| [TacHarness: Agentic Infrastructure for Continually Improving Visuotactile Robot Policies](https://openreview.net/forum?id=V8hQBmyydD) | 2026 | Paper | — |
| [Tether: Autonomous Functional Play with Correspondence-Driven Trajectory Warping](https://arxiv.org/abs/2603.03278) | 2026 | Paper | <a href="https://github.com/tether-research/tether"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation](https://arxiv.org/abs/2603.02623) | 2026 | Paper | — |
| [V-CAGE: Vision-Closed-Loop Agentic Generation Engine for Robotic Manipulation](https://arxiv.org/abs/2604.09036) | 2026 | Paper | — |
| [V-Dreamer: Automating Robotic Simulation and Trajectory Synthesis via Video Generation Priors](https://arxiv.org/abs/2603.18811) | 2026 | Paper | — |
| [Zero2Skill: Bootstrapping Robot Skills through Autonomous Data Collection, Training, and Deployment](https://arxiv.org/abs/2607.14047) | 2026 | Paper | <a href="https://github.com/open-gigaai/Zero2Skill"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning](https://arxiv.org/abs/2512.17853) | 2025 | Paper | — |
| [HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning](https://arxiv.org/abs/2507.00833) | 2025 | Paper | <a href="https://github.com/TeleHuman/HumanoidGen"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data](https://arxiv.org/abs/2501.04595) | 2025 | Paper · [Project](https://mobileh2r.github.io/) | — |
| [Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://arxiv.org/abs/2504.14588) | 2025 | Paper | <a href="https://github.com/GeWu-Lab/Motion-based-Self-Reflection-Framework"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboCerebra: A Large-scale Benchmark for Long-horizon Robotic Manipulation Evaluation](https://arxiv.org/abs/2506.06677) | 2025 | Paper | <a href="https://github.com/buaa-colalab/RoboCerebra"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboFactory: Exploring Embodied Agent Collaboration with Compositional Constraints](https://arxiv.org/abs/2503.16408v1) | 2025 | Paper · [Project](https://iranqin.github.io/robofactory/) | <a href="https://github.com/MARS-EAI/RoboFactory"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756) | 2025 | Paper · [Project](https://tangtaogo.github.io/RoboPearls/) | — |
| [RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://arxiv.org/abs/2506.18088) | 2025 | Paper | <a href="https://github.com/RoboTwin-Platform/RoboTwin"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboTwin: Dual-Arm Robot Benchmark with Generative Digital Twins](https://arxiv.org/abs/2504.13059) | 2025 | Paper | <a href="https://github.com/RoboTwin-Platform/RoboTwin/tree/gpt"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Video2Policy: Scaling up Manipulation Tasks in Simulation through Internet Videos](https://arxiv.org/abs/2502.09886) | 2025 | Paper | — |
| [SOAR: Autonomous Improvement of Instruction Following Skills via Foundation Models](https://arxiv.org/abs/2407.20635) | 2024 | Paper | <a href="https://github.com/rail-berkeley/soar"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents](https://arxiv.org/abs/2401.12963) | 2024 | Paper | — |
| [BBSEA: An Exploration of Brain-Body Synchronization for Embodied Agents](https://arxiv.org/html/2402.08212) | 2024 | Paper · [Project](https://bbsea-embodied-ai.github.io) | — |
| [GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs](https://arxiv.org/abs/2410.03645) | 2024 | Paper | <a href="https://github.com/GenSim2/GenSim2"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Manipulate-Anything: Automating Real-World Robots using Vision-Language Models](https://arxiv.org/abs/2406.18915) | 2024 | Paper | <a href="https://github.com/Robot-MA/manipulate-anything"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting](https://arxiv.org/abs/2403.03174) | 2024 | Paper | <a href="https://github.com/moka-manipulation/moka"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GenSim: Generating Robotic Simulation Tasks via Large Language Models](https://arxiv.org/abs/2310.01361) | 2023 | Paper | <a href="https://github.com/liruiw/GenSim"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [OLAF: Interactive Robot Learning from Verbal Correction](https://arxiv.org/abs/2310.17555) | 2023 | Paper · [Project](https://ut-austin-rpl.github.io/olaf/) | — |
| [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) | 2023 | Paper | <a href="https://github.com/Genesis-Embodied-AI/RoboGen"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Scaling Up: Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition](https://arxiv.org/abs/2307.14535) | 2023 | Paper | <a href="https://github.com/columbia-ai-robotics/scalingup"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="infrastructure-training"></a>

## Infrastructure / Training

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [AGPS: Accelerating Robotic Reinforcement Learning with Agent Guidance](https://arxiv.org/abs/2602.11978) | 2026 | Paper | — |
| [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474) | 2026 | Paper | — |
| [APPL: Agent Priors-guided Policy Learning](https://arxiv.org/abs/2609.35690) | 2026 | Paper | — |
| [Agent-Driven RL: Agent-Driven Autonomous Reinforcement Learning Research: Iterative Policy Improvement for Quadruped Locomotion](https://arxiv.org/abs/2603.27416) | 2026 | Paper | — |
| [AI Training Manager: Bounded Closed-Loop Control of Adaptive Training Recipes](https://arxiv.org/abs/2606.29871) | 2026 | Paper | — |
| [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | 2026 | Paper | — |
| [Autoresearch Gym](https://github.com/gabec-slop/autoresearch-gym) | 2026 | Repository | <a href="https://github.com/gabec-slop/autoresearch-gym"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [autoresearch-robotics: Autonomous Robotics Research with Simulation Feedback](https://github.com/jellyheadandrew/autoresearch-robotics/tree/ff30cc481af9343b9c96f448b5ed72b75bfcd562) | 2026 | Repository | <a href="https://github.com/jellyheadandrew/autoresearch-robotics"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Causal Reward Models: Causal Reward World Models: Zero-shot Reward Design for Automated Skill Generation](https://arxiv.org/abs/2606.23280) | 2026 | Paper | — |
| [Embody: Claude plays robotics](https://www.anthropic.com/research/claude-plays-robotics) | 2026 | Research blog | — |
| [Robo-COP: Co-Evolving Robot Orchestrators and Policies through Deployment](https://arxiv.org/abs/2610.09228) | 2026 | Paper | — |
| [CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning](https://arxiv.org/abs/2607.01721) | 2026 | Paper | <a href="https://github.com/nihx9919/CoRe"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [DexSim2Real: Foundation Model-Guided Sim-to-Real Transfer for Generalizable Dexterous Manipulation](https://arxiv.org/abs/2605.05241) | 2026 | Paper | — |
| [EmbodiedClaw: Conversational Workflow Execution for Embodied AI Development](https://arxiv.org/abs/2604.13800) | 2026 | Paper | — |
| [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | 2026 | Paper | <a href="https://github.com/EmbodiedSWE/EmbodiedSWE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation](https://arxiv.org/abs/2609.38905) | 2026 | Paper | — |
| [EndoRSI: Physical-Evidence-Driven Recursive Improvement of Endoscopic Robot Policies](https://arxiv.org/abs/2610.13376) | 2026 | Paper | — |
| [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980) | 2026 | Paper | <a href="https://github.com/NVlabs/ENPIRE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EvoNav: Evolutionary Reward Function Design for Robot Navigation with Large Language Models](https://arxiv.org/abs/2605.11859) | 2026 | Paper | — |
| [Demo2Reward: From Demonstrations to Rewards: Test-Time Prompt Optimization for VLM Reward Models](https://arxiv.org/abs/2606.00083) | 2026 | Paper | — |
| [RoboCoach: From Digital to Physical: Digital Agents as Autonomous Coaches for Physical Intelligence](https://arxiv.org/abs/2601.21570) | 2026 | Paper | — |
| [Gemini 4 Argon: Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/) | 2026 | Project / report | — |
| [GenPHRI: Agentic Generative Simulation for Physical Human-Robot Interaction](https://arxiv.org/abs/2604.08664) | 2026 | Paper | — |
| [GigaWorld-Policy 0.5: GigaWorld-Policy-0.5: A Faster and Stronger WAM Empowered by AutoResearch](https://arxiv.org/abs/2607.13960) | 2026 | Paper | — |
| [HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning](https://arxiv.org/abs/2606.08610) | 2026 | Paper | <a href="https://github.com/supersglzc/harbor-rl"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Hermes Embodied: Self-Improving Robotics via Hermes Agent](https://github.com/bryercowan/hermes-embodied) | 2026 | Repository | <a href="https://github.com/bryercowan/hermes-embodied"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Hyperagents](https://arxiv.org/abs/2603.19461) | 2026 | Paper | <a href="https://github.com/facebookresearch/Hyperagents"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Waddle: Introducing Waddle: Agents that Control Robots](https://waddlelabs.ai/research/introducing-waddle) | 2026 | Project / report | — |
| [Nautilus: From One Prompt to Plug-and-Play Robot Learning](https://arxiv.org/abs/2605.11665) | 2026 | Paper | — |
| [Nebius Physical AI](https://github.com/nebius/nebius-physical-ai) | 2026 | Software | <a href="https://github.com/nebius/nebius-physical-ai"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [IDM: Predict Before You Modify: Learning Improvement Dynamics for Self-Evolving Agents](https://arxiv.org/abs/2610.13991) | 2026 | Paper | — |
| [Prompt2Policy: Prompt-to-Policy: Agentic Engineering for Reinforcement Learning](https://github.com/krafton-ai/Prompt2Policy) | 2026 | Repository | <a href="https://github.com/krafton-ai/Prompt2Policy"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RDA: Reward Design Agent for Reinforcement Learning](https://arxiv.org/abs/2606.01672) | 2026 | Paper | — |
| [ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies](https://arxiv.org/abs/2606.09630) | 2026 | Paper | — |
| [ResearchBoost: ResearchBoost-Agent: An autonomous agent that profiles, optimizes, and validates AI training code](https://github.com/AI4AI-for-Anything/ResearchBoost-Agent) | 2026 | Repository | <a href="https://github.com/AI4AI-for-Anything/ResearchBoost-Agent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RLE-Bench: A Qualifying Exam for Coding Agents as Robot Learning Engineers](https://arxiv.org/abs/2609.34210) | 2026 | Paper | <a href="https://github.com/RLE-Bench/RLE-Bench"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | 2026 | Paper | <a href="https://github.com/robolineage/robolineage"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [robot-autoresearch](https://github.com/AlmondGod/robotics-autoresearch) | 2026 | Repository | <a href="https://github.com/AlmondGod/robotics-autoresearch"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792) | 2026 | Paper | [Code pending release](https://github.com/Self-Evolving-Agentic-Robotics/SEAR) |
| [SEES: A Self-Evolving Embodied System via Failure-Guided VLA Policy Adaptation](https://arxiv.org/abs/2609.32698) | 2026 | Paper | — |
| [SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning](https://arxiv.org/abs/2605.09423) | 2026 | Paper | — |
| [SUN: Agentic Robot Policy Learning with Persistent Task Programs](https://arxiv.org/abs/2608.31167) | 2026 | Paper | — |
| [TacHarness: Agentic Infrastructure for Continually Improving Visuotactile Robot Policies](https://openreview.net/forum?id=V8hQBmyydD) | 2026 | Paper | — |
| [RQGM: The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators](https://arxiv.org/abs/2606.26294) | 2026 | Paper | — |
| [VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning](https://arxiv.org/abs/2610.08761) | 2026 | Paper | — |
| [IKER: A Real-to-Sim-to-Real Approach to Robotic Manipulation with VLM-Generated Iterative Keypoint Rewards](https://arxiv.org/abs/2502.08643) | 2025 | Paper · [Project](https://iker-robot.github.io/) | <a href="https://github.com/shivanshpatel35/IKER"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AnyTask: an Automated Task and Data Generation Framework for Advancing Sim-to-Real Policy Learning](https://arxiv.org/abs/2512.17853) | 2025 | Paper | — |
| [AURA (Zhu): AURA: Autonomous Upskilling with Retrieval-Augmented Agents](https://arxiv.org/abs/2506.02507) | 2025 | Paper | — |
| [CRAFT: Coaching Reinforcement Learning Autonomously using Foundation Models for Multi-Robot Coordination Tasks](https://arxiv.org/abs/2509.14380) | 2025 | Paper | — |
| [ELEMENTAL: Interactive Learning from Demonstrations and Vision-Language Models for Reward Design in Robotics](https://proceedings.mlr.press/v267/chen25at.html) | 2025 | Paper | — |
| [LAMARL: LLM-Aided Multi-Agent Reinforcement Learning for Cooperative Policy Generation](https://arxiv.org/html/2506.01538) | 2025 | Paper · [Project](https://windylab.github.io/LAMARL/) | — |
| [Reflective Adaptation: Reflection-Based Task Adaptation for Self-Improving VLA](https://arxiv.org/abs/2510.12710) | 2025 | Paper | — |
| [RE-GoT: Reward Evolution with Graph-of-Thoughts: A Bi-Level Language Model Framework for Reinforcement Learning](https://arxiv.org/abs/2509.16136) | 2025 | Paper | — |
| [STRIDE: Automating Reward Design, Deep Reinforcement Learning Training and Feedback Optimization in Humanoid Robotics Locomotion](https://arxiv.org/abs/2502.04692) | 2025 | Paper | — |
| [CARD: A Large Language Model-Driven Reward Design Framework via Dynamic Feedback for Reinforcement Learning](https://arxiv.org/abs/2410.14660) | 2024 | Paper | — |
| [Agentic Skill Discovery](https://arxiv.org/abs/2405.15019) | 2024 | Paper | <a href="https://github.com/xf-zhao/Agentic-Skill-Discovery"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AHA: A Vision-Language-Model for Detecting and Reasoning Over Failures in Robotic Manipulation](https://arxiv.org/abs/2410.00371) | 2024 | Paper | <a href="https://github.com/NVlabs/AHA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Code as Reward: Empowering Reinforcement Learning with VLMs](https://proceedings.mlr.press/v235/venuto24a.html) | 2024 | Paper | — |
| [CurricuLLM: Automatic Task Curricula Design for Learning Complex Robot Skills using Large Language Models](https://arxiv.org/abs/2409.18382) | 2024 | Paper | <a href="https://github.com/labicon/CurricuLLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [DrEureka: Language Model Guided Sim-To-Real Transfer](https://arxiv.org/abs/2406.01967) | 2024 | Paper | <a href="https://github.com/eureka-research/DrEureka"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Eurekaverse: Environment Curriculum Generation via Large Language Models](https://arxiv.org/abs/2411.01775) | 2024 | Paper | <a href="https://github.com/eureka-research/eurekaverse"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Game On: Towards Language Models as RL Experimenters](https://arxiv.org/abs/2409.03402) | 2024 | Paper | — |
| [GenSim2: Scaling Robot Data Generation with Multi-modal and Reasoning LLMs](https://arxiv.org/abs/2410.03645) | 2024 | Paper | <a href="https://github.com/GenSim2/GenSim2"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Self-Alignment: Learning Reward for Robot Skills Using Large Language Models via Self-Alignment](https://proceedings.mlr.press/v235/zeng24d.html) | 2024 | Paper | — |
| [LLM Locomotion Design: Leveraging large language models for comprehensive locomotion control in humanoid robots design](https://doi.org/10.1016/j.birob.2024.100187) | 2024 | Paper | — |
| [REvolve (2024): REvolve: Reward Evolution with Large Language Models using Human Feedback](https://arxiv.org/abs/2406.01309) | 2024 | Paper | <a href="https://github.com/RishiHazra/Revolve"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SDS: SDS – See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration](https://arxiv.org/abs/2410.11571) | 2024 | Paper | <a href="https://github.com/RPL-CS-UCL/SDS"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Video2Reward: Generating Reward Function from Videos for Legged Robot Behavior Learning](https://arxiv.org/abs/2412.05515) | 2024 | Paper | — |
| [BOSS: Bootstrap Your Own Skills: Learning to Solve New Tasks with Large Language Model Guidance](https://arxiv.org/html/2310.10021) | 2023 | Paper | — |
| [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) | 2023 | Paper | <a href="https://github.com/eureka-research/Eureka"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Gen2Sim: Scaling up Robot Learning in Simulation with Generative Models](https://arxiv.org/abs/2310.18308) | 2023 | Paper | <a href="https://github.com/pushkalkatara/Gen2Sim"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LARG²: LARG, Language-based Automatic Reward and Goal Generation](https://arxiv.org/abs/2306.10985) | 2023 | Paper | — |
| [RoboGen: Towards Unleashing Infinite Data for Automated Robot Learning via Generative Simulation](https://arxiv.org/abs/2311.01455) | 2023 | Paper | <a href="https://github.com/Genesis-Embodied-AI/RoboGen"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Self-Refined LLM: Self-Refined Large Language Model as Automated Reward Function Designer for Deep Reinforcement Learning in Robotics](https://arxiv.org/abs/2309.06687) | 2023 | Paper | — |
| [Text2Reward: Reward Shaping with Language Models for Reinforcement Learning](https://arxiv.org/abs/2309.11489) | 2023 | Paper | <a href="https://github.com/xlang-ai/text2reward"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="infrastructure-evaluation"></a>

## Infrastructure / Evaluation

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [ARS: Agentic Reward System for Robot Learning](https://arxiv.org/abs/2609.34484) | 2026 | Paper | <a href="https://github.com/midea-ai/ars"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ARSTAG: An Agentic Real2Sim2Real System for Task-Specific Robot Data Generation](https://arxiv.org/abs/2609.24563) | 2026 | Paper | — |
| [Autoresearch Gym](https://github.com/gabec-slop/autoresearch-gym) | 2026 | Repository | <a href="https://github.com/gabec-slop/autoresearch-gym"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [autoresearch-robotics: Autonomous Robotics Research with Simulation Feedback](https://github.com/jellyheadandrew/autoresearch-robotics/tree/ff30cc481af9343b9c96f448b5ed72b75bfcd562) | 2026 | Repository | <a href="https://github.com/jellyheadandrew/autoresearch-robotics"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [BenchMend: Agent-Guided Instruction Repair for Robotics Benchmarks](https://tianqi-zh.github.io/BenchMend/) | 2026 | Project / report | — |
| [Robo-COP: Co-Evolving Robot Orchestrators and Policies through Deployment](https://arxiv.org/abs/2610.09228) | 2026 | Paper | — |
| [CoDimRecon: Agentic Reconstruction of Sim-Ready 3D Scenes with Deformable Curves, Surfaces, and Volumes](https://arxiv.org/abs/2609.36024) | 2026 | Paper | — |
| [Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction](https://arxiv.org/abs/2609.13082) | 2026 | Paper | — |
| [EmbodiedClaw: Conversational Workflow Execution for Embodied AI Development](https://arxiv.org/abs/2604.13800) | 2026 | Paper | — |
| [EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation](https://arxiv.org/abs/2609.38905) | 2026 | Paper | — |
| [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980) | 2026 | Paper | <a href="https://github.com/NVlabs/ENPIRE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HALTER: From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation](https://arxiv.org/abs/2609.19413) | 2026 | Paper | — |
| [HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning](https://arxiv.org/abs/2606.08610) | 2026 | Paper | <a href="https://github.com/supersglzc/harbor-rl"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Hermes Embodied: Self-Improving Robotics via Hermes Agent](https://github.com/bryercowan/hermes-embodied) | 2026 | Repository | <a href="https://github.com/bryercowan/hermes-embodied"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ManipEvalAgent: Promptable and Efficient Evaluation Framework for Robotic Manipulation Policies](https://proceedings.iclr.cc/paper_files/paper/2026/file/8833c8aa10542d24d693bbaf6a4598f5-Paper-Conference.pdf) | 2026 | Paper | — |
| [MEMENTO: Memory-Guided Memetic Code-as-Policy Evolution](https://arxiv.org/abs/2607.22832) | 2026 | Paper | <a href="https://github.com/sygkounas/MEMENTO"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Nautilus: From One Prompt to Plug-and-Play Robot Learning](https://arxiv.org/abs/2605.11665) | 2026 | Paper | — |
| [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | 2026 | Paper | <a href="https://github.com/robolineage/robolineage"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [robot-autoresearch](https://github.com/AlmondGod/robotics-autoresearch) | 2026 | Repository | <a href="https://github.com/AlmondGod/robotics-autoresearch"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SceneSmith: Agentic Generation of Simulation-Ready Indoor Scenes](https://arxiv.org/abs/2602.09153) | 2026 | Paper | <a href="https://github.com/nepfaff/scenesmith"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [TacHarness: Agentic Infrastructure for Continually Improving Visuotactile Robot Policies](https://openreview.net/forum?id=V8hQBmyydD) | 2026 | Paper | — |
| [vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models](https://arxiv.org/abs/2603.13966) | 2026 | Paper | <a href="https://github.com/allenai/vla-evaluation-harness"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](https://arxiv.org/abs/2608.09892) | 2026 | Paper | <a href="https://github.com/XPolicyLab/XPolicyLab"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboPAIR: Jailbreaking LLM-Controlled Robots](https://arxiv.org/abs/2410.13691) | 2024 | Paper · [Project](https://robopair.org/) | <a href="https://github.com/arobey1/robopair"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="infrastructure-diagnosis"></a>

## Infrastructure / Diagnosis

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [ATP-VPDSG: Adaptive Task Planning for Long-Horizon Robotic Manipulation Based on Video Priors and Dynamic Scene Graphs](https://doi.org/10.3390/s26175595) | 2026 | Paper | — |
| [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474) | 2026 | Paper | — |
| [Agent-Driven RL: Agent-Driven Autonomous Reinforcement Learning Research: Iterative Policy Improvement for Quadruped Locomotion](https://arxiv.org/abs/2603.27416) | 2026 | Paper | — |
| [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](https://arxiv.org/abs/2610.10479) | 2026 | Paper | — |
| [autoresearch-robotics: Autonomous Robotics Research with Simulation Feedback](https://github.com/jellyheadandrew/autoresearch-robotics/tree/ff30cc481af9343b9c96f448b5ed72b75bfcd562) | 2026 | Repository | <a href="https://github.com/jellyheadandrew/autoresearch-robotics"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [BenchMend: Agent-Guided Instruction Repair for Robotics Benchmarks](https://tianqi-zh.github.io/BenchMend/) | 2026 | Project / report | — |
| [CoDimRecon: Agentic Reconstruction of Sim-Ready 3D Scenes with Deformable Curves, Surfaces, and Volumes](https://arxiv.org/abs/2609.36024) | 2026 | Paper | — |
| [D-World: An Explicit World-Language-Action Model with Recursive Self-Improvement under Dual Control](https://arxiv.org/abs/2610.17114) | 2026 | Paper | — |
| [EnactOpt: Diagnosis-Guided Harness Evolution for Embodied Agents](https://arxiv.org/abs/2610.14977) | 2026 | Paper | — |
| [EndoRSI: Physical-Evidence-Driven Recursive Improvement of Endoscopic Robot Policies](https://arxiv.org/abs/2610.13376) | 2026 | Paper | — |
| [ENPIRE: Agentic Robot Policy Self-Improvement in the Real World](https://arxiv.org/abs/2606.19980) | 2026 | Paper | <a href="https://github.com/NVlabs/ENPIRE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [FLARE (2026): FLARE: A Failure-Aware Framework for Autonomous Correction and Recovery in Visual-Language Robotic Manipulation](https://arxiv.org/abs/2608.26645v1) | 2026 | Paper | — |
| [Fly-by-Code: Embodied Coding Agents for Aerial Manipulation with Active Visual and Physical Feedback](https://arxiv.org/abs/2610.12549) | 2026 | Paper · [Project](https://fly-by-code.github.io/) | — |
| [RoboCoach: From Digital to Physical: Digital Agents as Autonomous Coaches for Physical Intelligence](https://arxiv.org/abs/2601.21570) | 2026 | Paper | — |
| [SERA: From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560) | 2026 | Paper | <a href="https://github.com/StevenKKXS/SERA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Gemini 4 Argon: Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/) | 2026 | Project / report | — |
| [HARBOR: A Harness Framework for Agentic Robot Reinforcement Learning](https://arxiv.org/abs/2606.08610) | 2026 | Paper | <a href="https://github.com/supersglzc/harbor-rl"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Dream2Fix: Learning Actionable Manipulation Recovery via Counterfactual Failure Synthesis](https://arxiv.org/abs/2603.13528) | 2026 | Paper | — |
| [GLIDE: Learning Beyond What Humans Can Demonstrate](https://arxiv.org/abs/2609.24996) | 2026 | Paper | — |
| [Recursia: Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation](https://arxiv.org/abs/2610.24464) | 2026 | Paper | <a href="https://github.com/cocacola-lab/Recursia"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [PhysEvo: Astra Can Act, Let It](https://arxiv.org/abs/2610.08995) | 2026 | Paper | — |
| [RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Deployment](https://arxiv.org/html/2602.01515) | 2026 | Paper · [Project](https://humphreymunn.github.io/RAPT/) | <a href="https://github.com/humphreymunn/RAPT"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RE-0: Verified Recursive Improvement of Embodied Code-as-Policy Agents through Local On-Policy Distillation](https://arxiv.org/abs/2609.32416) | 2026 | Paper | — |
| [ReCoVLA: VLM-Guided Reward Compilation for Failure Recovery in Vision-Language-Action Policies](https://arxiv.org/abs/2606.09630) | 2026 | Paper | — |
| [Local Recovery: Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision](https://arxiv.org/abs/2610.05151) | 2026 | Paper | — |
| [RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies](https://robodoctor-rsi.github.io/) | 2026 | Project / report | <a href="https://github.com/THUSI-Lab/RoboDoctor"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboLineage: Agent-Native Data Lifecycle Governance Across Robot Policy Iterations](https://arxiv.org/abs/2606.22142) | 2026 | Paper | <a href="https://github.com/robolineage/robolineage"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks](https://arxiv.org/abs/2610.18835) | 2026 | Paper | <a href="https://github.com/robosimstudio/robosimstudio"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [VAP-TAMP: Robot Planning and Situation Handling with Active Perception](https://arxiv.org/abs/2604.26988v1) | 2026 | Paper · [Project](https://vap-tamp.github.io/vap-tamp/) | — |
| [SPINE (2026): SPINE: Bridging the Cyber-Physical Gap with Agentic AI](https://arxiv.org/abs/2607.13049) | 2026 | Paper | — |
| [TacHarness: Agentic Infrastructure for Continually Improving Visuotactile Robot Policies](https://openreview.net/forum?id=V8hQBmyydD) | 2026 | Paper | — |
| [vla-eval: A Unified Evaluation Harness for Vision-Language-Action Models](https://arxiv.org/abs/2603.13966) | 2026 | Paper | <a href="https://github.com/allenai/vla-evaluation-harness"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [XPolicyLab: A Unified Standard and Open Ecosystem for Robot Policy Evaluation and Deployment](https://arxiv.org/abs/2608.09892) | 2026 | Paper | <a href="https://github.com/XPolicyLab/XPolicyLab"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AURA (Buchholz): A Collaborative Reasoning Framework for Anomaly Diagnostics in Underwater Robotics](https://arxiv.org/abs/2511.03075) | 2025 | Paper | — |
| [Unified Failure Handling: A Unified Framework for Real-Time Failure Handling in Robotics Using Vision-Language Models, Reactive Planner and Behavior Trees](https://arxiv.org/abs/2503.15202) | 2025 | Paper | — |
| [Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection](https://arxiv.org/abs/2412.04455) | 2025 | Paper · [Project](https://zhoues.github.io/Code-as-Monitor) | — |
| [UROSA: Distributed AI Agents for Cognitive Underwater Robot Autonomy](https://arxiv.org/abs/2507.23735) | 2025 | Paper · [Project](https://markusbuchholz.github.io/urosa.html) | <a href="https://github.com/markusbuchholz/urosa_underwater_autonomy"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Reflective Adaptation: Reflection-Based Task Adaptation for Self-Improving VLA](https://arxiv.org/abs/2510.12710) | 2025 | Paper | — |
| [RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction](https://arxiv.org/abs/2505.12224) | 2025 | Paper | <a href="https://github.com/MINT-SJTU/RoboFAC"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboPearls: Editable Video Simulation for Robot Manipulation](https://arxiv.org/abs/2506.22756) | 2025 | Paper · [Project](https://tangtaogo.github.io/RoboPearls/) | — |
| [ROS Help Desk: GenAI Powered, User-Centric Framework for ROS Error Diagnosis and Debugging](https://arxiv.org/abs/2507.07846) | 2025 | Paper | — |
| [LASP: Language-Augmented Symbolic Planner for Open-World Task Planning](https://arxiv.org/abs/2407.09792) | 2024 | Paper | — |
| [LLM2Swarm: Robot Swarms that Responsively Reason, Plan, and Collaborate through LLMs](https://arxiv.org/html/2410.11387) | 2024 | Paper | <a href="https://github.com/Pold87/LLM2Swarm"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | 2023 | Paper | <a href="https://github.com/columbia-ai-robotics/reflect"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

[Back to overview](../README.md)
