# Autonomous Researcher Loop Operating Procedure

This loop is a bounded-autonomy research workbench for the OCECM project. It should make progress without waiting for routine permission, but it must surface conceptual decisions before silently locking them into the project.

## Loop objective

Each cycle should advance at least one of these publication-critical tracks:

1. theorem development;
2. simulation design and model recovery;
3. RAID variable audit and empirical modeling;
4. manuscript/SI production;
5. claim, assumption, and citation governance.

The loop's north-star deliverable is a PNAS-ready manuscript showing that omitted context can make false cognitive models appear correct.

## Cycle structure

### 1. Orient

Read, in this order:

1. `docs/current_project_context.md`;
2. `registries/assumption_register.csv`;
3. `registries/claim_register.md`;
4. open GitHub issues labeled `decision-needed`, `proof`, `simulation`, `empirical`, or `manuscript`;
5. the latest entries in `logs/research_updates/` and `simulations/run_registry.csv`, when present;
6. files touched in the most recent merged PR.

### 2. Select one bounded task

Choose a task that can produce a reviewable artifact within one cycle. Good tasks include:

- tighten one theorem statement;
- add one simulation factor;
- write one model specification;
- produce one diagnostic table;
- draft one SI subsection;
- create one coding-audit checklist;
- update one registry entry;
- create one synthetic-data or CI test improvement.

Avoid broad tasks such as "solve theorem" or "analyze RAID" unless decomposed into a concrete subtask.

### 3. Execute

For routine implementation work, proceed without asking first. Examples:

- small code edits;
- unit tests or smoke tests;
- adding documentation;
- drafting theorem wording;
- preparing simulation grids;
- creating issue checklists;
- updating registries;
- generating synthetic public data.

### 4. Self-check

Before proposing changes, answer:

1. Does this change add or modify an assumption?
2. Does it change the estimand?
3. Does it choose or reinterpret the primary false-complex model?
4. Does it make a literature claim?
5. Does it make a causal claim about SES/context?
6. Does it require confidential RAID data?
7. Does it make a large compute request?
8. Does it promote a claim's evidence status?

If yes to any item, mark the update as requiring PI direction or registry review.

### 5. Report

Every cycle must produce two reports:

1. a human-readable update in the PR, issue, or chat;
2. a machine-readable JSON update in `logs/research_updates/` following `schemas/research_update.schema.json`.

Every cycle report should include:

- **What changed**: files, theorem pieces, simulation settings, or analysis outputs.
- **Why it matters**: relation to theorem, simulation, RAID, or manuscript.
- **Evidence**: tests run, diagnostics, citations checked, or proof obligations discharged.
- **Registry updates**: assumption/claim/run entries created or changed.
- **Open decision**: exactly one PI decision request when needed.
- **Next proposed cycle**: one bounded task.

Validate a structured update with:

```bash
make validate-update
```

## Human decision gates

Pause and request direction before:

1. adding new assumptions to a theorem;
2. changing the target estimand;
3. selecting the primary false-complex model for the empirical paper;
4. claiming the RAID context association is causal;
5. deleting files or rewriting project history;
6. running expensive jobs;
7. submitting, preprinting, or changing target venue;
8. exposing or committing confidential RAID data;
9. promoting a central claim to `supported_final`.

## Default project decisions unless overruled

Use these defaults to avoid unnecessary interruption:

- Target proof route: mixture representation -> Gaussian constructive heterogeneity -> KL dominance -> AIC/BIC threshold corollaries.
- Target empirical contrast: M2/M3 context-aware simple model versus M4 context-omitting complex model.
- Primary predictive metric: PSIS-LOO ELPD, with held-out participant log score as robustness.
- AIC/BIC: simulation/theory bridge only, not the final Bayesian empirical criterion.
- SES context proxies: income and education separately, then composite as sensitivity.
- RAID claim: model-sensitivity demonstration, not causal identification.
- Public reproducibility: synthetic RAID-style data and simulation code, not restricted data.

## Update template

```markdown
## Cycle update: <short title>

### Completed
- ...

### Why this matters
- ...

### Checks run
- ...

### Registry updates
- ...

### Decision needed
- <none, or one specific PI question>

### Next bounded task
- ...
```

## Structured update template

```json
{
  "cycle_title": "Short title",
  "track": "theorem",
  "completed": ["..."],
  "why_it_matters": ["..."],
  "files_changed": ["..."],
  "checks_run": [
    {"name": "make smoke", "status": "pass", "notes": "..."}
  ],
  "decision_needed": {
    "needed": false,
    "question": "",
    "options": [],
    "default_if_no_response": "Continue approved default."
  },
  "risks_or_uncertainties": ["..."],
  "next_bounded_task": "..."
}
```

## Quality rules

- Do not bury uncertainty.
- Do not let a more general theorem outrun the constructive proof.
- Do not interpret a complex-model win as psychological truth unless context-aware alternatives have been checked.
- Do not tune exclusions or model choice based on desired empirical conclusions.
- Prefer synthetic or simulated data in the public repo when real RAID data are restricted.
- Keep assumption and claim registries synchronized with theorem, simulation, and manuscript edits.
