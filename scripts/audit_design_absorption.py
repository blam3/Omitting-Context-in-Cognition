#!/usr/bin/env python3
"""Audit all declared (W,t) rows; numeric rho probes are not all-rho proofs.
CSV support_probability is the W probability repeated per trial, not a row weight.
"""
import argparse
import csv
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]

def rank(a):
    a=[list(map(F,row)) for row in a]; i=0
    for j in range(len(a[0])):
        pivot=next((k for k in range(i,len(a)) if a[k][j]),None)
        if pivot is None: continue
        a[i],a[pivot]=a[pivot],a[i]
        scale=a[i][j]; a[i]=[v/scale for v in a[i]]
        for k in range(len(a)):
            if k!=i:
                scale=a[k][j]; a[k]=[v-scale*u for v,u in zip(a[k],a[i])]
        i+=1
        if i==len(a): break
    return i

def quotient_test(D,d1,dr,tol=1e-10):
    # Remove nuisance column space without assuming those columns are independent.
    u=d1-D@np.linalg.lstsq(D,d1,rcond=None)[0]
    v=dr-D@np.linalg.lstsq(D,dr,rcond=None)[0]
    scale=max(1.,float(np.linalg.norm(d1)),float(np.linalg.norm(dr)))
    eps=tol*scale
    if np.linalg.norm(u)<=eps:
        return {'diagnostic':'compatible_at_tolerance' if np.linalg.norm(v)<=eps else 'nonzero_quotient_at_tolerance',
                'c':'any_positive' if np.linalg.norm(v)<=eps else None,
                'residual':float(np.linalg.norm(v))}
    c=float(u@v/(u@u)); residual=float(np.linalg.norm(v-c*u))
    result='compatible_at_tolerance' if residual<=eps and c>tol else ('nonpositive_or_near_zero_c' if residual<=eps else 'noncollinear_quotients')
    return {'diagnostic':result,'c':c,'residual':residual}

def weight(p,rho):
    if p==0: return 0.
    if p==1: return 1.
    return float(np.exp(-(-np.log(p))**rho))

def audit(path):
    rows=list(csv.DictReader(path.open()))
    required=['support_id','support_probability','z','trial','v_A','v_R','p_A','p_R','A','s']
    if not rows or any(k not in rows[0] for k in required): raise ValueError('Incomplete support schema')
    groups={}; exact=[]; d1=[]
    for row in rows:
        for k in required[1:]: row[k]=F(row[k])
        if row['trial'].denominator!=1 or row['trial']<1: raise ValueError('Invalid trial index')
        if row['support_probability']<=0: raise ValueError('Nonpositive support mass')
        if not all(0<=row[k]<=1 for k in ['p_A','p_R']): raise ValueError('Probability outside [0,1]')
        if any(row[k]<0 for k in ['v_A','v_R','A']): raise ValueError('Negative gain/ambiguity input')
        groups.setdefault(row['support_id'],[]).append(row)
        b=row['v_A']*row['A']/2
        exact.append([F(1),row['s'],b,b*row['z']])
        d1.append(row['v_A']*row['p_A']-row['v_R']*row['p_R'])
    masses=[]; ts=[]
    for group in groups.values():
        if len({r['support_probability'] for r in group})!=1 or len({r['z'] for r in group})!=1: raise ValueError('Inconsistent W group')
        trials=sorted(int(r['trial']) for r in group)
        if trials!=list(range(1,len(group)+1)): raise ValueError('Missing/duplicate trials')
        masses.append(group[0]['support_probability']); ts.append(len(group))
    if sum(masses)!=1 or len(set(ts))!=1: raise ValueError('Support masses or fixed T invalid')
    D=np.array(exact,dtype=float); base=np.array(d1,dtype=float)
    probes=[]
    for rho in [.25,.5,1.,1.5,3.]:
        dr=np.array([float(r['v_A'])*weight(float(r['p_A']),rho)-float(r['v_R'])*weight(float(r['p_R']),rho) for r in rows])
        probes.append({'rho':rho,**quotient_test(D,base,dr)})
    return {'source':str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
            'declared_support_points':len(groups),'T':ts[0],'stacked_rows':len(rows),
            'nuisance_columns':['1','s','b=v_A*A/2','b*Z'],
            'exact_rational_rank_D':rank(exact),
            'exact_rational_rank_D_and_d1':rank([a+[b] for a,b in zip(exact,d1)]),
            'numeric_rho_probes':probes,
            'scope':'Entire declared CSV support only. Completeness relative to an actual task requires protocol verification. Numerical probes are not an all-rho or observable-separation certificate.'}

def checks():
    # Algebra fixtures exercise sensitivity orientation; these are not new task designs.
    D=np.ones((3,1)); d=np.array([-1.,0.,1.])
    assert quotient_test(D,d,-d)['diagnostic']=='nonpositive_or_near_zero_c'
    assert quotient_test(D,d,np.ones(3))['diagnostic']=='nonpositive_or_near_zero_c'
    assert quotient_test(D,d,2*d+3)['diagnostic']=='compatible_at_tolerance'
    assert quotient_test(D,d,np.array([0.,1.,0.]))['diagnostic']=='noncollinear_quotients'
    assert quotient_test(D,np.ones(3),2*np.ones(3))['diagnostic']=='compatible_at_tolerance'

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--support',type=Path,default=ROOT/'registries/primary_design_support.csv')
    parser.add_argument('--output',type=Path,default=ROOT/'logs/theory_checks/2026-09-08_design_absorption.json')
    args=parser.parse_args(); checks(); result=audit(args.support.resolve())
    result['algebra_regressions']='pass; positive, zero, negative c; noncollinearity; zero quotient'
    args.output.write_text(json.dumps(result,indent=2)+'\n'); print(json.dumps(result,indent=2))
