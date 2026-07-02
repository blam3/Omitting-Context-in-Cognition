#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install openai python-dotenv

Rscript -e "if (!requireNamespace('renv', quietly = TRUE)) install.packages('renv')"
Rscript -e "if (!requireNamespace('testthat', quietly = TRUE)) install.packages('testthat')"

echo "Local setup complete."
