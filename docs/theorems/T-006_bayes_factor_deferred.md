<!-- theorem-meta
id: T-006
title: Bayes-factor consequence (DEFERRED - not a theorem target)
claim: C-004
status: deferred
assumptions: A-011
depends_on: T-004
approval: D-003
-->

# T-006 — Why the Bayes-Factor Result Is Not a Theorem Target

Status: **deferred**. Removed from the proof route by D-003
(`docs/approval_log.md`, 2026-09-08). The declared priors and estimator now
govern a numerical prior-sensitivity study reported as a robustness appendix.

This document records *why*, because "it is hard" is not a scientific reason and
would not survive a reviewer asking why the Bayes-factor arm is missing.

## 1. It answers a different question from the one the paper asks

C-001 is a claim about **what an analyst will conclude from model comparison**.
The comparison practices actually used in computational cognitive modelling are
predictive: ELPD, WAIC, PSIS-LOO, cross-validated log score, and — in the older
literature — AIC and BIC. Establishing the failure mode for those criteria is
what makes the paper's warning actionable.

A Bayes factor answers a different question: given two declared prior
predictive distributions, which assigned higher probability to the observed
data? That is a statement about **model evidence under a prior**, not about the
predictive performance an analyst would observe. A theorem about `\log BF_{K,S}`
would broaden the paper's scope without strengthening its central claim, and
would import a second literature (Lindley–Jeffreys, prior sensitivity,
marginal-likelihood estimation) whose disputes are orthogonal to the thesis.

## 2. Its answer is prior-manipulable in the direction that matters

For nested models, `\log BF_{K,S}` contains an Occam-factor term whose magnitude
scales with the prior width on the parameters unique to `M_K`. The sign of
`\log BF_{K,S}` is therefore controllable by the prior scale: a diffuse prior on
the extra ambiguity or mixture parameters penalises `M_K` arbitrarily heavily,
and a tight one favours it.

Any theorem would consequently have the form "for priors in region `R`, model
evidence favours `M_K`" — and a reviewer would correctly observe that the result
is then a statement about `R`, not about omitted context. The predictive results
(T-004, T-005) carry no such dependence, which is exactly what makes them the
stronger evidence for C-001.

## 3. The asymptotic machinery a theorem would need does not apply

`M_K` is a singular statistical model (D-004,
`docs/theorems/T-007_finite_sample_selection.md` §3). The Laplace approximation
underlying every closed-form Bayes-factor asymptotic — BIC, the Schwarz
approximation, the standard `\log BF \approx D_n - \tfrac{1}{2}\Delta k \log n`
expansion — requires a non-degenerate Hessian at an interior maximum. For
mixture and hierarchical models it degenerates precisely at the parameter values
that the project's own boundary conditions 1–3 make central.

The correct expansion is Watanabe's, with the real log canonical threshold
`\lambda` in place of `k/2`. A theorem would therefore need `\lambda` for **both**
`M_S` and `M_K`. RLCTs are known in closed form only for a small catalogue of
model families, and are not known for the ambiguity-model classes in A-009.
There is no route to a rigorous statement without first solving an open problem
in algebraic geometry that is not this paper's contribution.

## 4. The empirical arm could not confirm it anyway

Marginal likelihoods for hierarchical models must be estimated. Bridge sampling
is the best available option and is still sensitive to the proposal, the number
of posterior draws, and the parameterisation; harmonic-mean-type estimators are
inconsistent in the relevant regime. A theorem whose predicted effect is smaller
than the estimator's own variance is not testable in this project, and T-004 §6
shows the population effects here are of order `10^{-6}` per observation.

## 5. What is retained

The Bayes-factor arm survives as a **numerical prior-sensitivity study**, under
the specification declared in D-003:

- priors: standardised coefficients `N(0,1)`; population means `N(0,1)`; scales
  half-`N(0,1)`; correlations LKJ(2); mixture weights Dirichlet(1, …, 1);
- prior-scale sensitivity over multipliers `s \in \{0.5, 1, 2\}`, all reported;
- marginal likelihood by bridge sampling (Meng–Wong), with its relative standard
  error reported; harmonic-mean and posterior-mean estimators prohibited;
- WBIC at inverse temperature `1/\log n` as the required cross-check;
- reported as a robustness appendix; excluded from the abstract; not citable in
  support of C-001.

The scientific value of this study is precisely its *negative* framing: it shows
how much the model-evidence conclusion moves across defensible priors, which
supports the paper's broader point that model-comparison verdicts are less
stable than they are usually reported to be. That is a stronger use of the
material than a fragile theorem.

## 6. Conditions under which this decision should be revisited

Re-open the gate if any of the following becomes true:

1. an RLCT becomes available for the specific `M_S` / `M_K` families in A-009;
2. the project's scope changes so that model evidence, rather than predictive
   performance, becomes the target estimand;
3. a reviewer requires a Bayes-factor theorem for publication — in which case
   the honest response is the sensitivity study plus an explicit statement that
   the singular-model asymptotics are unavailable, not a theorem stated under
   regularity conditions known to fail.
