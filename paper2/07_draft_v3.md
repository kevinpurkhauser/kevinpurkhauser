---
title: "Following Conditionalization: Computable Agents and the Noise in Evidence"
---

**Abstract.** Some computable priors have conditional distributions that no algorithm can compute (Ackerman, Freer and Roy). I use an elementary construction to show something different. Restricted to priors whose conditional distributions *are* computable, there is still no procedure that is both sound and complete: none commits to an update on every such prior and only ever commits to correct updates. I draw two conclusions about conditionalization, understood as a rule that a computable agent follows rather than as an evaluative ideal. First, whether an agent can follow the rule depends on the class of representations its belief-forming processes can produce, not only on its present credence function. Second, consider an agent that learns open-endedly, adopting arbitrary priors over hypotheses and new models of evidence sources. It can follow the rule only if it models each continuous source as having a bounded likelihood density given the hypotheses, that is, as noisy, or else restricts its priors over the hypotheses. The noise may be arbitrarily small, and the agent may be uncertain about its size without assuming a lower bound. A computational fact thus bears on how a rule-following learner must model its evidence.

# 1. Introduction

When a Bayesian agent learns that a continuous quantity $Y$ took the value $y$, the event $Y = y$ has probability zero and the ratio formula is silent. The standard answer is Kolmogorov conditionalization. The new credence is given by a regular conditional distribution: a kernel $y \mapsto P[\,\cdot \mid Y = y]$ that disintegrates the prior, defined up to sets of observations of measure zero. (The measure-theoretic notion of conditional probability goes back to Kolmogorov 1933; regular versions and disintegrations belong to later developments.) Rescorla (2018) has proved Dutch book and converse Dutch book theorems for this rule, and Rescorla (2025) extends them to non-factive learning.

Ackerman, Freer and Roy (2011, 2019; hereafter AFR) showed that the rule can outrun computation. There are computable random variables $X$ and $Y$ whose conditional distribution of $X$ given $Y$ has no version that is computable on a set of measure one. The obvious response is that the defect lies in particular priors, not in the rule. On this view computable rationality should constrain priors, as computability considerations already do in other respects (Lopez-Wild 2026; Huttegger, Walsh and Zaffora Blando 2025). The agent should simply hold a prior whose conditional distributions are computable.

I argue that this response does not take us where it seems to. My thesis has three parts.

1. **No sound and complete updater** (Proposition 1'). Restrict attention to presented priors that can be updated computably. Even then, no procedure commits to an update on all of them while committing only to correct updates. Updatability can hold of a prior without being recognisable from any presentation of it.
2. **Representation-dependence.** Suppose that following a diachronic rule requires a single procedure that is sound and complete on the states the agent's belief-forming processes can produce. Then whether an agent can follow conditionalization depends on that class of states. Two agents with the same credence function can differ in whether they can follow it.
3. **Noise.** Suppose a learner may adopt any computable prior over its hypotheses and may model new continuous sources exactly. Then it cannot follow conditionalization, even when each source model is a trivial exact report of one hypothesis variable. If it models each continuous source as having a bounded density given the hypotheses, it can follow the rule whatever its priors over the hypotheses. The only general alternative known is to place the bounded-density condition inside the prior over the hypotheses, which restricts what the agent may believe about them.

Part 1 is an elementary consequence of AFR, and I present it as such. Parts 2 and 3 are the contribution. AFR already observe that independent computable noise with a bounded density restores computable conditioning, and that conditioning cannot in general be approximated uniformly by shrinking the noise. What is new is the argument that a rule-following learner, as opposed to a modeller looking for tractable cases, has to model its evidence as noisy, and the claim that its standing as a follower of the rule depends on the form of its representational system.

The scope is limited in three ways.
- Nothing here concerns conditionalization as an evaluative ideal, against which any transition can be assessed whether or not anyone can meet it.
- Nothing here concerns discrete evidence, or evidence of positive probability, where the ratio formula is computable.
- The conclusions depend on two principles, FOLLOW and a restricted ought-implies-can, which Section 2 states and Section 4 defends.

# 2. Conditionalization as a rule followed

I work in computable probability theory, which Huttegger, Walsh and Zaffora Blando (2025) propose as a framework for modelling computationally bounded Bayesians.

The basic notions are these.
- Outcome spaces are computable metric spaces, for example the reals, Cantor space, and finite products of them.
- A probability measure is *computable* if some program, on input $k$, outputs a finitely supported measure with rational weights at rational points within Prokhorov distance $2^{-k}$ of it. Such a program is a *presentation* of the measure.
- A conditional distribution map for $H$ given $Y$ is *computable* if some version of it is computable on a set of observations of measure one. Here it is a map from observations to measures, and the observation is given as an oracle, that is, as a stream of approximations.

Correctness is a property of kernels, not of single transitions. Every individual observation has probability zero, so any posterior at a single point agrees with some version. Accordingly:
- an *updating procedure* takes a presentation of a prior and either never commits, or commits to a program that, given the observation as an oracle, outputs a posterior;
- it is *correct* on a presentation if the committed program computes a version of the conditional distribution map on a set of observations of measure one.

The two readings of the conditionalization rule can then be stated.
- On the *ideal reading* the rule is a standard. The correct kernel exists whether or not anyone can compute it.
- On the *followed reading* the rule is something the agent does. The agent updates by conditionalizing in the way someone adds by following the rule for addition, not merely by producing sums.

The followed reading is the one in play when Bayesian models are offered as accounts of how minds or machines learn, and when we ask what a bounded agent is required to do.

Let the *representational system* of an agent be the class of presentations that its belief-forming processes can put it in. These processes are prior formation, acceptance of models from others, revision of its models of evidence sources, and its own updating. Call a procedure *sound* on a class if it is correct whenever it commits. Call it *complete* on a class if it commits on every member of the class that has a computable conditional distribution map. Completeness is relative to what can be done at all, so AFR's uncomputable priors place no demand on it.

**FOLLOW.** A computable agent can follow conditionalization only if some single procedure is sound and complete on its representational system.

**OIC.** A computable agent is bound by conditionalization *as a followed rule* only if it can follow it.

FOLLOW asks for no proof that the procedure is correct. It asks for generality: soundness and completeness across the states the agent's own processes can produce. OIC is ought-implies-can, restricted to the followed reading. It does not touch the ideal reading. Section 4 defends both. First, the result that gives them force.

# 3. A prior that cannot be certified

Fix the AFR pair: computable random variables $(X, Y)$ with joint law $B$ such that $B[X \mid Y]$ has no version computable on a $B_Y$-measure-one set. In AFR's construction the conditional distribution encodes the halting problem. Fix any computable measure $\nu$ on the range of $X$, and a binary variable $I$. For each Turing machine $M$, let $w_M = 2^{-n}$ if $M$ halts at step $n$, and $w_M = 0$ if it never halts. Define, on triples $(I, X, Y)$,

$$P_M = (1 - w_M)\,(\delta_0 \otimes \nu \otimes B_Y) \;+\; w_M\,(\delta_1 \otimes B).$$

With weight $1 - w_M$ the agent thinks that $I = 0$, that $X$ is drawn from $\nu$, and that $Y$ is drawn independently from $B$'s $Y$-marginal. With weight $w_M$ it thinks that $I = 1$ and that $(X, Y)$ is drawn from $B$.

**Lemma 1.** $P_M$ is computable uniformly in $M$. To approximate $w_M$ within $2^{-k}$, run $M$ for $k$ steps; mixtures of computable measures with computable weights are computable.

**Lemma 2.** Both components have $Y$-marginal $B_Y$. If $w_M > 0$, then for almost every $y$ the conditional distribution of $(I, X)$ given $Y = y$ is $(1 - w_M)\,\delta_0 \otimes \nu + w_M\,\delta_1 \otimes B[X \mid Y = y]$. Restricting a computable version of it to $I = 1$ and renormalising yields a computable version of $B[X \mid Y]$.

**Proposition 1.** $P_M$ has a computable conditional distribution map if and only if $M$ never halts. If $M$ never halts, $P_M = \delta_0 \otimes \nu \otimes B_Y$, and the constant kernel $\delta_0 \otimes \nu$ is computable. If $M$ halts, Lemma 2 and the AFR theorem rule out a computable version.

**Proposition 1' (no sound and complete updater).** No procedure is both sound and complete on the class $\{P_M\}$. If one were, the set of $M$ on which it commits would be computably enumerable. Completeness puts every non-halting $M$ in that set, and soundness together with Proposition 1 keeps every halting $M$ out of it. So the set would be exactly the set of non-halting machines, which is not computably enumerable.

**Corollary 1 (no single theory certifies every case).** Let $T$ be any consistent, computably axiomatized theory that proves Proposition 1, such as ZFC or any consistent extension of it. Let $M_T$ search for a proof of $0 = 1$ in $T$. Then $M_T$ never halts, so the presentation $P_{M_T}$ presents the tractable prior $\delta_0 \otimes \nu \otimes B_Y$. But $T$ does not prove that it does. If it did, it would prove that $M_T$ never halts, and hence its own consistency, which Gödel's second incompleteness theorem rules out. Each instance can be settled in a stronger theory: ZFC + Con(ZFC) settles $P_{M_{\mathrm{ZFC}}}$. What no single theory can do is settle them all.

**Corollary 2 (fragility in the family).** The tractable prior $Q = \delta_0 \otimes \nu \otimes B_Y$ is the limit in total variation, as the computable weight $w$ goes to $0$, of the priors $(1 - w)\,Q + w\,(\delta_1 \otimes B)$. None of these has a computable conditional distribution map. So within this family, updatability is not open. That is the property which Rice-Shapiro style reasoning connects with failure of semi-decidability.

The proofs are in the appendix. The results are elementary. The interest lies in what they show about following the rule.

# 4. Representation-dependence

## 4.1 The argument

1. **(R1)** FOLLOW.
2. **(R2)** OIC.
3. **(R3)** A computable agent that holds a computable prior, receives continuous evidence, and can follow conditionalization is bound by it as a followed rule.
4. **(R4)** There are two computable agents with the same present credence function such that the first can follow conditionalization and the second cannot.
5. **(R5)** So the first agent is bound by conditionalization as a followed rule and the second is not (R2, R3, R4). Whether an agent is so bound is not determined by its credence function.

The witness for R4 is as follows. Both agents now hold the tractable measure $Q$.

The first agent, the *channel agent*, has a representational system consisting of channel presentations (Section 5): a prior over hypotheses, a likelihood density for each source, and a stated bound on each density. By the AFR theorem for bounded densities, together with Lemma 3, one procedure is sound and complete on this whole class, and the class is closed under the agent's updating. So, by FOLLOW's standard, the channel agent can follow the rule.

The second agent, the *open agent*, has a system that admits any presentation of a computable prior that its processes deliver. A general-purpose probabilistic reasoner is like this. It accepts priors written as arbitrary programs, from its own model-building or from others, and conditions them on continuous data. Such a system contains every $P_M$, since each is a perfectly ordinary program for a perfectly ordinary measure. By Proposition 1', no procedure is sound and complete on it. So the open agent cannot follow conditionalization, although its present state is one that the channel agent updates without difficulty.

R1 enters as the premise that makes R4 true of the witness. The rest of the section defends R1 and R2.

## 4.2 Why soundness and completeness on the system

The strongest objection is that the open agent can update its present prior correctly. The constant procedure "output $\delta_0 \otimes \nu$" is there for the taking. More generally, any non-halting $M$ admits some sound procedure that commits on $P_M$. Why should anything more be required?

The reply is that an update rule is diachronic and open-ended. The agent's procedure must handle not only its present state but every state its belief-forming processes may deliver. A procedure tailored to $P_{M_{\mathrm{ZFC}}}$ is sound only because it refuses to commit everywhere else. It then fails completeness on the rest of the open agent's system, which contains infinitely many updatable presentations. An agent that runs such a procedure updates correctly on one state and cannot update at all on others that are just as tractable. That agent is not following conditionalization. It has a single correct answer stored for one case.

The analogy with arithmetic makes the point. A child follows the rule for addition because her procedure is sound and complete on the numerals she can be given. It is not enough that she gets today's sum right. FOLLOW transfers this standard to updating. The relevant domain is the representational system, because that is the class of states to which the agent's updating must apply. A domain chosen to suit one case would not be.

The objection has a sharper form. If the system is the class of all presentations, then by AFR no agent follows conditionalization, and the moral is just AFR's. That is not the present claim. AFR's priors with no computable update put no demand on completeness. Proposition 1' concerns the priors that *can* be updated. Its moral is that an unrestricted system fails even on the tractable part of its domain. A restricted system, the channel class, succeeds on all of its domain, and that domain allows every computable prior over hypotheses. The difference between the two agents is therefore not between an agent that tries the impossible and one that does not. It is between two systems that make the same tractable states available, only one of which can be followed.

Nor does FOLLOW prove too much. The worry is that if norms bind only agents who can meet them by a general procedure, then coherence, consistency, or even holding a total program would cease to bind. FOLLOW is a condition on following *diachronic* rules, which produce new states from old ones. A presentation of a measure is coherent because of what it presents, and nothing has to be executed for it to be so. Updating, by contrast, has to be executed, and executing it means running a procedure on representations.

## 4.3 OIC and functionalism

OIC is restricted to the followed reading. It says that conditionalization binds an agent as a rule it follows only if the agent can follow it. Someone who rejects even this restricted principle owes an account of how a rule can bind as followed when no procedure available to the agent's system could follow it. The ideal reading is untouched: both agents fall short of, or meet, the same evaluative standard to the same degree.

Do the two agents behave identically? On their present state they produce the same posterior. They differ in what their updating would do on other states their systems allow. Functionalists individuate states by dispositional roles, not by a single actual output. So R5 does not conflict with functionalism about the updater. It conflicts with the view that the credence function alone fixes an agent's standing as a follower of conditionalization.

## 4.4 How this differs from logical non-omniscience

Representation-dependence is familiar from the literature on logical non-omniscience. Agents whose beliefs are logically equivalent can differ in what they are able to infer, which is the motivation for treating logical learning as a source of confirmation (Hacking 1967; Garber 1983). Mahtani (2024) argues that credences are hyperintensional, depending on the mode of presentation of their objects. The present result differs from these in two ways.

1. In those cases the agent cannot reach a further proposition, some consequence of what it believes. Here the credence function is fully given and computable, and nothing about its content is hidden. What varies is whether a norm can be executed on it, given the agent's system.
2. The non-omniscience gap can be closed instance by instance by more logical work. Here too each instance can be closed (Corollary 1). But no single sound procedure, and no single consistent computably axiomatized theory, closes all the instances an open system contains (Proposition 1', Corollary 1). So the dependence is not a shortfall from a uniformly attainable ideal.

# 5. Why the rule-follower must model noise

Distinguish the agent's *hypothesis variables* $H$, the quantities its credences are about and that it is learning, from its *observation variables*, the readings delivered by its sources. A *channel presentation* consists of three things:
- a program for a prior $\mu$ over $H$;
- for each source, a program for a likelihood density $p(y \mid h)$ with respect to a computable reference measure;
- a rational bound $c$ on that density.

AFR prove that in this dominated setting, with a bounded computable density, the conditional distribution map is computable. The special case of additive independent noise with a bounded computable density is their Corollary 9.7 in the arXiv and journal numbering. This result is the basis of the following lemma.

**Lemma 3.** The channel class has four properties.
- **Soundness and completeness.** One procedure is sound and complete on the class. It reads the bound and applies the AFR algorithm, relative to the observation as an oracle.
- **Any prior over hypotheses.** Every computable prior over $H$ has a channel presentation, for example with any bounded computable noise.
- **Mixtures.** The class is closed under finite computable mixtures (adjoin the index to $H$ and take the largest bound). It is closed under countable mixtures only when there is a given uniform bound.
- **New sources.** The class is closed under adding sources that are conditionally independent given $H$. The joint density is the product of the densities, and it is bounded by the product of their bounds.

Now consider exact sources. The simplest is an exact report of one hypothesis variable. Rename the coordinate $Y$ of Section 3 as a hypothesis variable $Z$, and let a source report $Z$ exactly. The source model is then fixed and trivial: a coordinate projection, the same for every $M$. The priors $P_M$ over $(I, X, Z)$ form a uniformly computable family of priors over hypotheses. By Proposition 1', no procedure is sound and complete on the presentations that combine these priors with this exact source.

The argument for the noise thesis is then as follows.

1. **(N1)** An open-ended learner may adopt any computable prior over its hypotheses, and it incorporates new sources by modelling how their readings depend on the hypotheses.
2. **(N2)** By FOLLOW, it can follow conditionalization only if one procedure is sound and complete on the resulting system.
3. **(N3)** If the system admits exact source models, then with unrestricted priors over hypotheses it contains the family just described, so no such procedure exists (Proposition 1').
4. **(N4)** If every continuous source is modelled with a bounded computable density given the hypotheses, a procedure that is sound and complete on the whole system exists, with unrestricted priors over hypotheses (Lemma 3).
5. **(N5)** So an open-ended learner can follow conditionalization while leaving its priors over hypotheses unrestricted if it models its continuous sources in this way, and it cannot if it admits exact source models. A source with a bounded density given the hypotheses is one whose reading is not a function of them. Such a source is noisy.

Three qualifications are needed.

**Exact sources with restricted priors.** An exact report of $Z$ can be followed if the prior gives $Z$ a bounded computable density given the other hypothesis variables, presented with its bound. The condition is the same, moved from the channel to the prior over hypotheses: the reading must have *slack*, a bounded density, relative to the variables the agent is learning about. One might object that the difference is only a matter of labelling, since a reading is a physical quantity too. The distinction I need is not between the world and something outside it. It is between the variables that are the targets of learning and the readings. With the slack in the channel, the agent's marginal credences over its targets are unrestricted, and only its model of how readings depend on them is constrained. With the slack in the prior, its credences over the targets themselves are constrained. For example, it may not be certain that the reported quantity is an exact function of other quantities it is learning about. The joint credence is constrained either way. What differs is which part of it the constraint falls on.

**Other routes.** The exchangeable case is a genuine alternative. Freer and Roy (2010) show that, for exchangeable sequences, posteriors over the de Finetti measure are computable from the predictive distributions. That route does not use densities. But it certifies updating on a source whose predictive distributions are already part of the agent's state. It does not tell an agent how to take on a new source that it models by how the source depends on hypothesis variables, which is the case N1 concerns. I know of no general route for that case other than the dominated one. N5 claims sufficiency for the dominated route and failure for exact source models in general. It does not claim that no other route could exist.

**What the certificate is.** Whether a program computes a density bounded by $c$ is not decidable, so the channel format, like any certified format, works because the bound is supplied as part of the representation. What makes this certificate apt for an open-ended learner is that it is *local*. It concerns one source model, can be stated without reference to the agent's priors over hypotheses, and composes across sources and mixtures. A stored posterior kernel is also a certificate, but it has to be recomputed for every new prior and every new source, and that recomputation is exactly what is in question.

Two refinements show that the requirement is weaker than it may sound.

**No floor on noise.** One might think a follower must be certain that its noise exceeds some fixed level, which would be a dogmatic belief about its instruments. It need not be. Let the noise be Gaussian with unknown scale $s$, and let the agent's prior over $s$ on $(0, 1)$ be $\pi$, with $s$ integrated out of the likelihood.
- After $n$ readings from the source, the joint density of the readings given $h$ is at most $(2\pi)^{-n/2}\,\mathbb{E}_\pi[s^{-n}]$, with equality when every reading equals $h$. So it is bounded if and only if $\mathbb{E}_\pi[s^{-n}] < \infty$.
- For $\pi(s) \propto e^{-1/s}$, every such moment is finite, and every interval $(0, d)$ has positive prior probability.
- Hence, for any number of readings, the posterior over hypotheses is covered by Lemma 3, though the agent leaves open how small its noise is.

Two limits remain.
- The weaker prior $\pi(s) = 2s$ covers one reading but not two.
- Learning about $s$ itself is not covered, since the density given $(h, s)$ is unbounded as $s$ goes to $0$. Whether a follower can learn its own noise scale without further restriction is a question I leave open.

**The scale is substantive.** In the AFR examples the exact conditional distribution is badly discontinuous, and AFR note that conditional distributions cannot in general be approximated uniformly by shrinking the noise. So the channel model is not an approximation, which the agent fails to compute, of some computable exact-evidence target. The agent's model of its channel is part of the content of its credal state, and it answers to evidence about the channel like any other part.

The conclusion connects with practice. Bayesian models of perception typically posit likelihoods with densities rather than conditioning on exact values of the hypothesis variables. This is usually defended on the empirical ground that neural and physical channels are noisy. The present argument supplies an independent ground. A computable system that follows conditionalization open-endedly, with unrestricted priors over hypotheses, has to represent its continuous evidence that way, whatever the physics of its channels.

# 6. Objections

**From capacity to norm.** The conclusion seems to rest on a fact about the agent's capacities, not on evidence about its channels. It is conditional, and I state it so. *If* conditionalization is to be a rule that a computable learner follows open-endedly, as Bayesian models of cognition presuppose, *then* the learner must model its continuous sources as noisy or restrict its priors over hypotheses. This does not tell an agent with exact continuous evidence, considered as an ideal reasoner, to doubt it. It tells us what the followed rule can be. In the format, exact deterministic channels are not representable. Their exclusion is a cost, and it is not grounded in evidence. It is the same kind of cost as the limits that any representational system places on its hypothesis space. In the cases that matter it is small, because the excluded hypotheses are exact relations that no physical measurement is believed to satisfy. Exact evidence of other kinds, such as computed outputs or a simulation's own state variables, is usually discrete and so outside the scope.

**Total evidence.** The channel-modeller still learns its reading exactly. That is right, and it conditions on exactly that reading. What it does not assume is that the reading is a deterministic function of the hypotheses. So it obeys the requirement of total evidence; what it changes is the model of how evidence relates to hypotheses.

**The Dutch book.** By Rescorla's theorems, an agent that departs from Kolmogorov conditionalization of its own prior is exposed to a Dutch book. The channel-modeller does not depart from it. It conditionalizes its own prior, which includes the channel model, on what it learns. Dutch book vulnerability is assessed against the agent's own credences, so the channel-modeller is not exposed. If its evidence is in fact exact, its credences are inaccurate in a respect it cannot represent, which is a cost of accuracy rather than of coherence. Rescorla's (2025) extension to non-factive learning, where the conditioning proposition may be false, confirms that Kolmogorov conditionalization keeps its pragmatic credentials when evidence is not taken to be infallible.

**Digital evidence.** An agent whose evidence is the content of an input register has exact evidence, and should not model it as noisy. That evidence is discrete, the ratio formula applies, and nothing here says otherwise.

**The evaluative ideal.** Kolmogorov conditionalization may never have been meant as an instruction. If so, nothing here touches it. The claim concerns the rule as followed, which is the reading on which Bayesian models describe how bounded learners actually learn.

# 7. Conclusion

A computable agent may hold a prior that anybody could update and still be unable to follow conditionalization, because its representational system admits states on which no sound general procedure can be complete. Whether it can follow the rule therefore depends on that system, not only on its credences. For an open-ended learner the general way to make the rule followable is to model every continuous source as a noisy channel, while leaving its priors over hypotheses free. The noise can be arbitrarily small, and its size can be uncertain. The lesson is not that exact conditionalization is wrong as an ideal. It is that it cannot be the rule an open-ended computable learner follows. The rule such a learner follows is conditionalization on evidence modelled as having slack.

# Appendix A. Proofs

Notation is as in Section 3. $I$ has the discrete metric, and products carry the maximum metric, so the slices $I = 0$ and $I = 1$ are at distance 1.

**Lemma 1.** On input $k$, run $M$ for $k$ steps. Output $2^{-n}$ if it halted at step $n \le k$, and $0$ otherwise. The error is at most $2^{-k}$. For computable $P$, $Q$ and a computable real $w$, $(1 - w)P + wQ$ is computable: approximate $P$, $Q$ and $w$ closely enough, and mix the finite approximations. All steps are uniform in $M$, by the s-m-n theorem.

**Lemma 2.** Both components have $Y$-marginal $B_Y$, so $P_{M,Y} = B_Y$ for every $M$. Let $w = w_M > 0$ and $\kappa(y) = (1 - w)\,\delta_0 \otimes \nu + w\,\delta_1 \otimes B[X \mid Y = y]$. For measurable $A \subseteq \{0, 1\} \times \mathcal{X}$ and $C \subseteq \mathcal{Y}$, write $A_i = \{x : (i, x) \in A\}$. Then

$$\int_C \kappa(y)(A)\,B_Y(dy) = (1 - w)\,\nu(A_0)\,B_Y(C) + w \int_C B[X \mid Y = y](A_1)\,B_Y(dy) = P_M(A \times C).$$

So $\kappa$ is a version, and any version agrees with it $B_Y$-almost everywhere.

Let $\kappa'$ be a version computable on a measure-one set $S$. Given a finite approximation $\lambda'$ within Prokhorov distance $\varepsilon < \min(1/2,\, w/4)$ of $\kappa'(y)$, its restriction to $\{1\} \times \mathcal{X}$ has mass within $\varepsilon$ of $w$. Renormalising it gives an approximation within $4\varepsilon/w$ of $B[X \mid Y = y]$. So a version of $B[X \mid Y]$ is computable on $S$, which contradicts the AFR theorem.

**Propositions 1 and 1'.** If $M$ never halts, $P_M = \delta_0 \otimes \nu \otimes B_Y$, and the constant kernel is a computable version. If $M$ halts, apply Lemma 2. For 1', let $U$ be sound and complete on $\{P_M\}$ and let $C = \{M : U \text{ commits on } P_M\}$. $C$ is computably enumerable, since $U$ is run in parallel on all $P_M$ and a program for $P_M$ is computable from $M$. Completeness gives $\overline{\mathrm{HALT}} \subseteq C$. Soundness and Proposition 1 give $C \subseteq \overline{\mathrm{HALT}}$. So $C = \overline{\mathrm{HALT}}$, which is not computably enumerable.

**Corollary 1.** If $T$ proves Proposition 1 and proves that $P_{M_T}$ has a computable conditional distribution map, then $T$ proves that $M_T$ never halts, that is, $\mathrm{Con}(T)$.

**Lemma 3.** The joint law of a channel presentation $(\mu, p, c)$ is $\mu(dh)\,p(y \mid h)\,\lambda(dy)$, with a bounded computable density. AFR's theorem for this dominated case gives a conditional distribution map that is computable relative to $y$, uniformly in the presentation and the bound. Mixtures and products are handled as stated in Section 5.

**Noise scale.** For Gaussian noise, $\varphi_s(e) \le \varphi_s(0) = (s\sqrt{2\pi})^{-1}$. So $\int \prod_{i \le n} \varphi_s(y_i - h)\,\pi(ds) \le (2\pi)^{-n/2} \int s^{-n}\,\pi(ds)$, with equality when every $y_i = h$. For $\pi(s) \propto e^{-1/s}$ on $(0, 1)$, substitute $t = 1/s$: $\int_0^1 s^{-n} e^{-1/s}\,ds = \int_1^\infty t^{n-2} e^{-t}\,dt < \infty$.

# References

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2011. Noncomputable conditional distributions. In *Proceedings of the 26th Annual IEEE Symposium on Logic in Computer Science (LICS 2011)*, 107-116.

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2019. On the computability of conditional probability. *Journal of the ACM* 66(3), Article 23: 1-40.

Freer, Cameron E. and Daniel M. Roy. 2010. Posterior distributions are computable from predictive distributions. In *Proceedings of the 13th International Conference on Artificial Intelligence and Statistics (AISTATS 2010)*.

Garber, Daniel. 1983. Old evidence and logical omniscience in Bayesian confirmation theory. In John Earman (ed.), *Testing Scientific Theories*, Minnesota Studies in the Philosophy of Science 10, 99-131. Minneapolis: University of Minnesota Press.

Hacking, Ian. 1967. Slightly more realistic personal probability. *Philosophy of Science* 34(4): 311-325.

Huttegger, Simon M., Sean Walsh and Francesca Zaffora Blando. 2025. Bayesian convergence for computably bounded agents. *Philosophy and Phenomenological Research* 112(1): 307-324.

Kolmogorov, Andrei N. 1933. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Berlin: Springer.

Lopez-Wild, Josiah. 2026. Computable Bayesian epistemology. *Philosophy of Science*. doi:10.1017/psa.2026.10273.

Mahtani, Anna. 2024. *The Objects of Credence*. Oxford: Oxford University Press.

Rescorla, Michael. 2018. A Dutch book theorem and converse Dutch book theorem for Kolmogorov conditionalization. *The Review of Symbolic Logic* 11(4): 705-735.

Rescorla, Michael. 2025. Non-factive Kolmogorov conditionalization. *The Review of Symbolic Logic* 18(1). doi:10.1017/S1755020323000345.
