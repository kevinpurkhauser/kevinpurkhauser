# Round 2: role A (specialist) on draft v3

Report reproduced verbatim from the subagent's hand-back.

Referee report: "Following Conditionalization: Computable Agents and the Noise in Evidence"

Summary of the submission. The paper builds a uniformly computable family of priors P_M. Each is a mixture, with weight w_M = 2^-n (where M halts at step n, else 0), of a trivially updatable product prior Q and the Ackerman, Freer and Roy (AFR) pair B. It shows that P_M has a computable conditional distribution map if and only if M never halts (Prop. 1). It concludes that no updater is sound and complete on {P_M} (Prop. 1'), and adds a Gödel II corollary and a fragility corollary. On top of this it builds two philosophical theses. (a) Whether an agent can follow conditionalization depends on its "representational system", not only on its credence function. (b) An open-ended learner with unrestricted priors over hypotheses can follow the rule if it models continuous sources with bounded likelihood densities, and cannot if it admits exact source models.

What checks out. I verified the following and found them correct.
- Lemma 1: approximating w_M by running M for k steps, and computing mixtures uniformly in M.
- Lemma 2: the version computation, and the renormalisation argument. With slices at distance 1 and epsilon < 1/2, Prokhorov approximations do not move mass across slices by more than epsilon.
- The c.e. argument for Prop. 1'.
- The Gödel II argument for Corollary 1 (given standard provability predicates).
- The total variation claim in Corollary 2: the distance is at most 2w.
- The Gaussian scale-mixture computation. The supremum of the n-reading density is attained at y_i = h. The substitution t = 1/s gives the integral of t^(n-2) e^(-t) from 1 to infinity. For pi(s) = 2s, E[s^-1] = 2 and E[s^-2] diverges, so the claim "one reading but not two" is right.

Bibliography. I checked these and they are accurate:
- AFR 2011 (LICS, 107-116) and AFR 2019 (JACM 66(3), Art. 23).
- The "Corollary 9.7 (Independent noise)" numbering for arXiv v4 and JACM. In arXiv v2 it is Corollary 36, so "the arXiv numbering" should name v4.
- AFR's remark that noise cannot in general be shrunk uniformly.
- Rescorla 2018 (RSL 11(4): 705-735).
- Rescorla 2025 (RSL 18(1), first online 2023; the start page 186 could be added).
- Huttegger, Walsh and Zaffora Blando, PPR 112(1): 307-324. Crossref lists this as 2025 even though volume 112 is nominally 2026.
- Lopez-Wild, Phil. Sci., doi 10.1017/psa.2026.10273.
- Hacking 1967, Garber 1983, Mahtani 2024, Kolmogorov 1933, Freer and Roy 2010 (AISTATS; JMLR W&CP 9: 233-240 could be added).

I found no fabricated or misattributed reference. The problems are in what is claimed from the results.

Points

1. [S] The abstract and Thesis 1 misstate Proposition 1'.
- Where: the abstract says "Restricted to priors whose conditional distributions *are* computable, there is still no procedure that is both sound and complete". Section 1, item 1, says "Restrict attention to presented priors that can be updated computably. Even then, no procedure commits..."
- What is wrong: Prop. 1' is proved for the class {P_M}, which contains the halting-M presentations, and those are not updatable. Restricted to the updatable members of the family (the non-halting M), every member presents the same measure Q. The constant procedure "output delta_0 x nu" is sound and complete there. So the result as proved is not a result about a class restricted to updatable priors. It is a result about a class that mixes updatable and non-updatable presentations, where updatability cannot be recognised. Read literally, the abstract's claim is either false for this family or unproved in general.
- Fix, option one: restate the result honestly. "On any class containing {P_M}, no procedure commits on every updatable member while committing only correctly."
- Fix, option two: prove the stronger statement, that there is no uniform updater on the class of all presentations of updatable computable priors. A natural route is a continuity or non-uniformity argument. Computable operators are continuous, and disintegration is discontinuous even among updatable priors. For example, take Y uniform and X equal to the n-th binary digit of Y. These laws are within Prokhorov distance 2^-n of the independent law, but their kernels stay far from the constant kernel. Turning that into a uniform-computability contradiction needs care with "computable on a measure-one set", so it is not immediate.
- Why it matters: this is the paper's headline technical claim, and as written it is overstated.

2. [S] The abstract's "only if" claim about noise is not established, and the body says so.
- Where: the abstract says the learner "can follow the rule only if it models each continuous source as having a bounded likelihood density given the hypotheses... or else restricts its priors". Section 5, "Other routes", says by contrast: "N5 claims sufficiency for the dominated route and failure for exact source models in general. It does not claim that no other route could exist."
- What is wrong: the argument shows two things only. Bounded computable densities suffice (AFR Cor. 9.6/9.7), and exact channels fail. Between these lie unbounded densities, lower-semicomputable or a.e.-computable densities, and singular non-degenerate channels. None of them is treated.
- The paper's own example points the other way. Take pi(s) = 2s and two readings. For almost every y (namely y_1 != y_2), the likelihood p(y | h) is bounded uniformly in h, by a bound computable from y, because (y_1 - h)^2 + (y_2 - h)^2 >= (y_1 - y_2)^2 / 2 > 0. AFR's proof of the dominated case appears to need only such a local, y-relative bound in order to compute the integral of p(y | h) mu(dh) and the normalised posterior on a measure-one set. If so, global boundedness is not necessary, and the "bounded density" line is drawn in the wrong place.
- Likewise, learning the noise scale s (left open in Section 5) is probably not out of reach. Under pi(s) proportional to e^(-1/s), the product pi(s) phi_s(y - h) is jointly bounded, so the integrals the AFR algorithm needs are computable even though p(y | h, s) is unbounded.
- Fix: drop the necessity claim from the abstract and conclusion, or else prove it. If kept, state the sufficient condition at its proper strength: an effectively integrable likelihood with a y-local bound. Then try to settle the scale question, which the above suggests has a positive answer under mild conditions.

3. [S] The claim that the channel class is "closed under the agent's updating" (Section 4.1, Lemma 3) is false as stated.
- What is wrong: the posterior after observing a typically non-computable real y is computable only relative to y. It is not a computable prior, so it is not a member of a class of computable presentations. The representational system, soundness, completeness and FOLLOW are all defined over (unrelativised) computable presentations.
- Second problem: in the noise-scale example, successive readings are not conditionally independent given h, because they are correlated through s. So the "new sources" closure clause does not apply to sequential updating there. The agent must either re-present the joint n-reading channel or carry s as a hypothesis variable, and Section 5 says the latter is not covered.
- Fix: relativise the whole framework to oracles. AFR's positive results relativise uniformly, and the paper should say so and cite it. Also show explicitly that the post-update state is again a (relativised) channel presentation, including in the scale-mixture case.

4. [S] Thesis 2 (representation-dependence) is an instance of a well-known phenomenon, and the paper neither acknowledges this nor engages with that literature.
- Where: Section 4, and the "contribution" sentence in Section 1.
- What is wrong: in computable analysis it is standard that whether an operation is computable depends on the representation of its domain. See Kreitz and Weihrauch, Weihrauch's *Computable Analysis* (2000), and the theory of represented spaces and admissible representations. Equality on reals is decidable on rational names but not on Cauchy names. "Same mathematical object, different representational system, different computability of the operation" is exactly R4.
- The arithmetic analogy in 4.2 cuts the same way. A child whose numerals include "the number of steps M takes to halt" could not follow addition soundly and completely either.
- The novelty is therefore the application to the norm of conditionalization, not the phenomenon. The dialectic also partly vindicates the "obvious response" in Section 1: the response must be applied at the level of a uniformly updatable system, and the channel class is such a system.
- Fix: say this explicitly, cite the represented-spaces literature, and reframe the contribution. The point is that the computability constraint on priors must be a uniformity constraint on systems. Then defend the claim that this is a philosophically significant refinement.

5. [S] FOLLOW's completeness clause does a lot of quiet work in R4.
- Where: Section 2 and Section 4.2.
- What is wrong: the open agent fails only because its system contains non-updatable presentations (halting M) that it cannot recognise. A defender of the "obvious response" will say the open agent's fault is precisely that it accepts priors it cannot update. That is a restriction on priors, and the paper itself in effect adopts it for the channel agent.
- The paper's reply in 4.2 ("two systems that make the same tractable states available") does not address this. The open agent's system makes untractable states available too, and that is the whole difference.
- Fix: engage this objection directly. Explain why "admit only priors in a uniformly updatable class" is not simply the obvious response done properly. Alternatively, accept that it is, and locate the new content in which uniformly updatable class an open-ended learner should choose, namely the channel class with unrestricted priors over hypotheses.

6. [S] The claim "a source with a bounded density given the hypotheses is one whose reading is not a function of them. Such a source is noisy" (N5) holds only if the reference measure is non-atomic.
- What is wrong: the channel format allows "a computable reference measure", which may have atoms. A deterministic channel into a discrete space has density 1 with respect to counting measure.
- More generally, a bounded density means a non-degenerate conditional law, which is weaker than "noise" in the ordinary sense of measurement error. A deterministic but many-to-one map plus an independent latent variable also qualifies.
- Fix: require lambda to be non-atomic for continuous sources, and replace "noisy" with "non-degenerate given the hypotheses", or argue for the identification.

7. [S] Corollary 1 is ornamental relative to FOLLOW, which "asks for no proof that the procedure is correct" (Section 2).
- What is wrong: Section 4.4(2) uses Corollary 1 as if it added something to Prop. 1'. But the fact that no single computably axiomatized sound theory certifies all instances already follows from Prop. 1': the set of M certified by T is c.e.
- Fix: present Corollary 1 as an illustration, or drop the claim that it is a separate support.
- Minor wording: "ZFC or any consistent extension of it" should be "any consistent, computably axiomatized extension". The theorem is correctly restricted, but the example phrase is not.

8. [S] The uniformity claims attributed to AFR should be checked and cited precisely.
- Where: Lemma 3 says "uniformly in the presentation and the bound", and Section 4.1 refers to "the AFR theorem for bounded densities".
- What is wrong: AFR's dominated-case result (Thm 9.? / Cor. 9.6 in arXiv v4 and JACM) is stated for P-almost computable random variables and a bounded computable density. The uniform version, with the bound supplied as input, is plausible from the proof but should be stated and cited by number.
- The density must also be computable jointly in (h, y). "A program for p(y | h)" should say so, since this implies continuity, and Lemma 3's "any prior over hypotheses" and "mixtures" clauses depend on it.

9. [S] Section 6 ("In the cases that matter it is small...") makes an unsupported empirical claim. It says excluded exact hypotheses "are exact relations that no physical measurement is believed to satisfy". Exact constraints such as conservation laws, or a reading that is a known deterministic function of a latent state in a model, are routinely held in scientific modelling. Fix: qualify the claim, or argue that such exact constraints can always be relocated into the prior over hypotheses at acceptable cost (the "slack in the prior" option).

10. [P] Corollary 2 says "That is the property which Rice-Shapiro style reasoning connects with failure of semi-decidability." This should be made precise. The relevant topology on presentations is the weak (Prokhorov) topology. Non-openness in total variation implies non-openness in the coarser weak topology, and that is what the argument needs. Also note that a sound and complete updater on a class yields a semi-decision procedure for updatability within it, which is the link.

11. [P] State AFR's theorem in the form used. AFR's notion is "computable on a P_Y-measure-one set" for P-almost computable variables. Note also which of AFR's constructions (the a.e.-continuous one or the everywhere-discontinuous one) is fixed as B.

12. [P] Engage the relevant applied literature. Practice in probabilistic programming languages, and the semantics literature on soft versus hard conditioning, already treats conditioning on continuous observations through likelihood densities, partly for computability reasons. Section 5's claim that the argument "supplies an independent ground" for density-based perceptual models would be stronger if placed against that literature.

13. [P] In Section 1 the parenthesis on Kolmogorov 1933 is fine, but "regular versions and disintegrations belong to later developments" deserves one citation, for example Doob or the Chang and Pollard disintegration paper.

14. [P] The witness for R4 uses the same measure Q under two representations. Say explicitly how the channel agent represents Q, for instance with reference measure B_Y and density 1. Otherwise readers may wonder whether Q (with AFR's Y-marginal) has a bounded density with respect to any natural reference measure.

Overall assessment. The formal core is correct but elementary, and the author says as much. Representation-dependence (Thesis 2) is a correct but well-known computable-analysis phenomenon, and the paper does not position it against that literature. The most interesting claim, that an open-ended rule-follower must model evidence as noisy, is overstated in the abstract and conclusion. The body proves sufficiency of bounded densities and failure of exact channels, not necessity, and the paper's own scale-mixture example suggests that boundedness is not the right line. The closure-under-updating claim needs relativisation to be true. These are fixable, and the philosophical framing (followed versus ideal reading, FOLLOW, the slack-in-channel versus slack-in-prior distinction) is clear and worth having. In its present form, however, the headline claims outrun the results.

Verdict: major revision.

Scores:
- Originality: 5
- Correctness: 5 (no false technical lemma, but the headline claims in the abstract and conclusion are overstated or unproved, and the closure claim is false as stated)
- Importance: 5

Sources consulted (web): arXiv:1005.3014 (AFR, v2 and v4 numbering); Cambridge Core page for Rescorla, "Non-factive Kolmogorov Conditionalization" (RSL 18(1), 2025, doi 10.1017/S1755020323000345); Crossref and PhilSci listings for Huttegger, Walsh and Zaffora Blando (PPR 112(1): 307-324) and Lopez-Wild (Phil. Sci., doi 10.1017/psa.2026.10273).
