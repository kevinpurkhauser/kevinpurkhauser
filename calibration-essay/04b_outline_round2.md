# 04b. Outline, round 2 (revised in response to 04a critique)

Main change: the core argument is now a single schematic argument about world-independently securable standards; calibration is one instance and the testing generalization is another. The barometer case is demoted to an illustration. All formal facts the argument needs are introduced in one section.

1. Introduction (400)
   - Reliabilism about credence needs a measure of reliability; calibration is the leading proposal (SEP formulation; Dunn).
   - Thesis: no measure of calibration, however conditioned and however modally robust, suffices for justification; nor does any outcome-based track-record standard of a broad and precisely specified kind. Reason: such standards can be met in every world by a process that uses no information about the world, and every such process has a world in which it is unreliable.

2. Calibrationism, parametrized (900)
   - Schema CR(X, W): a credence produced by process rho in world w is justified to the degree that rho is X-calibrated throughout W(w, rho).
   - X ranges over: sharp or smooth calibration; conditional on a family R of reference classes (evidence cells, groups); limiting or finite with tolerance.
   - W: actual world only; actual plus nearby (Dunn); normal worlds; all worlds.
   - Goldman's case; the nearby-worlds reply (as reported in SEP); Tang's evidence-insensitivity objection; why the reply seemed adequate (accidental calibration is fragile).
   - Two desiderata calibration was meant to meet: no penalty for mid credences; a track record.

3. Calibration without information (900)
   - Definition of a history-based process; "uninformed" = forecast rule fixed in advance, inputs only the history of the forecast sequence (outcomes, labels, own forecasts) and private randomness.
   - FV theorem with assumptions. Finite-sample rates.
   - Deterministic smooth calibration (Foster-Hart).
   - Checking rules (SSV), complexity-bounded families (FRST), multicalibration.
   - Anti-tracking lemma (O1): for every history-based process there is an ordinary exogenous chance world in which it is, on every day, at least 0.4 from the chance in expectation. Proof in appendix.
   - Contrast: a deterministic learner (e.g. a Bayesian) is miscalibrated in its own anti-tracking world; the uninformed calibrated process is not. That combination is what matters.

4. The argument (1100)
   - P1 For every history-based process there is a world in which it is not reliable. (O1 + premise R)
   - R (normative): a process whose credences in w are on every occasion at least 0.4 from the chances, and which is strictly dominated in chance-expected accuracy, on every occasion and under every strictly proper score, by another process available in w, is not reliable in w.
   - P2 Definition: S is world-independently securable iff some history-based process meets S in every world (almost surely, or with probability at least 1 - epsilon).
   - P3 If S is world-independently securable and sufficient for reliability, some history-based process is reliable in every world (on a set of runs of probability at least 1 - epsilon).
   - C1 No world-independently securable standard is sufficient for reliability.
   - P4 Every calibration standard X of section 2 is world-independently securable (theorems).
   - P5 Reliabilism: justification requires reliability (sufficiency direction of CR is what is targeted).
   - C2 For every X and W, CR(X, W) is false.
   - Note why W drops out (dominance).
   - Defense of R: proper-score dominance; anti-alignment; the calibrationist's own motivation (mid credences) is idle in w*.
   - Illustrations for the weaker variants: barometer, testimony.

5. Objections (1500)
   5.1 "Reliability for credence just is calibration" (deny R). Reply: then reliability is not a relation of fit; Connection Problem; proper-score dominance.
   5.2 "The process is a learner; its credences are justified." Reply: argument does not need that its credences are never justified; it needs CR's verdict that they are maximally justified in w*. Dawid/Oakes: scorecard repair versus coherence.
   5.3 "Randomized credence is not credence; FV is not a cognitive process." Reply: Foster-Hart deterministic; reliabilism is a theory of all possible processes; generality problem does not help.
   5.4 "w* is far-fetched / not nearby." Reply: w* is an ordinary exogenous chance world; the range W drops out; any world can be actual.
   5.5 "Demon worlds: robustness is a virtue." Reply: right verdict for the wrong reason; overgeneration.
   5.6 Comparative calibrationism. Reply: benchmark dilemma.

6. Beyond calibration (800)
   - Sandroni (finite horizon), Olszewski-Sandroni (future-independent), Shmaya (Borel). These give P4' for every such standard the chance-matcher meets. Same argument.
   - Limits, stated exactly: non-manipulable tests (Dekel-Feinberg; Olszewski-Sandroni 2009) are future-dependent and infinite-horizon; computational limits (Fortnow-Vohra); restricted domains (Al-Najjar et al.); comparative testing (Al-Najjar-Weinstein). Why none rescues track-record reliabilism.

7. What reliability for credence must be (700)
   - Chance given grounds (Tang-type); graded by excess expected inaccuracy (f - c)^2.
   - Why calibration looked right: chance-matching implies calibration almost surely, not conversely.
   - Humean collapse worry and reply.

8. Conclusion (200)

Appendix: proofs of O1 and of the chance-matcher's calibration; precise statement of FV. (400)

## Critique of round 2
- Section 5.2 and 5.1 overlap: both are about whether the uninformed process is in fact reliable. Merge as "Is the uninformed process unreliable in w*?" with two prongs (definitional and learner).
- Premise R contains "another process available in w": availability is not needed for unreliability. The chance-matcher may not be available to the agent. The point of R is about the process's relation to the chances, not comparison with an available competitor. Remove availability; use dominance by the chance function itself, which is a fact about w, not about rivals.
- P3 in the probabilistic case is sloppy: CR evaluates realized records, so "reliable on a set of runs" conflates CR's verdict (run-dependent) with reliability (process-environment relation). Better: P3: if S is sufficient for reliability, then whenever a run meets S the process is reliable; so in w* the process is reliable on runs of probability at least 1 - epsilon; but it is unreliable in w* on every run (reliability in R is a property of the process in the environment); contradiction since 1 - epsilon > 0.
- Section 2 needs to make explicit that CR is a sufficiency claim as well as a necessity claim; target only sufficiency.
- The argument's dependence on "chance" in R: a calibrationist who rejects chances altogether? Then use deterministic version of O1: in a deterministic world (chances 0/1), the uninformed process's expected credence is on the wrong side of 1/2 each day. Need to mention: R can be stated with truth-values in deterministic worlds (expected Brier at least 1/4 every day while a process with credence equal to the truth-value scores 0). Add one sentence.
- Missing: what exactly is the "range" W for the uninformed process under Dunn: process-relative nearby worlds are those that hold fixed "the regularities the process tracks". For FV, what regularities does it track? None; so the nearby worlds could be all worlds. Good point for 5.4: Dunn's own criterion, applied to a process that tracks nothing, plausibly makes every world relevant, and FV is calibrated in all. Use with care: Dunn's text not verified beyond secondary reports. Frame as conditional.
- Section 6 limits: risk of overclaiming about non-manipulable tests. Restrict to what abstracts say.
- Section 7 needs a sentence on basing (grounds the process actually uses) and on the Connection Problem (cite Pettigrew only for the problem, not his solution).
- Length: appendix + 8 sections around 6,800 planned. Too long. Cut: section 3 to 800, objections to 1300, section 6 to 700, appendix to 350.
