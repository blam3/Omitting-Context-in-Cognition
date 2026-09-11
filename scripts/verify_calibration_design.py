#!/usr/bin/env python3
"""Numerical transcription checks of an analytic nonabsorption certificate."""
import math,json,csv
from pathlib import Path
rows=[(0,0,-1),(.5,0,-1),(1,0,-1),(0,0,1),(.5,0,1),(1,0,1),(.25,.25,-1),(.75,.5,1)]
p=Path('docs/designs');p.mkdir(exist_ok=True)
with (p/'calibrated_eight_trial_support.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['Z','W_probability','trial','v_A','v_R','p_A','p_R','ambiguity_width','side'])
 for z in [-1,1]:
  for t,(prob,amb,side) in enumerate(rows,1):w.writerow([z,.5,t,1,1,prob,.5,amb,side])
# W_probability is repeated metadata, not a row probability to sum over trials.
def weight(p,r):return p if p in (0,1) else math.exp(-(-math.log(p))**r)
checks=[]
for r in [.5,1,2]:
 alpha,beta,tau=.2,-.3,1.7
 for side in [-1,1]:
  ell=[alpha+beta*side+tau*(weight(p,r)-weight(.5,r)) for p in [0,.5,1]]
  contrast=ell[1]-(ell[0]+ell[2])/2
  got_tau=ell[2]-ell[0];m=(ell[1]-ell[0])/got_tau
  got_r=math.log(-math.log(m))/math.log(math.log(2))
  assert abs(got_tau-tau)<1e-12 and abs(got_r-r)<1e-12
  assert abs(contrast-tau*(weight(.5,r)-.5))<1e-12
  assert abs(contrast)<1e-12 if r==1 else abs(contrast)>1e-3
  checks.append({'rho':r,'side':side,'contrast':contrast,'recovered_rho':got_r})
out={'scope':'Analytic identity transcription checks only; no KL witness','W_support_size':2,'trials_per_participant':8,'checks':checks}
Path('logs/theory_checks/2026-09-11_calibration_design.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: complete 2-by-8 support, contrast identity and inverse at six parameter/side settings.')
