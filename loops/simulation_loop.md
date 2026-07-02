# Simulation Loop

## Purpose

Demonstrate model misselection and downstream bias under approved DGM conditions.

## Steps

1. Simulation Architect proposes a design cell.
2. PI Agent checks whether it is within approved grid.
3. Code Engineer implements or updates code.
4. Code Engineer runs unit tests.
5. Reproducibility Auditor runs smoke simulation.
6. Reviewer 2 Agent checks whether the simulation supports the target claim.
7. Expensive runs require human approval.
8. Results are registered and summarized.

## Output files

- `simulations/design_grid.csv`
- `simulations/run_registry.csv`
- `results/`
- `manuscript/tables/`
- `manuscript/figures/`
