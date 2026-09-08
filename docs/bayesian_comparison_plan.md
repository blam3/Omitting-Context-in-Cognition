# Bayesian comparison plan

Updated 2026-09-08 under delegated PI authority for prior families, scales and the evidence estimator. Primary predictive criterion: trial-level LOO. See pi_decisions_2026-09-08.md for the exact target.

## Model-family contract

M1 is context-omitting structural ambiguity; M2 adds context to its latent mean; M3 additionally allows context-dependent dispersion. M4 is the PI-selected probability-distortion model without context; M5 adds the same context specification. Shared baseline value, side and domain terms must match across candidates. Do not equate M4 with the existing quadratic/source GLM proxy.

A concrete proposed M4 parameterization is one-parameter weighting

    w(p; rho) = exp(-(-log(p))^rho), rho > 0,
    w(0; rho)=0, w(1; rho)=1, w(p;1)=p.

This is the functional form introduced by [Prelec (1998)](https://nelmit.wordpress.com/wp-content/uploads/2016/10/26probabilitycopy.pdf); allowing rho>1 is an explicit modeling extension of the paper's highlighted 0<rho<1 case. Use log(rho) as the working parameter. The family is selected; this precise form is a modeling proposal until the task-level equation is reviewed. In particular, specify whether weighting precedes ambiguity adjustment, which lottery probabilities enter each value, and how losses are represented. Do not pass a negative ambiguity-adjusted quantity into w or silently clip it. The single-level Stan skeleton is not yet a validated gain/loss two-lottery implementation.

## Proper weakly informative defaults selected by the LLM

The following are project defaults, not literature-derived universal scales. They apply on the stated working scales and must pass prior predictive checks before final comparison. Use identical priors for shared parameters across models. Fixed scale sensitivity is 0.5x, 1x and 2x the listed standard deviations, retaining centers and supports; show all results rather than choosing the scale that favors M4.

| Parameter / working scale | Default prior |
|---|---|
| Choice intercept, if present | Normal(0, 1.5) |
| Centered side and gain/loss coefficients | Normal(0, 1) |
| Population mean of unconstrained ambiguity parameter theta | Normal(0, 1) |
| Context slopes a1 and gamma, on standardized continuous predictors | Normal(0, 0.5) |
| Participant residual SD on theta scale | Half-Normal(0, 1) |
| Population mean of log choice sensitivity tau | Normal(0, 1) |
| Participant SD of log(tau) | Half-Normal(0, 0.5) |
| Population mean of log probability-distortion rho | Normal(0, 0.5) |
| Participant SD of log(rho), if included | Half-Normal(0, 0.5) |
| Log-dispersion intercept / context slopes, if M3 included | Normal(0, 1) / Normal(0, 0.5) |

All Normal entries give mean and SD. Half-Normal densities must include their normalization. Use fixed task-design units for monetary values (declare the conversion before outcomes are examined), probabilities/ambiguity on 0–1, and documented context centering/scaling. The tau prior presumes a dimensionless utility difference of order one; define that scale before fitting. Without those transformations the numerical priors are not ready for raw RAID data. If theta must be constrained, specify a link and its Jacobian where needed; an unconstrained Gaussian theta cannot be silently treated as positive ambiguity aversion. Correlations and additional cognitive parameters are outside this initial independent-effects specification and need a stated prior if introduced.

For future compact constructive proofs, a convenient proper weak prior is independent Normal(0,1) truncated to the explicitly specified parameter boxes, with all normalization constants retained. On a fixed compact box the density is bounded above and bounded away from zero, making it a tractable candidate for evidence bounds. This does not by itself prove a BF result: likelihood concentration and the KL gap still need proof. The existing benchmark keeps its original normalized Uniform[-1,1] priors to preserve reviewed dependencies. Its result is not automatically a result for the new priors or models.

## Marginal likelihood and numerical estimator

The theoretical object is m_M(D)=integral L_M(D|phi) pi_M(phi) dphi, with all latent variables/global parameters integrated under a proper normalized prior. Prove statements about that integral directly; no numerical estimator is required to define the theorem.

Select bridge sampling for structural/hierarchical computation. Validate against deterministic quadrature for low-dimensional cases; retain normalizing constants and transformation Jacobians, including in Stan log-density evaluation. Repeat the bridge calculation and posterior fits, report log-evidence uncertainty/stability, and compare approximation error with the between-model log-BF difference. Failed or unstable estimates are missing evidence, not model-selection wins. BIC or harmonic-mean output is not an automatic fallback.

Bridge sampling has been developed and demonstrated for cognitive and hierarchical models; the ordinary harmonic-mean estimator can have infinite variance. These motivate the numerical choice, not a guarantee of accuracy for this project. See the [bridge-sampling tutorial](https://www.maths.bris.ac.uk/R/web/packages/bridgesampling/vignettes/bridgesampling_tutorial.pdf) and [package methods paper](https://www.jstatsoft.org/article/view/v092i10).

BF uses the complete data evidence; changing LOO's holdout unit does not turn BF into a trial-deletion criterion. Bayes factors remain prior-sensitive secondary evidence alongside primary trial-LOO. Model prior odds are unnecessary for a BF; specify them separately if posterior model probabilities are reported.

## Simulation contract and exit checks

1. Specify a context-aware simple DGP with rho=1, and M4 with free rho but no context. Specify which latent parameter context changes. Establish identifiability before attributing apparent distortion to omission.
2. Include correct-model parameter recovery; context-null with residual heterogeneity; a separate fixed-parameter representable null; and a true-distortion positive control. Match baseline terms and model flexibility fairly.
3. Freeze cells, seeds, priors and exclusion rules before runs. Estimate selection proportions with Monte Carlo intervals, signed bias, RMSE and coverage only for parameters with a meaningful truth correspondence. Do not confuse mean absolute error with absolute bias.
4. Validate conditional per-trial log likelihood and exact single-trial refits first. Validate PSIS against those refits and assess participant-clustered uncertainty. Optional LOPO results stay separately labeled.
5. Report predictive preferences as preferences; in simulation mechanistic truth is known by construction, but a RAID M4 win is not proof of true probability distortion. Context can change predictions without yielding a universal direction or magnitude of selection.
6. Run only bounded local checks within the existing compute policy until a production budget is approved. No outcome is established by this planning document.

## Comparison questions — retained from the pre-2026-09-08 plan

| Question | Contrast | Estimand | Selection direction |
|---|---|---|---|
| Can omitted context make false complexity predict better? | `M4` versus `M1`; then `M4` versus `M2/M3` | Expected leave-out log predictive density and LOOIC | Higher ELPD / lower LOOIC |
| Can omitted context make false complexity receive more Bayesian model evidence? | Same contrasts under the declared candidate models | `log BF_{K,S}` | Positive log Bayes factor |

The first contrast demonstrates misselection pressure; the second tests whether
the context-aware explanation remains preferable once context is modeled. The
estimand column states the original LOOIC framing; under the 2026-09-08
decision the primary predictive estimand is trial-level LOO.

## Reporting contract — retained from the pre-2026-09-08 plan

For each simulated data set, preserve the common DGM and candidate-model
definitions across all criteria. Fit only Bayesian models with proper priors.
Store posterior log likelihood at the unit needed for the declared LOO target
and record the marginal-likelihood method used for each Bayes factor. Report:

- ELPD and LOOIC differences, selection rates, and type I/type II error;
- Pareto-k summaries, the number of unreliable units, and any refit or exact
  fallback;
- log Bayes factors, selection rates, and the full prior-scale sensitivity
  grid;
- held-out participant log score as a robustness check;
- AIC/BIC only as a labelled proxy bridge from the GLM scaffold.

The current GLM proxy simulation is not permitted to emit Bayes factors or
LOOIC. Its role is limited to DGM screening and AIC/BIC continuity until the
hierarchical Bayesian model path is implemented.

## Resolved decision gate — primary leave-out unit

The pre-2026-09-08 plan left the primary LOO target open and recommended
leave-one-participant-out, on the reasoning that the scientific question
concerns generalization to new people rather than another trial from an
already-observed participant.

**The PI resolved this gate on 2026-09-08 in the opposite direction:**
trial-level LOO is the primary predictive target, conditioned on the person's
remaining responses, and whole-participant LOPO is a separately labelled
secondary target. See `docs/pi_decisions_2026-09-08.md`. The earlier
recommendation is recorded here only so the reversal is auditable; it is not
current guidance.

The requirement it carried does still stand: the first Bayes-factor
implementation must separately document its proper prior families,
prior-scale sensitivity grid, and marginal-likelihood estimator.

The pre-2026-09-08 six-step theorem route is recorded in
`docs/theorem_backlog.md` under the superseded planned route.
