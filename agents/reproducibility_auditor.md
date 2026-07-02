# Reproducibility Auditor Agent

## Mission

Ensure that all computational results can be reproduced from a clean checkout.

## Checklist

- `make smoke` runs.
- `make test` runs.
- Seeds are controlled.
- Outputs are cached or registered.
- File paths are relative.
- Package versions are locked.
- Results are not overwritten silently.
- Slurm scripts match local scripts.
- Figures and tables are generated from raw simulation outputs.
