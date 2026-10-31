# Round 5: role C (technical) on draft v6

Report reproduced verbatim from the subagent's hand-back.

Technical and citation check of "Following Conditionalization: Computability Constrains Spaces of Credences, Not Credences" (submission_r5.md)

The mathematics is essentially sound. I checked the appendix proof line by line and found no error. Proposition 4's sketch has one small gap, at the edges of [0,1], that is easy to fix. Two statements about how the family relates to the regularity class are worded inaccurately. One quantifier issue in the framework should be addressed. Every citation I could check is accurate. arxiv.org and ar5iv were blocked in this session (they must be allowed in the session's network settings if you want them), so AFR's section numbering stays unverified.

A. Construction and Lemma 1

1. E_n and the comb f_n (Section 3.1). Verified. Positions n to 2n are n+1 digits. Digits 1 to n-1 are free, which gives 2^{n-1} intervals of length 2^{-2n}. Tents of mass 2^{-(n-1)} sum to 1. The peak is 2m/w = 2 x 2^{-(n-1)} x 2^{2n} = 2^{n+2}. On the central half the height is at least half the peak, 2^{n+1}. Neighbouring intervals sit 2^{-(n-1)} apart, so the tents are disjoint and f_n is continuous. f_n and B_n are uniformly computable in n.

2. Lemma 1. Verified. If M has not halted by step k, then either it never halts or n = m+2 >= k+3, so the omitted weight is at most 2^{-k-3}. TV(mu_M, A) <= 2^{-n}, and Prokhorov distance is at most TV. 2^{-k-1} + 2^{-k-3} < 2^{-k}. The "equivalent" countable-mixture form is also verified: each p_n(M) is decidable, and 1 - sum p_n(M) is a computable real, with tail at most 2^{-N+1}.

3. Posterior formula (Section 3.2). Verified. P_Z has density at least 1 - 2^{-n} > 0 everywhere, so the continuous version is the unique continuous one. It is computable for each M (each prior separately, not uniformly).

B. Proposition 2 and the appendix (step by step)

4. Recursion theorem and e*. Verified. By Lemma 1, a presentation of mu_{M*} is obtained uniformly from M*'s index. Self-reference in the search is harmless. When M* simulates U querying e* at precision k, it simulates its own first k steps, and that is a bounded computation. The pair found is a genuine halting computation on the actual oracle.

5. Decidability of "every point of K has a name extending tau". Verified. This means the closed rational interval K lies inside the finitely many open balls (q_i - 2^{-i}, q_i + 2^{-i}). That is a finite check of strict rational inequalities.

6. "The search succeeds". Verified. Choose a name of z with |q_i - z| < 2^{-i-1}. For i <= |tau| and |x - z| < 2^{-|tau|-1}: |q_i - x| < 2^{-i-1} + 2^{-|tau|-1} <= 2^{-i}, so K qualifies. Output at precision 1/16 within 1/16 of delta_0 meets the 1/8 test. Using z in (0,1) from the measure-one correctness set is legitimate.

7. Choice of n. Verified. An interval of width r >= 2 x 2^{-(n-1)} contains an aligned dyadic interval of length 2^{-(n-1)}. That interval fixes digits 1 to n-1 and contains exactly one E_n interval, the one with digits n to 2n equal to 0.

8. The 2/3 bound. Verified. The numerator 2^{-n} x 2^{n+1} = 2. The denominator (1 - 2^{-n}) + 2 < 3, so the ratio is greater than 2/3.

9. Closing inequality. Verified, but the wording could be tighter.
- m is more than 2/3 - 1/8 from the true posterior.
- U's limit output is within 1/16 of m.
- So the limit differs from the truth by more than 2/3 - 1/8 - 1/16 > 0.
- The text says "wrong by more than 2/3 - 1/8 > 1/16", which compresses this. Stating the limit-versus-approximation step explicitly would help.
- Using P_Z >= (1 - 2^{-n}) Leb: verified.
- Every version agrees a.e. with the continuous posterior on that positive-measure set: verified.

10. Main-text sketch of Proposition 2. Verified. It agrees with the appendix (1/8, and 2^{-(n-1)} < r/2).

11. [S] Input format is unstated. Proposition 2 is proved only for procedures that receive the bare measure presentation. Yet (G2) and Section 4.2 rely on agents reaching the family by operation (X), which hands the agent mixture data: the component presentations of A and B_n and the weights p_n(M). The argument does extend. The mixture representation is uniform in M, and even with the component densities f_n the sum sum p_n f_n(z) has no computable tail bound, because the terms reach about 4. But this extension is neither stated nor proved. Fix: state Proposition 2 for any representation computable uniformly in M, and note this explicitly. Without it, (G2)'s claim that "(X) does" is not covered by the stated proposition.

C. Proposition 3

12. Proposition 3(a). Plausible, with minor gaps.
- The formula is correct.
- Integrals of bounded computable functions with a known bound against a computable measure are computable. Here q computable in (h,y) makes q(.,y) computable relative to every name of y.
- The denominator is positive P_Y-a.s.: correct.
- The presentation must also guarantee that q rho x lambda is a probability measure.
- lambda being atomless plays no role in computing the posterior.
- The attribution "AFR 2019, Section 9" is unverified, because arxiv.org was blocked. My recollection is that the positive results, covering bounded computable densities and independent noise, are in AFR's final section, so the attribution is plausible. Search snippets confirm that the JACM abstract mentions "independent computable noise with a sufficiently smooth bounded density" and that a Section 9.2 exists.

13. Proposition 3(b). Verified as an instance of (a), with q(h,y) = phi(y - z) and lambda = Lebesgue on R. Note that Y now takes values in R, not [0,1]. The claim is about updating on Y = Z + xi, not on Z. The paper says so, but the abstract's "a model of the evidence source" understates that the evidence has been changed. Attributing the result to AFR's noisy-observation corollary is correct in substance. AFR's abstract speaks of "sufficiently smooth" bounded density; a computable density, being continuous, appears to meet their hypothesis.

D. Proposition 4

14. Boundary bound. Verified. P_Y has density p <= C. The delta-neighbourhood of the two endpoints of B has Lebesgue measure at most 4 delta, so its P-mass is at most 4C delta. This lets one compute P(Y in B) and P(g(H); Y in B) from a Prokhorov presentation, uniformly in C, with y given by a name. For the second quantity, use continuous approximations to the indicator.

15. Lipschitz estimate. Verified, and conservative. The averaging error is at most ||g|| L times the mean of |y' - y| over B, which is ||g|| L eps/2 (and L eps/2 for p).

16. [S] Edge effect. The class lives on H x [0,1]. For y within eps of 0 or 1, the ball B leaves [0,1], where the density is 0. Then P(Y in B)/(2 eps) underestimates p(y), and the stated L eps bounds fail. Fix: from the name of y, first find delta with y in (delta, 1 - delta), which exists for a.e. y, and restrict to eps < delta. Alternatively, use one-sided intervals. This repair is easy, and Proposition 4 then holds.

17. Lower bound and rate. Verified. Compute p(y) with known error until some approximation exceeds its error bound. The ratio error is then computable from C, L and that bound.

18. [P] C is redundant. With rho the H-marginal, q(h,.) integrates to 1 over [0,1] for rho-a.e. h. A function that is L-Lipschitz on [0,1] and has integral 1 satisfies q <= 1 + L/2. So C is implied by L.

19. [S, minor] Wrong quantity for "lies in no single class C_{C,L}". The paper cites the Lipschitz constant of "2^{-n} f_n, which grows like 2^{2n}". The arithmetic is right: the slope is 2^{n+2} / 2^{-2n-1} = 2^{3n+3}, times 2^{-n} gives 2^{2n+3}. But the class is defined by the density q with respect to rho x Leb, where rho is the H-marginal. For halting M that gives q(1,.) = f_n, whose Lipschitz constant grows like 2^{3n}. Its sup 2^{n+2} also breaks every bound C. The conclusion stands, but the justification uses a quantity that is not the one in the definition. Fix: cite f_n, or note that the unnormalised component 2^{-n} f_n is the density with respect to delta-weighted Leb.

20. Class closure (supports G4). Verified, though the paper leaves it implicit. C_{C,L} is closed under finite and countable mixtures. At each h the mixture's q(h,.) is a convex combination of the components' q(h,.), so the bounds survive. An agent confined to C_{C,L} with (A) and (X) therefore stays in the class. The paper should say this, since (G4) needs it.

E. Other technical claims

21. [S, minor] Iterated updating is undefined. FOLLOW quantifies over reachable states, which include posteriors produced by (U). But the framework defines a credal state on H x Y with a single Y, and never says what further observations posterior states face. It also never shows that C_{C,L}-confined agents stay updatable after (U). Fix: specify a sequence of observations, or restrict reachable states to pre-observation states.

22. Section 4.2, kernel storage is not closed under (X). Verified. The mixture posterior is sum w_i p_i(y) kappa_i(y) / sum w_i p_i(y), which needs the marginal densities p_i.

23. Section 4.3, presented data "encodes the halting time". Verified, and in fact understated. Any bound c >= q for mu_M decides whether M halts: run M for about log2(c) steps, and if it has not halted it never will. So the regularity data are not computable from M at all.

24. Section 5, interval conditioning. Verified.
- For a computable measure, the measure of an open rational interval is lower semicomputable and of a closed one upper semicomputable. If the boundary is null, the value is computable.
- With atoms it may not be computable.
- Lévy's upward theorem gives a.s. convergence along the dyadic filtration for each g. With a countable dense family of g, the posteriors converge weakly a.s. to a version of the exact posterior.
- Coarsening at random is correctly credited to Heitjan and Rubin 1991.

25. Section 5, Rescorla's Dutch book. Correct as a description. The theorems target departures, on positive-measure sets, from a regular conditional distribution of the agent's own prior.

26. Characterisation of AFR's theorem (Section 2). Plausible but unverified. AFR do construct computable X and Y whose conditional distribution is not computable, including results on almost-continuous versions. I could not check that the theorem is stated exactly as "not computable on any set of measure one", or which variable is conditioned on which. The paper should cite the theorem number.

27. "Close relative of the non-computability of the Radon-Nikodym operator". Fair. The posterior here is essentially dP(I=1, Z in .)/dP_Z, so Proposition 2 is a non-uniformity result of the same kind. This confirms the author's own admission that the mathematics is not new. The contribution rests on the framing in FOLLOW and (G4). (G4) follows almost by definition once FOLLOW quantifies over reachable states.

F. Citations

28. Verified:
- AFR 2019: JACM 66(3), Article 23, pp. 23:1-40, DOI 10.1145/3321699.
- Hoyrup, Rojas and Weihrauch 2012: Computability 1(1): 3-13, DOI 10.3233/COM-2012-005. It does show the Radon-Nikodym operator is not computable.
- Rescorla 2025: "Non-factive Kolmogorov conditionalization" is in RSL vol. 18 (online 2023) and proves non-factive Dutch book and converse Dutch book theorems. The issue (1) and pages 186-212 are unverified.
- Huttegger, Walsh and Zaffora Blando: "Bayesian convergence for computably bounded agents", PPR 112(1): 307-324, listed as 2025. It concerns convergence to the truth for computable priors, so the description is accurate.
- Lopez-Wild: "Computable Bayesian epistemology", Philosophy of Science, DOI 10.1017/psa.2026.10273 exists. The preprint proves that no computable probability measure is merely finitely additive. The paper's qualifier "on countably generated spaces" should be checked against the published statement.
- Shan and Ramsey: POPL 2017, pp. 130-144.

29. Verified from my own knowledge, without a search:
- AFR 2011, LICS pp. 107-116.
- Rescorla 2018, RSL 11(4): 705-735.
- Hacking 1967, Phil Sci 34(4): 311-325.
- Garber 1983, Minnesota Studies 10: 99-131.
- Heitjan and Rubin 1991, Ann. Statist. 19(4): 2244-2253.
- Kolmogorov 1933 (Springer), Kripke 1982 (Harvard), Marr 1982 (Freeman), Weihrauch 2000 (Springer), Mahtani 2024 (OUP).
- "Regular versions came later": correct.

30. [P] Missing citation. The claim that AFR have their "own results on the discontinuity of conditioning" needs a theorem or section number.

Summary of errors. Nothing is outright false. Things to fix:
- (16) the edge gap in Proposition 4;
- (19) the Lipschitz statement cites the wrong density;
- (11) Proposition 2 is stated only for bare presentations, while (G2) needs mixture-data inputs;
- (21) iterated updating and closure are left unspecified;
- the AFR section and theorem numbers are unverified.

Suggested scores from a technical standpoint: correctness 7, originality 4 (the mathematics is a known-style non-uniformity result, and the novelty is the framing), importance 4. Suggested verdict: minor revision on technical grounds. Whether the philosophical thesis is mostly a matter of definition is the main referee's call.

Sources:
- [AFR, arXiv 1005.3014](https://arxiv.org/abs/1005.3014)
- [Rescorla, Non-factive Kolmogorov conditionalization](https://cambridge.org/core/journals/review-of-symbolic-logic/article/nonfactive-kolmogorov-conditionalization/43143C279BB1BF896E4AC48C0F14BF8A)
- [HWZB, PhilSci 27049](https://philsci-archive.pitt.edu/27049)
- [Lopez-Wild preprint](https://philsci-archive.pitt.edu/23862/1/Computable_Bayesian_Epistemology%20(2).pdf)
- [Lopez-Wild DOI listing](https://www.citedrive.com/en/discovery/computable-bayesian-epistemology/)
- [HRW, DOI 10.3233/COM-2012-005](https://dx.doi.org/10.3233/COM-2012-005)
- [Shan and Ramsey, POPL 2017](https://popl17.sigplan.org/details/POPL-2017-papers/20/Exact-Bayesian-Inference-by-Symbolic-Disintegration)
