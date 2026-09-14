# Minimal Bayesian computation validation

Date: 2026-09-13. M2 complete at numerical-validation level. No external or formal verification. Protocol was written before pilot execution in `minimal_pilot_protocol.json`; all 60 dataset records and seeds are retained in `../logs/theory_checks/2026-09-13_minimal_bayes.json`.

## Computational checks

The implementation uses dependency-free Gauss–Legendre quadrature over the actual normalized uniform-theta and uniform-rho priors. Likelihoods use labeled responses, so no binomial combinatorial coefficient is introduced. Exact trial deletion reduces only the appropriate trial/outcome count by one. At most four distinct deletion fits are required because these homogeneous product likelihoods depend only on those counts. This shortcut is exact for this contract, not for a participant-effect model.

On a fixed six-participant dataset, direct posterior predictive integration after explicitly omitting each response agrees with the evidence-ratio prediction to below 2e-15 in log probability. Integrating K in delta coordinates with the prior Jacobian agrees with rho-coordinate log evidence and total ELPD to below 9e-15. This coordinate check preserves the same prior; it is not prior sensitivity. Empty-data prior integration checks normalization.

Every pilot dataset passed the predeclared 1e-5 agreement tolerance for log evidence and total ELPD under quadrature refinement. Largest final discrepancy: 3.81e-06. Datasets requiring order 192: 13/60. These are convergence diagnostics, not rigorous quadrature error bounds. No PSIS approximation or MCMC was used.

BIC optimization uses concavity in (theta,delta): a monotone score solves the theta profile, then a one-dimensional concave maximization includes both delta endpoints. The one/two parameter counts and participant n match the proof.

## All pilot preference counts

Each row has 10 independent replicates. Entries count K preferences; lower BIC/LOOIC and larger BF_KS favor K.

| DGP | Participants | BIC | BF | LOOIC |
|---|---:|---:|---:|---:|
| context | 50 | 0/10 | 1/10 | 2/10 |
| context | 200 | 1/10 | 3/10 | 4/10 |
| context | 1000 | 1/10 | 7/10 | 8/10 |
| null | 50 | 1/10 | 4/10 | 4/10 |
| null | 200 | 0/10 | 7/10 | 6/10 |
| null | 1000 | 0/10 | 3/10 | 1/10 |

The small positive population gap does not deliver uniform finite-sample preference. In particular the n=1000 contextual sample favors K often by BF/LOOIC but rarely by BIC in this small pilot. The null also exhibits finite-sample K wins, consistent with the theorem making no positive-gap preference claim there. A context-aware oracle remains correctly specified in the analytical control; this pilot compares S/K only and does not estimate a contextual model.

Ten replicates per cell are too few for precise rates. Plug-in binomial Monte Carlo standard errors are stored per cell and range up to about 0.158; values of zero at observed 0/10 or 10/10 do not mean certainty. For example a 95% Wilson interval for 0/10 is approximately [0,0.278]. These are simulation-replicate uncertainties, not standard errors treating dependent trial scores as iid.

No seeds, design, priors or sample sizes were changed after observing preference outcomes. The existing small asymptotic gap and this unfavorable BIC evidence must appear in the manuscript. No large-n grid or seed search is justified merely to obtain more wins.

## Next step

M3: write the concise manuscript from the reviewed direct proof, reporting the small gap, fixed shared constants, global parameter counts and distortion/offset equivalence. Include this full pilot table with its limitations. Preserve the context-aware and context-null theoretical controls; do not imply that the pilot establishes mechanistic identification or precise power.
