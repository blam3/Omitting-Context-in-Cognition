# L3 KL Dominance Bridge

> **Status:** Statement-and-proof draft for backlog item T-004. It is not
> accepted for manuscript use and does not promote C-004 beyond `planned`.
> Two new assumptions (A-009, A-010) are proposed and decision-gated. The
> draft deliberately reaches a *negative-sounding* structural conclusion about
> the scientific weight of Result 3; see §6.

## 1. Objects & Notation

### 1.1 The comparison unit

Every divergence in this document is defined at a **declared comparison
unit**. This is not decoration. The proof-critic review of Lemma 1.1
(`docs/proofs/reviews/L1_mixture_lemma_claude_review.md`, finding F2)
established that the mixture lemma is a *per-trial* identity and that the
within-participant joint law does not factor into a product of trial-level
marginals:

$$\int \prod_t p(y_t \mid x_t,\theta;\eta^*)\, dF(\theta) \;\neq\; \prod_t \int p(y_t \mid x_t,\theta;\eta^*)\, dF(\theta).$$

Accordingly, let the comparison unit be written generically as $O=(W,V)$,
where $W$ is the modeled response and $V$ the conditioning covariates. Two
instantiations are admissible:

| Unit | $W$ | $V$ | Target law $p_0(w\mid v)$ |
|---|---|---|---|
| Trial | $Y_{it}$ | $(X_{it},Z_i)$ | Lemma 1.1: $\int p(y\mid x,\theta;\eta^*)\,dF_{\Theta\mid X,Z}(\theta\mid x,z)$ |
| Participant | $Y_{i,1:T_i}$ | $(X_{i,1:T_i},Z_i)$ | joint mixture $\int \prod_t p(y_{it}\mid x_{it},\theta;\eta^*)\,dF_{\Theta_i\mid X_i,Z_i}(\theta\mid x_i,z_i)$ |

The participant-level row is the object that finding F2 says must be derived
from Lemma 1.1 rather than assumed. That derivation is **not** performed here;
this document takes whichever $p_0$ the declared unit supplies as given, and
its results hold for either instantiation.

Let $P_V$ denote the covariate/design distribution over $V$ in the target
population, and $P_0$ the joint law of $(W,V)$ with conditional density $p_0$.
Because choices are binary or multinomial and $T_i$ is finite, $W$ has finite
support at both units, so the finite-outcome hygiene noted in §7 of the
mixture-lemma draft carries over unchanged.

### 1.2 Model classes

Three classes of *conditional* models for $W$ given $V$:

- $\mathcal M_S=\{q_\eta(\cdot\mid\cdot):\eta\in H_S\}$, the **context-omitting
  simple** class ($M1$ in the empirical ladder);
- $\mathcal M_K=\{q_\psi(\cdot\mid\cdot):\psi\in H_K\}$, the **context-omitting
  complex** class ($M4$);
- $\mathcal M_{S+C}=\{q_\phi(\cdot\mid\cdot):\phi\in H_{S+C}\}$, the
  **context-aware simple** class ($M2$/$M3$), defined here only because §7
  shows it is needed by the project thesis and is absent from the current
  theorem route.

Members of $\mathcal M_S$ and $\mathcal M_K$ condition only on $V$, which
excludes $C$. Neither class is assumed to contain $p_0$; both are misspecified
in general, which is exactly why pseudo-true quantities are required.

### 1.3 Risk and divergence

$$D(q):=\mathbb E_{V}\big[\mathrm{KL}\big(p_0(\cdot\mid V)\,\big\|\,q(\cdot\mid V)\big)\big],\qquad
R(q):=-\,\mathbb E_{(W,V)}\big[\log q(W\mid V)\big],$$

$$H:=-\,\mathbb E_{(W,V)}\big[\log p_0(W\mid V)\big],\qquad
\delta_S:=\inf_{\eta\in H_S} D(q_\eta),\qquad \delta_K:=\inf_{\psi\in H_K} D(q_\psi).$$

$D$ is the expected *conditional* divergence, $R$ the expected negative log
score (cross-entropy risk), and $H$ the conditional entropy of the target law.
Write $\Delta\ell:=\delta_S-\delta_K$.

## 2. Assumptions Used

1. **Lemma 1.1 (T-001), at the declared unit.** The target $p_0$ is the
   omitted-context marginal law. T-001 is itself in proof-critic revision
   (findings F1, F2), so every result below inherits that status.

2. **A-009, common comparison unit and design distribution (proposed,
   decision-gated).** $\mathcal M_S$, $\mathcal M_K$, and $\mathcal M_{S+C}$
   are evaluated at the same declared comparison unit, against the same target
   law $p_0$, under the same covariate distribution $P_V$, and $P_V$ is the
   distribution of the population to which the scientific claim generalizes.

3. **A-010, kernel non-degeneracy (proposed, decision-gated).** There exist
   $\epsilon\in(0,1/2)$ and a finite $T_{\max}$ such that every *per-trial*
   choice probability — under $p_0$ and under every candidate model used in the
   comparison — lies in $[\epsilon,1-\epsilon]$ for $P_V$-almost every $v$, and
   no participant contributes more than $T_{\max}$ trials. The bound is imposed
   on the trial-level kernel rather than on the unit-level density, because at
   the participant unit the response has $2^{T_i}$ support points and its
   probabilities cannot all exceed a fixed $\epsilon$. It follows that the
   unit-level log densities are uniformly bounded,
   $|\log q(w\mid v)|\le B:=T_{\max}\log(1/\epsilon)$, with $T_{\max}=1$ at the
   trial unit. This makes $H$, $R$, and $D$ finite and makes differences between
   them well defined.

4. **Standard results.** Linearity of expectation; Fubini for bounded
   integrands; Gibbs' inequality ($\mathrm{KL}\ge 0$, with equality iff the
   laws agree); and, for Proposition L3.4 only, dominated convergence to
   exchange $\nabla_\psi$ with $\mathbb E_{P_0}$.

No assumption about *which* model is mechanistically true is used anywhere
below. No Gaussian, KL-of-normals, or heteroskedasticity assumption is used;
L2 is not a prerequisite for L3.

## 3. Formal Statement

### Proposition L3.1 (risk–divergence decomposition)

Under A-009 and A-010, $H$ is finite and does not depend on the candidate
model, and for every candidate $q$ in any of the three classes,

$$D(q)=R(q)-H .$$

Consequently, for any two candidates $q_1,q_2$: $\;D(q_1)-D(q_2)=R(q_1)-R(q_2)$.

### Theorem L3.2 (KL dominance is the population log-score gap)

Under A-009 and A-010,

$$\Delta\ell \;=\; \delta_S-\delta_K \;=\; \sup_{\psi\in H_K}\mathbb E_{P_0}\big[\log q_\psi(W\mid V)\big]\;-\;\sup_{\eta\in H_S}\mathbb E_{P_0}\big[\log q_\eta(W\mid V)\big].$$

In particular $\delta_K<\delta_S$ **if and only if** the complex class attains
a strictly larger supremal expected log likelihood per declared unit, and the
common value of the two sides is exactly the quantity called "expected
per-observation log-score advantage" in the finite-sample threshold corollaries
(T-007).

### Proposition L3.3 (under nesting, dominance is automatic — and therefore weak)

Suppose there is a map $\iota:H_S\to H_K$ with $q_{\iota(\eta)}=q_\eta$ for
every $\eta\in H_S$, i.e. $\mathcal M_S\subseteq\mathcal M_K$. Then

$$\delta_K\le\delta_S,\qquad\text{equivalently}\qquad \Delta\ell\ge 0,$$

and this holds **for every target law $p_0$ whatsoever** — with or without
omitted context, with or without a context effect on $\Theta$.

### Proposition L3.4 (a checkable sufficient condition for *strict* dominance)

Assume A-009, A-010, and the nesting of Proposition L3.3. Assume further that
$\delta_S$ is attained at some $\eta^\dagger\in H_S$; that
$H_K\subseteq\mathbb R^{k_K}$ with $\iota(\eta^\dagger)$ in its interior; and
that $\psi\mapsto\mathbb E_{P_0}[\log q_\psi(W\mid V)]$ is differentiable at
$\iota(\eta^\dagger)$ with derivative obtained by exchanging $\nabla_\psi$ and
$\mathbb E_{P_0}$. Define the population score of the complex class at the
embedded pseudo-true simple model,

$$s^\dagger:=\nabla_\psi\,\mathbb E_{P_0}\big[\log q_\psi(W\mid V)\big]\Big|_{\psi=\iota(\eta^\dagger)} .$$

If $s^\dagger\neq 0$, then $\delta_K<\delta_S$ strictly.

Moreover the components of $s^\dagger$ tangent to $\iota(H_S)$ vanish, so
$s^\dagger\neq0$ holds if and only if the **extra-parameter block** of the
score has nonzero mean under $p_0$:

$$\mathbb E_{P_0}\Big[\nabla_{\psi_{\mathrm{extra}}}\log q_\psi(W\mid V)\Big|_{\iota(\eta^\dagger)}\Big]\neq 0 .$$

The condition $s^\dagger\ne 0$ is **sufficient but not necessary**: strict
dominance can also arise from second- or higher-order improvement when
$s^\dagger=0$.

### Corollary L3.5 (what L3 does and does not hand downstream)

Under A-009 and A-010:

1. **To T-007 (AIC/BIC bridge).** The symbol $\Delta\ell$ in the thresholds
   $2n\,\Delta\ell>2(k_K-k_S)$ and $2n\,\Delta\ell>(k_K-k_S)\log n$ is
   $\delta_S-\delta_K$ *at the declared unit*, and $n$ counts **units of that
   declared type** — participants, not trials, whenever the participant unit is
   declared. The thresholds additionally require independence across units and
   the usual maximized-likelihood asymptotics; they compare a population
   quantity to a finite-sample penalty and remain heuristic bridges.
2. **To T-005 (LOOIC).** $\Delta\ell>0$ does **not** imply
   $\Delta\mathrm{elpd}_{\mathrm{LOO}}>0$. The elpd of a Bayesian model is an
   expected *posterior predictive* log density, not the plug-in log density at
   a pseudo-true parameter; the two agree only asymptotically under regularity,
   and differ in finite samples by effective-complexity terms that penalize
   $\mathcal M_K$ precisely because it is larger. T-005 must be derived
   separately.
3. **To T-006 (Bayes factors).** $\Delta\ell>0$ does **not** imply
   $\log\mathrm{BF}_{K,S}>0$. A marginal likelihood integrates over the prior
   and carries an Ockham factor that penalizes $\mathcal M_K$'s larger
   parameter space; the sign can invert for any $\Delta\ell>0$ under a
   sufficiently diffuse prior on the extra parameters. T-006 must be derived
   separately.

Items 2 and 3 give the mathematical reason for the repository's existing rule
that LOOIC and Bayes-factor results may not be inferred from the KL bridge.

## 4. Proof

### 4.1 Proposition L3.1

Fix $v$ in the support of $P_V$. Since $W$ has finite support,

$$\mathrm{KL}\big(p_0(\cdot\mid v)\,\|\,q(\cdot\mid v)\big)
=\sum_{w} p_0(w\mid v)\log p_0(w\mid v)\;-\;\sum_{w} p_0(w\mid v)\log q(w\mid v).$$

By A-010 every $\log$ term is bounded in absolute value by
$B=T_{\max}\log(1/\epsilon)$, uniformly in $v$ and in the candidate, so both
sums are bounded uniformly in $v$ and both are $P_V$-integrable. Taking
$\mathbb E_{P_V}$ and applying Fubini to each bounded sum separately gives

$$D(q)=\mathbb E_{P_V}\Big[\sum_w p_0(w\mid v)\log p_0(w\mid v)\Big]
-\mathbb E_{P_V}\Big[\sum_w p_0(w\mid v)\log q(w\mid v)\Big]=-H+R(q),$$

where the second equality uses the tower property, $\mathbb E_{P_0}[g(W,V)]
=\mathbb E_{P_V}\big[\sum_w p_0(w\mid V)g(w,V)\big]$, applied to
$g=\log p_0$ and $g=\log q$. Both $H$ and $R(q)$ are finite by the same
bound, and $H$ involves only $p_0$, hence does not depend on $q$. The
difference statement follows by subtraction, the finite $H$ cancelling. $\square$

### 4.2 Theorem L3.2

By Proposition L3.1, $D(q_\eta)=R(q_\eta)-H$ for every $\eta\in H_S$, and $H$
is a finite constant, so

$$\delta_S=\inf_{\eta\in H_S}\big(R(q_\eta)-H\big)=\Big(\inf_{\eta\in H_S}R(q_\eta)\Big)-H,$$

and identically $\delta_K=\big(\inf_{\psi}R(q_\psi)\big)-H$. Subtracting, the
$H$ terms cancel:

$$\delta_S-\delta_K=\inf_{\eta}R(q_\eta)-\inf_{\psi}R(q_\psi).$$

Since $R(q)=-\mathbb E_{P_0}[\log q(W\mid V)]$, we have
$\inf_q R(q)=-\sup_q \mathbb E_{P_0}[\log q(W\mid V)]$, which gives the stated
identity. The "if and only if" is immediate because the two sides are equal, and
both infima are finite by A-010. $\square$

### 4.3 Proposition L3.3

For every $\eta\in H_S$, $q_{\iota(\eta)}=q_\eta$, hence
$D(q_{\iota(\eta)})=D(q_\eta)$. Therefore
$\{D(q_\psi):\psi\in H_K\}\supseteq\{D(q_\eta):\eta\in H_S\}$, and the infimum
over a superset is no larger:

$$\delta_K=\inf_{\psi\in H_K}D(q_\psi)\;\le\;\inf_{\eta\in H_S}D(q_\eta)=\delta_S.$$

No property of $p_0$ was used. $\square$

### 4.4 Proposition L3.4

Write $L(\psi):=\mathbb E_{P_0}[\log q_\psi(W\mid V)]$, finite by A-010. By
Theorem L3.2 it suffices to show $\sup_\psi L(\psi)>\sup_\eta L(\iota(\eta))=
L(\iota(\eta^\dagger))$, the equality holding because $\eta^\dagger$ attains
$\delta_S$ and $D(q_\eta)=-L(\iota(\eta))+H$.

Suppose $s^\dagger\neq0$. Since $\iota(\eta^\dagger)$ is interior and $L$ is
differentiable there, for $\varepsilon>0$ small enough that
$\iota(\eta^\dagger)+\varepsilon s^\dagger\in H_K$,

$$L\big(\iota(\eta^\dagger)+\varepsilon s^\dagger\big)
= L\big(\iota(\eta^\dagger)\big)+\varepsilon\,\|s^\dagger\|^2+o(\varepsilon).$$

Because $\|s^\dagger\|^2>0$, the right-hand side strictly exceeds
$L(\iota(\eta^\dagger))$ for all sufficiently small $\varepsilon>0$. Hence
$\sup_\psi L(\psi)>L(\iota(\eta^\dagger))=\sup_\eta L(\iota(\eta))$, and
Theorem L3.2 yields $\delta_K<\delta_S$.

For the block characterization: $\eta^\dagger$ maximizes $\eta\mapsto
L(\iota(\eta))$ over $H_S$. If $\eta^\dagger$ is interior in $H_S$ and
$\iota$ is a differentiable embedding, the chain rule gives
$0=\nabla_\eta L(\iota(\eta))|_{\eta^\dagger}=D\iota(\eta^\dagger)^{\!\top}s^\dagger$,
so $s^\dagger$ annihilates the tangent space of $\iota(H_S)$. In the
coordinates in which $\psi=(\eta,\psi_{\mathrm{extra}})$ and $\iota(\eta)=
(\eta,0)$, this says the first block of $s^\dagger$ vanishes, so
$s^\dagger\ne0$ is equivalent to a nonzero extra-parameter block. $\square$

### 4.5 Remark: L3.4 is computable without fitting the complex model

The quantity $\mathbb E_{P_0}[\nabla_{\psi_{\mathrm{extra}}}\log q_\psi]$ at
$\iota(\eta^\dagger)$ is the population version of a score (Lagrange-multiplier)
statistic. In the simulation track it can be estimated by simulating from the
DGM, fitting only $\mathcal M_S$, and averaging the complex model's
extra-parameter score at the embedded simple fit. No fit of $\mathcal M_K$ is
required. This gives the simulation track a cheap, theorem-aligned screen for
which false-complex parameterizations are even capable of dominating.

## 5. Boundary Conditions, Stated Formally

The project's boundary-case list maps onto L3 as follows.

| Project boundary case | Formal counterpart in L3 |
|---|---|
| 1. $C$ has no effect on $\Theta$ ($\gamma=0$) | See the correction below — this does **not** by itself give $\Delta\ell=0$. |
| 2. $C$ adds only correctly modeled iid noise | If the induced $p_0$ lies in $\mathcal M_S$, this is case 3. |
| 3. $\mathcal M_S$ already represents the marginal law | $p_0\in\mathcal M_S\Rightarrow\delta_S=0$; with nesting, $\delta_K=0$ too, so $\Delta\ell=0$ and no dominance. |
| 4. $\mathcal M_K$ does not approximate the mixture better | $\Delta\ell=0$; a sufficient local witness of its failure is $s^\dagger\neq0$ (L3.4). |
| 5. Penalties dominate in finite samples | Not an L3 statement at all; $\Delta\ell>0$ with $2n\Delta\ell$ below the penalty. Lives entirely in T-007. |

**Correction to boundary case 1.** Setting $\gamma=0$ removes the
*context-induced* component of the mixing distribution, but $F_{\Theta\mid X,Z}$
generally remains non-degenerate because of $U$. The target $p_0$ is then still
a mixture, and $\Delta\ell>0$ remains possible from ordinary unmodeled
individual heterogeneity. What $\gamma=0$ removes is the *attribution* of any
dominance to omitted context, not dominance itself. The current phrasing of
boundary case 1 in `docs/current_project_context.md` and
`docs/theorem_backlog.md` is therefore stronger than what L3 supports and
should be narrowed when those files are next revised.

## 6. What This Result Does Not Establish — and a Framing Consequence

Theorem L3.2 is an identity, not a discovery. Its content is bookkeeping: it
fixes the precise sense in which "KL dominance" and "population log-score
advantage" are the same statement, and it pins down the object $\Delta\ell$
that T-005, T-006, and T-007 each consume differently.

Proposition L3.3 carries the uncomfortable structural consequence. **If the
false-complex model $M_K$ nests the simple model $M_S$ — which is how the
empirical ladder currently reads, with $M4$ adding source/colour/condition and
nonlinear ambiguity terms to $M1$ — then $\Delta\ell\ge0$ holds automatically,
for any data-generating process, with no reference to omitted context at all.**
Under nesting, the *sign* of the KL gap is not evidence for the OCECM thesis
and should not be presented as a theorem about context omission.

Two consequences follow for the paper:

1. The scientific weight of the theorem package cannot rest on Result 3. It
   must rest on (a) the *magnitude* of $\Delta\ell$ and its dependence on the
   omitted-context mixture, and (b) the finite-sample and Bayesian criteria in
   T-005/T-006/T-007, where the penalty terms make the comparison non-trivial.
2. If instead $M_K$ is genuinely **non-nested** with respect to $M_S$ (a
   different cognitive architecture rather than an elaboration of the same
   one), then $\delta_K<\delta_S$ is a substantive claim, Proposition L3.3 does
   not apply, and Proposition L3.4 is unavailable as stated. A separate
   sufficient condition would be required, most plausibly constructed from the
   L2 Gaussian mixture. That construction is not attempted here.

Whether the empirical $M_K$ nests $M_S$ is therefore a modelling decision with
direct consequences for what the theorem package can claim. It is raised as
this cycle's decision gate.

## 7. Counter-Example Candidates

- **CE-1: dominance without any omitted context (succeeds; limits the claim).**
  Let $C\equiv0$, so nothing is omitted, but let the true kernel contain a
  trial-level nonlinearity that $\mathcal M_S$ cannot represent and
  $\mathcal M_K$ can. Then $\Delta\ell>0$. KL dominance is thus **not**
  diagnostic of context omission: an observed complex-model win is consistent
  with plain misspecification of the trial-level kernel. Any empirical
  demonstration must separate these two sources, and the manuscript must not
  read $\Delta\ell>0$ as evidence of omitted context.

- **CE-2: the thesis needs a comparison L3 does not make (succeeds; scope
  gap).** Claim C-001 asserts that a simpler *context-aware* model is the
  better mechanistic explanation. L3 compares only $\mathcal M_S$ against
  $\mathcal M_K$. Nothing here rules out $\delta_{S+C}<\delta_K$, nor
  establishes it. The theorem backlog contains no item for the
  $\mathcal M_{S+C}$ versus $\mathcal M_K$ contrast even though
  `docs/bayesian_comparison_plan.md` lists it as the second empirical
  contrast. A new backlog item (T-008) is proposed to close this asymmetry.

- **CE-3: non-attainment (limits L3.4, not L3.2).** If $H_S$ is open or
  unbounded and the infimum $\delta_S$ is not attained — e.g. choice
  sensitivity drifting to the boundary — there is no $\eta^\dagger$ and the
  first-order argument of L3.4 is unavailable. Theorem L3.2 is stated with
  infima and survives; L3.4 carries attainment as an explicit hypothesis.

- **CE-4: infinite divergence (motivates A-010).** If the per-trial kernel is
  allowed to approach $0$ or $1$ (deterministic choice in the limit of large
  sensitivity), $D(q)$ can be infinite for some candidates and differences of
  infima become ill-defined. A-010 excludes this. Note that the bound must be
  placed on the per-trial kernel and paired with a finite trial cap: at the
  participant unit the response has $2^{T_i}$ support points, so a bound of the
  form $[\epsilon,1-\epsilon]$ on the *unit-level* density is unsatisfiable for
  $T_i$ large and would make A-010 vacuous rather than restrictive. Without a
  correctly placed bound, Theorem L3.2 is false as an identity.

- **CE-5: unit substitution (motivates A-009).** Computing $\delta_S$ at the
  trial unit and $\delta_K$ at the participant unit produces a difference with
  no interpretation, since the entropies $H$ differ and do not cancel. A-009
  forbids this.

## 8. Need for New Assumptions?

Yes — two, both proposed and decision-gated, recorded in
`docs/proposed_assumptions.md` and `registries/assumption_register.csv`:

1. **A-009**, common comparison unit and design distribution. Load-bearing for
   Theorem L3.2 (CE-5).
2. **A-010**, kernel non-degeneracy. Load-bearing for Propositions L3.1 and
   L3.4 and Theorem L3.2 (CE-4).

The strictness condition $s^\dagger\neq0$ of Proposition L3.4 is deliberately
**not** registered as a project assumption. It is a hypothesis of one
proposition, checkable per data-generating process, not a standing modelling
commitment of the project; registering it would misrepresent a conditional
result as an adopted belief. This follows the distinction drawn in finding N6
of the L1 proof-critic review between load-bearing and interpretive entries.

No claim-registry status is promoted by this draft. C-004 remains `planned`.

## 9. Next Proof Actions

1. Obtain the PI decision on whether $M_K$ nests $M_S$ (§6).
2. Send L3 for proof-critic review, together with T-001's revision, since
   L3 consumes whatever $p_0$ the revised Lemma 1.1 supplies.
3. If the participant unit is selected as primary, derive the participant-level
   joint-mixture target from Lemma 1.1 (L1 review finding F2) before L3 can be
   instantiated at that unit.
4. If $M_K$ is non-nested, draft a separate sufficient condition for
   $\delta_K<\delta_S$ built on the L2 Gaussian mixture.
5. Consider opening T-008 for the $\mathcal M_{S+C}$ versus $\mathcal M_K$
   contrast that claim C-001 requires (CE-2).
