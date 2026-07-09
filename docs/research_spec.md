# Research Specification

## Domain

Latent variable modeling, cognitive modeling, and causal inference.

## Core claim

When an exogenous contextual variable causally influences a cognitive parameter in a computational cognitive model, but that contextual variable is omitted, a more complex cognitive model may be selected over the simpler true model with the contextual factor. The more complex model can absorb otherwise unexplained contextual heterogeneity, but it is not the true model and can induce biased estimates, incorrect model selection, and false inferences.

## Target asymptotic property

Show that, under specific conditions, even as sample size and behavioral-task length increase, the more complex omitted-context model may be selected over the simpler omitted-context model, even though the actual data-generating process is a simpler contextual model.

## Applied problem

Decision-making under ambiguity. The motivating concern is that cognitive-model development can overfit unmodeled contextual heterogeneity, such as socioeconomic background, by adding cognitive parameters rather than embedding cognitive parameters in their causal and environmental context.

## Intended contribution

A conceptual formalization and bias-demonstration paper advocating an embedded cognition framework for computational cognitive modeling.

## Simulation grid

- Sample sizes: 40, 100, 250, 500, 1000
- Monte Carlo replications: 1000
- Trial lengths: 40, 100, 200
- Contextual-variable distribution: unrestricted vs range-restricted
- Context effect: weak vs strong
- Bayesian design factors:
  - primary leave-out unit: participant versus trial (PI decision gate);
  - proper prior scale for each candidate model;
  - marginal-likelihood estimator and its numerical diagnostics.
- Primary outcomes:
  - LOO expected-log-predictive-density and LOOIC differences for `M4` versus `M1` and `M2/M3`;
  - LOOIC selection accuracy plus type I and type II error under the declared leave-out target;
  - Pareto-k reliability rates and fallback-method use;
  - log Bayes-factor differences plus selection accuracy and type I/type II error;
  - Bayes-factor sensitivity across the predeclared prior-scale grid.
- Secondary outcomes:
  - held-out participant log score;
  - AIC/BIC proxy comparisons for theorem/scaffold continuity;
  - absolute bias, relative bias, RMSE, and coverage.

## Planned artifacts

- Manuscript `.tex`
- Proof supplement
- Simulation code
- Figures
- Tables
- GitHub repository
- OSF repository
- Preprint
