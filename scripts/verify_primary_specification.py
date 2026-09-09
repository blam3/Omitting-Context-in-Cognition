import json, math, hashlib
from pathlib import Path
P=[.4,.1,.1,.4]; S=[.7,.1,.1,.1]; K=[.25]*4
kl=lambda p,q:sum(a*math.log(a/b) for a,b in zip(p,q))
marg=lambda q,t:[sum(q[j] for j in range(4) if ((j>>(1-t))&1)==b) for b in range(2)]
def conditional(p,q,t):
 pm,qm=marg(p,1-t),marg(q,1-t)
 return sum(p[j]*math.log((p[j]/pm[(j>>t)&1])/(q[j]/qm[(j>>t)&1])) for j in range(4))
joint=kl(P,S)-kl(P,K)
cond=sum(conditional(P,S,t)-conditional(P,K,t) for t in range(2))/2
assert abs(joint-math.log(3125/1568)/5)<1e-12
assert abs(cond-math.log(32/49)/5)<1e-12
for t in range(2):
 assert abs(conditional(P,S,t)-(kl(P,S)-kl(marg(P,1-t),marg(S,1-t))))<1e-12
# Exact discrete latent integration: full/deleted evidence equals deletion-posterior prediction.
weights=[.3,.7]; probs=[[.2,.8],[.6,.4]]; y=[1,0]
full=sum(w*p[0]*(1-p[1]) for w,p in zip(weights,probs))
deleted=sum(w*(1-p[1]) for w,p in zip(weights,probs))
pred=sum(w*(1-p[1])/deleted*p[0] for w,p in zip(weights,probs))
assert abs(full/deleted-pred)<1e-12
state=json.loads(Path('registries/proof_progress.json').read_text())
assert state['active_item']=='G2_observable_separation'
assert state['completed_obligations']==[]
ids={i['id'] for i in state['items']}
for item in state['items']:
 assert set(item['depends_on'])<=ids
 for path in item['evidence']:
  if not path.endswith('2026-09-08_G1_completion.json'): assert Path(path).is_file(),path
spec=Path('docs/primary_theorem_specification.md').read_text()
for i in range(1,11): assert f'PG-L{i}:' in spec
assert 'A-006 remains rejected' in spec
out={'scope':'G1 author checks only; no cognitive separation proof or independent review','joint_counterexample_gap':joint,'conditional_counterexample_gap':cond,'trial_deletion_evidence_identity':'pass on two-atom latent example','state_dependency_and_evidence_checks':'pass','lemma_inventory':'PG-L1 through PG-L10 present','legacy_sha256':hashlib.sha256(Path('PROOF_PACKAGE.md').read_bytes()).hexdigest()}
Path('logs/theory_checks/2026-09-08_G1_completion.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
