# Round 3: role B (defender) on draft v4

Report reproduced verbatim from the subagent's hand-back.

Referee report on "Following Conditionalization: Computable Agents and Inexact Evidence"

Summary of the submission. The paper builds a uniformly computable family of priors mu_M, each a mixture of a uniform law on Z and a law with tent density f_n, with the mixing weight 2^-n set by the halting time of M. Proposition 2 says that each member can be updated computably on an exact report of Z, but no single procedure can update them all. Proposition 3 says that one procedure updates them all when the report is noisy with a presented bounded density, or when it is a rational interval. From this, and a uniformity principle about rule-following (FOLLOW), the paper concludes three things: conditionalization is followable only relative to a format; exactness of evidence, not the prior, is the obstacle; and an open-ended computable learner must model continuous evidence as inexact.

I write as a defender of orthodox Bayesianism: Kolmogorov conditionalization on exact evidence, and ideal norms that bounded agents need not be able to meet. The mathematics is mostly sound. My main objection is that the headline thesis ("exactness, not the prior, is the obstacle") does not follow from the propositions, and is contradicted by the paper's own Section 5.3.

Checks of the mathematics

I checked these and found them correct:
- E_n is a union of 2^(n-1) intervals of length 2^(-2n), with total length 2^(-(n+1)).
- Each tent has mass 2^(-(n-1)), so f_n integrates to 1. Its peak height is 2^(n+2), so f_n is at least 2^(n+1) on the central halves.
- The posterior bound of at least 2/3 holds, and the appendix's use of 1 in place of (1 - w) in the denominator is legitimate.
- Lemma 1's error bound holds: w_M is at most 2^(-(k+1)) if M has not halted by step k.
- The choice n = max(t, |sigma|+1) + 1 guarantees n - 1 is at least |sigma| + 1, so the digits in positions n to 2n are free inside [sigma].
- In Section 5.4, sup over s of e^(-1/s) s^(-n) is (n/e)^n, attained at s = 1/n. The prior 2s gives a bounded joint density for one reading and not for two.
- Appendix B's Goedel step is valid: T proving that P_{M_T} is updatable, together with the facts T is assumed to prove, would give Con(T).

The substantive objections below are about what these results show, not about whether they hold.

Points

1. [S] The central contrast confounds exactness with presentation of a density bound. Section 3.3 says: "The priors are the same in both, and they are presented in the same way. What changes is only whether the evidence is modelled as an exact point." This is false.
- In format L (F3, Lemma 3), each source comes with "a presented bounded computable likelihood density". The procedure gets a density and its bound as extra input.
- In J_ex (F2), the prior comes only as a bare measure, with no density for the reported variable.
- Proposition 2 fails for exactly that reason. Every mu_M has a bounded density for Z given I, but the bound 2^(n+2) is not presented uniformly, because n encodes halting.
- Section 5.3 concedes the point: "An exact report of Z can be followed if the prior gives Z a presented bounded density given the other hypotheses. The family {mu_M} violates this only because its densities are not presented uniformly."
- So the fair comparison is J_ex plus a presented density bound against L. Both have one uniform procedure, and exact evidence is no obstacle in either.

What Propositions 2 and 3 actually show is AFR's own lesson: uniform conditioning needs dominated structure with a known bound. Thesis 1, F2/F3 as a contrast "of exactness", N3, and the Conclusion's "the format it needs is one in which continuous evidence is inexact" should all be withdrawn or restated as "the format must present a dominating density with its bound". Under that restatement exact evidence is allowed.

2. [S] The reply to the labelling objection (Section 5.3) fails, and the asymmetry it claims does not exist.
- The paper says the channel is the better place for slack because Z is a "target of learning" whose prior should be unrestricted.
- But in the paper's own exact case, the posterior over Z is the trivial point mass at z. The only nontrivial target is I.
- Relabel Z as the reading and I as the hypothesis. Then "prior over (I, Z) with a presented bounded density of Z given I" is literally an instance of format L.
- The restriction in L (the reading is not a deterministic function of the hypotheses) and the restriction in the density-presented exact format (the reported variable is not a deterministic function of the other hypotheses) are the same constraint on the joint law. Which variable carries the name "hypothesis" is a matter of labelling.

The paper says "the joint credence is constrained either way". That concedes the point, since F4 makes the joint credal state the object of evaluation. Fix: drop the claim that inexactness in the channel differs in kind from regularity in the prior, or give a non-verbal criterion for which variables are "targets".

3. [S] "Any prior" in Lemma 3 and N1/N4 hides an equally strong restriction on channel models.
- N1 lets the learner adopt any computable prior over hypotheses. N4 then restricts its models of new sources to presented bounded continuous likelihoods.
- That excludes standard noise models with unbounded densities: a Gamma with shape below 1, chi-square with one degree of freedom, and scale mixtures like the 2s case of Section 5.4.
- It also excludes deterministic sensors, and channels whose bound is not known in advance.
- An "open-ended" learner that may not adopt these channel models is no more open-ended than one that may not adopt priors without presented densities.

N5's "can follow if inexact, cannot if exact" therefore compares an unrestricted exact format with a restricted inexact one. Fix: compare formats with matched restrictions, or drop "open-ended".

4. [S] The interval format is discrete evidence, which the paper says is out of scope. Proposition 3(b) conditions on "Z in J" for a rational interval J. The set of rational intervals is countable, so the report variable is discrete and ratio conditionalization applies. The paper itself says (Section 1, Section 6 "Digital evidence") that discrete evidence is untouched. So one of its two "inexact formats" is not a way of conditioning on continuous evidence at all: it changes the subject.

There is a further problem from the orthodox standpoint. Conditioning on the event "Z in J" is correct only if the reporting protocol is non-informative (coarsening at random, Heitjan and Rubin 1991). The correct update conditions on the report R = J, and that requires a model of P(R = J | H). Fix: recast (b) as discrete conditionalization on a modelled report, and state the coarsening-at-random assumption.

5. [S] N4 says "whatever its priors" for interval reports, which is false as stated. Proposition 3(b) relies on Z having no atoms, so that the boundary of J is null and mu(J) is computable. Lemma 3 says "Every computable prior over hypotheses appears in L", and N4 extends the claim to interval formats "whatever its priors over hypotheses". For a computable prior with an atom at an endpoint of J, mu(J) is in general only semi-computable, so ratio conditionalization is not uniformly computable. If the prior gives J probability zero, the ratio is undefined. Fix: restrict to priors that are atomless on reported variables, or to intervals chosen to avoid atoms (only almost all endpoints work, and finding them is itself non-uniform).

6. [S] The "Finite precision" reply misstates how the exact rule relates to bounded agents. The paper claims "exact conditionalization is not even the rule they approximate in a uniform way."
- By Levy's upward theorem (martingale convergence), P(H | Y in J_k), for the nested dyadic intervals J_k shrinking to y, converges to a version of P(H | Y = y) for P_Y-almost every y.
- So the interval learner's computable posteriors converge almost surely to the Kolmogorov posterior. The exact kernel is a limit of computable approximations; only the rate is noncomputable.
- That is precisely how an orthodox Bayesian says an ideal norm governs bounded agents: they approximate it in the limit.

The qualifier "in a uniform way" makes the paper's statement true only in a weak sense that does not support its conclusion. Fix: acknowledge the almost-sure convergence, and say that only rates of convergence fail.

7. [S] FOLLOW is too strong, and it does the deciding work. The paper admits (Section 4.1) that "all the weight rests on F1".
- FOLLOW requires one procedure correct on every updatable presentation in the format, with no restriction on how presentations are given.
- By that standard, most familiar operations are not "followed" on their natural formats. Examples are equality testing on reals, or evaluating a function given as a program.
- The bad-format reply concedes this and turns it into the thesis. But then the thesis is a corollary of the platitude, already in Weihrauch, that computability depends on representation. It is not a finding about conditionalization or about evidence.
- The "Capacity" reply says FOLLOW ranks formats, not agents. That severs the link to rationality: no norm on the agent follows.

Fix: either argue that the agent's format is fixed by something other than the presentation chosen (point 1 shows it is not fixed by the evidence), or restate the conclusion as a claim about presentations.

8. [S] The defence against the Dutch book (Section 6) begs the question. The paper says the inexact learner "conditionalizes its own prior, channel model included". That holds only because the learner's evidence variable has been redefined as Y.
- If the agent in fact learns Z = z exactly (a register value, or a mathematically fixed quantity), then updating as though it received Z plus noise is conditioning on a weaker proposition than its total evidence.
- Rescorla's 2018 theorem then applies to the actual learning situation, since the update is not Kolmogorov conditionalization of the prior on what was learned.
- The paper's own concession, "If its evidence is in fact exact, its credences are inaccurate in a respect it cannot represent", is a violation of total evidence, not merely a "cost in accuracy".

On Meehan and Zhang (2022), the paper's reading is flagged "as I understand it". The criterion should be stated precisely. It concerns the agent's certainty about the evidence it received, and it is not clear how that criterion applies once the evidence proposition has been swapped. Fix: argue that the agent's evidence is constitutively what it models, or concede that exact learners who adopt the inexact model depart from total evidence.

9. [S] The claim that the noise scale is "substantive" (Section 5.4) rests on unverified attributions to AFR. The paper writes: "In one of AFR's constructions the exact conditional distribution is discontinuous on a set of measure one. AFR also remark that conditional distributions given continuous observations cannot in general be approximated uniformly by shrinking the noise."
- I could confirm that AFR have a section on discontinuous conditional distributions and a section on noisy observations (Section 9.3 in the arXiv version).
- I could not confirm the remark about shrinking noise. In particular, I could not confirm that it is stated as a remark rather than inferred.
- Even granted, failure of uniform approximation is compatible with pointwise almost-sure convergence as the noise goes to zero (point 6). So it does not show that the noise model is "not an approximation to an exact target".

Fix: quote AFR with exact location and distinguish uniform from almost-sure approximation.

10. [S] The citation "AFR 2019, Corollaries 9.6 and 9.7 in the journal numbering" is doubtful. The arXiv version I could access through search snippets states the noisy-observation result as Corollary 36 in Section 9.3. Its abstract says computability holds when the noise has "sufficiently smooth bounded density". The submission says "bounded computable density". The smoothness condition should be checked against AFR's actual hypothesis, since Proposition 3(a) rests on it. I could not open the JACM text (arxiv.org is not reachable from this session), so the numbering needs verifying. If AFR require more than boundedness and computability (for instance a Lipschitz condition), the scope of L shrinks accordingly.

11. [S] The novelty claim for Proposition 2 is unsupported. The paper says AFR already give the dominated-case positive result. AFR also study whether conditioning is computable as an operator on restricted classes, and pose the question for continuous conditional distributions. A uniform non-computability result for a halting-indexed family with computable, continuous individual conditionals is a standard recursion-theorem diagonalisation, and may already appear in AFR or in the computable-analysis literature on conditioning (for example, work by Hoyrup and Rojas). The paper should survey this explicitly before claiming that Proposition 2 refutes the "natural response".

12. [S] The "natural response" is mis-described, so the target is a straw man. Section 1 defines it as requiring "a prior whose conditional distributions are computable". Proposition 2 shows that this per-prior condition does not yield uniformity. But a careful defender of prior constraints would require a uniformly presented restriction: a prior given together with a dominating density and its bound. That is exactly what Section 5.3 shows works for exact evidence. The paper's own Section 4.2 ("The natural response done properly") concedes this. Then "aimed at the wrong object" amounts to "aimed at the right object but stated imprecisely". Fix: tone down the thesis.

13. [S] The proof of Proposition 2 has a gap: oracle names versus binary digits. Z is "identified with its binary expansion", and sigma is treated as a binary prefix whose cylinder [sigma] contains whole intervals of E_n. In computable analysis (Weihrauch 2000, which the paper cites), the binary representation of the reals is not admissible. An oracle "stream of approximations", as in Section 2, gives a Cauchy name, and a finite prefix of a Cauchy name determines a rational ball, not a dyadic cylinder. Given the paper's emphasis on representation, this matters.

The proof can be repaired:
- choose n large enough relative to the ball's radius that the ball contains a full dyadic cylinder of length about 2^(-|sigma|-2);
- note that Cauchy-to-binary conversion is computable on non-dyadic reals, a measure-one set.

The appendix should do this explicitly.

14. [S] "The tail matters" (Section 5.4) shows less than claimed. The prior 2s only shows that the paper's sufficient condition (a bounded joint density) fails after two readings. It does not show that updating fails or is non-uniform: the s-marginalised likelihood may still be bounded and computable away from a null set. Fix: say "our sufficient condition fails", or give a non-computability result.

15. [S] The "no floor" claim is technically true but philosophically weak. Under pi(s) proportional to e^(-1/s), the prior probability that s is below d is of order e^(-1/d). The likelihood bound also grows as (n/e)^n with the number of readings, so the procedure needs n as input. The prior is, in effect, a soft floor. This should be acknowledged.

16. [P] Appendix B is called "not needed for the main argument" but takes up the abstract-level space of Section 3.3. In Appendix B, I' is introduced and nu is used without explanation of the variables they range over. The phrase "restricting a computable version to I' = 1" should be spelled out: it is conditioning on I' = 1, an event of positive probability w_M, with a computable value.

17. [P] Section 2 defines correctness "on a set of observations of measure one", but does not say which measure (P_Y for that presentation). It also does not say whether the procedure must be correct for every name of each such observation.

18. [P] The reference for Rescorla (2025) has an open-ended page range ("186-"). It should be completed (the article is about 27 pages, starting at 186).

19. [P] The paper lists Huttegger, Walsh and Zaffora Blando (2025) as PPR 112(1): 307-324, and I could confirm it. However, characterising that paper as "proposing computable probability theory as a framework for computationally bounded Bayesians" overstates it. It is a paper on convergence theorems that uses that framework.

20. [P] Lopez-Wild (2026) is cited in support of computability constraints on priors. Its main result as reported (computable measures are countably additive) fits that use, but the specific connection should be stated.

21. [P] Marr's computational and algorithmic levels are invoked without a citation (Marr 1982).

Bibliographic checks. I could confirm the following:
- AFR 2011 is in LICS.
- AFR 2019 is J. ACM 66(3), 23:1-23:40.
- Meehan and Zhang is RSL 15(3): 722-757 (2022).
- Rescorla 2025 is RSL 18(1), starting at 186, doi 10.1017/S1755020323000345, a non-factive Dutch book theorem.
- Huttegger, Walsh and Zaffora Blando is PPR 112(1): 307-324.
- Lopez-Wild has doi 10.1017/psa.2026.10273.

I did not check these by search, but they match standard records:
- Rescorla 2018 (RSL 11(4): 705-735)
- Hacking 1967
- Garber 1983
- Kripke 1982
- Mahtani 2024
- Weihrauch 2000
- Kolmogorov 1933

The only items I could not confirm are the AFR corollary numbering and the remark about shrinking noise (points 9 and 10).

Overall assessment. The construction is neat and the proofs are essentially correct, apart from the representation gap in point 13. The philosophical conclusion, though, is not supported.
- Propositions 2 and 3 differ in whether a dominating density with a known bound is presented, not in whether evidence is exact. Section 5.3 concedes that exact reports become uniformly updatable once such a density is presented for the prior.
- The interval format is discrete evidence, which the paper excludes from scope.
- The finite-precision reply ignores the almost-sure convergence of interval posteriors to the Kolmogorov posterior.
- The Dutch book reply works only by redefining the agent's evidence.

What remains is a correct and modest observation: uniform conditioning needs presented dominated structure. That is close to AFR's own positive result, and it is compatible with orthodox Bayesianism as an ideal norm that bounded agents approximate in the limit.

Verdict: major revision, bordering on reject. The thesis needs restating as a claim about presented domination rather than about exactness of evidence, and points 1 to 8 need answers.

Scores:
- Originality: 5
- Correctness: 5 (the mathematics is mostly correct; the philosophical inferences from it are not)
- Importance: 4

Sources consulted:
- https://philsci-archive.pitt.edu/27049
- https://philsci-archive.pitt.edu/23862/1/Computable_Bayesian_Epistemology%20(2).pdf
- https://www.citedrive.com/en/discovery/computable-bayesian-epistemology/
- https://pdf.arxiv.org/pdf/1005.3014
- https://dblp.org/rec/journals/rsl/MeehanZ22.html
- https://www.ebsco.com/articles/religion-and-philosophy/c34e5863-ad7f-5e5c-9339-8ad7cbf81517/non-factive-kolmogorov-conditionalization
- https://cambridge.org/core/journals/review-of-symbolic-logic/article/nonfactive-kolmogorov-conditionalization/43143C279BB1BF896E4AC48C0F14BF8A

Note: arxiv.org is blocked in this session's network settings, so I could not read the AFR full text directly.
