#!/usr/bin/env python3
"""Numerical checks of PROOF_PACKAGE.md, not a proof or a selection-rate study.

Requires numpy. Run from the repository root; optional --output writes
JSON. Bayesian integrals use tensor Gauss-Legendre quadrature with a refinement
check. LOO deletes a complete pair; four distinct response patterns suffice.
"""
import argparse
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
def expit(value):
    return 1 / (1 + np.exp(-np.asarray(value)))


def logsumexp(values):
    peak = np.max(values)
    return peak + np.log(np.exp(values-peak).sum())


def decreasing_root(function, left=-1., right=1.):
    # Maximizer of a concave scalar objective from its decreasing derivative.
    if function(left) <= 0:
        return left
    if function(right) >= 0:
        return right
    for _ in range(64):
        middle = (left+right)/2
        if function(middle) > 0:
            left = middle
        else:
            right = middle
    return (left+right)/2

STATES = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
TRUE = np.array([11, 13, 19, 37]) / 80
X = np.array([1., 2.])


def log_prob(theta, model):
    theta = np.atleast_2d(theta)
    design = X[:, None] if model == 'S' else np.column_stack((X, X**2))
    eta = theta @ design.T
    return eta @ STATES.T - np.logaddexp(0, eta).sum(axis=1)[:, None]


def kl(p, q):
    return float(np.sum(p * np.log(p / q)))


def fitted_loglik(counts, model):
    n = counts.sum()
    successes = counts @ STATES
    def best_b(d):
        return decreasing_root(lambda b: (successes-n*expit(b*X+d*X**2)) @ X)
    if model == 'S':
        theta = [best_b(0.)]
    else:
        # Profile likelihood is concave in d; optimize its envelope derivative.
        d = decreasing_root(lambda d: (successes-n*expit(best_b(d)*X+d*X**2)) @ X**2)
        theta = [best_b(d), d]
    return float(log_prob(theta, model)[0] @ counts)


def integrals(counts, model, order):
    nodes, weights = leggauss(order)
    if model == 'S':
        theta = nodes[:, None]
        log_weights = np.log(weights / 2)
    else:
        a, b = np.meshgrid(nodes, nodes, indexing='ij')
        theta = np.column_stack((a.ravel(), b.ravel()))
        log_weights = np.log(np.outer(weights, weights).ravel() / 4)
    lp = log_prob(theta, model)
    log_integrand = lp @ counts + log_weights
    lm = float(logsumexp(log_integrand))
    # p(w_i|W_-i) = m(W)/m(W_-i), deleting the entire two-trial pair.
    loo = sum(float(counts[w]) * (lm - float(logsumexp(log_integrand-lp[:, w])))
              for w in range(4) if counts[w] > 0)
    return np.array([lm, loo])


def refined_integrals(counts, model):
    previous = integrals(counts, model, 48)
    for order in (96, 192, 384, 768):
        current = integrals(counts, model, order)
        error = float(np.max(np.abs(current-previous)))
        if error < 1e-6:
            return current, order, error
        previous = current
    raise RuntimeError(f'{model}: quadrature refinement did not converge by 768 nodes')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    # Reconstruct the whole participant mixture, not just its marginals.
    p_context = [expit(np.zeros(2)), expit(np.log(3)*X)]
    reconstructed = sum(np.prod(p**STATES * (1-p)**(1-STATES), axis=1)
                        for p in p_context)/2
    np.testing.assert_allclose(reconstructed, TRUE, atol=1e-14)
    marginal = TRUE @ STATES
    np.testing.assert_allclose(marginal, [5/8, 7/10], atol=1e-14)
    covariance = TRUE[3] - np.prod(marginal)
    assert abs(covariance-1/40) < 1e-14
    a1, a2 = np.log(5/3), np.log(7/3)
    theta_k = np.array([2*a1-a2/2, a2/2-a1])
    b_s = decreasing_root(lambda b: (marginal-expit(b*X)) @ X, a2/2, a1)
    qk = np.exp(log_prob(theta_k, 'K')[0])
    qs = np.exp(log_prob([b_s], 'S')[0])
    product = np.prod(marginal**STATES*(1-marginal)**(1-STATES), axis=1)
    np.testing.assert_allclose(qk, product, atol=1e-14)
    risk_k, risk_s = kl(TRUE, qk), kl(TRUE, qs)
    assert 0 < risk_k < risk_s
    bern_gap = sum(kl(np.array([p, 1-p]), np.array([q, 1-q]))
                   for p, q in zip(marginal, expit(b_s*X)))
    assert abs((risk_s-risk_k)-bern_gap) < 1e-13
    # A degenerate context removes both dependence and curvature advantage.
    null = np.exp(log_prob([0.5], 'S')[0])
    np.testing.assert_allclose(null, np.exp(log_prob([0.5, 0.], 'K')[0]))
    # Every q is a normalized probability on four response vectors.
    for model, parameters in [('S', [[-1], [0], [1]]),
                              ('K', [[-1, -1], [0, 0], [1, 1]])]:
        np.testing.assert_allclose(np.exp(log_prob(parameters, model)).sum(axis=1), 1)
    rng = np.random.default_rng(20260905)
    examples = []
    for n in (80, 400, 1600):
        counts = rng.multinomial(n, TRUE)
        results = {}
        for model, k in [('S', 1), ('K', 2)]:
            ll = fitted_loglik(counts, model)
            integral, order, error = refined_integrals(counts, model)
            results[model] = {'loglik': ll, 'bic': -2*ll+k*np.log(n),
                              'log_evidence': float(integral[0]),
                              'lopoic': float(-2*integral[1]),
                              'quadrature_order': order, 'refinement_error': error}
        gain = results['K']['loglik']-results['S']['loglik']
        bic_diff = results['K']['bic']-results['S']['bic']
        assert abs(bic_diff-(-2*gain+np.log(n))) < 1e-9
        examples.append({'participants': n, 'counts_00_10_01_11': counts.tolist(),
                         'bic_K_minus_S': bic_diff,
                         'log_BF_K_over_S': results['K']['log_evidence']-results['S']['log_evidence'],
                         'lopoic_K_minus_S': results['K']['lopoic']-results['S']['lopoic'],
                         'models': results})
    report = {'seed': 20260905, 'unit': 'participant response pair',
              'prior': 'uniform [-1,1]^k', 'true_cells': TRUE.tolist(),
              'simple_optimum': b_s, 'complex_optimum': theta_k.tolist(),
              'R_K': risk_k, 'R_S': risk_s, 'Delta_per_participant': risk_s-risk_k,
              'checks': 'passed', 'finite_sample_examples': examples,
              'limits': 'Three seeded datasets, not selection rates or a proof; quadrature is numerical, not symbolic exact integration.'}
    content = json.dumps(report, indent=2, allow_nan=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(content+'\n')
    print(content)


if __name__ == '__main__':
    main()
