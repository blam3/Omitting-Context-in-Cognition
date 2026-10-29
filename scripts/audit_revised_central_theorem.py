#!/usr/bin/env python3
"""Independent numerical audit of revised_central_theorem.tex (October 2026 revision).

Dependency-free. Recomputes the revised manuscript's explicit numbers and tests
claims that admit a direct check. These are diagnostics: passing them supports
arithmetic and specific instances, not the general proofs.

  R1  Theorem 3.1 witness: cells, projections, gaps, the revised rho box, Prop 5.2.
  R2  Lemma 2.2: product-reduction identities on random positive laws (T = 3).
  R3  Proposition 7.7: joint-versus-conditional sign reversal numbers.
  R4  Theorem 5.1 scope: Lambda = 0 yet Delta_J > 0 (drift is not necessary).
  R5  Corollary 8.1 lemma: positive laws with zero average conditional KL coincide.
  R6  Theorem 7.2 at an interior positive-variance hierarchical baseline:
      exact joint and conditional gaps versus the local projection formulas.
"""
from __future__ import annotations

import itertools
import json
import math
import random
from fractions import Fraction as Fr
from pathlib import Path

OUT = Path("logs/theory_checks/2026-10-29_revised_theorem_audit.json")


def sig(x):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    z = math.exp(x)
    return z / (1 + z)


def logit(p):
    return math.log(p / (1 - p))


def bern(y, p):
    return p if y else 1 - p


def cells(T):
    return list(itertools.product([0, 1], repeat=T))


def kl(p, q):
    return sum(v * math.log(v / q[y]) for y, v in p.items() if v > 0)


def marg_drop(p, t):
    out = {}
    for y, v in p.items():
        k = y[:t] + y[t + 1:]
        out[k] = out.get(k, 0.0) + v
    return out


def cond_risk(p, q, T):
    """(1/T) sum_t [KL(p||q) - KL(p_-t||q_-t)] = average expected conditional KL."""
    j = kl(p, q)
    return sum(j - kl(marg_drop(p, t), marg_drop(q, t)) for t in range(T)) / T


def solve(A, b):
    n = len(A)
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[piv] = M[piv], M[c]
        for r in range(n):
            if r != c and M[r][c]:
                f = M[r][c] / M[c][c]
                for k in range(c, n + 1):
                    M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def newton_min(f, x0, h=1e-4, iters=60, tol=1e-12):
    """Damped Newton with central-difference derivatives (smooth low-dimensional f)."""
    x = list(x0)
    k = len(x)
    fx = f(x)
    for _ in range(iters):
        g = []
        H = [[0.0] * k for _ in range(k)]
        for a in range(k):
            e = [0.0] * k
            e[a] = h
            fp, fm = f([x[i] + e[i] for i in range(k)]), f([x[i] - e[i] for i in range(k)])
            g.append((fp - fm) / (2 * h))
            H[a][a] = (fp - 2 * fx + fm) / h ** 2
        for a in range(k):
            for b in range(a + 1, k):
                pp = f([x[i] + (h if i in (a, b) else 0) for i in range(k)])
                pm = f([x[i] + (h if i == a else -h if i == b else 0) for i in range(k)])
                mp = f([x[i] + (-h if i == a else h if i == b else 0) for i in range(k)])
                mm = f([x[i] - (h if i in (a, b) else 0) for i in range(k)])
                H[a][b] = H[b][a] = (pp - pm - mp + mm) / (4 * h * h)
        step = solve(H, g)
        lam = 1.0
        while lam > 1e-10:
            xn = [x[i] - lam * step[i] for i in range(k)]
            fn = f(xn)
            if fn <= fx + 1e-15:
                break
            lam /= 2
        x, fx = xn, fn
        if max(abs(lam * s) for s in step) < tol:
            break
    return x, fx


# ---------------------------------------------------------------------------
# R1. Theorem 3.1 witness
# ---------------------------------------------------------------------------

def r1_witness():
    rates = {0: (Fr(1, 2), Fr(1, 2)), 1: (Fr(1, 4), Fr(1, 10))}
    P = {y: sum(math.prod(bern(y[t], rates[c][t]) for t in range(2)) for c in (0, 1)) / 2
         for y in cells(2)}
    assert [P[(0, 0)], P[(1, 0)], P[(0, 1)], P[(1, 1)]] == [Fr(37, 80), Fr(19, 80),
                                                            Fr(13, 80), Fr(11, 80)]
    pf = {y: float(v) for y, v in P.items()}
    m = [3 / 8, 3 / 10]
    # Simple projection: unique root of sum_t x_t (sig(-x_t th) - p_t) = 0 by bisection.
    lo, hi = 0.0, 2.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if sum(x * (sig(-x * mid) - pt) for x, pt in zip((1, 2), m)) > 0:
            lo = mid
        else:
            hi = mid
    thS = (lo + hi) / 2
    prod = lambda pis: {y: math.prod(bern(y[t], pis[t]) for t in range(2)) for y in cells(2)}
    qS = prod([sig(-thS), sig(-2 * thS)])
    thK, dK = math.log(7 / 5), math.log(21 / 25)
    qK = prod([sig(dK - thK), sig(dK - 2 * thK)])
    RS, RK = kl(pf, qS), kl(pf, qK)
    dJ = RS - RK
    dC = cond_risk(pf, qS, 2) - cond_risk(pf, qK, 2)
    assert abs(dC - dJ / 2) < 1e-15
    w = lambda p, r: math.exp(-(-math.log(p)) ** r)
    delta = lambda r: 4 * (w(0.5, r) - 0.5)
    L2 = math.log(2)
    rhoK = math.log(-math.log(0.5 + dK / 4)) / math.log(L2)
    box = (delta(0.25), delta(2.0))
    assert box[0] < dK < box[1] and 0.25 < rhoK < 2
    # Prop 5.2 in the delta coordinate on the revised box.
    pis = [sig(-thS), sig(-2 * thS)]
    om = [pi * (1 - pi) for pi in pis]
    Lam = sum(mt - pt for mt, pt in zip(m, pis))
    gss = sum(o * x * x for o, x in zip(om, (1, 2)))
    gse = sum(o * (-x) for o, x in zip(om, (1, 2)))
    coef = gse / gss
    c = [1 - (-x) * coef for x in (1, 2)]
    B = 0.25 * sum(ci * ci for ci in c)
    s = Lam / B
    th_end = thS - s * coef
    feasible = box[0] < s < box[1] and 0 <= th_end <= 2
    bound = Lam ** 2 / (2 * B)
    assert feasible and bound <= dJ
    return {"theta_S_star_12dp": round(thS, 12),
            "manuscript_theta_S_star": 0.4429045138,
            "theta_S_discrepancy": thS - 0.4429045138,
            "R_S": RS, "R_K": RK, "Delta_J": dJ, "Delta_C": dC, "rho_K_star": rhoK,
            "delta_range_for_rho_in_[1/4,2]": box,
            "prop_5_2_step_s": s, "prop_5_2_theta_at_step": th_end,
            "prop_5_2_bound": bound}


# ---------------------------------------------------------------------------
# R2. Lemma 2.2 on random positive laws
# ---------------------------------------------------------------------------

def r2_product_reduction(trials=200):
    rng = random.Random(20261029)
    T = 3
    worst = 0.0
    for _ in range(trials):
        raw = {y: rng.random() + 0.05 for y in cells(T)}
        z = sum(raw.values())
        p = {y: v / z for y, v in raw.items()}
        pm = [sum(v for y, v in p.items() if y[t]) for t in range(T)]
        prodp = {y: math.prod(bern(y[t], pm[t]) for t in range(T)) for y in cells(T)}
        I = kl(p, prodp)
        for _ in range(2):
            qt = [rng.uniform(0.05, 0.95) for _ in range(T)]
            q = {y: math.prod(bern(y[t], qt[t]) for t in range(T)) for y in cells(T)}
            margs = sum(pm[t] * math.log(pm[t] / qt[t]) + (1 - pm[t]) * math.log((1 - pm[t]) / (1 - qt[t]))
                        for t in range(T))
            worst = max(worst, abs(kl(p, q) - (I + margs)))
            # Conditional identity, eq (productC), for each t.
            for t in range(T):
                pdrop = marg_drop(p, t)
                lhs = sum(v * math.log((v / pdrop[y[:t] + y[t + 1:]]) / bern(y[t], qt[t]))
                          for y, v in p.items())
                It = sum(v * math.log(v / (pdrop[y[:t] + y[t + 1:]] * bern(y[t], pm[t])))
                         for y, v in p.items())
                kt = pm[t] * math.log(pm[t] / qt[t]) + (1 - pm[t]) * math.log((1 - pm[t]) / (1 - qt[t]))
                worst = max(worst, abs(lhs - (It + kt)))
    assert worst < 1e-12
    return {"max_identity_error": worst, "random_laws": trials}


# ---------------------------------------------------------------------------
# R3. Proposition 7.7 reversal
# ---------------------------------------------------------------------------

def r3_reversal():
    order = [(0, 0), (0, 1), (1, 0), (1, 1)]
    vec = lambda xs: dict(zip(order, xs))
    p, s, k = vec([.27, .28, .33, .12]), vec([.11, .12, .19, .58]), vec([.68, .05, .06, .21])
    seg = lambda lam: {y: s[y] + lam * (k[y] - s[y]) for y in order}
    dfun = lambda lam: -sum(p[y] * (k[y] - s[y]) / seg(lam)[y] for y in order)
    assert dfun(0) < 0 < dfun(1)
    lo, hi = 0.0, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if dfun(mid) < 0 else (lo, mid)
    lam = (lo + hi) / 2
    qK = seg(lam)
    dJ = kl(p, s) - kl(p, qK)
    dC = cond_risk(p, s, 2) - cond_risk(p, qK, 2)
    assert dJ > 0 > dC
    return {"lambda_star": lam, "Delta_J": dJ, "Delta_C": dC, "R_K": kl(p, qK),
            "manuscript": {"lambda_star": 0.281900, "Delta_J": 0.098320, "Delta_C": -0.052440}}


# ---------------------------------------------------------------------------
# R4. Lambda = 0 but Delta_J > 0 (drift sufficient, not necessary)
# ---------------------------------------------------------------------------

def r4_drift_not_necessary():
    """K: logit -rho^2 - theta x_t, rho in R, embeds S at rho = 0 with zero first derivative.

    d eta / d rho = -2 rho = 0 at rho = 0, so Lambda = 0 identically, yet K contains every
    nonpositive offset, including the witness optimum delta = log(21/25) < 0.
    """
    m = [3 / 8, 3 / 10]
    lo, hi = 0.0, 2.0
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if sum(x * (sig(-x * mid) - pt) for x, pt in zip((1, 2), m)) > 0 else (lo, mid)
    thS = (lo + hi) / 2
    Lambda = sum((-2 * 0.0) * (mt - sig(-x * thS)) for mt, x in zip(m, (1, 2)))
    margkl = lambda a, b: a * math.log(a / b) + (1 - a) * math.log((1 - a) / (1 - b))
    marg_S = sum(margkl(mt, sig(-x * thS)) for mt, x in zip(m, (1, 2)))
    rho = math.sqrt(-math.log(21 / 25))
    marg_K = sum(margkl(mt, sig(-rho ** 2 - x * math.log(7 / 5))) for mt, x in zip(m, (1, 2)))
    assert Lambda == 0 and marg_K < 1e-15 and marg_S > 6e-4
    return {"Lambda": Lambda, "Delta_J": marg_S - marg_K, "rho_K": rho}


# ---------------------------------------------------------------------------
# R5. Corollary 8.1: zero average conditional KL forces equality (positive laws)
# ---------------------------------------------------------------------------

def r5_conditional_identification(trials=300):
    rng = random.Random(7)
    T = 3
    smallest = float("inf")
    for _ in range(trials):
        mk = lambda: (lambda r: {y: v / sum(r.values()) for y, v in r.items()})(
            {y: rng.random() + 0.02 for y in cells(T)})
        p, q = mk(), mk()
        c = cond_risk(p, q, T)
        smallest = min(smallest, c / kl(p, q))
    assert smallest > 0
    return {"min_ratio_conditional_to_joint_KL": smallest}


# ---------------------------------------------------------------------------
# R6. Theorem 7.2 at an interior positive-variance hierarchical baseline
# ---------------------------------------------------------------------------

def gauss_legendre(n):
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


LQ = 12.0
NODES = [(LQ * x, LQ * w * math.exp(-0.5 * (LQ * x) ** 2) / math.sqrt(2 * math.pi))
         for x, w in gauss_legendre(160)]
T6 = 3
KAP = [0.3, -0.2, 0.1]
BET = [1.0, 2.0, 3.0]
EXT = [0.5, -0.3, 0.8]  # extra logit signature of K (a stand-in for d eta / d rho)
MU0, LV0 = 0.4, math.log(0.5)


def hier(mu, logv, delta=0.0, lam=0.0):
    """Integrated law with latent theta = mu + sd*(E + lam*(E^2-1)), E ~ N(0,1)."""
    sd = math.exp(0.5 * logv)
    out = {y: 0.0 for y in cells(T6)}
    for e, w in NODES:
        th = mu + sd * (e + lam * (e * e - 1))
        pis = [sig(KAP[t] + delta * EXT[t] - BET[t] * th) for t in range(T6)]
        for y in out:
            out[y] += w * math.prod(bern(y[t], pis[t]) for t in range(T6))
    z = sum(out.values())
    return {y: v / z for y, v in out.items()}


def r6_hierarchical_local():
    p0 = hier(MU0, LV0)
    ys = cells(T6)
    hs = 1e-5

    def score(fn):
        up, dn = fn(hs), fn(-hs)
        return [(math.log(up[y]) - math.log(dn[y])) / (2 * hs) for y in ys]

    sS = [score(lambda d: hier(MU0 + d, LV0)), score(lambda d: hier(MU0, LV0 + d))]
    sE = score(lambda d: hier(MU0, LV0, delta=d))
    h = score(lambda d: hier(MU0, LV0, lam=d))
    wts = [p0[y] for y in ys]
    ip = lambda a, b: sum(w * x * z for w, x, z in zip(wts, a, b))

    def proj(v, basis):
        G = [[ip(a, b) for b in basis] for a in basis]
        co = solve(G, [ip(a, v) for a in basis])
        return [sum(co[j] * basis[j][i] for j in range(len(basis))) for i in range(len(v))]

    PS, PK = proj(h, sS), proj(h, sS + [sE])
    rS = [a - b for a, b in zip(h, PS)]
    rK = [a - b for a, b in zip(h, PK)]
    d = [a - b for a, b in zip(PK, PS)]

    def Aop(f):
        fd = dict(zip(ys, f))
        out = []
        for y in ys:
            tot = 0.0
            for t in range(T6):
                num = den = 0.0
                for yt in (0, 1):
                    yy = y[:t] + (yt,) + y[t + 1:]
                    num += p0[yy] * fd[yy]
                    den += p0[yy]
                tot += fd[y] - num / den
            out.append(tot / T6)
        return out

    Ad = Aop(d)
    L = ip(d, Ad) + 2 * ip(rK, Ad)
    pred = {"R_S": 0.5 * ip(rS, rS), "R_K": 0.5 * ip(rK, rK), "Delta_J": 0.5 * ip(d, d),
            "Delta_C": 0.5 * L}
    rows = []
    for lam in (0.08, 0.04, 0.02, 0.01):
        p = hier(MU0, LV0, lam=lam)
        fS = lambda x: kl(p, hier(x[0], x[1]))
        fK = lambda x: kl(p, hier(x[0], x[1], delta=x[2]))
        xS, RS = newton_min(fS, [MU0, LV0])
        xK, RK = newton_min(fK, xS + [0.0])
        qS, qK = hier(*xS), hier(xK[0], xK[1], delta=xK[2])
        CS, CK = cond_risk(p, qS, T6), cond_risk(p, qK, T6)
        rows.append({"lambda": lam,
                     "R_S_ratio": RS / (lam ** 2 * pred["R_S"]),
                     "R_K_ratio": RK / (lam ** 2 * pred["R_K"]),
                     "Delta_J_ratio": (RS - RK) / (lam ** 2 * pred["Delta_J"]),
                     "Delta_C_ratio": (CS - CK) / (lam ** 2 * pred["Delta_C"]),
                     "Delta_J": RS - RK, "Delta_C": CS - CK})
    # Risks match the leading term directly. The gaps have a tiny leading coefficient
    # (||d||^2 << ||r_S||^2), so next-order terms dominate unless lambda is very small;
    # extrapolate ratio(lambda) = c0 + c1 lambda + c2 lambda^2 from the last three rows.
    last = rows[-1]
    assert abs(last["R_S_ratio"] - 1) < 0.01 and abs(last["R_K_ratio"] - 1) < 0.01
    extrap = {}
    for key in ("Delta_J_ratio", "Delta_C_ratio"):
        (l1, r1), (l2, r2), (l3, r3) = [(r["lambda"], r[key]) for r in rows[-3:]]
        # Quadratic through three points evaluated at lambda = 0 (Lagrange).
        c0 = (r1 * l2 * l3 / ((l1 - l2) * (l1 - l3)) + r2 * l1 * l3 / ((l2 - l1) * (l2 - l3))
              + r3 * l1 * l2 / ((l3 - l1) * (l3 - l2)))
        extrap[key] = c0
        assert abs(c0 - 1) < 0.05, (key, c0)
    return {"coefficients_per_lambda^2": pred, "L": L,
            "leading_gap_over_leading_R_S": pred["Delta_J"] / pred["R_S"],
            "rows": rows, "extrapolated_ratio_at_lambda_0": extrap}


def main():
    res = {
        "scope": "Independent audit diagnostics for revised_central_theorem.tex; not proofs.",
        "R1_witness": r1_witness(),
        "R2_product_reduction": r2_product_reduction(),
        "R3_reversal": r3_reversal(),
        "R4_drift_not_necessary": r4_drift_not_necessary(),
        "R5_conditional_identification": r5_conditional_identification(),
        "R6_hierarchical_local_theorem_7_2": r6_hierarchical_local(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(res, indent=2) + "\n")
    print(json.dumps(res, indent=2))
    print("all audit checks passed")


if __name__ == "__main__":
    main()
