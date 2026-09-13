#!/usr/bin/env python3
import math, json, random, time
from pathlib import Path
L2=math.log(2); inv=lambda d:math.log(-math.log(.5+d/4))/math.log(L2)
RL,RU=inv(-.5),inv(.5)
def gl(n):
 out=[]
 for i in range(1,n+1):
  x=math.cos(math.pi*(i-.25)/(n+.5))
  for _ in range(30):
   p0,p1=1.,x
   for k in range(2,n+1):p0,p1=p1,((2*k-1)*x*p1-(k-1)*p0)/k
   der=n*(x*p1-p0)/(x*x-1);dx=p1/der;x-=dx
   if abs(dx)<2e-15:break
  out.append((x,2/((1-x*x)*der*der)))
 return out
def grid(model,n,coord='rho'):
 nodes=gl(n);out=[]
 for z,w in nodes:
  th=z+1
  other=[(0,1)] if model=='S' else nodes
  for zz,ww in other:
   if model=='S':delta=0;weight=w/2
   elif coord=='rho':
    rho=(RL+RU)/2+(RU-RL)*zz/2;delta=4*(math.exp(-L2**rho)-.5);weight=w*ww/4
   else:
    delta=zz/2;m=.5+delta/4;jac=1/(4*m*math.log(m)*math.log(L2));weight=w*ww*jac/(4*(RU-RL))
   ls=[]
   for x in [1,2]:
    eta=delta-th*x;ls.extend([-math.log1p(math.exp(eta)),-math.log1p(math.exp(-eta))])
   out.append((math.log(weight),ls))
 return out
def lse(v):
 m=max(v);return m+math.log(sum(math.exp(x-m) for x in v))
def evidence(g,c):return lse([w+sum(a*b for a,b in zip(c,lp)) for w,lp in g])
def counts(data):return [sum(y[t]==v for y in data) for t in [0,1] for v in [0,1]]
def scores(g,c):
 full=evidence(g,c);total=0
 for j,k in enumerate(c):
  if k:
   deleted=c.copy();deleted[j]-=1;total+=k*(full-evidence(g,deleted))
 return full,total
def fit(c,delta):
 lo,hi=0.,2.
 for _ in range(65):
  th=(lo+hi)/2;score=0
  for t,x in enumerate([1,2]):
   p=1/(1+math.exp(th*x-delta));score+=x*((c[2*t]+c[2*t+1])*p-c[2*t+1])
  if score>0:lo=th
  else:hi=th
 th=(lo+hi)/2
 val=sum(c[2*t]*(-math.log1p(math.exp(delta-th*x)))+c[2*t+1]*(-math.log1p(math.exp(th*x-delta))) for t,x in enumerate([1,2]))
 return val
def mle(c,model):
 if model=='S':return fit(c,0)
 lo,hi=-.5,.5
 for _ in range(65):
  a=lo+(hi-lo)/3;b=hi-(hi-lo)/3
  if fit(c,a)<fit(c,b):lo=a
  else:hi=b
 return max(fit(c,(lo+hi)/2),fit(c,-.5),fit(c,.5))
if __name__=='__main__':
 start=time.time();protocol=json.loads(Path('docs/minimal_pilot_protocol.json').read_text());cache={}
 def get(m,n,coord='rho'):
  key=(m,n,coord)
  if key not in cache:cache[key]=grid(m,n,coord)
  return cache[key]
 tiny=protocol['tiny_data'];c=counts(tiny);checks=[]
 for model in ['S','K']:
  g=get(model,96);z,elpd=scores(g,c)
  assert abs(evidence(g,[0]*4))<1e-10
  maxerr=0
  # Explicit retained response loop, independently reconstructing likelihood.
  for i,y in enumerate(tiny):
   for t in [0,1]:
    vals=[];nums=[]
    for w,lp in g:
     ld=w+sum(lp[2*s+v] for k,row in enumerate(tiny) for s,v in enumerate(row) if (k,s)!=(i,t))
     vals.append(ld);nums.append(ld+lp[2*t+y[t]])
    direct=lse(nums)-lse(vals);d=c.copy();d[2*t+y[t]]-=1
    maxerr=max(maxerr,abs(direct-(z-evidence(g,d))))
  alt=scores(get(model,96,'delta'),c);err=max(abs(z-alt[0]),abs(elpd-alt[1]))
  assert maxerr<1e-10 and err<1e-8
  checks.append({'model':model,'log_evidence':z,'elpd':elpd,'direct_deletion_max_error':maxerr,'alternative_coordinate_error':err})
 rows=[]
 for ri,regime in enumerate(protocol['regimes']):
  for n in protocol['participants']:
   for rep in range(protocol['replicates_per_cell']):
    seed=20260913+100000*ri+1000*n+rep;rng=random.Random(seed);data=[]
    for _ in range(n):
     context=int(rng.random()<.5) if regime=='context' else 0
     data.append([int(rng.random()<(1/(1+3**(context*x)))) for x in [1,2]])
    c=counts(data);result={};errors=[];used=96
    for m in ['S','K']:
     low=scores(get(m,48),c);high=scores(get(m,96),c);error=max(abs(a-b) for a,b in zip(low,high))
     if error>1e-5:
      higher=scores(get(m,192),c);error=max(abs(a-b) for a,b in zip(high,higher));high=higher;used=192
     assert error<1e-5,(regime,n,rep,m,error)
     result[m]=high;errors.append(error)
    row={'regime':regime,'n':n,'rep':rep,'seed':seed,'counts':c,'log_BF_KS':result['K'][0]-result['S'][0],'LOOIC_K_minus_S':-2*(result['K'][1]-result['S'][1]),'BIC_K_minus_S':-2*(mle(c,'K')-mle(c,'S'))+math.log(n),'quadrature_max_error':max(errors),'max_order':used}
    rows.append(row)
 summary=[]
 for regime in protocol['regimes']:
  for n in protocol['participants']:
   rr=[r for r in rows if r['regime']==regime and r['n']==n];wins={}
   for metric in ['BIC_K_minus_S','log_BF_KS','LOOIC_K_minus_S']:
    count=sum(r[metric]>0 if metric=='log_BF_KS' else r[metric]<0 for r in rr);p=count/len(rr)
    wins[metric]={'K_wins':count,'replicates':len(rr),'binomial_mcse':math.sqrt(p*(1-p)/len(rr))}
   summary.append({'regime':regime,'n':n,'preferences':wins})
 out={'protocol':protocol,'tiny_checks':checks,'pilot_summary':summary,'datasets':rows,'runtime_seconds':time.time()-start,'limitations':'Deterministic quadrature with convergence checks, not symbolic integration or formal error certificate. Ten replicates per cell give imprecise rates; zero empirical MCSE at endpoints does not establish certainty.'}
 p=Path('logs/theory_checks/2026-09-13_minimal_bayes.json');p.parent.mkdir(exist_ok=True,parents=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'tiny_checks':checks,'summary':summary,'seconds':out['runtime_seconds']},indent=2))
