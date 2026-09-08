<!-- theorem-meta
id: T-007
title: Finite-sample selection thresholds, corrected for misspecification and singularity
claim: C-004
status: proof-draft
assumptions: A-001, A-002, A-003, A-007, A-008, A-009, A-011
depends_on: T-004
approval: D-004, D-006
-->

<!-- coherence-allow: bare_delta_ell -->

# T-007 — Finite-Sample Selection Thresholds

Status: `proof-draft`. Split into three parts by D-004 (2026-09-08); the
inherited T-004 assumptions were approved by D-006 (2026-09-09). Not accepted:
proof-critic review is outstanding, and T-007c is a policy rather than a
theorem. Notation is bound by
`docs/notation_registry.md`.

## 0. Two errors in the previous statement

The prior formulation read:

> AIC-like selection favors the complex model when `2 n \Delta\ell > 2(k_K - k_S)`;
> BIC-like selection favors it when `2 n \Delta\ell > (k_K - k_S)\log n`.

**Error 1 — expected and realised quantities are conflated.** `\Delta\ell` is a
population per-observation gap evaluated at pseudo-true parameters. AIC and BIC
are computed from the *realised* maximised log-likelihoods on the observed
sample. The two differ by a random term of order `n^{-1/2}` per observation,
i.e. `O_p(\sqrt n)` in total — the same order as the AIC penalty for moderate
`n`. Writing a deterministic threshold in `\Delta\ell` states as certain
something that is a probability tending to one, and gives no guidance at the
sample sizes the project actually has.

**Error 2 — the penalties are invalid for `M_K`.** `2k` and `(k/2)\log n` are
derived under correct specification and a non-singular Fisher information at an
interior maximum. Neither holds here: `p_0 \notin M_S` and `p_0 \notin M_K` by
construction, and `M_K` is a mixture / random-effects family, hence a
**singular** model. See §3.

The corrected result is three separate statements with three different
epistemic statuses.

## 1. T-007a — Exact algebra (a definition, not a theorem)

Let `\hat L_n(M) = n\,\hat\ell_n(M)` be the realised maximised log-likelihood and

$$D_n \ :=\ \hat L_n(M_K) - \hat L_n(M_S)$$

the realised log-likelihood difference. Then, identically and with no
assumptions whatsoever,

$$\mathrm{AIC}(M_S) - \mathrm{AIC}(M_K) > 0 \iff D_n > k_K - k_S,$$
$$\mathrm{BIC}(M_S) - \mathrm{BIC}(M_K) > 0 \iff D_n > \tfrac{1}{2}(k_K - k_S)\log n .$$

This is a rearrangement of the definitions of AIC and BIC. It is stated here so
that the manuscript never again presents it as a result, and so that the symbol
`D_n` (realised) is visibly distinct from `\Delta\ell^{*}` (population).

## 2. T-007b — The bridge, in the regular case only

**Theorem T-007b.** Assume the conditions of T-004, so `\Delta\ell^{*} > 0`, and
assume in addition:

- **(P1)** each model has a unique pseudo-true parameter `\beta^{\circ}` in the
  **interior** of its parameter space;
- **(P2)** the Fisher information `J(\beta^{\circ})` is non-singular for both
  models;
- **(P3)** `\omega^2 = \mathrm{Var}_{p_0}\big( \log p_{\beta_K^{\circ}}(Y \mid X)
  - \log p_{\beta_S^{\circ}}(Y \mid X) \big) > 0`;
- **(P4)** standard M-estimation regularity (dominating envelopes, Donsker class).

Then

$$\frac{D_n}{n} \ \xrightarrow{\ p\ } \ \Delta\ell^{*}, \qquad
\sqrt{n}\left( \frac{D_n}{n} - \Delta\ell^{*} \right) \Rightarrow N(0, \omega^2),$$

and therefore

$$P\big(\mathrm{AIC} \text{ selects } M_K\big)
= \Phi\!\left( \frac{n\Delta\ell^{*} - (k_K - k_S)}{\sqrt{n}\,\omega} \right) + o(1),
\qquad
P\big(\mathrm{BIC} \text{ selects } M_K\big)
= \Phi\!\left( \frac{n\Delta\ell^{*} - \tfrac{1}{2}(k_K-k_S)\log n}{\sqrt{n}\,\omega} \right) + o(1).$$

Both tend to `1`, since `\log n = o(n)`.

**Proof.** `\hat\ell_n(M) \to_p \ell(\beta^{\circ}_M)` and the corresponding CLT
follow from (P1)–(P4) by the standard theory for misspecified maximum
likelihood (White; Vuong). Substituting into T-007a's exact equivalences and
applying the continuous mapping theorem gives the displays. `\square`

**Corollary T-007b' (minimum sample size).** The smallest `n` at which AIC
favours `M_K` with probability at least `1-\alpha` solves

$$n\,\Delta\ell^{*} \ -\ z_{1-\alpha}\,\sqrt{n}\,\omega \ -\ (k_K - k_S) \ =\ 0,$$

a quadratic in `\sqrt{n}`. This — not the deterministic threshold — is the
quantity the simulation arm must report, and it is what makes the project's
boundary condition 5 ("penalties dominate in the finite sample") quantitative
rather than rhetorical.

**The two thresholds differ by five orders of magnitude, and that difference is
the whole content of §0's Error 1.** With `\Delta\ell^{*} \approx 7\times10^{-6}`
from T-004 §6, `k_K - k_S = 1`, `\omega \approx 1` and `\alpha = 0.05`:

| Threshold | Formula | Value |
|---|---|---|
| deterministic, as previously stated | `n > (k_K-k_S)/\Delta\ell^{*}` | `n \approx 1.4\times10^{5}` |
| probabilistic, T-007b' | `n\Delta\ell^{*} - z_{0.95}\sqrt{n}\,\omega - (k_K-k_S) = 0` | `n \approx 5.5\times10^{10}` |

The deterministic threshold is the sample size at which the *expected* AIC
difference changes sign — a coin flip. The T-007b' value is the sample size at
which AIC selects `M_K` with 95% probability. Quoting the first as if it were
the second overstates detectability by a factor of roughly `4\times10^{5}`. The
`\omega \approx 1` used here is a placeholder; the simulation arm must estimate
`\omega` rather than assume it, and the crossover scales with `\omega^2`.

## 3. T-007c — The singular case, which is the actual case

(P1) and (P2) **fail for `M_K`.** This is not a technicality; it is the generic
situation for the models this project compares.

`M_K^{\mathrm{mix}}` is a finite mixture and `M_K^{\mathrm{flex}}` has a variance
parameter constrained to `s^2 \ge 0`. At a parameter value where a mixture
component has weight zero, or two components coincide, or a variance is zero,
the parameter is not locally identifiable and the Fisher information matrix
degenerates. These are exactly the parameter values that matter here: under the
project's boundary conditions 1–3 the pseudo-true parameter of `M_K` **is** such
a point, because `p_0` then lies in the `M_S` submodel embedded in `M_K`.

Consequences, each of which changes what the project may report.

**(a) BIC is invalid and biased against `M_K`.** The `(k/2)\log n` penalty comes
from a Laplace approximation to the marginal likelihood requiring a
non-degenerate Hessian. For singular models the correct asymptotic free-energy
expansion is Watanabe's,

$$-\log Z_n \ =\ n\,\hat\ell_n \ +\ \lambda \log n \ -\ (m-1)\log\log n \ +\ O_p(1),$$

where `\lambda` is the real log canonical threshold and `m` its multiplicity,
with `\lambda \le k/2` and the inequality typically strict for mixture and
hierarchical models. BIC therefore **over-penalises `M_K`**. It follows that a
BIC result favouring `M_S` is not evidence against C-004, and D-004 prohibits
citing BIC in support of C-004 in either direction. Where a BIC-like quantity is
wanted, WBIC (evaluated at inverse temperature `1/\log n`) is the admissible
substitute, because it estimates the free energy without assuming regularity.

**(b) AIC's `2k` correction is invalid under misspecification, and the
misspecification-robust replacement is itself invalid under singularity.** Under
misspecification with non-singular `J`, the correct bias correction is
Takeuchi's `2\,\mathrm{tr}(J^{-1}V)`, which equals `2k` only when
`J = V` (correct specification). When `J` is singular, `\mathrm{tr}(J^{-1}V)`
does not exist and no fixed-`k` correction is available.

**(c) No significance reading of `D_n`.** Since `M_S \subset M_K`, one might
reach for a likelihood-ratio test. Its null reference is **not**
`\chi^2_{k_K - k_S}`: with the pseudo-true parameter on the boundary of the
parameter space, the limiting null distribution is a mixture of chi-squares
(Chernoff; Self and Liang), and for mixture models with non-identified nuisance
parameters it can be non-standard altogether. No `p`-value on `D_n` may be
reported.

**(d) Nominal parameter counts are not complexity.** `k_S` and `k_K` may not be
reported as the complexity of the comparison. Report `p_{\mathrm{loo}}` or
`p_{\mathrm{waic}}`, which are estimated from the data and remain meaningful
under singularity (T-005b).

**Adopted policy (D-004).** PSIS-LOO / WAIC are the primary finite-sample
criteria, because they remain asymptotically equivalent to the Bayes
generalisation error for singular models. AIC and BIC are retained only as
legacy bridge diagnostics maintaining continuity with the fast GLM scaffold, are
labelled as such in `R/model_selection.R`, and may not be cited in support of
C-004.

## 4. Boundary conditions

| Condition | Effect on T-007 |
|---|---|
| `\Delta\ell^{*} = 0` (T-004 boundary conditions 1–4) | `D_n = O_p(1)`; AIC/BIC both favour `M_S` eventually; no crossover exists |
| `\omega^2 = 0` | the CLT in T-007b degenerates; `D_n` has a chi-squared-type limit and T-007b' does not apply |
| pseudo-true parameter on the boundary | T-007b does not apply at all; only T-007c governs |
| `n` below the T-007b' crossover | penalties dominate; this is boundary condition 5, now quantitative |

## 5. Numerical verification

`tests/testthat/test-theorem-numerics.R`, case `T-007`, checks the T-007a
identities symbolically on random inputs, and checks the T-007b' crossover
formula against a Monte Carlo estimate of `P(\mathrm{AIC} \text{ selects } M_K)`
on simulated samples from the T-004 construction.
