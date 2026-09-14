#!/usr/bin/env python3
"""D1 adversarial-review arithmetic, independent of the author verifier.

Standard library only. Exact fractions check joint laws and counterexamples;
60-digit Decimal checks support, but do not replace, the analytical KL proof.
"""
import argparse
from decimal import Decimal as D, localcontext
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path

STATES = tuple(product((0, 1), repeat=2))  # 00, 01, 10, 11


def cells(p1, p2):
    return {w: (p1 if w[0] else 1-p1)*(p2 if w[1] else 1-p2) for w in STATES}


def run():
    low, high = cells(F(1, 2), F(1, 2)), cells(F(3, 4), F(9, 10))
    p = {w: (low[w]+high[w])/2 for w in STATES}
    assert p == {(0, 0): F(11, 80), (0, 1): F(19, 80),
                 (1, 0): F(13, 80), (1, 1): F(37, 80)}
    assert sum(p.values()) == 1 and min(p.values()) > 0
    marg = [sum(prob for w, prob in p.items() if w[t]) for t in (0, 1)]
    assert marg == [F(5, 8), F(7, 10)]
    prod_marg = cells(*marg)
    covariance = p[(1, 1)]-marg[0]*marg[1]
    determinant = p[(0, 0)]*p[(1, 1)]-p[(0, 1)]*p[(1, 0)]
    assert covariance == determinant == F(1, 40) and p != prod_marg
    # Z is a baseline fair bit, independent of U. Theta is constant.
    # Independence of trials given Theta does not imply independence given Z,Theta.
    conditional = {z: {w: F(0) for w in STATES} for z in (0, 1)}
    for z, u in product((0, 1), repeat=2):
        conditional[z][(u, u ^ z)] += F(1, 2)
    unconditional = {w: (conditional[0][w]+conditional[1][w])/2 for w in STATES}
    assert unconditional == low
    for z in (0, 1):
        for t in (0, 1):
            assert sum(prob for w, prob in conditional[z].items() if w[t]) == F(1, 2)
        assert conditional[z] != low
    # X=Theta; an independent fair response has the same integrated kernel
    # under two unequal mixing distributions. Exogeneity is sufficient, not necessary.
    for x in (0, 1):
        dep, marginal = [F(int(t == x)) for t in (0, 1)], [F(1, 2), F(1, 2)]
        assert dep != marginal
        assert sum(w*F(1, 2) for w in dep) == sum(w*F(1, 2) for w in marginal)
    with localcontext() as ctx:
        ctx.prec = 60
        dec = lambda f: D(f.numerator)/D(f.denominator)
        sig = lambda x: 1/(1+(-x).exp())
        a1, a2 = dec(F(5, 3)).ln(), dec(F(7, 3)).ln()
        bk, dk = 2*a1-a2/2, a2/2-a1
        assert -1 < bk < 1 and -1 < dk < 1 and dk != 0
        score = lambda b: dec(marg[0])-sig(b)+2*(dec(marg[1])-sig(2*b))
        left, right = a2/2, a1
        assert score(left) > 0 > score(right)
        for _ in range(150):
            middle = (left+right)/2
            if score(middle) > 0:
                left = middle
            else:
                right = middle
        bs = (left+right)/2
        qk, qs = cells(sig(bk+dk), sig(2*bk+4*dk)), cells(sig(bs), sig(2*bs))
        pd = {w: dec(prob) for w, prob in p.items()}
        risk = lambda q: sum(pd[w]*(pd[w]/q[w]).ln() for w in STATES)
        rk, rs = risk(qk), risk(qs)
        assert 0 < rk < rs
        assert max(abs(qk[w]-dec(prod_marg[w])) for w in STATES) < D('1e-55')
        arbitrary = [D('0.2'), D('0.8')]
        marginal_kl = sum(dec(pm)*(dec(pm)/qm).ln()+(1-dec(pm))*((1-dec(pm))/(1-qm)).ln()
                          for pm, qm in zip(marg, arbitrary))
        assert abs(risk(cells(*arbitrary))-rk-marginal_kl) < D('1e-55')
        # A different two-parameter model (intercept+slope) ties K at two levels.
        intercept, slope = 2*a1-a2, a2-a1
        qi = cells(sig(intercept+slope), sig(intercept+2*slope))
        assert max(abs(qi[w]-qk[w]) for w in STATES) < D('1e-55')
        return {'checks': 'passed', 'arithmetic': 'exact Fraction; Decimal precision 60',
                'cells_by_response_pair': {str(w): str(prob) for w, prob in p.items()},
                'covariance': str(covariance), 'independence_determinant': str(determinant),
                'simple_optimum': str(bs), 'complex_optimum': [str(bk), str(dk)],
                'R_K': str(rk), 'R_S': str(rs), 'Delta_per_participant': str(rs-rk),
                'conditional_independence_counterexample': {
                    'construction': 'Z,U independent fair bits; Theta constant; Y1=U; Y2=U xor Z',
                    'given_Z_0': {str(w): str(prob) for w, prob in conditional[0].items()},
                    'given_Z_1': {str(w): str(prob) for w, prob in conditional[1].items()},
                    'unconditional': {str(w): str(prob) for w, prob in unconditional.items()}},
                'additional_checks': ['KL decomposition at an arbitrary product distribution',
                                      'Constant-kernel exogeneity counterexample',
                                      'Intercept-plus-slope alternative ties quadratic marginal fit'],
                'limits': 'Arithmetic supports a separate LLM review pass; no simulation, criterion re-verification or independent external review.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(run(), indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text+'\n')
    print(text)
