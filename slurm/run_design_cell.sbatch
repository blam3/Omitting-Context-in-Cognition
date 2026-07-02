#!/bin/bash
#SBATCH --job-name=embedded_cognition_sim
#SBATCH --output=logs/slurm_%A_%a.out
#SBATCH --error=logs/slurm_%A_%a.err
#SBATCH --time=04:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --array=1-60

# Bouchet/YCRC template.
# Review resource requirements before submitting.
# Expensive jobs require human approval per docs/approval_policy.md.

module purge

mkdir -p logs results

GRID="simulations/design_grid.csv"
ROW=$(awk -v row=$((SLURM_ARRAY_TASK_ID+1)) 'NR==row {print}' $GRID)

IFS=',' read -r N TRIALS CONTEXT_RANGE CONTEXT_EFFECT REPLICATIONS <<< "$ROW"

Rscript R/run_design_cell.R \
  --n "$N" \
  --trials "$TRIALS" \
  --context_range "$CONTEXT_RANGE" \
  --context_effect "$CONTEXT_EFFECT" \
  --replications "$REPLICATIONS" \
  --seed "$((20260630 + SLURM_ARRAY_TASK_ID * 100000))"
