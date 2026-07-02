# Approval Policy

## May proceed without approval

Agents may propose or make local branch edits for:

- Code comments.
- Unit tests.
- Simulation parameters within the approved design grid.
- Theorem wording proposals that do not change substantive assumptions.
- Manuscript wording proposals that do not introduce new interpretive claims.
- Git commits on non-main branches.
- Sub-goals and sub-tasks.
- Small local smoke runs.

## Must pause for approval

Agents must request explicit human approval before:

- Adding or changing assumptions.
- Adding or changing estimands.
- Adding or changing big-picture goals.
- Making interpretive claims.
- Making literature claims.
- Deleting files.
- Running expensive jobs.
- Launching cluster jobs above configured thresholds.
- Submitting, posting, or disseminating scientific claims.
- Changing target journal strategy.

## Expensive job default threshold

A job is expensive by default if it exceeds any of the following:

- More than 250 Monte Carlo replications.
- More than 32 cores.
- More than 4 hours wall time.
- Any Slurm array with more than 20 array tasks.
- Any job expected to write more than 10 GB.

## Error policy

For coding failures:

1. Try to diagnose and fix.
2. Repeat for at most 10 attempts.
3. If still failing, write an error report.
4. Open a GitHub issue with logs, reproduction steps, and suspected causes.
5. Stop.

For proof failures:

1. Identify the exact unsupported step.
2. Try a counterexample search.
3. Downgrade theorem to conjecture if necessary.
4. Record the gap in the unproven-claims registry.
5. Stop if a new assumption would be needed.
