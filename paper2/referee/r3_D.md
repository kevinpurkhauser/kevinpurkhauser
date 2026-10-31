# Round 3: role D (generalist) on draft v4

Report reproduced verbatim from the subagent's hand-back.

Referee report: "Following Conditionalization: Computable Agents and Inexact Evidence"

Summary of contribution. The paper adds a small but real result: a uniformly computable family of priors in which each member's exact-report conditional distribution is computable, but no single procedure computes all of them, while AFR's ratio-of-integrals method updates the same family uniformly once the report is noisy (with a bounded computable density) or interval-valued. Its philosophical addition is to read this, through a rule-following principle (FOLLOW), as showing that "followed" conditionalization is format-relative and that the constraint belongs on the model of evidence rather than on priors. The second claim is weaker than advertised, because the paper itself concedes (Section 5.3) that a constraint on how priors are presented works just as well.

Points

1. [S] The central contrast "exactness, not the prior, is the obstacle" (abstract; Section 1, thesis 1; Section 7) is contradicted by Section 5.3. There the paper says exact reports can be followed if the prior gives Z a presented bounded density, and that the family {mu_M} fails "only because its densities are not presented uniformly." So Proposition 2 shows that uniform updating fails when you have both exact reports and priors given only as measures. Either restriction on its own gives uniformity. The result therefore does not show that the natural response is "aimed at the wrong object"; it shows there are two places to put the restriction. Section 5.3's argument for preferring the channel ("for an agent whose priors over its targets are meant to answer only to evidence") is undercut by Section 5.4, which insists that "the agent's model of its channel is part of the content of its credal state, and it answers to evidence like any other part." If the channel model answers to evidence, constraining it is just as much a constraint on credence as constraining the prior. Fix: restate thesis 1 as a disjunction (slack in the channel or slack in the presented prior), drop "wrong object" from the abstract and conclusion, and give a non-question-begging reason for preferring the channel that survives the Section 5.4 claim.

2. [S] The paper says repeatedly that inexact formats avoid "exact point evidence" (line 28: "exact point evidence is not something such a learner can represent"; Section 6, Finite precision: the learner cannot "treat the limit of its intervals as an exact point to be conditioned on"). This is inaccurate for format L. In L the agent conditions on the event Y = y, an exact point reading, using the oracle for y in exactly the way the exact-report procedure uses its oracle for z. What L excludes is that the reading is a deterministic function of the hypotheses; in other words, it requires the conditional law of Y given H to be dominated by a fixed reference measure with a bounded density. Section 5.1 half-recognises this ("slack"), but the abstract, introduction and Section 6 do not. Fix: state the thesis throughout as one about deterministic versus dominated channels, not exact versus inexact evidence, and rewrite the Finite precision reply. This also shows the positive half is AFR's dominated-case theorem, restated uniformly.

3. [S] The interval format overclaims. N4 and the abstract say interval reports give a single correct procedure "whatever its priors over hypotheses." Proposition 3(b) is proved only for mu_M, using the fact that Z has no atoms, so the boundary of J is null. For arbitrary computable priors this fails. Take a uniformly computable family whose atom sits at 1/2 + 2^{-n} if M halts at step n and at 1/2 otherwise. Then mu_M([0,1/2]) is 0 or 1 depending on whether M halts, so it is not uniformly computable. Priors can also give a reported rational interval probability zero. Fix: restrict (b) to priors with null boundaries for the reported intervals (for example, atomless reported quantities), or use randomised or open intervals, and weaken N4 and N5 to match.

4. [S] Conditioning on "Z in J" is the right update on the report "J" only if the coarsening mechanism is uninformative (coarsening at random, in the sense of Heitjan and Rubin). Section 6 proposes that a real-time learner conditions on the interval it has received, but intervals read off a Cauchy name of Z depend on Z in ways that need not be uninformative. Fix: state the condition and say what the agent must believe about its reporting mechanism. Note that this makes the interval format another case of a modelled channel.

5. [S] FOLLOW as stated is trivially satisfiable. Every credal state lies in many formats, including a singleton format, and some procedure is correct on any updatable presentation. So the second clause ("an agent follows conditionalization only if its credal states lie in a format on which it follows it") excludes nothing unless formats must be closed under the agent's own updating and belief-forming, and must contain whatever the agent could come to hold. Section 4.2 appeals to closure informally ("applied again and again to whatever states the agent's own updating ... produce") but never builds it into the principle. In Section 5, N1 (open-endedness) does the real work. Fix: build a closure or open-endedness condition into FOLLOW, and check that F2 to F5 and N2 to N5 still go through.

6. [S] F5 is close to analytic given FOLLOW, which defines following relative to a format. The paper admits "all the weight rests on F1," but then advertises format-relativity as a thesis. The argument also slips. F2 is stated for J_ex (exact point reports), but F4's example places the noisy-reading state in a general joint-measure format. That format contains J_ex's members as joint measures, so the conclusion holds, but F2 should be stated for the general joint-measure format. Fix: state F2 for the joint-measure format and present Section 4 as a consequence of FOLLOW plus Proposition 2, not as an independent thesis.

7. [S] Novelty of Proposition 2. The proof is correct (see point 11), but it is an instance of a familiar non-uniformity: a density, or Radon-Nikodym derivative, is not computable from a presentation of the measure alone, even when it is continuous and computable in each case. The paper says "the mathematics is elementary" but does not place Proposition 2 against this known fact, or against what AFR themselves say about discontinuity and non-uniformity of conditioning. Fix: add this comparison, so readers can see what is new beyond packaging.

8. [S] "No floor on noise" (Section 5.4) is in tension with "any prior." The construction needs a prior on s that decays faster than every power of s near 0 (e^{-1/s}), and the paper shows that 2s fails. That is a strong restriction on the prior over a hypothesis variable the agent is said to learn about. In effect it is a soft floor, and it is exactly the kind of prior constraint the paper says the channel approach avoids. Also, "the tail matters" is shown only for a sufficient condition. An unbounded density under pi(s) = 2s shows only that Lemma 3 does not apply, not that updating is non-uniform. Fix: acknowledge the prior restriction on s, and either prove failure for the 2s case or weaken the claim.

9. [S] The definitions in Section 2 do not cover format L. A "presentation" is defined as a program for the joint law, and an "updating procedure" takes such a presentation. L-presentations are a prior plus a density program plus a bound. The F3 and N4 claims need the definitions extended, and the bound must be part of the input, since uniformity depends on it. Fix: define presentations for each format explicitly.

10. [S] Representation of observations. Z is "identified with its binary expansion," and the proof of Proposition 2 uses cylinders [sigma] of binary digits. Section 2, though, gives the oracle as "an infinite stream of approximations," that is, a Cauchy-style name, which is the admissible representation. The positive results are naturally stated for Cauchy names. The negative proof does go through for Cauchy names (a finite prefix fixes a rational neighbourhood that contains whole E_n intervals once n is large enough), but as written the two halves use different representations. Given that the paper's thesis is about representation-dependence, this needs to be made consistent. Fix: use Cauchy names throughout and adjust the choice of n in the proof.

11. Technical checks (not points against the paper unless flagged).
- E_n: 2^{n-1} intervals of length 2^{-2n}, total 2^{-(n+1)}. Correct.
- Tents of mass 2^{-(n-1)} have peak 2^{n+2}, so f_n is at least 2^{n+1} on central halves. Correct.
- Posterior lower bound 2/3: correct.
- The diagonal argument in Appendix A is valid. "The computation is genuine" is more than needed: U's computation on e* with prefix sigma is a fixed deterministic fact, and its step-count bound is idle.
- Appendix B: valid. Both components share the Y-marginal B_Y, so I' is independent of Y with P(I' = 1 | y) = w, and restricting to I' = 1 recovers B[X | Y]. The Goedel II step is valid under the stated hypothesis that T proves the relevant facts.
- The calculation sup e^{-1/s} s^{-n} = (n/e)^n at s = 1/n is correct, and so is continuous extension by 0.
- [P] Lemma 1 needs w_M at most 2^{-(k+1)} (true, since non-halting by step k means n is at least k+1), not merely w_M < 2^{-k}, for the two error terms to sum to 2^{-k}. Say so.
- [P] w_M is undefined if M halts at step 0 or 1 (E_n needs n at least 2). Shift the index.
- [P] The metric d on measures on {0,1} is unspecified.
- [P] The symbol pi is used both for the prior on s and for the constant in (2 pi)^{-n/2}.

12. Claims about other authors.
- AFR's main theorem, and their observation that independent noise with a bounded computable density yields computability: accurately reported.
- The specific citation "Corollaries 9.6 and 9.7 in the journal numbering" I cannot verify. The authors should check it.
- The AFR examples of a conditional distribution discontinuous on a measure-one set, and the remark that shrinking noise does not in general approximate exact conditioning uniformly: plausible, but the paper should give theorem numbers.
- Rescorla 2018 (Dutch book and converse Dutch book for Kolmogorov conditionalization) and Rescorla's non-factive extension: accurately characterised.
- Meehan and Zhang: the use is hedged ("as I understand it"). The application is plausible but should be argued, not hedged, since the Dutch book reply depends on it.
- Kolmogorov 1933 versus later regular versions: accurate.
- Marr's computational and algorithmic levels: accurate, but Marr is cited without a reference entry [P].

13. Bibliography.
- [P] Rescorla 2025 has an open page range ("186-").
- [P] Huttegger, Walsh and Zaffora Blando 2025 is given as PPR volume 112(1). That volume number looks more like a 2026 volume, so check the year and volume.
- [P] Lopez-Wild 2026 could not be checked.
- The other entries (AFR 2011 LICS 107-116; AFR 2019 JACM 66(3) Article 23; Freer and Roy 2010 AISTATS PMLR 9; Garber 1983; Hacking 1967; Kripke 1982; Mahtani 2024; Meehan and Zhang 2022; Rescorla 2018; Weihrauch 2000) look correct as far as I can tell without a search.

14. [P] The abstract's two bullet lists, and the claim that "the scale can be learned without assuming a lower bound," should be softened to match points 3 and 8.

15. [P] The "Capacity" paragraph ("FOLLOW ranks formats, not agents") conflicts with FOLLOW's own second clause, which is a condition on agents. Clarify.

Verdict: major revision. The technical core is correct and neatly done, and the question is a good one. But the headline philosophical claim (evidence, not priors) is undercut by the paper's own Section 5.3 and Section 5.4. The interval half of the positive claim is false for arbitrary priors. FOLLOW needs a closure condition before it can carry the argument.

Scores: originality 5, correctness 6, importance 5.
