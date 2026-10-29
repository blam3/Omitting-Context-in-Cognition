# Independent audit of the revised central-theorem manuscript

Date: 2026-10-29. Auditor: Claude, in a session separate from the one that produced the revision. The auditor wrote the original 2 October draft, so this is independent of the revision, not of the project.

**Audited file:** `revised_central_theorem.tex`, SHA-256 `a2f75be4…d6744`.
**Compared against:** the original draft `central_theorem_full_draft.pdf` (SHA-256 `75caabb0…08af6`), identical to the copy in [`docs/`](central_theorem_full_draft.md), and the handoff note `central-theorem-plan.md`.
**Not available:** the revision's `verify_revised_theorem.py` was not provided, so its code was not audited.

Every numerical claim was instead recomputed by a new, dependency-free script, [`scripts/audit_revised_central_theorem.py`](../scripts/audit_revised_central_theorem.py), with output in [`logs/theory_checks/2026-10-29_revised_theorem_audit.json`](../logs/theory_checks/2026-10-29_revised_theorem_audit.json). Numerical agreement supports arithmetic and specific instances only. Each proof was checked by hand.

## 1. Verdict

**No theorem in the revision is false as stated.** The revision is a substantive improvement: it puts the exact witness first, separates the homogeneous and hierarchical regimes, and makes the hierarchical extension explicitly conditional. Several of its corrections to the original draft are correct and important:

- the parity hypothesis (the extra score must be Z-even);
- the singular-direction caveat in Remark 6.3;
- the zero-variance boundary exclusion;
- the hypercube argument in Corollary 8.1, which removes a special-case condition from the original.

It is **not yet watertight**:

- **Two issues must be fixed before the stated results follow** (§2, F1–F2).
- **Three proof-completeness gaps** should be closed for publication (F3–F5).
- **About ten minor or editorial points** remain (F6–F16).
- The change log mischaracterizes three items of the original draft (§5).

None of these affects the hierarchical extension's starting point. After F1–F2 the manuscript is a sound foundation. The numerical test of Theorem 7.2 (§6) yields one important practical lesson for that extension.

## 2. Findings, ranked

Severity levels:

- **S1:** a stated result does not follow as written.
- **S2:** a proof step is a sketch or uses a tool outside its stated conditions; the conclusion is believed true.
- **S3:** a minor error or wording issue.
- **E:** editorial.

| ID | Location | Severity | Issue | Fix |
|---|---|---|---|---|
| F1 | Thm 4.1 / Cor 8.1 | S1 | Thm 4.1 assumes $\mathcal Q_S\subseteq\mathcal Q_K$. Cor 8.1 applies it to $S_C$ versus $K$, which are not nested (neither contains the other). As written, Cor 8.1's selection claims do not follow from Thm 4.1. The proof of Thm 4.1 never uses nesting except in the likelihood-ratio sentence. | Drop nesting from Thm 4.1's hypotheses. State it only for the likelihood-ratio sentence: "If moreover $\mathcal Q_S\subseteq\mathcal Q_K$, the LR statistic …" |
| F2 | Thm 6.2 proof | S1 | The theorem asserts expansions of the **global** risks $R_M(\varepsilon)$. The proof only shows that a *local* quadratic approximation is minimized by weighted least squares; it never shows that global KL projections lie near $p_0$. That localization step appears only later, in Thm 7.2's proof. | Prove Thm 6.2 as the $k=2$, $h=h_A+h_D$ case of Thm 7.2 (move 7.2's statement earlier, or forward-reference it), then specialize with the product reduction. Affine-logit families are analytic, so the $O(\varepsilon^5)$ remainder survives. |
| F3 | Thm 4.1 proof | S2 | Small-cell exclusion for noncompact parameter spaces, and uniform posterior concentration over all $nT$ single-response deletions, are asserted ("standard likelihood-gap bounds") rather than proved. The logic is right: it is L4–L6 of [`primary_separation_attempt_2026-09-08.md`](primary_separation_attempt_2026-09-08.md). | Add an appendix with the explicit argument: one frequency event, a deterministic $O(1/n)$ effect of deleting a participant, a tilt bounded below by $(q^\star_{\min}/2)\Pi_{-i}(V_0)$, and Lipschitz logs. |
| F4 | Thm 7.2 proof | S2 | It cites "the implicit-function theorem" although $p_\varepsilon$ is only $p_0\{1+\varepsilon^kh+o(\varepsilon^k)\}$ and need not be differentiable in $\varepsilon$. The argument is valid if the IFT is applied with the **law $p$** as parameter: $\nabla_\psi\mathrm{KL}(p\Vert q(\psi))$ is linear in $p$ and $C^1$ in $\psi$ for a $C^2$ chart. The fitted coordinate is then $C^1$ in $p$ and $p_\varepsilon-p_0=O(\varepsilon^k)$. | Say so explicitly. Also note uniqueness: strict convexity of $\psi\mapsto\mathrm{KL}(p\Vert q(\psi))$ near 0 holds for $p$ near $p_0$ by continuity of the Hessian. |
| F5 | §1, §4 | S2 | BIC, $m_M$, BF, ELPD/LOOIC and "selects" are never defined, though the theorems are about them. BIC must use $\sup_\phi$ when the maximum is not attained; LOOIC must be $-2\sum_{i,t}\log\hat p_M(y_{it}\mid D_{-it})$. | Add a short definitions paragraph (as in §1.4 of the original draft). |
| F6 | Thm 3.1 table | S3 | $\theta_S^\star=0.4429045138$ is wrong in the 9th digit; the root of $\sum_tx_t\{\mathrm{expit}(-x_t\theta)-p_t\}=0$ is $0.4429045203$. $R_S$ is unaffected to 10 digits because the objective is flat. | Correct the digit. |
| F7 | Prop 5.2 | S3 | (i) §5 defines $e$ and $\Lambda$ with respect to $\rho$, while Prop 5.2 silently redefines $e=\partial_\delta\eta_K$, so $\Lambda$ there is $\Lambda_\delta=\Lambda_\rho/\delta'(\rho_0)$. (ii) The Taylor bound needs the whole segment $s\in[0,\Lambda/B]$ to be feasible, not only the endpoint; this is automatic for convex parameter boxes. | Write $\Lambda_\delta$. Say "for all $s$ between 0 and $\Lambda_\delta/B$". |
| F8 | §1, eq. (3) | S3 | $C_M$ depends on which optimal law is used when the optimum is not unique. | "For a chosen optimal law; when used for LOO, uniqueness (T3) is assumed." |
| F9 | Lemma 2.3 | S3 | "Its risk is strictly positive whenever $R_K+\mathrm{I}(Y;C\mid W)>0$" is a tautology, because that sum *is* the risk. | Replace with "it is positive iff $p(\cdot\mid w,c)$ varies with $c$ on a positive-mass set or $R_K>0$." |
| F10 | throughout | E | Notation clashes and gaps: $\pi'_{t0}$ is used but never defined (it means $\pi_{t0}(1-\pi_{t0})$); $H_p(Y\mid W)$ (entropy) clashes with $H(w)$ (design weights); $\mathrm{IP}$ is a nonstandard macro. | Define $\pi'$; write $\mathrm{Ent}_p$; write $I$. |
| F11 | Remark 6.3 | S3 | "An exact zero gap for every truth requires $\overline{\mathcal Q_S}=\overline{\mathcal Q_K}$" is slightly too strong: only positive truths are considered, and nonpositive boundary laws have infinite KL. The exact condition is that the positive parts of the closures coincide. | Add "on positive laws". |
| F12 | Prop 7.5 | S3 | The hypothesis an "identifiable even/odd score decomposition" should say what the proof uses: the simple tangent space is invariant under the reflection $Z\mapsto-Z$, i.e., it is the direct sum of its even and odd parts. The last sentence should read "$Zs_v$ has a component orthogonal to the simple odd-score span". | Reword. |
| F13 | Thm 3.1 | S3 | The prior box $\rho\in[1/4,2]$ ($\delta\in[-0.394,0.474]$) differs from the project's minimal contract ($\delta\in[-\tfrac12,\tfrac12]$, $\rho\in[0.053,2.060]$), which the pilot simulations used. The asymptotic theorem is unaffected; finite-sample BF figures are not comparable. | Use the contract box, or state the difference. |
| F14 | Prop 7.7 | E | The cell order $(00,01,10,11)$ differs from the witness order $(00,10,01,11)$. | Harmonize. |
| F15 | Remark 5.3 | E | The claim "$\Lambda\ne0$ is sufficient, not necessary" is correct but unillustrated. Audit check R4 gives a one-line example: $K$: $\mathrm{logit}\,q_t=-\rho^2-\theta x_t$ embeds $S$ at $\rho=0$ with $\partial_\rho\eta=0$, so $\Lambda=0$. Yet it contains the witness's optimal offset, so $\Delta_J=0.000699>0$. The same example illustrates Remark 6.3's singular direction. | Add it. |
| F16 | Prop 7.4 | S3 (omission) | Only $\Delta_J$ is bounded. Since $0\le C_M\le R_M$ (the chain rule subtracts a nonnegative marginal KL), also $\Delta_C\le C_S\le R_S=O(\varepsilon^6)$. Both hierarchical gaps are therefore high order. | Add one line. |

## 3. Result-by-result audit

| Result | Status | Notes |
|---|---|---|
| §1 setting, eqs. (1)–(3) | Correct | Closure formulation and positivity of minimizers are right. See F5 and F8. |
| Lemma 2.1 (mixture, moments, covariance) | Correct | The independent-copy covariance argument is complete. |
| Lemma 2.2 (product reduction) | Correct | Both identities checked on 200 random positive laws (R2; error below $10^{-15}$). $\Delta_C=\Delta_J/T$ holds because projections onto closures of product families are products. |
| Lemma 2.3 (context) | Correct | See F9. |
| Thm 3.1 (witness) | Correct | Recomputed exactly (R1): cells, $3/8$, $3/10$, covariance $1/40$, $R_S=0.0069680830$, $R_K=0.0062695683$, $\Delta_J=0.0006985147$, $\Delta_C=\Delta_J/2$, $\rho^\star_K=0.662697\in[1/4,2]$. Uniqueness of both laws, monotonicity of $\rho\mapsto\delta$ and interiority were verified. See F6 and F13. |
| Thm 4.1 (transfer) | Correct with F1, F3, F5 | The LOO identity (eq. 8) was checked algebraically. The limits hold without nesting. |
| Remark 4.2 | Correct | — |
| Thm 5.1 (drift) | Correct | One-way implication, properly stated. |
| Prop 5.2 (lower bound) | Correct with F7 | Recomputed in the witness on the revised box: step $s=-0.160$, $\theta=0.345$, both feasible; bound $6.42\times10^{-4}\le\Delta_J$. |
| Lemma 6.1 (expansion) | Correct | Previously verified (check E1 of the 2 October verifier: remainder orders 1 and 2). See F10. |
| Thm 6.2 (weighted projection) | Correct conclusion, proof gap F2 | Full column rank of $[J_S,e]$ already implies $\tilde e\ne0$, so the division is valid within the theorem's hypotheses. The formulas match check L1 of the 2 October verifier. |
| Remark 6.3 | Correct (important) | A singular extra direction can affect the leading risk term; R4 is a concrete instance. See F11. |
| Thm 7.1 (hierarchical transfer) | Correct | Inherits F1/F3 from Thm 4.1. |
| Thm 7.2 (regular local hierarchical) | Correct with F4 | **Numerically confirmed at an interior positive-variance baseline** (§6). |
| Remark 7.3 (boundary) | Correct (important) | The zero-variance point is a boundary; Thm 7.2 does not apply there. |
| Prop 7.4 (variance matching) | Correct | A direct comparator bound, so it needs no regularity and is unaffected by the boundary issue. See F16. |
| Prop 7.5 (parity) | Correct with F12 | — |
| Remark 7.6 | Correct | A valid counterexample to the original draft's unstated assumption. |
| Prop 7.7 (reversal) | Correct | Reproduced (R3): $\lambda^\star=0.281900$, $\Delta_J=0.098320$, $\Delta_C=-0.052440$; $R_K=0.374>0$. The derivative changes sign on $(0,1)$ and the objective is strictly convex. |
| Cor 8.1 (context-aware) | Correct with F1 | The hypercube argument is valid. If all full conditionals of two positive laws agree, the ratio $p/q$ is constant across edges, hence across the connected hypercube, so $p=q$. R5 confirms that the conditional risk is a positive fraction (at least 0.32 in 300 random trials) of the joint risk. |

## 4. Numerical reproduction

| Quantity | Revision | Independent recomputation |
|---|---|---|
| $\theta_S^\star$ | 0.4429045138 | **0.4429045203** (F6) |
| $R_S$; $R_K$ | 0.0069680830; 0.0062695683 | 0.0069680830; 0.0062695683 |
| $\Delta_J$; $\Delta_C$ | 0.0006985147; 0.0003492573 | 0.0006985147; 0.0003492573 |
| $\rho_K^\star$ | 0.662697 | 0.662697 |
| Prop 7.7: $\lambda^\star$, $\Delta_J$, $\Delta_C$ | 0.281900, 0.098320, −0.052440 | 0.281900, 0.098320, −0.052440 |

## 5. Accuracy of the change log ("Corrections to the 2 October draft")

The change log will likely be read by collaborators, so it should describe the original draft accurately.

| Item | Assessment |
|---|---|
| 1. Closure and attainment | **Inaccurate.** The original Lemma 2.1 already stated that $R_M$ is "attained on $\overline{\mathcal Q}_M$" and that "$R_M>0$ iff $p\notin\overline{\mathcal Q}_M$", and defined $R_M$ as an infimum over $\mathcal Q_M$. Nothing needed correcting here. (The handoff note's claim that the original asserted attainment *in the family* is likewise not borne out by the text.) |
| 2. Marginal shape | Fair. The original Cor. 1.5 said the marginal curve "is not of the kernel's form" without noting possible absorption by other simple-model parameters. |
| 3. Drift | Partly fair. Original Thm 2.4 was already a one-way implication, but its Remark 1 overstated it ("occurs exactly when"). |
| 4. Gap bound | Partly fair. The original Prop 2.5 assumed an interior projection and step feasibility; positive-definite nuisance information was implicit. |
| 5. Regular local geometry | Fair in substance. The original Thm 2.6 assumed H1–H2, but Theorem 0(b) said "any regular candidates" without flagging the zero-variance boundary. |
| 6. Tangent absorption | **Fair.** The original said "no gap for any context law" and "wins iff", which overstated a leading-order statement. |
| 7. Higher moments | Partly fair. The moment conditions were in the original Thm 1.4 but not restated in Prop 4.3. |
| 8. Parity | **Fair and important.** The original proof assumed a Z-even extra score without stating it. |
| 9–11 | Fair. |

## 6. Readiness for the hierarchical extension

**What is solid.** Theorem 7.1 (transfer, given the two gaps) and Theorem 7.2 (local formulas at an interior, regular baseline) are correct, subject to F1, F3 and F4. Propositions 7.4–7.5 correctly limit where an advantage can come from. Check R6 tested Theorem 7.2 directly in a genuinely hierarchical setting:

- **Design:** $T=3$, logits $\kappa_t-\beta_t\theta$ with $\kappa=(0.3,-0.2,0.1)$ and $\beta=(1,2,3)$.
- **Simple model $S$:** a normal random effect $(\mu,\log\sigma^2)$ at the interior baseline $\sigma^2=0.5$.
- **Complex model $K$:** $S$ plus one global parameter with logit signature $(0.5,-0.3,0.8)$.
- **Truth:** a skewed latent law $\theta=\mu+\sigma\{E+\lambda(E^2-1)\}$, $E\sim N(0,1)$.

Exact global KL projections were computed by quadrature and Newton's method:

| $\lambda$ | $R_S$ / formula | $R_K$ / formula | $\Delta_J$ / formula | $\Delta_C$ / formula |
|---:|---:|---:|---:|---:|
| 0.08 | 1.002 | 1.002 | 8.14 | 3.03 |
| 0.04 | 1.003 | 1.003 | 3.68 | 1.98 |
| 0.02 | 1.002 | 1.002 | 2.12 | 1.48 |
| 0.01 | 1.001 | 1.001 | 1.50 | 1.24 |
| extrapolated to 0 | — | — | **1.002** | **0.999** |

**Three lessons for the extension.**

1. **The leading coefficient can be tiny.** Here $\lVert d\rVert^2/\lVert r_S\rVert^2=3\times10^{-5}$: the extra parameter is almost orthogonal to a skewness perturbation. Next-order terms then dominate the gap until the perturbation is very small; at $\lambda=0.01$ the true gap is still 50% above the leading-order prediction. *The local formula is a guide for choosing a construction, not a certificate.* Any hierarchical witness should be certified by direct global computation (exact projections with error control) or by a nonasymptotic bound, not by the sign of $\lVert d\rVert$ or $L$ alone.
2. **The conditional gap is unconstrained in both directions.** Here $L>0$, and the trial-conditional gap per trial is about 21 times $\Delta_J/T$. In Prop 7.7 it has the opposite sign. For hierarchical models, $\Delta_C$ must be computed, not inferred.
3. **Work at a positive-variance baseline.** By Prop 7.4 plus F16, perturbing around the zero-variance point gives gaps of order $\varepsilon^6$ or smaller in both targets, and Thm 7.2 does not apply there anyway. The natural route matches the revision's recommendation:
   - start from an interior hierarchical law;
   - add a perturbation the normal working family cannot absorb (skew or bimodality of the context mixture, or asymmetric heteroskedasticity across $Z$, respecting Prop 7.5);
   - choose a design, such as the eight-trial calibrated design, on which the distortion signature has a sizeable partial alignment with that perturbation;
   - certify $0<R_K<R_S$ and $\Delta_C>0$ by exact global computation.

## 7. Recommended next actions

1. **Apply F1–F2** (one-line hypothesis change; re-derive Thm 6.2 from Thm 7.2), then F3–F5 (appendix and definitions). Make the minor edits F6–F16 and correct change-log items 1, 3, 4 and 7.
2. **Then begin the hierarchical construction** along the route in §6, using check R6's code as the starting harness. It already computes exact hierarchical projections, the local coefficients $d$ and $L$, and both gaps.
