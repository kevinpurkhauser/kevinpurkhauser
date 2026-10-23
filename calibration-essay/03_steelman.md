# 03. Steelmanning calibrationism

Target schema. Calibrationist reliabilism (CR): a credence is justified (to degree d) iff (to the extent that) it is produced by a process that is reliable (to degree d), where the reliability of a credence-forming process is a measure of its calibration, assessed over some range W of worlds. Variants differ on (i) what calibration is conditioned on, (ii) which worlds W, (iii) finite or limiting, (iv) what supplements calibration.

What the opponent wants from calibration (from Dunn as verified, and SEP): a reliability measure for credence that (a) does not punish mid-level credences in domains where only mid-level credences are appropriate (the reason for rejecting a Brier or truth-possession measure), and (b) is a matter of how the process performs, actual and counterfactual, a track record.

For each variant: statement; can a process with no information about the data-generating process satisfy it (by Step 2)? Verdict.

Notation: FV = Foster-Vohra forecaster (T4); FV_E = the same run separately within each cell of the agent's evidence partition, or the SSV/FRST forecaster with checking rules indexed by evidence (T6, T7); FH = Foster-Hart deterministic smooth-calibrated forecaster (T5); O1-world = anti-tracking chance world for a given history-based process.

---

## V1. Actual-world calibration
A process is reliable iff its actual outputs are calibrated.
- Ignorant satisfier: Goldman's uniform .7 (as reported in SEP); FV, trivially.
- Verdict: falls. Already conceded by calibrationists (the move to processes and nearby worlds).

## V2. Dunn's view: process-level, actual and nearby worlds
Reliable iff the process is well calibrated in the actual world and in nearby worlds (worlds differing in accidental features while the regularities the process tracks are held fixed, per secondary reports).
- The reply to Goldman: uniform .7 is calibrated actually only by accident; in nearby worlds where the base rate differs it is miscalibrated.
- Ignorant satisfier: FV is calibrated almost surely in every world of type W3, hence in every nearby world, whatever "nearby" means (O4). FH deterministically for smooth calibration.
- Verdict: falls. Moreover the robustness requirement cannot discriminate against FV at all (dominance, O4), and wider ranges favor FV over any informed process whose calibration depends on the world's regularities.

## V3. Hypothetical (limiting) frequency calibration
Reliable iff calibrated in the hypothetical infinite continuation of the process's use (van Fraassen-style "potential calibration", mentioned in the literature as a variant; I have not read van Fraassen's text, so the paper will state the variant without attributing it).
- Ignorant satisfier: FV is calibrated almost surely in every infinite continuation.
- Verdict: falls.

## V4. Normal-worlds calibration
Reliable iff calibrated in normal worlds (worlds where the process's environment is as it normally is).
- Ignorant satisfier: FV, by O4.
- Verdict: falls.

## V5. Conditional calibration on the agent's evidence (cell-wise calibration)
Reliable iff, for each evidence state e in the agent's evidence partition, among the occasions with evidence e and credence p, a fraction p is true; assessed across nearby worlds.
- Motivation: blocks the barometer case (the evidence-ignoring FV is miscalibrated within the barometer-high cell in worlds where the barometer is informative).
- Ignorant satisfier: FV_E. It uses the evidence only as a label: it has no information about how e bears on the outcome; it learns, by feedback, the frequency within each cell. Calibrated in every world, almost surely (T6 with checking rules "days with evidence e").
- Is FV_E ignorant in the relevant sense? It has no information about the data-generating process. But in worlds where outcomes are independent across days given e, calibration within cells forces its forecasts toward the conditional frequencies; there it behaves like an inductive learner. So the counterexample must not rest on FV_E behaving badly in nice worlds. It rests on: (i) O1-worlds for FV_E (chance set adversarially against its expected forecast given the cell): FV_E is always at least 0.4 from chance yet calibrated; the chance-matcher is calibrated too; tie; (ii) its credences are insensitive to the content of e until feedback accumulates in that cell, so on first and rare occasions (for fine-grained evidence, nearly all occasions) its credence is unconstrained by e's content. Example: e = "a reliable expert testifies the chance is 0.9", or "the die is symmetric". FV_E's first credences in that cell are whatever its bookkeeping dictates.
- Verdict: falls, but this is the first variant where the counterexample needs care. The paper should present O1 plus the dominance argument as the core, and the rare-cell point as a supplement.

## V6. Reference-class calibration (many reference classes at once)
Reliable iff calibrated relative to every reference class in a privileged countable family R (e.g., all classes definable from the agent's evidence).
- Ignorant satisfier: SSV forecaster for any countable R (T6), for every infinite data string.
- Verdict: falls.

## V7. Multicalibration
Reliable iff calibrated on every subpopulation identifiable by a class C of bounded complexity (Hebert-Johnson et al.), or online against every sequence (FRST 2011; Gupta et al.).
- Ignorant satisfier: FRST/online multicalibrated forecaster, for any C of bounded sequential complexity. For unbounded C, multicalibration against every sequence is not available; but then nothing satisfies it in every world, including the informed process (unless C is countable: SSV).
- Verdict: falls. Note: the bounded-complexity condition is what makes it achievable; enlarging C to all classes makes the standard unsatisfiable by finite records, not discriminating.

## V8. Inclusive calibrationism (Wilcox 2024, verified at abstract level)
Trustworthy only if produced by a maximally inclusive (takes into account all evidence the agent considers relevant) and well calibrated process.
- Ignorant satisfier: FV_E takes the evidence into account in the sense of conditioning its bookkeeping on it. If "inclusive" means using all evidence as input, FV_E is inclusive. If it means weighing evidence by its bearing, inclusivity is no longer a calibration condition but an evidentialist one, and the view becomes a hybrid of the Tang type.
- Verdict: falls in the outcome reading; in the evidential reading it is accommodated as a non-calibrationist hybrid. (Wilcox's topic is trustworthiness, not justification; the paper should mention the view only briefly, as a natural strengthening, without claiming Wilcox defends calibrationist reliabilism about justification.)

## V9. Finite-horizon calibration
Reliable iff, over the actual finite history of T uses (and nearby finite histories), the calibration error is below a tolerance tau.
- Ignorant satisfier: with expected l1 error of order T^{-1/3} uniformly over worlds (Step 2, sec. 2), FV meets any fixed tau for T large, with high probability. For small T, no process meets small tau reliably (lower bound T^{-0.46} approx), including the informed one. Also Seidenfeld: short-run calibration rewards hedging, a calibration score in the short run is improper.
- Verdict: falls.

## V10. Calibration plus sharpness (refinement) thresholds
Reliable iff calibrated and the refinement (spread of forecasts, equivalently Brier score for a calibrated forecaster) is at least as good as a threshold.
- Absolute threshold: re-imports Dunn's objection to Brier (punishes mid-credence domains).
- World-relative threshold equal to the best achievable given the chances: not outcome-based (requires the chance). That is the positive view.
- Verdict: absolute version rejected by the calibrationist's own lights; relative version is accommodated by the positive view.

## V11. Comparative outcome-based reliability
Reliable iff calibrated and not beaten in Brier score by any process available to the agent (a calibration version of Goldman's non-undermining clause).
- Escapes the barometer case: the barometer process beats FV.
- Ignorant satisfier: an aggregator that takes the available processes' outputs as inputs and achieves, on every sequence, cumulative Brier score within a bounded regret of the best available process (prediction with expert advice; to be cited only if verified: Cesa-Bianchi and Lugosi 2006, ch. 3; currently only the table of contents verified). Such an aggregator is not ignorant of the available processes' outputs; it defers to the best of them. So not a counterexample in the barometer case.
- Problem: reliability becomes relative to which processes are around. In an O1-world where every available process is history-based and uninformed, the best of them is certified maximally reliable while always at least 0.4 from chance. The benchmark must be the chance-tracking process, which may not be available. Comparative testing works (Al-Najjar and Weinstein) because one of the compared experts knows the truth.
- Verdict: survives the barometer case; fails O1-worlds unless the benchmark is the chance; then it is the positive view.

## V12. Non-manipulable test reliabilism
Reliable iff the process, regarded as a theory (its full contingency plan of credences), passes a non-manipulable test such as the global category test (Olszewski and Sandroni 2009) or Dekel-Feinberg.
- Not reached by T10-T13: these tests are future-dependent and infinite-horizon.
- Costs: (i) not calibration and not a track record of credences actually formed: it evaluates the process's predictions about data not yet observed (Olszewski-Sandroni 2008 say this is necessary); (ii) the verdict is settled only by the infinite future, so no finite stretch of the record bears on it; (iii) separating power is topological (category): each manipulator fails on a non-meagre set of worlds, which says nothing about how far its credences are from chance where it passes; (iv) pass/fail, no degrees; the calibrationist wanted a graded measure. Details of (iii) must be stated only at the level verified (abstract: controls type I error, non-manipulable, no continuum hypothesis).
- Verdict: a genuine limit on the generalization. The paper must state that outcome-based standards immune to manipulation exist, and argue that they are not what calibrationists want and do not supply a graded reliability measure. Honest status: not refuted, set aside with reasons.

## V13. Computationally bounded reliabilism
Restrict processes to efficient ones; use a Fortnow-Vohra-type test.
- Calibration itself is achievable efficiently by FV; so calibrationism gains nothing. The Fortnow-Vohra test is specially designed, relies on unproven hardness assumptions, and is not a calibration test.
- Verdict: does not rescue calibrationism; a limit on the generalization (state it).

## V14. Chance calibration given grounds (Tang-type indicator view; and, per SEP, an evidence-relative calibration view shown by Pettigrew to be extensionally equivalent to a version of it)
C(p) is justified only if based on a ground g such that the objective probability (chance) of p given g approximates C(p).
- Ignorant satisfier? Consider FV with ground g = (history, randomization outcome). Chance of x_t given g is the world's conditional chance, not FV's forecast. In O1-worlds FV is at least 0.4 from it every day. In nice (independent) worlds FV's forecasts converge toward conditional frequencies and so approach the chance; there the view counts FV's later credences as approximately justified, which is the right verdict for a learner.
- Is it outcome-based? No. It requires a chance. If chances are Humean (supervene on the total mosaic), the condition is determined by outcomes, but (a) it depends on the whole mosaic including the future, so it is not future-independent and T12 does not apply; (b) there is no fixed data-generating measure that a "true expert" knows in advance, so the type I error framework does not apply as such; (c) O1 still applies if the forecaster's outputs are part of the mosaic, since the anti-tracking regularity is then part of the world's pattern and the best-system chances follow it (to be argued, not proved; flag as a plausibility claim).
- Verdict: survives. The paper must accommodate it: it is the strongest surviving view, and it is not calibrationism in the track-record sense. The paper's positive upshot should show why the theorems force a view of this form and what it adds: reliability as expected accuracy by the lights of chance given grounds, measured relative to the best achievable (the excess expected Brier score of a credence f over the chance c equals (f - c)^2, by the propriety decomposition E_c[(f - x)^2] = (f - c)^2 + c(1 - c)). This keeps Dunn's desideratum (a), since mid-level credences in mid-chance domains have zero excess, and answers why calibration seemed right: the chance-matching process is calibrated (almost surely), but not conversely.

## V15. Deflationary reply: the FV process is a learner and its credences are justified
The FV process uses the past outcomes, which are evidence. Its calibration is earned by learning, not luck.
- Answer: (i) dominance: CR says FV is at least as justified as any process, in every world, for every agent, whatever else the agent knows; even if FV's credences are sometimes justified, this verdict is false (barometer, testimony); (ii) O1-worlds: equally calibrated as the chance-matcher, though always 0.4 further from chance; a measure of reliability that ties them is not measuring reliability; (iii) FV adopts credences to repair its scorecard: Dawid (via Oakes) shows a coherent forecaster cannot adjust predictions to correct past miscalibration without sacrificing coherence; FV is calibrated in every world precisely because it is not a coherent Bayesian conditioning on a prior (a Bayesian expects calibration but is not calibrated in every world, T2, T1, T3). So the property that makes FV unbeatable on calibration is the property that makes it no model of evidential responsiveness.
- Verdict: the most important objection to answer explicitly; the dominance and O1 arguments do not depend on denying that FV ever yields justified credence.

## V16. The new evil demon reply
Calibrationism's robustness is a virtue: FV is calibrated even in demon worlds (O1 worlds are demon worlds for credence), so CR gives demon-world victims justification, as internalist intuition demands.
- Answer: the demon intuition credits the victim's good response to her evidence. CR gives the verdict whether or not the process responds to evidence (barometer case), so it gets the verdict for the wrong reason and overgenerates. The positive view can take a standard reliabilist line on demon worlds (normal-worlds chance, or the "actual-world" rigidification) without the overgeneration.
- Verdict: answerable; include as an objection.

## V17. Process individuation and psychological reality
Reliabilists evaluate psychologically real process types; FV is an algorithm, not a cognitive process; randomized credence is not credence.
- Answer: (i) FH is deterministic, stationary, finite-recall, finite grid; nothing exotic; (ii) reliabilism must say what makes any possible process reliable; the definition of reliability, not the frequency of FV-like agents, is at issue; (iii) the generality problem does not help: FV is a single uniform procedure; any natural type containing it is calibrated in every world because FV is.
- Verdict: answerable.

---

## Strongest surviving versions

1. V14 (chance given grounds): survives; not a calibrationist view in the track-record sense; the paper accommodates it as the positive upshot and must answer the Humean collapse worry.
2. V12 (non-manipulable test reliabilism): survives the theorems; set aside as a limit, with explicit reasons (future-dependence, infinite horizon, topological separation, ungraded). Must be stated honestly as not refuted.
3. V11 (comparative): survives the barometer case; fails in O1-worlds unless the benchmark is the chance; then it collapses into V14.

The strongest calibrationist view properly so called (track-record based) is V5/V7 with comparative supplement V11: conditional, multicalibrated, counterfactually robust, comparative. Against it: O1 plus dominance plus the benchmark dilemma (an available uninformed benchmark certifies ignorance; a chance benchmark abandons track-record reliability).

## Implications for the paper's thesis
- Main claim: no track-record (future-independent, outcome-based, world-by-world) measure of calibration, however conditioned and however modally robust, is sufficient for justification; the theorems show this is not a matter of finding the right reference class.
- Generalization: restricted as in Step 2 (finite horizon, future-independent, or Borel standards that the truth passes).
- Positive: chance-given-grounds with an accuracy-based graded measure (excess expected inaccuracy), plus basing. Calibration is a symptom of reliability, not its measure.
