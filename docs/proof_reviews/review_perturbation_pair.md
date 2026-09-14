# Separate review of the joint and conditional perturbation lemmas

Date: 2026-09-10. Reviewer: same LLM task in a separate adversarial pass; not an independent external reviewer, Lean verification, or PI acceptance. Reviewed commit: ca32dff. Verdict: PASS within the stated finite exponential-family scope. No load-bearing mathematical defect found; no source-proof edits needed. Cognitive instantiation and Bayesian score convergence remain unreviewed/open here.

## Locked sources and scope

- `docs/context_score_perturbation_2026-09-09.md` (CP), SHA256 `6e967ebf77d5ba2f23c226bb68dee08554ba30cd38cbc25d571337bc0cb71181`.
- `docs/trial_conditional_perturbation_2026-09-09.md` (TC), SHA256 `706408b864995c3b46cde41bb8bd4b26581a7138c4f83a8525c7e15528e001c6`.

Line anchors below refer to those hashes. Governing scope: finite W and response support; positive baseline probabilities; bounded centered tilt; fixed H; full real natural-parameter spaces; positive-definite observable score covariance. These are conditional theorem hypotheses, not findings about RAID or the approved nonlinear hierarchy. Conditional positivity/connected-support claims are checked only with their stated additional support condition.

## Obligation-by-obligation findings

| Obligation and source | Reconstruction / attempted failure | Verdict |
|---|---|---|
| Tilt validity, CP 16–20 | The density multiplier is positive for the stated strict bound. Conditional mean zero normalizes each latent law. Bayes' formula gives h=E[k|Y,W], hence exact p_e=p0(1+e h) and bounded h. Fixed H is retained. | Pass |
| Score centering, CP 11–25 | Subtracting conditional score means merely changes each log normalizer. Positive-definite G gives invertible I and strictly positive Schur complement J. | Pass |
| Existence versus global fitting, CP 40–44 | The inverse function theorem alone would only yield a local stationary branch. Here every tilted finite law has the same positive support. A zero covariance direction would be constant on each conditional support at baseline too, contradicting G>0. The objective is strictly convex on all R^(d+1), so the stationary point is the unique GLOBAL minimum. No compact box or unexplained optimizer assumption is used. | Pass |
| KL remainder, CP 46–57 | On a small closed interval in e, positivity and analyticity provide bounded derivatives over finitely many cells. The fitted branch is analytic and O(e); Taylor errors are O(|e|^3). Normalization cancels linear terms. The positive residual coefficient establishes strictly positive risk at the attained global K optimum, not merely at a selected parameter. | Pass |
| Latent alignment, CP 61–73 | E[V_perp|W]=0 implies centering of g and g_C by the tower property. Both are bounded. Taking k=g_C gives B=E[g_C²]; conditioning on W includes X throughout. Reweighting by (C,W) preserves u|C,W but need not preserve u|Z or fixed context moments. The source explicitly records those limitations. | Pass |
| Conditional expansion, TC 44–64 | Marginalization changes a first-order score into its baseline conditional expectation. The exact chain rule uses the perturbed retained-response distribution; only the leading quadratic inner product uses p0. Expanding normalized paths removes the mean second-order density term. No unjustified replacement of an O(e) expectation contribution occurs. | Pass |
| Operator sign, TC 9–40 | Each conditional expectation is an orthogonal projection. Their complement average A is positive semidefinite, but is generally NOT a projection. The proof uses self-adjointness and positivity only, never A²=A. Joint orthogonality does not remove the A-weighted cross-term. | Pass |
| Sufficient sign conditions, TC 66–76 | Invariance kills the cross-term by orthogonality to the full K tangent space. The quantitative bound follows from Cauchy–Schwarz in the A seminorm, including degeneracy. Full Cartesian positive support makes zero energy imply coordinatewise constancy; structural-zero cases are explicitly excluded from this shortcut. | Pass |
| Counterexample global fits, TC 80–107 | In K, x|y=-1 is uniform, x|y=+1 is free, and a controls the y marginal independently of b. The claimed fit minimizes the two free factors exactly. The supplied a,b realize it. The true mean in the fixed stratum is 4e, so K remains false for every nonzero admissible e. | Pass |
| Positive control, TC 109–116 | K has independent binary marginals; its joint projection matches both. The true interaction e/2 cannot be matched. d=y is an A eigenvector with eigenvalue 1/2, so conditional improvement follows without a conditional refit. | Pass |
| Downstream interpretation, TC 118–122 | Fixed-e population risk expansions are not n-asymptotics, and the source does not claim they establish posterior/deletion convergence. Neither diagnostic is presented as the approved cognitive example. | Pass |

## Independent reconstruction of the negative control

Let F(z)=((1+z)log(1+z)+(1-z)log(1-z))/2, the KL divergence from a binary law of mean z to the fair law. Decomposing by y in the negative example gives exactly

    R_S = [F(2e)+F(4e)]/2,
    R_K = F(4e)/2,
    Delta_J = F(2e)/2.

The y marginals of P, S and K all agree. The x means are respectively 3e, 0 and e. The difference in x-marginal KL risks is therefore

    G(e)=E_P log(q_K,x/q_S,x)
        =log(1-e²)/2+3e atanh(e).

Consequently Delta_C=F(2e)/2-G(e)/2. Expanding F(z)=z²/2+O(z^4) and G(e)=5e²/2+O(e^4) gives Delta_C=-e²/4+O(e^4), independently recovering the operator calculation. This checks the sign without differentiating a fitted conditional objective.

The exact rational inner products give joint-gap coefficient 1, complex-risk coefficient 4 and conditional-gap coefficient -1/4. For the positive control they give 1/2, 1/8 and 1/4. The new checker also evaluates the closed negative-control risks using 65-digit decimal arithmetic at positive and negative e. These numerical evaluations support transcription/algebra checking; the local sign statement rests on the analytic expansion.

## Adversarial attacks and boundaries

Attack 1: try to invalidate the optimum by a distant or boundary natural parameter. This fails within these families because strict convexity plus the existing stationary point gives a global minimizer. It remains a REAL unresolved issue outside exponential families; do not transfer this reasoning to mixtures by analogy.

Attack 2: try to invalidate the conditional expansion because its conditioning distribution changes with e. This fails because the exact KL chain identity already uses that distribution. The quadratic expansion is performed separately on joint and retained-marginal KL, with their actual normalized paths.

Degenerate checks: B=0 or J=0 does not yield a strict gap; J=0 falls outside the theorem. A zero K residual cannot prove observable falsity through this second-order result. L=0 cannot decide the conditional sign. Reweighting an unconstrained context law is not automatically permitted if specific conditional moments or residual independence must stay fixed. All are either excluded or explicitly left open in the sources.

## Verification and acceptance limits

Executed `python3 scripts/verify_perturbation_review.py`: rational projection/conditional-expectation checks and separate closed-risk evaluations passed. Evidence: `logs/theory_checks/2026-09-10_perturbation_review.json`, which records source hashes. No Lean build, new Monte Carlo fit, external review, new scientific assumption approval or Bayesian convergence proof occurred.

These lemmas can now feed the next author development stage with the label “separate same-LLM review passed.” That label must not be shortened to “independently verified” or “formally verified.” The reviewed source files remain unchanged so subsequent revisions can be detected from hashes.

## Next exact task

Write `docs/smooth_observable_extension.md`: a finite-support smooth nested observable-family theorem with explicit local charts, tangent injectivity, regularity and a global-localization condition. Prove the global projection stays in the regular chart or clearly state that condition as a remaining sufficient hypothesis. Reuse the conditional operator argument only after the joint fitted-path expansion is established. The cognitive-model check of those hypotheses remains a separate obligation.
