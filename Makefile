.PHONY: setup smoke test simulate-small synthetic-raid validate-update manuscript clean check-coherence theorem-numerics lean verify

setup:
	Rscript -e "if (!requireNamespace('renv', quietly = TRUE)) install.packages('renv'); renv::restore(prompt = FALSE)"

smoke:
	Rscript R/run_smoke_simulation.R

test:
	Rscript -e "if (!requireNamespace('testthat', quietly = TRUE)) install.packages('testthat'); testthat::test_dir('tests/testthat')"

simulate-small:
	Rscript R/run_design_cell.R --n 40 --trials 40 --context_range unrestricted --context_effect weak --replications 10 --seed 20260630

synthetic-raid:
	Rscript R/generate_synthetic_raid_data.R --participants 12 --trials 20 --seed 20260704 --out_dir data_synthetic

validate-update:
	python3 scripts/validate_research_update.py logs/research_updates/example_update.json schemas/research_update.schema.json

manuscript:
	cd manuscript && latexmk -pdf main.tex

clean:
	rm -rf results cache logs/tmp tmp manuscript/*.aux manuscript/*.bbl manuscript/*.blg manuscript/*.fdb_latexmk manuscript/*.fls manuscript/*.out

check-coherence:
	python3 scripts/test_check_coherence.py
	python3 scripts/check_coherence.py

theorem-numerics:
	Rscript -e "if (!requireNamespace('testthat', quietly = TRUE)) install.packages('testthat'); testthat::test_file('tests/testthat/test-theorem-numerics.R', stop_on_failure = TRUE)"

lean:
	cd formal && lake exe cache get && lake build

# Everything that can reject a wrong proof, in the order it should be run.
verify: check-coherence theorem-numerics lean
