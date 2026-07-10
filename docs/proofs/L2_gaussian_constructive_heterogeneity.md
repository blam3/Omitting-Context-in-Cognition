# L2 Gaussian Constructive Heterogeneity

> **Status:** Conditional proof draft. The moment lemma is decision-gated by
> A-003 and proposed A-007; the distributional corollary is additionally
> decision-gated by proposed A-008. This file does not promote C-003 or support
> manuscript use before those decisions and proof review.

## 1. Objects & Notation

Let $i$ be an arbitrary participant index. Let
$(\Omega,\mathcal F,\mathbb P)$ be a probability space, and let
$Z_i$, $C_i$, and $u_i$ be real-valued random variables. Write

$$
\mathcal G_i=\sigma(Z_i).
$$

The covariate $Z_i$ is scalar, as indicated by the target expression
$\alpha_1 Z_i$. Let $\alpha_0,\alpha_1,\gamma\in\mathbb R$ be fixed, let
$\sigma_u^2\geq 0$ be fixed, and let $m$ and $v$ be measurable functions with
$v(z)\geq 0$ where defined.

A-003 supplies square integrability and the structural equation

$$
\theta_i=\alpha_0+\alpha_1 Z_i+\gamma C_i+u_i.
$$

For conditional covariance, use

$$
\operatorname{Cov}(C_i,u_i\mid\mathcal G_i)
=
\mathbb E\!\left[
  \bigl(C_i-\mathbb E[C_i\mid\mathcal G_i]\bigr)
  \bigl(u_i-\mathbb E[u_i\mid\mathcal G_i]\bigr)
  \,\middle|\,\mathcal G_i
\right].
$$

All conditional equalities are equalities of versions and therefore imply the
corresponding statement for $P_{Z_i}$-almost every conditioning value $z$. In
the proof, subscripts are suppressed after this section: $Z=Z_i$, $C=C_i$,
$u=u_i$, $\theta=\theta_i$, and $\mathcal G=\mathcal G_i$.

## 2. Assumptions Used

1. **A-003, constructive heterogeneity moments (decision-gated).** The
   variables $Z_i$, $C_i$, and $u_i$ are square-integrable; the structural
   equation holds; and, conditionally on $Z_i=z$, $C_i$ has mean $m(z)$ and
   variance $v(z)$, while $u_i$ has mean $0$ and variance $\sigma_u^2$.

2. **A-007, conditional context-disturbance orthogonality (proposed,
   decision-gated).** Conditional context-disturbance orthogonality:
   $\operatorname{Cov}(C_i,u_i\mid Z_i)=0$ almost surely. Conditional
   independence of $C_i$ and $u_i$ given $Z_i$ is a stronger sufficient
   condition but is not required for the moment lemma.

3. **A-008, conditional joint Gaussianity (proposed, decision-gated; corollary
   only).** For $P_{Z_i}$-almost every $z$, $(C_i,u_i)\mid Z_i=z$ is
   bivariate normal. This assumption is not used in the moment lemma.

4. **Standard probability results.** Conditional expectation is linear; a
   $\mathcal G$-measurable term has zero conditional variance; conditional
   variance is the conditional second moment around the conditional mean; and
   an affine image of a multivariate normal vector is multivariate normal.
   These are the only standard results invoked below.

No normality assumption is used by Lemma L2.1.

## 3. Formal Statement

### Lemma L2.1 (Constructive conditional moment identities)

Assume A-003 and A-007. Then, almost surely,

$$
\mathbb E[\theta_i\mid Z_i]
=
\alpha_0+\alpha_1 Z_i+\gamma m(Z_i)
$$

and

$$
\operatorname{Var}(\theta_i\mid Z_i)
=
\gamma^2 v(Z_i)+\sigma_u^2.
$$

Equivalently, for $P_{Z_i}$-almost every $z$,

$$
\mathbb E[\theta_i\mid Z_i=z]
=
\alpha_0+\alpha_1 z+\gamma m(z)
$$

and

$$
\operatorname{Var}(\theta_i\mid Z_i=z)
=
\gamma^2 v(z)+\sigma_u^2.
$$

If $\gamma\ne0$ and $v(Z_i)$ is not almost surely constant, the conditional
variance of $\theta_i$ is not almost surely constant. This is the precise
constructive heterogeneity consequence; it does not itself imply
false-complex model selection.

### Corollary L2.2 (Gaussian distributional conclusion)

Assume A-003, A-007, and A-008. Then, for $P_{Z_i}$-almost every $z$,

$$
(C_i,u_i)\mid Z_i=z
\sim
\mathcal N_2\!\left(
  \begin{pmatrix}m(z)\\0\end{pmatrix},
  \begin{pmatrix}v(z)&0\\0&\sigma_u^2\end{pmatrix}
\right),
$$

and hence

$$
\theta_i\mid Z_i=z
\sim
\mathcal N\!\left(
  \alpha_0+\alpha_1 z+\gamma m(z),
  \gamma^2v(z)+\sigma_u^2
\right).
$$

Degenerate normal cases with zero variance are permitted. A stronger sufficient
alternative to A-008 is that, conditional on $Z_i=z$, $C_i$ and $u_i$ are
independent Gaussian variables with the respective moments in A-003. That
alternative is not required by the moment lemma.

## 4. Proof (or Proof Sketch)

### 4.1 Strategy Overview

We first condition on $\mathcal G=\sigma(Z)$ and use linearity to obtain the
conditional mean. We then subtract that mean from the structural equation and
expand its conditional square. A-007 removes the only cross term. For the
corollary, A-008 makes $(C,u)$ conditionally bivariate normal, so the
structural equation is an affine transformation of a normal vector.

### 4.2 Step-by-Step Derivation

1. By A-003, the conditional moment assumptions can be written as

   $$
   \mathbb E[C\mid\mathcal G]=m(Z),\qquad
   \operatorname{Var}(C\mid\mathcal G)=v(Z),\qquad
   \mathbb E[u\mid\mathcal G]=0,\qquad
   \operatorname{Var}(u\mid\mathcal G)=\sigma_u^2.
   $$

   (A-003 and the conditional-law convention in Section 1.)

2. Conditioning the structural equation on $\mathcal G$ gives

   $$
   \begin{aligned}
   \mathbb E[\theta\mid\mathcal G]
   &=
   \alpha_0+\alpha_1Z+
   \gamma\mathbb E[C\mid\mathcal G]
   +\mathbb E[u\mid\mathcal G]\\
   &=
   \alpha_0+\alpha_1Z+\gamma m(Z).
   \end{aligned}
   $$

   (A-003 and linearity of conditional expectation.)

3. Subtracting the conditional mean in Step 2 from the structural equation
   yields

   $$
   \theta-\mathbb E[\theta\mid\mathcal G]
   =
   \gamma\bigl(C-m(Z)\bigr)+u.
   $$

   (A-003 and Step 2.)

4. Therefore the conditional variance expands as

   $$
   \begin{aligned}
   \operatorname{Var}(\theta\mid\mathcal G)
   &=
   \mathbb E\!\left[
     \bigl\{\gamma(C-m(Z))+u\bigr\}^2
     \,\middle|\,\mathcal G
   \right]\\
   &=
   \gamma^2v(Z)
   +2\gamma\,
     \mathbb E\!\left[(C-m(Z))u\mid\mathcal G\right]
   +\sigma_u^2.
   \end{aligned}
   $$

   (definition of conditional variance, expansion of a square, and Step 1.)

5. The middle term in Step 4 is zero because

   $$
   \begin{aligned}
   \mathbb E\!\left[(C-m(Z))u\mid\mathcal G\right]
   &=
   \operatorname{Cov}(C,u\mid\mathcal G)\\
   &=0.
   \end{aligned}
   $$

   (the conditional-covariance definition, Step 1, and A-007.)

6. Substituting Step 5 into Step 4 proves

   $$
   \operatorname{Var}(\theta\mid\mathcal G)
   =
   \gamma^2v(Z)+\sigma_u^2,
   $$

   while Step 2 proves the conditional-mean identity; translating both
   conditional-expectation versions to $z$ proves Lemma L2.1 for
   $P_Z$-almost every $z$. (Steps 2, 4, and 5.)

7. For the corollary, fix a $z$ in the full-$P_Z$-measure set on which all
   conditional statements hold. Define

   $$
   W=\begin{pmatrix}C\\u\end{pmatrix},\qquad
   a_z=\alpha_0+\alpha_1z,\qquad
   \ell=\begin{pmatrix}\gamma\\1\end{pmatrix}.
   $$

   By A-003 and A-007, $W\mid Z=z$ has mean
   $(m(z),0)^\mathsf T$ and covariance matrix
   $\operatorname{diag}(v(z),\sigma_u^2)$; by A-008 it is bivariate normal.
   Since $\theta=a_z+\ell^\mathsf TW$, the conditional law of $\theta$ is
   normal with mean $a_z+\ell^\mathsf T(m(z),0)^\mathsf T$ and variance

   $$
   \ell^\mathsf T
   \begin{pmatrix}v(z)&0\\0&\sigma_u^2\end{pmatrix}
   \ell
   =
   \gamma^2v(z)+\sigma_u^2.
   $$

   (A-003, A-007, A-008, and the standard theorem on affine images of
   multivariate normal vectors.)

### 4.3 Conclusion

The requested conditional mean and variance formulas follow from the
structural equation, the stated conditional moments, and conditional zero
covariance. Normality is unnecessary for those identities. Conditional joint
Gaussianity is used only to obtain the Gaussian conditional distribution in
Corollary L2.2.

## 5. Known Gaps / Unproven Steps

- None in the conditional algebra of Lemma L2.1 or Corollary L2.2 once the
  listed assumptions are imposed.
- A-003, A-007, and A-008 remain decision-gated. That is a governance and
  scope limitation, not an unproved inference inside the conditional proof.
- The proof does not establish KL dominance, finite-sample selection, or any
  universal false-complex-selection conclusion.

## 6. Counter-Example Candidates

- **Why A-007 is needed.** Let $Z=0$ almost surely,
  $\alpha_0=\alpha_1=0$, $\gamma=1$, and $C=u=X$ with
  $X\sim\mathcal N(0,1)$. Then $m(0)=0$, $v(0)=1$,
  $\mathbb E[u\mid Z]=0$, and $\operatorname{Var}(u\mid Z)=1$, but
  $\operatorname{Cov}(C,u\mid Z)=1$. Consequently
  $\operatorname{Var}(\theta\mid Z)=4$, not the claimed two-term value $2$.

- **Why A-008 is needed for the distributional conclusion.** Let $Z=0$
  almost surely, $C=X$ with $X\sim\mathcal N(0,1)$, and let $S$ be an
  independent fair Rademacher variable. Set $u=SX$. Both $C$ and $u$ are
  standard normal and their covariance is zero, but
  $C+u=X(1+S)$ has an atom at zero with probability one-half and is not
  normal. Thus normal marginals plus zero covariance do not replace
  conditional joint Gaussianity.

- **When heterogeneity does not arise.** If $\gamma=0$ or $v(Z)$ is almost
  surely constant, the variance identity remains true but does not yield
  context-dependent conditional variance. Similarly, a simple model with
  sufficient random-effect structure can already represent the induced
  marginal law.

## 7. Need for New Assumptions?

Yes.

1. **A-007** is proposed, not approved, in both
   docs/proposed_assumptions.md and registries/assumption_register.csv.
   It is the minimal conditional-zero-covariance condition needed for the
   two-term variance identity.

2. **A-008** is proposed, not approved, in the same two governance files. It
   is required only for the Gaussian distributional corollary; it is not an
   assumption of the moment lemma.

The existing decision-gated A-003 was expanded in the assumption register to
state the supplied square-integrability and $u_i$ moment conditions explicitly.
No claim-registry status was promoted.
