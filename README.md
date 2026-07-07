# OCECM Autonomous Researcher Workbench

This repository is a bounded-autonomy research workbench for the project **Omitting Contextual Factors in Cognitive Models**.

## Current project thesis

When a contextual variable, such as socioeconomic resources or life-context uncertainty, shapes a latent decision parameter, omitting that contextual factor can change the observed choice law. The resulting residual structure can look like a different, more complex cognitive architecture. A false complex model may therefore beat a simpler context-omitting model in model comparison, even when a simpler context-aware model is the better mechanistic explanation.

The planned paper combines:

1. a formal theorem package;
2. Monte Carlo and RAID-calibrated simulations;
3. an empirical RAID trial-level decision-under-uncertainty demonstration;
4. a manuscript/SI package suitable for a high-impact methods-and-cognitive-science submission.

## Intended use

This is not a free-running agent swarm. It is a controlled research workbench with:

1. manager-led orchestration;
2. specialized research-agent instructions;
3. explicit human decision gates;
4. reproducible simulation scripts;
5. proof-review logs;
6. claim, assumption, citation, and run registries;
7. GitHub issue and pull-request workflows;
8. local plus cluster execution when needed.

## Start here

The autonomous researcher should read these files before taking action:

1. [`docs/current_project_context.md`](docs/current_project_context.md) — current theorem, simulation, RAID, and manuscript context.
2. [`loops/autonomous_researcher_loop.md`](loops/autonomous_researcher_loop.md) — cycle protocol and human-decision gates.
3. [`agents/research_manager.md`](agents/research_manager.md) — research-manager role prompt.
4. [`registries/README.md`](registries/README.md) — registry governance rules.
5. [`registries/assumption_register.csv`](registries/assumption_register.csv) — assumption tracking.
6. [`registries/claim_register.md`](registries/claim_register.md) — claim/evidence tracking.
7. [`docs/raid_variable_coding_memo_template.md`](docs/raid_variable_coding_memo_template.md) — required audit before empirical RAID modeling.
8. [`docs/hierarchical_bayes_milestones.md`](docs/hierarchical_bayes_milestones.md) — staged plan from GLM proxies to Stan/brms models.
9. [`schemas/research_update.schema.json`](schemas/research_update.schema.json) — structured cycle-update format.
10. [`logs/research_updates/example_update.json`](logs/research_updates/example_update.json) — example machine-readable loop update.

## Formal proof route

The current proof route is:

1. **Omitted-context mixture representation**: integrating out context induces a marginal response law.
2. **Gaussian constructive case**: omitted context induces context-dependent mean and variance in a latent parameter.
3. **KL dominance**: a flexible false model can lie closer to the omitted-context mixture than the restricted context-omitting true architecture.
4. **Finite-sample threshold corollaries**: AIC/BIC-like criteria select the false complex model when log-score gains exceed complexity penalties.

Boundary cases must always be stated: no context effect, harmless iid noise, sufficient simple random-effect structure, lack of complex-model approximation advantage, or finite-sample penalty dominance.

## Simulation scaffold

The R scaffold implements a lightweight proxy DGM and model suite:

- `R/dgm.R`: simulates a simple context-aware ambiguity task in which SES shifts latent ambiguity aversion and its heterogeneity.
- `R/fit_models.R`: fits fast GLM proxies for simple omitted context, complex omitted context, and simple context-aware reference models.
- `R/model_selection.R`: computes AIC/BIC proxy comparisons and finite-sample log-likelihood threshold diagnostics.
- `R/run_replication.R`: runs one theorem-aligned simulation replication.
- `R/run_design_cell.R`: runs a small grid cell and writes results.
- `R/generate_synthetic_raid_data.R`: generates public synthetic RAID-style trial and demographic files.

These GLM proxies are for smoke tests and fast screening only. Final empirical models should use hierarchical Bayesian structural models with PSIS-LOO and held-out participant log score.

## Bayesian modeling milestones

The staged path from proxies to publication models is documented in [`docs/hierarchical_bayes_milestones.md`](docs/hierarchical_bayes_milestones.md). The first Stan skeleton is [`stan/simple_ambiguity_single_level.stan`](stan/simple_ambiguity_single_level.stan).

Milestones:

1. proxy scaffold integrity;
2. single-level structural ambiguity likelihood;
3. participant-level hierarchical ambiguity model;
4. context-aware mean model;
5. context-aware mean-plus-variance model;
6. primary false-complex model after PI selection;
7. final empirical model suite.

## Basic commands

```bash
make smoke
make simulate-small
make synthetic-raid
make test
make validate-update
```

## Continuous integration

The GitHub Actions workflow `.github/workflows/r-smoke.yml` runs on pushes and pull requests to `main` and checks:

1. smoke simulation;
2. synthetic RAID-style data generation;
3. testthat tests;
4. example structured update validation.

## Governance artifacts

- `registries/assumption_register.csv` tracks assumptions, status, decision state, and dependencies.
- `registries/claim_register.md` tracks claims, evidence status, and allowed manuscript use.
- `.github/ISSUE_TEMPLATE/decision_needed.yml` creates PI decision issues.
- `.github/ISSUE_TEMPLATE/proof_task.yml`, `simulation_task.yml`, and `empirical_task.yml` scope bounded autonomous tasks.
- `logs/research_updates/` stores machine-readable cycle reports.

## Required human approval

The loop must pause and request approval before:

- adding new theorem assumptions;
- adding or changing estimands;
- selecting the primary false-complex empirical model;
- making interpretive literature claims;
- making causal claims about RAID context effects;
- choosing exclusion thresholds after seeing results;
- deleting files or rewriting history;
- running expensive jobs;
- deciding or changing submission venue;
- exposing restricted RAID data.

Routine code edits, tests, theorem wording proposals, simulation parameter edits, subtask creation, and Git commits may be proposed automatically, but final merge remains human-controlled.

## Repository layout

```text
.
├── agents/                    # Agent role specifications
├── loops/                     # Loop operating procedures
├── schemas/                   # JSON schemas for structured agent outputs
├── registries/                # Assumption and claim registries
├── logs/research_updates/     # Machine-readable autonomous cycle reports
├── docs/                      # Design documents, model milestones, governance
├── data_synthetic/            # Synthetic, non-confidential RAID-style examples
├── R/                         # R simulation and analysis code
├── stan/                      # Stan model skeletons and final model code
├── tests/testthat/            # Unit tests
├── simulations/               # Design grid and run registry
├── manuscript/                # Manuscript and supplement skeleton
├── slurm/                     # Slurm templates
├── scripts/                   # Setup, validators, and runner scripts
├── src/loop_researcher/       # Optional Python API-based orchestrator
├── .github/workflows/         # CI smoke checks
└── Makefile
```
