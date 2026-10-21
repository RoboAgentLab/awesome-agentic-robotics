"""Render the reading lists from public bibliographic metadata (standard library only)."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PAPERS = json.loads((ROOT / "data/papers.json").read_text())
CATEGORIES = json.loads((ROOT / "data/categories.json").read_text())

INTRO = {
    "policy": """# Agent as Policy

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
""",
    "infrastructure": """# Agent as Infrastructure

[Home](../README.md) · [Policy](policy.md) · [Self-Evolver](self-evolver.md)

Agents build and coordinate robotics development workflows across **collection, training, and inference**. Collection includes environment generation and dataset construction; inference includes evaluation and diagnosis. Inclusion requires agent decisions about the workflow, not simply running a fixed script.
""",
    "self-evolver": """# Agent as Self-Evolver

[Home](../README.md) · [Policy](policy.md) · [Infrastructure](infrastructure.md)

Agents use feedback to make changes retained for later tasks or development.

| Family | Retained update targets |
| --- | --- |
| Iterative Artifact Refinement | Programs and skills; knowledge and memory; rewards; environments and datasets; robot morphology |
| Component Optimization | Learned models; code inside reusable tools |
| Harness Improves Harness | Representation; state management; tool interfaces; execution workflows |
| Successor AI R&D | Updated researchers and subsequent research decisions |

An improvement to a tool's internal algorithm differs from a change to its calling interface. Retaining a lesson differs from changing how lessons are stored and retrieved. Membership concerns the documented update target, not every configuration of a project.

"""
}

def section_file(category):
    if category.startswith("O"):
        return "policy"
    return "infrastructure" if category.startswith("Infrastructure") else "self-evolver"

def escape(text):
    return text.replace("|", r"\|").replace("\n", " ").replace("[", r"\[").replace("]", r"\]")

def render():
    files = {}
    ids = {p["id"] for p in PAPERS}
    assert len(ids) == len(PAPERS), "Duplicate bibliography identifiers"
    known = {g["name"] for g in CATEGORIES}
    for paper in PAPERS:
        assert paper["title"] and paper["categories"]
        assert set(paper["categories"]) <= known
        assert urlparse(paper["url"]).scheme == "https", paper["id"]
        if paper.get("code_url"):
            link = urlparse(paper["code_url"])
            assert link.scheme == "https" and link.netloc == "github.com", paper["id"]
    for name, intro in INTRO.items():
        groups = [g for g in CATEGORIES if section_file(g["name"]) == name]
        text = intro + "\n## Browse\n\n"
        text += "\n".join(f'- [{g["name"]}](#{g["id"]})' for g in groups) + "\n"
        for group in groups:
            entries = sorted(
                (p for p in PAPERS if group["name"] in p["categories"]),
                key=lambda p: (-(p["year"] or 0), p["title"].casefold())
            )
            text += f'\n<a id="{group["id"]}"></a>\n\n## {group["name"]}\n\n'
            if group["name"].endswith("Successor AI R&D"):
                text += "These non-robotics works examine research-agent succession, automated research, and its evaluation. A key distinction is whether the updated model takes over later research decisions or remains the target of a fixed researcher.\n\n"
            text += "| Work | Year | Source | Code |\n| --- | --- | --- | --- |\n"
            for p in entries:
                code = f'<a href="{p["code_url"]}"><img src="../assets/github.svg" width="18" height="18" alt="GitHub" /></a>' if p.get("code_url") else "—"
                text += f'| [{escape(p["title"])}]({p["url"]}) | {p["year"] or "—"} | {p["source_type"]} | {code} |\n'
        files[f"docs/{name}.md"] = text + "\n[Back to overview](../README.md)\n"
    resources = json.loads((ROOT / "data/resources.json").read_text())
    text = "# Data and feedback resources\n\n[Home](../README.md)\n\nModels and tools supporting robotics workflows, listed separately from the agent-role taxonomy.\n"
    for r in resources:
        text += f'\n## [{r["title"]}]({r["url"]})\n\n{r["description"]}\n\n[Project]({r["url"]}) · [Open models]({r["models_url"]})\n'
    files["docs/resources.md"] = text
    return files

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Check metadata and generated reading lists.")
    args = parser.parse_args()
    outputs = render()
    for relative, content in outputs.items():
        path = ROOT / relative
        if args.check:
            assert path.read_text() == content, f"Regenerate {relative}"
        else:
            path.write_text(content)
    print(f'{"Checked" if args.check else "Rendered"} {len(PAPERS)} sources, {len(CATEGORIES)} categories, {len(outputs)} reading lists.')
