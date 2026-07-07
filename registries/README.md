# Project Registries

The autonomous researcher must use these registries to keep scientific commitments explicit and reviewable.

## Registry purposes

| Registry | Purpose | Update trigger |
|---|---|---|
| `assumption_register.csv` | Tracks theorem, simulation, and empirical assumptions | Any time an assumption is added, removed, narrowed, or strengthened |
| `claim_register.md` | Tracks manuscript-level claims and their evidence status | Any time a claim is drafted, promoted, weakened, or cited |
| `simulations/run_registry.csv` | Tracks simulation runs and output locations | Any time a simulation job writes results |
| `logs/research_updates/` | Stores structured cycle reports | Every autonomous researcher cycle |

## Governance rules

1. New assumptions require a decision gate unless they are purely bookkeeping assumptions already implied by an approved theorem statement.
2. No claim should move to the manuscript as a main-text claim until its evidence status is at least `supported_preliminary`.
3. Every causal claim requires explicit PI approval and an evidence note explaining the identification strategy.
4. Claims based only on proxy GLM smoke tests must be marked `scaffold_only`.
5. Claims about real RAID data must not include confidential values or participant-level information.

## Status values

Suggested evidence statuses:

- `scaffold_only`
- `planned`
- `in_progress`
- `supported_preliminary`
- `supported_final`
- `unsupported`
- `rejected`
- `decision_needed`

## Decision values

Suggested decision values:

- `approved_default`
- `pi_approved`
- `decision_needed`
- `deferred`
- `rejected`
