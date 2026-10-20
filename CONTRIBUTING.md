# Contributing

Submit a pull request or issue with:

1. The work's title, year, and primary paper, report, or project link.
2. The documented robot-domain decision made by the agent.
3. The configuration and proposed category, supported by a section or page reference.
4. For Self-Evolver entries, what changes, how feedback is used, and what is retained.

Use concise names. Multiple categories are welcome when the source supports distinct configurations. Do not infer agentic behavior from ordinary VLA inference, a fixed score, or a fixed training procedure.

Non-robotics automated-research work belongs in the clearly labeled successor-context collection. State whether the updated researcher actually continues making later research decisions.

Edit `data/papers.json` and run:

```bash
python3 scripts/build.py
python3 scripts/build.py --check
```

Do not add private manuscript files, author correspondence, access credentials, or internal work logs. Code links should identify substantive implementations; a project-page repository alone does not establish implementation availability.
