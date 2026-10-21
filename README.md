<div align="center">
  <img src="https://huggingface.co/spaces/RoboAgentLab/README/resolve/main/avatar.png" width="90" alt="RoboAgentLab">
  <h1>Awesome Agentic Robotics</h1>
  <p><strong>Agents that Act, Build, and Evolve.</strong></p>
  <p>A curated reading list for robot execution, robotics development, and persistent improvement.</p>
  <p>
    <a href="https://github.com/RoboAgentLab/RoboAgentLab">Open platform</a> ·
    <a href="https://huggingface.co/RoboAgentLab">Datasets</a> ·
    <a href="CONTRIBUTING.md">Contribute</a>
  </p>
</div>

## Overview

Foundation-model agents can direct robot behavior, build robotics workflows, and revise systems from feedback. This collection follows the framework of our forthcoming paper, **Agents that Act, Build, and Evolve: A Unified Framework and Platform for Agentic Robotics**.

Browse **382 sources across 29 categories**. Categories are non-exclusive; distinct configurations of a work may appear in several places.

| Role | What the agent does | Browse |
| --- | --- | --- |
| **Act — Agent as Policy** | Select behaviors, orchestrate tools, or write robot-execution programs. | [Observation × execution interfaces](docs/policy.md) |
| **Build — Agent as Infrastructure** | Construct and coordinate collection, training, evaluation, and diagnosis workflows. | [Development lifecycle](docs/infrastructure.md) |
| **Evolve — Agent as Self-Evolver** | Use feedback to revise and retain artifacts, components, or the agent harness. | [Retained update targets](docs/self-evolver.md) |

## Browse the collection

### Agent as Policy

| Observation interface | A1: Behavior Selection | A2: Tool Orchestration | A3: Code Synthesis |
| --- | --- | --- | --- |
| **O1 — Sensory input** | [Code executor](docs/policy.md#o1-a1-code) · [Model executor](docs/policy.md#o1-a1-model) | [O1 / A2](docs/policy.md#o1-a2) | [O1 / A3](docs/policy.md#o1-a3) |
| **O2 — Perception tools** | [Code executor](docs/policy.md#o2-a1-code) · [Model executor](docs/policy.md#o2-a1-model) | [O2 / A2](docs/policy.md#o2-a2) | [O2 / A3](docs/policy.md#o2-a3) |
| **O3 — Privileged state** | [Code executor](docs/policy.md#o3-a1-code) · [Model executor](docs/policy.md#o3-a1-model) | [O3 / A2](docs/policy.md#o3-a2) | [O3 / A3](docs/policy.md#o3-a3) |

### Agent as Infrastructure

| Stage | Categories |
| --- | --- |
| Collection | [Environment Generation](docs/infrastructure.md#infrastructure-environment-generation) · [Dataset Construction](docs/infrastructure.md#infrastructure-dataset-construction) |
| Training | [Training](docs/infrastructure.md#infrastructure-training) |
| Inference | [Evaluation](docs/infrastructure.md#infrastructure-evaluation) · [Diagnosis](docs/infrastructure.md#infrastructure-diagnosis) |

### Agent as Self-Evolver

| Family | Update targets |
| --- | --- |
| Iterative Artifact Refinement | [Programs and Skills](docs/self-evolver.md#self-evolver-programs-and-skills) · [Knowledge and Memory](docs/self-evolver.md#self-evolver-knowledge-and-memory) · [Rewards](docs/self-evolver.md#self-evolver-rewards) · [Environments and Datasets](docs/self-evolver.md#self-evolver-environments-and-datasets) · [Robot Morphology](docs/self-evolver.md#self-evolver-robot-morphology) |
| Component Optimization | [Model](docs/self-evolver.md#self-evolver-model) · [Tool Code](docs/self-evolver.md#self-evolver-code) |
| Harness Improves Harness | [Representation](docs/self-evolver.md#self-evolver-representation) · [State Management](docs/self-evolver.md#self-evolver-state-management) · [Tool Interface](docs/self-evolver.md#self-evolver-tool-interface) · [Execution Workflows](docs/self-evolver.md#self-evolver-execution-workflows) |
| Successor AI R&D | [Research agents and succession](docs/self-evolver.md#self-evolver-successor-ai-r-d) |

## Scope

We include documented foundation-model agent decisions in physical or simulated robot tasks and robotics development. Ordinary VLA inference, implicit reasoning, fixed scoring, and fixed training alone do not establish an agent role. Classification follows the demonstrated configuration.

Each entry links to a primary paper, report, project, or repository. Source types are labeled. A clickable <img src="assets/github.svg" width="16" height="16" alt="GitHub" /> in the Code column links to available implementation code; a dash means no code link is currently listed. A literature entry does not imply that its implementation has been integrated into RoboAgentLab or that its reported results have been reproduced.

## RoboAgentLab resources

- **[RoboAgentLab platform](https://github.com/RoboAgentLab/RoboAgentLab)** — Robotics extensions for the [pi](https://github.com/earendil-works/pi) agent harness. Services expose simulation, robot, perception, planning, and policy capabilities; skills describe how to use them.
- **[Robot policy interactions](https://huggingface.co/datasets/RoboAgentLab/pi-embodied-policy-interactions)** — Agent interactions with robot environments.
- **[Robotics R&D interactions](https://huggingface.co/datasets/RoboAgentLab/pi-embodied-rd-interactions)** — Coding-agent traces from robotics development and testing.
- **Paper** — Public manuscript and citation information will be linked here when released.

## Contributing and reuse

Corrections and additions are welcome. Please provide a primary source, the relevant robot-domain agent decision, and the proposed classification. See [CONTRIBUTING.md](CONTRIBUTING.md).

The searchable metadata is in [`data/papers.json`](data/papers.json); reading lists can be regenerated with `python3 scripts/build.py`. This collection was initialized from our paper's taxonomy on **20 October 2026**.

We thank [Awesome-Agentic-Robots](https://github.com/chonghanqin/Awesome-Agentic-Robots) for inspiration for the reading-list presentation. This collection uses RoboAgentLab's role-based taxonomy.

Original list text and metadata are available under [CC BY 4.0](LICENSE). Linked papers, code, logos, and datasets retain their respective licenses.
