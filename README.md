# Autonomous Loop Researcher Starter

This repository scaffold is designed for a bounded-autonomy research workbench for a project on contextual omission in cognitive computational models.

## Project thesis

When an exogenous contextual variable, such as socioeconomic background, causally influences a cognitive parameter, omitting that contextual factor can make a more complex but false cognitive model appear preferable to the simpler true model. The planned study combines human-readable mathematical proof, selective formal verification, Bayesian model comparison, LOO-based comparison, and Monte Carlo simulation.

## Intended use

This is not a free-running agent swarm. It is a controlled research workbench with:

1. Manager-led orchestration.
2. Specialized research agents.
3. Explicit approval gates.
4. Reproducible simulation scripts.
5. Proof-review logs.
6. Claim and citation registries.
7. GitHub issue and pull-request workflows.
8. Local plus cluster execution.

## Recommended first week

1. Create a public GitHub repository.
2. Copy this scaffold into the repository.
3. Add a real `renv.lock` by running `renv::init()` in R.
4. Add an OpenAI API key locally in `.env`, never in GitHub.
5. Convert the placeholder model functions in `R/` into the first real ambiguity-attitude model.
6. Run `make smoke`.
7. Create three GitHub issues:
   - Formalize the minimal theorem.
   - Implement the one-parameter true contextual model.
   - Implement the omitted-context one- and two-parameter comparison models.

## Repository layout

```text
.
├── agents/                    # Agent role specifications
├── loops/                     # Loop operating procedures
├── schemas/                   # JSON schemas for structured agent outputs
├── docs/                      # Design documents and governance
├── R/                         # R simulation and analysis code
├── tests/testthat/            # Unit tests
├── simulations/               # Design grid and run registry
├── manuscript/                # Manuscript and supplement skeleton
├── slurm/                     # Bouchet/YCRC Slurm templates
├── scripts/                   # Setup and runner scripts
├── src/loop_researcher/       # Optional Python API-based orchestrator
├── .github/workflows/         # CI smoke checks
└── Makefile
```

## Required human approval

The loop must pause and request approval before:

- Adding new assumptions.
- Adding or changing estimands.
- Making interpretive claims.
- Making literature claims.
- Deleting files.
- Running expensive jobs.
- Deciding submission venue.

Routine code edits, unit tests, theorem wording proposals, simulation parameter edits, subtask creation, and Git commits may be proposed automatically, but final merge remains human-controlled.
