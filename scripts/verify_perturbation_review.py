#!/usr/bin/env python3
"""Separate rational/operator and closed-risk checks for the review."""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext
from pathlib import Path
import json, hashlib
states=[(-1,-1),(-1,1),(1,-1),(1,1)]
def inner(a,b):return sum(x*y for x,y in zip(a,b))/4
def E(v,t):return [sum(v[j] for j,z in enumerate(states) if z[1-t]==y[1-t])/2 for y in states]
def A(v):return [v[i]-(E(v,0)[i]+E(v,1)[i])/2 for i in range(4)]
records=[]
for kind in ['negative','positive']:
    u=[F(y if kind=='negative' else x) for x,y in states]
    d=[F(x+x*y if kind=='negative' else y) for x,y in states]
    r=[F(2*(x-x*y)) if kind=='negative' else F(x*y,2) for x,y in states]
    assert inner(u,d)==inner(u,r)==inner(d,r)==0
    for t in range(2):
        assert E(E(r,t),t)==E(r,t)
        assert inner(r,E(d,t))==inner(E(r,t),d)
    joint=inner(d,d)/2; risk=inner(r,r)/2
    cond=(inner(d,A(d))+2*inner(r,A(d)))/2
    expected=(F(1),F(4),F(-1,4)) if kind=='negative' else (F(1,2),F(1,8),F(1,4))
    assert (joint,risk,cond)==expected
    records.append({'case':kind,'exact_joint_coefficient':str(joint),'exact_K_risk_coefficient':str(risk),'exact_conditional_coefficient':str(cond)})
# Independent closed expressions derived by decomposing joint fits into strata.
with localcontext() as ctx:
    ctx.prec=65
    def bern(z):return ((1+z)*(1+z).ln()+(1-z)*(1-z).ln())/2
    checks=[]
    for e in [D('0.05'),D('0.025'),D('-0.025')]:
        joint=bern(2*e)/2; rk=bern(4*e)/2
        marginal_adv=((1-e*e).ln()/2+3*e*((1+e)/(1-e)).ln()/2)
        cond=joint-marginal_adv/2
        assert rk>0 and joint>0 and cond<0
        checks.append({'epsilon':str(e),'joint_gap':str(joint),'K_risk':str(rk),'conditional_gap':str(cond)})
files=['docs/context_score_perturbation_2026-09-09.md','docs/trial_conditional_perturbation_2026-09-09.md']
out={'review_type':'same LLM separate review pass; not formal or external verification','rational_checks':records,'closed_expression_checks':checks,'source_sha256':{f:hashlib.sha256(Path(f).read_bytes()).hexdigest() for f in files}}
Path('logs/theory_checks/2026-09-10_perturbation_review.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact rational projections, operator identities and 65-digit closed-risk expressions.')
