# Plan: cognitive-model extension and Bayesian trial LOO

Updated 2026-09-10. Status: execution plan, not proof acceptance. General theorem remains primary. The approved synthetic gain-only probability-distortion pair supplies a nonvacuous application; it does not replace the general theorem. Existing author perturbation results cover finite exponential families. All new sufficient hypotheses below must be stated and checked, not silently entered as approved scientific assumptions.

## Target and success criteria

Prove, for a declared class of omitted-context cognitive DGMs and matched candidate families, that both candidates are observably false and

    0<R_K<R_S, Delta_C>0.

R_M is joint participant KL risk minimized over the candidate family; Delta_C is the average single-trial conditional KL advantage evaluated at those SAME joint-optimal observable laws. Separately prove

    (ELPD_K-ELPD_S)/(nT) -> Delta_C,
    (LOOIC_K-LOOIC_S)/(nT) -> -2 Delta_C

in probability under fixed T and independent participants. The held-out response belongs to an already observed participant. BIC and BF use the joint gap; their proofs remain separate. No forecast interpretation is asserted for arbitrary trial deletion.

Success requires: an audited general statement, a faithful cognitive witness satisfying its hypotheses, separate posterior/deletion convergence, tested exact-refit computation, an honest formal-verification coverage report, and review of scientific scope. A theorem that merely assumes the desired gaps closes only the criterion-transfer part.

## Starting evidence and known obstructions

- `context_score_perturbation_2026-09-09.md`: author joint-risk expansion after nuisance refitting and latent tilt construction.
- `trial_conditional_perturbation_2026-09-09.md`: author conditional expansion with A=average(Id-E[.|Y_-t,W]); exact positive and negative controls at global joint fits.
- `primary_separation_attempt_2026-09-08.md` L4–L8: conditional finite-design posterior, response-deletion, evidence and BIC arguments. Audit applicability rather than re-proving by analogy.
- Existing design absorption: some complete designs make S and K identical observable families. Further optimization cannot repair this. Preserve all shared intercept, side, sensitivity and random-effect terms.
- `formal/` contains status/notation scaffolding, not the new mathematical theorems. Some comments contain superseded assumption statuses; reconcile them with the live register before substantive formalization. A successful scaffold build is not a verified scientific result.

## Dependency-ordered work sessions

Sessions are bounded daily goals, not promises of calendar completion. Each ends with a named artifact, evidence and an exact next action. A failed gate changes the route; it does not authorize weaker scientific scope.

| Session | Work and exit artifact | Gate and fallback |
|---|---|---|
| 1 | Adversarial review of both perturbation proofs: `proof_reviews/review_perturbation_pair.md`. Reconstruct normalization, global optimum, remainders, latent tilt admissibility and conditional operator independently of author verdicts. | Repair any load-bearing defect before downstream use. Label same-LLM review honestly; seek a human statistician/mathematician for final scope review. |
| 2 | State a smooth observable-family extension: `smooth_observable_extension.md`. Define regular local coordinates at p0, tangent spaces, nesting and conditional KL residuals. | Derive the expansion with uniform remainder bounds and global localization. If singular, work in identifiable observable coordinates or restrict the conditional theorem explicitly; do not invert a singular parameter Hessian. |
| 3 | Specify a richer complete cognitive design and audit it: `cognitive_design_manifest.md`. Include both lotteries, side, ambiguity, Z support and allowed co-occurrences. | Verify the global positive-scale absorption condition fails; then separately assess observable rank/identifiability. Rank alone is not separation. Retain previously absorbed designs as negative controls. |
| 4 | Derive observable cognitive scores and latent-to-observable perturbations: `cognitive_score_certificate.md`. Differentiate the participant mixture with justified domination and include all shared nuisance scores. | Show a context tilt is admissible and aligns with the residual distortion score. Keep prescribed context moments and residual constraints explicit. If alignment vanishes, record why and switch to a constrained finite-support tilt or higher-order calculation. |
| 5 | Establish global joint projections, strict superiority and remaining falsity: `cognitive_joint_separation.md`. | Certify that a locally improving fit beats the GLOBAL simple infimum; exclude distant/boundary representations. Use analytic bounds or rigorously validated interval bounds. If impossible, retain a local result with its limitation and pursue a different authorized support, not omitted nuisance terms. |
| 6 | Evaluate conditional sign at those joint fits: `cognitive_conditional_separation.md`. Compute d, r_K and L=<d,Ad>+2<r_K,Ad>. | Prove L>0 or a direct positive conditional gap. If L<0, report the BIC/BF-only possibility and the LOO reversal; the simultaneous goal stays open. If L=0, higher order is required. |
| 7 | Audit and adapt posterior concentration and deletion stability: `bayesian_trial_LOO_theorem.md`. First use finite design/fixed T. | Verify positivity, prior support, optimal-law uniqueness or equivalent conditional predictions, and log control. Continuous W is a later extension with envelopes and uniform integrability; do not claim it from finite-cell counts. |
| 8 | Integrate separate BIC, BF and exact LOO corollaries: `criterion_corollaries_review.md`. | Keep fixed perturbation versus shrinking perturbation regimes explicit. Do not add a Laplace/Bernstein–von Mises detour if first-order evidence bounds suffice. |
| 9 | Implement exact deletion and bounded simulation pilot: `bayesian_LOO_validation.md` and reproducible scripts. | Match the scientific holdout target; compare exact refits with quadrature and PSIS. Failed diagnostics trigger refits or reported computational limits, not a criterion substitution. |
| 10 | Integrate proof, Lean coverage, code checks and scope: `extension_verdict.md`. | Each claim points to its proof, assumptions and verification status. Final scientific acceptance remains distinct from author completion. |

Lean proceeds alongside sessions 1–8 in small completed units. It must not consume repeated sessions without closing a mathematical or formal obligation.

## Mathematical route beyond exponential families

Let q_M(theta) denote the integrated observable law, rather than conditional logits before integrating latent effects. At a common baseline p0, seek C3 local observable charts with full-rank derivative and positive cells on the finite support. Establish that the global KL minimizers for p_e=p0(1+e h) enter these charts as e->0. Local regularity alone does not establish this; remote branches and boundary sequences must be excluded or represented in the chart.

Then prove the local quadratic risk expansion and nuisance adjustment for each tangent space. Curvature contributes to remainders; the leading residuals should be r_M=h-P_M h. Only after proving that bridge may we reuse the conditional operator calculation. Exact equality of the exponential-family and cognitive parameterizations is unnecessary, but equality of the relevant local observable geometry and global projection behavior must be justified.

For the approved cognitive pair preserve

    eta=alpha+beta_side s+tau[v_A{w(p_A;rho)-theta A/2}-v_R w(p_R;rho)],
    w(p;rho)=exp(-(-log p)^rho), S:rho=1, K:rho>0.

Integrate the same working participant-effect family in both models and retain Z. Do not apply the exponential-family theorem directly to this nonlinear integrated mixture. Changes to working effect families, domain restrictions or priors require explicit scope records.

## Bayesian LOO bridge: precise obligations

For global phi, let q_i(y_i;phi) be the participant joint marginal and q_i,-t its marginal after deleting only response t. Exact prediction is

    integral [q_i(y_i;phi)/q_i,-t(y_i,-t;phi)] pi(phi|D_-it) dphi.

The posterior uses q_i,-t times the other participants' joint likelihoods. This learns participant effects from retained responses. Three separate steps are required:

1. Concentrate on joint-optimal observable laws under the chosen fixed proper priors. Positive prior mass near an optimum and population likelihood separation need proofs. Parameter identifiability is stronger than necessary; distinct parameters may encode the same law.
2. Extend concentration uniformly over single-response deletions. In the finite setting, deleting one whole participant as an intermediate argument changes empirical frequencies deterministically by O(1/n); restoring retained responses is a bounded likelihood tilt whose normalizer needs a positive lower bound. The final holdout remains one response.
3. Control log predictions, then use a participant-cluster LLN for the normalized score. A fixed positive-cell floor is sufficient in the finite setting. Pointwise probability convergence alone does not control logs in general.

If several joint optima yield different conditionals, characterize the posterior mixture or withhold the single Delta_C limit. State variable trial counts, increasing T, adaptive designs and correlated participants as separate extensions. No CLT or fitted-score standard-error theorem is implied by a LLN.

## Where GPT-6 Astra needs external checks

No calibrated theorem-proving error rate for this model has been established in this project. The following are anticipated LLM failure modes, not measured claims about Astra's benchmark performance. Fluent explanations, repeated agreement and long reasoning are not acceptance evidence.

| Failure mode | Concrete danger here | Required check |
|---|---|---|
| Assumption substitution | Import convexity of an exponential family into a nonlinear mixture; drop nuisance terms or replace F(theta|X,Z) by F(theta|Z). | Assumption-by-assumption mapping and theorem statement diff; human scientific-scope review. |
| Local/global confusion | Treat a stationary point or numerical optimum as the global KL projection. | Global localization/coercivity or certified bounds; adversarial remote-parameter and boundary searches. |
| Invalid limit manipulations | Differentiate a latent integral without domination; pass to logs near zero; turn fixed-deletion convergence into uniform LOO. | Explicit bounds with quantifiers, Lean for tractable identities, separate analytic review of convergence. |
| Wrong prediction target | Refitting conditional risk, deleting whole persons, or using full-data participant effects in an uncorrected held-out score. | Exact deletion identities and tiny-data refit tests with deliberately influential responses. |
| Overclaimed positivity | Infer trial advantage from joint advantage or observable falsity from nonidentical parameters. | Mandatory reversal and absorbed-design controls; closure argument for positive residual risk. |
| Circular verification | Tests reproduce the same erroneous formula; the author “reviews” its own proof favorably. | Independent direct sums versus derived formulas, distinct review pass, and human review of central hypotheses. |
| Formalization of the wrong theorem | Lean proves a weaker implication or assumes the desired gap as a hypothesis. | Side-by-side natural-language/Lean statement and dependency audit. |
| Fabricated literature or tool success | Misstate a cited theorem or claim an unrun build passed. | Inspect primary sources and capture actual commands, exit status, versions and artifact hashes. |

## Lean verification plan

Use the existing Lean project, with a reviewed, pinned mathlib addition if needed. Pin both Lean and dependencies; build from a clean environment. Formalize in this order:

1. Finite conditional probabilities, normalization and the KL joint/marginal chain identity under explicit positivity.
2. Finite weighted inner-product projections, the A operator and the quadratic difference identity; positive-energy and invariance sufficient conditions.
3. The exact four-cell positive/negative examples, including their fitted-law optimality, not just rational arithmetic on chosen laws.
4. Finite Bayes evidence/deletion identities with proper measures; then posterior concentration lemmas if the existing measure/probability library makes the task bounded.
5. Smooth risk expansions and asymptotic LOO only after the preceding definitions and analytic assumptions are settled. These may remain independently reviewed informal proofs initially; label their coverage accurately.

For every accepted formal theorem, store the rendered statement, dependency/axiom report, source hash and successful build log. Reject `sorry`, `admit`, `sorryAx`, or custom axioms encoding unresolved claims. Inspect `#print axioms` transitively; standard Lean logical axioms are not the same as a hidden theorem assumption. Audit hypotheses for inconsistency or for containing the intended conclusion. Avoid extending the trusted base through unchecked/native mechanisms without an explicit review.

Lean checks derivations from formal definitions and assumptions. It does not establish that a cognitive kernel matches the task, that chosen priors are scientifically appropriate, that a translated statement matches the paper, or that a separate numerical implementation uses those definitions. Those require semantic and implementation review. See the official [proof-validation guide](https://lean-lang.org/doc/reference/latest/ValidatingProofs/) and [axiom reference](https://lean-lang.org/doc/reference/latest/Axioms/).

## Simulation and computation plan

Predeclare designs, perturbations, seeds, sample sizes, metrics and tolerances BEFORE examining preference rates. Stage numerical discovery separately from confirmatory validation; any search-selected witness must receive an analytic or validated-numerical certificate, not be advertised as representative behavior.

- Preserve the exact positive, conditional-reversal, no-context, representable shared-effect and absorbed-design controls. Validate both signs, not just favorable cases.
- First enumerate the finite observable examples and check normalization, moment matching, joint KL and DIRECT conditional KL. Compare with the independent marginal-chain calculation. The current six checks are a start, not a complete model-recovery study.
- For low-dimensional cognitive models, compare independent quadrature implementations and successively tighter integration tolerances. Multi-start fitting diagnoses local optima but does not certify globality. Ordinary floating-point agreement is not a positivity proof when the gap is near numerical error.
- Pilot proposal: 20 replications per predeclared cell at n=50,200,1000, fixed T and fixed seeds; first benchmark one dataset to cap runtime. This pilot detects implementation problems, not precise win rates. Report all cells, MC uncertainty, fitting failures and numerical error. Expand only after diagnostics warrant it; do not launch the existing large replication grid.
- Validate Bayesian fitting on correctly specified controls with prior predictive checks and, where feasible, simulation-based calibration. Calibration of a correctly specified computation does not prove the misspecified scientific claim. Compare low-dimensional posterior predictions against quadrature.
- On a small dataset, refit every single-trial deletion exactly under each candidate. Compare predictions with the evidence-ratio identity and then with PSIS-LOO. If using a latent-draw conditional likelihood for PSIS, check its importance-weight identity; if integrating effects first, use the correct joint-to-retained-marginal ratio, not a product of unconditional trial marginals.
- Record PSIS Pareto diagnostics, posterior effective sample sizes, Monte Carlo score error and exact-refit discrepancies. Use documented package diagnostics rather than an invented universal threshold. Difficult deletions receive exact refits or an explicit unavailable result. LOOIC=-2 ELPD; do not substitute WAIC.
- Summarize paired trial scores within participants. Report Monte Carlo variation across independent simulated datasets separately from uncertainty estimated within one dataset. Shared training data complicate fitted-score standard errors; do not claim a proved cluster SE without a separate argument.

The distinction between observation and group holdouts is documented in the [loo FAQ](https://mc-stan.org/loo/articles/online-only/faq.html); approximation outputs and diagnostics are documented in the [loo reference](https://mc-stan.org/loo/reference/loo.html). Simulation can falsify a claimed implication or expose coding errors. Agreement across finitely many runs cannot establish a universal theorem, uniform convergence, global optimality or scientifically correct assumptions.

## Operating rules and definition of done

Two distinct proof attacks per obligation per run; two no-progress runs require a recorded fallback. Cap a Lean setup/library detour at one session, then continue useful mathematical work. A missing lemma becomes an explicit obligation, never an axiom disguised as a proof. Preserve unfavorable results and failed routes. Do not change priors, seeds, shared baseline or holdout unit to create a desired outcome.

Maintain an evidence ledger with independent columns: author proof, separate mathematical review, formalized statement/coverage, numerical validation, cognitive-assumption verification, and PI acceptance. No column substitutes for another. Update the existing roadmap and state after each bounded result. Final packet must say exactly which general theorem is proved, which cognitive examples instantiate it, which criteria favor K, what remains conditional, and what Lean actually checked.
