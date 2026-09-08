<!-- theorem-meta
id: T-003
title: Gaussian constructive heterogeneity result
claim: C-003
status: proof-draft
assumptions: A-001, A-002, A-003, A-007, A-008
depends_on: T-001, T-002
approval: D-001, D-006
-->

# T-003 — Gaussian Constructive Heterogeneity

Status: `proof-draft`. A-003 approved by D-001; A-007 and A-008, used by
Corollary T-003b, approved by D-006 (2026-09-09). Not accepted for
`manuscript/supplement_proofs.tex`: proof-critic review is outstanding.

Notation is bound by `docs/notation_registry.md`.

## 1. Role in the proof route

T-001 says the analyst's target is a mixture over `F_{\Theta \mid X,Z}`. It does
not say what that mixing law looks like. T-003 computes it exactly in the
Gaussian-linear case, and in doing so produces the single quantity the rest of
the route runs on: a **conditional latent variance that depends on `z`**.

T-003 is deliberately not general. Its job is to make T-004 checkable.

## 2. Statement

**Theorem T-003.** Assume A-001, A-002, and A-003. Concretely, let

$$\Theta_i = \alpha_0 + \alpha_1^{\top} Z_i + \gamma\, C_i + U_i,$$

with `U_i \sim N(0, \sigma_u^2)` independent of `(Z_i, C_i)`, and

$$C_i \mid Z_i = z \ \sim\ N\big(m(z),\, v(z)\big), \qquad v(z) \ge 0 .$$

Then for `Z`-almost every `z`,

$$\Theta_i \mid Z_i = z \ \sim\ N\big(\mu(z),\, \sigma^2(z)\big), \qquad
\mu(z) = \alpha_0 + \alpha_1^{\top} z + \gamma\, m(z), \qquad
\sigma^2(z) = \sigma_u^2 + \gamma^2 v(z).$$

**Proof.** Conditional on `Z_i = z`, `\Theta_i` is an affine function of the
independent Gaussians `C_i \mid Z_i = z` and `U_i`, hence Gaussian. Its mean is
`\alpha_0 + \alpha_1^{\top} z + \gamma m(z)` by linearity of conditional
expectation. Its variance is
`\gamma^2 \mathrm{Var}(C_i \mid Z_i = z) + \mathrm{Var}(U_i) = \gamma^2 v(z) + \sigma_u^2`,
where the cross term vanishes by the independence of `U_i` and `(Z_i, C_i)`. `\square`

**Corollary T-003a (sharp heteroskedasticity criterion).**
`\sigma^2(\cdot)` is non-constant **if and only if** `\gamma \ne 0` and
`v(\cdot)` is non-constant.

This is an "if and only if", not an "if", and it is what makes the project's
boundary conditions 1 and 2 exact rather than rhetorical:

- if `\gamma = 0` (omitted context does not shape the latent parameter), the
  induced latent variance is the constant `\sigma_u^2`;
- if `v(\cdot)` is constant (omitted context is present but its conditional
  spread does not vary with observables), the induced latent variance is again
  constant, at `\sigma_u^2 + \gamma^2 v`, and is absorbed by any model with a
  free latent variance.

In both cases the omission is *harmless to model selection* in the precise sense
that the induced mixing law stays inside the simple model's reach (T-004 §4).

## 3. The bridge corollary: probit attenuation

This is the corollary that T-004 actually consumes. It requires A-007 (probit
kernel), approved by D-006. The identity is exact for probit; the logit case is
only approximate and must be derived and labelled separately.

**Corollary T-003b (context-omitted response law under a probit kernel).**
Take the scalar ambiguity index `X = A` with kernel

$$P(Y = 1 \mid A = a, \Theta = \theta) = \Phi(b_0 + \theta a).$$

Then, combining T-001 with T-003, for `Z`-almost every `z`

$$P(Y = 1 \mid A = a, Z = z)
= \Phi\!\left( \frac{b_0 + \mu(z)\, a}{\sqrt{1 + \sigma^2(z)\, a^2}} \right).$$

**Proof.** By T-001 the left side equals
`\int \Phi(b_0 + \theta a)\, dF_{\Theta \mid A, Z}(\theta \mid a, z)`. Under A-008
the design is exogenous in the sense of T-002, so the mixing law is
`N(\mu(z), \sigma^2(z))` from T-003. Apply the Gaussian identity
`\mathbb{E}[\Phi(\alpha + \beta W)] = \Phi\big(\alpha / \sqrt{1 + \beta^2}\big)`
for `W \sim N(0,1)`, with `\alpha = (b_0 + \mu(z) a)/1` and
`\beta = \sigma(z) a`. `\square`

**Remark (this is where false complexity is manufactured).** Write the
*attenuation factor*

$$\kappa(a, z) \ :=\ \big(1 + \sigma^2(z)\, a^2\big)^{-1/2}.$$

The context-omitted response law is `\Phi\big(\kappa(a,z)\,(b_0 + \mu(z)a)\big)`.
Two things follow, and only the second is the paper's contribution:

1. `\kappa` depends on `a` even when `\sigma^2` is constant. So the marginal
   response is already not a linear-index probit. This is ordinary
   random-effects attenuation and is *not* evidence for anything; `M_S` is
   defined to contain exactly this shape.
2. When `\sigma^2(\cdot)` is non-constant, the analyst who also omits `z`
   observes a **mixture over attenuation factors**, and that mixture is a
   different functional form. It presents as an ambiguity-level-dependent
   distortion of the choice curve — which is precisely what a
   source-specific, condition-specific, or nonlinear-in-ambiguity cognitive
   model is parameterised to absorb.

Claim 2 is what T-004 must prove, and it is proved there by an explicit
non-representability argument, not by appeal to this remark.

## 4. Numerical check

`tests/testthat/test-theorem-numerics.R`, case `T-003`, verifies the closed form
against Monte Carlo integration of the kernel, and verifies Corollary T-003a in
both directions. A Python cross-check at 4e6 draws gives a maximum absolute
deviation of `1.0e-4` between the Monte Carlo and closed-form response
probabilities, consistent with Monte Carlo error at that sample size.

## 5. What this result does not establish

- It does not show that any model-selection criterion favours a false complex
  model. That is T-004 (population) and T-007 (finite sample).
- It does not generalise beyond the Gaussian-linear construction. Per D-001
  condition 1, no statement may drop the qualifier.
- It says nothing about whether `\gamma` is identified from data; `C` is
  omitted, so it is not.
