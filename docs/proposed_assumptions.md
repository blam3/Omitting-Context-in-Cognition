# Proposed Assumptions

Agents may append proposed assumptions here. They must not move them into `assumption_registry.md` without human approval.

## A-006 Trial-design exogeneity for simplified mixture

Status: rejected by PI direction on 2026-07-07. Do not approve A-006 for the
primary theorem statement. Use `F_{theta|X,Z}` as primary and mention
`F_{theta|Z}` only as a corollary under additional fixed-design or exogeneity
conditions.

For the omitted-context mixture lemma to use
`dF_{theta|Z}(theta|z)` rather than `dF_{theta|X,Z}(theta|x,z)`,
trial features `X_it` are fixed by design or assigned independently of
`theta_i` conditional on `Z_i`.

Rationale: Issue #4 proposes the simplified `theta | Z` mixture display, but
the direct conditional law of total probability gives a mixture over
`theta | X,Z`. The simplified display is appropriate only under a fixed-design
convention or conditional trial-design exogeneity.

## A-007 Conditional context-disturbance orthogonality

Status: proposed; decision needed from PI/theorem review.

Conditional context-disturbance orthogonality: Cov(C_i, u_i | Z_i) = 0 almost
surely. Conditional independence of C_i and u_i given Z_i is a stronger
sufficient condition but is not required for the moment lemma.

Rationale: The L2 conditional variance is
`gamma^2 v(z) + sigma_u^2 + 2 gamma Cov(C_i, u_i | Z_i=z)`. The requested
two-term formula therefore needs this minimal orthogonality condition (or the
stronger conditional-independence alternative).

## A-008 Conditional joint Gaussianity for distributional corollary

Status: proposed; decision needed from PI/theorem review.

Conditional joint Gaussianity for the distributional corollary: for
P_{Z_i}-almost every z, (C_i, u_i) conditional on Z_i=z is bivariate normal.
This assumption is used only for the Gaussian distribution corollary, not for
the moment lemma.

Rationale: Conditional zero covariance proves the moment identity but not a
Gaussian conditional law for theta_i. Conditional joint Gaussianity, together
with A-003 and A-007, makes the affine-sum distributional conclusion valid.

## A-009 Conditional choice-kernel sufficiency

Status: proposed; decision needed from PI/theorem review.

For every outcome `y` in the finite response space,
`E[1{Y_it = y} | X_it, Z_i, theta_i] = p(y | X_it, theta_i; eta*)` almost
surely. This is the minimal condition used to substitute the registered choice
kernel into the conditional-expectation proof of Lemma 1.1.

Rationale: A-001's current wording does not by itself establish the equality
after conditioning on `Z_i`. This condition is narrower than assuming a full
participant-level joint-response factorization.

## A-010 Jointly measurable choice kernel

Status: proposed; decision needed from PI/theorem review.

For every outcome `y` in the finite response space, the map
`(x, theta) -> p(y | x, theta; eta*)` is jointly Borel measurable. Since it
is bounded in `[0,1]`, it is integrable against the regular conditional
distribution.

Rationale: This is the regularity condition needed to express the
conditional expectation in Lemma 1.1 as the displayed mixture integral.
