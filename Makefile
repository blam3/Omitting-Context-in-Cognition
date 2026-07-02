.PHONY: setup smoke test simulate-small manuscript clean

setup:
	Rscript -e "if (!requireNamespace('renv', quietly = TRUE)) install.packages('renv'); renv::restore(prompt = FALSE)"

smoke:
	Rscript R/run_smoke_simulation.R

test:
	Rscript -e "if (!requireNamespace('testthat', quietly = TRUE)) install.packages('testthat'); testthat::test_dir('tests/testthat')"

simulate-small:
	Rscript R/run_design_cell.R --n 40 --trials 40 --context_range unrestricted --context_effect weak --replications 10 --seed 20260630

manuscript:
	cd manuscript && latexmk -pdf main.tex

clean:
	rm -rf results cache logs tmp manuscript/*.aux manuscript/*.bbl manuscript/*.blg manuscript/*.fdb_latexmk manuscript/*.fls manuscript/*.out
