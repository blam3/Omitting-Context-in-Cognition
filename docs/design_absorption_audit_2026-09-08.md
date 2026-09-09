# Full-support nuisance-absorption audit

## Claim

Audit the exact G1 matched candidates on every currently specified design-support point before another separation construction. Give a reusable criterion for the same pointwise normal-effect reparameterization, including its positive-sensitivity restriction. Do not remove shared terms, introduce a new winning design, or infer observable separation from failed absorption.

## Status

PROVABLE AS STATED for the scoped algebraic audit below.
Verification: Verified (author derivation and local checks only; not independent review or PI acceptance).

The only complete primary support in the repository is the two-trial common design crossed with $Z=-1,+1$. Its full support is absorbed for every $\rho>0$. There is no complete richer primary or empirical RAID support on which to issue a further pass/fail verdict. That input limitation is not filled by the GLM scaffold or single-level Stan model. Strict separation remains unproved; P-G3 remains a conditional proposal with unchanged approval status.

## Assumptions and scope inventory

This audit preserves G1's free intercept, side coefficient, global positive sensitivity, ambiguity mean intercept and Z slope, and positive normal shared-effect SD. It uses the existing full parameter supports and $\rho>0$; no compact boxes, fixed effects, new priors or Gaussian truth restrictions are adopted.

| Source | Full-support readiness | Audit disposition |
|---|---|---|
| `primary_separation_attempt_2026-09-08.md`, L1/L2 | Two common trials, $Z=\pm1$ each with probability 1/2; both lotteries and side specified | Fully enumerated in `registries/primary_design_support.csv`; all-rho absorption proved below |
| `primary_theorem_specification.md` | Defines a class of possible designs, not another particular support | Functional criterion below applies when a support is supplied; no blanket absorption verdict |
| `raid_variable_coding_memo.md` | Option alignment, other-lottery probability/payoff, side codes and loss availability remain unresolved | Cannot reconstruct $d_\rho,b,s$ or support completeness; no empirical rank or identifiability verdict |
| `R/dgm.R`, `R/generate_synthetic_raid_data.R` | Proxy has probability/value/ambiguity and other scaffold fields, but no validated two-lottery G1 mapping | Do not infer the missing lottery or transfer its continuous input ranges to G1 |
| `stan/simple_ambiguity_single_level.stan` | One-value, single-level model with different restrictions | Not the exact shared-effect S/K pair; cannot stand in for its design audit |

The CSV is a transcription of the prior attempt, not a newly chosen design. A row is a pair $(W,t)$, not an independent observation. `support_probability` is the probability of the entire W vector, repeated per trial; sum it once per `support_id`. Both boundary and finite-context attempts use this same support. Their different C laws do not change this design audit.

## Notation

Let $\mathcal S=\{(W,t):W\in\operatorname{supp}(W),1\leq t\leq T\}$, with equality on its actual support (or almost surely for a general random design). Stack every supported row, including all Z values and all stimulus/side assignments that can occur. Define

$$b=v_AA/2,\quad d_r=v_Aw(p_A;r)-v_Rw(p_R;r),\quad D=[\mathbf1,s,b,bZ].$$

Columns denote functions on the entire support; on a finite support they are vectors. All coefficients below are global constants, not per participant, per Z or per trial. Denote the nuisance span by $\mathcal N=\operatorname{span}\{1,s,b,bZ\}$ and use $[v]$ for its quotient class. Shared-effect logits are

$$\eta_r(E)=\alpha+\beta s+\tau d_r-\tau b(\mu_0+\mu_1 Z+\sigma E),\qquad E\sim N(0,1).$$

## Verification Target and Bottleneck

The target is the functional equation $d_r=c d_1+Dh$ with one $c>0$ and one $h$ on all of $\mathcal S$. Matching separate blocks with different coefficients is insufficient. The current support satisfies this equation for every r, so it cannot furnish a strict gap. The next empirical/richer-design audit requires a complete support manifest; a rho grid cannot supply that missing input.

## Anchors and Borrowing

Self-contained finite-dimensional linear algebra and direct substitution in the G1 logit. The parameter map extends the already recorded L2 calculation into an explicit support-wide test. No new selection theorem, external citation, posterior limit or benchmark result is imported.

Implicit machinery disclosure: a quotient vector space, elementary column rank, orthogonal projection for numerical diagnostics, and injectivity of the logistic function. The observable conclusion follows by integrating identical conditional products against the same standard-normal draw. No claim of identifiability of a general finite mixture is implicit.

## Dependency Map

1. L1 proves the positive-scaling quotient criterion for pointwise absorption (O1).
2. L2 proves the finite-support diagnostic and its limits (O2).
3. L3 evaluates the full existing support analytically for every r (O3).
4. L4 defines what the local tangent test and missing-support inventory do and do not establish (O4).

## Obligation Ledger

- O1 Positive-scale pointwise criterion — CLOSED-LOCAL. Closed at: L1 coefficient comparison and parameter substitution.
- O2 Full-support quotient/rank test — CLOSED-LOCAL. Closed at: L2 quotient cases including zero and negative scale.
- O3 Existing four-row all-rho audit — CLOSED-LOCAL. Closed at: L3 global intercept/side representation and exact ranks.
- O4 Tangent and observable-scope boundaries — CLOSED-LOCAL. Closed at: L4 differentiation and distinction between pointwise and integrated laws.

## Proof

### L1. Preserve all shared terms in the absorption map

For a fixed r, suppose $d_r=c d_1+h_0+h_s s+h_b b+h_z bZ$ everywhere on the support, with $c>0$. For any K parameter choose

$$\tau_S=c\tau_K,\quad\alpha_S=\alpha_K+\tau_Kh_0,\quad\beta_S=\beta_K+\tau_Kh_s,$$
$$\mu_{0S}=(\mu_{0K}-h_b)/c,\quad\mu_{1S}=(\mu_{1K}-h_z)/c,\quad\sigma_S=\sigma_K/c.$$

Substitution yields identical logits for every supported row and every E. In particular $\tau_S\sigma_S=\tau_K\sigma_K$: dispersion was transformed, not dropped or fixed. All transformed parameters remain in their original supports. The integrated participant-vector laws therefore agree. If the condition holds for every r, reverse nesting at r=1 gives $\mathcal Q_K=\mathcal Q_S$.

Conversely, if two parameter sets have identical logits for all supported rows and the same E, set $c=\tau_S/\tau_K>0$. Comparing constant-in-E terms gives precisely $d_r-cd_1\in\mathcal N$. If at least one supported $b\ne0$, comparison of the E coefficient also forces $\sigma_S=\sigma_K/c$. If every b is zero the SD is unobservable; the same displayed map still suffices. Thus the criterion is necessary and sufficient for this pointwise representation, not asserted necessary for equality of integrated response laws under every possible representation.

Keeping $\sigma$ fixed when rescaling $\tau$ would generally break this identity. Allowing $c\leq0$ would leave the stipulated sensitivity support (and zero c would collapse it). Neither change is permitted.

### L2. Test the quotient, then the orientation

The equation in L1 is equivalent to

$$[d_r]=c[d_1],\qquad c>0.$$

For a finite support let $P_D$ be projection onto the column space of D and put $u=(I-P_D)d_1$, $v=(I-P_D)d_r$.

1. If $u=0$, absorption holds exactly when $v=0$. Any positive c then works because $d_r-cd_1$ lies in the nuisance span.
2. If $u\ne0$, the only possible scale is $c=(u^Tv)/(u^Tu)$. Absorption holds exactly when $v-cu=0$ and $c>0$.

These statements follow by applying $I-P_D$ to the equation and then using its null space. Rank equality of $[D,d_1,d_r]$ and $[D,d_1]$ alone is insufficient: if $u\ne0$ and $v=0$, only c=0 works; if $v=-u$, only c=-1 works. Both fail positive sensitivity despite the rank equality. Rank deficiency within D is permitted and is not repaired by removing a scientifically shared term.

Support probabilities do not change this exact span criterion when every declared point has positive mass. They do affect statistical information and KL objectives. Zero-probability rows are not support. Replicating an identical row does not add a constraint; increasing the number of participants or repetitions cannot repair exact absorption. Auditing each participant or each Z level separately with different coefficients is invalid.

For nonfinite support the same equation is a functional equality. Finite probing can disprove a proposed global map but cannot prove one on an unexamined continuum. Numerical small residuals depend on tolerance, scaling and conditioning; they are diagnostics, not exact all-rho certificates. `audit_design_absorption.py` labels them accordingly and retains the positive-c test.

### L3. Evaluate every row of the current support

Rows ordered as $(Z,t)=(-1,1),(-1,2),(1,1),(1,2)$ give

$$D=\begin{pmatrix}
1&-1&1/8&-1/8\\
1&1&1/4&-1/4\\
1&-1&1/8&1/8\\
1&1&1/4&1/4
\end{pmatrix},\qquad
d_1=(-1/4,1/4,-1/4,1/4)^T.$$

Here $b=3\mathbf1/16+s/16$ and $d_1=s/4$. The columns $1,s,bZ$ are independent: comparing the two Z values at each trial forces the coefficient of bZ to zero, after which the opposite sides force both remaining coefficients to zero. Hence $\operatorname{rank}(D)=\operatorname{rank}([D,d_1])=3$ exactly, despite four stacked rows.

Let $a(r)=w(1/4;r)-w(1/2;r)$ and $e(r)=w(3/4;r)-w(1/2;r)$. For every r>0,

$$d_r=(a,e,a,e)^T=\frac{a+e}{2}\mathbf1+\frac{e-a}{2}s.$$

Thus both quotient vectors vanish for all r, not just for the diagnostic grid. A convenient global map uses c=1, $h_b=h_z=0$,

$$h_0=(a+e)/2,\qquad h_s=(e-a)/2-1/4.$$

These same constants apply to both Z values and all trials. Every shared term remains present. The bZ column does not rescue separation because the distortion offset has no Z dependence on this support. The SD and sensitivity may even remain unchanged in this particular map. Therefore both DGPs from the previous attempt have equal S/K KL infima on their full support, independent of their context distribution.

The numerical script independently checks exact rational ranks and the quotient equations at r=1/4,1/2,1,3/2,3; the analytic expression above is the all-rho certificate. The CSV's four rows exhaust the previously specified W support, including every trial in each W.

### L4. Tangent checks and the limits of this audit

For interior probabilities, differentiating the specified weighting function gives

$$\dot w(p;1)=-p(-\log p)\log(-\log p),$$

and the endpoint derivatives are zero because the endpoint definitions are constant in r. If a differentiable absorption path exists through r=1 with c(1)=1 and h(1)=0, then

$$\dot d_1=c'(1)d_1+Dh'(1)\in\operatorname{span}(D,d_1).$$

Failure of this tangent condition rules out that differentiable pointwise path; satisfaction does not prove a global path or identifiability. A zero derivative can hide higher-order changes, and an isolated r can be absorbed even when nearby values are not. On the current support, the all-rho representation in L3 is stronger than a tangent check and includes the endpoints of the allowed probability domain when relevant.

The quotient criterion is about equality of logits under a common E representation. Finite-trial integration may produce equality by other means, so failure of the criterion is not proof of observable noncontainment. Even observable noncontainment would not establish $0<R_K<R_S$ for a chosen DGP, a unique joint projection, a positive conditional gap, or BF/LOO preference. Those remain distinct obligations. No P-G3 convergence assumption is used in L1–L4.

## Required next input and gate before construction

A further actual-support audit needs a complete stimulus/protocol manifest listing every supported W and its trials, both lottery probabilities/payoffs, ambiguity widths, exact side coding, retained Z support or its declared continuous law, and permitted co-occurrences/randomizations. Supply support probabilities once per W if finite; document exclusions that remove support before inspecting outcomes. Marginal lists of stimulus levels do not establish which combinations occur. An observed finite sample is not automatically the population support.

Keep the existing gain-only scope; empirical gain/loss extensions require their own validated kernel and shared domain terms. If more shared nuisance columns are later specified, append them to D and repeat the audit rather than omitting them to obtain rank. The current scaffold's source/color terms are not silently added to, or substituted for, G1.

No new separation construction is made here. The current support is ruled out by exact absorption. A future support must first have its completeness documented, then receive an all-rho analytic audit or a precisely bounded nonabsorption result. If it escapes this pointwise obstruction, the next step is an observable-law audit, not automatic separation. P-G3 and all live assumption/claim approval statuses remain unchanged.

## Verification Checks

- Localization/expansion: no likelihood expansion; the optional derivative test is explicitly local and not used for the global conclusion.
- Norm/mode: exact functional/vector equality is distinguished from finite floating-point residual checks.
- Good events and asymptotic rates: not applicable; deterministic algebra only.
- Quantifiers: constants are global across all supported W and t; all-rho proof supplied only for the existing complete support.
- Citation and applicability: no source-specific theorem imported; standard linear algebra and direct substitution only.
- Negligibility: not applicable; no asymptotic remainder.
- Boundary/singularity: zero/negative c rejected; rank-deficient nuisance columns retained; b=0 case stated; shared dispersion rescaled correctly.
- Scientific status: no new design, prior, P-G3 approval, accepted theorem or final claim.
