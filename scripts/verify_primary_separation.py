#!/usr/bin/env python3
"""Bounded algebra/quadrature diagnostics; not a separation search or proof certificate."""
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
from numpy.polynomial.hermite import hermgauss

def expit(x):
    return np.exp(-np.logaddexp(0., -x))

ROOT = Path(__file__).resolve().parents[1]
CELLS = np.array(list(itertools.product([0, 1], repeat=2)))
PA, PR = np.array([.25, .75]), np.array([.5, .5])
B, SIDE = np.array([.125, .25]), np.array([-1., 1.])

def distortion(p, rho):
    return np.exp(-(-np.log(p))**rho)

def law_from_theta(theta, weights, alpha=0., beta=0., tau=1., rho=1.):
    eta = alpha + beta * SIDE + tau * (distortion(PA, rho) - distortion(PR, rho) - np.asarray(theta)[:, None] * B)
    prob = expit(eta)
    return np.array([np.dot(weights, np.prod(np.where(y, prob, 1-prob), axis=1)) for y in CELLS])

def normal_law(z, par, order=64):
    alpha, beta, tau, mu0, mu1, sd, rho = par
    nodes, weights = hermgauss(order)
    return law_from_theta(mu0+mu1*z+sd*np.sqrt(2)*nodes, weights/np.sqrt(np.pi), alpha, beta, tau, rho)

def marginal(q, y, t):
    return q[CELLS[:, 1-t] == y[1-t]].sum()

def run():
    max_boundary = 0.
    max_refine = 0.
    boundary_laws = {}
    for z in [-1, 1]:
        par = [0., 0., 1., 1., .75, np.sqrt(1.25), 1.]
        q = normal_law(z, par)
        nodes, w = hermgauss(32)
        # Independent C~N(1+z/2,1), u~N(0,1/4), theta=z/4+C+u.
        theta = z/4 + 1+z/2 + np.sqrt(2)*nodes[:, None] + .5*np.sqrt(2)*nodes[None, :]
        direct = law_from_theta(theta.ravel(), (w[:, None]*w[None, :]/np.pi).ravel())
        max_boundary = max(max_boundary, np.max(np.abs(q-direct)))
        max_refine = max(max_refine, np.max(np.abs(q-normal_law(z, par, 128))))
        assert abs(q.sum()-1) < 1e-12 and q.min() > 0
        boundary_laws[str(z)] = q.tolist()
    assert max_boundary < 1e-11 and max_refine < 1e-11

    max_absorption = 0.
    for rho in [.25, .5, 1., 1.5, 3.]:
        delta = distortion(PA, rho)-distortion(PR, rho)-(PA-PR)
        h0, hs = delta.mean(), (delta[1]-delta[0])/2
        for z in [-1, 1]:
            pk = [.2, -.3, 1.2, -.4, .6, .7, rho]
            ps = [pk[0]+pk[2]*h0, pk[1]+pk[2]*hs, *pk[2:6], 1.]
            qk, qs = normal_law(z, pk), normal_law(z, ps)
            max_absorption = max(max_absorption, np.max(np.abs(qk-qs)))
            for e in [-2., -.3, 0., 1.7]:
                eta_k = pk[0]+pk[1]*SIDE+pk[2]*(distortion(PA,rho)-distortion(PR,rho)-B*(pk[3]+pk[4]*z+pk[5]*e))
                eta_s = ps[0]+ps[1]*SIDE+ps[2]*(PA-PR-B*(ps[3]+ps[4]*z+ps[5]*e))
                assert np.max(np.abs(eta_k-eta_s)) < 1e-12
    assert max_absorption < 1e-12

    finite_context = {}
    for z, amplitude in [(-1, 1.), (1, 2.)]:
        p = law_from_theta(np.array([-amplitude, amplitude]), np.array([.5, .5]))
        finite_context[str(z)] = {'mean_C': 0., 'var_C': amplitude**2, 'response_law': p.tolist()}
        assert abs(p.sum()-1) < 1e-12

    # A diagnostic finite global-prior grid: this is NOT the plan's continuous prior.
    # Normal shared effects and the exact G1 kernel are still integrated by GH.
    pars = [[0., 0., 1., 1., .75, np.sqrt(1.25), 1.],
            [.3, -.2, .8, -.5, .2, .6, .5],
            [-.2, .1, 1.4, .7, -.3, .9, 1.5]]
    prior = np.array([.2, .3, .5])
    data = [(1, 1), (-1, 2), (1, 3)]  # (z, response-cell index)
    likelihoods = np.array([[normal_law(z, par) for z, _ in data] for par in pars])
    full_terms = np.array([np.prod([likelihoods[j,i,y] for i,(_,y) in enumerate(data)]) for j in range(len(pars))])
    full_evidence = prior @ full_terms
    max_delete = 0.
    for i, (_, yindex) in enumerate(data):
        y = CELLS[yindex]
        for t in [0, 1]:
            other = np.array([np.prod([likelihoods[j,k,c] for k,(_,c) in enumerate(data) if k != i]) for j in range(len(pars))])
            retained = np.array([marginal(likelihoods[j,i], y, t) for j in range(len(pars))])
            deleted_evidence = prior @ (other * retained)
            posterior = prior*other*retained/deleted_evidence
            conditional = likelihoods[:,i,yindex]/retained
            prediction = posterior @ conditional
            max_delete = max(max_delete, abs(prediction-full_evidence/deleted_evidence))
            assert 0 < prediction < 1
    assert max_delete < 1e-12
    q = np.array(boundary_laws['1'])
    unconditional = q[CELLS[:,0] == 1].sum()
    retained_prediction = q[3]/q[CELLS[:,1] == 1].sum()
    assert abs(retained_prediction-unconditional) > 1e-4

    # Deterministic empirical-frequency sequence, not Monte Carlo or production fitting.
    # Checks the deletion-score limit on the explicitly labeled finite prior grid.
    qgrid = np.array([[normal_law(z, par) for z in [-1, 1]] for par in pars])
    rtrue = .5*qgrid[0]
    convergence = []
    for n in [32, 128, 512, 2048]:
        counts = np.floor(n*rtrue).astype(int)
        residual = n-counts.sum()
        for index in np.argsort((n*rtrue-counts).ravel())[::-1][:residual]:
            counts.flat[index] += 1
        log_full = np.log(prior)+np.sum(counts[None,:,:]*np.log(qgrid), axis=(1,2))
        max_error = 0.
        for iz in range(2):
            for iy,y in enumerate(CELLS):
                if counts[iz,iy] == 0:
                    continue
                for t in range(2):
                    retained = np.array([marginal(qgrid[j,iz], y, t) for j in range(len(pars))])
                    log_deleted = log_full-np.log(qgrid[:,iz,iy])+np.log(retained)
                    post = np.exp(log_deleted-np.max(log_deleted))
                    post /= post.sum()
                    predicted = post @ (qgrid[:,iz,iy]/retained)
                    target = qgrid[0,iz,iy]/retained[0]
                    max_error = max(max_error, abs(np.log(predicted)-np.log(target)))
        convergence.append({'n':n, 'max_deleted_log_prediction_error':float(max_error)})
    assert convergence[-1]['max_deleted_log_prediction_error'] < 1e-5

    out = {'scope':'Author diagnostics only; no optimization, selection simulation or theorem acceptance.',
           'boundary_gaussian_convolution_max_error':float(max_boundary),
           'boundary_GH64_vs_GH128_max_error':float(max_refine),
           'absorption_max_cell_error':float(max_absorption),
           'deletion_evidence_vs_deleted_posterior_max_error':float(max_delete),
           'deletion_check_prior':'Three-point diagnostic prior, not the selected continuous Bayesian prior.',
           'finite_prior_deterministic_sequence':convergence,
           'boundary_laws':boundary_laws,'finite_context_attempt':finite_context,
           'retained_trial_prediction':float(retained_prediction), 'unconditional_trial_prediction':float(unconditional),
           'strict_separation':'Impossible on attempted two-trial design by analytic family equality; existence on richer designs unresolved.',
           'legacy_sha256':hashlib.sha256((ROOT/'PROOF_PACKAGE.md').read_bytes()).hexdigest()}
    assert out['legacy_sha256'] == '46e98f94d57f86a724f1a03ac5cdeba4c27324a06d331c403cbc4524cd33943c'
    dest=ROOT/'logs/theory_checks/2026-09-08_primary_separation.json'
    dest.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))

if __name__ == '__main__':
    run()
