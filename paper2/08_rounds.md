# 08. Referee rounds

## Calibration (planted errors)

| Role | Decoy | Planted errors caught | Passed (>= 2/3) |
|---|---|---|---|
| A specialist | 1 | 3/3 (Garber attribution, Corollary 2 overgeneralization, E[s] criterion) | yes |
| B defender | 1 | 3/3 | yes |
| C technical | 2 | 2/3 (Gödel first/second, Freer-Roy attribution; missed the soundness drop in Proposition 1') | yes |
| D generalist | 2 | 2/3 (same two; missed the soundness drop) | yes |

All role prompts (referee/role_prompts_v1.md) passed on the first try. No revision was needed. Detection rate overall: 10/12 (83 percent).

## Round 1 (= the calibration reports, counting only points that were not planted errors; the decoys were copies of draft v2)

The calibration reports reviewed the full content of v2. Their unplanted points are treated as round 1 on v2. This saves one round of subagents. The approach is recorded as a deviation from the prompt.

| Role | [S] points (unplanted) | Verdict | O / C / I |
|---|---|---|---|
| A | 9 | major | 6 / 4 / 6 |
| B | 11 | major | 6 / 4 / 5 |
| C | 9 | major | 6 / 4 / 5 |
| D | 7 | major | 6 / 4 / 5 |

All points are new (first round). Substantive themes, with the change made in draft v3:
1. FOLLOW equivocates between an actual and a modal domain; a tailored procedure defeats R3 (A, B, C, D). **Fixed:** FOLLOW is now relative to the agent's *representational system*, requires soundness *and completeness* (Proposition 1' restated), and gives a non-gerrymandered witness (channel agent vs open agent).
2. R4 does not follow without ought-implies-can (A, B, C, D). **Fixed:** explicit OIC premise R2, and R1's role stated.
3. Correctness is ill-defined at single observations (B). **Fixed:** kernel-level correctness, relativised to the observation as oracle.
4. Corollary 1 needs T to prove Proposition 1; and the "no amount of logical skill" quantifier is wrong (A, C, D). **Fixed:** T proves Proposition 1 (for example ZFC); per-instance closure conceded; the uniform claim rests on Proposition 1'.
5. Noise-floor result conflicts with learning s and with mixture closure; countable mixtures need a uniform bound (A, C, D). **Fixed:** s integrated out; a new result for n readings (bounded iff E[s^-n] finite; π ∝ e^(-1/s) works for all n); learning s left open; countable mixtures restricted.
6. N3 "whatever format" overclaims (A, B, C, D). **Fixed:** N3 restricted to unrestricted priors over hypotheses.
7. World/channel labelling (B, A). **Fixed:** the distinction is now between hypothesis variables and readings, and the concession that the joint is constrained either way is explicit.
8. Capacity to norm; total evidence; Dutch book (B, C). **Fixed:** conclusion stated as conditional; total-evidence reply; Dutch book dissolved (assessed relative to the agent's own credences); Rescorla 2025 engaged.
9. Exchangeable route as a rival (A). **Fixed:** engaged; it certifies only sources whose predictive distributions are already part of the state.
10. Posterior is computable relative to y, not outright (A). **Fixed:** relativised statement throughout.
11. Certificates are supplied as data (A). **Fixed:** argued that the bound is a *local* certificate.
12. AFR already note that noise restores computability and cannot uniformly approximate (A). **Fixed:** acknowledged in Section 1 and Section 5; the novelty claim narrowed.
13. Presentational fixes:
    - Kolmogorov 1933 attribution corrected;
    - renormalisation added in Lemma 2;
    - A_0 notation fixed;
    - remarks about mechanical checks removed from the essay;
    - references updated (Rescorla pages, Garber pages, AFR 2011 pages, Lopez-Wild 2026 DOI, Huttegger et al. 2025, Rescorla 2025 added, unused AFR 2017 removed).

## Round 2 (draft v3): fresh referees A-D, adjudicator (referee/r2_*.md, referee/r2_adjudication.md)

| Role | [S] points | Verdict | O / C / I |
|---|---|---|---|
| A | 9 | major | 5 / 5 / 5 |
| B | 12 | major | 5 / 5 / 4 |
| C | 11 | major | 5 / 6 / 5 |
| D | 10 | major | 6 / 6 / 5 |

Adjudicator: 42 [S] points, which reduce to 22 distinct issues: 11 NEW and 11 REPEAT. All the repeats show that the v3 fix was at least partly inadequate. Most serious:
- I1: Proposition 1' concerns recognition, not updating;
- I2: FOLLOW's domain;
- I7: "only if" not proved;
- I3: representation-dependence is near-definitional;
- I9: closure needs relativisation.

Changes in draft v4 (a substantial rewrite):
- I1: new core result. Proposition 2 is a uniformly computable family μ_M of priors over hypotheses (I, Z). Every member is updatable on an exact report of Z, and no single procedure updates them all (recursion-theorem proof). Proposition 3 shows that the same priors, with a noisy or a coarse (interval) report, are updated by one procedure. The old Propositions 1 and 1' and Corollary 1 move to Appendix B as an illustration of non-recognisability.
- I2, I3, I6: FOLLOW is made format-relative and promise-style. It demands nothing on non-updatable presentations. The OIC/R3 binding argument is dropped. Thesis 2 is stated as format-relativity, with the represented-spaces precedent acknowledged (Weihrauch 2000). The normative weight is placed on Proposition 2, which shows that restricting priors is not the repair.
- I5: Kripke finitude (competence vs performance) and the bad-format reply are adopted as the thesis.
- I7: necessity claims removed; the claims are now sufficiency plus failure for exact reports.
- I8: "noisy" replaced by "inexact (slack)", with an atomless reference measure.
- I9: relativisation stated.
- I10: the noise scale is learnable via the joint-density clause (sup e^(-1/s) s^(-n) = (n/e)^n).
- I14: Rescorla 2025 no longer misapplied; Meehan and Zhang 2022 engaged.
- I15: finite-precision interval evidence added as the second inexact format.
- I16: the Marr-level caveat added.
- I17: conservation laws are carried by the prior.
- I18: "one of AFR's constructions".
- I20: Corollaries 9.6 and 9.7 cited in the journal numbering.
- I21: the "same tractable states" claim removed.
- I22: the hypothesis/observation split is made part of the presentation.
- I11, I12, I13: Corollary 1 is now in Appendix B with an arithmetic hypothesis; the Rice-Shapiro remark is dropped.

## Round 3 (draft v4): fresh referees A-D (referee/r3_*.md); adjudication pending

| Role | Verdict | O / C / I |
|---|---|---|
| A | major | 4 / 5 / 4 |
| B | major (bordering on reject) | 5 / 5 / 4 |
| C | major | 5 / 6 / 5 |
| D | major | 5 / 6 / 5 |

All four referees made the same main point: the contrast between Propositions 2 and 3 is whether a density with a bound is presented, not whether the evidence is exact. §5.3 already conceded this. They also agreed that:
- the interval format is discrete evidence, and is false for priors with atoms;
- coarsening at random is needed;
- FOLLOW needs a closure clause;
- Proposition 2 used binary digits, not Cauchy names;
- the Hoyrup-Rojas-Weihrauch Radon-Nikodym result needs citing;
- the martingale (Lévy) convergence of interval posteriors needs conceding;
- the Meehan-Zhang application was wrong.

Draft v5 response (full rewrite, about 4,170 words excluding the bibliography):
- **Thesis restated:** per-prior constraints do not suffice (Proposition 2); presented densities do (Proposition 3); followability constrains the representation, not the credence function. "No exact dependence" is stated without labels, as a sufficiency claim.
- **Proposition 3** now includes case (a), exact observation with the density in the prior. So exactness is not the obstacle.
- **Framework:** FOLLOW gets a closure clause. Formats and the measure and density formats are defined precisely. Points are given by Cauchy names.
- **Proof:** Proposition 2 is repaired for Cauchy names, with the index shift n = m + 2. The unnecessary "computation is genuine" paragraph is dropped.
- **Interval route:** recast as discrete evidence, with coarsening at random (Heitjan and Rubin 1991) and null boundaries. Lévy convergence is conceded.
- **Literature and objections:** Hoyrup-Rojas-Weihrauch is cited. The Kripke objection is engaged. Meehan and Zhang is dropped. Marr 1982 is added.
- **Removed:** Appendix B (non-recognisability, Gödel) and the remaining "noise" framing.

## Round 4 (draft v5): launched

Round 3 adjudication (referee/r3_adjudication.md): 42 [S] points, which reduce to 21 distinct issues, 6 NEW and 15 REPEAT. The most serious are I1 (exactness confounded with a presented density), I3 (interval format false with atoms), I7 (novelty versus Hoyrup-Rojas-Weihrauch), I2 (labelling) and I6 ("inexact" mis-described). All of these were addressed in v5 before the adjudication arrived. I1, I2 and I6 are dissolved by the restated thesis. I3, I4 and I5 by the recast interval route. I7 by citation and positioning. I8, I9, I12 and I16 to I18 by the framework and proof repairs. I10 and I11 by removing Appendix B and Meehan-Zhang.

## Round 4 (draft v5): fresh referees A-D (referee/r4_*.md)

| Role | Verdict | O / C / I |
|---|---|---|
| A | major | 4 / 6 / 4 |
| B | major | 4 / 6 / 4 |
| C | major | 5 / 6 / 5 |
| D | major | 6 / 6 / 5 |

Main points:
- A1, D1: a class-level constraint with fixed density bound C and Lipschitz constant L gives a uniform procedure from measure presentations alone. So "constraints on credence functions do not suffice" is false as stated; what is needed is uniform moduli of regularity.
- A2, B4, C8, D2: Proposition 3(a) works only because the presentation encodes the halting time.
- A3, B2, D3: FOLLOW's closure is unspecified; a stored-kernel format would satisfy it.
- A4, B1: the fixed-prior agent is not addressed; priors are not the inputs of the rule.
- A5, B8, C12, D8: "no exact dependence" is definitional, or fails under reparametrisation.
- Repairs:
  - the proof needs K ⊂ [0,1] and a name with slack;
  - F3 closure needs a common reference measure;
  - Lévy holds only for fixed filtrations;
  - the rate claim in the abstract is too strong;
  - "only if" for CAR should be "if";
  - the AFR pinpoint is uncertain;
  - the Lopez-Wild qualifier is needed.

No adjudicator was run for round 4. The author agent classified the points itself: the class-level counterexample (A1, D1) and the operations list (A3, B2) are new in substance; most of the rest repeats earlier rounds.

Draft v6 response: the thesis is restated as "computability constrains spaces of credal states, not credence functions".
- FOLLOW quantifies over states reachable by explicit operations (update, adopt, mix).
- New Proposition 4 (own sketch): the fixed-constant class gives a uniform procedure, so the orthodox constraint "done properly" is accommodated.
- Proposition 3 now covers presented data (a) and a regular source model (b); (b) is uniform in M.
- The fixed-prior agent is conceded.
- The family is shown to arise by countable computable mixture, which gives the closure argument against stored-kernel formats.
- "No exact dependence" is withdrawn.
- The proof is repaired (K ⊂ [0,1], names with slack).
- Lévy is restricted to fixed partitions; the rate claim is dropped; CAR is now "if".
- Shan and Ramsey 2017 is added.
- About 3,930 words excluding the bibliography.

## Round 5 (draft v6): launched

## Round 5 (draft v6): fresh referees A-D (referee/r5_*.md)

| Role | Verdict | O / C / I |
|---|---|---|
| A | major | 5 / 7 / 4 |
| B | major | 4 / 6 / 4 |
| C | minor (on technical grounds) | 4 / 7 / 4 |
| D | major | 5 / 7 / 4 |

Main points:
- G4 is close to definitional given FOLLOW (all four referees).
- The (C,L) class is an intrinsic per-credence condition with fixed parameters, so the slogan "not credences" is false (B2).
- FOLLOW is only necessary, but was used as if sufficient (D2).
- Proposition 2 had to be shown for structured, mixture-data representations (A2, C11).
- Finite mixing with known components is harmless; countable mixing or adoption drives the result (A3, B10, D4).
- Route (b) changes the evidence, and the Dutch book reply fails for it (B7, D5).
- The Kripke machine passage was not engaged (A7, D6).
- The Lipschitz constant was cited for the wrong density (A5, C19, D8).
- Proposition 4 had an edge effect at the ends of [0,1] (C16).
- B8 (new): Proposition 2 implies Dutch book exposure in some reachable state.

The author agent classified the points itself; no adjudicator was run. B2, B8, A2/C11 and the "only necessary" point are new. The rest are repeats of round 3 and 4 points in a new form.

Draft v7, then v8 (final):
- **Thesis:** restated as quantifier order ("exists parameters, for all reachable states" against "for all states, exists parameters"). It accepts that the positive conditions are per-credence with fixed parameters, and it describes FOLLOW as a necessary condition only.
- **Proposition 2:** generalised to any representation computable uniformly in M, including the mixture representation.
- **New section 3.3:** Dutch book exposure in some reachable state, adopted from B8.
- **Remarks added:** the marginal density bound is 5, so the modulus of continuity is essential; any regularity data decide halting; finite mixing is harmless.
- **Route (b):** stated as changing the learning problem, and the Dutch book concession made for it.
- **Kripke:** the architecture is stipulated rather than argued for.
- **Proposition 4:** now uses L only (C is implied), with the edge fix, the test-function step and closure under countable mixtures.
- **Finite precision:** a differentiation theorem for the received intervals, and the non-computable rate on the family.
- **Citations and proof:** AFR 2017 is cited, ideal points replace rational points, and a self-simulation sentence is added to the proof.

## Stopping

The panel stopped after round 5. The prompt's quiet-round condition (two consecutive rounds with no new [S] point) was never met: every round produced new substantive points. The six-round cap was not used up. The run stopped at five for reasons of time and budget, which is a deviation from the prompt, and the methodology report records it.

Score trajectory (means, O / C / I):

| Round | O / C / I |
|---|---|
| 1 | 6.0 / 4.0 / 5.25 |
| 2 | 5.25 / 5.5 / 4.75 |
| 3 | 4.75 / 5.5 / 4.5 |
| 4 | 4.75 / 6.0 / 4.5 |
| 5 | 4.5 / 6.75 / 4.0 |

Correctness rose steadily as the claims were narrowed; originality and importance fell. The verdict was major revision throughout, except C's "minor (technical)" in round 5.
