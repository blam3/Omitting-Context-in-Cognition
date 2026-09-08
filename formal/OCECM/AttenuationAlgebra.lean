import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# Lemma T-004a, algebraic core

`docs/theorems/T-004_kl_dominance.md` reduces membership of the omitted-context
response law in the simple model class `M_S` to a decidable question: is
`a ↦ Φ⁻¹(p a) * √(1 + s² a²)` affine?

The probit link contributes nothing to that reduction — `Φ` is a bijection
`ℝ → (0,1)`, so the whole content is the algebraic identity below, on the
*index scale*. That identity is what is formalised here.

This is deliberately the only Lean file in the package with mathematical
content. The measure-theoretic mixture lemma (T-001) and the asymptotic results
(T-005, T-007) are not formalised: mathlib has no M-estimation,
cross-validation, or singular-learning theory, so T-005 and T-007 are not
formalisable today, and T-001 awaits a separate disintegration-API pass. See
`docs/theorem_backlog.md`.
-/

namespace OCECM

/-- The attenuation radicand `1 + s² a²` is strictly positive whenever `0 ≤ s²`,
so its square root never vanishes and division by it is safe. -/
theorem attenuation_sqrt_pos {s2 a : ℝ} (hs : 0 ≤ s2) :
    0 < Real.sqrt (1 + s2 * a ^ 2) := by
  apply Real.sqrt_pos.mpr
  have h : 0 ≤ s2 * a ^ 2 := mul_nonneg hs (sq_nonneg a)
  linarith

/--
**Lemma T-004a (algebraic core).** On the index scale, a response law lies in the
simple class `M_S` with attenuation parameter `s²` exactly when rescaling by
`√(1 + s² a²)` makes it affine in the design point `a`.

The left-hand side is membership in `M_S`; the right-hand side is the affineness
test the numerical harness evaluates (`affine_residual` in
`R/theorem_numerics.R`). Their equivalence is what makes non-representability
decidable by a one-dimensional search over `s²`.
-/
theorem mem_M_S_iff_affine_after_rescaling
    {s2 : ℝ} (hs : 0 ≤ s2) (g : ℝ → ℝ) (b0 b1 : ℝ) :
    (∀ a : ℝ, g a = (b0 + b1 * a) / Real.sqrt (1 + s2 * a ^ 2))
      ↔ (∀ a : ℝ, g a * Real.sqrt (1 + s2 * a ^ 2) = b0 + b1 * a) := by
  constructor
  · intro h a
    have hne : Real.sqrt (1 + s2 * a ^ 2) ≠ 0 := (attenuation_sqrt_pos hs).ne'
    rw [h a]
    field_simp
  · intro h a
    have hne : Real.sqrt (1 + s2 * a ^ 2) ≠ 0 := (attenuation_sqrt_pos hs).ne'
    rw [eq_div_iff hne]
    exact h a

/--
The boundary case `s² = 0`: with no attenuation the criterion degenerates to
plain affineness, which is the homogeneous-context case of T-004 (registered
boundary condition 2) where the KL gap vanishes.
-/
theorem mem_M_S_iff_affine_of_no_attenuation (g : ℝ → ℝ) (b0 b1 : ℝ) :
    (∀ a : ℝ, g a = (b0 + b1 * a) / Real.sqrt (1 + 0 * a ^ 2))
      ↔ (∀ a : ℝ, g a = b0 + b1 * a) := by
  simp

end OCECM
