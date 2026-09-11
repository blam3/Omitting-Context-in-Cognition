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

**(P1) and (P2) are independent of T-004's hypotheses — they do not come for
free.** This is worth stating because §3 below argues that they *fail* for `M_K`,
and a reader may reasonably ask how T-004 can hold while they fail. The two are
consistent, as follows.

T-004's condition (i) is `p_0 \notin \bar M_S`. Its proof locates the `M_S`
minimiser in `\bar M_S = M_S \cup D` and does **not** place it in `M_S`. So even
under T-004's hypotheses there may be no pseudo-true parameter for `M_S` in the
parameter space at all — `T-004_kl_dominance.md` §3 exhibits a `p_0` for which
the minimiser sits in the degenerate family `D`, i.e. at `s = \infty`. (P1) is
therefore an assumption T-007b adds, not one it inherits.

For `M_K` the failure is different in kind and not repairable by assumption:
`M_K` is singular, so (P2) fails on a set of parameter values that includes the
pseudo-true point under boundary conditions 1–3. T-007b is stated for the
regular case precisely so that §3 can say what happens outside it.

Empirically both hold for the omitted-context mixture family this project
studies — the `M_S` minimiser is interior and unique across all cases in
`T-004_kl_dominance.md` §5 and a 58-configuration scan. That is evidence, not
proof, and it must be rechecked when the model family or design changes.

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

**`\omega` is not a free parameter in this regime — it is determined by
`\Delta\ell^{*}`.** The earlier draft of this corollary used `\omega \approx 1`
as a placeholder and quoted a crossover of `5.5\times10^{10}`. That was wrong by
about four orders of magnitude, and the error was structural rather than
arithmetic: `\omega` is the standard deviation of the *pointwise* log-likelihood
difference between two models whose KL gap is `\sim 10^{-6}`, so the two log
densities differ by `O(10^{-3})` pointwise and `\omega` inherits that scale. It
cannot be of order one.

**Lemma T-007b'' (`\omega^2 = 2\Delta\ell^{*}` under containment).** When
`p_0 \in M_K` (condition (ii) of T-004, so `\inf_{M_K}\mathrm{KL}_Q = 0`), the
pointwise log-score difference has

$$\omega^2 \; = \; 2\,\Delta\ell^{*} \, \big(1 + o(1)\big)$$

as the gap shrinks. This is the standard `\chi^2 \approx 2\,\mathrm{KL}`
relation between nearby laws. Numerically the ratio `\omega^2 / (2\Delta\ell^{*})`
stays within `10^{-3}` of `1` across a hundredfold range of effect sizes
(`0.9993` to `1.0003`). It requires containment: for `M_K^{\mathrm{flex}}`, which
does not contain `p_0`, the ratio is `0.58`.

**Corollary T-007b''' (the crossover is a fixed multiple of the deterministic
threshold).** Substituting `\omega = \sqrt{2\Delta\ell^{*}}` into T-007b' and
writing `u = \sqrt{n\,\Delta\ell^{*}}` turns the defining equation into

$$u^2 \;-\; z_{1-\alpha}\sqrt{2}\; u \;-\; (k_K - k_S) \;=\; 0,$$

which **does not involve the effect size at all**. Hence
`n^{*} = u_{*}^2 / \Delta\ell^{*}` with `u_{*}` a pure function of `\alpha` and
`k_K - k_S`:

| `\alpha` | `u_{*}` | crossover |
|---|---|---|
| `0.05` | `2.697` | `n^{*} = 7.27\,/\,\Delta\ell^{*}` |
| `0.10` | `2.256` | `n^{*} = 5.09\,/\,\Delta\ell^{*}` |
| `0.25` | `1.585` | `n^{*} = 2.51\,/\,\Delta\ell^{*}` |

So at `\alpha = 0.05` the probabilistic crossover is about **`7.3` times** the
deterministic threshold `1/\Delta\ell^{*}` — the same order of magnitude, not
five orders above it. Applied to the cases of `T-004_kl_dominance.md` §5:

| Case | `\Delta\ell^{*}` | `\omega` | deterministic `1/\Delta\ell^{*}` | probabilistic `n^{*}` |
|---|---|---|---|---|
| A mean + variance | `6.90\times10^{-6}` | `3.71\times10^{-3}` | `144{,}949` | `1{,}054{,}173` |
| B variance only | `1.07\times10^{-6}` | `1.47\times10^{-3}` | `931{,}099` | `6{,}771{,}638` |

**What survives of §0's Error 1.** The distinction is real and the correction
stands: the deterministic threshold is where the *expected* AIC difference
changes sign — a coin flip — while `n^{*}` is where AIC selects `M_K` with
probability `1-\alpha`. What does **not** survive is the claimed size of the
gap between them. It is a factor of about seven, not `10^5`. Quoting the
deterministic threshold as a detectability threshold overstates power by
roughly `7\times`, which is a real but modest error, and the earlier text
replaced it with a far larger one of its own.

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
Takeuchi's `2\,\mathrm{tr}(J^{-1}V)`. Correct specification gives `J = V` and
hence `\mathrm{tr}(J^{-1}V) = k`, recovering AIC. The converse does **not**
hold: `\mathrm{tr}(J^{-1}V) = k` is one scalar equation on `k^2` entries, so its
solution set is a hypersurface rather than the single point `J = V` — a random
search finds such pairs readily (75 in `2\times10^5` draws with
`\lVert J - V \rVert_F > 1`). The point for this project is one-directional and
unaffected: under misspecification one may not *assume* `\mathrm{tr}(J^{-1}V) = k`,
so AIC's `2k` is unjustified. When `J` is singular, `\mathrm{tr}(J^{-1}V)` does
not exist at all and no fixed-`k` correction is available.

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
| no pseudo-true parameter in `M_S` (minimiser in `D`, i.e. `s = \infty`) | (P1) fails; T-007b does not apply. Possible even under T-004's hypotheses — see §2 |
| `n` below the T-007b' crossover | penalties dominate; this is boundary condition 5, now quantitative |

## 5. Numerical verification

`tests/testthat/test-theorem-numerics.R`, cases `T-007a`, `T-007b-2`, `T-007b-3`
and `T-007b`.

**What is checked.**

1. The T-007a identities, symbolically, on 400 random `(D_n, k_S, k_K, n)`.
2. Lemma T-007b'': `\omega` lies in `(10^{-4}, 10^{-2})` — emphatically not near
   `1` — and `\omega^2 / (2\Delta\ell^{*}) = 1` to `10^{-3}` for both containment
   cases.
3. Corollary T-007b''': the multiplier is `7.27` and is invariant across four
   orders of magnitude of effect size, and the two quoted `n^{*}` figures
   reproduce.
4. **The T-007b selection probability against simulated data.** Data are
   generated from the T-004 construction, `M_S` and `M_K^{\mathrm{flex}}` are
   fitted by maximum likelihood, and the realised
   `P(\mathrm{AIC} \text{ selects } M_K)` is compared with
   `\Phi\big((n\Delta\ell^{*} - \Delta k)/(\sqrt{n}\,\omega)\big)`:

| `n` | replicates | simulated | T-007b formula | difference |
|---|---|---|---|---|
| `2000` | 400 | `0.200` | `0.121` | `0.079` (about 4 s.e.) |
| `8000` | 400 | `0.585` | `0.573` | `0.013` (under 1 s.e.) |
| `20000` | 300 | `0.880` | `0.861` | `0.019` (about 1 s.e.) |
| `50000` | 250 | `1.000` | `0.987` | `0.013` (about 1 s.e.) |

The formula is confirmed for `n \ge 8000`, where `n\Delta\ell^{*} \gtrsim 1`. At
`n = 2000` (`n\Delta\ell^{*} = 0.30`) it is about four standard errors low. That
is the expected pre-asymptotic regime for **nested** models: `M_S \subset M_K`,
so `D_n \ge 0` identically and `D_n` carries an `O(1)` chi-bar-squared
contribution from the extra parameter, on top of the `O(n\Delta\ell^{*})` and
`O(\sqrt{n}\,\omega)` terms T-007b models. The normal approximation omits it, and
it is negligible only once `n\Delta\ell^{*} \gg 1`. **The T-007b' crossover should
therefore not be read as accurate below itself** — which is precisely where a
project tempted to cite it would want to use it.

**A note on how this was checked.** The first attempt fitted `M_K` from an
independent start and produced `\mathbb{E}[2D_n] = 0.32` against a `\chi^2_1`
target of `1`, because the optimiser under-fitted the larger model; that run
suggested a spurious finding, which was withdrawn. Seeding `M_K` at the fitted
`M_S` with `\beta_2 = 0` makes `D_n \ge 0` hold by nesting and removes the
artefact. The regression test uses the seeded form and asserts `D_n \ge 0` in
every replicate, so the failure mode cannot silently return.

**Earlier claim, now corrected.** This section previously asserted that the test
suite checked the crossover formula against a Monte Carlo estimate of
`P(\mathrm{AIC} \text{ selects } M_K)`. It did not — the only check performed was
that the formula solved its own defining quadratic. The simulation described
above was written in proof-critic review (2026-09-11) to make the claim true.
