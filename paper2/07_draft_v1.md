---
title: "Following Conditionalization: Computable Agents and the Noise in Evidence"
---

**Abstract.** Some computable priors have conditional distributions that no algorithm can compute (Ackerman, Freer and Roy). I use an elementary construction to show something different. No sound procedure can recognise, from the program that presents a prior, every prior whose conditional distributions are computable. There is a prior that, if ZFC is consistent, is extensionally identical to a perfectly tractable one, yet no ZFC proof shows that it can be updated. I draw two conclusions about conditionalization understood as a rule that a computable agent follows, rather than as an evaluative ideal. First, whether an agent can follow the rule depends on how it represents its prior, not only on its credence function. Second, an agent that learns open-endedly, from sources it models by their relation to the world, can follow the rule for any prior over the world if it models each continuous source as a channel with a bounded likelihood density, that is, as noisy. The noise may be arbitrarily small and needs no lower bound. A purely computational fact thus yields a normative reason to treat continuous evidence as inexact. It also explains a feature of Bayesian models of perception that is usually defended on empirical grounds alone.

# 1. Introduction

Bayesian epistemology tells an agent who learns that a random quantity $Y$ took the value $y$ to adopt as new credences its prior conditional on $Y = y$. When $Y$ is continuous, the event $Y = y$ has probability zero, and the ratio formula is undefined. The standard answer is Kolmogorov conditionalization: the new credence is given by a regular conditional distribution, a kernel $y \mapsto P[\,\cdot \mid Y = y]$ that disintegrates the prior (Kolmogorov 1933). Rescorla (2018) has given Dutch book and converse Dutch book theorems for this rule, so it has the same pragmatic credentials as ordinary conditionalization.

Ackerman, Freer and Roy (2011, 2019; hereafter AFR) showed that the rule can outrun computation. There are computable random variables $X$ and $Y$ such that no version of the conditional distribution of $X$ given $Y$ is computable on any set of measure one. A computable agent with this prior cannot, by any algorithm, adopt the credences that Kolmogorov conditionalization prescribes.

There is an obvious response, and it is correct as far as it goes. The defect lies in particular priors, not in the rule, so computable rationality should constrain priors, as computability arguments already constrain them in other respects (Lopez-Wild forthcoming; Huttegger, Walsh and Zaffora Blando 2026). The agent should simply have a prior whose conditional distributions are computable.

This paper argues that the obvious response does not take us where it seems to. My thesis has three parts.

1. **No sound general updater (Proposition 1').** No procedure that commits only to correct updates commits on every presented prior that can in fact be updated computably. The good priors cannot be recognised as good from their presentations.
2. **Representation-dependence.** Suppose conditionalization is a rule that a computable agent follows, and suppose following a rule requires a general procedure that is correct on the states it is applied to. Then whether an agent can follow the rule depends on how it represents its prior, not only on which prior it has.
3. **Noise.** There is one general format in which every computable prior over the world can be held so that the rule can be followed open-endedly. In it, each continuous source of evidence is modelled as a channel whose output, given the world, has a bounded density. Following the rule for new sources therefore requires treating continuous evidence as noisy. The noise can be arbitrarily small, and its scale can be uncertain without a lower bound.

The first part is an elementary consequence of AFR, and I present it as such. The other two are the contribution. They should surprise in two directions.
- Defenders of exact-evidence models of learning will not expect a computational fact to bear on how evidence ought to be modelled. The usual reason to model evidence as noisy is that measurement is noisy, which is an empirical fact.
- Those who hold that computability only prunes the space of acceptable priors will not expect it to make the standing of an agent depend on the form of its representation, with the credence function held fixed.

The scope is limited in three ways that I state now.
- Nothing here concerns conditionalization as an evaluative ideal, a standard against which any credal transition can be assessed whether or not anyone can meet it.
- Nothing here concerns discrete evidence, or evidence of positive probability, where the ratio formula is computable.
- The conclusions are conditional on a principle about rule-following, stated in Section 2 and defended in Section 4.

# 2. Conditionalization as a rule followed

I work in the framework of computable probability theory, which Huttegger, Walsh and Zaffora Blando (2026) recommend for modelling computationally bounded Bayesians.
- The outcome spaces are computable metric spaces, such as the reals, Cantor space, and finite products of these.
- A probability measure $P$ is *computable* if some program, on input $k$, outputs a finitely supported measure with rational weights on rational points that lies within Prokhorov distance $2^{-k}$ of $P$.
- I call such a program a *presentation* of $P$.
- A conditional distribution map for $H$ given $Y$ is *computable* if some version of it is computable, as a map from observations to measures, on a set of observations of measure one.

A computable agent, in the sense used here, holds its prior as a presentation and receives its evidence as a computable stream of approximations to the observed value. Its updating is a procedure that takes these as input.

Two readings of the conditionalization rule must be kept apart.
- **Ideal reading.** The rule is a standard: a transition from prior to posterior is correct if and only if the posterior is a version of the conditional distribution at the observed value. Whether anyone can make correct transitions is irrelevant to the standard.
- **Followed reading.** The rule is something the agent does. It updates by conditionalizing in the way someone adds by following the rule for addition, and not merely by happening to produce sums.

The followed reading is the one in play when Bayesian models are offered as accounts of how minds or machines actually learn, and when one asks what a bounded agent is required to do. I assume the following principle about it.

**FOLLOW.** A computable agent follows a diachronic rule only if its transitions are produced by a single procedure. That procedure must take the agent's representation of its current state and its evidence as input. It must be correct, by the rule's lights, on every state to which the agent applies it.

FOLLOW does not require the agent to prove anything. It requires a procedure that is general and sound on its domain. Section 4 defends it. First, the result that gives it force.

# 3. A prior no one can certify

Fix the AFR pair: computable random variables $(X, Y)$ with joint law $B$ such that $B[X \mid Y]$ is not computable on any $B_Y$-measure-one set (AFR 2019; the construction encodes the halting times of all Turing machines into the conditional distribution). Fix also any computable measure $\nu$ on the range of $X$, and a binary variable $I$.

For each Turing machine $M$, let $w_M = 2^{-n}$ if $M$ halts at step $n$, and $w_M = 0$ if $M$ never halts. Define

$$P_M = (1 - w_M)\,(\delta_0 \otimes \nu \otimes B_Y) \;+\; w_M\,(\delta_1 \otimes B)$$

on the space of triples $(I, X, Y)$.

In words: with weight $1 - w_M$ the agent thinks that $I = 0$, that $X$ is drawn from $\nu$, and that $Y$ is drawn independently from the $Y$-marginal of $B$. With weight $w_M$ it thinks that $I = 1$ and that $(X, Y)$ is drawn from $B$.

Three facts are proved in the appendix.
- **Lemma 1.** $P_M$ is computable uniformly in $M$. To approximate $w_M$ within $2^{-k}$, run $M$ for $k$ steps. Mixtures with computable weights of computable measures are computable.
- **Lemma 2.** If $w_M > 0$, then the observation has the same marginal under both components. So for almost every $y$, the conditional distribution of $(I, X)$ given $Y = y$ is $(1 - w_M)\,\delta_0 \otimes \nu + w_M\,\delta_1 \otimes B[X \mid Y = y]$. From a computable version of it one can compute a version of $B[X \mid Y]$: restrict to $I = 1$ and divide by $w_M$.
- **Proposition 1.** $P_M$ has a computable conditional distribution map if and only if $M$ never halts. If $M$ never halts, $P_M = \delta_0 \otimes \nu \otimes B_Y$, and the conditional distribution is the constant $\delta_0 \otimes \nu$. If $M$ halts, Lemma 2 and the AFR theorem exclude a computable version.

Since the set of machines that never halt is not computably enumerable, two corollaries follow.

**Proposition 1' (no sound general updater).** Call a procedure a *sound general updater* if, given a presentation of a prior, it either never commits, or commits at some finite stage to a program that computes a version of the prior's conditional distribution map. No sound general updater commits on every $P_M$ that can be updated computably. If one did, the set of $M$ on which it commits would be computably enumerable. By soundness and Proposition 1, it would be exactly the set of non-halting machines.

**Corollary 1 (no theory certifies).** Let $T$ be any consistent, computably axiomatized theory that interprets enough arithmetic. Let $M_T$ search for a proof of $0 = 1$ in $T$. Then $M_T$ never halts, so $P_{M_T}$ is the tractable prior $\delta_0 \otimes \nu \otimes B_Y$. But $T$ does not prove that the presented prior has a computable conditional distribution. If it did, it would prove that $M_T$ never halts, and so its own consistency. With $T$ = ZFC: if ZFC is consistent, the program $P_{M_{\mathrm{ZFC}}}$ presents a prior that anyone can update, and no ZFC proof shows that it can be.

**Corollary 2 (fragility).** The tractable prior $Q = \delta_0 \otimes \nu \otimes B_Y$ is the limit in total variation, as $w \to 0$, of the priors $(1 - w)\,Q + w\,(\delta_1 \otimes B)$. None of these has a computable conditional distribution. In this family, being updatable is not preserved under arbitrarily small changes of credence.

These results are elementary. They are instances of the familiar pattern by which a semantic property of programs that is not open cannot be recognised by any procedure. What is new is the use to which they are put.

# 4. Representation-dependence

## 4.1 The argument

1. **(R1) FOLLOW.** A computable agent follows conditionalization only if its updates are produced by a single sound procedure applied to its representation of its current prior and to its evidence. The procedure must be correct on every state to which it is applied.
2. **(R2)** An agent that holds a computable prior, receives continuous evidence, and can so follow conditionalization is bound by conditionalization as a followed rule.
3. **(R3)** There are two agents with the same credence function such that the first can so follow conditionalization and the second cannot.
4. **(R4)** So whether an agent is bound by conditionalization as a followed rule is not determined by its credence function alone.

The inference from R1 to R3 to R4 is valid. Its first-order skeleton was checked mechanically, together with the check that it becomes invalid when R1 is dropped. R2 is the orthodox assumption that able agents are bound. R3 is witnessed as follows.
- Let the first agent hold $Q = \delta_0 \otimes \nu \otimes B_Y$ through the obvious presentation. Its procedure reads off $\nu$ and outputs it, and that procedure is sound on all priors of this form.
- Let the second agent hold the same measure through the presentation $P_{M_{\mathrm{ZFC}}}$.

What would the second agent's general procedure be?
- The constant procedure "output $\delta_0 \otimes \nu$" produces the right posterior here. But as a general procedure applied to presentations of the form $P_M$, it is unsound: it gives the wrong answer whenever $M$ halts.
- Any procedure that is sound across the family of presentations the agent might hold must, by Proposition 1', fail to commit on some updatable member. Nothing available to the agent distinguishes its own case from those.

R4 follows. The rest of the section defends R1, since everything turns on it.

## 4.2 Why a single sound procedure

The strongest objection to R1 is that it confuses satisfying a norm with being able to show that one satisfies it.
- The second agent can run the correct update. The constant procedure is there for the taking.
- A child follows the rule for addition without being able to prove that her algorithm computes sums.
- Following a rule, on standard accounts, requires a disposition guided by the rule, not a proof.

I accept the last point, and R1 asks for no proof. What it asks for is generality. The child's disposition is not correct merely on today's sum. It is a procedure that, applied to any pair of numbers she meets, delivers their sum. That is what makes her output an instance of adding rather than a lucky guess. The second agent, by contrast, has a procedure that is correct on its current input only by accident. Applied to the presentations it could equally have held, it errs.

Why must the procedure for updating be general across *presentations*, rather than across observations for a fixed prior? Because conditionalization is diachronic. The posterior that one update produces becomes the prior that the next update takes as input. An agent that follows the rule over time must therefore apply its procedure to whatever presentations its own past updates and its other belief-forming processes deliver. It cannot fix a prior in advance and tailor a procedure to it. In this respect updating differs from state norms such as coherence. A computable presentation of a probability measure is coherent because of what it presents, and nothing has to be executed to keep it so. A diachronic rule, by contrast, has to be executed, and executing it is running a procedure on representations.

This also answers the objection that R1 proves too much. The worry is that if norms bind only those who can certify compliance, then consistency, coherence and even holding a total program would cease to bind, since none of these can be certified in general. R1 is not a certification principle for states. It is a condition on following diachronic rules, which produce new states from old ones. A computable agent is not required to verify that its presentation defines a measure, any more than a calculator is required to verify that its registers hold numbers. It is required to update by a procedure that works on the representations it will in fact have to update.

## 4.3 Same behaviour, different standing

A related objection says that the two agents behave identically. On this evidence their outputs agree at every stage, forever, so a functionalist about credal states must count them as the same.

The reply is that the relevant behaviour is dispositional and spans states. The agents agree on this input. They differ in which procedure produces the output and in what that procedure would do elsewhere. Functionalists distinguish states by their dispositional roles, not by their actual outputs on one occasion. So the result does not conflict with functionalism about the *updater*. It does conflict with the view that the credence function alone fixes the standing of an agent as a follower of conditionalization, and that is the conclusion I draw.

## 4.4 Why this is not the familiar point

Representation-dependence is familiar from logical non-omniscience. Agents who believe logically equivalent sentences can differ in what they are able to infer (Hacking 1967; Garber 1983). Mahtani (2024) argues that credences are hyperintensional in a related way, since a credence in a proposition can depend on its mode of presentation. Two differences separate the present result from these.

1. In those cases what the agent cannot reach is a further proposition, a consequence of what it believes. Here nothing is unknown about the content of the credal state: the credence function is fully given and computable. What the agent cannot reach is the executability of a norm on that content.
2. The familiar cases are open to the reply that an ideal agent would close the gap, so representation-dependence marks a lack of logical skill. Here no amount of logical skill within a consistent computably axiomatized theory closes the gap (Corollary 1). The dependence is not a shortfall from an attainable ideal. It is a structural feature of following this rule computably.

# 5. Why the rule-follower must model noise

If the good priors cannot be recognised as good, a follower of conditionalization needs a format in which goodness can be read off. One such format lies close to hand.

**Channel presentations.** Present a prior over the world-variables $H$ and an observation $Y$ by three things:
- a program for the prior $\mu$ over $H$;
- a program for a likelihood density $p(y \mid h)$ with respect to a fixed computable reference measure;
- a rational number $c$ with $p \le c$.

AFR prove that in the dominated setting with a bounded computable density, the conditional distribution map is computable (AFR 2019; the special case of additive independent noise with a bounded computable density is their Corollary 9.7). So a single procedure updates every channel presentation and is sound on all of them. It reads the bound and applies the AFR algorithm.

Channel presentations have three further properties (Lemma 3, appendix).
- **Unrestricted world prior.** Every computable prior $\mu$ over the world has a channel presentation, for instance with any fixed bounded computable noise. So the format places no constraint on what the agent believes about the world, other than about its own evidential channels.
- **Closure under mixture.** Computable mixtures of channel presentations are channel presentations: put the mixture index among the world-variables and take the maximum of the bounds. An agent can therefore be uncertain which channel model is correct without leaving the format.
- **Closure under new sources.** If a new source $Y'$ is conditionally independent of the old ones given the world and has its own bounded likelihood density, the joint likelihood is the product, which is bounded by the product of the bounds. So the posterior after any finite sequence of such observations is again updatable by the same procedure.

The argument from these facts to the noise thesis needs one more element. A competitor format stores the prior as a marginal over observations together with a computable posterior kernel, so that updating means applying the kernel. Call this an *evidence-first* format. Any prior with a computable conditional distribution has one, so evidence-first presentations are trivially certifiable. Does this undercut the case for noise? It does not, for the following reason.

1. **(N1)** An open-ended learner meets sources of evidence that it did not anticipate when its current state was formed. It incorporates each by modelling how that source's output depends on the world.
2. **(N2)** For a computable agent to follow conditionalization on such a source, there must be a sound procedure that takes the agent's current state together with its model of the source and returns a presentation that can be updated on the source's output (FOLLOW).
3. **(N3)** A model of how a source depends on the world is a conditional law of the output given the world. An evidence-first presentation of the current state does not combine with such a law to yield an evidence-first presentation of the joint: computing the new posterior kernel is precisely the inversion whose general computability is in question. So the format does not extend to new sources by a sound procedure. The same holds, by Proposition 1', for exact deterministic source models: by AFR, they include models with no computable inversion, and by Proposition 1' the good ones cannot be soundly recognised.
4. **(N4)** If the source is modelled with a bounded computable likelihood density, the extension is sound and uniform (Lemma 3).
5. **(N5)** So an open-ended computable learner can follow conditionalization, for any prior over the world, if it models its continuous sources as channels with bounded densities. Among the formats known to me, this is the one that does the job in general. A bounded density means that, given the world, the source's output is not a deterministic function of it. The source is noisy.

N5 is stated with the hedge it needs. I do not claim that no other format could do the work. I claim that the one general route known is the dominated channel. Every route discussed in the literature I have been able to consult is either discrete, and so outside the scope, or dominated.

Two refinements show that the requirement is weaker than it may sound.

**No floor on noise.** One might think a certifiable agent must be certain that its noise exceeds some fixed level, which would be a dogmatic belief about the world. It need not be. Suppose the noise is Gaussian with unknown scale $s$, and the agent's prior over $s$ on $(0, 1)$ is $\pi$. The mixed noise density is maximised at zero, where it equals $(2\pi)^{-1/2}\,\mathbb{E}_\pi[1/s]$. It is therefore bounded if and only if $\mathbb{E}_\pi[1/s] < \infty$.
- The prior with density $2s$ gives $\mathbb{E}[1/s] = 2$ and puts positive weight on every interval $(0, d)$.
- The uniform prior gives $\mathbb{E}[1/s] = \infty$.

(Both computations were checked symbolically.) What the format requires is not a floor but a tail condition: the agent may think the noise arbitrarily small, but not too probably so.

**The scale is substantive, not an approximation.** In the AFR examples the exact conditional distribution is badly discontinuous. So posteriors under channel models need not converge to anything computable as the noise shrinks. It is natural to read this as a cost: the channel model makes the posterior depend on a parameter for which there may be no fact to approach. I read it the other way. It shows that the channel model is not an approximation to an exact-evidence model that the agent is failing to compute. In the cases that matter, there is no computable target to approximate. The agent's model of its channel is part of the content of its credal state, and it is answerable to evidence about the channel like any other part.

The conclusion connects to practice. Bayesian models of perception and sensorimotor learning almost always posit a likelihood with a density, a noise model, rather than conditioning on exact values of world-variables. This is usually defended on the empirical ground that neural and physical channels are noisy. The present argument supplies a second, independent ground. A computable system that follows conditionalization open-endedly has to represent its continuous evidence this way, whatever the physics of its channels.

# 6. Further objections

**The wrong kind of reason.** The agent seems to believe its channel is noisy because that belief makes its updating followable, not because of evidence about channels. Credences adopted for convenience are not thereby rational.

The reply is that the requirement fixes a format, not a credence.
- Within the dominated class, the agent's credences about how noisy its channel is are set by evidence, and can come to favour very small noise (as the no-floor result shows).
- What the format excludes is a single class of models, deterministic exact channels, and these receive prior probability zero within it.

I concede that this exclusion is not grounded in evidence. A computable agent that follows conditionalization assigns probability zero to exact deterministic channels for reasons that concern its own capacities. This is a real cost. It is of a familiar kind, since every agent's model space is limited by its means of representation. It is also cheap, since the excluded hypotheses are ones that no physical measurement is believed to satisfy.

**The Dutch book.** By Rescorla's theorem, an agent whose evidence is exact and who updates other than by Kolmogorov conditionalization on that exact value is exposed to a diachronic Dutch book. A channel-modeller in a world with exact continuous evidence is therefore exposed.

I accept the conditional. Its antecedent requires that the agent be offered and settle bets conditional on exact real values. For a computable agent, the exact value arrives only as a convergent stream of approximations. The bookie who exploits the gap must be able to make the agent's credences depend on the limit. Whether a computable bookie can do this against a computable agent is a question the present framework raises and does not settle. I record it as an open cost.

**Digital evidence.** An agent whose evidence is the content of an input register has exact evidence, knows that it does, and should not model it as noisy. That is right, and nothing here says otherwise. Such evidence is discrete, the ratio formula applies, and conditionalization is computable. The thesis concerns continuous evidence only.

**Other certifiable routes.** There are other certifiable routes, such as exchangeable sequences, for which posteriors are computable from predictive distributions (Freer and Roy 2010). These concern discrete-valued sequences and fall outside the scope. Any general route for continuous observations that I know of runs through a bounded density.

**The evaluative ideal.** One may say that Kolmogorov conditionalization was never meant as an instruction, so none of this touches it. That is correct, and the paper does not claim otherwise. The claim concerns the rule as followed, which is the reading under which Bayesian models describe how bounded learners actually learn.

# 7. Conclusion

A computable agent's prior may be one that anybody can update, and yet the agent may be unable to follow conditionalization on it. Whether it can depends on the form in which it holds the prior. That much follows from an elementary consequence of the work of Ackerman, Freer and Roy, together with a principle about following diachronic rules. The general way out is to hold one's prior in a format where updatability can be read off. For an open-ended learner the one general format known models every continuous source of evidence as a noisy channel. The required noise can be as small as one likes and of unknown size. The lesson for Bayesian epistemology is not that exact conditionalization is wrong, but that it cannot be the rule a computable learner follows. The rule such a learner follows is conditionalization on evidence modelled as inexact.

# Appendix A. Proofs

Notation is as in Section 3. Measures are on computable metric spaces with the weak topology. The binary variable $I$ takes values in $\{0, 1\}$ with the discrete metric.

**Lemma 1.** On input $k$, run $M$ for $k$ steps, and output $2^{-n}$ if it has halted at step $n \le k$, otherwise $0$. The output is within $2^{-k}$ of $w_M$. A mixture $(1 - w)P + wQ$ of computable measures, with $w$ a computable real, is computable: approximate $P$, $Q$ and $w$ to sufficient precision and mix the finite approximations. All steps are uniform in $M$, since a program for $P_M$ is obtained from $M$ by the s-m-n theorem.

**Lemma 2.** Suppose $w = w_M > 0$. The $Y$-marginal of $\delta_0 \otimes \nu \otimes B_Y$ is $B_Y$, and so is that of $\delta_1 \otimes B$. Hence $P_{M,Y} = B_Y$. Let $\kappa(y) = (1 - w)\,\delta_0 \otimes \nu + w\,\delta_1 \otimes B[X \mid Y = y]$. For measurable $A \subseteq \{0, 1\} \times \mathcal{X}$ and $C \subseteq \mathcal{Y}$,
$$\int_C \kappa(y)(A)\, B_Y(dy) = (1 - w)\,(\delta_0 \otimes \nu)(A)\, B_Y(C) + w \int_C B[X \mid Y = y](A_1)\, B_Y(dy),$$
where $A_1 = \{x : (1, x) \in A\}$. This equals $P_M(A \times C)$. So $\kappa$ is a version of the conditional distribution, and any version agrees with it $B_Y$-almost everywhere.

Now let $\kappa'$ be a version computable on a measure-one set $S$. Let $R(\lambda)$ be the restriction of a measure $\lambda$ on $\{0, 1\} \times \mathcal{X}$ to $\{1\} \times \mathcal{X}$, scaled by $1/w$. Since $\{1\} \times \mathcal{X}$ is at distance 1 from its complement, a finite approximation within Prokhorov distance $\varepsilon < 1/2$ restricts to an approximation of $R(\lambda)$ within $\varepsilon/w$. So $y \mapsto R(\kappa'(y))$ is computable on $S$. It agrees almost everywhere with $B[X \mid Y = y]$, and redefining a version on a null set leaves it a version. This yields a version of $B[X \mid Y]$ that is computable on a measure-one set, contradicting the AFR theorem.

**Proposition 1 and 1'.** If $M$ never halts, $P_M = \delta_0 \otimes \nu \otimes B_Y$, and the constant kernel $\delta_0 \otimes \nu$ is a computable version. If $M$ halts, Lemma 2 applies. For 1': soundness gives that the commit set is contained in the set of updatable $P_M$. The hypothesis gives the converse. So the commit set equals the complement of the halting set. But the commit set is computably enumerable, and the complement of the halting set is not.

**Lemma 3.** For a channel presentation $(\mu, p, c)$, the joint law is $\mu(dh)\,p(y \mid h)\,\lambda(dy)$, with a bounded computable likelihood density. This is the dominated case with bounded computable density in which AFR prove the conditional distribution map computable. For a computable mixture $\sum_i a_i(\mu_i, p_i, c_i)$, adjoin the index $i$ to the world-variables: the prior is $\sum_i a_i\,\delta_i \otimes \mu_i$, the likelihood is $p_i(y \mid h)$, and the bound is $\max_i c_i$ (or a computable uniform bound in the countable case). For conditionally independent sources, the likelihood of $(y, y')$ is $p(y \mid h)\,p'(y' \mid h)$, bounded by $c c'$.

**Noise scale.** For Gaussian noise with scale $s$, the density at $e$ is $\varphi_s(e) = (s\sqrt{2\pi})^{-1}\exp(-e^2/2s^2)$, which is at most $\varphi_s(0)$. So the mixture density $\int \varphi_s(e)\,\pi(ds)$ has supremum $(2\pi)^{-1/2}\int s^{-1}\,\pi(ds)$.

# References

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2011. Noncomputable conditional distributions. In *Proceedings of the 26th Annual IEEE Symposium on Logic in Computer Science (LICS 2011)*.

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2017. On computability and disintegration. *Mathematical Structures in Computer Science* 27(8): 1287-1314.

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2019. On the computability of conditional probability. *Journal of the ACM* 66(3), Article 23: 1-40.

Freer, Cameron E. and Daniel M. Roy. 2010. Posterior distributions are computable from predictive distributions. In *Proceedings of the 13th International Conference on Artificial Intelligence and Statistics (AISTATS 2010)*.

Garber, Daniel. 1983. Old evidence and logical omniscience in Bayesian confirmation theory. In John Earman (ed.), *Testing Scientific Theories*, Minnesota Studies in the Philosophy of Science 10. Minneapolis: University of Minnesota Press.

Hacking, Ian. 1967. Slightly more realistic personal probability. *Philosophy of Science* 34(4): 311-325.

Huttegger, Simon M., Sean Walsh and Francesca Zaffora Blando. 2026. Bayesian convergence for computably bounded agents. *Philosophy and Phenomenological Research* 112(1): 307-324.

Kolmogorov, Andrei N. 1933. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Berlin: Springer.

Lopez-Wild, Josiah. Forthcoming. Computable Bayesian epistemology. Preprint, PhilSci-Archive 23862.

Mahtani, Anna. 2024. *The Objects of Credence*. Oxford: Oxford University Press.

Rescorla, Michael. 2018. A Dutch book theorem and converse Dutch book theorem for Kolmogorov conditionalization. *The Review of Symbolic Logic* 11(4).
