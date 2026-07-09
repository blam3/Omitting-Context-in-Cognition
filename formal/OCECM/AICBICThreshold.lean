import OCECM.Basic

/-!
# Secondary AIC/BIC threshold scaffold

This file is a placeholder for finite-sample threshold corollaries. The intended
results are conditional comparisons:

- AIC-like selection favors the complex model when
  `2 * n * Delta_ell > 2 * (k_K - k_S)`.
- BIC-like selection favors the complex model when
  `2 * n * Delta_ell > (k_K - k_S) * log n`.

No theorem is asserted here, and these thresholds must not be read as universal
model-selection guarantees.
-/

namespace OCECM

def aicBicThresholdCard : TheoremCard :=
  { label := "T-007 secondary AIC/BIC finite-sample threshold corollaries"
    claimId := "C-004"
    assumptionIds := []
    status := TheoremStatus.backlog
    manuscriptReady := false }

universe uQuantity

section StatementShape

variable {Quantity : Type uQuantity}

/-- Symbolic slots for future threshold corollaries. -/
structure ThresholdComparisonShape where
  sampleSize : Quantity
  perObservationLogScoreGain : Quantity
  complexParameterCount : Quantity
  simpleParameterCount : Quantity

end StatementShape

end OCECM
