#!/usr/bin/env python3
"""Check minimal ambiguity mapping and exact analytical projection; no simulation."""
import math,json
from fractions import Fraction as F
from pathlib import Path
sig=lambda x:1/(1+math.exp(-x))
states=[(0,0),(1,0),(0,1),(1,1)]
p=[]
for y in states:
 cell=F(0)
 for rates in [(F(1,2),F(1,2)),(F(1,4),F(1,10))]:
  cell+=math.prod([rates[t] if y[t] else 1-rates[t] for t in range(2)])/2
 p.append(cell)
assert p==[F(37,80),F(19,80),F(13,80),F(11,80)]
m=[F(3,8),F(3,10)];assert p[3]-m[0]*m[1]==F(1,40)
theta=math.log(7/5);delta=math.log(21/25)
rho=lambda d:math.log(-math.log(.5+d/4))/math.log(math.log(2))
rL,rU=rho(-.5),rho(.5);r=rho(delta)
assert 0<rL<r<1<rU and 0<theta<2
for x,target in zip([1,2],m):
 w=math.exp(-math.log(2)**r)
 assert abs(sig(4*(w-.5)-theta*x)-float(target))<1e-14
lo,hi=0.,2.
for _ in range(100):
 mid=(lo+hi)/2
 score=sum(x*(sig(-mid*x)-float(t)) for x,t in zip([1,2],m))
 if score>0:lo=mid
 else:hi=mid
ts=(lo+hi)/2
q=lambda t,d:[math.prod(sig(d-t*x) if yj else 1-sig(d-t*x) for x,yj in zip([1,2],y)) for y in states]
kl=lambda q:sum(float(a)*math.log(float(a)/b) for a,b in zip(p,q))
rs,rk=kl(q(ts,0)),kl(q(theta,delta));assert 0<rk<rs
def conditional_risk(qv):
 total=0.
 for t in range(2):
  for j,y in enumerate(states):
   ids=[h for h,z in enumerate(states) if z[1-t]==y[1-t]]
   pm=sum(float(p[h]) for h in ids);qm=sum(qv[h] for h in ids)
   total+=float(p[j])*math.log((float(p[j])/pm)/(qv[j]/qm))
 return total/2
conditional_gap=conditional_risk(q(ts,0))-conditional_risk(q(theta,delta))
assert abs(conditional_gap-(rs-rk)/2)<1e-14
out={'scope':'Analytical construction checks, not model-selection simulation','P':[str(v) for v in p],'theta_S':ts,'theta_K':theta,'delta_K':delta,'rho_K':r,'rho_bounds':[rL,rU],'R_S':rs,'R_K':rk,'joint_gap':rs-rk,'trial_conditional_gap':(rs-rk)/2}
Path('logs/theory_checks/2026-09-12_minimal_ambiguity.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
