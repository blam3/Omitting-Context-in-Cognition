# Claim Registry

Claims must be tagged by status.

## Status labels

- `conjecture`: plausible but unproven.
- `proved`: proof reviewed and accepted.
- `simulation-supported`: supported by simulation results.
- `literature-supported`: supported by verified citation.
- `uncertain`: should not appear in manuscript as a claim.
- `rejected`: found false or misleading.

## Claim template

```text
ID:
Claim:
Type: mathematical | simulation | literature | interpretation
Status:
Evidence:
Citations:
Used in manuscript section:
Needs approval: yes | no
Reviewer-2 concerns:
```

## Initial claim

```text
ID: C-0001
Claim: Omitting a contextual variable that causally influences a cognitive parameter may lead model-selection criteria to prefer a more complex omitted-context model over a simpler omitted-context model.
Type: mathematical/simulation/interpretation
Status: conjecture
Evidence: project premise; requires proof and simulation.
Citations: pending
Used in manuscript section: Introduction, Theory
Needs approval: yes
Reviewer-2 concerns: Need to specify conditions under which this occurs; cannot be universal without assumptions.
```
