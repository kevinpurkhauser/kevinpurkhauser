# Round 3: role C (technical) on draft v4

Report reproduced verbatim from the subagent's hand-back.

REFEREE REPORT (technical and citation check)
Submission: "Following Conditionalization: Computable Agents and Inexact Evidence"

Summary. The paper builds a uniformly computable family of priors mu_M (Section 3.1). Each member is updatable on an exact report of Z (Section 3.2), but no single procedure updates them all (Proposition 2). With a noisy report of bounded density, or with an interval report, one procedure updates them all (Proposition 3). From this the paper argues, via a principle FOLLOW, that conditionalization is followable only relative to a format, and that an open-ended learner must treat continuous evidence as inexact. I checked every mathematical step and every citation I could. The central construction and Proposition 2 are essentially correct. The noise-scale computation and Appendix B are correct. The main problems are these:
- an unstated representation assumption in the proof of Proposition 2;
- an error-budget slip in Lemma 1;
- an overclaim about the interval format (atoms, and the coarsening mechanism);
- a format slip in F4;
- a tension between the "wrong object" thesis and Section 5.3;
- a Kripke citation that cuts against the use made of it.

My web access was limited. arxiv.org, ar5iv and cfreer.org were blocked in this session, so I could not open the AFR full text. My checks of AFR's content rest on search excerpts and abstracts.

Points

1. [S] Proposition 2 assumes binary-digit oracles, but the framework says otherwise.
- The framework (Section 2) defines the observation oracle as "an infinite stream of approximations".
- The proof (Appendix A) instead treats sigma as a finite string of binary digits of z, with [sigma] a dyadic cylinder. It uses |sigma| to guarantee that "the digits of z in positions n to 2n are free inside [sigma]". Section 3.1 also says "identified with its binary expansion".
- The two representations differ. The binary-expansion representation of [0,1] is not admissible, and a procedure computable from Cauchy names is not the same thing as one computable from binary digits.
- With Cauchy names, the set of z compatible with a finite prefix sigma is the intersection of the balls B(q_j, 2^-j) for j up to |sigma|. That is an open interval whose width can be far smaller than 2^-|sigma|, so "n - 1 >= |sigma|" no longer guarantees that it contains a whole interval of E_n.
- Verdict: the conclusion survives, but the step as written is wrong for the stated framework.
- Fix: either fix the oracle as binary digits throughout, which works because U is quantified over oracle machines of that kind, and say so. Or, for Cauchy names, have M* compute a rational interval inside the open set determined by sigma, with width r, and choose n so that 2^-(n-1) < r/2 as well as n > t. Then the interval contains a whole period of the E_n pattern, so it contains a whole interval of E_n.

2. [S] Lemma 1 (Appendix A) has an error-budget slip.
- The text approximates "within 2^(-k-1)" and then adds a total-variation error "w_M < 2^(-k)". These sum to more than 2^-k, so the stated bound does not follow.
- The bound holds anyway: if M has not halted by step k, it halts at step k+1 or later, so w_M <= 2^-(k+1), and the total is at most 2^-k.
- Fix: state w_M <= 2^-(k+1). The main-text version of Lemma 1 also ignores the approximation error of the uniform component and should be brought into line.
- Also verified: Prokhorov distance is bounded by total variation, and the construction is uniform in M by the s-m-n theorem.

3. [P] The case n = 1 is undefined. E_n is defined only for n >= 2, but w_M = 2^-n is assigned whenever M halts at step n. Set w_M = 0, or use f_2, when M halts at step 1. M* itself always halts at a step n >= |sigma| + 2 >= 2, so the proof is unaffected.

4. Verified: the construction in Section 3.1.
- E_n frees digits 1 to n-1, so it is a union of 2^(n-1) intervals of length 2^(-2n). Their total length is 2^-(n+1).
- Each tent has mass 2^-(n-1), so f_n has total mass 1 and is continuous.
- The peak height is 2 x mass / length = 2^(n+2). On the central half of each interval the tent is at least half its peak, so f_n >= 2^(n+1), as claimed.
- The posterior formula is correct. The lower bound 2/3 holds: w f_n >= 2, and x/(a+x) is decreasing in a, so replacing (1 - w) by 1 gives a valid lower bound.
- Each fixed kernel is computable: for a halting M it is a computable function of z, and for a non-halting M it is the constant delta_0. So each mu_M is updatable, as claimed.

5. Proposition 2, recursion-theorem proof, checked step by step.
- (a) Fixed point. The map from M to a presentation of mu_M is computable (Lemma 1 plus s-m-n), so the recursion theorem yields M* with access to the presentation e*. Verified.
- (b) The search succeeds. If M* never halts, the true I-marginal is delta_0 almost everywhere. A correct U at precision 2^-4 outputs within 1/16 < 1/8 of delta_0 while reading a finite prefix, so the dovetailed search finds sigma. Verified.
- (c) Halting time. n = max(t, |sigma| + 1) + 1 exceeds t and |sigma| + 1, and M* can idle until step n. Verified.
- (d) "The computation is genuine." This paragraph is unnecessary, and the main-text sketch misdescribes the logic when it says U's computation is "unchanged, because it saw too little of M* to tell". There is no counterfactual. U's run on the fixed index e* with oracle prefix sigma is a single deterministic computation, and it is U's actual output for every z in [sigma], whatever it simulates. The claim that nested simulations cover fewer than t steps is true under standard step counting, but nothing depends on it. Recommend deleting the paragraph or recasting it [P].
- (e) Wrongness on a set of positive measure. [sigma] contains whole intervals of E_n, and their central halves have positive Lebesgue measure. P_Y has density (1 - w) + w f_n >= 1 - w > 0, so this set has positive P_Y-measure. On a two-point space with d(0,1) = 1, the Prokhorov distance from delta_0 to (1-p, p) is p. So the true marginal is at distance at least 2/3, and an output m with d(m, delta_0) < 1/8 is off by more than 1/16. This contradicts correctness. Verified, modulo point 1.
- (f) U is supposed to output posteriors over H = (I, Z), but the proof speaks of "a measure m on I". Say that one takes the I-marginal; projection is 1-Lipschitz, so Prokhorov distances do not increase [P].
- Overall: correct once point 1 is repaired.

6. [S] The novelty of Proposition 2 is not located against prior work.
- Mathematically, the result shows that the conditioning map is not uniformly computable from a Prokhorov presentation, even on measures that have densities. That follows from the non-uniform computability of densities from absolutely continuous computable measures, and from the weak discontinuity of conditioning.
- The paper says "the mathematics is elementary" but cites no source for these uniformity facts. I could not check whether AFR or the Hoyrup and Rojas line of work states such a non-uniformity result explicitly.
- Fix: cite or discuss the known non-uniformity facts, and present Proposition 2 as a clean instance rather than as a new phenomenon.

7. Proposition 3(a): verified, with the citation partly verified.
- The ratio-of-integrals argument is correct for bounded computable, hence continuous, densities given the bound.
- The denominator p(y) is positive P_Y-almost everywhere, since P_Y({p = 0}) = integral of p over {p = 0} = 0. The ratio is then computable relative to y.
- AFR's independent-noise result exists and states this. The abstract mentions noise with a "sufficiently smooth bounded density". Search excerpts of the arXiv/JACM-era text name it Corollary 9.7, following from Corollary 9.6. The LICS 2011 version calls it Corollary 36.
- So "Corollaries 9.6 and 9.7" matches the arXiv numbering. I could not confirm that the JACM print numbering is the same, so "in the journal numbering" is unverified. Fix: cite the arXiv version, or confirm against JACM.

8. [S] Proposition 3(b) and claim N4 overreach.
- (i) Atoms. Proposition 3(b) is proved only for mu_M, using "Z has no atoms". But N4 asserts that interval reports give a single correct procedure "whatever its priors over hypotheses". That is false as stated. For a computable prior with an atom at a rational endpoint, mu(Z in [a, b]) is only upper semicomputable, and it can be noncomputable, since an atom's mass can be any right-c.e. real. Lemma 3 covers only the format L and gives no support here.
  Fix: restrict the interval format to intervals with null boundary or open intervals, or to atomless priors. Or randomise the endpoints.
- (ii) The report mechanism. Ratio conditionalization on the event {Z in J} equals Kolmogorov conditioning on the report "J" only if the process generating J is ignorable: a fixed partition, or coarsening at random in the sense of Heitjan and Rubin (1991). The paper leaves the report process unspecified ("a rational interval J containing Z"). The Section 6 "Finite precision" reply, about intervals received from an approximation stream, needs the same condition.
  Fix: state the coarsening condition and model it.

9. [S] F4 misplaces its example.
- F2 is stated for J_ex, defined as "priors over hypotheses given as measures, with exact point reports".
- F4's example is a joint law with Gaussian noise, given as a joint measure, said to fall "in a format of the first kind". That state is not in J_ex.
- Fix: define a general joint-measure format J containing J_ex. Note that J contains the family mu_M with exact reports, so the argument of Proposition 2 applies to J. Then run F2 to F5 with J. As written, the argument from F1 to F5 is not valid.

10. [S] The "wrong object" thesis is in tension with Section 5.3.
- The abstract, Section 1 and Section 7 say that restricting priors "cannot be the general repair".
- Section 5.3 concedes that exact reports become followable if the prior gives Z a presented bounded density given the other hypotheses. That is a restriction on priors, and on how they are presented.
- So Proposition 2 refutes only one version of the natural response, namely restricting to priors whose conditionals are computable one by one. It does not refute restrictions on the format of priors.
- Fix: state the thesis as a disjunction. Uniformity needs slack, either in the channel or in a density-presented prior. Then argue the preference for the channel (Section 5.3) as a separate and weaker claim.

11. [S] The Kripke citation in Section 4.2 ("Finitude") cuts against the paper.
- The paper cites Kripke (1982) for finitude and then answers with a competence/performance distinction ("given unlimited time and memory").
- Kripke's sceptic explicitly argues that appeals to idealised dispositions or competence are circular or empty when they are used to fix which rule is followed.
- The use here is defensible, because FOLLOW concerns whether a procedure exists rather than which rule is meant. But the paper needs to say that and engage the objection, not cite Kripke as if he supported the move.

12. Lemma 3: plausible, with one overstatement.
- The finite-mixture clause holds: adjoin the index and take the maximum bound. The product-of-likelihoods clause holds.
- "Closed under countable mixtures only with a uniform bound": a uniform bound is sufficient, but "only" claims necessity, which is not shown. Say "given a uniform bound" [P].
- The joint-density clause needs the density to be computable, hence continuous, together with its bound, and the integration to run over a finite reference measure on the hypothesis side. In the noise-scale application the reference on s is Lebesgue measure on (0,1), and y is not integrated. Say so.

13. Section 5.4, the noise scale: verified.
- The product of the phi_s(y_i - h) is at most (2 pi)^(-n/2) s^(-n).
- The supremum of e^(-1/s) s^(-n) over 0 < s < 1 is (n/e)^n, attained at s = 1/n, which lies in (0,1) for n >= 2. For n = 1 the function is increasing on (0,1), so the supremum is e^-1, not attained. The bound still holds.
- The function extends continuously by 0 at s = 0. The prior e^(-1/s) is normalisable, and every interval (0, d) has positive mass.
- For pi(s) = 2s: with one reading the density is at most 2(2 pi)^(-1/2), so bounded. With two readings, at y1 = y2 = h the density is 1/(pi s), so unbounded. Verified.
- Caveats [P]. The symbol pi denotes both the prior and the constant. "The tail matters" should say behaviour near s = 0. Unboundedness only means the sufficient condition fails; it does not show the posterior is noncomputable, and the text should not suggest otherwise.

14. AFR content claims.
- (a) "No version computable on a set of measure one" (Section 1). Plausible but unverified in full text. AFR's main theorem gives computable X and Y with noncomputable P[X|Y], and their framework uses computability on P_Y-measure-one sets.
- (b) "In one of AFR's constructions the exact conditional distribution is discontinuous on a set of measure one" (Section 5.4). Verified, and understated: AFR Proposition 5.1 states that every version is discontinuous everywhere on every measure-one set.
- (c) "Cannot in general be approximated uniformly by shrinking the noise." Verified from a search excerpt of AFR's remark after the noise corollary: one cannot computably tell how little noise gives a given accuracy.
- (d) "AFR already observe that independent computable noise with a bounded density makes conditioning computable." Verified.

15. Appendix B: verified, with presentational gaps.
- Both components have Y-marginal B_Y, so the posterior on I' is the constant (1 - w, w).
- If M never halts, the kernel is the constant delta_0 x nu.
- If M halts, a computable version restricted to the clopen set {I' = 1} and renormalised by the known value w would give a computable version of B[X|Y], contradicting AFR. So the updatable indices form the complement of the halting set, which is co-c.e. and not c.e.
- The Gödel step is valid under the stated hypotheses: T must prove "if M halts then P_M is not updatable", and must prove that "M_T never halts" is equivalent to Con(T). Gödel II holds for consistent, computably axiomatised theories that interpret Q.
- Gaps [P]:
  - "commits" is undefined; define it as halting with a flag.
  - "proves the relevant facts" requires T strong enough to formalise AFR's theorem. Name a candidate, for example ZFC.
  - nu's space should be stated.

16. Meehan and Zhang gloss (Section 6, "The Dutch book"): plausible but unverified.
- Their paper concerns plans that give posterior zero to the evidence learned (improper versions), and proposes Kolmogorov-Blackwell conditionalization.
- Propriety is a pointwise property. A procedure that is correct only almost everywhere does not fix the version on null sets.
- Also, the posterior is over H only, so propriety with respect to Y is not even represented.
- Fix: argue that a proper version is selected, or weaken the claim. The author's own hedge "as I understand it" signals the gap.

17. Rescorla claims: verified. Rescorla (2018) proves Dutch book and converse Dutch book theorems. Rescorla (2025) extends them to scenarios in which the conditioning proposition may be false.

18. Huttegger, Walsh and Zaffora Blando: verified bibliographically ("Bayesian convergence for computably bounded agents", PPR 112(1): 307-324, as listed by Crossref). Their advocacy of computable measures as a framework for bounded reasoners is confirmed by the abstract. That they "propose computable probability theory as a framework" is a fair gloss.

19. Lopez-Wild 2026: verified. "Computable Bayesian Epistemology", Philosophy of Science, doi 10.1017/psa.2026.10273. However, Section 1 attributes to it the view that computability considerations "constrain priors". Its headline result is that computable probability measures are countably additive. That is a constraint on credences, so the gloss is acceptable, though thin.

Bibliographic checks
- AFR 2011, LICS pp. 107-116: verified.
- AFR 2019, JACM 66(3), Article 23, pp. 1-40, doi 10.1145/3321699: verified.
- Freer and Roy 2010, AISTATS, PMLR 9: 233-240: verified.
- Meehan and Zhang 2022, RSL 15(3): 722-757: verified (online 2020).
- Rescorla 2018, RSL 11(4): 705-735: verified.
- Rescorla 2025, RSL 18(1): 186-, doi 10.1017/S1755020323000345: issue and start page verified (online 31 October 2023). The end page is missing [P].
- Mahtani 2024, OUP: verified.
- Huttegger, Walsh and Zaffora Blando 2025, PPR 112(1): 307-324: verified via Crossref listing.
- Kolmogorov 1933 (Springer), Weihrauch 2000 (Springer), Kripke 1982 (Harvard), Hacking 1967 (Philosophy of Science 34(4): 311-325), Garber 1983 (Minnesota Studies 10, 99-131): all match standard records; not searched individually.
- Missing reference: Heitjan and Rubin (1991) on coarsening at random, needed for point 8.

Verdict: major revision. The core mathematics is sound and cleanly presented. The repairs to the proof of Proposition 2 (point 1) and Lemma 1 (point 2) are routine. But the interval-format claim in N4 is false for general priors, F4 is invalid as written, and the headline thesis is overstated given Section 5.3. These would change the paper's claims.

Scores: originality 5, correctness 6, importance 5.
