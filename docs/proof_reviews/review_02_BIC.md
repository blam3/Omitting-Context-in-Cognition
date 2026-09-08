# D2 review: uniform convergence, localization and BIC

Date: 2026-09-07. Review type: **separate LLM review pass in the same task**, not independent external acceptance. Scope: L2/C1 and O4–O6 in [PROOF_PACKAGE.md](../../PROOF_PACKAGE.md), lines 143–196. The source SHA-256 is `46e98f94d57f86a724f1a03ac5cdeba4c27324a06d331c403cbc4524cd33943c`, matching the completed D1 review. The proof source was not changed in this run.

## Verdict

**L2 and C1 pass under the stated assumptions.** No missing hypothesis, incorrect constant or invalid probability limit was found in O4–O6. The proof is complete, with participant count growing and two trials fixed. No new assumptions or criterion substitutions are needed.

A model-specific sufficient-statistic argument below gives an additional complete derivation of the uniform bound with a smaller constant. It is recorded as a local refinement for the integration review; the existing valid proof has not been rewritten. Neither bound gives useful ordinary-sample-size guidance for the small gap in this example.

## Checked assumptions and dependencies

- A-007 supplies independent identically distributed **participant pairs**, not independent marginal trial rows. Dependence between the two responses is retained.
- A-008 supplies fixed compact boxes, normalized candidate probabilities and two fixed design vectors. Candidate dimension is one versus two.
- A-010 defines $n$ as participant count with the response-pair design fixed. The BIC comparison uses this $n$.
- D1 verified the strictly positive KL gap and interior population optima. The matching source hash permits reuse without repeating that review.
- A-009's priors are not used in L2 or C1. A-011 affects the separate general vector corollary, not the constructive sampling calculation.
- O4 plus the positive gap is sufficient for BIC selection consistency. O5's parameter localization is needed for later evidence integration, not logically necessary for the BIC sign limit. The presentation can exploit this distinction at integration without changing the conclusion.

Sketch classification: COMPLETE. Verification status: verified within this scoped LLM pass. No dependency on an uninspected external theorem; the only tools used in the analytical check are finite sums, Chebyshev, union bounds, compactness and finite-dimensional calculus.

## O4: finite-state uniform convergence

**Source lines 145–152.** A simple predictor has absolute value at most $2$; a quadratic predictor has absolute value at most $|b|2+|d|4=6$. Both success and failure probabilities are therefore at least $\sigma(-6)$, and every pair probability is at least $\delta=\sigma(-6)^2$. Thus $M=-\log\delta$ is a finite log-probability envelope.

For either candidate, write the empirical objective using the same four pair frequencies $f_n(w)$. The triangle inequality gives

$$U_n\le M\sum_{w\in\mathcal W}|f_n(w)-P(w)|.$$

If $U_n\ge u>0$, at least one cell frequency deviation is at least $u/(4M)$. For each cell its indicator is Bernoulli across independent participants, so its sample-frequency variance is $P(w)(1-P(w))/n\le1/(4n)$. Chebyshev followed by a union bound gives

$$P(U_n\ge u)\le\min\{1,4\cdot(1/(4n))\cdot(4M/u)^2\}
=\min\{1,16M^2/(nu^2)\}.$$

This also proves the displayed strict-tail bound. The non-strict form justifies its later use on complement and tie events; no continuity of the finite-sample distribution is being assumed. The four cells need not be mutually independent. There is no extra factor for the two models: a single envelope event controls both parameter families simultaneously.

**Source lines 154–156.** Pointwise objective deviations bounded by $U_n$ imply deviations of their maxima bounded by $U_n$, by applying the upper and lower inequalities at maximizers. Compactness and continuity ensure maxima exist. Thus

$$|D_n/n-\Delta|\le2U_n\to_p0.$$

This controls optimized log likelihood, not just likelihood at the population parameter. Measurability causes no hidden issue: at each fixed $n$ the empirical frequency vector takes only finitely many values, and each corresponding compact optimization has a unique result.

## O5: curvature and localization

**Source lines 158–167.** The logarithm of each logistic trial probability has second derivative $-\sigma'(\eta)$ with respect to its linear predictor, regardless of the response. Summing two trials and dividing the participant log likelihood by $n$ gives exactly the Hessian displayed in L2. Within-person correlation affects the score covariance, but does not invalidate this algebraic Hessian identity.

The Gram matrices are $G_S=(5)$ and $G_K=\begin{pmatrix}5&9\\9&17\end{pmatrix}$. The latter has eigenvalues $11\pm\sqrt{117}>0$. Since $\sigma'$ is even and decreasing in absolute predictor value, the global lower factor $\sigma'(6)$ and upper factor $1/4$ are valid on both boxes. Consequently the stated $\lambda_j$ and $L_j$ are fixed, strictly positive/finite curvature constants.

**Source lines 169–177.** Empirical optimality gives the population objective loss at the fitted parameter at most $2U_n$. Population strong concavity around the known interior population maximizer then gives

$$\frac{\lambda_j}{2}\|\widehat\theta_{j,n}-\theta_j^*\|^2\le2U_n.$$

This population Taylor step does not assume the empirical parameter is interior. It is valid along the segment inside the convex box, and the gradient vanishes at the already verified population optimum.

Let $d_j$ be its distance to the box boundary, $r_j=d_j/4$, and $c=\min_j\lambda_jr_j^2/4>0$. On $E_n=\{U_n<c\}$ the parameter error is strictly smaller than $r_j$. Hence the fitted parameter's distance to the boundary exceeds $d_j-r_j=3r_j$; the claimed radius-$r_j$ ball is contained in the box. The explicit event bound is

$$P(E_n^c)\le\min\{1,16M^2/(nc^2)\}\longrightarrow0.$$

Localization therefore precedes any empirical-maximizer Taylor argument needed later. It is not true that the empirical optimum is interior for every sample: for one observed pair $00$, the simple maximizer is $b=-1$, and the quadratic maximizer is $(b,d)=(-1,-1)$. That boundary sample is consistent with the high-probability localization claim and is not a counterexample to it.

## O6: BIC algebra and probability conversion

**Source lines 181–189.** With $k_K-k_S=1$ the difference is exactly $-2D_n+\log n$. The complex candidate wins iff $2D_n>\log n$, and equality is a tie. Dividing by $n$, using O4 and $\log n/n\to0$, gives convergence in probability to $-2\Delta<0$. A neighborhood of that negative limit lies wholly below zero, which proves that the probability of complex selection tends to one. No true-model assumption for either candidate is needed to establish this result for the explicitly defined BIC statistic.

**Source lines 191–194.** Put $a_n=\Delta-\log(n)/(2n)$. Only when $a_n>0$ does the failure event imply

$$\Delta-D_n/n\ge a_n,\quad U_n\ge a_n/2.$$

The non-strict Chebyshev bound from O4 then gives exactly

$$P(\operatorname{BIC}_K\ge\operatorname{BIC}_S)
\le\min\{1,64M^2/(na_n^2)\}.$$

The coefficient $64$ and square on the gap are correct. When $a_n\le0$, this expression is not licensed by the argument, even if its algebraic denominator exists; use the trivial probability bound $1$. Expected gain is never substituted for realized gain in the deterministic criterion. Neither $D_n-n\Delta=O_p(1)$ nor finite-sample certainty is assumed.

The use of participant count is appropriate to the stated fixed-length participant model. Using $2n$ would add a constant $\log2$ to this model-pair BIC difference and alter the exact finite-sample threshold; it would not alter this asymptotic sign limit. Neither choice licenses a growing-trial or general hierarchical BIC approximation. Evidence equivalence remains D3's separate obligation.

## Additional local refinement: two sufficient statistics

This derivation uses the same model, parameter boxes and sampling law, with **no additional assumption**. It sharpens the constant; it does not change the rate or empirical claims.

For one pair set $A=Y_1+2Y_2$ and $B=Y_1+4Y_2$. Define the centered sample means $e_A=\overline A-EA$ and $e_B=\overline B-EB$. The pair log likelihood in K is

$$bA+dB-\log(1+e^{b+d})-\log(1+e^{2b+4d}).$$

The deterministic log-normalizing terms cancel when subtracting the population objective from the empirical normalized objective. Thus the difference is **exactly** $be_A+de_B$ in K and $be_A$ in S. Taking absolute suprema on the boxes gives

$$U_n=|e_A|+|e_B|.$$

The maximum is attained at a box corner with coefficient signs matching the respective errors; K contains S at $d=0$. This shows why the four-cell envelope proof is more general than this example requires.

Using the already checked $p_1=5/8$, $p_2=7/10$, covariance $1/40$, and marginal variances $15/64$ and $21/100$,

$$EA=81/40,\quad EB=137/40,$$
$$\operatorname{Var}(A)=15/64+4(21/100)+4(1/40)=1879/1600,$$
$$\operatorname{Var}(B)=15/64+16(21/100)+8(1/40)=6071/1600.$$

These variances explicitly include within-person dependence. Independence of participants gives variance of each centered sample mean equal to its one-person variance divided by $n$. The inclusion

$$\{|e_A|+|e_B|\ge u\}\subseteq\{|e_A|\ge u/2\}\cup\{|e_B|\ge u/2\}$$

and two Chebyshev bounds give, for all $n\ge1,u>0$,

$$P(U_n\ge u)\le\min\{1,4[\operatorname{Var}(A)+\operatorname{Var}(B)]/(nu^2)\}
=\min\{1,159/(8nu^2)\}.$$

No independence between $A$ and $B$ is used. Substituting $u=a_n/2$, for $a_n>0$, yields the additional BIC bound

$$P(\operatorname{BIC}_K\ge\operatorname{BIC}_S)\le\min\{1,159/(2na_n^2)\}.$$

The original uniform coefficient is about $2305.90$, versus $159/8=19.875$ here, a factor of about $116$ before truncation at one. This is **not** a 116-fold empirical improvement or a guarantee of a comparably smaller required sample: both are loose worst-case bounds, often equal to one after truncation. Record the refinement for D5's presentation choice; do not infer practical model-selection rates from it.

## Checks, closure and next action

[verify_bic_review.py](../../scripts/verify_bic_review.py) uses exact fractions to check the two sufficient-statistic variances and all multinomial frequency vectors for $n=1,2,4,8$ (214 vectors total). For five positive thresholds at each $n$, it computes exact $P(U_n\ge u)$ and checks the refined inequality. It also checks the box-corner supremum and Gram eigenvalue identities. The [result artifact](../../logs/theory_checks/2026-09-07_BIC_review.json) records all outcomes, including trivial bounds. These finite calculations support the analytical derivation above; they are not a proof for all $n$ or a simulation study.

| Obligation | Closure | Evidence |
|---|---|---|
| O4 | CLOSED-LOCAL, reviewed | Finite-cell Chebyshev and maximum inequalities; exact sufficient-statistic refinement |
| O5 | CLOSED-LOCAL, reviewed | Response-independent Hessian, positive Gram eigenvalues, explicit interior-event bound |
| O6 | CLOSED-LOCAL, reviewed | Exact BIC algebra, probability sign limit and failure-event inclusion |

No S0/S1 issue was found, and no main-proof edit or assumption-register change was necessary. The checked proof hash is unchanged. A new structural-lint pass is unnecessary because the proof was not edited; D1's lint remains a structure check only.

Next: **D3_BF_review**, O7. Verify both prior-weighted integral bounds on the interior event and the $O_p(1)$ remainder relative to the realized fitted likelihood. O4–O6 are closed for this separate LLM review; full-package external acceptance remains pending.
