# Round 5: role A (specialist) on draft v6

Report reproduced verbatim from the subagent's hand-back.

Referee report on "Following Conditionalization: Computability Constrains Spaces of Credences, Not Credences"

Summary of the submission. The paper separates two readings of Kolmogorov conditionalization: an evaluative ideal, and a rule a computable agent follows. It defines FOLLOW: a single updating procedure must be correct on every reachable state that can be updated, where reachable means reachable by updating (U), adopting (A) and mixing (X). It builds a uniformly computable family mu_M = (1 - 2^-n)A + 2^-n B_n, indexed by the halting time of M. Every member has a continuous, computable posterior on an exact observation of Z. A recursion-theorem diagonal argument (Proposition 2) shows that no single procedure is correct on all members. Propositions 3 and 4 give single procedures when uniform information about regularity is available: a presented density, a bounded noise model, or fixed bound and Lipschitz constants. The philosophical conclusion (G4) is that computability constrains spaces of credal states rather than individual credence functions.

I checked the mathematics line by line. The construction, Lemma 1, the posterior formula and the appendix proof are correct, apart from small slips noted below. The paper is clearly written and honest about its scope. Its weaknesses are philosophical. The central thesis comes close to following from how FOLLOW is defined. The mathematical core is a standard non-uniformity phenomenon. Several claims about the "three routes" are stated more strongly than the propositions support.

Verification of technical claims

1. The construction (Section 3.1) is correct. E_n, the set of z whose binary digits n to 2n are all 0, fixes n+1 digits and leaves digits 1 to n-1 free, so it is 2^(n-1) intervals of length 2^(-2n). Tents of mass 2^-(n-1) on these intervals add up to total mass 1. Peak height is 2 x mass / length = 2^(n+2), and the tent is at least half its peak, 2^(n+1), on the central half of each interval. All as stated.

2. Lemma 1 is correct. If M has not halted within k steps, the omitted weight is 2^-(m+2) <= 2^-(k+3). Prokhorov distance is at most total variation, so the total error is below 2^-k. The countable-mixture description is fine: the weights p_n(M) are uniformly computable and the tail is computably bounded.

3. The posterior formula in Section 3.2 is correct, and for each fixed M it is continuous and computable in z.

4. The appendix proof of Proposition 2 is correct. Each step checks out:
- Every point within 2^(-|tau|-1) of z lies in all the balls named by tau.
- Membership of K in the balls is decidable.
- Since 2^-(n-1) < r/2, K contains a dyadic interval of length 2^-(n-1), and that interval contains an E_n interval starting at its left endpoint.
- The bound 2/(3 - 2^-n) > 2/3 holds.
- The margin 2/3 - 1/8 > 1/16 contradicts correctness at precision 2^-4.
- Positive Lebesgue measure gives positive P_Z measure.

5. The Lipschitz figure is inconsistent. Section 4.1 says the Lipschitz constant of "the I = 1 part, 2^-n f_n" grows like 2^(2n). That is right for the density with respect to counting measure times Lebesgue: 2^-n x 2^(3n+3) = 2^(2n+3). But Proposition 4 defines the density with respect to rho x Leb, with rho the H-marginal, and then q(1, .) = f_n, whose Lipschitz constant is 2^(3n+3) and whose peak is 2^(n+2). The conclusion (no single class C_{C,L} contains the family) holds either way, but the text should use one normalization throughout. See point S5 for why this matters.

6. The description of AFR is accurate. AFR (2011, 2019) give computable random variables with a version of the conditional distribution that is continuous on a measure-one set but no computable version, and the noncomputability holds on every measure-one set. The stronger claim, noncomputability on every set of sufficiently large measure, is in Ackerman, Freer and Roy, "On computability and disintegration" (Mathematical Structures in Computer Science, 2017). That paper is not cited and should be.

7. The pointer "AFR 2019, Section 9" for the dominated-density argument could not be confirmed. The numbering of theorems and sections differs between the arXiv versions and the JACM version: in one draft the dominated-density and noisy-observation results are Corollaries 35 and 36. Cite the result by its theorem or corollary number in the JACM version. Also note that AFR's noisy-observation result is stated for a bounded computable noise density, and their abstract speaks of a "sufficiently smooth bounded density". Proposition 3(b) should state exactly the hypotheses AFR use.

8. Bibliography. I confirmed the following entries:
- Rescorla 2018 (RSL 11(4): 705-735).
- Rescorla 2025, "Non-factive Kolmogorov conditionalization" (RSL 18(1); online since 2023). The paper's description of it is accurate.
- Lopez-Wild, "Computable Bayesian epistemology" (Philosophy of Science, doi 10.1017/psa.2026.10273). The paper's description is accurate: on countably generated spaces there are no computable merely finitely additive probability measures.
- Huttegger, Walsh and Zaffora Blando, "Bayesian convergence for computably bounded agents" (PPR 112(1): 307-324). The issue is listed as 2025 online; volume 112 may be dated 2026 in print, so check the year.
- AFR 2019 (JACM 66(3), Article 23, pp. 1-40).

The other entries match my knowledge: Hoyrup, Rojas and Weihrauch 2012 (Computability 1(1): 3-13), Heitjan and Rubin 1991, Hacking 1967, Garber 1983, Shan and Ramsey POPL 2017, Kolmogorov 1933, Kripke 1982, Marr 1982, Weihrauch 2000 and Mahtani 2024. The historical remark that regular conditional distributions came after Kolmogorov 1933 is correct.

Points

[S1] The thesis comes close to following from the definition of FOLLOW. (Sections 2 and 4.2: "FOLLOW ... a single procedure is correct on every reachable state", and "G4 is the thesis. It needs FOLLOW, which quantifies over reachable states, and the propositions.")
- What is wrong: once FOLLOW quantifies over reachable states, it is true by definition that following the rule depends on the reachable space. The only mathematical content G4 adds is that the uniform requirement is strictly stronger than the per-prior requirement. That a family of individually computable functions need not be uniformly computable is a basic fact of computable analysis. Proposition 2 is a nice instance of it, but it cannot carry a new epistemological thesis by itself. FOLLOW is motivated in one paragraph. That paragraph appeals to "the rule is applied to whatever states the agent's operations produce", which is the very point at issue.
- What would fix it: give independent support for FOLLOW from the rule-following literature: following versus conforming, the role of a single general procedure, and the analogy with adding machines treated more carefully. Engage at least one competitor that a defender of the per-prior response would offer, for example "the agent follows conditionalization if, for each state it actually holds, it runs a procedure correct for that state". Then show that this competitor fails for principled reasons, not merely that it differs from FOLLOW.

[S2] FOLLOW makes the procedure's input a bare measure presentation, but an agent that reaches mu_M by (X) built mu_M itself. (Sections 3.2, 4.2, "Why the operations matter".)
- What is wrong: the obvious objection is that a mixing agent knows its components and weights, and that FOLLOW should let the procedure use that structured representation. As far as I can see, the result survives. Given the components B_n with their densities f_n (uniformly computable, with bounds 2^(n+2)) and the weight sequence p(M), a procedure still reads only a finite prefix of the weights. That prefix cannot rule out a later halting time n, and z may lie in E_n. The same diagonal goes through on the structured representation. But the paper neither states nor proves this. Its only remark, that a stored kernel is not closed under (X), addresses a different format.
- What would fix it: state and prove a version of Proposition 2 in which the procedure also receives the mixture structure (component presentations, densities, per-component bounds, weights). This would make the result robust and answer the most natural reply.

[S3] The role of (X) is overstated, and so is the claim that "the family arises by operation (X) alone" (Section 3.2).
- What is wrong: (X) mixes "states it can hold", so A and every B_n must already be reachable, through the initial state or through (A). The paper does not say how B_n (I = 1 for certain, with a comb density) becomes reachable. Moreover, each class C_{C,L} is closed under countable mixtures: the density of a mixture with respect to the mixture's marginal is pointwise a convex combination. So mixing is harmless. The failure comes from the reachable space containing components with unbounded regularity constants, combined with a representation that hides the index. Countable mixtures are not essential either. The family {A} together with {(1 - 2^-n)A + 2^-n B_n : n}, given by Lemma-1-style presentations, already defeats every procedure by a continuity argument; see P1.
- What would fix it: say exactly which components must be reachable. Note that C_{C,L} is closed under (X). Recast the diagnosis: the property that blocks a single procedure is unbounded regularity across the reachable space, and the operations matter only insofar as they produce it.

[S4] The finite-precision objection (Section 5) is set aside too quickly, and it threatens the "followed reading" of exact conditionalization. ("That is discrete evidence ... it replaces Kolmogorov conditionalization rather than following it.")
- What is wrong: a computable agent's updating procedure, as defined in Section 2, only ever reads finite segments of a name, that is, rational intervals. Ratio conditionalization on the intervals received is a single procedure that is correct, uniformly, for every prior whose interval boundaries are null. That includes the whole mu_M family, which has no atoms in Z. So a defender of the per-prior response can say that a computable agent never follows exact Kolmogorov conditionalization on a real in any case, and that the rule it does follow is uniform. The paper needs to explain why the followed reading of exact conditionalization is a coherent target at all, given its own model of input.
- Two further technical issues. First, Levy's upward theorem needs a fixed filtration. The intervals of a Cauchy name are neither nested nor centred, so convergence of the agent's actual interval posteriors needs a differentiation theorem (Besicovitch for centred balls; non-centred intervals need more), not Levy. Second, on the mu_M family the rate of convergence depends on the halting time and is therefore not computable, so "approached almost surely by followable updates" (Conclusion) never yields a certified approximation.
- What would fix it: engage the objection head on, distinguish the dyadic-filtration case from the agent's actual input, and state the noncomputable rate explicitly.

[S5] Route (a) is misdescribed as "regularity data", and the claim that only the third route remains is too strong. (Sections 4.1 and 4.3: "For an agent that must be able to adopt any measure-presented prior, only the third route among these is available. That gives a computational reason, independent of physics, to model continuous evidence sources as regular channels.")
- What is wrong, first: in Proposition 3(a) what is presented is the density q itself, the full likelihood, not merely regularity constants. With respect to the fixed reference measure (counting measure times Lebesgue), the joint density of every mu_M is bounded by 4 uniformly. So a uniform bound is already available for the whole family. The information that encodes the halting time is the density, not the bound. This also shows something the paper should say: a uniform bound on the density is not enough when only measure presentations are given, and the obstacle is the modulus of continuity alone. The sentence "The densities f_n have peak heights 2^(n+2)", offered as part of what defeats U, should be revised.
- What is wrong, second: route (b) is derived from route (a), so the routes are not independent. Route (b) also does not leave priors "unrestricted". It requires every adopted joint state to have the form rho (x) (fixed noise), which is a restriction on the class of adoptable joint states. An agent that "must be able to adopt any measure-presented prior" over H x Y can adopt mu_M on the exact Z-observation, and then route (b) does not help. Finally, route (b) answers a different evidential question (a noisy reading, not Z), so it is not conditionalization on the same evidence.
- What would fix it: rename (a) "presented likelihood", note the uniform bound on the family, present (b) as a restricted class of joint states, and weaken the "only the third route" and "computational reason to model channels as regular" claims to what the propositions show.

[S6] "Admissibility is not intrinsic" (Section 4.3) runs together a property of the agent and a property of a credence function.
- What is wrong: under FOLLOW, following the rule is a property of an agent, meaning its procedure together with its reachable space. It is not a property of mu_{M0}. Saying that whether a credence function "is fit to be held depends on what else could have been held" (Conclusion) moves without argument from the agent to the credence. The claim that this holism is "new to this debate" is also asserted without support.
- What would fix it: either restate the claim as a claim about agents, or argue for the move to a property of credence functions. Remove or defend the novelty claim.

[S7] The use of Kripke (Section 4.2, "Finitude") misrepresents his discussion.
- What is wrong: the paper answers Kripke by saying that for an engineered system "which procedure runs is fixed by its code". Kripke (1982, around pp. 33-37) considers machines explicitly and argues that which function a physical machine computes, including malfunction and finitude, is fixed only relative to its designer's intentions or a program taken as an abstract object. The reply therefore assumes what Kripke disputes.
- What would fix it: either engage that passage directly or drop the Kripke framing and say plainly that the paper takes the program as given.

[S8] The mathematical novelty is overstated relative to known results.
- What is wrong: the paper says Proposition 2 is a "close relative" of known results, and that is fair. But given that it is, Section 4.3's claim of "a kind of holism ... new to this debate" and the abstract's framing rest heavily on a lemma that follows from the discontinuity of the disintegration map at A. Related uniformity results are in Ackerman, Freer and Roy 2017 ("On computability and disintegration") and in Hoyrup, Rojas and Weihrauch's counterexample to the Radon-Nikodym operator.
- What would fix it: cite AFR 2017, state precisely what is new in Proposition 2 compared with these results, and present the contribution as primarily conceptual.

[S9] Proposition 4 needs small repairs.
- What is wrong: the estimate that divides by 2 epsilon fails when the ball around y extends beyond [0,1], where the density is zero. The procedure must choose epsilon < min(y, 1 - y), which it can do for y in (0,1). The averaging error is at most ||g|| L epsilon / 2; the stated bound of ||g|| L epsilon is valid but loose. The step from computable posterior expectations of bounded Lipschitz g to a measure presentation of the posterior on a general H needs a sentence: it works because a probability measure is computable if and only if its integrals of bounded Lipschitz test functions are uniformly computable, but that should be said.
- What would fix it: add these qualifications. None of them changes the result.

[S10] The per-prior response is attributed to nobody.
- What is wrong: the disclaimer in Section 1 is honest, but it leaves the target looking constructed for the purpose. AFR themselves, and the probabilistic-programming literature, in effect recommend restricting attention to models whose conditional distributions are computable.
- What would fix it: find and cite actual statements close to the per-prior response, or recast it explicitly as a natural default.

[P1] Proposition 2 does not need the recursion theorem. Take any presentation of A. A correct U halts with output near delta_0 after reading a finite prefix of the presentation and of the name. Then (1 - 2^-n)A + 2^-n B_n, for large n, has a presentation agreeing with that prefix, since its total-variation distance from A is 2^-n. The halting-time indexing is needed only to support the remark that presented data "cannot always be derived from the prior", and that remark also follows from Proposition 2 together with Proposition 3(a). The simpler argument would make the discontinuity explicit and the connection to AFR transparent.

[P2] The appendix should add one sentence on self-simulation. Any level k of e* that M*'s search has finished evaluating simulates M* for k steps, which forces k to be below the current running time of M*, and so below m*. That is why the computation of U on e* found during the search is still valid for the actual mu_{M*}.

[P3] Section 2: say "ideal points of the computable metric space" rather than "rational points". The atomless condition on lambda in Proposition 3(a) is unnecessary. State that q rho (x) lambda must be normalized.

[P4] The abstract's three bullets and the list in Section 1 repeat the same content. The abstract could be shorter.

[P5] Section 4.2 G4 example: note that a single mu_{M0} lies in some C_{C,L} with C of order 2^(n+2) and L of order 2^(3n+3) (under the rho-relative normalization), so that the example can be checked.

Verdict: major revision.

The mathematics is correct and cleanly done. The question is a worthwhile one for formal epistemology, and the separation of the ideal reading from the followed reading is useful. But the main thesis is too close to built into FOLLOW. The obvious structured-representation and finite-precision replies are not answered. The "three routes" discussion contains claims that are wrong as stated (S5). The mathematical core is a known kind of non-uniformity. A revision that defends FOLLOW independently, proves the structured-representation version of Proposition 2 and deals properly with interval conditionalization could be a solid contribution.

Scores:
- Originality: 5
- Correctness: 7
- Importance: 4

Sources consulted: PhilSci Archive and CiteDrive listings for Lopez-Wild; Cambridge Core for Rescorla 2025; PhilPeople and PhilSci Archive for Huttegger, Walsh and Zaffora Blando; the arXiv 1005.3014 abstract and listings, the ACM DOI 10.1145/3321699, and arXiv 1509.02992 for AFR. I could not open the full text of arXiv or ar5iv because those hosts are not in this session's allowed network domains, so the AFR section number in point 7 remains unverified.
