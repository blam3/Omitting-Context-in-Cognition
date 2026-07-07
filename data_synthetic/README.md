# Synthetic RAID-Style Data

This directory is reserved for public, non-confidential synthetic data that mimic the **schema** of the RAID trial-level files without reproducing any participant data.

## Generate synthetic data

```bash
make synthetic-raid
```

This writes:

- `data_synthetic/raid_trial_synthetic.csv`
- `data_synthetic/raid_demographics_synthetic.csv`

The generator uses `R/generate_synthetic_raid_data.R`, which calls the public simulation DGM in `R/dgm.R` and then maps simulated variables onto RAID-like column names.

## Intended use

Synthetic data are for:

1. testing cleaning and modeling code;
2. running CI without confidential data;
3. demonstrating variable transformations;
4. building public examples and tutorials.

Synthetic data are **not** evidence about the real RAID sample and must not be used for empirical claims.

## Confidentiality rule

Do not commit real RAID data, participant-level summaries, or outputs that could reveal confidential values. Use this directory only for generated public examples.
