# 05. Steelman and ideological Turing test

Files: `05_author_opposing_case.md` (the author agent's statement of the opposition), `05_advocate_case.md` (a fresh advocate subagent, primed only with the opposing side and web search). Turing-test result: see the end of this file.

Procedure note. The author agent's case was written after the advocate's note had arrived. It drew on a list of objections (O1, O2, O3, O5, O6 below) that was made before. This contaminates the test in the author's favour, and the methodology report says so.

## Objections and their fate

| # | Objection | Source | Status | Paper's response |
|---|---|---|---|---|
| O1 | The certifiability principle proves too much. It would condemn coherence, consistency and totality too | both | **survives in part** | The principle is restricted to *generative* (diachronic) norms, which require the agent to produce a new state from its current one. State norms have nothing to execute. The paper must defend this asymmetry and concede it as a premise |
| O2 | Rule-following does not need proof of correctness: a child follows addition | author | **survives; forces reformulation** | The child's procedure is a sound *general* updater, correct on its whole domain. Diachronic uniformity: posteriors become priors, so the agent's updating disposition must apply across the states it may come to be in. Reformulated Proposition 1 (no sound general updater commits on every updatable presentation) is exactly the failure the child lacks |
| O3 | "Certification" is trivial: build a certificate into the format, e.g. attach the disintegration | author | **survives; forces refinement** | Accepted: evidence-first formats (observation marginal plus a stored posterior kernel) are certifiable. They do not extend to a *new* evidence source modelled by its relation to the world, because Bayes' rule for the new source needs a likelihood. Lemma 3 shows the world-first channel format is closed under new conditionally independent sources. Thesis restricted to open-ended learning from modelled sources |
| O4 | Wrong kind of reason: noise belief adopted for convenience | both | **survives in part** | The constraint fixes a format, not a credence. It rules out exact deterministic channel models as followable, while credence within the dominated class is set by evidence. Real channels are noisy, and Bayesian models of perception already use noise likelihoods. Conceded: in a world with exact continuous evidence, a rule-following computable agent is at a disadvantage |
| O5 | Noise-scale dependence: no limit as noise goes to 0 in bad cases | author | **accepted** | Turned into a claim: the channel model is not an approximation of an exact model, and the scale parameter is substantive |
| O6 | Representation-dependence is old (Hacking, Garber) | author | **survives in part** | Difference: here the credence function itself is fully given and computable. What is opaque is not a logical consequence of the content but whether a norm can be executed on it |
| O7 | Relativity to ZFC: in ZFC + Con(ZFC) the prior is certifiable | advocate | **answered** | Proposition 1 is theory-free: no c.e. procedure, and so no sound c.e. theory, certifies all updatable presentations. ZFC is one instance (Corollary 1 holds for every T) |
| O8 | Same input-output behaviour, differ only in syntax: a reductio for functionalists | advocate | **survives in part** | The relevant behaviour is the updater's dispositional profile across states (O2), not its output on one prior. Conceded: rational standing *as rule-follower* is not functional at the level of the credence function |
| O9 | Ideal norms are evaluative standards, not instructions | advocate | **accepted as scope limit** | The paper claims nothing about the evaluative ideal. Its target is conditionalization as a rule followed |
| O10 | The noise-floor objection: mixing over scales needs a floor | advocate | **refuted** | Lemma 4: the mixture is bounded iff E[1/s] < ∞, which allows positive weight near 0 (π(s) = 2s) |
| O11 | Other certifiable routes exist: discrete evidence, bounded densities generally, exchangeability, typed languages | advocate | **accepted; claim narrowed** | Discrete and exchangeable (discrete-outcome) cases are outside scope. Bounded densities in general are the dominated class, which is the claim. Typed languages: unverified; the claim is stated as "every route known to the author" |
| O12 | Exact digital register | advocate | **outside scope** | Discrete evidence: ratio conditionalization, unaffected |
| O13 | Rescorla's Dutch book exposes the noise-modeller if evidence is exact | advocate | **survives in part** | Conceded for worlds with exact evidence and bets on exact values. For a computable agent the exact value arrives only as a convergent stream of approximations; the paper flags this as a cost, not a refutation |

## Positions the paper must defeat or accommodate

1. **Defeat:**
   - O7 (theory-relativity), by the theory-free form of Proposition 1;
   - O10 (noise floor), by Lemma 4.
2. **Accommodate as scope:**
   - O9 (evaluative ideal);
   - O11 (discrete and exchangeable cases);
   - O12 (digital evidence).
3. **Argue against, conceding a premise:**
   - O1 (proves too much), via the generative-versus-state norm asymmetry;
   - O2 (rule-following), via diachronic uniformity and the no-sound-general-updater form;
   - O4 (wrong kind of reason), via format versus credence;
   - O8 (functionalism), conceded in a qualified form;
   - O13 (Dutch book), conceded as a cost.
4. **Incorporate:**
   - O3: evidence-first formats are certifiable, but they are not open-ended;
   - O5: noise is substantive, not an approximation.

## Revised thesis (T2')

1. **No sound general updater.** No procedure that commits only to correct conditional distributions commits on every presentation of a computable prior that can be updated computably. This follows from Proposition 1.
2. **Representation-dependence.** Whether a computable agent can follow conditionalization as a general rule depends on how it represents its prior, not only on its credence function.
3. **Noise for open-ended learning.** A computable agent can follow conditionalization as an open-ended rule, for any world prior and any new source it models, if it models each continuous source as a dominated channel, one with a bounded likelihood density. The required noise can be arbitrarily small and needs no floor.

## Turing-test result

Fresh judge, saw only the two notes, unlabelled (X = author agent, Y = advocate), no web access.
- Impostor guess: **Y, 65 percent confidence. Wrong.** The author agent's note was not identified as the proponent's.
- Stronger case: **Y (advocate).** The judge found X's points sound but more general.
- Highest-damage objections, as rated by the judge:
  - b, "satisfying a norm is not the same as showing one satisfies it" (5/5): the same as O2 above;
  - a, proves too much (4);
  - i, other certifiable routes (4);
  - k, noise floor (4);
  - l, wrong kind of reason (4).
- Objections only in X that the judge rated as missing from Y: rule-following (d), the Hacking/Garber precedent (h), the triviality of built-in certificates (i), and noise-scale sensitivity (m).

Consequence. The test was passed on identification but not on strength. The prompt's remedy is to strengthen the author's version. Instead of rewriting X, the steelman used for the paper is the union of both notes (table above), with every objection rated 4 or 5 given a dedicated reply in the draft. Objection b/O2 rated 5 is the paper's central obstacle. It is answered by the "no sound general updater" form of Proposition 1 together with diachronic uniformity. Lemma 4 refutes k.
