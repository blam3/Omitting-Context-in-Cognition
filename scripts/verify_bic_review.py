#!/usr/bin/env python3
"""Exact finite-support checks for the D2 BIC review; no simulation/packages.

Checks sufficient-statistic variances and exact multinomial tail probabilities.
These calculations support, but do not replace, the analytical review.
"""
from fractions import Fraction as F
from math import factorial, exp, sqrt, log
from itertools import product
from pathlib import Path
import argparse
import json


def run():
    states = [(0, 0), (1, 0), (0, 1), (1, 1)]
    p = [F(11, 80), F(13, 80), F(19, 80), F(37, 80)]
    a = [y1+2*y2 for y1, y2 in states]
    b = [y1+4*y2 for y1, y2 in states]
    mean_a, mean_b = [sum(pi*v for pi, v in zip(p, values)) for values in [a, b]]
    var_a, var_b = [sum(pi*(v-mu)**2 for pi, v in zip(p, values))
                    for values, mu in [(a, mean_a), (b, mean_b)]]
    assert (mean_a, mean_b) == (F(81, 40), F(137, 40))
    assert (var_a, var_b) == (F(1879, 1600), F(6071, 1600))
    coefficient = 4*(var_a+var_b)
    assert coefficient == F(159, 8)
    thresholds = [F(1, 4), F(1), F(2), F(4), F(6)]
    tests = []
    for n in [1, 2, 4, 8]:
        tails = {u: F(0) for u in thresholds}
        total = F(0)
        vectors = 0
        for c0 in range(n+1):
            for c1 in range(n-c0+1):
                for c2 in range(n-c0-c1+1):
                    counts = [c0, c1, c2, n-c0-c1-c2]
                    mass = F(factorial(n))
                    for c, pi in zip(counts, p):
                        mass *= pi**c/F(factorial(c))
                    total += mass
                    vectors += 1
                    e_a = sum(c*v for c, v in zip(counts, a))/F(n)-mean_a
                    e_b = sum(c*v for c, v in zip(counts, b))/F(n)-mean_b
                    u_exact = abs(e_a)+abs(e_b)
                    # Supremum of the linear empirical-minus-population error
                    # over the compact quadratic box occurs at these corners.
                    assert max(abs(beta*e_a+d*e_b) for beta, d in product([-1, 1], repeat=2)) == u_exact
                    for u in thresholds:
                        if u_exact >= u:
                            tails[u] += mass
        assert total == 1
        for u, tail in tails.items():
            bound = min(F(1), coefficient/(n*u*u))
            assert tail <= bound
            tests.append({'participants': n, 'count_vectors': vectors,
                          'u': str(u), 'exact_P_U_ge_u': str(tail),
                          'upper_bound': str(bound)})
    # Curvature constants: G_K has positive eigenvalues 11 +/- sqrt(117).
    eig_min, eig_max = 11-sqrt(117), 11+sqrt(117)
    assert eig_min > 0 and abs(eig_min*eig_max-4) < 1e-12
    sigma_prime_6 = exp(-6)/(1+exp(-6))**2
    m = 2*log(1+exp(6))
    return {'checks':'passed', 'means_A_B':[str(mean_a),str(mean_b)],
            'variances_A_B':[str(var_a),str(var_b)],
            'uniform_tail_coefficient':str(coefficient),
            'BIC_failure_coefficient':str(4*coefficient),
            'original_uniform_tail_coefficient_approx':16*m*m,
            'coefficient_improvement_factor_approx':16*m*m/float(coefficient),
            'lambda_S_approx':5*sigma_prime_6,
            'lambda_K_approx':eig_min*sigma_prime_6,
            'exact_tail_checks':tests,
            'limits':'Exact checks for four small participant counts; no selection-rate study. The analytical review proves the bound for all n.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    report = json.dumps(run(),indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(report+'\n')
    print(report)
