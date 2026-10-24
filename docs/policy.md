# Agent as Policy

[Home](../README.md) · [Infrastructure](infrastructure.md) · [Self-Evolver](self-evolver.md)

Agents direct robot task execution by selecting behaviors, orchestrating tools, or writing executable task logic. The observation interface and execution authority are separate axes.

| Axis | Category | Meaning |
| --- | --- | --- |
| Observation | O1 — Sensory input | Images, proprioception, touch, or other sensory inputs. Perception constructed by the agent remains O1. |
| Observation | O2 — Perception tools | Supplied perception outputs or callable perception services. |
| Observation | O3 — Privileged state | Simulator state unavailable through ordinary robot sensing. |
| Execution | A1 — Behavior Selection | Choose behaviors, continuous targets, or trajectories for a fixed code-based or learned executor. |
| Execution | A2 — Tool Orchestration | Select existing execution APIs and supply arguments. |
| Execution | A3 — Code Synthesis | Write execution logic, such as conditions, loops, or intermediate computations. |

**Code / Model in A1 describes the executor, not the deciding agent.** Calling a Python API does not by itself establish A3. A project can appear in multiple cells because its documented configurations differ.

Configuration notes: FluxVLA refers to its GPT-controlled robot adapters. ASPIRE entries distinguish generated CaP programs from its released MCP execution interface. NavGPT-3's sensory ablations are listed; its full observed-map A2 configuration is not assigned an observation category while map provenance remains unresolved.

## Browse

- [O1 / A1 Code](#o1-a1-code)
- [O1 / A1 Model](#o1-a1-model)
- [O1 / A2](#o1-a2)
- [O1 / A3](#o1-a3)
- [O2 / A1 Code](#o2-a1-code)
- [O2 / A1 Model](#o2-a1-model)
- [O2 / A2](#o2-a2)
- [O2 / A3](#o2-a3)
- [O3 / A1 Code](#o3-a1-code)
- [O3 / A1 Model](#o3-a1-model)
- [O3 / A2](#o3-a2)
- [O3 / A3](#o3-a3)

<a id="o1-a1-code"></a>

## O1 / A1 Code

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [AgentRob: From Virtual Forum Agents to Hijacked Physical Robots](https://arxiv.org/abs/2602.13591v1) | 2026 | Paper | — |
| [An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond](https://arxiv.org/abs/2609.24170) | 2026 | Paper | <a href="https://github.com/RoboProbe/RoboProbe"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy](https://research.nvidia.com/labs/srl/projects/astranomy/) | 2026 | Project / report | — |
| [Can a Frontier VLM Serve as a Robot Policy for Memory-Dependent Manipulation?](https://arxiv.org/abs/2610.17350) | 2026 | Paper | <a href="https://github.com/jackbjed/embodied-astra-robomme"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embody: Claude plays robotics](https://www.anthropic.com/research/claude-plays-robotics) | 2026 | Research blog | — |
| [Contextual Safety Reasoning and Grounding for Open-World Robots](https://arxiv.org/abs/2602.19983) | 2026 | Paper | — |
| [DrivingBench: Can Vision-Language Models Drive a Toyota Corolla?](https://arxiv.org/abs/2609.38948v1) | 2026 | Paper | <a href="https://github.com/aditya-ramabadran/drivingbench_harness_v1"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation](https://arxiv.org/abs/2607.26148) | 2026 | Paper | <a href="https://github.com/jianzhou0420/MIP"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation](https://arxiv.org/abs/2608.17512) | 2026 | Paper | <a href="https://github.com/ZJU-OmniAI/Embodied-Navigator"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence](https://arxiv.org/abs/2609.17210) | 2026 | Paper | <a href="https://github.com/FluxVLA/FluxVLA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051) | 2026 | Paper | <a href="https://github.com/IRVLUTD/LLM_LIBERO"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Frontier LLMs Enter the World of Robotics: A Cross-Model Evaluation on RoboColiseum](https://robocoliseum.ai/techreport/agent2act) | 2026 | Project / report | — |
| [GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation](https://tactalent.github.io/) | 2026 | Project / report | — |
| [Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471) | 2026 | Paper | <a href="https://github.com/OpenSenseNova/SenseNova-RoboRSI"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [In-Context Robot Learning with VLM Agents](https://arxiv.org/abs/2609.19138) | 2026 | Paper | <a href="https://github.com/cheng-haha/GPT-Policy"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884) | 2026 | Paper | <a href="https://github.com/insight-vla/insight"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI](https://arxiv.org/abs/2610.06306) | 2026 | Paper | <a href="https://github.com/robocurve/inspect-robots"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GPT-GEAR: Large Multimodal Models for Direct Robot Control: GPT-6 as a Beginning](https://arxiv.org/abs/2610.28259) | 2026 | Paper · [Project](https://6uooon9.github.io/GPT-GEAR) | <a href="https://github.com/6UOOON9/GPT-GEAR"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ManiSkillFormer: Demonstration-Free Compositional Manipulation via Geometric Contracts and Agentic Skill Graph](https://arxiv.org/abs/2609.16331) | 2026 | Paper | — |
| [NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime](https://arxiv.org/abs/2610.10787) | 2026 | Paper | <a href="https://github.com/metacognitionai/NavGPT-3"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning](https://arxiv.org/abs/2602.20119) | 2026 | Paper | <a href="https://github.com/jiahui-fu/NovaPlan"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [PhysEvo: Astra Can Act, Let It](https://arxiv.org/abs/2610.08995) | 2026 | Paper | — |
| [ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation](https://arxiv.org/abs/2610.15814) | 2026 | Paper | — |
| [RoboAgent: Chaining Basic Capabilities for Embodied Task Planning](https://arxiv.org/abs/2604.07774) | 2026 | Paper | — |
| [RoboICL: Embodied In-Context Learning with GPT-6 Astra](https://arxiv.org/abs/2609.34261) | 2026 | Paper | <a href="https://github.com/Mosi-AI/RoboICL"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Robota-Embed: Unified VLA Embeddings for Robot In-Context Learning and Evolution](https://arxiv.org/abs/2610.19495) | 2026 | Paper | — |
| [RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments](https://arxiv.org/abs/2610.10409) | 2026 | Paper | <a href="https://github.com/robotworldai/robotworld"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) | 2026 | Paper | — |
| [Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522) | 2026 | Paper | <a href="https://github.com/showlab/Show-Harness"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [TacZero: Training-Free Peg Insertion Using a General-Purpose Vision-Language Model with Tactile Feedback](https://arxiv.org/abs/2610.07621) | 2026 | Paper | — |
| [Bitter Lesson: The Bitter Lesson Comes to Robotics](https://arxiv.org/abs/2610.25287) | 2026 | Paper | — |
| [VIA: Visual Interface Agent for Robot Control](https://arxiv.org/abs/2607.11119) | 2026 | Paper | <a href="https://github.com/hengyuan-hu/via"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiedBench: Comprehensive Benchmarking Multi-modal Large Language Models for Vision-Driven Embodied Agents](https://arxiv.org/abs/2502.09560) | 2025 | Paper | <a href="https://github.com/EmbodiedBench/EmbodiedBench"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](https://arxiv.org/abs/2503.02247) | 2025 | Paper | <a href="https://github.com/B0B8K1ng/WMNavigation"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Automating Robot Failure Recovery Using Vision-Language Models With Optimized Prompts](https://arxiv.org/abs/2409.03966) | 2024 | Paper | <a href="https://github.com/hychen-naza/Robot_ErrorRecovery_VLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs](https://arxiv.org/abs/2402.07872) | 2024 | Paper | — |
| [Wonderful Team: Zero-Shot Physical Task Planning with Visual LLMs](https://arxiv.org/abs/2407.19094) | 2024 | Paper | <a href="https://github.com/wonderful-team-robotics/wonderful_team_robotics"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Look Before You Leap: Unveiling the Power of GPT-4V in Robotic Vision-Language Planning](https://arxiv.org/abs/2311.17842) | 2023 | Paper | — |
| [EmbodiedJev](https://github.com/FBddcz/embodied-jev) | — | Repository | <a href="https://github.com/FBddcz/embodied-jev"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [quackd](https://github.com/rokbenko/quackd) | — | Repository | <a href="https://github.com/rokbenko/quackd"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o1-a1-model"></a>

## O1 / A1 Model

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [2AM: Grounding Agent-Side Memory as Guidance for Steerable Action Models in Long-Horizon Manipulation](https://arxiv.org/abs/2609.11308) | 2026 | Paper | — |
| [AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning](https://arxiv.org/abs/2606.10927) | 2026 | Paper | — |
| [AtomicVLA: Unlocking the Potential of Atomic Skill Learning in Robots](https://arxiv.org/abs/2603.07648) | 2026 | Paper | <a href="https://github.com/zhanglk9/AtomicVLA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embody: Claude plays robotics](https://www.anthropic.com/research/claude-plays-robotics) | 2026 | Research blog | — |
| [Cortex: A Bidirectionally Aligned Embodied Agent Framework for Long-horizon Manipulation](https://arxiv.org/abs/2607.05377) | 2026 | Paper | — |
| [Critic in the Loop: A Tri-System VLA Framework for Robust Long-Horizon Manipulation](https://arxiv.org/abs/2603.05185) | 2026 | Paper | — |
| [CycleVLA: Proactive Self-Correcting Vision-Language-Action Models via Subtask Backtracking and Minimum Bayes Risk Decoding](https://arxiv.org/abs/2601.02295) | 2026 | Paper | <a href="https://github.com/dannymcy/cyclevla_code"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Diagnosing Semantic Handoff Failures in Agent-Orchestrated Vision-Language-Action Skill Composition](https://arxiv.org/abs/2607.06256) | 2026 | Paper | — |
| [From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation](https://arxiv.org/abs/2610.29560) | 2026 | Paper | <a href="https://github.com/StevenKKXS/SERA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Goal2Skill: Long-Horizon Manipulation with Adaptive Planning and Reflection](https://arxiv.org/abs/2604.13942) | 2026 | Paper | — |
| [Has GPT-6-Astra Achieved Embodied Intelligence?](https://arxiv.org/abs/2610.22471) | 2026 | Paper | <a href="https://github.com/OpenSenseNova/SenseNova-RoboRSI"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HINT: Human-Intent Inception for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2609.02653) | 2026 | Paper | — |
| [HumanCLAW: Can Vision-Language Models Act Through a Body?](https://arxiv.org/abs/2607.27180) | 2026 | Paper | <a href="https://github.com/Human-CLAW/HumanCLAW"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884) | 2026 | Paper | <a href="https://github.com/insight-vla/insight"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Learning What to Say to Your VLA: Mostly Harmless Vision Language Action Model Steering](https://arxiv.org/abs/2606.12299) | 2026 | Paper | — |
| [MobiAgent: Dual-Loop Recursive Policy Self-Improvement for Long-Horizon Mobile Manipulation](https://arxiv.org/abs/2610.03476) | 2026 | Paper | <a href="https://github.com/kaiknower/MobiAgent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime](https://arxiv.org/abs/2610.10787) | 2026 | Paper | <a href="https://github.com/metacognitionai/NavGPT-3"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [PlayWorld: Learning Robot World Models from Autonomous Play](https://arxiv.org/abs/2603.09030) | 2026 | Paper | <a href="https://github.com/irom-princeton/open-world"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) | 2026 | Paper | — |
| [Slow Brain, Fast Planner: Latency-Resilient VLM-Augmented Urban Navigation](https://arxiv.org/abs/2606.20458) | 2026 | Paper | — |
| [Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models](https://arxiv.org/abs/2605.13119) | 2026 | Paper | — |
| [Agentic Robot: A Brain-Inspired Framework for Vision-Language-Action Models in Embodied Agents](https://arxiv.org/abs/2505.23450) | 2025 | Paper | <a href="https://github.com/Agentic-Robot/agentic-robot"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [DeCo: Task Decomposition and Skill Composition for Zero-Shot Generalization in Long-Horizon 3D Manipulation](https://arxiv.org/abs/2505.00527) | 2025 | Paper | <a href="https://github.com/chenzixuan99/RoboHiMan"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [DualVLN: Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation](https://arxiv.org/abs/2512.08186) | 2025 | Paper · [Project](https://dualvln.github.io/) | <a href="https://github.com/InternRobotics/InternNav"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://arxiv.org/abs/2502.19417) | 2025 | Paper | — |
| [Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation](https://arxiv.org/abs/2506.22827) | 2025 | Paper | — |
| [Phoenix: A Motion-based Self-Reflection Framework for Fine-grained Robotic Action Correction](https://arxiv.org/abs/2504.14588) | 2025 | Paper | <a href="https://github.com/GeWu-Lab/Motion-based-Self-Reflection-Framework"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboFAC: A Comprehensive Framework for Robotic Failure Analysis and Correction](https://arxiv.org/abs/2505.12224) | 2025 | Paper | <a href="https://github.com/MINT-SJTU/RoboFAC"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Self-Improving Loops for Visual Robotic Planning](https://arxiv.org/abs/2506.06658) | 2025 | Paper | <a href="https://github.com/brown-palm/silvr"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o1-a2"></a>

## O1 / A2

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589) | 2026 | Paper | <a href="https://github.com/xinxinliu-ai/AgenticRoboRL"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy](https://research.nvidia.com/labs/srl/projects/astranomy/) | 2026 | Project / report | — |
| [Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448) | 2026 | Paper | <a href="https://github.com/RLinf/RPent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [InSight: Self-Guided Skill Acquisition via Steerable VLAs](https://arxiv.org/abs/2606.24884) | 2026 | Paper | <a href="https://github.com/insight-vla/insight"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Open Gemini 4 Argon Robot Harness — A Zero-Shot Bimanual Handover Case Study](https://ehehee.github.io/blog/open-gemini-harness/) | 2026 | Project / report | <a href="https://github.com/ehehee/open-gemini-robot-harness"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation](https://arxiv.org/abs/2610.01178) | 2026 | Paper | — |
| [ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction](https://arxiv.org/abs/2603.26997) | 2026 | Paper | <a href="https://github.com/ROSClaw/rosclaw"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Spotter: Let the Embodied Model Lead, and the VLM Reflect for It](https://arxiv.org/abs/2609.36808) | 2026 | Paper | <a href="https://github.com/zqc3117/Spotter"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [VoLo: A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation](https://arxiv.org/abs/2606.07723) | 2026 | Paper | <a href="https://github.com/NVlabs/VoLoAgent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o1-a3"></a>

## O1 / A3

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [Act-Observe-Rewrite: Multimodal Coding Agents as In-Context Policy Learners for Robot Manipulation](https://arxiv.org/abs/2603.04466) | 2026 | Paper | — |
| [Agent as Policy for Robotic Manipulation](https://arxiv.org/abs/2609.12541) | 2026 | Paper | <a href="https://github.com/agent-as-policy-2026/agent-as-policy"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [BiGym 2.0: Benchmarking Learned and Agent-Developed Policies for Humanoid Household Manipulation](https://arxiv.org/abs/2610.07594) | 2026 | Paper | <a href="https://github.com/swirl-uk/BiGym2"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Compile Once, Run Cheap: Frozen, Portable Skills for Embodied Agents, and What Recursive Self-Improvement Adds](https://arxiv.org/abs/2610.25114) | 2026 | Paper | <a href="https://github.com/Orillusion/embodied-skill-rsi"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embodied First Exam](https://github.com/mll-lab-nu/embodied-first-exam) | 2026 | Repository | <a href="https://github.com/mll-lab-nu/embodied-first-exam"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ETM: Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](https://arxiv.org/abs/2610.12369) | 2026 | Paper · [Project](https://ropedia.github.io/ropedia-a0/) | — |
| [EmbodiedEvo: Self-Evolving Coding Agent For Physical Intelligence](https://arxiv.org/abs/2610.18867) | 2026 | Paper | — |
| [Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/) | 2026 | Project / report | — |
| [Learning Beyond What Humans Can Demonstrate](https://arxiv.org/abs/2609.24996) | 2026 | Paper | — |
| [LITHE: Bridging Best-Effort Python and Real-Time C++ for Hot-Swapping Robotic Control Laws on Commodity Linux](https://arxiv.org/abs/2603.07442) | 2026 | Paper | — |
| [OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies](https://arxiv.org/abs/2610.02459v1) | 2026 | Paper | <a href="https://github.com/terminalworld/OpenRUA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Recursive Self-Improvement of Visuomotor Policies through Local Recovery Supervision](https://arxiv.org/abs/2610.05151) | 2026 | Paper | — |
| [RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents](https://arxiv.org/abs/2609.32862) | 2026 | Paper | — |
| [Scaling Online Exploration for Robot Agents](https://arxiv.org/abs/2610.22496) | 2026 | Paper | <a href="https://github.com/robot-agent-exploration/rax/tree/real/franka"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Self-Evolving Embodied Agents via Skill-Harness Evolution](https://arxiv.org/abs/2608.11350) | 2026 | Paper | — |
| [Welcome to the Era of Embodied AI: Introducing AA-Robotics v0.1](https://artificialanalysis.ai/articles/aa-robotics) | 2026 | Project / report | — |
| [WetRobo: A Reproducible Robot Kit for Coding Agents in Biological Laboratories](https://arxiv.org/abs/2609.18435) | 2026 | Paper | <a href="https://github.com/tsudalab/WetRobo"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboSafe: Safeguarding Embodied Agents via Executable Safety Logic](https://arxiv.org/abs/2512.21220) | 2025 | Paper | — |
| [Robotic Programmer: Video Instructed Policy Code Generation for Robotic Manipulation](https://arxiv.org/abs/2501.04268) | 2025 | Paper | — |
| [Manipulate-Anything: Automating Real-World Robots using Vision-Language Models](https://arxiv.org/abs/2406.18915) | 2024 | Paper | <a href="https://github.com/Robot-MA/manipulate-anything"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [robo-harness](https://github.com/grmkris/robo-harness) | — | Repository | <a href="https://github.com/grmkris/robo-harness"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o2-a1-code"></a>

## O2 / A1 Code

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/abs/2607.10350) | 2026 | Paper | — |
| [AgentVLN: Towards Agentic Vision-and-Language Navigation](https://arxiv.org/abs/2603.17670) | 2026 | Paper | <a href="https://github.com/Allenxinn/AgentVLN"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ASPIRE: Public Robot Skill Discovery Implementation](https://github.com/NVlabs/ASPIRE/tree/fa00f0ef2bc1d91d594b9aa502c22133c9f538f7) | 2026 | Repository | <a href="https://github.com/NVlabs/ASPIRE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Bridging Semantics and Physics with Constrained LLMs for Safe and Trustworthy Robotic Manipulation](https://arxiv.org/abs/2608.29379) | 2026 | Paper | — |
| [Embodied Task Agents Can Perform Fine Manipulation through Tactile In-Context Learning](https://arxiv.org/abs/2610.27613) | 2026 | Paper | <a href="https://github.com/No-518/Tactile-ETA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ETA: A New Agentic Paradigm for Embodied Tasks](https://arxiv.org/abs/2608.03924) | 2026 | Paper | <a href="https://github.com/OpenMOSS/OpenETA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use](https://arxiv.org/abs/2608.14047) | 2026 | Paper | — |
| [EvoMemNav: Efficient Self-Evolving Fine-Grained Memory for Zero-Shot Embodied Navigation](https://arxiv.org/abs/2606.03509) | 2026 | Paper | — |
| [Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](https://arxiv.org/abs/2607.13653) | 2026 | Paper | <a href="https://github.com/InternRobotics/REAL"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Guava: Distilling Frontier VLM Agents into a Compact Model with a Manipulation Harness](https://arxiv.org/abs/2606.18363) | 2026 | Paper | <a href="https://github.com/hdacnw/guava-release"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HATS: A Human-Agent Teleoperation System for Multi-Arm Data Collection](https://arxiv.org/abs/2606.16491) | 2026 | Paper | — |
| [HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System](https://arxiv.org/abs/2603.14807) | 2026 | Paper | <a href="https://github.com/lvkailin0118/HiMemVLN"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HomeBody: A Humanoid That Explores, Remembers, and Acts on Its Own](https://tml.stanford.edu/homebody/) | 2026 | Project / report | <a href="https://github.com/Stanford-TML/homebody"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Know Your Body: A Harness for Direct and Self-Improving Robot Control with VLMs](https://arxiv.org/abs/2609.28530) | 2026 | Paper | — |
| [KPI: A Promptable Kernel for Physical Interaction on Humanoids](https://arxiv.org/abs/2609.36151) | 2026 | Paper | — |
| [M2HRI: An LLM-Driven Multimodal Multi-Agent Framework for Personalized Human-Robot Interaction](https://arxiv.org/abs/2604.11975) | 2026 | Paper | — |
| [Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools](https://arxiv.org/abs/2609.39018) | 2026 | Paper | — |
| [MEMORA: Embodied Action Memory from Egocentric Videos for Reasoning and Planning](https://arxiv.org/abs/2607.14252) | 2026 | Paper | <a href="https://github.com/yuzihaowashu/MEMORA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation](https://arxiv.org/abs/2609.38078) | 2026 | Paper | <a href="https://github.com/Motor-Mind/MotorMind-Code"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [PLanAR: Planning-Language-Grounded Agentic Reasoning for Robot Manipulation](https://arxiv.org/abs/2602.01662) | 2026 | Paper | — |
| [RACAS: Controlling Diverse Robots With a Single Agentic System](https://arxiv.org/abs/2603.05621) | 2026 | Paper | <a href="https://github.com/janprz11/robot-agnostic-control"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboStream: Weaving Spatio-Temporal Reasoning with Memory in Vision-Language Models for Robotics](https://arxiv.org/abs/2603.12939) | 2026 | Paper | — |
| [SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM](https://arxiv.org/abs/2603.08269) | 2026 | Paper | — |
| [SpaceVLN: A Zero-Shot Vision-and-Language Navigation Agent with Online Spatial Cognitive Memory and Reasoning](https://arxiv.org/abs/2606.08992) | 2026 | Paper | — |
| [SysNav: Multi-Level Systematic Cooperation Enables Real-World, Cross-Embodiment Object Navigation](https://arxiv.org/abs/2603.06914) | 2026 | Paper | <a href="https://github.com/zwandering/SysNav"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Uni-Skill: Building Self-Evolving Skill Repository for Generalizable Robotic Manipulation](https://arxiv.org/abs/2603.02623) | 2026 | Paper | — |
| [A Pragmatist Robot: Learning to Plan Tasks by Experiencing the Real World](https://arxiv.org/abs/2507.16713) | 2025 | Paper | <a href="https://github.com/leggedrobotics/pragmabot"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [CLEA: Closed-Loop Embodied Agent for Enhancing Task Execution in Dynamic Environments](https://arxiv.org/abs/2503.00729) | 2025 | Paper | <a href="https://github.com/SP4595/CLEA-Closed-Loop-Embodied-Agent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LLM-Empowered Embodied Agent for Memory-Augmented Task Planning in Household Robotics](https://arxiv.org/abs/2504.21716) | 2025 | Paper | <a href="https://github.com/marc1198/chat-hsr"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboMemory: A Brain-inspired Multi-memory Agentic Framework for Interactive Environmental Learning in Physical Embodied Systems](https://arxiv.org/abs/2508.01415) | 2025 | Paper | — |
| [RoboReflect: A Robotic Reflective Reasoning Framework for Grasping Ambiguous-Condition Objects](https://arxiv.org/abs/2501.09307) | 2025 | Paper | — |
| [Towards Proprioception-Aware Embodied Planning for Dual-Arm Humanoid Robots](https://arxiv.org/abs/2510.07882) | 2025 | Paper | <a href="https://github.com/ds199895/DualTHOR"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [BUMBLE: Unifying Reasoning and Acting with Vision-Language Models for Building-wide Mobile Manipulation](https://arxiv.org/abs/2410.06237) | 2024 | Paper | <a href="https://github.com/UT-Austin-RobIn/BUMBLE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models](https://arxiv.org/abs/2409.15146) | 2024 | Paper | <a href="https://github.com/MrKeee/COHERENT"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [InterPreT: Interactive Predicate Learning from Language Feedback for Generalizable Task Planning](https://arxiv.org/abs/2405.19758) | 2024 | Paper | <a href="https://github.com/hmz-15/interactive-predicate-learning"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation](https://arxiv.org/abs/2403.08605) | 2024 | Paper | <a href="https://github.com/robot-learning-freiburg/MoMa-LLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LLM3:Large Language Model-based Task and Motion Planning with Motion Failure Reasoning](https://arxiv.org/abs/2403.11552) | 2024 | Paper | <a href="https://github.com/AssassinWS/LLM-TAMP"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [MOKA: Open-World Robotic Manipulation through Mark-Based Visual Prompting](https://arxiv.org/abs/2403.03174) | 2024 | Paper | <a href="https://github.com/moka-manipulation/moka"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Multi-Modal Grounded Planning and Efficient Replanning For Learning Embodied Agents with A Few Examples](https://arxiv.org/abs/2412.17288) | 2024 | Paper | <a href="https://github.com/snumprlab/flare"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs](https://arxiv.org/abs/2409.18794) | 2024 | Paper | <a href="https://github.com/YanyuanQiao/Open-Nav"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ReMEmbR: Building and Reasoning Over Long-Horizon Spatio-Temporal Memory for Robot Navigation](https://arxiv.org/abs/2409.13682) | 2024 | Paper | <a href="https://github.com/NVIDIA-AI-IOT/remembr"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Robi Butler: Multimodal Remote Interaction with a Household Robot Assistant](https://arxiv.org/abs/2409.20548) | 2024 | Paper | <a href="https://github.com/threefruits/zoom_robot_interface"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ROS-LLM: A ROS framework for embodied AI with task feedback and structured reasoning](https://arxiv.org/abs/2406.19741) | 2024 | Paper | <a href="https://github.com/huawei-noah/HEBO/tree/master/ROSLLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SPINE: Online Semantic Planning for Missions with Incomplete Natural Language Specifications in Unstructured Environments](https://arxiv.org/abs/2410.03035) | 2024 | Paper | <a href="https://github.com/KumarRobotics/spine"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) | 2023 | Paper | <a href="https://github.com/UMass-Embodied-AGI/CoELA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Co-NavGPT: Multi-Robot Cooperative Visual Semantic Navigation Using Vision Language Models](https://arxiv.org/abs/2310.07937) | 2023 | Paper | <a href="https://github.com/ybgdgh/Co-NavGPT2"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://arxiv.org/abs/2309.16650) | 2023 | Paper | <a href="https://github.com/concept-graphs/concept-graphs"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [CoPAL: Corrective Planning of Robot Actions with Large Language Models](https://arxiv.org/abs/2310.07263) | 2023 | Paper | — |
| [DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://arxiv.org/abs/2307.00329) | 2023 | Paper | — |
| [Language to Rewards for Robotic Skill Synthesis](https://arxiv.org/abs/2306.08647) | 2023 | Paper | <a href="https://github.com/google-deepmind/language_to_reward_2023"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoCo: Dialectic Multi-Robot Collaboration with Large Language Models](https://arxiv.org/abs/2307.04738) | 2023 | Paper | <a href="https://github.com/MandiZhao/robot-collab"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning](https://arxiv.org/abs/2307.06135) | 2023 | Paper | — |
| [TidyBot: Personalized Robot Assistance with Large Language Models](https://arxiv.org/abs/2305.05658) | 2023 | Paper | <a href="https://github.com/jimmyyhwu/tidybot"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](https://arxiv.org/abs/2212.04088) | 2022 | Paper | <a href="https://github.com/OSU-NLP-Group/LLM-Planner"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiedJev](https://github.com/FBddcz/embodied-jev) | — | Repository | <a href="https://github.com/FBddcz/embodied-jev"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o2-a1-model"></a>

## O2 / A1 Model

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [Exploratory, Communicative, and Deployable: Vision-Driven Embodied Agents for Open-World Mobile Manipulation](https://arxiv.org/abs/2607.13653) | 2026 | Paper | <a href="https://github.com/InternRobotics/REAL"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.18869) | 2026 | Paper | — |
| [KPI: A Promptable Kernel for Physical Interaction on Humanoids](https://arxiv.org/abs/2609.36151) | 2026 | Paper | — |
| [ME-Brain-1.0: Memory, Cognition and Action for Evolving Embodied Intelligence](https://arxiv.org/abs/2609.24271) | 2026 | Paper | — |
| [RoBridge: A Hierarchical Architecture Bridging Cognition and Execution for General Robotic Manipulation](https://arxiv.org/abs/2505.01709) | 2025 | Paper | <a href="https://github.com/abliao/RoBridge"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Robi Butler: Multimodal Remote Interaction with a Household Robot Assistant](https://arxiv.org/abs/2409.20548) | 2024 | Paper | <a href="https://github.com/threefruits/zoom_robot_interface"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ROS-LLM: A ROS framework for embodied AI with task feedback and structured reasoning](https://arxiv.org/abs/2406.19741) | 2024 | Paper | <a href="https://github.com/huawei-noah/HEBO/tree/master/ROSLLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [DoReMi: Grounding Language Model by Detecting and Recovering from Plan-Execution Misalignment](https://arxiv.org/abs/2307.00329) | 2023 | Paper | — |
| [LLM-State: Open World State Representation for Long-horizon Task Planning with Large Language Model](https://arxiv.org/abs/2311.17406) | 2023 | Paper | — |
| [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928) | 2023 | Paper | <a href="https://github.com/google-research/google-research/tree/master/language_model_uncertainty"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Text2Motion: From Natural Language Instructions to Feasible Plans](https://arxiv.org/abs/2303.12153) | 2023 | Paper | — |
| [Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691) | 2022 | Paper | <a href="https://github.com/google-research/google-research/tree/master/saycan"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) | 2022 | Paper | — |
| [LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](https://arxiv.org/abs/2212.04088) | 2022 | Paper | <a href="https://github.com/OSU-NLP-Group/LLM-Planner"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Open-vocabulary Queryable Scene Representations for Real World Planning](https://arxiv.org/abs/2209.09874) | 2022 | Paper | — |

<a id="o2-a2"></a>

## O2 / A2

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474) | 2026 | Paper | — |
| [Addressing the Orchestration Gap in Generalist Robots via Physical Agency](https://arxiv.org/abs/2607.21725) | 2026 | Paper | <a href="https://github.com/lianegalanti/Pigey"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [CLASP: Language-Driven Robot Skill Selection and Composition using Task-Parameterized Learning](https://arxiv.org/abs/2606.08169) | 2026 | Paper | — |
| [Co-Evolving Robot Orchestrators and Policies through Deployment](https://arxiv.org/abs/2610.09228) | 2026 | Paper | — |
| [DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents](https://arxiv.org/abs/2609.40306) | 2026 | Paper | — |
| [Enabling Extensible Embodied Capabilities with Tools](https://arxiv.org/abs/2605.26637) | 2026 | Paper | — |
| [ETA: A New Agentic Paradigm for Embodied Tasks](https://arxiv.org/abs/2608.03924) | 2026 | Paper | <a href="https://github.com/OpenMOSS/OpenETA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HarnessVLN: Unifying Training-Free Embodied Navigation through an Agent Harness](https://arxiv.org/abs/2609.15195) | 2026 | Paper | — |
| [HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](https://arxiv.org/abs/2606.23565) | 2026 | Paper | <a href="https://github.com/HorizonRobotics/HoloAgent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning](https://arxiv.org/abs/2609.29394) | 2026 | Paper | <a href="https://github.com/Robo-Harness/racap"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RegenHarness: A Robot Agent Harness with Evidence-Gated Recursive Self-Improvement](https://arxiv.org/abs/2609.27612) | 2026 | Paper | — |
| [RHO: Your Coding Agent is Secretly a Roboticist](https://arxiv.org/abs/2606.16458) | 2026 | Paper | <a href="https://github.com/KE7/HELIX"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Robo-Harness K1: Harnessing Robot-Use Agents via Perception Augmentation](https://arxiv.org/abs/2609.29389) | 2026 | Paper | <a href="https://github.com/Robo-Harness/k1"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboClaw: An Agentic Framework for Scalable Long-Horizon Robotic Tasks](https://arxiv.org/abs/2603.11558) | 2026 | Paper | <a href="https://github.com/RoboClaw-Robotics/RoboClaw"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboDoctor: Training-Free Recursive Self-Improvement for Robot Policies](https://robodoctor-rsi.github.io/) | 2026 | Project / report | <a href="https://github.com/THUSI-Lab/RoboDoctor"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboHarn-Evo: Evolving Hierarchical Physical Knowledge for Self-Improving Robotic Manipulation](https://arxiv.org/abs/2609.37583) | 2026 | Paper | <a href="https://github.com/RUCKBReasoning/RoboHarn-Evo"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboHarness: A Simple Harness Outperforms VLA and World Action Models](https://bincequ.github.io/RoboHarness/) | 2026 | Project / report | <a href="https://github.com/BinceQu/RoboHarness"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060) | 2026 | Paper | — |
| [ROSClaw: An OpenClaw ROS 2 Framework for Agentic Robot Control and Interaction](https://arxiv.org/abs/2603.26997) | 2026 | Paper | <a href="https://github.com/ROSClaw/rosclaw"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SCOPE: Real-Time Natural Language Camera Agent at the Edge](https://arxiv.org/abs/2606.02951) | 2026 | Paper | — |
| [Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence](https://arxiv.org/abs/2609.35432) | 2026 | Paper | — |
| [TARSphere: A Robot-Oriented Full-Stack Framework for Long-Horizon Embodied Agents in Evolving Physical and Social Environments](https://arxiv.org/abs/2610.30043) | 2026 | Paper · [Project](https://xuyicheng-zju.github.io/TARSphere/) | <a href="https://github.com/xuyicheng-zju/TARSphere"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Towards the Harness of Embodied Agents](https://arxiv.org/abs/2608.11246) | 2026 | Paper | <a href="https://github.com/EIT-HAI/Thea"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal](https://arxiv.org/abs/2609.29964) | 2026 | Paper | — |
| [General-Purpose Robotic Navigation via LVLM-Orchestrated Perception, Reasoning, and Acting](https://arxiv.org/abs/2506.17462) | 2025 | Paper | — |
| [RAI: Flexible Agent Framework for Embodied AI](https://arxiv.org/abs/2505.07532) | 2025 | Paper | <a href="https://github.com/RobotecAI/rai"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o2-a3"></a>

## O2 / A3

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [Agent as Policy for Robotic Manipulation](https://arxiv.org/abs/2609.12541) | 2026 | Paper | <a href="https://github.com/agent-as-policy-2026/agent-as-policy"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](https://arxiv.org/abs/2610.10479) | 2026 | Paper | — |
| [ASPIRE: Agentic /Skills Discovery for Robotics](https://arxiv.org/abs/2607.00272) | 2026 | Paper | <a href="https://github.com/NVlabs/ASPIRE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ASPIRE: Public Robot Skill Discovery Implementation](https://github.com/NVlabs/ASPIRE/tree/fa00f0ef2bc1d91d594b9aa502c22133c9f538f7) | 2026 | Repository | <a href="https://github.com/NVlabs/ASPIRE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) | 2026 | Paper | <a href="https://github.com/capgym/cap-x"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Co-Evolving Robot Orchestrators and Policies through Deployment](https://arxiv.org/abs/2610.09228) | 2026 | Paper | — |
| [Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens](https://arxiv.org/abs/2610.01939) | 2026 | Paper | <a href="https://github.com/DAGroup-PKU/PyRUA-Lean"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [From Reaction to Anticipation: Proactive Failure Recovery through Agentic Task Graph for Robotic Manipulation](https://arxiv.org/abs/2605.11951) | 2026 | Paper | <a href="https://github.com/EDEM-AI/AgentChord"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](https://arxiv.org/abs/2607.05369) | 2026 | Paper | <a href="https://github.com/graph-robots/graph-as-policy"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Guava: Distilling Frontier VLM Agents into a Compact Model with a Manipulation Harness](https://arxiv.org/abs/2606.18363) | 2026 | Paper | <a href="https://github.com/hdacnw/guava-release"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents](https://arxiv.org/abs/2610.23479) | 2026 | Paper | <a href="https://github.com/HexaFuture/HexaShell"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration](https://arxiv.org/abs/2610.23098) | 2026 | Paper | — |
| [Introducing Waddle: Agents that Control Robots](https://waddlelabs.ai/research/introducing-waddle) | 2026 | Project / report | — |
| [Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools](https://arxiv.org/abs/2609.39018) | 2026 | Paper | — |
| [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419) | 2026 | Paper | <a href="https://github.com/Playful-RATs/rats"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning](https://arxiv.org/abs/2609.29394) | 2026 | Paper | <a href="https://github.com/Robo-Harness/racap"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RAPID: Robot Agentic Programming from Demonstrations](https://arxiv.org/abs/2609.30249) | 2026 | Paper | — |
| [RE-0: Verified Recursive Improvement of Embodied Code-as-Policy Agents through Local On-Policy Distillation](https://arxiv.org/abs/2609.32416) | 2026 | Paper | — |
| [Real2Gym: Building Gyms from Videos, Bringing Skills to Robots](https://arxiv.org/abs/2609.37089) | 2026 | Paper | <a href="https://github.com/real2gym/R2G_Agent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204) | 2026 | Paper | — |
| [Recova: Agent-Guided Failure Recovery for Autonomous Robotic Manipulation](https://arxiv.org/abs/2610.01178) | 2026 | Paper | — |
| [Retriever: Composing the Perception-Reasoning-Action Loop for Long-Horizon Manipulation](https://arxiv.org/abs/2607.17213) | 2026 | Paper | <a href="https://github.com/openretriever/retriever"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RHO: Your Coding Agent is Secretly a Roboticist](https://arxiv.org/abs/2606.16458) | 2026 | Paper | <a href="https://github.com/KE7/HELIX"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents](https://arxiv.org/abs/2609.32862) | 2026 | Paper | — |
| [Scaling Online Exploration for Robot Agents](https://arxiv.org/abs/2610.22496) | 2026 | Paper | <a href="https://github.com/robot-agent-exploration/rax/tree/real/franka"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SEAR: Self-Evolving Agentic Robotics](https://arxiv.org/abs/2610.18792) | 2026 | Paper | — |
| [Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence](https://arxiv.org/abs/2609.35432) | 2026 | Paper | — |
| [Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence](https://arxiv.org/abs/2608.16590) | 2026 | Paper | <a href="https://github.com/air-embodied-brain/Zetta-Embodiment"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Code-as-Symbolic-Planner: Foundation Model-Based Robot Planning via Symbolic Code Generation](https://arxiv.org/abs/2503.01700) | 2025 | Paper | <a href="https://github.com/yongchao98/Code-as-Symbolic-Planner"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Maestro: Orchestrating Robotics Modules with Vision-Language Models for Zero-Shot Generalist Robots](https://arxiv.org/abs/2511.00917) | 2025 | Paper | — |
| [Memory Transfer Planning: LLM-driven Context-Aware Code Adaptation for Robot Manipulation](https://arxiv.org/abs/2509.24160) | 2025 | Paper | — |
| [Robotic Long-Horizon Manipulation with Progressive In-Context Code Generation and Episodic Feedback](https://arxiv.org/abs/2503.21969) | 2025 | Paper | <a href="https://github.com/Ghiara/DAHLIA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Towards Reliable Code-as-Policies: A Neuro-Symbolic Framework for Embodied Task Planning](https://arxiv.org/abs/2510.21302) | 2025 | Paper | — |
| [ChatGPT for Robotics: Design Principles and Model Abilities](https://doi.org/10.1109/ACCESS.2024.3387941) | 2024 | Paper | — |
| [Closed-Loop Open-Vocabulary Mobile Manipulation with GPT-4V](https://arxiv.org/abs/2404.10220) | 2024 | Paper | — |
| [GenCHiP: Generating Robot Policy Code for High-Precision and Contact-Rich Manipulation Tasks](https://arxiv.org/abs/2404.06645) | 2024 | Paper | — |
| [Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models](https://arxiv.org/abs/2406.18746) | 2024 | Paper | — |
| [MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation](https://arxiv.org/abs/2411.17636) | 2024 | Paper | — |
| [RePLan: Robotic Replanning with Perception and Language Models](https://arxiv.org/abs/2401.04157) | 2024 | Paper | — |
| [RoboScript: Code Generation for Free-Form Manipulation Tasks across Real and Simulation](https://arxiv.org/abs/2402.14623) | 2024 | Paper | <a href="https://github.com/SgtVincent/RoboScript"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ROS-LLM: A ROS framework for embodied AI with task feedback and structured reasoning](https://arxiv.org/abs/2406.19741) | 2024 | Paper | <a href="https://github.com/huawei-noah/HEBO/tree/master/ROSLLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Deploying and Evaluating LLMs to Program Service Mobile Robots](https://arxiv.org/abs/2311.11183) | 2023 | Paper | <a href="https://github.com/ut-amrl/codebotler"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Distilling and Retrieving Generalizable Knowledge for Robot Manipulation via Language Corrections](https://arxiv.org/abs/2311.10678) | 2023 | Paper | <a href="https://github.com/Stanford-ILIAD/droc"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model](https://arxiv.org/abs/2305.11176) | 2023 | Paper | <a href="https://github.com/OpenGVLab/Instruct2Act"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Lifelong Robot Learning with Human Assisted Language Planners](https://arxiv.org/abs/2309.14321) | 2023 | Paper | — |
| [Statler: State-Maintaining Language Models for Embodied Reasoning](https://arxiv.org/abs/2306.17840) | 2023 | Paper | <a href="https://github.com/ripl/statler"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) | 2022 | Paper | <a href="https://github.com/google-research/google-research/tree/master/code_as_policies"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ProgPrompt: Generating Situated Robot Task Plans using Large Language Models](https://arxiv.org/abs/2209.11302) | 2022 | Paper | — |

<a id="o3-a1-code"></a>

## O3 / A1 Code

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [Code Owns the Simulation, Jev Owns the Evaluation](https://arxiv.org/abs/2610.01834) | 2026 | Paper | — |
| [DV-VLN: Dual Verification for Reliable LLM-Based Vision-and-Language Navigation](https://arxiv.org/abs/2601.18492) | 2026 | Paper | — |
| [GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning](https://arxiv.org/abs/2609.19315) | 2026 | Paper | — |
| [Jev Arm Demo: Jev vs LLM: Robot Arm Control](https://github.com/FazalAAli/jev-robotics-demo) | 2026 | Engineering demo | <a href="https://github.com/FazalAAli/jev-robotics-demo"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Askable Arm: jev-askable-arm](https://github.com/TarunTomar122/jev-askable-arm) | 2026 | Engineering demo | <a href="https://github.com/TarunTomar122/jev-askable-arm"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [jev-drone](https://github.com/RomanSlack/jev-drone) | 2026 | Repository | <a href="https://github.com/RomanSlack/jev-drone"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [jev-libero](https://github.com/Dimweaker/jev-libero) | 2026 | Repository | <a href="https://github.com/Dimweaker/jev-libero"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [jev-robot-control](https://github.com/openroboto-ai/jev-robot-control) | 2026 | Repository | <a href="https://github.com/openroboto-ai/jev-robot-control"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboJEV](https://github.com/lykycy123/RoboJEV) | 2026 | Repository | <a href="https://github.com/lykycy123/RoboJEV"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RobotWorld: Benchmarking Multimodal Agents for Robot Use Across Diverse Tasks and Embodiments](https://arxiv.org/abs/2610.10409) | 2026 | Paper | <a href="https://github.com/robotworldai/robotworld"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents](https://arxiv.org/abs/2410.22662) | 2024 | Paper | <a href="https://github.com/SgtVincent/EMOS"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Language-Grounded Dynamic Scene Graphs for Interactive Object Search with Mobile Manipulation](https://arxiv.org/abs/2403.08605) | 2024 | Paper | <a href="https://github.com/robot-learning-freiburg/MoMa-LLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Large Language Models for Orchestrating Bimanual Robots](https://arxiv.org/abs/2404.02018) | 2024 | Paper | <a href="https://github.com/Kchu/LABOR-Agent"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LLaMAR: Long-Horizon Planning for Multi-Agent Robots in Partially Observable Environments](https://arxiv.org/abs/2407.10031) | 2024 | Paper | <a href="https://github.com/nsidn98/LLaMAR"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LLM-Personalize: Aligning LLM Planners with Human Preferences via Reinforced Self-Training for Housekeeping Robots](https://arxiv.org/abs/2404.14285) | 2024 | Paper | <a href="https://github.com/gdg94/codellmpersonalize"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LLM3:Large Language Model-based Task and Motion Planning with Motion Failure Reasoning](https://arxiv.org/abs/2403.11552) | 2024 | Paper | <a href="https://github.com/AssassinWS/LLM-TAMP"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [MapGPT: Map-Guided Prompting with Adaptive Path Planning for Vision-and-Language Navigation](https://arxiv.org/abs/2401.07314) | 2024 | Paper | <a href="https://github.com/chen-judge/MapGPT"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://arxiv.org/abs/2411.00081) | 2024 | Paper | <a href="https://github.com/facebookresearch/partnr-planner"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models](https://arxiv.org/abs/2409.19471) | 2024 | Paper | <a href="https://github.com/lt-asset/selp"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [AutoTAMP: Autoregressive Task and Motion Planning with LLMs as Translators and Checkers](https://arxiv.org/abs/2306.06531) | 2023 | Paper | <a href="https://github.com/yongchao98/AutoTAMP"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Building Cooperative Embodied Agents Modularly with Large Language Models](https://arxiv.org/abs/2307.02485) | 2023 | Paper | <a href="https://github.com/UMass-Embodied-AGI/CoELA"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Language to Rewards for Robotic Skill Synthesis](https://arxiv.org/abs/2306.08647) | 2023 | Paper | <a href="https://github.com/google-deepmind/language_to_reward_2023"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [LLM-State: Open World State Representation for Long-horizon Task Planning with Large Language Model](https://arxiv.org/abs/2311.17406) | 2023 | Paper | — |
| [NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models](https://arxiv.org/abs/2305.16986) | 2023 | Paper | <a href="https://github.com/GengzeZhou/NavGPT"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction](https://arxiv.org/abs/2306.15724) | 2023 | Paper | <a href="https://github.com/columbia-ai-robotics/reflect"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://arxiv.org/abs/2307.01928) | 2023 | Paper | <a href="https://github.com/google-research/google-research/tree/master/language_model_uncertainty"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoCo: Dialectic Multi-Robot Collaboration with Large Language Models](https://arxiv.org/abs/2307.04738) | 2023 | Paper | <a href="https://github.com/MandiZhao/robot-collab"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems?](https://arxiv.org/abs/2309.15943) | 2023 | Paper | <a href="https://github.com/yongchao98/multi-agent-framework"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition](https://arxiv.org/abs/2307.14535) | 2023 | Paper | <a href="https://github.com/columbia-ai-robotics/scalingup"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [EmbodiedJev](https://github.com/FBddcz/embodied-jev) | — | Repository | <a href="https://github.com/FBddcz/embodied-jev"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o3-a1-model"></a>

## O3 / A1 Model

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [Agent Priors-guided Policy Learning](https://arxiv.org/abs/2609.35690) | 2026 | Paper | — |
| [PARTNR: A Benchmark for Planning and Reasoning in Embodied Multi-agent Tasks](https://arxiv.org/abs/2411.00081) | 2024 | Paper | <a href="https://github.com/facebookresearch/partnr-planner"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |

<a id="o3-a2"></a>

## O3 / A2

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510) | 2026 | Paper | — |
| [DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents](https://arxiv.org/abs/2609.40306) | 2026 | Paper | — |
| [EmbodiRSI: Recursive Self-Improvement for Data-Efficient Robot Adaptation](https://arxiv.org/abs/2609.38905) | 2026 | Paper | — |
| [Jev Arm Demo: Jev vs LLM: Robot Arm Control](https://github.com/FazalAAli/jev-robotics-demo) | 2026 | Engineering demo | <a href="https://github.com/FazalAAli/jev-robotics-demo"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [RoboHarness: Memory-Driven Orchestration of Heterogeneous Robot Policies for Long-Horizon Planning](https://arxiv.org/abs/2607.18060) | 2026 | Paper | — |

<a id="o3-a3"></a>

## O3 / A3

| Work | Year | Source | Code |
| --- | --- | --- | --- |
| [AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.20474) | 2026 | Paper | — |
| [Agentic RSR: Real-to-Sim-to-Real through Scene Reconstruction and Execution-Grounded Robot Policies](https://arxiv.org/abs/2610.10479) | 2026 | Paper | — |
| [AgenticRoboRL: Bringing Coding-Agent Post-Training to Agentic Robotics](https://arxiv.org/abs/2610.28589) | 2026 | Paper | <a href="https://github.com/xinxinliu-ai/AgenticRoboRL"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510) | 2026 | Paper | — |
| [CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435) | 2026 | Paper | <a href="https://github.com/capgym/cap-x"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embodied First Exam](https://github.com/mll-lab-nu/embodied-first-exam) | 2026 | Repository | <a href="https://github.com/mll-lab-nu/embodied-first-exam"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Embodied Playground: A Long-Horizon Agentic Robotics Benchmark for Physical, Strategic, and Spatial Reasoning](https://arxiv.org/abs/2610.27039) | 2026 | Paper | — |
| [ETM: Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement](https://arxiv.org/abs/2610.12369) | 2026 | Paper · [Project](https://ropedia.github.io/ropedia-a0/) | — |
| [EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308) | 2026 | Paper | <a href="https://github.com/EmbodiedSWE/EmbodiedSWE"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [GaP: A Graph-as-Policy Multi-Agent Self-Learning Harness For Variational Automation Tasks](https://arxiv.org/abs/2607.05369) | 2026 | Paper | <a href="https://github.com/graph-robots/graph-as-policy"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Gemini 4 Argon for Robotics](https://developers.googleblog.com/gemini-4-argon-for-robotics/) | 2026 | Project / report | — |
| [Playful Agentic Robot Learning](https://arxiv.org/abs/2606.19419) | 2026 | Paper | <a href="https://github.com/Playful-RATs/rats"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents](https://arxiv.org/abs/2610.02204) | 2026 | Paper | — |
| [RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents](https://arxiv.org/abs/2609.32862) | 2026 | Paper | — |
| [RoboSimStudio: An Interactive Toolkit for Human and Agent Rapid Real2Sim of Robot Manipulation Tasks](https://arxiv.org/abs/2610.18835) | 2026 | Paper | <a href="https://github.com/robosimstudio/robosimstudio"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SkillClaw: Collectively Self-Improving Robot Agents](https://github.com/lilyzhng/SkillClaw) | 2026 | Repository | <a href="https://github.com/lilyzhng/SkillClaw"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [VLCP: Vision Language Control Policy Closed-Loop Code Replanning for Robot Manipulation](https://arxiv.org/abs/2608.16978) | 2026 | Paper | — |
| [ChatGPT for Robotics: Design Principles and Model Abilities](https://doi.org/10.1109/ACCESS.2024.3387941) | 2024 | Paper | — |
| [Lifelong Robot Library Learning: Bootstrapping Composable and Generalizable Skills for Embodied Control with Language Models](https://arxiv.org/abs/2406.18746) | 2024 | Paper | — |
| [MALMM: Multi-Agent Large Language Models for Zero-Shot Robotics Manipulation](https://arxiv.org/abs/2411.17636) | 2024 | Paper | — |
| [RoboScript: Code Generation for Free-Form Manipulation Tasks across Real and Simulation](https://arxiv.org/abs/2402.14623) | 2024 | Paper | <a href="https://github.com/SgtVincent/RoboScript"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models](https://arxiv.org/abs/2309.10062) | 2023 | Paper | <a href="https://github.com/SMARTlab-Purdue/SMART-LLM"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [Code as Policies: Language Model Programs for Embodied Control](https://arxiv.org/abs/2209.07753) | 2022 | Paper | <a href="https://github.com/google-research/google-research/tree/master/code_as_policies"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a> |
| [ProgPrompt: Generating Situated Robot Task Plans using Large Language Models](https://arxiv.org/abs/2209.11302) | 2022 | Paper | — |

[Back to overview](../README.md)
