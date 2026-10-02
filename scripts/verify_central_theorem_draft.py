#!/usr/bin/env python3
"""Dependency-free checks for docs/central_theorem_full_draft.md.

These checks guard the one-shot central-theorem draft against algebra, sign and
order-of-magnitude errors. They are numerical diagnostics and exact rational
checks of identities used in the draft. Passing them does NOT prove any theorem,
certify global optimality in general, or replace review.

Sections (labels match the draft):
  I1  minimal ambiguity instance: cells, signatures, projections, extra-score drift
      (Thm 2.4) and its gap bounds (Prop 2.5), conditional gap, context-aware risk
      identity (Prop 1.6), finite-sample heuristics (Remark 3.10);
  E1  heterogeneity expansion (Thm 1.4): closed form, orthogonality, O(eps) remainder;
  L1  local mechanism theorem for homogeneous candidates (Thm 2.6 / Cor 2.7),
      including the product-candidate reduction of Lemma 2.3;
  H1  hierarchical absorption of the second-order term (Prop 4.3);
  H2  parity obstruction at the tangent level (Prop 4.4).
"""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

OUT = Path("logs/theory_checks/2026-10-02_central_theorem_draft.json")


# ----------------------------------------------------------------------------
# Elementary helpers
# ----------------------------------------------------------------------------

def sig(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


def logit(p: float) -> float:
    return math.log(p / (1.0 - p))


def bern(y: int, p):
    return p if y else 1 - p


def kl_bern(p: float, q: float) -> float:
    out = 0.0
    if p > 0:
        out += p * math.log(p / q)
    if p < 1:
        out += (1 - p) * math.log((1 - p) / (1 - q))
    return out


def cells(T: int):
    return list(itertools.product([0, 1], repeat=T))


def solve(A, b):
    """Gaussian elimination with partial pivoting (small dense systems)."""
    n = len(A)
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[piv][c]) < 1e-300:
            raise ZeroDivisionError("singular system")
        M[c], M[piv] = M[piv], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]
                if f:
                    for k in range(c, n + 1):
                        M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def marginals(p: dict, T: int):
    return [sum(v for y, v in p.items() if y[t] == 1) for t in range(T)]


def multi_information(p: dict, T: int) -> float:
    m = marginals(p, T)
    return sum(v * math.log(v / math.prod(bern(y[t], m[t]) for t in range(T)))
               for y, v in p.items())


def kl_joint(p: dict, q: dict) -> float:
    return sum(v * math.log(v / q[y]) for y, v in p.items())


def drop(y, t):
    return y[:t] + y[t + 1:]


def retained_marginal(p: dict, t: int) -> dict:
    out = {}
    for y, v in p.items():
        k = drop(y, t)
        out[k] = out.get(k, 0.0) + v
    return out


def conditional_risk(p: dict, q: dict, T: int) -> float:
    """(1/T) sum_t E_{p,Y_-t} KL(p(Y_t|Y_-t) || q(Y_t|Y_-t)), computed directly."""
    total = 0.0
    for t in range(T):
        pm, qm = retained_marginal(p, t), retained_marginal(q, t)
        for y, v in p.items():
            k = drop(y, t)
            total += v * math.log((v / pm[k]) / (q[y] / qm[k]))
    return total / T


def product_law(pi: list) -> dict:
    T = len(pi)
    return {y: math.prod(bern(y[t], pi[t]) for t in range(T)) for y in cells(T)}


def gauss_legendre(n: int):
    """Nodes/weights on [-1, 1] via Newton iteration (as in validate_minimal_bayes.py)."""
    out = []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            der = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / der
            x -= dx
            if abs(dx) < 1e-16:
                break
        out.append((x, 2 / ((1 - x * x) * der * der)))
    return out


def normal_nodes(n: int = 160, L: float = 12.0):
    """Quadrature for E[g(E)], E ~ N(0,1), via Gauss-Legendre on [-L, L]."""
    c = 1 / math.sqrt(2 * math.pi)
    return [(L * x, L * w * c * math.exp(-0.5 * (L * x) ** 2)) for x, w in gauss_legendre(n)]


# ----------------------------------------------------------------------------
# Product-family KL projection (weighted logistic regression on marginals)
# ----------------------------------------------------------------------------

def project_product(pbar, H, offset, J, phi0, iters=200):
    """Minimise sum_w H[w] sum_t KL(Bern(pbar[w][t]) || Bern(sig(offset + J phi))).

    pbar, offset: dict w -> list over t; J: dict w -> list over t of length-k lists.
    The logits are affine in phi, so the objective is convex; damped Newton.
    """
    k = len(phi0)
    phi = list(phi0)

    def obj(ph):
        s = 0.0
        for w in pbar:
            for t, pb in enumerate(pbar[w]):
                eta = offset[w][t] + sum(J[w][t][j] * ph[j] for j in range(k))
                s += H[w] * kl_bern(pb, sig(eta))
        return s

    cur = obj(phi)
    for _ in range(iters):
        g = [0.0] * k
        Hm = [[0.0] * k for _ in range(k)]
        for w in pbar:
            for t, pb in enumerate(pbar[w]):
                eta = offset[w][t] + sum(J[w][t][j] * phi[j] for j in range(k))
                pi = sig(eta)
                for a in range(k):
                    g[a] += H[w] * J[w][t][a] * (pi - pb)
                    for b in range(k):
                        Hm[a][b] += H[w] * J[w][t][a] * J[w][t][b] * pi * (1 - pi)
        if max(abs(x) for x in g) < 1e-17:
            break
        step = solve(Hm, g)
        lam = 1.0
        while lam > 1e-12:
            trial = [phi[j] - lam * step[j] for j in range(k)]
            val = obj(trial)
            # Rounding-tolerant acceptance: near the optimum the objective change is
            # below machine precision, while the Newton step is still informative.
            if val <= cur + 1e-15 * (1 + abs(cur)):
                break
            lam /= 2
        phi, cur = trial, val
        if max(abs(lam * s) for s in step) < 1e-15:
            break
    return phi, obj(phi)


def wls_project(a, Omega, cols):
    """Omega-weighted LS projection of vector a onto span(cols). Vectors are flat lists."""
    k = len(cols)
    G = [[sum(Omega[i] * cols[r][i] * cols[c][i] for i in range(len(a))) for c in range(k)]
         for r in range(k)]
    rhs = [sum(Omega[i] * cols[r][i] * a[i] for i in range(len(a))) for r in range(k)]
    coef = solve(G, rhs)
    return [sum(coef[r] * cols[r][i] for r in range(k)) for i in range(len(a))]


def wnorm2(a, Omega):
    return sum(Omega[i] * a[i] * a[i] for i in range(len(a)))


def drift_bounds(rows_S, row_e, pis, Hs):
    """Partial information and the rigorous curvature bound for one extra parameter.

    rows_S[i]: S logit-gradient at stacked index i; row_e[i]: extra logit derivative;
    pis[i]: S-projection probability; Hs[i]: H(w) for that index.  Returns
    (I_{e|S}, Bbar) with I = J_ee - J_eS J_SS^{-1} J_Se (J at the S projection) and
    Bbar = (1/4) sum_i H_i c_i^2 for the efficient direction c = e - rows_S J_SS^{-1} J_Se.
    """
    k = len(rows_S[0])
    wts = [Hs[i] * pis[i] * (1 - pis[i]) for i in range(len(pis))]
    JSS = [[sum(wts[i] * rows_S[i][a] * rows_S[i][b] for i in range(len(wts)))
            for b in range(k)] for a in range(k)]
    JSe = [sum(wts[i] * rows_S[i][a] * row_e[i] for i in range(len(wts))) for a in range(k)]
    Jee = sum(wts[i] * row_e[i] ** 2 for i in range(len(wts)))
    coef = solve(JSS, JSe)
    I_part = Jee - sum(JSe[a] * coef[a] for a in range(k))
    c = [row_e[i] - sum(rows_S[i][a] * coef[a] for a in range(k)) for i in range(len(wts))]
    Bbar = 0.25 * sum(Hs[i] * c[i] ** 2 for i in range(len(wts)))
    return I_part, Bbar


# ----------------------------------------------------------------------------
# I1. Minimal ambiguity instance (docs/minimal_ambiguity_proof.md)
# ----------------------------------------------------------------------------

def check_instance():
    T = 2
    x = [1, 2]
    # Exact rational cells: C ~ Bern(1/2); C=0 -> rates (1/2,1/2); C=1 -> (1/4,1/10).
    rates = {0: (Fr(1, 2), Fr(1, 2)), 1: (Fr(1, 4), Fr(1, 10))}
    p_c = {c: {y: math.prod(bern(y[t], rates[c][t]) for t in range(T)) for y in cells(T)}
           for c in (0, 1)}
    P = {y: (p_c[0][y] + p_c[1][y]) / 2 for y in cells(T)}
    assert [P[(0, 0)], P[(1, 0)], P[(0, 1)], P[(1, 1)]] == [Fr(37, 80), Fr(19, 80), Fr(13, 80),
                                                            Fr(11, 80)]
    m = [sum(v for y, v in P.items() if y[t]) for t in range(T)]
    assert m == [Fr(3, 8), Fr(3, 10)]
    cov = P[(1, 1)] - m[0] * m[1]
    assert cov == Fr(1, 40) and cov > 0  # Prop 1.3(a): positive within-person dependence

    Pf = {y: float(v) for y, v in P.items()}
    mf = [float(v) for v in m]
    info = multi_information(Pf, T)

    # Kernel-at-mean logits versus true marginal logits (attenuation toward 1/2).
    theta_bar = math.log(3) / 2
    kernel_at_mean = [-theta_bar * xt for xt in x]
    marginal_logits = [logit(v) for v in mf]
    attenuation = [ml - km for ml, km in zip(marginal_logits, kernel_at_mean)]
    assert all(a > 0 for a in attenuation) and attenuation[1] > attenuation[0]

    # S: logit -theta x_t.  K: logit delta - theta x_t (delta = 4[w(1/2;rho)-1/2]).
    pbar = {0: mf}
    H = {0: 1.0}
    off = {0: [0.0, 0.0]}
    JS = {0: [[-x[0]], [-x[1]]]}
    JK = {0: [[-x[0], 1.0], [-x[1], 1.0]]}
    (thS,), _ = project_product(pbar, H, off, JS, [0.4])
    (thK, dK), _ = project_product(pbar, H, off, JK, [0.3, 0.0])
    assert abs(thK - math.log(7 / 5)) < 1e-12 and abs(dK - math.log(21 / 25)) < 1e-12
    assert 0 < thS < 2  # interior; unrestricted optimum
    qS = product_law([sig(-thS * xt) for xt in x])
    qK = product_law([sig(dK - thK * xt) for xt in x])
    RS, RK = kl_joint(Pf, qS), kl_joint(Pf, qK)
    assert abs(RK - info) < 1e-14  # K matches marginals: R_K = multi-information
    gap = RS - RK
    assert 0 < RK < RS

    # Conditional (trial-LOO) gap computed directly, then compared with gap / T.
    dC = conditional_risk(Pf, qS, T) - conditional_risk(Pf, qK, T)
    assert abs(dC - gap / T) < 1e-14

    # Alignment number A = E_P[d/d delta log q_K] at (theta_S, delta=0).
    piS = [sig(-thS * xt) for xt in x]
    A = sum(mf[t] - piS[t] for t in range(T))
    assert A < 0  # decreasing delta (rho < 1) lowers risk; consistent with delta_K < 0
    # S first-order condition at its optimum: sum_t x_t (piS_t - p_t) = 0.
    assert abs(sum(x[t] * (piS[t] - mf[t]) for t in range(T))) < 1e-14

    # Prop 2.5: gap from the drift. Rigorous lower bound Lambda^2/(2 Bbar) and the
    # score-test approximation A^2/(2 I_{e|S}).
    I_eS, Bbar = drift_bounds([[-xt] for xt in x], [1.0, 1.0], piS, [1.0, 1.0])
    drift_lower = A * A / (2 * Bbar)
    drift_approx = A * A / (2 * I_eS)
    assert drift_lower <= gap and abs(drift_approx / gap - 1) < 0.01
    step = A / Bbar  # the one-step move stays inside the K parameter box
    assert -0.5 < step < 0.5 and 0 < thS + step * (-sum(
        (piS[t] * (1 - piS[t])) * (-x[t]) for t in range(T)) / sum(
        (piS[t] * (1 - piS[t])) * x[t] ** 2 for t in range(T))) < 2

    # Implied Prelec parameter at the K projection.
    L2 = math.log(2)
    rhoK = math.log(-math.log(0.5 + dK / 4)) / math.log(L2)
    assert 0.6 < rhoK < 0.7

    # Prop 1.6: context-aware risk identity and zero risk of the contextual model.
    def ctx_risk(q):
        return 0.5 * sum(kl_joint({y: float(v) for y, v in p_c[c].items()}, q) for c in (0, 1))

    I_YC = 0.5 * sum(kl_joint({y: float(v) for y, v in p_c[c].items()}, Pf) for c in (0, 1))
    assert I_YC > 0
    for q in (qS, qK):
        assert abs(ctx_risk(q) - (kl_joint(Pf, q) + I_YC)) < 1e-14

    # Finite-sample guide (heuristic, Remark 3.10): Vuong-type moments of log q_K*/q_S*.
    lr = {y: math.log(qK[y] / qS[y]) for y in cells(T)}
    mean_lr = sum(Pf[y] * lr[y] for y in lr)
    assert abs(mean_lr - gap) < 1e-14
    sd_lr = math.sqrt(sum(Pf[y] * (lr[y] - mean_lr) ** 2 for y in lr))

    def bic_crossing():
        lo, hi = 10.0, 1e7
        for _ in range(200):
            mid = (lo + hi) / 2
            if mid * gap - 0.5 * math.log(mid) < 0:
                lo = mid
            else:
                hi = mid
        return hi

    def n_for_prob(z, penalty):
        """Smallest n with sqrt(n)*gap - penalty(n)/sqrt(n) >= z*sd (normal heuristic)."""
        lo, hi = 1.0, 1e9
        for _ in range(300):
            mid = (lo + hi) / 2
            if math.sqrt(mid) * gap - penalty(mid) / math.sqrt(mid) < z * sd_lr:
                lo = mid
            else:
                hi = mid
        return hi

    n_star = bic_crossing()
    n_bic50 = n_for_prob(0.0, lambda n: 0.5 * math.log(n))
    n_bic80 = n_for_prob(0.8416212335729143, lambda n: 0.5 * math.log(n))

    # Remark 3.10 heuristics (NOT theorems): regular misspecified-likelihood expansions.
    # Per-participant sensitivity J = E[-Hessian] and score covariance Kc at each projection.
    var = [mf[t] * (1 - mf[t]) for t in range(T)]
    cv = float(cov)

    def info_mats(rows, pis):
        k = len(rows[0])
        Jm = [[sum((pis[t] * (1 - pis[t])) * rows[t][a] * rows[t][b] for t in range(T))
               for b in range(k)] for a in range(k)]
        Km = [[sum(var[t] * rows[t][a] * rows[t][b] for t in range(T))
               + sum(cv * rows[t][a] * rows[u][b] for t in range(T) for u in range(T) if t != u)
               for b in range(k)] for a in range(k)]
        return Jm, Km

    def tr_inv(Jm, Km):
        cols = [solve(Jm, [Km[r][c] for r in range(len(Km))]) for c in range(len(Km))]
        return sum(cols[c][c] for c in range(len(Km)))

    def trial_score_mat(rows, pis):
        """E[sum_t s_t s_t'] (within-trial outer products only): trial-LOO's penalty."""
        k = len(rows[0])
        return [[sum((var[t] + (mf[t] - pis[t]) ** 2) * rows[t][a] * rows[t][b]
                     for t in range(T)) for b in range(k)] for a in range(k)]

    rowsS = [[-xt] for xt in x]
    rowsK = [[-xt, 1.0] for xt in x]
    piK = [sig(dK - thK * xt) for xt in x]
    JS_, KS_ = info_mats(rowsS, piS)
    JK_, KK_ = info_mats(rowsK, piK)
    trS, trK = tr_inv(JS_, KS_), tr_inv(JK_, KK_)
    assert abs(trK - 2) < 1e-12  # saturated marginals: cross-trial term drops out exactly
    ttrS = tr_inv(JS_, trial_score_mat(rowsS, piS))
    ttrK = tr_inv(JK_, trial_score_mat(rowsK, piK))
    detJK = JK_[0][0] * JK_[1][1] - JK_[0][1] * JK_[1][0]
    # Prior densities at the projections (theta,delta coordinates; uniform theta on [0,2],
    # uniform rho on [rho_L, rho_U] with the delta Jacobian from the M1 review).
    rL = math.log(-math.log(3 / 8)) / math.log(L2)
    rU = math.log(-math.log(5 / 8)) / math.log(L2)
    mm = 0.5 + dK / 4
    piK_dens = 0.5 / (rU - rL) / abs(4 * mm * math.log(mm) * math.log(L2))
    piS_dens = 0.5
    c0_bf = (math.log(piK_dens / piS_dens) + 0.5 * math.log(2 * math.pi)
             - 0.5 * math.log(detJK / JS_[0][0]))
    bonus = 0.5 * (trK - trS)  # mean in-sample fitting bonus of K over S
    phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
    thresholds = {
        "BIC": lambda n: 0.5 * math.log(n) - bonus,
        "BF_Laplace": lambda n: 0.5 * math.log(n) - c0_bf - bonus,
        "trial_LOO_TIC": lambda n: (ttrK - ttrS) - bonus,
    }
    heur = {}
    for n in (200, 1000, 10000, 100000):
        heur[str(n)] = {name: phi((n * gap - c(n)) / (math.sqrt(n) * sd_lr))
                        for name, c in thresholds.items()}
    n_loo80 = n_for_prob(0.8416212335729143, lambda n: (ttrK - ttrS) - bonus)

    # Loose but rigorous Hoeffding bound (Thm 3.3(c)) on compact boxes: all candidate
    # trial probabilities exceed a = sig(-9/2); |log q| <= M := 2 log(1/a); J = 4 cells.
    a = sig(-4.5)
    M = 2 * math.log(1 / a)
    Jc = 4

    def hoeffding_n(target=0.05):
        lo, hi = 10.0, 1e14
        for _ in range(300):
            mid = (lo + hi) / 2
            g = gap - 0.5 * math.log(mid) / mid
            ok = g > 0 and 2 * Jc * math.exp(-mid * g * g / (2 * M * M * Jc * Jc)) <= target
            if ok:
                hi = mid
            else:
                lo = mid
        return hi

    # Local heterogeneity approximation evaluated (outside its regime) at the instance:
    # Theta = theta_bar + eps V, V = +-1, eps = log(3)/2, v = 1.
    eps = theta_bar
    pi0 = [sig(-theta_bar * xt) for xt in x]
    Om = [p * (1 - p) for p in pi0]
    avec = [0.5 * xt ** 2 * (1 - 2 * p) for xt, p in zip(x, pi0)]
    cols_S = [[-xt for xt in x]]
    cols_K = cols_S + [[1.0, 1.0]]
    PSa, PKa = wls_project(avec, Om, cols_S), wls_project(avec, Om, cols_K)
    d2 = wnorm2([u - v for u, v in zip(PKa, PSa)], Om)
    hD2 = (x[0] ** 2) * (x[1] ** 2) * Om[0] * Om[1]
    local_gap = 0.5 * eps ** 4 * d2
    local_RK = 0.5 * eps ** 4 * (wnorm2([u - v for u, v in zip(avec, PKa)], Om) + hD2)

    return {
        "cells_P_order_00_10_01_11": [str(P[(0, 0)]), str(P[(1, 0)]), str(P[(0, 1)]),
                                      str(P[(1, 1)])],
        "marginals": [str(v) for v in m],
        "covariance": str(cov),
        "multi_information_I_P": info,
        "kernel_logits_at_mean": kernel_at_mean,
        "true_marginal_logits": marginal_logits,
        "attenuation_logit_shift": attenuation,
        "theta_S_star": thS,
        "theta_K_star": thK,
        "delta_K_star": dK,
        "rho_K_star": rhoK,
        "R_S": RS,
        "R_K": RK,
        "Delta_J_per_participant": gap,
        "Delta_C_per_trial": dC,
        "alignment_A_at_S_projection": A,
        "partial_information_I_e_given_S": I_eS,
        "curvature_bound_Bbar": Bbar,
        "gap_lower_bound_A2_over_2Bbar": drift_lower,
        "gap_score_test_approx_A2_over_2I": drift_approx,
        "I_Y_C_given_W": I_YC,
        "context_aware_risk_S": ctx_risk(qS),
        "context_aware_risk_K": ctx_risk(qK),
        "sd_log_likelihood_ratio_per_participant": sd_lr,
        "heuristic_n_expected_BIC_crossing": n_star,
        "heuristic_n_BIC_50pct_ignoring_fit_bonus": n_bic50,
        "heuristic_n_BIC_80pct_ignoring_fit_bonus": n_bic80,
        "heuristic_n_trial_LOO_80pct": n_loo80,
        "participant_TIC_trace_S": trS,
        "participant_TIC_trace_K": trK,
        "trial_LOO_penalty_trace_S": ttrS,
        "trial_LOO_penalty_trace_K": ttrK,
        "mean_fit_bonus_K_minus_S": bonus,
        "det_J_K_over_J_S": detJK / JS_[0][0],
        "BF_Laplace_constant_c0": c0_bf,
        "heuristic_selection_probabilities_note": (
            "Normal approximation for the pseudo-true log-likelihood ratio plus mean fitting "
            "bonus; BF uses Laplace and is unreliable when the delta posterior is truncated "
            "by the prior box (roughly n <= 1000 here). Heuristic only."),
        "heuristic_selection_probabilities": heur,
        "rigorous_hoeffding_n_for_BIC_failure_le_0.05": hoeffding_n(),
        "local_formula_at_instance_gap": local_gap,
        "local_formula_at_instance_R_K": local_RK,
        "local_formula_ratio_gap_exact_over_local": gap / local_gap,
    }


# ----------------------------------------------------------------------------
# E1 + L1. Heterogeneity expansion and local mechanism theorem (homogeneous S, K)
# ----------------------------------------------------------------------------

# Design: two retained-covariate cells w in {-1,+1}, T = 3 trials, logistic kernel
#   eta_t = alpha_t - beta_t theta.  Truth: Theta | w = thbar(w) + eps * sqrt(v(w)) * V.
DES_T = 3
ALPHA = [0.3, -0.2, 0.1]
BETA = [1.0, 2.0, 3.0]
WS = (-1, 1)
HW = {-1: 0.5, 1: 0.5}
THBAR = {-1: 0.1, 1: 0.7}
VW = {-1: 0.5, 1: 1.5}
V_ASYM = [(-1.0, 1 / 3), (0.0, 1 / 2), (2.0, 1 / 6)]  # mean 0, var 1, skewed
V_SYM = [(-1.0, 0.5), (1.0, 0.5)]  # mean 0, var 1, kurtosis 1
EXTRA = [0.5, -0.3, 0.8]  # generic extra logit column (stands in for d eta / d rho)


def true_law(w, eps, Vdist):
    out = {y: 0.0 for y in cells(DES_T)}
    for v, pv in Vdist:
        th = THBAR[w] + eps * math.sqrt(VW[w]) * v
        pis = [sig(ALPHA[t] - BETA[t] * th) for t in range(DES_T)]
        for y in out:
            out[y] += pv * math.prod(bern(y[t], pis[t]) for t in range(DES_T))
    return out


def h_closed_form(w, y):
    pi = [sig(ALPHA[t] - BETA[t] * THBAR[w]) for t in range(DES_T)]
    e = [y[t] - pi[t] for t in range(DES_T)]
    hA = 0.5 * VW[w] * sum(BETA[t] ** 2 * (1 - 2 * pi[t]) * e[t] for t in range(DES_T))
    hD = 0.5 * VW[w] * sum(BETA[t] * BETA[u] * e[t] * e[u]
                           for t in range(DES_T) for u in range(DES_T) if t != u)
    return hA, hD


def check_expansion():
    res = {}
    for name, Vd in (("asymmetric_V", V_ASYM), ("symmetric_V", V_SYM)):
        errs = []
        # Skewed V has a large third-order constant here (beta up to 3), so the
        # asymptotic O(eps) regime starts at small eps.
        for eps in (0.02, 0.01, 0.005, 0.0025):
            mx = 0.0
            for w in WS:
                p = true_law(w, eps, Vd)
                p0 = true_law(w, 0.0, Vd)
                for y in p:
                    hA, hD = h_closed_form(w, y)
                    mx = max(mx, abs((p[y] / p0[y] - 1) / eps ** 2 - (hA + hD)))
            errs.append(mx)
        # Remainder O(eps) for skewed V, O(eps^2) for symmetric V.
        rates = [math.log(errs[i] / errs[i + 1]) / math.log(2) for i in range(len(errs) - 1)]
        res[name] = {"max_abs_error": errs, "observed_orders": rates}
    assert all(0.85 < r < 1.15 for r in res["asymmetric_V"]["observed_orders"])
    assert all(1.85 < r < 2.15 for r in res["symmetric_V"]["observed_orders"])

    # Independent finite-difference check of h = (1/2) v g''/g at theta_bar.
    fd_err = 0.0
    step = 1e-4
    for w in WS:
        for y in cells(DES_T):
            g = lambda th: math.prod(bern(y[t], sig(ALPHA[t] - BETA[t] * th))
                                     for t in range(DES_T))
            th = THBAR[w]
            g2 = (g(th + step) - 2 * g(th) + g(th - step)) / step ** 2
            hA, hD = h_closed_form(w, y)
            fd_err = max(fd_err, abs(0.5 * VW[w] * g2 / g(th) - (hA + hD)))
    assert fd_err < 1e-6

    # Centering and orthogonality under p0, per w.
    worst_mean, worst_cross = 0.0, 0.0
    for w in WS:
        p0 = true_law(w, 0.0, V_SYM)
        mA = sum(p0[y] * h_closed_form(w, y)[0] for y in p0)
        mD = sum(p0[y] * h_closed_form(w, y)[1] for y in p0)
        cr = sum(p0[y] * h_closed_form(w, y)[0] * h_closed_form(w, y)[1] for y in p0)
        worst_mean = max(worst_mean, abs(mA), abs(mD))
        worst_cross = max(worst_cross, abs(cr))
    assert worst_mean < 1e-15 and worst_cross < 1e-15

    # Prop 1.3(a): exact positive covariance for every pair at a non-small eps.
    for w in WS:
        p = true_law(w, 0.7, V_ASYM)
        m = marginals(p, DES_T)
        for t in range(DES_T):
            for u in range(t + 1, DES_T):
                p11 = sum(v for y, v in p.items() if y[t] and y[u])
                assert p11 - m[t] * m[u] > 0
    res["finite_difference_h_error"] = fd_err
    res["max_abs_mean_and_cross_moment"] = [worst_mean, worst_cross]
    return res


def check_local_mechanism():
    """Exact projections versus the eps^4 formulas (homogeneous product candidates)."""
    # Stacked (w,t) vectors and weights at the eps = 0 baseline.
    idx = [(w, t) for w in WS for t in range(DES_T)]
    pi0 = {(w, t): sig(ALPHA[t] - BETA[t] * THBAR[w]) for (w, t) in idx}
    Om = [HW[w] * pi0[(w, t)] * (1 - pi0[(w, t)]) for (w, t) in idx]
    avec = [0.5 * VW[w] * BETA[t] ** 2 * (1 - 2 * pi0[(w, t)]) for (w, t) in idx]
    # S: theta = mu0 + mu1 z (both retain Z); K adds a z-independent extra column.
    colS = [[-BETA[t] for (w, t) in idx], [-BETA[t] * w for (w, t) in idx]]
    colK = colS + [[EXTRA[t] for (w, t) in idx]]
    PSa, PKa = wls_project(avec, Om, colS), wls_project(avec, Om, colK)
    rS_A = wnorm2([u - v for u, v in zip(avec, PSa)], Om)
    rK_A = wnorm2([u - v for u, v in zip(avec, PKa)], Om)
    d2 = wnorm2([u - v for u, v in zip(PKa, PSa)], Om)
    hD2 = sum(HW[w] * VW[w] ** 2 * sum(BETA[t] ** 2 * BETA[u] ** 2 * pi0[(w, t)]
                                       * (1 - pi0[(w, t)]) * pi0[(w, u)] * (1 - pi0[(w, u)])
                                       for t in range(DES_T) for u in range(t + 1, DES_T))
              for w in WS)
    # Frisch-Waugh-Lovell form of ||d||^2 for one extra column.
    e = colK[-1]
    MSe = [u - v for u, v in zip(e, wls_project(e, Om, colS))]
    fwl = (sum(Om[i] * avec[i] * MSe[i] for i in range(len(e)))) ** 2 / wnorm2(MSe, Om)
    assert abs(fwl - d2) < 1e-12 * max(1.0, d2)
    assert d2 > 0 and hD2 > 0

    rows = []
    for Vname, Vd in (("asymmetric_V", V_ASYM), ("symmetric_V", V_SYM)):
        for eps in (0.2, 0.1, 0.05, 0.025, 0.0125, 0.00625):
            laws = {w: true_law(w, eps, Vd) for w in WS}
            pbar = {w: marginals(laws[w], DES_T) for w in WS}
            off = {w: list(ALPHA) for w in WS}
            JS = {w: [[-BETA[t], -BETA[t] * w] for t in range(DES_T)] for w in WS}
            JK = {w: [[-BETA[t], -BETA[t] * w, EXTRA[t]] for t in range(DES_T)] for w in WS}
            phiS, mS = project_product(pbar, HW, off, JS, [0.4, 0.3])
            phiK, mK = project_product(pbar, HW, off, JK, phiS + [0.0])
            info = sum(HW[w] * multi_information(laws[w], DES_T) for w in WS)
            RS, RK = info + mS, info + mK
            # Direct conditional gap at the same joint projections.
            dC = 0.0
            for w in WS:
                qS = product_law([sig(ALPHA[t] - BETA[t] * (phiS[0] + phiS[1] * w))
                                  for t in range(DES_T)])
                qK = product_law([sig(ALPHA[t] - BETA[t] * (phiK[0] + phiK[1] * w)
                                      + EXTRA[t] * phiK[2]) for t in range(DES_T)])
                dC += HW[w] * (conditional_risk(laws[w], qS, DES_T)
                               - conditional_risk(laws[w], qK, DES_T))
                # Lemma 2.3 identity on each w: joint = multi-information + marginal KLs.
                lhs = kl_joint(laws[w], qS)
                rhs = multi_information(laws[w], DES_T) + sum(
                    kl_bern(pbar[w][t], sig(ALPHA[t] - BETA[t] * (phiS[0] + phiS[1] * w)))
                    for t in range(DES_T))
                assert abs(lhs - rhs) < 1e-13
            gap = RS - RK
            assert abs(dC - gap / DES_T) < 1e-12 * max(1.0, gap) + 1e-16
            # Alignment number at the S projection along the extra column.
            A = sum(HW[w] * EXTRA[t] * (pbar[w][t] - sig(ALPHA[t] - BETA[t]
                                                          * (phiS[0] + phiS[1] * w)))
                    for w in WS for t in range(DES_T))
            A_local = eps ** 2 * sum(Om[i] * avec[i] * MSe[i] for i in range(len(e)))
            # Prop 2.5 at the exact S projection (no small-eps approximation inside).
            piS_stack = [sig(ALPHA[t] - BETA[t] * (phiS[0] + phiS[1] * w)) for (w, t) in idx]
            I_eS, Bbar = drift_bounds([[-BETA[t], -BETA[t] * w] for (w, t) in idx],
                                      [EXTRA[t] for (w, t) in idx], piS_stack,
                                      [HW[w] for (w, t) in idx])
            assert A * A / (2 * Bbar) <= gap * (1 + 1e-9) + 1e-18
            rows.append({
                "V": Vname, "eps": eps,
                "R_S_ratio": RS / (0.5 * eps ** 4 * (rS_A + hD2)),
                "R_K_ratio": RK / (0.5 * eps ** 4 * (rK_A + hD2)),
                "gap_ratio": gap / (0.5 * eps ** 4 * d2),
                "multi_info_ratio": info / (0.5 * eps ** 4 * hD2),
                "A_ratio": A / A_local,
                "gap_over_score_test_approx": gap / (A * A / (2 * I_eS)),
                "gap_over_rigorous_lower_bound": gap / (A * A / (2 * Bbar)),
                "Delta_C_equals_gap_over_T": True,
            })
    # Ratios approach one as eps -> 0.
    for r in rows:
        if r["eps"] == 0.00625:
            for key in ("R_S_ratio", "R_K_ratio", "gap_ratio", "multi_info_ratio", "A_ratio"):
                assert abs(r[key] - 1) < 0.06, (r["V"], key, r[key])
    return {"norms": {"||a-P_S a||^2": rS_A, "||a-P_K a||^2": rK_A, "||d||^2": d2,
                      "||h_D||^2": hD2},
            "rows": rows}


# ----------------------------------------------------------------------------
# H1. Hierarchical absorption: free-variance normal random effect absorbs eps^2 term
# ----------------------------------------------------------------------------

NODES = normal_nodes(160, 12.0)


def hier_law(alpha, beta, mu, s2, offset=0.0, T=None):
    """Integrated participant law under a normal working effect theta ~ N(mu, s2)."""
    T = len(alpha) if T is None else T
    out = {y: 0.0 for y in cells(T)}
    s = math.sqrt(s2)
    for e, wt in NODES:
        th = mu + s * e
        pis = [sig(alpha[t] + offset - beta[t] * th) for t in range(T)]
        for y in out:
            out[y] += wt * math.prod(bern(y[t], pis[t]) for t in range(T))
    return out


def check_hierarchical_absorption():
    # One retained-covariate cell; T = 3; truth thbar + eps V.  Compare
    #   (i) the best homogeneous (product) S law  -> KL ~ eps^4,
    #  (ii) the specific hierarchical S law N(thbar, eps^2) -> KL ~ eps^6 (skewed V)
    #       or eps^8 (symmetric V).  (ii) upper-bounds the hierarchical R_S.
    th = 0.4
    v = 1.0
    out = {}
    norm_err = abs(sum(hier_law(ALPHA, BETA, th, 0.3).values()) - 1)
    assert norm_err < 1e-13
    for Vname, Vd, power in (("asymmetric_V", V_ASYM, 6), ("symmetric_V", V_SYM, 8)):
        rat_h, rat_p = [], []
        for eps in (0.2, 0.1, 0.05, 0.025):
            p = {y: 0.0 for y in cells(DES_T)}
            for vv, pv in Vd:
                pis = [sig(ALPHA[t] - BETA[t] * (th + eps * math.sqrt(v) * vv))
                       for t in range(DES_T)]
                for y in p:
                    p[y] += pv * math.prod(bern(y[t], pis[t]) for t in range(DES_T))
            q = hier_law(ALPHA, BETA, th, eps ** 2 * v)
            rat_h.append(kl_joint(p, q) / eps ** power)
            # Best homogeneous S (theta free): multi-information + marginal fit.
            pbar = {0: marginals(p, DES_T)}
            (_,), mS = project_product(pbar, {0: 1.0}, {0: list(ALPHA)},
                                       {0: [[-b] for b in BETA]}, [th])
            rat_p.append((multi_information(p, DES_T) + mS) / eps ** 4)
        out[Vname] = {"hierarchical_KL_over_eps^%d" % power: rat_h,
                      "homogeneous_R_S_over_eps^4": rat_p}
        # Ratios stabilise (bounded, nonvanishing) as eps decreases.
        assert 0.9 < rat_h[-1] / rat_h[-2] < 1.1 and rat_h[-1] > 0
        assert 0.9 < rat_p[-1] / rat_p[-2] < 1.1 and rat_p[-1] > 0
    out["quadrature_normalisation_error"] = norm_err
    return out


# ----------------------------------------------------------------------------
# H2. Parity obstruction (tangent level) for hierarchical S/K retaining Z
# ----------------------------------------------------------------------------

def check_parity():
    T = 3
    alpha = [0.0, 0.0, 0.0]
    beta = [1.0, 2.0, 3.0]
    vbar = 0.6
    hstep = 1e-5

    def laws(mu0, mu1, s2, delta=0.0, lam=0.0, het=False):
        """het=True: truth path Theta|z ~ N(mu0+mu1 z, vbar + lam z)."""
        out = {}
        for z in WS:
            var = (vbar + lam * z) if het else s2
            out[z] = hier_law(alpha, beta, mu0 + mu1 * z, var, offset=delta)
        return out

    def analyse(mu1_base):
        base = (0.4, mu1_base, vbar, 0.0)
        p0 = laws(*base)
        keys = [(z, y) for z in WS for y in cells(T)]
        wts = [HW[z] * p0[z][y] for (z, y) in keys]

        def score(i):
            up, dn = list(base), list(base)
            up[i] += hstep
            dn[i] -= hstep
            lu, ld = laws(*up), laws(*dn)
            return [(math.log(lu[z][y]) - math.log(ld[z][y])) / (2 * hstep) for (z, y) in keys]

        sS = [score(0), score(1), score(2)]  # mu0, mu1, sigma^2
        sE = score(3)  # extra (offset / distortion-like) direction
        lu = laws(0.4, mu1_base, vbar, lam=hstep, het=True)
        ld = laws(0.4, mu1_base, vbar, lam=-hstep, het=True)
        h = [(math.log(lu[z][y]) - math.log(ld[z][y])) / (2 * hstep) for (z, y) in keys]
        PSh = wls_project(h, wts, sS)
        PKh = wls_project(h, wts, sS + [sE])
        d2 = wnorm2([u - v for u, v in zip(PKh, PSh)], wts)
        rS2 = wnorm2([u - v for u, v in zip(h, PSh)], wts)
        eS2 = wnorm2([u - v for u, v in zip(sE, wls_project(sE, wts, sS))], wts)
        return {"||d||^2": d2, "||h-P_S h||^2": rS2, "||s_extra - P_S s_extra||^2": eS2}

    sym = analyse(0.0)
    asym = analyse(0.5)
    assert sym["||d||^2"] < 1e-12 and sym["||h-P_S h||^2"] > 1e-4
    assert sym["||s_extra - P_S s_extra||^2"] > 1e-4  # not absorbed: obstruction is parity
    assert asym["||d||^2"] > 1e-8  # breaking the symmetry restores first-order alignment
    return {"z_symmetric_baseline": sym, "z_asymmetric_baseline_mu1_0.5": asym}


def main():
    results = {
        "scope": ("Diagnostics for docs/central_theorem_full_draft.md; exact rational and "
                  "numerical checks, not proofs or certified global optimisation."),
        "I1_instance": check_instance(),
        "E1_heterogeneity_expansion": check_expansion(),
        "L1_local_mechanism_homogeneous": check_local_mechanism(),
        "H1_hierarchical_absorption": check_hierarchical_absorption(),
        "H2_parity_obstruction": check_parity(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results, indent=2))
    print("all central-theorem draft checks passed")


if __name__ == "__main__":
    main()
