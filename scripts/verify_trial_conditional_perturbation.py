#!/usr/bin/env python3
"""Finite-law diagnostics; not a cognitive-model witness or proof substitute."""
import json, math
from pathlib import Path
states=[(-1,-1),(-1,1),(1,-1),(1,1)]
def kl(p,q): return sum(a*math.log(a/b) for a,b in zip(p,q))
def conditional(p,q):
    total=0.0
    for t in range(2):
        for j,z in enumerate(states):
            ids=[i for i,v in enumerate(states) if v[1-t]==z[1-t]]
            pm=sum(p[i] for i in ids); qm=sum(q[i] for i in ids)
            total+=p[j]*math.log((p[j]/pm)/(q[j]/qm))
    return total/2
out={'scope':'Exact joint-fitted observable exponential-family diagnostics only','examples':[]}
for name in ['negative','positive']:
    rows=[]
    for e in [.05,.025,.0125]:
        h=[3*x-x*y if name=='negative' else y+x*y/2 for x,y in states]
        p=[(1+e*z)/4 for z in h]; s=[.25]*4
        k=[((1+2*e*x)/4 if y==1 else .25) if name=='negative' else (1+e*y)/4 for x,y in states]
        assert min(p+k)>0 and abs(sum(p)-1)<1e-14 and abs(sum(k)-1)<1e-14
        # Verify sufficient-statistic matching for the stated GLOBAL joint fits.
        stats=[[y for x,y in states], [x+x*y for x,y in states]] if name=='negative' else [[x for x,y in states],[y for x,y in states]]
        for stat in stats: assert abs(sum((a-b)*v for a,b,v in zip(p,k,stat)))<1e-14
        cj=kl(p,s)-kl(p,k); cc=conditional(p,s)-conditional(p,k)
        # Independent marginal chain-rule calculation.
        mg=0
        for t in range(2):
            idx=[[i for i,z in enumerate(states) if z[t]==v] for v in [-1,1]]
            marg=lambda q:[sum(q[i] for i in ids) for ids in idx]
            mg+=kl(marg(p),marg(s))-kl(marg(p),marg(k))
        assert abs(cc-(cj-mg/2))<1e-13
        assert kl(p,k)>0 and cj>0 and (cc<0 if name=='negative' else cc>0)
        rows.append({'epsilon':e,'joint_gap_over_e2':cj/e**2,'K_risk_over_e2':kl(p,k)/e**2,'conditional_gap_over_e2':cc/e**2})
    expected=[1,4,-.25] if name=='negative' else [.5,.125,.25]
    last=rows[-1]
    for key,val in zip(['joint_gap_over_e2','K_risk_over_e2','conditional_gap_over_e2'],expected): assert abs(last[key]-val)<.005
    out['examples'].append({'name':name,'expected_coefficients':expected,'rows':rows})
if __name__=='__main__':
    p=Path('logs/theory_checks/2026-09-09_trial_conditional_perturbation.json')
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
