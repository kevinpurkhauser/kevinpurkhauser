# Round 2 adjudication (fresh subagent)

Report reproduced verbatim from the subagent's hand-back.

# Adjudication of round 2 (draft v3)

## Basis

I read only the nine files in the adj/ folder. These round 1 points only report planted errors, so I excluded them:

- Garber misattribution: A1, B13 (first part).
- E[s] boundedness condition: A2, B10.
- Corollary 2 overgeneralised: A7, B11.
- Gödel's first theorem cited for the second: C1, D1.
- Freer and Roy 2010 misattribution: C6, D7.

No round 1 referee caught the planted Proposition 1' soundness gap; C and D both marked Proposition 1' as verified. All five caught planted errors appear to be fixed in v3. Round 2 referees confirm the Gödel II wording, the Freer and Roy citation and the E[s^-n] condition.

Round 2 has 42 [S] points: A 9, B 12, C 11, D 10.

## 1 and 2. Round 2 [S] points, classified

"Fix inadequate?" applies only to REPEAT points. Issue codes (I1 to I22) are defined in section 3.

### Referee A

| Pt | Summary | Class | Round 1 location | Fix inadequate? | Issue |
|---|---|---|---|---|---|
| A1 | The abstract and Thesis 1 say Prop 1' holds "restricted to updatable priors". On the updatable members of {P_M}, a constant procedure is sound and complete, so this overstates the result. | NEW (small precursor: B20 [P] said "no sound general updater" reads stronger than proved) | n/a | n/a | I1 |
| A2 | The "only if" noise claim in the abstract is not proved, and the body disclaims it. A y-local bound may suffice, and learning s looks feasible. | REPEAT | A11, B14, C10 | Yes. The body was hedged but the abstract and conclusion were not, so the paper now contradicts itself. | I7 (also I10) |
| A3 | "Closed under updating" is false: posteriors are computable only relative to y. In the scale mixture, readings are not conditionally independent given h. | REPEAT | A9; A3, C7 | Yes. The unrelativised claim is still asserted. | I9 |
| A4 | Representation-dependence is a known phenomenon in computable analysis (Weihrauch, represented spaces), and the paper does not acknowledge it. | NEW | n/a | n/a | I4 |
| A5 | FOLLOW's completeness clause does quiet work. "Admit only uniformly updatable priors" is just the obvious response done properly. | REPEAT | A5, B3, B4, C4, D3 | Yes. The modal or system version of FOLLOW was adopted, but this objection is not met. | I2 |
| A6 | "Bounded density means noisy" fails for atomic reference measures and is weaker than ordinary noise. | NEW | n/a | n/a | I8 |
| A7 | Corollary 1 is ornamental, because Prop 1' already gives the uniform claim. Also, "any consistent extension" should be "any consistent, computably axiomatized extension". | REPEAT | A6(b); C3, D5 | Partly. The quantifier slip is fixed, but Section 4.4 still uses Corollary 1 as separate support. | I12 (also I11) |
| A8 | The uniformity and joint computability of the AFR bounded-density theorem should be stated and cited by number. | REPEAT | D8 | Yes. The exact hypotheses are still not given. | I20 |
| A9 | "No physical measurement is believed to satisfy" exact relations is unsupported. Conservation laws and deterministic latent maps are counterexamples. | REPEAT | B8 (second half) | Yes. The claim was kept unchanged. | I17 |

### Referee B

| Pt | Summary | Class | Round 1 location | Fix inadequate? | Issue |
|---|---|---|---|---|---|
| B1 | The procedure "always commit to K_M" is correct on every tractable P_M. Prop 1' shows only that updatable presentations cannot be recognised. The demand that a follower abstain is unargued. | NEW (same precursor as A1) | n/a | n/a | I1 |
| B2 | Representation-dependence is built into FOLLOW, so the argument begs the question. The addition analogy gives no independent support. | NEW | n/a | n/a | I3 (also I5) |
| B3 | Nothing principled separates a "representational system" from a domain chosen to suit one case. | REPEAT | B4, B3, A5 | Yes. The criterion round 1 asked for is still missing. | I2 |
| B4 | R3 ("can follow implies bound") is load-bearing but undefended. With OIC, an agent escapes the norm by becoming more expressive. | NEW (it arises from the OIC premise added in answer to round 1 A4, B1, C5, D4) | n/a | n/a | I6 |
| B5 | Evidence is modelled as an infinite oracle. A bounded agent receives finite-precision, positive-probability evidence, so ratio conditioning applies and the noise thesis disappears. | NEW (related to, but distinct from, round 1 B9) | n/a | n/a | I15 |
| B6 | Closure under updating needs oracle-relative presentations. | REPEAT | A9 | Yes | I9 |
| B7 | The claims about Bayesian cognitive science overreach: most of that work is at Marr's computational level. | NEW | n/a | n/a | I16 |
| B8 | The "noise" gloss is too strong: the slack may come from coarse-graining, or from a singular reference measure. | NEW | n/a | n/a | I8 |
| B9 | "Only general alternative" is underargued. Other certificate formats, such as a modulus of continuity, exist. | REPEAT | B14, C10, A11 | Yes | I7 |
| B10 | The open question about the noise scale probably has an answer under the prior e^{-1/s}. | REPEAT | A3, C7, D6 | Partly. v3 now concedes the gap instead of making a false claim, but leaves open a gap that is probably closable. | I10 |
| B11 | Verification block. The technical claims hold, with caveats: Corollary 1 needs arithmetic and formalised AFR; the Rice-Shapiro appeal in Corollary 2 needs the TV-to-weak step; Lemma 3's "any prior" clause is trivial. | Mixed. The Corollary 1 caveat is a REPEAT; the Corollary 2 caveat is NEW. | B12, C2, D2 (Corollary 1) | Partly (see I11) | I11, I13 |
| B12 | Rescorla 2025 is used for more than it shows. The channel prior is shaped by convenience, not by evidence. | REPEAT | C11 (Dutch book); A12 (Rescorla 2025); B8 (capacity to norm) | Yes. The added citation is misapplied. | I14 |

### Referee C

| Pt | Summary | Class | Round 1 location | Fix inadequate? | Issue |
|---|---|---|---|---|---|
| S1 | The "only if" thesis is not established; the abstract and conclusion contradict the body. | REPEAT | C10, B14, A11 | Yes | I7 |
| S2 | Closure under updating is false as stated; relativise. | REPEAT | A9 | Yes | I9 |
| S3 | The open question about s is answered by the paper's own route: the joint density is bounded under e^{-1/s}. | REPEAT | C7, A3, D6 | Partly | I10 |
| S4 | "The AFR examples are badly discontinuous" is false for AFR's everywhere-continuous construction. | NEW | n/a | n/a | I18 |
| S5 | AFR's "shrinking the noise does not approximate uniformly" remark has no location given. | NEW (citation check of material added in response to round 1 A12 and B9) | n/a | n/a | I19 |
| S6 | Corollary 1 is missing the arithmetic hypothesis Gödel II needs. | REPEAT | C2, D2, A6(a), B12 | Partly. The round 1 fix ("proves Proposition 1") dropped "enough arithmetic". | I11 |
| S7 | Rice-Shapiro is the wrong theorem for Corollary 2; cite Kreisel-Lacombe-Shoenfield/Ceitin, and handle TV versus the weak topology. | NEW (v3 apparently adopted round 1 A16 [P], which recommended Rice-Shapiro) | n/a | n/a | I13 |
| S8 | The Dutch book reply ignores Meehan and Zhang 2020. | REPEAT | C11 | Yes. The reply is still incomplete. | I14 |
| S9 | The N3/N4 dichotomy is not exhaustive. "Noisy" is necessary for a bounded density but not sufficient. | NEW | n/a | n/a | I8 |
| S10 | Prop 1' is a standard non-uniformity phenomenon. The channel format works by an unchecked promise (the bound), so R4 is close to definitional. | NEW | n/a | n/a | I4, I3 |
| S11 | The definition of a presentation does not fix which coordinates are hypotheses and which are observations. | NEW | n/a | n/a | I22 |

### Referee D

| Pt | Summary | Class | Round 1 location | Fix inadequate? | Issue |
|---|---|---|---|---|---|
| D1 | "Both systems make the same tractable states available" is false: the channel class excludes tractable joint states such as exact Y = Z. | REPEAT | A10, B7 (also D14 [P]) | Yes. v3 restates the contrast that round 1 challenged. | I21 |
| D2 | FOLLOW ranks the more capable open agent below the channel agent. The 4.2 reply answers only a procedure tailored to one case, not a sound procedure that commits on a large c.e. set. | REPEAT | C4, D3, A5, B3 | Yes. The defence still meets only the weakest form of the round 1 objection. | I2 |
| D3 | The addition analogy undercuts completeness: Kripke's finitude point, and the bad-format reading. | REPEAT | B5 | Yes. The analogy was kept and still cuts the other way. | I5 |
| D4 | The abstract claims a necessity the body does not prove. "Noisy" is weaker than "bounded density". | REPEAT | C10, B14, A11 | Yes | I7 (also I8) |
| D5 | Leaving the learning of s open conflicts with Section 5's claim that the channel model answers to evidence. It is probably closable via a bounded joint density. | REPEAT | D6, A3, C7 | Partly. A residual inconsistency remains. | I10 |
| D6 | Corollary 1's "any consistent extension" must say "computably axiomatized". | REPEAT | D2, C2, A6(a), B12 | Partly (wording) | I11 |
| D7 | Rescorla 2025 is misapplied: non-factive learning is not what the channel-modeller does. | REPEAT | A12, C11 | Yes | I14 |
| D8 | Given FOLLOW, representation-dependence is close to definitional. | NEW | n/a | n/a | I3 |
| D9 | Novelty of Prop 1' relative to AFR's own discussion of the conditioning operator needs checking. | NEW | n/a | n/a | I4 |
| D10 | Closure needs relativisation. A computable density excludes discontinuous densities such as uniform noise. | REPEAT | A9; D8 | Yes | I9 (also I20) |

## 3. Distinct issues

| Issue | Description | Round 2 points | Class |
|---|---|---|---|
| I1 | Prop 1' shows that updatable presentations cannot be recognised, not that they cannot be updated; the headline overstates it | A1, B1 | NEW |
| I2 | FOLLOW's domain or system is unprincipled, and its defence fails against sound recognising procedures | A5, B3, D2 | REPEAT |
| I3 | Representation-dependence is built into FOLLOW, so it is near-definitional | B2, C S10, D8 | NEW |
| I4 | Novelty: a known computable-analysis non-uniformity phenomenon; position relative to AFR | A4, C S10, D9 | NEW |
| I5 | The addition analogy cuts the other way | D3 (also B2, A4 in passing) | REPEAT |
| I6 | R3 ("can follow implies bound") undefended; exemption by becoming more expressive | B4 | NEW |
| I7 | "Only if" necessity of bounded densities not proved; other formats exist | A2, B9, C S1, D4 | REPEAT |
| I8 | "Bounded density" is not the same as "noisy" | A6, B8, C S9 (also D4) | NEW |
| I9 | Closure under updating needs relativisation and conditional independence | A3, B6, C S2, D10 | REPEAT |
| I10 | Learning the noise scale left open, probably closable, and inconsistent with Section 5 | B10, C S3, D5 (also A2) | REPEAT |
| I11 | Corollary 1 hypotheses (arithmetic; computably axiomatized) | C S6, D6, B11 (also A7) | REPEAT |
| I12 | Corollary 1 ornamental relative to Prop 1' in Section 4.4 | A7 | REPEAT |
| I13 | Rice-Shapiro misattribution and topology in Corollary 2 | C S7, B11 | NEW |
| I14 | Dutch book reply: Rescorla 2025 misapplied, Meehan and Zhang omitted | B12, C S8, D7 | REPEAT |
| I15 | Infinite-oracle evidence versus finite-precision boundedness | B5 | NEW |
| I16 | Overreach about Bayesian cognitive science (Marr levels) | B7 | NEW |
| I17 | "No physical measurement satisfies exact relations" unsupported | A9 (also B12) | REPEAT |
| I18 | AFR examples wrongly called "badly discontinuous" | C S4 | NEW |
| I19 | AFR shrinking-noise remark has no location | C S5 | NEW |
| I20 | Hypotheses and uniformity of the AFR dominated theorem not stated | A8 (also D10) | REPEAT |
| I21 | "Same tractable states available" is false; the channel class restricts the joint | D1 | REPEAT |
| I22 | Presentations do not fix the hypothesis/observation split | C S11 | NEW |

**Counts: 22 distinct issues: 11 NEW and 11 REPEAT.**

All 11 repeats show that the v3 fix was at least partly inadequate.

- **Fully inadequate:** I2, I5, I7, I9, I14, I17, I20, I21. The original problem persists, or the new wording revives it.
- **Partly inadequate:** I10, I11, I12. The false claim was withdrawn or the main slip corrected, but a gap or new wording problem remains. For I11, adding "proves Proposition 1" dropped the arithmetic hypothesis.

Some round 1 issues were not raised again and appear resolved:

- R1 to R4 invalidity (OIC added; mechanical-check claim gone)
- N3 "whatever format"
- countable mixtures in Lemma 3
- correctness at single observations (round 1 B2)
- Lemma 2 renormalisation
- the "no logical skill" quantifier slip

Three new issues were induced by round 1 fixes:

- I6 follows from adding OIC.
- I13 follows from adopting the Rice-Shapiro citation suggested at round 1 A16.
- I3 follows from making FOLLOW system-relative.

On I19, referees disagree. A and B both report that they verified AFR's shrinking-noise remark; C could not locate it. It is probably a false alarm, but the author should still give a precise location.

## 4. Five most serious issues

1. **I1 (Prop 1' misread).** The headline technical claim and the open agent's failure in the witness both rest on reading Prop 1' as an updating failure. B1 shows a single procedure that is correct on every tractable P_M, so what fails is recognition (abstention), which the paper never argues a follower must achieve.
2. **I2 (FOLLOW's domain and defence).** This was raised by all four referees in round 1 and by three again. Without a principled criterion for the system, and a reply to sound procedures that commit on large c.e. sets, Thesis 2 is not established.
3. **I7 ("only if" unproved).** Four referees agree. The abstract and conclusion assert a necessity the body explicitly disclaims, and A2's y-local bound suggests the boundedness line may be drawn in the wrong place.
4. **I3 (near-definitional).** Even if I2 is repaired, three referees argue that representation-dependence then follows almost by definition from FOLLOW plus a known non-uniformity fact (I4), so Thesis 2 risks being trivial rather than false.
5. **I9 (closure under updating).** All four referees say this is false as stated. It is a repeat that v3 left unfixed, and the channel agent's witness depends on the class containing its own posteriors. The repair (relativisation) is likely routine but must be made.

Next in line are I10 (noise-scale inconsistency, probably closable) and I4 (novelty).

## 5. Verdicts and scores

| Referee | Role | Verdict | Originality | Correctness | Importance |
|---|---|---|---|---|---|
| A | specialist | Major revision | 5 | 5 | 5 |
| B | defender | Major revision | 5 | 5 | 4 |
| C | technical | Major revision | 5 | 6 | 5 |
| D | generalist | Major revision | 6 | 6 | 5 |
| Mean | | Unanimous major revision | 5.25 | 5.5 | 4.75 |

Compared with round 1, mean correctness rose from 4.0 to 5.5. Mean originality fell from 6.0 to 5.25, and importance from 5.25 to 4.75. The verdict was major revision in both rounds.
