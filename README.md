# OCECM Autonomous Researcher Workbench

This repository is a research workbench for the project **Omitting Contextual Factors in Cognitive Models**.

## Current project thesis

When a contextual variable, such as socioeconomic resources or stressful life events, shapes a latent decision/cognitive parameter, omitting that contextual factor can change the observed choice pattern. The resulting residual structure can look like the result of a different, more complex cognitive model. A false complex model may therefore beat a simpler context-omitting model in model comparison, even when a simpler model that incorporates context is the better mechanistic explanation.

The planned paper combines:

1. a formal theorem package;
2. Monte Carlo and RAID-calibrated simulations, where RAID is an empirical dataset;
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
2. [`docs/approval_log.md`](docs/approval_log.md) — **binding decisions**; an agent may not reopen one.
3. [`docs/notation_registry.md`](docs/notation_registry.md) — the single binding source for symbols; enforced by CI.
4. [`docs/theorems/`](docs/theorems/) — precise statements for T-003 to T-007.
2. [`loops/autonomous_researcher_loop.md`](loops/autonomous_researcher_loop.md) — cycle protocol and human-decision gates.
3. [`agents/research_manager.md`](agents/research_manager.md) — research-manager role prompt.
4. [`docs/procedure_compliance.md`](docs/procedure_compliance.md) — required PR-body audit trail for autonomous cycles.
5. [`.github/pull_request_template.md`](.github/pull_request_template.md) — PR template with required procedure-compliance section.
6. [`registries/README.md`](registries/README.md) — registry governance rules.
7. [`registries/assumption_register.csv`](registries/assumption_register.csv) — assumption tracking.
8. [`registries/claim_register.md`](registries/claim_register.md) — claim/evidence tracking.
9. [`docs/raid_variable_coding_memo_template.md`](docs/raid_variable_coding_memo_template.md) — required audit before empirical RAID modeling.
10. [`docs/hierarchical_bayes_milestones.md`](docs/hierarchical_bayes_milestones.md) — staged plan from GLM proxies to Stan/brms models.
11. [`schemas/research_update.schema.json`](schemas/research_update.schema.json) — structured cycle-update format.
12. [`logs/research_updates/example_update.json`](logs/research_updates/example_update.json) — example machine-readable loop update.

## Formal proof route

Precise statements live in [`docs/theorems/`](docs/theorems/). Symbols are bound
by [`docs/notation_registry.md`](docs/notation_registry.md). Binding decisions
are in [`docs/approval_log.md`](docs/approval_log.md).

1. **T-001 omitted-context mixture representation**: integrating out context
   induces a marginal response law over `F_{Theta | X,Z}` (primary; the
   `F_{Theta | Z}` display is the T-002 corollary only).
2. **T-003 Gaussian constructive case**: omitted context induces a
   context-dependent latent mean and variance — and does so *if and only if*
   the context coefficient is non-zero and its conditional variance is
   non-constant.
3. **T-004 KL dominance**: conditions under which a flexible false model lies
   strictly closer to the omitted-context mixture than the restricted simple
   model. The mechanism is **variance** heterogeneity: mean shift alone is
   absorbed by the simple random-effects model (Proposition T-004d).
4. **T-005 predictive consequence**: the estimator-to-population bridge for
   trial-level LOO, whose implicit penalty is `p_loo`, not `k`.
5. **T-007 finite-sample thresholds**: split into exact algebra, a
   regular-case probabilistic bridge with a minimum-sample-size corollary, and
   a singular-case correction.

**T-006 (Bayes factors) is deferred and is not a theorem target** — see
[`docs/theorems/T-006_bayes_factor_deferred.md`](docs/theorems/T-006_bayes_factor_deferred.md).

**AIC/BIC are legacy diagnostics only.** `M_K` is a singular statistical model,
so their asymptotics are invalid here; PSIS-LOO and WAIC are the primary
criteria. See T-007c and decision D-004.

Boundary cases must always be stated: no context effect, harmless iid noise,
sufficient simple random-effect structure, lack of complex-model approximation
advantage, mismatched leave-out unit, or finite-sample penalty dominance.

## Verifying the theorem package

The proof route is guarded by three checks. Run them all with `make verify`.

| Check | Command | What it rejects |
|---|---|---|
| Cross-result coherence | `make check-coherence` | notation drift, assumption leaks across `depends_on`, dependency cycles, registry disagreements, Lean/doc status divergence |
| Numerical verification | `make theorem-numerics` | a stated theorem that is numerically false, including every registered boundary case |
| Lean typechecking | `make lean` | a formal statement that does not compile against mathlib |

The coherence checker is itself tested (`scripts/test_check_coherence.py`, run
first in CI): twelve fixtures assert that each rule actually rejects a violating
repository. A checker that never fails is worthless.

All three run in CI — `.github/workflows/coherence.yml`,
`.github/workflows/ci.yml`, and `.github/workflows/formal-lean.yml`.

## Simulation scaffold

The R scaffold implements a lightweight proxy DGM and model suite:

- `R/dgm.R`: simulates a simple context-aware ambiguity task in which SES shifts latent ambiguity aversion and its heterogeneity.
- `R/fit_models.R`: fits fast GLM proxies for simple omitted context, complex omitted context, and simple context-aware reference models.
- `R/model_selection.R`: computes AIC/BIC proxy comparisons and finite-sample log-likelihood threshold diagnostics; it does not calculate Bayesian criteria.
- `R/run_replication.R`: runs one theorem-aligned simulation replication.
- `R/run_design_cell.R`: runs a small grid cell and writes results.
- `R/generate_synthetic_raid_data.R`: generates public synthetic RAID-style trial and demographic files.

These GLM proxies are for smoke tests and fast screening only. They do not
produce valid Bayes factors or LOOIC, and their AIC/BIC output is a legacy
bridge diagnostic that may not be cited in support of C-004 (decision D-004). Final empirical models should use
hierarchical Bayesian structural models with PSIS-LOOIC, a declared-prior Bayes
factor sensitivity analysis, and held-out participant log score.

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

The GitHub Actions workflow `.github/workflows/pr-procedure-compliance.yml` runs on pull requests and verifies that the PR body exposes the required `## Procedure compliance` audit section.

## Governance artifacts

- `registries/assumption_register.csv` tracks assumptions, status, decision state, and dependencies.
- `registries/claim_register.md` tracks claims, evidence status, and allowed manuscript use.
- `.github/ISSUE_TEMPLATE/decision_needed.yml` creates PI decision issues.
- `.github/ISSUE_TEMPLATE/proof_task.yml`, `simulation_task.yml`, and `empirical_task.yml` scope bounded autonomous tasks.
- `.github/pull_request_template.md` requires a PR-body procedure-compliance checklist.
- `docs/procedure_compliance.md` explains how to use and review the compliance audit trail.
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
├── formal/                    # Lean 4 + mathlib formalization (gated by CI)
├── slurm/                     # Slurm templates
├── scripts/                   # Setup, validators, and runner scripts
├── src/loop_researcher/       # Optional Python API-based orchestrator
├── .github/workflows/         # CI and PR compliance checks
└── Makefile
```
