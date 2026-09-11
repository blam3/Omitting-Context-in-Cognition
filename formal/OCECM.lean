import OCECM.Basic
import OCECM.AttenuationAlgebra
import OCECM.MixtureLemma
import OCECM.GaussianConstructive
import OCECM.AICBICThreshold

/-!
# OCECM formalization root

Root module for the `OCECM` library. Lake resolves `lean_lib OCECM` through this
file, so every module in `OCECM/` must be imported here to be built and checked
by CI. A module that is not listed here is not verified.
-/
