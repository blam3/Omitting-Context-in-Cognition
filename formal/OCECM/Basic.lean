/-!
OCECM formal scaffold.

This file intentionally contains shared definitions and status metadata only.
It does not assert or prove any theorem from the OCECM proof route.
-/

namespace OCECM

universe uY uX uZ uTheta uProb

/-- Lightweight status values mirroring `docs/theorem_backlog.md`. -/
inductive TheoremStatus where
  | backlog
  | statementDraft
  | proofDraft
  | proofCriticReview
  | accepted
  | decisionGated
deriving DecidableEq, Repr

/-- Registry-linked metadata for theorem files. -/
structure TheoremCard where
  label : String
  claimId : String
  assumptionIds : List String
  status : TheoremStatus
  manuscriptReady : Bool := false
deriving Repr

/--
A choice kernel placeholder. Future theorem work should replace `Prob` with a
probability object supplied by the selected formal probability library.
-/
structure ChoiceKernel
    (Y : Type uY) (X : Type uX) (Theta : Type uTheta) (Prob : Type uProb) where
  eval : Y -> X -> Theta -> Prob

/-- Observed response law after conditioning on trial features and covariates. -/
structure MarginalLaw
    (Y : Type uY) (X : Type uX) (Z : Type uZ) (Prob : Type uProb) where
  eval : Y -> X -> Z -> Prob

end OCECM
