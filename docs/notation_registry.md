<!-- coherence-allow: F_Theta_given_Z, eta_model_index, bare_delta_ell, k_as_complexity -->
# OCECM Notation Registry

_Last updated: 2026-09-08_

This file is the **single binding source** for symbols used in the theorem
package. It exists because the proof route spans seven interdependent results
across `docs/`, `manuscript/`, and `formal/`, and single-pass drafting reliably
introduces silent notation drift.

`scripts/check_coherence.py` enforces this file. A symbol used in a theorem
document that is not registered here, or used in a sense this file forbids, is
a CI failure. Do not resolve such a failure by editing the theorem text alone;
either register the symbol here or use the registered one.

## 1. Indices and counts

| Symbol | Meaning | Notes |
|---|---|---|
| `i` | participant index | |
| `t` | trial index within participant | |
| `j` | generic observation index | a participant-trial pair |
| `n` | number of observations in the analysed sample | |
| `N` | number of participants | `n` and `N` are never interchangeable |
| `J` | number of distinct trial-design support points | |
| `K` | number of support points of the omitted-context cell variable | |

## 2. Random variables

| Symbol | Meaning |
|---|---|
| `Y` | observed choice outcome |
| `X` | observed trial features (design vector) |
| `Z` | observed participant covariates |
| `C` | **omitted** context |
| `U` | idiosyncratic latent heterogeneity |
| `\Theta` | latent decision parameter, `\Theta = h(Z, C, U)` |

## 3. Laws

| Symbol | Meaning | Binding rule |
|---|---|---|
| `p(y \mid x, \theta; \eta)` | conditional choice kernel | `\eta` is the **kernel** parameter, never a model index |
| `\eta^*` | true kernel parameter in the DGM | |
| `F_{\Theta \mid X,Z}` | regular conditional law of `\Theta` given `(X,Z)` | **primary** mixing law everywhere |
| `F_{\Theta \mid Z}` | conditional law of `\Theta` given `Z` alone | **corollary-only** (T-002). Forbidden in any primary statement. A-006 is rejected. |
| `p_0(y \mid x, z)` | omitted-context marginal law; the target of model comparison | |
| `Q` | design measure on `(X, Z)` | all design-averaged quantities are w.r.t. `Q` |

## 4. Model classes and their parameters

The previous drafts used `\eta` both for the kernel parameter and as the index
of the simple model class, and `\psi` for the complex model class. That clash
is resolved as follows and the old usage is forbidden.

| Symbol | Meaning |
|---|---|
| `M_S` | context-omitting **simple** model class |
| `M_K` | context-omitting **complex** ("false-complex") model class |
| `M_{S+C}` | context-**aware** simple model class (reference, empirical track) |
| `\beta_S \in B_S` | parameter indexing `M_S` |
| `\beta_K \in B_K` | parameter indexing `M_K` |
| `\beta_S^{\circ}, \beta_K^{\circ}` | **pseudo-true** (KL-minimising) parameters under `p_0` |
| `\hat\beta_S, \hat\beta_K` | estimates from the observed sample |
| `k_S, k_K` | **nominal** parameter counts; never an effective complexity |

Forbidden: `\eta \in M_S`, `\psi \in M_K`, `\eta` as any model index.

## 5. Scores, gaps, and criteria

The dominant source of error in the earlier drafts was conflating **population
expectations** with **realised sample quantities**, and **per-observation** with
**total** log score. Both distinctions are now carried by the notation itself.

| Symbol | Meaning | Kind |
|---|---|---|
| `\ell` | **per-observation** expected log score | population |
| `L` | **total** expected log score, `L = n\,\ell` | population |
| `\hat\ell_n` | per-observation realised log score | realised |
| `\hat L_n` | total realised maximised log-likelihood, `\hat L_n = n\,\hat\ell_n` | realised |
| `\Delta\ell^{*}` | population per-observation gap `\ell(M_K) - \ell(M_S)` at pseudo-true parameters | population |
| `D_n` | **realised** maximised log-likelihood difference `\hat L_n(M_K) - \hat L_n(M_S)` | realised |
| `\omega^2` | `\mathrm{Var}_{p_0}` of the pointwise log-score difference (Vuong variance) | population |

Binding rules:

1. A hat means realised on the observed sample. No hat means a population
   expectation under `p_0` and `Q`.
2. Lowercase `\ell` is per observation. Uppercase `L` is the total. Never write
   a threshold that mixes the two without the explicit factor `n`.
3. `D_n` and `\Delta\ell^{*}` are **different objects**. `D_n / n \to \Delta\ell^{*}`
   is a theorem (T-007b), not a definition, and it requires regularity that
   fails in the singular case (T-007c).

## 6. Divergences and predictive criteria

| Symbol | Meaning |
|---|---|
| `\mathrm{KL}_Q(p_0 \Vert p_\beta)` | design-averaged conditional Kullback-Leibler divergence |
| `G` | prespecified leave-out unit. **Bound to: a single trial** (approval 2026-09-08) |
| `\mathrm{elpd}^{G}_{M}` | expected log predictive density of model `M` for unit `G` |
| `\widehat{\mathrm{elpd}}^{G}_{M}` | its PSIS-LOO estimator |
| `\mathrm{LOOIC}(M)` | `-2\,\mathrm{elpd}^{G}_{M}` |
| `p_{\mathrm{loo}}` | effective number of parameters; the **only** admissible complexity measure for `M_K` |
| `\hat k` | Pareto shape diagnostic of PSIS |

## 7. Singular-learning quantities

Required because `M_K` is a mixture/random-effects family and is therefore a
**singular** statistical model (see `docs/theorems/T-007_finite_sample_selection.md`).

| Symbol | Meaning |
|---|---|
| `\lambda` | real log canonical threshold (RLCT). Replaces `k/2` in the free-energy expansion |
| `m` | multiplicity of the RLCT |
| `J(\beta)` | expected Hessian of the negative log-likelihood (the "sandwich" bread) |
| `V(\beta)` | expected outer product of the score (the "sandwich" meat) |
| `\mathrm{WBIC}` | Watanabe's widely applicable BIC, evaluated at inverse temperature `1/\log n` |

Binding rule: `k/2` may never be substituted for `\lambda` for `M_K`, and
`\mathrm{tr}(J^{-1}V)` may never be substituted by `k` when `p_0 \notin M`.

## 8. How to add a symbol

1. Add the row here, with its kind (population vs realised) if it is a score.
2. If it is a new modelling commitment, add an assumption row to
   `registries/assumption_register.csv` with `decision_status = decision_needed`.
3. Re-run `python3 scripts/check_coherence.py`.
