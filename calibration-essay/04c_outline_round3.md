# 04c. Outline, round 3 (final; revised in response to 04b critique)

Title: "Calibrated Everywhere, Reliable Nowhere: A Theorem Against Track-Record Reliabilism about Credence"

Word budget: 5,800 including appendix (bibliography excluded).

## 1. Introduction (350)
- Reliabilism for credence: the measure problem. Calibration as the leading answer (SEP's formulation: a credence is justified iff produced by a well-calibrated process; Dunn 2015).
- Thesis (T): no standard of calibration, conditioned on any admissible family of reference classes and assessed over any range of worlds, is sufficient for reliability, and so none suffices for justification on reliabilist terms. Generalization (G): the same holds for every outcome-based standard that is finite-horizon, or future-independent, or Borel, and that a chance-matching process meets.
- Mechanism in one sentence: such standards can be met in every world by a process that uses no information about the world, and every such process has a world in which it is unreliable.
- Road map.

## 2. Calibrationism (850)
2.1 Definitions: credence-forming process; calibration (sharp, bins); conditional calibration on a family R; smooth calibration.
2.2 The schema CR(X, W). Sufficiency half (CR-S) is the target. Necessity left aside (Dorst-type points about rational miscalibration are a separate matter; one line).
2.3 Goldman's case and the reply: accidental calibration is fragile across nearby worlds (SEP report). Dunn: assess the process in nearby worlds as well as actual cases (verified quote). Tang: calibrated yet evidence-insensitive processes (SEP report). The strengthened view appears to answer both: conditionalize on evidence cells (answers Tang), require robustness across worlds (answers Goldman).
2.4 Desiderata: (D1) no penalty for mid credences; (D2) reliability as track record, actual and counterfactual.

## 3. Calibration without information (800)
3.1 History-based processes; uninformed processes (rule fixed in advance, inputs: history of outcomes, labels, own forecasts, private randomness).
3.2 Foster-Vohra: exact statement and assumptions (randomization; current coin hidden; finite grid; asymptotic; finite-sample rate order T^{-1/3}).
3.3 Strengthenings achieved by uninformed processes: deterministic smooth calibration (Foster-Hart), countable checking rules (SSV), bounded-complexity families (FRST), multicalibration.
3.4 Anti-tracking lemma (stated; proof in appendix). Note: the anti-tracking world is an ordinary exogenous chance world. Deterministic variant for those who reject chance.
3.5 The contrast that matters: a deterministic learner is miscalibrated in its own anti-tracking world (calibration error at least 0.4), so calibration correctly condemns it there; the uninformed calibrated process is calibrated there too.

## 4. The argument (1100)
Premises:
- (R) Reliability condition. If, in world w, a process's credence on every occasion is at least 0.4 from the chance of its content (given everything the process takes as input), in expectation, then the process is not reliable in w.
- (P1) For every history-based process rho there is a world w_rho in which the antecedent of R holds for rho. [Lemma]
- (P2) So for every history-based process there is a world in which it is not reliable. [R, P1]
- (Def) S is world-independently securable iff for some history-based process rho, in every world, rho's record meets S with probability at least 1 - epsilon, for some epsilon < 1 (probability over the process's randomization and the world's chances).
- (P3) If S is sufficient for reliability, then any process whose record meets S in w is reliable in w.
- (P4) Suppose S is world-independently securable, witnessed by rho, and sufficient for reliability. In w_rho, rho's record meets S with probability at least 1 - epsilon > 0, so by P3 rho is reliable in w_rho. By P2 it is not. Contradiction.
- (C1) No world-independently securable standard is sufficient for reliability.
- (P5) For every X of section 2 and every range W, the standard "X-calibrated throughout W(w, rho)" is world-independently securable. [Theorems of 3.2-3.3; W drops out because the witness is X-calibrated in every world]
- (C2) For every X and W, CR-S(X, W) is false. [C1, P5, and reliabilism's identification of justifying processes with reliable ones]
Defense of R (main philosophical work): 
- Proper-score dominance: in w_rho the chance-matcher's credences are, on every occasion, strictly better in chance-expected accuracy under every strictly proper score; rho's expected Brier is at least 0.25, the constant 1/2 forecast's; it is anti-aligned (its expected credence is below 1/2 exactly when rain is 90% likely).
- D1 is idle: the chances are 0.9 and 0.1, not mid-level.
- R is weak: it does not say reliability is closeness to chance; only that uniform, large distance from chance is unreliability.
- Deterministic-world version of R for chance-sceptics.
Illustrations for unconditional variants (barometer) and for conditional variants (testimony in a rare cell).

## 5. Objections and replies (1350)
5.1 Is the witness really unreliable in w_rho? (a) "Reliability is calibration, by definition": then reliability is no relation of fit with an environment, since one process has it in every environment; Connection Problem (Pettigrew) worsens. (b) "It is a learner whose credences are justified": argument needs only that CR-S's verdict of maximal reliability in w_rho is wrong; scorecard repair (Dawid's point via Oakes) explains why a calibrated-everywhere process cannot be a coherent conditionalizer.
5.2 Randomization and psychological reality: Foster-Hart; generality problem.
5.3 w_rho is remote: it is an exogenous chance world; dominance makes W idle; any world could be actual; on Dunn's criterion (regularities the process tracks are held fixed) a process tracking nothing has no restriction (conditional on the secondary reports).
5.4 Demon worlds: robustness as a virtue? Right verdict for the wrong reason; overgeneration.
5.5 Comparative calibrationism: benchmark dilemma.

## 6. Beyond calibration (700)
- Expert-testing results as P5': Sandroni (finite horizon); Olszewski-Sandroni 2008 (future-independent, with their verbatim gloss); Shmaya (Borel, truth always passes). Witness forecasts by a randomly drawn theory, so it is history-based and P1 applies. So C1 covers these standards: (G).
- Limits: non-manipulable tests exist (Dekel-Feinberg; Olszewski-Sandroni 2009): future-dependent, unbounded data, category notion; Fortnow-Vohra (computational); Al-Najjar et al. (restricted domains); Al-Najjar-Weinstein (comparative). Assessment: none gives a graded track-record measure; the comparative result shows what is missing: a benchmark that knows the chances.

## 7. What reliability for credence must be (550)
- Chance given grounds (Tang-type): degree of unreliability = expected (f - c_g)^2, the excess chance-expected Brier inaccuracy. Meets D1. Connects to accuracy.
- Basing: g = what the process uses.
- Why calibration looked right: chance-matching entails calibration almost surely (Dawid-type), not conversely; calibration is a symptom.
- Humean collapse: future-dependence; no fixed truth; anti-tracking regularity is part of the mosaic.
- Cost accepted: reliability is not a track-record property; no finite record verifies it. That is the lesson of the theorems, not a defect of the view.

## 8. Conclusion (150)

## Appendix (350)
A1 statement of FV (epsilon form). A2 proof of the anti-tracking lemma; exogeneity. A3 chance-matcher calibrated almost surely in w_rho (martingale SLLN, predictable selection). A4 deterministic learner miscalibrated in its anti-tracking world.

## Critique of round 3 (last check before drafting)
- Structure: linear, each section needed once. Good.
- Redundancy: 3.5 and 5.1(b) both touch learners; keep 3.5 to two sentences.
- Vagueness: "every occasion at least 0.4 in expectation" must be defined: E|f_t - c_t| >= 0.4 for all t, expectation over the process's randomization given the history. "Chance given everything the process takes as input" = chance of x_t given h_t (and the process's coin, which is independent). State it.
- Missing objection: "R is question-begging against calibrationism." Reply in 5.1(a): R is weaker than any accuracy measure; and the calibrationist's own motivation (D1) is satisfied by R's conception.
- Missing objection: "Use calibration as necessary only." Fine: then it is not calibrationist reliabilism in the SEP sense. One sentence in 2.2.
- Attribution risks: Dunn's nearby-world criterion (secondary); Tang's objection (SEP report); Pettigrew's Connection Problem (abstract). Phrase accordingly.
- Approved for drafting.
