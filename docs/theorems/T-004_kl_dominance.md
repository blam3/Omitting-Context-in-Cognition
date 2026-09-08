<!-- theorem-meta
id: T-004
title: KL dominance of the false complex model under omitted context
claim: C-004
status: proof-draft
assumptions: A-001, A-002, A-003, A-007, A-008, A-009
depends_on: T-001, T-003
approval: D-001, D-006
-->

<!-- coherence-allow: eta_model_index -->

# T-004 — When Does the KL Inequality Actually Hold?

Status: `proof-draft`. **Not accepted.** A-007, A-008 and A-009 were approved by
D-006 (2026-09-09), so the statement is no longer decision-blocked, but
proof-critic review is outstanding and nothing here may enter
`manuscript/supplement_proofs.tex` until it completes. Notation is bound by
`docs/notation_registry.md`.

**Scope (D-006).** A-007 fixes a probit kernel — the attenuation identity is
exact for probit and only approximate for logit. A-008 fixes a finite,
non-negative design with `J \ge 4` levels including `a = 0`. A-009 fixes explicit
parametric families for `M_S` and `M_K`. Results below transfer to other kernels,
designs or model families only by re-checking Lemma T-004a and the containment
or score condition. This is a constructive theorem, not a general one.

## 0. Why the previous statement was not a theorem

The prior formulation (`docs/current_project_context.md`, Result 3) read:

> If `\inf_{M_K} \mathrm{KL}(p_0 \Vert p) < \inf_{M_S} \mathrm{KL}(p_0 \Vert p)`,
> then the false complex model has higher asymptotic expected log likelihood
> than the context-omitting simple model.

This is not a theorem. Because
`\mathrm{KL}_Q(p_0 \Vert p_\beta) = -\mathbb{E}[\log p_\beta(Y \mid X)] + \mathbb{E}[\log p_0(Y \mid X)]`
and the second term does not depend on `\beta`, the hypothesis and the
conclusion are the same proposition written twice. It is recorded below as
Corollary T-004e, where it belongs.

The question the project needs answered is the one the old statement assumed:
**under what conditions on the omitted context does that inequality hold?**
This document states and proves that.

## 1. Setup

Assume A-001, A-002, A-003 (so T-003 applies), plus:

**A-007 (probit kernel, approved D-006).** The trial design reduces to a scalar ambiguity level
`A \in \mathcal{A}`, and

$$P(Y = 1 \mid A = a, \Theta = \theta) = \Phi(b_0 + \theta a).$$

**A-008 (finite support, design richness, approved D-006).**
`\mathcal{A} = \{a_1, \ldots, a_J\} \subset [0, \infty)` with `J \ge 4` distinct
levels including `a_1 = 0`, and design measure `Q` with `q_j > 0`.
Non-negativity is not cosmetic: it is used in Lemma T-004b, where a signed
design would make the degenerate limit `\rho\,\mathrm{sign}(a)` rather than a
constant. Ambiguity levels are non-negative by construction, so this costs
nothing here. `Z` has finite support `\{z_1, \ldots, z_K\}` with `\pi_k > 0`. `A`
is exogenous in the sense of T-002.

**A-009 (model classes, approved D-006).** Both candidate models omit context, i.e. neither uses
`Z` or `C`:

$$M_S = \Big\{\, a \mapsto \Phi\big( (\beta_0 + \beta_1 a) / \sqrt{1 + s^2 a^2} \big)
\ :\ \beta_0, \beta_1 \in \mathbb{R},\ s^2 \ge 0 \,\Big\}, \qquad k_S = 3,$$

the simple ambiguity model with a Gaussian random ambiguity sensitivity, and
either

$$M_K^{\mathrm{mix}} = \Big\{\, a \mapsto \sum_{l=1}^{L} w_l \,
\Phi\big( (\beta_{0l} + \beta_{1l} a)/\sqrt{1 + s_l^2 a^2} \big) \,\Big\},
\quad L \ge K, \qquad
M_K^{\mathrm{flex}} = \Big\{\, a \mapsto
\Phi\big( (\beta_0 + \beta_1 a + \beta_2 a^2)/\sqrt{1 + s^2 a^2} \big) \,\Big\}.$$

`M_K^{\mathrm{mix}}` is the latent-class / mixture-of-strategies model;
`M_K^{\mathrm{flex}}` is the nonlinear-ambiguity model. Both are standard
false-complex candidates in the cognitive-modelling literature, and both
contain `M_S` as a submodel.

By T-003 and T-003b, the target of model comparison is

$$p_0(a) \ =\ \sum_{k=1}^{K} \pi_k \,
\Phi\!\left( \frac{b_0 + \mu_k a}{\sqrt{1 + \sigma_k^2 a^2}} \right),
\qquad \mu_k = \mu(z_k),\ \ \sigma_k^2 = \sigma_u^2 + \gamma^2 v(z_k),$$

and the criterion is the design-averaged conditional divergence
`\mathrm{KL}_Q(p_0 \Vert p_\beta) = \sum_j q_j \, d\big(p_0(a_j) \,\Vert\, p_\beta(a_j)\big)`
with `d` the Bernoulli KL.

## 2. A decidable membership criterion for the simple model

Everything turns on whether `p_0` is inside `M_S`. That is an
infinite-dimensional question; the following lemma reduces it to a
one-dimensional search, and makes it checkable in finite arithmetic on `J`
points.

**Lemma T-004a (membership criterion).** Let `p : \mathcal{A} \to (0,1)` and set
`g(a) := \Phi^{-1}(p(a))`. Then

$$p \in M_S \iff \exists\, s^2 \ge 0 \ \text{such that} \
a \mapsto g(a)\sqrt{1 + s^2 a^2} \ \text{is affine on } \mathcal{A}.$$

**Proof.** (`\Rightarrow`) If `p \in M_S` with parameters `(\beta_0, \beta_1, s^2)`
then `g(a) = (\beta_0 + \beta_1 a)/\sqrt{1+s^2a^2}`, so
`g(a)\sqrt{1+s^2a^2} = \beta_0 + \beta_1 a`, which is affine.
(`\Leftarrow`) If `g(a)\sqrt{1+s^2a^2} = \beta_0 + \beta_1 a` on `\mathcal{A}`
for some `s^2 \ge 0`, then `p(a) = \Phi\big((\beta_0+\beta_1 a)/\sqrt{1+s^2a^2}\big)`,
so `p \in M_S`. `\Phi` is a bijection `\mathbb{R} \to (0,1)`, so `g` is
well-defined throughout. `\square`

Because `M_S` has three free parameters and `\mathcal{A}` has `J \ge 4` points,
affineness after rescaling is an over-determined system: membership is
non-generic, and failure is detectable.

**Lemma T-004b (the closure, and why it is needed).** `M_S` is not closed in
`(0,1)^{J}`. Its closure adds exactly the degenerate limits obtained as
`s \to \infty` with `\beta_1 / s \to \rho`:

$$\bar{M}_S \setminus M_S \ = \ \big\{\, p \ :\ \Phi^{-1}(p(0)) = c_0 \ \text{arbitrary},\
\Phi^{-1}(p(a)) = \rho \ \text{for all } a \in \mathcal{A}\setminus\{0\} \,\big\}.$$

**Proof.** Fix a sequence `\beta^{(n)} = (\beta_0^{(n)}, \beta_1^{(n)}, s_n^2)`
with `p_{\beta^{(n)}} \to p^{\infty} \in (0,1)^J`, so
`g_n(a) := (\beta_0^{(n)} + \beta_1^{(n)}a)/\sqrt{1+s_n^2a^2}` converges
pointwise on `\mathcal{A}` to a finite limit. Passing to a subsequence, assume
`s_n \to s \in [0, \infty]`; this is no loss, because every subsequential limit
of `p_{\beta^{(n)}}` must equal `p^{\infty}`. Evaluating at `a = 0` (which lies
in `\mathcal{A}` by A-008) gives `\beta_0^{(n)} \to c_0` finite. If
`s_n \to s < \infty`, then evaluating at any `a \ne 0` forces
`\beta_1^{(n)}` to converge, and the limit lies in `M_S`. If `s_n \to \infty`,
then for `a \ne 0`,

$$g_n(a) = \frac{\beta_0^{(n)} + \beta_1^{(n)} a}{s_n |a| \sqrt{1 + s_n^{-2}a^{-2}}} .$$

The `\beta_0^{(n)}` term contributes `O(1/s_n) \to 0`. The remaining term is
`(\beta_1^{(n)}/s_n) \cdot a/|a|`, which by A-008 (`a > 0`) is
`\beta_1^{(n)}/s_n`. Along a further subsequence `\beta_1^{(n)}/s_n` converges in
`[-\infty, +\infty]`; a divergent limit would contradict finiteness of
`g^{\infty}(a)`, so it converges to some `\rho \in \mathbb{R}` — the same value
for every `a > 0`.

For the reverse inclusion, any such `p` is attained: take
`\beta_0^{(n)} = c_0`, `s_n = n` and `\beta_1^{(n)} = \rho n`, so that
`g_n(0) = c_0` for every `n` and `g_n(a) \to \rho` for each `a > 0`. `\square`

**Corollary T-004c (decidable criterion for the closure).**
`p \in \bar{M}_S` if and only if either

- (a) `\exists s^2 \ge 0` with `a \mapsto \Phi^{-1}(p(a))\sqrt{1+s^2a^2}` affine
  on `\mathcal{A}`; or
- (b) `\Phi^{-1}(p(a))` is constant over `a \in \mathcal{A} \setminus \{0\}`.

Both branches are decidable by a one-dimensional search plus a finite equality
check.

## 3. Main result

**Theorem T-004 (strict KL dominance).** Assume A-001, A-002, A-003, A-007,
A-008, A-009. Suppose

- **(i) non-representability:** `p_0 \notin \bar{M}_S`; and
- **(ii) containment:** `p_0 \in M_K`.

Then

$$\inf_{\beta_K \in B_K} \mathrm{KL}_Q(p_0 \Vert p_{\beta_K}) \ = \ 0 \ < \
\inf_{\beta_S \in B_S} \mathrm{KL}_Q(p_0 \Vert p_{\beta_S}).$$

**Proof.** The left equality is immediate from (ii), since `\mathrm{KL}_Q \ge 0`
with equality when the laws agree `Q`-a.e.

For the right inequality, write `c := \inf_{\beta_S} \mathrm{KL}_Q(p_0 \Vert p_{\beta_S})`.
Taking `\beta_S = (0,0,0)` gives `p_{\beta_S} \equiv \Phi(0) = 1/2` and a finite
divergence, so `c < \infty`. Let `\beta^{(n)}` be a minimising sequence and let
`p^{(n)} \in (0,1)^J` be the induced probability vectors. By compactness of
`[0,1]^J`, pass to a subsequence with `p^{(n)} \to p^{\infty} \in [0,1]^J`.

Since `p_0(a_j) \in (0,1)` for every `j` and `q_j > 0`, the Bernoulli divergence
`d(p_0(a_j) \Vert \cdot)` diverges to `+\infty` at `0` and `1`; as `c < \infty`,
no coordinate of `p^{\infty}` can be `0` or `1`. Hence `p^{\infty} \in (0,1)^J`,
`\mathrm{KL}_Q(p_0 \Vert \cdot)` is continuous there, and
`\mathrm{KL}_Q(p_0 \Vert p^{\infty}) = c`. By construction
`p^{\infty} \in \bar{M}_S`, so by (i) `p^{\infty} \ne p_0`, and therefore
`c = \mathrm{KL}_Q(p_0 \Vert p^{\infty}) > 0` by strict positivity of the
Bernoulli divergence between distinct probability vectors. `\square`

The proof is short because the work was moved into Lemma T-004b: the only
subtlety is that `M_S` is not closed, and a naive argument that infers
`\inf > 0` from pointwise positivity is wrong.

**Theorem T-004' (strict improvement without containment).** Drop (ii) and
assume instead that `M_S \subset M_K` with `M_K` parameterised as
`(\beta_S, \beta_2)` with `\beta_2 = 0` recovering `M_S`, that
`\beta_S^{\circ}` attaining `\inf_{\bar M_S}` is unique and interior, and that
the extra direction has non-vanishing score at that point:

$$\left. \frac{\partial}{\partial \beta_2}\,
\mathrm{KL}_Q\big(p_0 \,\big\Vert\, p_{(\beta_S, \beta_2)}\big)
\right|_{(\beta_S^{\circ},\, 0)} \ \ne \ 0 .$$

Then `\inf_{M_K} \mathrm{KL}_Q < \inf_{M_S} \mathrm{KL}_Q` strictly.

**Proof.** A non-zero first derivative at an interior point means `\beta_2` can be
moved in the descending direction to strictly decrease the objective; the value
at `(\beta_S^{\circ}, 0)` equals `\inf_{M_S}`. `\square`

This is the version that applies to `M_K^{\mathrm{flex}}`, which does not contain
`p_0`. The score condition is a computable integral, not an assumption about the
conclusion.

## 4. Exactly when the inequality fails — the sharp boundary result

Condition (i) is where the omitted context enters, and it resolves more sharply
than the project's prose has assumed. The distinction that matters is **mean
heterogeneity versus variance heterogeneity**, and only the second is
load-bearing.

**Proposition T-004d (mean heterogeneity alone is absorbed).** Suppose the
induced latent variance is constant, `\sigma^2(z) \equiv \sigma^2` — by
Corollary T-003a this happens exactly when `\gamma = 0` or `v(\cdot)` is
constant — and suppose the induced latent mean `\mu(Z)` is Gaussian,
`\mu(Z) \sim N(\bar\mu, \omega^2)`. Then

$$p_0(a) \ =\ \mathbb{E}_{\mu}\!\left[ \Phi\!\left( \frac{b_0 + \mu a}{\sqrt{1+\sigma^2a^2}} \right) \right]
\ =\ \Phi\!\left( \frac{b_0 + \bar\mu a}{\sqrt{1 + (\sigma^2 + \omega^2)a^2}} \right)
\ \in\ M_S ,$$

so **both** infima are zero and there is no KL gap whatsoever.

**Proof.** Apply `\mathbb{E}[\Phi(\alpha + \beta W)] = \Phi(\alpha/\sqrt{1+\beta^2})`
with `\alpha = (b_0 + \bar\mu a)/\sqrt{1+\sigma^2a^2}` and
`\beta = \omega a / \sqrt{1+\sigma^2a^2}`, then simplify the radical. The result
is a member of `M_S` with `\beta_0 = b_0`, `\beta_1 = \bar\mu`, and
`s^2 = \sigma^2 + \omega^2`. `\square`

The interpretation is worth stating plainly in the manuscript: **omitting a
context variable that shifts only the mean of the latent parameter is harmless
to model selection**, because the simple random-effects model absorbs it into
its own latent variance. What the simple model cannot absorb is *heterogeneity
in the latent variance itself*, because `M_S` has one `s^2` and the induced law
is a mixture over several. This is the precise content of the paper's thesis,
and it is narrower and more defensible than "omitting context favours complex
models".

Mapping onto the project's registered boundary conditions:

| Boundary condition | Exact status under T-004 |
|---|---|
| 1. `C` has no effect on `\Theta` (`\gamma = 0`) | `\sigma^2(\cdot)` constant by T-003a; gap `= 0` exactly under T-004d |
| 2. `C` adds only correctly modelled iid noise (`v` constant) | same; absorbed into `s^2` |
| 3. simple model already has sufficient random-effect structure | this *is* `p_0 \in \bar M_S`, i.e. the negation of (i) |
| 4. complex model has no approximation advantage | negation of (ii) / of the score condition in T-004' |
| 5. finite-sample penalties dominate | **not addressed here.** T-004 is a population statement with no finite-sample content; see T-007 |

## 5. Numerical verification

`tests/testthat/test-theorem-numerics.R`, case `T-004`. Design
`\mathcal{A} = \{0, 0.25, 0.5, 0.75, 1\}`, uniform `Q`, `b_0 = 0.3`, two context
cells with `\pi = (0.5, 0.5)`. Cross-checked in Python at higher restart counts:

| Case | `(\mu_k)` | `(\sigma_k^2)` | `\inf_{M_S}\mathrm{KL}` | `\inf_{M_K^{\mathrm{flex}}}` | `\inf_{M_K^{\mathrm{mix}}}` | affine residual |
|---|---|---|---|---|---|---|
| A mean + variance heterogeneity | `(0.6, 1.8)` | `(0.2, 2.5)` | `6.90\times10^{-6}` | `1.27\times10^{-7}` | `0` (`-4\times10^{-17}`) | `1.85\times10^{-4}` |
| B variance heterogeneity only | `(1.2, 1.2)` | `(0.2, 2.5)` | `1.07\times10^{-6}` | `1.85\times10^{-7}` | `0` (`-4\times10^{-17}`) | `2.64\times10^{-5}` |
| C mean heterogeneity only (discrete `Z`) | `(0.6, 1.8)` | `(0.8, 0.8)` | `9.97\times10^{-9}` | `1.51\times10^{-9}` | `0` (`-5\times10^{-17}`) | `2.68\times10^{-7}` |
| D **boundary**: homogeneous | `(1.2, 1.2)` | `(0.8, 0.8)` | `0` (`-6\times10^{-17}`) | `0` | `0` | `1.06\times10^{-14}` |
| E `\gamma = 0`, Gaussian mean heterogeneity | Gaussian | constant | `0` (`-7\times10^{-17}`) | — | — | `0` |
| F variance heterogeneity, Gaussian `Z` | Gaussian | non-constant | `9.58\times10^{-7}` | — | — | `>0` |

Case E confirms Proposition T-004d against its closed form to
`1.1\times10^{-16}`, i.e. to machine precision. Cases B and F confirm that
variance heterogeneity alone suffices for a strict gap. Case D is the registered
boundary condition and returns exact zeros in every column, as it must. The
affine-residual column is the Lemma T-004a certificate: it is zero exactly when
`p_0 \in M_S`.

Case C deserves comment because it refines Proposition T-004d. With **discrete**
`Z`, mean heterogeneity alone leaves a strictly positive but negligible gap
(`10^{-8}`, three orders of magnitude below case A); with **Gaussian** `Z`
(case E) it is exactly zero. So the sharp statement is: mean heterogeneity is
exactly absorbed when the induced mean is Gaussian and approximately absorbed
otherwise, while variance heterogeneity is not absorbed in either case. The
manuscript should state the Gaussian version as the clean result and case C as
the numerical indication that the conclusion is not an artefact of Gaussianity.

## 6. Effect size — a caveat that must reach the manuscript

The gaps above are per-observation divergences of order `10^{-6}`. That number,
not the sign of the inequality, governs whether the phenomenon is detectable.
Carried into T-007, a gap `\Delta\ell^{*} \approx 7 \times 10^{-6}` with
`k_K - k_S = 1` puts the *deterministic* AIC threshold at
`n \approx 1.4 \times 10^{5}` trials — and once sampling variability is included,
the sample size at which AIC actually selects `M_K` with 95% probability is
`n \approx 5.5 \times 10^{10}` (T-007b'). Realistic RAID-scale designs are many
orders of magnitude smaller than either.

This does not weaken T-004, which is a statement about the population limit. It
does mean the paper must not present the asymptotic result as a claim about what
happens at realistic `n`. The honest framing is that context omission creates a
systematic, direction-specific pressure toward false complexity whose
finite-sample expression depends on the magnitude of the induced variance
heterogeneity — and the simulation arm exists to map that magnitude. The harness
therefore scans `\Delta\ell^{*}` against the heterogeneity ratio
`\max_k \sigma_k^2 / \min_k \sigma_k^2` rather than reporting a single value.

## 7. Corollary that used to be the theorem

**Corollary T-004e (asymptotic expected log score).** Under the conditions of
T-004 or T-004',

$$\Delta\ell^{*} \ :=\ \sup_{\beta_K} \ell(\beta_K) - \sup_{\beta_S} \ell(\beta_S)
\ = \ \inf_{\beta_S} \mathrm{KL}_Q(p_0 \Vert p_{\beta_S})
- \inf_{\beta_K} \mathrm{KL}_Q(p_0 \Vert p_{\beta_K}) \ > \ 0 .$$

**Proof.** `\mathrm{KL}_Q(p_0 \Vert p_\beta) = -\ell(\beta) + \mathbb{E}[\log p_0(Y \mid A)]`,
and the additive term is free of `\beta`. `\square`

This is a restatement, not a further result, and it must be labelled as such in
the manuscript. It carries **no** finite-sample content: `\Delta\ell^{*}` is a
population quantity at the pseudo-true parameters, and the realised
log-likelihood difference `D_n` is a different object. Conflating the two is the
error T-007 exists to correct.
