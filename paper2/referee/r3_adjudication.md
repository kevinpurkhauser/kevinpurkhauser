# Round 3 adjudication (fresh subagent)

Report reproduced verbatim from the subagent's hand-back.

# Adjudication of round 3 (draft v4)

I read only the files in the adj/ folder. For round 1 I left out every point that concerns a planted error in planted_errors.md: the Garber attribution, the overgeneralised Corollary 2, E[s] in place of E[1/s], the Freer and Roy misattribution, and Gödel's first theorem cited for the second. None of those points is used below as an earlier location. Round 1 locations are written cal_X#, round 2 locations r2_X#, and r2_C uses its own labels (S#, A#, B#).

## 1 and 2. Every round 3 [S] point, with its classification

Round 3 has 42 [S] points: A has 10, B has 15, C has 7 and D has 10. C's points 4, 5, 7 and 12 to 19 are unlabelled verification notes, and its point 3 is [P], so none of them is counted.

| Point | Summary | Status | Earlier location (for REPEAT) |
|---|---|---|---|
| A1 | "Exactness, not the prior, is the obstacle" is not shown. Prop 3(a) also supplies a presented density, and Section 5.3 concedes that exact reports work with one. | REPEAT | cal_A8, cal_B6, cal_C9 (N3 against the qualification that an exact report with a presented density works); r2_A5; r2_C S10 |
| A2 | The "wrong object" claim is overstated. The 5.3 preference for putting slack in the channel is undercut by 5.4. | REPEAT | cal_B7, cal_A10 (the world/channel boundary is not principled); r2_A5 |
| A3 | N4 and Lemma 3's "whatever its priors" are false for interval reports. Counterexample: atoms at halting-coded points make mu([0,1/2]) noncomputable. | NEW | |
| A4 | The paper is inconsistent about "inexact". Format L conditions on an exact reading. The real obstacle is a deterministic channel with no presented density. | REPEAT | r2_D7 (the channel-modeller conditions on its reading exactly); r2_B8, r2_A6, r2_C S9 ("noisy" should be "not determined by the hypotheses") |
| A5 | Novelty is not positioned against known non-uniformity results (Hoyrup, Rojas and Weihrauch on Radon-Nikodym derivatives). | REPEAT | r2_A4, r2_C S10, r2_D9 (the Hoyrup, Rojas and Weihrauch citation itself is new) |
| A6 | The Prop 2 proof mixes binary-digit and Cauchy-name oracles. Also: n<2 is undefined, and the "computation is genuine" paragraph is unnecessary. | NEW | |
| A7 | Appendix B is trivial for FOLLOW: every updatable member has the same kernel, so a constant procedure works. "Commits" is undefined, and the Gödel corollary needs an HBL predicate and adds little. | REPEAT | r2_A1, r2_B1 (constant procedure on the updatable members); r2_A7 (Gödel corollary ornamental); r2_C S6, cal_C2, cal_D2 (Gödel hypotheses) |
| A8 | The Dutch book paragraph misapplies Meehan and Zhang. The procedures output posteriors over H only, so propriety with respect to Y is not delivered. | REPEAT | r2_C S8 |
| A9 | The competence/performance defence cites Kripke but ignores Kripke's own objection to the competence move. | NEW (r2_D3 had only asked the paper to engage Kripke's finitude point) | |
| A10 | "The tail matters" (pi(s)=2s) shows only that the sufficient condition fails, not that updating fails. | REPEAT | r2_A2 (y-local bound for 2s with two readings); r2_D4, r2_C S1 |
| B1 | Same as A1: exactness is confounded with a presented density bound, and 5.3 concedes it. | REPEAT | as A1 |
| B2 | The reply to the labelling objection fails: relabelling Z as the reading turns the exact case into format L. | REPEAT | cal_B7; r2_B11 (last bullet: constrains the joint) |
| B3 | "Any prior" hides an equally strong restriction on channel models, so the comparison of open-ended learners is unmatched. | REPEAT | r2_D1, r2_B11, r2_A2 |
| B4 | The interval format is discrete evidence, which the paper puts out of scope. It also needs coarsening at random. | REPEAT (discrete-evidence half); the coarsening half is counted in NEW issue I4 | r2_B5 |
| B5 | Same as A3: "whatever its priors" is false for intervals when there are atoms. | NEW | |
| B6 | The "Finite precision" reply ignores Lévy's upward theorem: interval posteriors converge almost surely to the exact kernel. | REPEAT | r2_B5 (exact conditionalization as the ideal limit of finite-precision updating); cal_B9 |
| B7 | FOLLOW is too strong and does the deciding work. The thesis reduces to the platitude that computability depends on representation. | REPEAT | r2_B2, r2_D8, r2_D2, r2_A4 |
| B8 | The Dutch book defence begs the question by redefining the evidence, which violates total evidence. | REPEAT | cal_B9, cal_C11, r2_B12, r2_C S8 |
| B9 | The AFR claims about discontinuity and shrinking noise are unverified, and uniform approximation is not distinguished from almost-sure approximation. | REPEAT | r2_C S4, S5 (B2, B3) |
| B10 | The AFR "Corollaries 9.6 and 9.7" numbering is doubtful, and AFR's "sufficiently smooth" hypothesis needs checking. | REPEAT | r2_C B4, B5; r2_B13; r2_A8; cal_A13 |
| B11 | Prop 2's novelty is unsupported (AFR, Hoyrup and Rojas). | REPEAT | as A5 |
| B12 | The "natural response" is a straw man. 4.2 "done properly" and 5.3 concede that it works. | REPEAT | r2_A5 |
| B13 | Same as A6: the Prop 2 proof treats oracle names as binary digits. | NEW | |
| B14 | Same as A10: "the tail matters" shows less than claimed. | REPEAT | as A10 |
| B15 | "No floor" is in effect a soft floor through the prior on s. | REPEAT | r2_C S3 (slack moved into the prior over s) |
| C1 | Same as A6: binary versus Cauchy representations in the Prop 2 proof. | NEW | |
| C2 | Lemma 1 error-budget slip: it needs w_M ≤ 2^-(k+1), not w_M < 2^-k. | NEW | |
| C6 | Prop 2's novelty is not located against known non-uniformity results. | REPEAT | as A5 |
| C8 | Prop 3(b)/N4 overreach: (i) atoms; (ii) the report mechanism needs coarsening at random. | NEW | |
| C9 | F4 places its joint-measure example outside J_ex, so the F1 to F5 argument is invalid as written. | NEW | |
| C10 | The "wrong object" thesis is in tension with 5.3 and should be stated as a disjunction. | REPEAT | as A1 |
| C11 | The Kripke citation cuts against the competence move. | NEW | |
| D1 | "Exactness, not the prior" is contradicted by 5.3, and the channel preference is undercut by 5.4. | REPEAT | as A1 and A2 |
| D2 | Format L conditions on an exact point, so the thesis should be about deterministic versus dominated channels. | REPEAT | as A4 |
| D3 | Interval format fails for arbitrary priors (atom counterexample). | NEW | |
| D4 | Conditioning on "Z in J" needs coarsening at random. | NEW | |
| D5 | FOLLOW is trivially satisfiable (a singleton format) without a closure condition. | REPEAT | cal_A5, cal_B3, cal_C4, cal_D3 (FOLLOW's domain; tailored procedures); r2_B3 |
| D6 | F5 is near-analytic given FOLLOW, plus the F2 (J_ex) versus F4 slip. | REPEAT for the main point; the F2/F4 slip is counted in NEW issue I17 | r2_D8, r2_B2 |
| D7 | Prop 2 is an instance of known Radon-Nikodym non-uniformity. | REPEAT | as A5 |
| D8 | "No floor" relies on a strong prior on s (a soft floor), and "the tail matters" is shown only for the sufficient condition. | REPEAT | r2_C S3; r2_A2 |
| D9 | The Section 2 definitions do not cover format L, and the bound must be part of the input. | REPEAT | cal_D8, r2_A8 (whether the bound is supplied as input) |
| D10 | Same as A6: binary versus Cauchy representation. | NEW | |

Point tally: 13 NEW (A3, A6, A9, B5, B13, C1, C2, C8, C9, C11, D3, D4, D10) and 29 REPEAT. Two of the REPEATs, B4 and D6, also contain a new sub-point, and those sub-points are counted under the new issues I4 and I17.

## 3. Distinct issues

| Issue | Description | Round 3 points | Status |
|---|---|---|---|
| I1 | Exactness is confounded with a presented density. Thesis 1 and "wrong object" are contradicted by 5.3. | A1, B1, B12, C10, D1 | REPEAT |
| I2 | The asymmetry between channel and prior is labelling, and the 5.3 defence is undercut by 5.4. | A2, B2, D1 (part) | REPEAT |
| I3 | Interval format "whatever its priors" is false (atoms, null boundaries). | A3, B5, C8(i), D3 | NEW |
| I4 | Interval conditioning needs coarsening at random. | B4 (part), C8(ii), D4 | NEW |
| I5 | Interval evidence is discrete, and the Finite precision reply ignores almost-sure convergence. | B4, B6 | REPEAT |
| I6 | "Inexact" is mis-described: L conditions on an exact reading, and the real line is deterministic versus dominated channels. | A4, D2 | REPEAT |
| I7 | Novelty of Prop 2 against known non-uniformity results (AFR, Hoyrup, Rojas and Weihrauch). | A5, B11, C6, D7 | REPEAT |
| I8 | The Prop 2 proof mixes binary and Cauchy representations. | A6, B13, C1, D10 | NEW |
| I9 | Lemma 1 error-budget slip. | C2 | NEW |
| I10 | Appendix B is trivial for FOLLOW, "commits" is undefined, and the Gödel corollary is idle. | A7 | REPEAT |
| I11 | Dutch book reply: Meehan and Zhang, propriety, total evidence. | A8, B8 | REPEAT |
| I12 | Kripke's objection to the competence/performance move. | A9, C11 | NEW |
| I13 | "The tail matters" shows only that the sufficient condition fails. | A10, B14, D8 (part) | REPEAT |
| I14 | "No floor" is a soft floor through the prior on s. | B15, D8 | REPEAT |
| I15 | FOLLOW is too strong, and format-relativity is near-analytic. | B7, D6 | REPEAT |
| I16 | FOLLOW is trivially satisfiable without a closure condition. | D5 | REPEAT |
| I17 | The F2 (J_ex) versus F4 (joint-measure) slip makes F1 to F5 invalid as written. | C9, D6 (part) | NEW |
| I18 | Presentation definitions do not cover format L, and the bound should be an input. | D9 | REPEAT |
| I19 | "Any prior" hides a restriction on channel models. | B3 | REPEAT |
| I20 | AFR content claims (discontinuity, shrinking noise) are unverified. | B9 | REPEAT |
| I21 | AFR corollary numbering and the smoothness hypothesis. | B10 | REPEAT |

There are 21 distinct issues: 6 NEW (I3, I4, I8, I9, I12, I17) and 15 REPEAT.

## 4. The five most serious distinct issues

1. **I1, the exactness/presented-density confound (REPEAT).** This is the headline thesis, and all four referees reject it in the same form. The paper's own Section 5.3 concedes the point. It was first flagged as the N3 qualification in round 1 and as "natural response done properly" in round 2, and it is still unresolved.
2. **I3, the interval format is false for general priors (NEW).** This is a false positive claim with an explicit counterexample from A and D, raised independently by all four referees. It also undermines the Finite precision reply.
3. **I7, novelty against known non-uniformity results (REPEAT).** All four referees raise it. Without this comparison the technical contribution cannot be assessed, and it has persisted since round 2 (r2_A4, r2_C S10, r2_D9).
4. **I2, the channel/prior asymmetry is labelling (REPEAT).** This is what "wrong object" would need for support. It has been raised since round 1 (cal_B7), and Section 5.4's claim that the channel model answers to evidence now undercuts it from inside the paper.
5. **I6, "inexact" is mis-described (REPEAT).** The title thesis and the Section 6 reply both misdescribe format L, which conditions on an exact point. This was flagged in substance by r2_D7 and the round 2 "noisy" gloss points.

Next in seriousness are I8 (a core proof gap that all agree is easily repaired), I15 and I16 (FOLLOW is either too strong or trivially satisfiable), and I17 (the F-argument is invalid as written).

## 5. Round 3 verdicts and scores

| Referee | Role | Verdict | Originality | Correctness | Importance | [S] points |
|---|---|---|---|---|---|---|
| A | Specialist | Major revision | 4 | 5 | 4 | 10 |
| B | Defender | Major revision, bordering on reject | 5 | 5 | 4 | 15 |
| C | Technical | Major revision | 5 | 6 | 5 | 7 |
| D | Generalist | Major revision | 5 | 6 | 5 | 10 |
| Mean | | Unanimous major revision | 4.75 | 5.5 | 4.5 | 42 total |

**Assessment.** Most of the round 3 objections are repeats: 29 of 42 points and 15 of 21 issues. The most serious one, I1, has been raised in substance in every round. The new issues are concentrated in the material added in v4: the interval format (I3, I4), the new Prop 2 proof (I8, I9), the Kripke defence (I12) and the F-argument (I17).
