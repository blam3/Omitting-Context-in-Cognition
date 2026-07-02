# Reproducibility Loop

## Purpose

Ensure one-command reproduction and archive readiness.

## Steps

1. Reproducibility Auditor runs `make smoke`.
2. Reproducibility Auditor runs `make test`.
3. Reproducibility Auditor checks dependency lock files.
4. Reproducibility Auditor checks result provenance.
5. Code Engineer fixes failures.
6. After 10 failed repairs, open issue and stop.

## Output files

- CI logs
- `logs/error_reports/`
- `simulations/run_registry.csv`
