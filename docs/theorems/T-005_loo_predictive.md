<!-- theorem-meta
id: T-005
title: LOO predictive-score consequence at the trial level
claim: C-004
status: statement-draft
assumptions: A-001, A-002, A-003, A-007, A-008, A-009, A-010, A-011
depends_on: T-004
approval: D-002, D-004, D-006
-->

# T-005 — From the Population Gap to LOOIC

Status: `statement-draft`. Leave-out unit bound to the **trial** by D-002
(2026-09-08); the T-004 assumptions it inherits were approved by D-006
(2026-09-09).

**This result is deliberately NOT advanced to `proof-draft` alongside T-003,
T-004 and T-007** (D-006 condition 3). Its central statement T-005b is a proof
*sketch*: the leave-one-out expansion is quoted, not derived. Promoting it
requires writing that derivation out or replacing it with an explicit citation.
Notation is bound by `docs/notation_registry.md`.

## 0. Why the previous statement was not a theorem

The prior formulation read: if `\Delta_{\mathrm{LOO}} > 0` then the complex model
has lower LOOIC, *because* `\mathrm{LOOIC}(M) = -2\,\mathrm{elpd}_{\mathrm{LOO}}(M)`.

That is arithmetic. `\mathrm{LOOIC}` is a monotone decreasing affine function of
`\mathrm{elpd}`, so an `\mathrm{elpd}` ordering *is* a `\mathrm{LOOIC}` ordering,
by definition. Nothing about omitted context, cognitive models, or model
selection is involved.

The statement also silently identified three different objects:

1. the **population** predictive gap for the declared leave-out unit;
2. the **estimator** `\widehat{\mathrm{elpd}}` computed by PSIS-LOO from one sample;
3. the **population log-score gap at pseudo-true parameters**, `\Delta\ell^{*}`,
   which is what T-004 actually delivers.

These differ by an `O(1)` effective-complexity term and an `O_p(\sqrt n)`
sampling term. The content of T-005 is the relationship between them.

## 1. Objects

Under A-010, the leave-out unit `G` is **one trial**, and the predictive target
is a new trial from a participant already represented in the sample, with that
participant's remaining trials in the conditioning set.

$$\mathrm{elpd}^{G}_{M} \ :=\ \sum_{j=1}^{n} \mathbb{E}_{\tilde y_j}\big[
\log p_M(\tilde y_j \mid x_j, y_{-j}) \big], \qquad
\mathrm{LOOIC}(M) := -2\,\mathrm{elpd}^{G}_{M},$$

estimated by `\widehat{\mathrm{elpd}}^{G}_{M} = \sum_j \log \hat p_M(y_j \mid y_{-j})`
with the leave-one-out predictive densities obtained by Pareto-smoothed
importance sampling.

## 2. The definitional part, labelled as such

**Remark T-005a.** `\mathrm{LOOIC}(M_K) < \mathrm{LOOIC}(M_S)` if and only if
`\mathrm{elpd}^{G}_{M_K} > \mathrm{elpd}^{G}_{M_S}`. This is a change of scale and
sign, not a result. It may appear in the manuscript only as a reporting
convention.

## 3. The estimator-to-population bridge

This is the substantive statement.

**Theorem T-005b.** Assume R1–R6 of §4, and assume `\Delta\ell^{*} > 0` from
T-004. Then

$$\widehat{\mathrm{elpd}}^{G}_{M_K} - \widehat{\mathrm{elpd}}^{G}_{M_S}
\ =\ n\,\Delta\ell^{*} \ -\ \big(p_{\mathrm{loo}}(M_K) - p_{\mathrm{loo}}(M_S)\big)
\ +\ O_p(\sqrt{n}),$$

where, writing
`\widehat{\mathrm{lpd}}(M) = \sum_j \log p_M(y_j \mid y_{1:n})` for the in-sample
log pointwise predictive density,
`p_{\mathrm{loo}}(M) = \widehat{\mathrm{lpd}}(M) - \widehat{\mathrm{elpd}}^{G}_{M}`
is the effective number of parameters. (`\widehat{\mathrm{lpd}}` is the Bayesian
posterior predictive quantity, not the maximised log-likelihood
`n\,\hat\ell_n`; the two differ by `O_p(1)`, which is the same order as
`p_{\mathrm{loo}}` itself and so may not be conflated.) Consequently

$$P\big( \mathrm{LOOIC}(M_K) < \mathrm{LOOIC}(M_S) \big) \ \longrightarrow\ 1 .$$

**Proof sketch.** The leave-one-out predictive density admits the expansion
`\log p_M(y_j \mid y_{-j}) = \log p_M(y_j \mid y_{1:n}) - c_j + o_p(1/n)` with
`\sum_j c_j \to p_{\mathrm{loo}}(M)`; summing over `j` gives
`\widehat{\mathrm{elpd}}^{G}_{M} = \widehat{\mathrm{lpd}}(M) - p_{\mathrm{loo}}(M) + o_p(1)`,
and `\widehat{\mathrm{lpd}}(M) = n\,\hat\ell_n(M) + O_p(1)`.
Differencing the two models and applying the law of large numbers to
`\hat\ell_n(M_K) - \hat\ell_n(M_S) \to_p \Delta\ell^{*}` (valid under R2–R3)
gives the display. The penalty difference is `O_p(1)` while `n\Delta\ell^{*}`
diverges, so the sign is eventually determined by `\Delta\ell^{*} > 0`.
`\square`

Two consequences worth stating explicitly in the manuscript.

**The implicit penalty is `p_{\mathrm{loo}}`, not `k`.** T-005b has the same shape
as an AIC comparison, but with the *effective* complexity in place of the
nominal parameter count. This is precisely why LOO survives the singularity of
`M_K` (§4, R2) and AIC/BIC do not: `p_{\mathrm{loo}}` is estimated from the data
rather than assumed equal to `k_K`. Reporting `k_K - k_S` as the complexity of
the comparison is prohibited by D-004.

**Corollary T-005c (finite-`n` ordering with uncertainty).** Let
`\delta_j := \log \hat p_{M_K}(y_j \mid y_{-j}) - \log \hat p_{M_S}(y_j \mid y_{-j})`
and `\omega^2 := \mathrm{Var}_{p_0}(\delta)`. Under R5,

$$P\big(\mathrm{LOOIC}(M_K) < \mathrm{LOOIC}(M_S)\big)
\ =\ \Phi\!\left( \frac{n\,\Delta\ell^{*} - \Delta p_{\mathrm{loo}}}{\sqrt{n}\,\omega} \right) + o(1),$$

so the smallest `n` at which the complex model is favoured with probability
`1-\alpha` solves `n\Delta\ell^{*} - z_{1-\alpha}\sqrt{n}\,\omega - \Delta p_{\mathrm{loo}} = 0`,
a quadratic in `\sqrt{n}`. With the magnitudes measured in T-004 §6
(`\Delta\ell^{*} \sim 10^{-6}`), this is the calculation that decides whether the
phenomenon is visible at RAID scale, and it must be reported.

## 4. Regularity conditions

These are the conditions the previous draft did not state. Each is a real
restriction and none may be silently waived.

**R1 (declared unit and exchangeability).** `G` is a single trial, fixed before
fitting per D-002. Trials are conditionally exchangeable within participant
given the participant's latent parameters.

**R2 (posterior concentration under misspecification).** `p_0 \notin M_S` and
generally `p_0 \notin M_K`, so ordinary Bernstein–von Mises does not apply. For
models with a unique interior pseudo-true parameter and non-singular Fisher
information, use the misspecified BvM of Kleijn and van der Vaart, under which
the posterior concentrates at `\beta^{\circ}` with the sandwich covariance
`J^{-1}VJ^{-1}`. **For `M_K` this is not available**: mixture and random-effects
models are singular, the information matrix degenerates where a component is
empty or a variance is zero, and the pseudo-true parameter may sit on that
boundary. In the singular case the required substitute is Watanabe's singular
learning theory, under which PSIS-LOO and WAIC remain asymptotically equivalent
to the Bayes generalisation error. This is the technical reason LOO is the
project's primary criterion and AIC/BIC are not (D-004).

**R3 (moments).** `\mathbb{E}_{p_0}|\log p_M(Y \mid X, \beta)|^{2+\epsilon} < \infty`
in a neighbourhood of the pseudo-true parameter, uniformly, so the LLN and CLT
used in T-005b and T-005c apply.

**R4 (PSIS validity — a diagnostic, not an assumption).** The importance-sampling
approximation to `p(y_j \mid y_{-j})` is valid only where the Pareto shape
estimate satisfies `\hat k < 0.7`. Folds failing this must be refit exactly or
moved to K-fold. Reporting LOOIC without the `\hat k` distribution is
prohibited.

**R5 (non-degenerate Vuong variance).** `\omega^2 > 0`, i.e. the two models are
distinguishable at their pseudo-true parameters. **This fails exactly under the
project's boundary conditions 1–3**, where `p_0 \in \bar M_S \subset M_K` and the
models are nested with the smaller one adequate; there the difference is
`O_p(1)` with a chi-squared-type limit and the normal approximation in T-005c is
invalid. The simulation arm must therefore report `\hat\omega` and not apply
T-005c when it is near zero.

**R6 (inherited from T-004).** `\Delta\ell^{*} > 0` requires the conditions of
T-004, including non-representability. Boundary conditions 1–4 of T-004 transfer
here unchanged: when they hold, `\Delta\ell^{*} = 0` and T-005b gives no
ordering.

## 5. Hazards specific to the trial-level unit

D-002 bound `G` to the trial. Three consequences follow that the manuscript must
carry.

1. **Directional optimism toward `M_K`.** With trial-level leave-out, the
   participant's own remaining trials still inform that participant's latent
   parameters, so models with more participant-level or trial-level flexibility
   are advantaged. That is the same direction as the paper's claimed effect. A
   trial-level advantage for `M_K` is therefore *not* by itself evidence for
   C-001.
2. **Nested-model standard errors are anticonservative.** `M_S \subset M_K` by
   A-009. The usual `\sqrt{n}\,\mathrm{sd}(\delta_j)` standard error of the elpd
   difference understates uncertainty for nested models, so the common
   `\Delta\mathrm{elpd}/\mathrm{se} > 2` rule is not admissible here. Report the
   difference with its standard error *and* the caveat, and prefer the
   T-005c calculation with an explicitly reported `\hat\omega`.
3. **Participant-level K-fold is mandatory** (D-002, condition 3). It answers the
   different question — generalisation to a new participant — and it is the
   analysis that discriminates a genuine mechanism from a leave-out artefact. It
   must be reported whether or not it agrees with the primary result.

## 6. What this result does not establish

- It does not show that the trial-level advantage generalises to new
  participants. By construction it cannot; that is what §5.3 is for.
- It does not license any Bayes-factor conclusion. Model evidence is a different
  estimand and T-006 has been demoted (see
  `docs/theorems/T-006_bayes_factor_deferred.md`).
- It does not license AIC/BIC statements. See T-007.
