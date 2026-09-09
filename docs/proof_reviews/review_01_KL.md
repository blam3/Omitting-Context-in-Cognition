# D1 review: mixture and strict observable KL separation

Date: 2026-09-06. Scope: L1, T1 and O1–O3 in `PROOF_PACKAGE.md`, plus the scalar/exogenous/participant statements in `docs/omitted_context_mixture_lemma.md`. Review type: **separate LLM review pass in the same task**, with access to prior author work. This is not an independent external or human review.

## Verdict

**The scalar mixture lemma and the constructive strict participant-level KL separation are verified under their stated hypotheses.** The derivations are complete, and the infimal risks satisfy $0<R_K<R_S$. The general participant-vector extension needed a more precise (stronger) conditional-independence premise; that local gap is repaired and documented below. Exogeneity wording was also corrected to avoid an unjustified necessity claim.

No constructive model, data-generating assumption A-007–A-010, prior, sample unit, or target was changed. No criterion corollary is newly certified by this review. D1 can close and D2 can begin. Final manuscript acceptance remains pending.

## Source provenance and checked scope

The proof and mixture files matched the preceding day's staged versions byte-for-byte before this review. Git showed the previously recorded uncommitted work; no unrelated work was reverted.

| Source | Pre-review SHA-256 |
|---|---|
| `PROOF_PACKAGE.md` | `5a6c64ab5632a9b883051c86f2d49c14298a26f940eac8f37421b4a5ad9bc8b2` |
| `docs/omitted_context_mixture_lemma.md` | `cde0fad5e160d938543426d953796ec623e5cbea5e63ca6475fe95d84674dbde` |

Line anchors below refer to this reviewed version; the two repairs preserve line counts. The post-review proof hash is recorded in `registries/proof_progress.json`. Anchor links use repository-relative files for portability.

- [Proof package](../../PROOF_PACKAGE.md): assumptions lines 21–27; L1 lines 94–101; T1 lines 103–141; the Gram-matrix check for O2 lines 158–167.
- [Standalone mixture note](../omitted_context_mixture_lemma.md): lines 7–21, 23–25, 29–33.
- Numeric cross-check: [exact arithmetic report](../../logs/theory_checks/2026-09-06_KL_review.json), produced by [a separate standard-library verifier](../../scripts/verify_kl_review.py). It imports no author verifier code and runs no Monte Carlo simulation.

## Verification target, dependencies and assumption audit

The target is separation of the minima of joint KL risks over the **specified model families**, not positive risk at one arbitrary slope. The dependency chain is A-007/A-008 → exact pair distribution → marginal-logit incompatibility and attainable optima → KL decomposition → strictly positive risk difference. It does not use the later BIC/BF/LOO conclusions.

| Unit | Assumptions actually used | Verdict |
|---|---|---|
| Scalar L1 | Finite responses, measurable normalized conditional kernel, existence of the regular conditional mixing law | Complete tower-property proof; no exogeneity needed |
| Exogenous corollary | Scalar L1 plus $\Theta\perp X\mid Z$ | Valid sufficient condition; not an “only if” result for an individual integrated kernel |
| Participant-vector extension | Same trial kernels, deterministic common design, and mutual independence of trials **given $(\Theta,Z)$** | Valid after explicit scoped repair A-011 |
| T1 | A-007 and A-008 only | Complete direct finite-state proof |
| O2 matrix prerequisite | Two predictor vectors $(1,1)$ and $(2,4)$; candidate probabilities interior | Full rank; checked without importing later statistical convergence |

T1 needs neither priors nor participant-count asymptotics to establish its population KL result. Participant independence across people is declared for downstream inference, but the one-person KL calculation itself does not use it. Gaussianity is absent. The general existence of regular conditional distributions is assumed, not newly proved here; T1 uses finite context and so directly defines its mixing measure.

Sketch classification: COMPLETE for scalar L1 and T1. The participant extension had an insufficient premise under a literal reading; its corrected version now has a direct finite-vector tower proof. No sketch is being used in lieu of a missing convergence theorem in this scoped review.

## Reconstructed derivation, checked independently

### O1: four observable cells and actual dependence

For $C=0$, every response pair has probability $1/4$. For $C=1$, independent success probabilities $3/4$ and $9/10$ give probabilities $(1,3,9,27)/40$ in order $(00,10,01,11)$. Averaging yields $(11,13,19,37)/80$, as printed at proof lines 105–109.

Summation gives $p_1=5/8$ and $p_2=7/10$. The independence determinant is

$$P_{00}P_{11}-P_{01}P_{10}
=\frac{11\cdot37-19\cdot13}{80^2}=\frac1{40}>0.$$

It agrees with $\operatorname{Cov}(Y_1,Y_2)=1/40$. Every candidate in A-008 factors as a product, and its corresponding determinant is zero. Therefore **every** candidate joint distribution is false, including the risk minimizers. This conclusion does not rely on a fitted coefficient being nonzero.

### O2: optima and parameter interiors

Writing $a_1=\log(5/3)$ and $a_2=\log(7/3)$, matching the complex model's two logits solves the nonsingular linear system

$$b+d=a_1,\qquad 2b+4d=a_2.$$

Its unique solution is $(b,d)=(2a_1-a_2/2,a_2/2-a_1)$. The bounds at proof line 121 check algebraically: $d=-(1/2)\log(25/21)$ has magnitude below $2/21$, and $b=\log(25/(3\sqrt{21}))$ lies between zero and one. The proof's use of $e>5/2$ is justified, for example, by $e=\sum_{k\ge0}1/k!>1+1+1/2$.

The simple score is strictly decreasing because $F_S''(b)=-\sigma'(b)-4\sigma'(2b)<0$. Its signs at $a_2/2$ and $a_1$ are opposite because $25>21$. The intermediate value theorem and strict monotonicity give the unique global optimum in that interval. This establishes both attainment and interiority rather than assuming them.

For the shared O2 matrix prerequisite, the design determinant is $4-2=2$, so its Gram determinant is $4$. The Gram matrices printed in the package are correct. No identifiability failure or boundary optimum is hidden here.

### O3: decomposition, equality conditions and a strict infimum gap

For any $0<r_1,r_2<1$, insert and cancel the product of true marginals inside the log ratio:

$$\log\frac{P(w)}{Q_1(y_1)Q_2(y_2)}
=\log\frac{P(w)}{P_1(y_1)P_2(y_2)}
+\log\frac{P_1(y_1)}{Q_1(y_1)}
+\log\frac{P_2(y_2)}{Q_2(y_2)}.$$

Summing against $P$ proves the displayed joint/marginal KL decomposition. All probabilities involved are positive in the candidate boxes, so there is no undefined entropy subtraction. KL nonnegativity follows from $-\log t\ge1-t$ with $t=Q/P$, and equality forces identical distributions.

The complex optimum has zero marginal KL costs and retains strictly positive mutual information $I_P(Y_1;Y_2)$. The simple optimum cannot set both marginal costs to zero: that would imply $2\log(5/3)=\log(7/3)$, or $25=21$. Since the optimum is attained, failure of exact matching implies strictly positive excess risk; this is not the invalid general inference that mere nonmembership always implies separation from a nonclosed family.

Numerical checks at 60-digit working precision give:

| Quantity | Value (rounded; not an interval certificate) |
|---|---:|
| $b_S^*$ | 0.4429045203006521 |
| $b_K^*$ | 0.5980023173383796 |
| $d_K^*$ | −0.08717669357238888 |
| $R_K$ | 0.006269568286252995 |
| $R_S$ | 0.006968082969843056 |
| $\Delta$ per participant | 0.0006985146835900607 |

The analytical inequalities above, not numerical precision, establish strict positivity. The numerical report additionally checks the decomposition at a nonoptimal arbitrary product distribution to avoid testing only a tautological zero-marginal-cost case.

## Findings and repairs

### D1-I1 — S1: the general participant-vector corollary conditioned independence too weakly

**Evidence:** standalone mixture note, pre-review line 29, said trials were conditionally independent given a participant's latent parameter, but line 31 asserted their product factorization **after also conditioning on $Z$**. That implication does not hold in general.

**Counterexample:** let $Z$ and $U$ be independent fair bits, $\Theta$ constant, $Y_1=U$ and $Y_2=U\mathbin{\mathrm{xor}}Z$. Here $Z$ can be generated first as a baseline covariate. Unconditionally, $Y_1,Y_2$ are independent fair bits, so independence given constant $\Theta$ holds. Each trial is also a fair bit after conditioning on $(Z,\Theta)$, so the scalar trial-kernel premise holds. Yet conditional on $Z=0$, only pairs $00$ and $11$ occur, each with probability $1/2$; conditional on $Z=1$, only $01$ and $10$ occur. The displayed product of fair trial kernels would give $1/4$ in each cell and is false.

**Repair:** explicitly require mutual conditional independence given $(\Theta,Z)$ and the stated trial kernels. Then the vector conditional law factors, and the same tower argument gives the integral of that product. Also state the conclusion for $Z$-almost every $z$. The standalone note line 29 and the general participant sentence at proof line 101 now say this. Scoped assumption A-011 records the stronger sufficient premise; it is not silently treated as implied by A-001.

**Downstream impact:** none on the constructive T1 distribution or its A-007–A-010. The construction has no varying retained $Z$ and already assumes trial independence conditional on its shared context. The general scalar mixture identity also remains unchanged.

**Closure:** CLOSED after explicit assumption correction. This is a stronger premise for a general corollary, not a proof of the old literal statement.

### D1-I2 — S2: “Only under” overstated the role of exogeneity

**Evidence:** pre-review proof line 101 stated that only under $\Theta\perp X\mid Z$ could the simplified mixing law be used. Independence is a sufficient condition for equality of the mixing measures; equality of integrals for a particular kernel may occur even when those measures differ.

**Counterexample:** let $X=\Theta$ be a fair bit and let $Y$ be an independent fair bit, with $Z$ constant. The conditional mixing measure is a point mass; the marginal measure assigns $1/2$ to each point. They differ, but both integrate the constant kernel $p(Y=1\mid x,\theta)=1/2$ to $1/2$.

**Repair:** proof line 101 now says “Under” independence and expressly labels it sufficient, not necessary for the particular response-kernel equality. The standalone corollary already used the correct “If additionally” wording.

**Closure:** CLOSED. No new model condition or change to the primary $F_{\Theta\mid X,Z}$ statement.

## Adversarial model-scope checks (limitations, not failures of T1)

1. **Is the gap a parameter-box artifact?** Although the contextual slope $\log3$ exceeds the simple box's upper endpoint, the mixture's optimal simple slope lies strictly inside it. The derivative is strictly decreasing on all $\mathbb R$ and crosses zero at the same $b_S^*$. Thus enlarging $S$ to all real slopes leaves its minimum risk unchanged. Enlarging $K$ cannot beat the product-of-marginals minimum already attained. The same strict KL gap holds for these unconstrained families. This observation extends only the KL comparison, not the compactness-based criterion corollaries or priors.
2. **Is quadratic curvature identified by two trial levels?** No. A distinct two-parameter model $\sigma(a+bx)$ matches both marginals with $a=2a_1-a_2$ and $b=a_2-a_1$. It has the same product joint distribution as $K$ at its optimum and the same risk. T1 is specifically a comparison against the fixed-zero-intercept one-slope model; it does not distinguish curvature from every alternative explanation. A final cognitive interpretation must retain that restriction explicitly.
3. **Could shared random effects eliminate the gap?** Yes. Giving the simple model the correct shared two-point mixing law reproduces $P$ exactly. This is already a stated boundary and supports the intended omitted-context interpretation.
4. **Could nonmembership merely have zero infimal distance?** Not here: the minimizer is interior and attained, and its two marginal logits are incompatible. The review did not rely on nonmembership alone.
5. **Does a one-trial Bernoulli mixture prove observable complexity?** No. This proof uses two predictor values to force a response-function mismatch and the full response pair to establish that both joint distributions remain false.

The no-intercept restriction and two-level design should remain visible in the later ambiguity-mapping review. They do not require changing this existence theorem to rescue it.

## Check results, acceptance and next task

- Exact rational joint-cell, marginal, covariance and determinant checks: PASS.
- Explicit counterexamples to both overbroad statements: PASS.
- Independent Decimal calculation of the KL risks, marginal projection and optimum signs: PASS.
- Direct analytical review of L1 and T1, including the corrected vector premise: PASS within stated scope.
- Structural lint after the prose repairs: recorded separately; it does not verify mathematics.
- No new simulation grid, seed changes, criterion re-fit or full R test suite was needed for these proof-only repairs.

D1 has no unresolved S0/S1 issue within its scope. O1–O3 have a separate LLM review pass; all-package external acceptance is still pending. Next is **D2_BIC_review**: verify L2/C1 and O4–O6, especially the uniform convergence event, localization and finite-sample probability bound. Do not rerun D1 absent a changed dependency or new counterexample.
