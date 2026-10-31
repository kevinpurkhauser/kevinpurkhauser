# Calibration: role D on decoy 2

Report reproduced verbatim from the subagent's hand-back.

**Referee report: "Following Conditionalization: Computable Agents and the Noise in Evidence"**

**What the paper adds.** The paper builds a simple, uniformly computable family of priors from the Ackerman, Freer and Roy (AFR) example. It uses the family to argue that a computable agent's ability to follow Kolmogorov conditionalization depends on how its prior is represented, and not only on its credence function. It then argues that an open-ended learner with an unrestricted prior over the world can follow the rule in general only by modelling its continuous evidence as having a bounded likelihood density, that is, as noisy.

The noise thesis is a new and potentially valuable bridge between computable probability theory and the epistemology of evidence. However, the central argument from Proposition 1' to the claims about individual agents has a gap in scope. The paper also contains one misattributed theorem, at least one doubtful attribution, and a refinement that is inconsistent with the format it is meant to refine.

**Points**

1. [S] **The wrong incompleteness theorem.** Corollary 1 says that if T proved that M_T never halts, "it would prove ... its own consistency, contrary to Gödel's first incompleteness theorem." The fact that a consistent, computably axiomatized theory containing enough arithmetic cannot prove its own consistency is Gödel's second incompleteness theorem. Fix: cite the second theorem.

2. [S] **Corollary 1 is stated for theories too weak to support it.** The step "if T proved that the presented prior has a computable conditional distribution, it would prove that M_T never halts" needs T to prove the halting direction of Proposition 1. That is, T must prove that if M_T halts then P_{M_T} has no computable version, which requires formalizing the AFR theorem and Lemma 2 inside T. A theory that merely "interprets enough arithmetic", such as Robinson's Q, need not prove the AFR theorem. Fix: restrict the corollary to theories that prove the AFR theorem and Lemma 2, for example extensions of ZFC or a suitable second-order arithmetic. The ZFC instance then stands.

3. [S] **The paper slides from "no procedure handles all cases" to "no procedure handles this agent's case".** This is the main problem and it affects R3 (Section 4.1) and N3 (Section 5). Proposition 1' is a uniformity result: no sound updater commits on every updatable P_M. It does not follow that the second agent's own presentation, P_{M_ZFC}, escapes every sound procedure.

   Consider the procedure "if the input is syntactically P_{M_ZFC}, commit to the constant kernel δ_0 ⊗ ν; otherwise, never commit." It is sound if ZFC is consistent, it is general in the paper's sense, and it covers the agent's case. In fact every individual non-halting M has some sound procedure that commits on P_M.

   The text says "Nothing available to the agent distinguishes its own case from those." That sentence brings back an epistemic or certification requirement, which Section 4.2 explicitly disavows ("R1 asks for no proof").

   FOLLOW, as stated, also requires soundness only "on every state to which the agent applies it". So it does not rule out the tailored procedure above. The R3 argument instead appeals to "the presentations it could equally have held", a modal strengthening that FOLLOW does not contain. The diachronic defence in Section 4.2 does not close the gap either: the posteriors that later updates take as input are produced by the agent's own procedure and can be issued in a standard format.

   Fix: either (a) state a modal FOLLOW that requires soundness and completeness over a specified class of presentations, with an independent argument for why that class must include every P_M, or (b) concede that the asymmetry between the two agents rests on an epistemic condition and defend that condition. Without one of these, R3 and the claim of representation-dependence are not established. The open-ended version in Section 5 (N2 and N3) is in better shape, because there "any state it may be in" plausibly ranges over an unrestricted family. That should be made the primary argument.

4. [S] **The argument for R4 is invalid as stated.** R2 gives a sufficient condition for being bound: an agent that can follow the rule is bound by it. To conclude that the two agents differ in standing, you also need the converse, that an agent which cannot follow the rule is not bound by it as a followed rule (an ought-implies-can premise). Without that premise both agents could be bound, and R4 would fail. The text also says "the inference from R1 to R3 to R4 is valid", which omits R2. The report that the "first-order skeleton was checked mechanically" cannot be verified and does not reassure, given the missing premise. Fix: add the ought-implies-can premise explicitly, defend it, and give the full premise set.

5. [S] **"No amount of logical skill" overclaims (Section 4.4, point 2).** Corollary 1 shows that each theory T fails for its own M_T. A stronger theory, such as ZFC + Con(ZFC), proves that P_{M_ZFC} is updatable. What fails is a single theory that settles every case, not logical skill as such. The contrast with logical non-omniscience is therefore weaker than claimed. Fix: say that no single consistent, computably axiomatized theory closes all such gaps, and rework the contrast with Hacking and Garber around that claim.

6. [S] **The "no floor on noise" refinement is inconsistent with the channel format.** Lemma 3's closure under mixture puts the mixture index (here the noise scale s) among the world-variables and requires a bounded likelihood given all world-variables. With s as a world-variable, the likelihood φ_s(y − h) is unbounded as s goes to 0, so the channel format as defined does not cover this case. The bound (2π)^{-1/2} E_π[1/s] holds only for the density with s integrated out. That density gives a computable posterior over h by the cited theorem, but not over s. Section 6 then claims that "the agent's credences about how noisy its channel is are set by evidence", which needs the joint posterior over (h, s). The cited AFR theorem does not deliver that.

   The computations themselves are correct: the mixture density peaks at zero, the supremum is (2π)^{-1/2} E_π[1/s], the density 2s gives E[1/s] = 2 and the weight d² on (0, d), and the uniform prior gives an infinite expectation.

   Fix: either prove separately that the posterior over (h, s) is computable when E_π[1/s] is finite and computable, or confine the refinement to the posterior over h and drop the claim about learning the noise scale. The same issue affects the countable-mixture clause of Lemma 3: "a computable uniform bound in the countable case" may not exist, because the supremum of the bounds c_i can be infinite. Closure under mixture should be stated only for uniformly bounded families.

7. [S] **Probable misattribution to Freer and Roy (2010).** Section 5 says that the special case of additive independent noise with a bounded computable density "is due to Freer and Roy 2010". The cited AISTATS paper, "Posterior distributions are computable from predictive distributions", is about exchangeable sequences and de Finetti measures, which is how Section 6 correctly cites it. As far as I know, the additive-noise corollary appears in AFR's own work (LICS 2011 and JACM 2019). Fix: re-attribute it, or cite the correct source.

8. [S] **The bounded-density theorem needs its hypotheses spelled out.** As I recall, AFR's positive result requires the conditional density to be bounded and computable, which entails continuity on its domain, or else a stated almost-everywhere variant. Many natural noise models, such as uniform noise, have discontinuous densities. Lemma 3 should state the exact hypotheses of the theorem invoked, including whether the bound c must be supplied as input, and should say which channels meet them. Otherwise "every continuous source modelled as noisy" is broader than the theorem.

9. [S] **The claim that this holds "whatever format the current state is in" (N3) is asserted, not argued.** The claim that the obstacle survives an evidence-first format needs an argument that the states such a learner can reach, combined with a new exact source, include a family as rich as {P_M}. One way to do this is to show that the unrestricted world prior forces it. Fix: state this as a lemma.

10. [P] The sentence "Since the set of machines that never halt is not computably enumerable, two corollaries follow" is inaccurate for Corollary 1, which rests on incompleteness rather than on non-enumerability alone.

11. [P] Attributing regular conditional distributions and disintegration to Kolmogorov (1933) is loose. Kolmogorov defined conditional probability with respect to a random variable through Radon-Nikodym derivatives. The regularity of versions came later (Doob and others). Rephrase.

12. [P] In Lemma 2, restricting a finite approximation to {1} × X yields a sub-probability measure whose mass is only approximately w. Say that it must be renormalized and that the Prokhorov estimate survives renormalization. The argument is otherwise correct, as are Lemma 1 (the 2^{-k} bound) and Corollary 2 (the total variation distance is exactly w).

13. [P] Bibliography. The entries for AFR (LICS 2011; MSCS 27(8); JACM 66(3), Article 23), Rescorla (RSL 11(4), 2018), Hacking (1967), Garber (1983), Kolmogorov (1933) and Mahtani (2024) look correct. I could not verify Huttegger, Walsh and Zaffora Blando (2026, PPR 112(1): 307-324), or that its title and its recommendation of computable probability theory are as described. Please check them. Rescorla (2018) lacks page numbers. AFR 2017 is listed but never cited.

14. [P] Section 6 says exact channels "receive prior probability zero within" the format. Strictly, they are not representable in it at all, and neither is any mixture that gives an exact channel positive weight. Say so, since this is the substantive cost.

15. [P] The remark about mechanical verification and the parenthetical "(Both computations were checked symbolically.)" add nothing a reader can assess. Either supply the material or remove the remarks.

**Overall assessment.** The technical core (Lemmas 1 and 2, Proposition 1, Proposition 1' and Corollary 2) is correct, and the paper honestly presents it as elementary. The philosophical payoff rests on two steps that do not yet work. The first is the move from a uniformity result to a claim about a particular agent's standing (point 3). The second is the validity of the argument for R4 (point 4). The noise thesis is the most interesting contribution and survives in a weaker form if the argument is run through the open-ended learner. Even so, its refinement about the noise scale is not supported by the format as defined (point 6). There is one clear misattribution (Gödel's first theorem in place of the second) and one probable misattribution (Freer and Roy 2010).

**Verdict:** major revision.

**Scores:**
- Originality: 6/10
- Correctness: 4/10
- Importance: 5/10
