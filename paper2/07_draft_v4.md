---
title: "Following Conditionalization: Computable Agents and Inexact Evidence"
---

**Abstract.** Ackerman, Freer and Roy showed that some computable priors have conditional distributions that no algorithm can compute. The natural response is to require that rational computable agents hold priors whose conditional distributions are computable. I argue that this response is aimed at the wrong object. I construct a uniformly computable family of priors over hypotheses with these properties:
- every member can be updated computably on an exact report of one hypothesis variable;
- no single procedure updates them all;
- when the same priors are combined with a noisy report, or with a coarse report (an interval), a single procedure updates them all.

Read as a rule that a computable agent follows, rather than as an evaluative ideal, conditionalization is therefore followable only relative to a format of representation, and the decisive feature of the format is how it models evidence, not which priors it allows. I argue that an open-ended learner, one that may adopt any computable prior over its hypotheses, can follow conditionalization if it represents its continuous evidence as inexact, in either of two ways:
- as a reading with a presented likelihood density;
- as an interval.

Representing evidence as an exact point blocks the rule. The noise can be arbitrarily small, and its scale can be learned without assuming a lower bound.

# 1. Introduction

When a Bayesian agent learns that a continuous quantity took the value $y$, the event learned has probability zero and the ratio formula is silent. The standard answer is Kolmogorov conditionalization. The new credence is given by a regular conditional distribution, a kernel $y \mapsto P[\,\cdot \mid Y = y]$ that disintegrates the prior and is fixed up to observations of measure zero. (Kolmogorov 1933 gives the measure-theoretic notion of conditional probability; regular versions and disintegrations came later.) Rescorla (2018) proves Dutch book and converse Dutch book theorems for this rule, and Rescorla (2025) extends them to learning scenarios in which the conditioning proposition may be false.

Ackerman, Freer and Roy (2011, 2019; hereafter AFR) showed that the rule can outrun computation. There are computable random variables $X$ and $Y$ such that the conditional distribution of $X$ given $Y$ has no version that is computable on a set of measure one. The natural response is that the defect lies in particular priors, not in the rule. On this view, computable rationality should constrain priors, as computability considerations already do in other respects (Lopez-Wild 2026; Huttegger, Walsh and Zaffora Blando 2025). The agent should hold a prior whose conditional distributions are computable.

I argue that this response is aimed at the wrong object. The thesis has three parts.

1. **Exactness, not the prior, is the obstacle.** There is a uniformly computable family of priors over hypotheses with three properties. First, every member can be updated computably on an exact report of one hypothesis variable. Second, no single procedure performs all these updates (Proposition 2). Third, the same priors can be updated by a single procedure on a noisy report of the same variable, and on a coarse report of it (Proposition 3).
2. **Format-relativity.** If following a rule requires a single procedure that is correct across the states in the agent's format, then conditionalization is followable only relative to a format. One and the same credal state can be held in a format in which the rule can be followed and in one in which it cannot.
3. **Inexact evidence.** An open-ended learner may adopt any computable prior over its hypotheses. It can follow conditionalization if it represents each continuous source as inexact: as a reading with a presented likelihood density, or as an interval. If it admits exact point reports, it cannot follow the rule. With a density, the noise can be arbitrarily small, and its scale can be learned without a floor.

The mathematics is elementary. That the computability of an operation depends on the representation of its inputs is a familiar fact of computable analysis (Weihrauch 2000). AFR already observe that independent computable noise with a bounded density makes conditioning computable. The contribution lies elsewhere. The natural response to AFR is aimed at priors, and Proposition 2 shows that restricting priors cannot be the general repair, since the priors in the family are individually unobjectionable. What has to be restricted is how evidence is modelled. If conditionalization is the rule a computable learner follows, then exact point evidence is not something such a learner can represent.

The scope is limited in three ways.
- Nothing here concerns conditionalization as an evaluative ideal, against which any transition can be assessed whether or not anyone can meet it.
- Nothing here concerns discrete evidence.
- The conclusions depend on a principle about following rules (FOLLOW, Section 2), defended in Section 4.

# 2. Framework

I work in computable probability theory, which Huttegger, Walsh and Zaffora Blando (2025) propose as a framework for computationally bounded Bayesians. Its basic notions are these.

- **Spaces.** Outcome spaces are computable metric spaces, such as the reals, Cantor space, and finite products of these.
- **Computable measures.** A probability measure is *computable* if some program, on input $k$, outputs a finitely supported measure on ideal points, with rational weights, within Prokhorov distance $2^{-k}$ of it.
- **Presentations.** A *presentation* of a credal state is a program of this kind for the joint law of hypothesis variables $H$ and observation variables $Y$, with the split between them marked.
- **Updating procedures.** An *updating procedure* is an oracle program. Given a presentation, and the observation $y$ as an oracle (an infinite stream of approximations), it outputs approximations to a posterior over $H$.
- **Correctness.** Correctness is a property of kernels, since single observations have probability zero. A procedure is *correct* on a presentation if it computes a version of the conditional distribution map on a set of observations of measure one.
- **Updatability.** A presentation is *updatable* if some procedure is correct on it.

Posteriors are computable relative to the observation, not outright, so after updating the agent's state is a presentation relative to its evidence. Everything below relativises in this way, and I suppress the oracle where it does not matter.

The *ideal reading* of conditionalization treats the rule as a standard: the correct kernel exists whether or not anyone computes it. The *followed reading* treats it as something the agent does, in the way someone adds by following the rule for addition. The followed reading is in play when a Bayesian model is put forward as an algorithmic account of how a mind or machine learns. It is not in play when such a model specifies only what is to be computed, in Marr's computational-level sense, leaving the algorithm open. Many Bayesian models in cognitive science are offered at the computational level, and my conclusions do not touch them. They concern algorithmic-level proposals, and agents such as probabilistic programming systems that actually perform the updating.

A *format* is a class of presentations together with the way they are given. Examples are joint measures given as programs; a prior over hypotheses together with a likelihood density for each source; and a prior together with interval-valued reports.

**FOLLOW.** An agent follows conditionalization on a format $F$ only if a single procedure is correct on every updatable presentation in $F$. An agent follows conditionalization only if its credal states lie in a format on which it follows it.

FOLLOW asks for no proof of correctness. It also places no demand on presentations that are not updatable, where nothing could be correct. It asks for generality across the format.

# 3. Exact reports

## 3.1 The construction

The hypothesis variables are a bit $I$ and a real $Z \in [0,1]$, identified with its binary expansion. For $n \ge 2$, let $E_n$ be the set of $z$ whose binary digits in positions $n$ to $2n$ are all $0$. $E_n$ is a union of $2^{n-1}$ intervals of length $2^{-2n}$, with total length $2^{-(n+1)}$. Let $f_n$ be the continuous density that places, on each of these intervals, a tent of mass $2^{-(n-1)}$. For each Turing machine $M$, let $w_M = 2^{-n}$ if $M$ halts at step $n$, and $w_M = 0$ if it never halts. The prior $\mu_M$ is as follows:
- $I = 1$ with probability $w_M$;
- given $I = 0$, $Z$ is uniform on $[0,1]$;
- given $I = 1$, $Z$ has density $f_n$.

**Lemma 1.** $\mu_M$ is computable uniformly in $M$. To approximate it within $2^{-k}$, run $M$ for $k$ steps. If it has halted at some $n \le k$, approximate the mixture. Otherwise approximate the uniform law with $I = 0$; the error is at most $w_M < 2^{-k}$.

So the family $\{\mu_M\}$ is uniformly presented. Each member is an unremarkable prior: a mixture of a uniform law and a law with a continuous bounded density. Nothing about any single member is suspicious.

## 3.2 Every member can be updated, but not uniformly

Let the source report $Z$ exactly, so that the observation is $Y = Z$. Given $Y = z$, the posterior over $Z$ is the point mass at $z$, and the posterior over $I$ is given by Bayes' rule with the two densities:

$$P_M(I = 1 \mid Z = z) = \frac{w_M f_n(z)}{(1 - w_M) + w_M f_n(z)}.$$

For each fixed $M$ this is a computable function of $z$. So every $\mu_M$ is updatable on the exact report.

**Proposition 2.** No single procedure is correct on every $\mu_M$ with an exact report.

*Proof sketch* (details in the appendix). Suppose a procedure $U$ were correct on every member. By the recursion theorem, build a machine $M^*$ that searches for a finite prefix $\sigma$ of an observation on which $U$, applied to the presentation of $\mu_{M^*}$, outputs a posterior close to "$I = 0$ for certain". If the search succeeds, $M^*$ halts at a step $n$ larger than both the search time and the length of $\sigma$.

The search must succeed. If $M^*$ never halted, then $I = 0$ for certain under $\mu_{M^*}$, and a correct $U$ would output that posterior for almost every observation.

So $M^*$ halts at such an $n$. Then $U$'s finite computation on observations extending $\sigma$ is unchanged, because it saw too little of $M^*$ to tell. But on a set of positive measure inside $\sigma$ (the central parts of the intervals of $E_n$), the true posterior gives $I = 1$ probability at least $2/3$. So $U$ is wrong on a set of positive measure, which is a contradiction.

So exact evidence defeats uniform updating even on a family each of whose members is tractable, given by an ordinary presentation, and free of any noncomputable conditional distribution.

## 3.3 The same priors with inexact reports

**Proposition 3.** There is a single procedure that is correct on every $\mu_M$ combined with either of two kinds of report.
- **(a) Noisy report.** The reading is $Y = Z + \xi$, where $\xi$ is independent with a presented bounded computable density $\varphi$, for instance Gaussian with a given scale.
- **(b) Coarse report.** The reading is a rational interval $J$ containing $Z$.

For (a), the posterior expectation of a bounded continuous function $g$ of the hypotheses is

$$\frac{\int g(i, z)\,\varphi(y - z)\,\mu_M(di, dz)}{\int \varphi(y - z)\,\mu_M(di, dz)}.$$

Both integrals are integrals of bounded computable functions against a computable measure, so they are computable uniformly in the presentation of $\mu_M$. The denominator is positive for almost every $y$. This is AFR's argument for the dominated case (AFR 2019, Corollaries 9.6 and 9.7 in the journal numbering). The procedure never inspects $M$. It needs only the prior, given as a measure, and the likelihood, given as a function.

For (b), $Z$ has no atoms under any $\mu_M$, so the boundary of $J$ is null, and the probabilities needed for ratio conditionalization on $Z \in J$ are computable uniformly.

The contrast between Propositions 2 and 3 locates the obstacle. The priors are the same in both, and they are presented in the same way. What changes is only whether the evidence is modelled as an exact point. (A variant of the construction, mixing in AFR's own pair, shows more: within such a family, the presentations that can be updated at all cannot be recognised by any procedure, and for each consistent, computably axiomatized theory $T$ that interprets enough arithmetic and proves the relevant facts, there is a presentation that can be updated but that $T$ cannot show to be updatable. See Appendix B. This is not needed for the main argument.)

# 4. Format-relativity

## 4.1 The argument

1. **(F1)** FOLLOW.
2. **(F2)** In the format $J_{\mathrm{ex}}$ (priors over hypotheses given as measures, with exact point reports), no single procedure is correct on every updatable presentation, because the family $\{\mu_M\}$ lies in it (Proposition 2).
3. **(F3)** In the format $L$ (a prior over hypotheses given as a measure, with each source given by a presented bounded computable likelihood density), one procedure is correct on every presentation (Proposition 3a and Lemma 3 below).
4. **(F4)** One and the same credal state can be held in either format. For example, the joint law of $(I, Z)$ together with a reading that equals $Z$ plus independent Gaussian noise can be given as a joint measure, which places it in a format of the first kind, or as a prior together with the Gaussian likelihood, which places it in $L$.
5. **(F5)** So whether an agent can follow conditionalization on its credal state is not settled by the credal state. It depends on the format in which the state is held.

F5 follows from F1 to F4. F2 and F3 are theorems. F4 is a matter of definition. All the weight rests on F1.

## 4.2 Defending FOLLOW

**The single case.** For any updatable presentation there is some procedure correct on it, for instance one that has the answer built in. Why ask for more? Because a rule is followed across cases. A child follows the rule for addition because her procedure handles the numerals she may be given. Getting today's sum right is not enough. An updating rule is, moreover, applied again and again to whatever states the agent's own updating and belief-forming produce. A procedure that is correct on one presentation and silent or wrong on the rest of the agent's format is not an implementation of conditionalization. It is a stored answer.

**Finitude.** Actual children fail on numerals too long to process (Kripke 1982), so completeness over a format cannot be literal. FOLLOW is a condition on competence, not on performance. Proposition 2 is a failure of competence. No procedure, given unlimited time and memory, is correct across the format. A child's failure on very long numerals is a failure of performance, and it disappears with more resources.

**The bad-format reply.** Suppose numbers were given to the child as arbitrary programs, which may or may not halt with a numeral. One might say that she can still follow addition, and that the format is simply bad. I agree that the fault lies in the format. That is the thesis. The child can follow addition on a good format and cannot on a bad one. Proposition 2 shows that exact point reports form a bad format for conditionalization, and Proposition 3 shows that inexact reports form a good one.

**Capacity.** An agent whose states may come in either format can run the $L$-procedure on $L$-presentations and do what it can elsewhere. On the present view it follows conditionalization on $L$ and not on its whole format. FOLLOW ranks formats, not agents. A more expressive agent is not thereby a worse follower. It is a follower on part of what it can represent.

**The natural response done properly.** The natural response to AFR said: constrain priors. If constraining priors means constraining formats, the present view is that response done properly. But Proposition 2 shows that the constraint cannot be placed on priors over hypotheses as such, since the priors $\mu_M$ are individually tractable and jointly fine once evidence is inexact. It has to be placed on the model of evidence.

**Representation-dependence elsewhere.** Representation-dependence is familiar from the literature on logical non-omniscience (Hacking 1967; Garber 1983). Agents with logically equivalent beliefs can differ in what they can infer. Mahtani (2024) argues that the objects of credence are hyperintensional. The present phenomenon is closer to the computable-analysis one. The credal state is fully given, and nothing about its content is hidden. What varies with the format is whether a norm can be executed on it. The novelty is not the phenomenon but where it bites: on the rule that is supposed to define Bayesian learning, and on the representation of evidence rather than of belief.

# 5. Inexact evidence

## 5.1 The likelihood format

**Lemma 3.** The format $L$ has five properties.
- **One correct procedure.** A single procedure is correct on every presentation in $L$, relative to the observation (Proposition 3a).
- **Any prior.** Every computable prior over hypotheses appears in $L$, with any presented bounded computable noise.
- **Mixtures.** $L$ is closed under finite computable mixtures: adjoin the index to the hypotheses and take the largest bound. It is closed under countable mixtures only with a uniform bound.
- **New sources.** $L$ is closed under adding sources that are conditionally independent given the hypotheses. The joint likelihood is the product, bounded by the product of the bounds.
- **Joint densities.** The same ratio-of-integrals argument applies whenever the joint law has a presented bounded computable density with respect to the prior times a computable reference measure.

The density must be non-degenerate with respect to an atomless reference measure. Then a source with a density given the hypotheses is one whose reading is not a function of them: the reading has *slack* relative to the hypotheses. I call such a source inexact rather than noisy. The slack may come from measurement noise, from variables the agent has left out of its hypotheses, or from a deliberately coarse model.

## 5.2 The argument

1. **(N1)** An open-ended learner may adopt any computable prior over its hypotheses, and it incorporates new continuous sources by modelling how their readings depend on the hypotheses.
2. **(N2)** By FOLLOW, it follows conditionalization only if its credal states lie in a format on which a single procedure is correct.
3. **(N3)** If its format admits exact point reports of hypothesis variables, then, its priors being unrestricted, the format contains the family of Proposition 2. So no single procedure is correct on it.
4. **(N4)** If its format represents continuous sources either by presented bounded likelihood densities or by interval reports, a single procedure is correct on it, whatever its priors over hypotheses (Proposition 3, Lemma 3).
5. **(N5)** So an open-ended learner can follow conditionalization if it represents continuous evidence as inexact in one of these ways, and cannot if it admits exact point reports.

N5 is a sufficiency claim and a failure claim. It is not a claim of necessity. Other inexact formats may serve, for example likelihoods with an observation-dependent bound, or exchangeable sources given by their predictive distributions (Freer and Roy 2010). But the format that fails is exactly the exact-evidence model that the natural response left untouched.

## 5.3 Slack in the channel, slack in the prior

Exact reports can be followed if the prior is restricted. An exact report of $Z$ can be followed if the prior gives $Z$ a presented bounded density given the other hypotheses. The family $\{\mu_M\}$ violates this only because its densities are not presented uniformly. So the slack the rule needs can sit in the model of the source or in the prior over the hypotheses.

One might object that the difference is a matter of labelling. The distinction I need is between the variables that are targets of learning and the readings. With the slack in the channel, the agent's credences over its targets are unrestricted, and only the model of how readings depend on them is constrained. With the slack in the prior, the credences over the targets themselves are constrained. In particular, the agent may not be certain that the reported quantity is an exact function of other quantities it is learning about. The joint credence is constrained either way. What differs is which part bears the constraint. For an agent whose priors over its targets are meant to answer only to evidence, the channel is the better place.

## 5.4 Two refinements

**No floor on noise, and the scale can be learned.** One might think a follower must be certain that its noise exceeds some fixed level. Let the noise be Gaussian with unknown scale $s$, treated as a further hypothesis variable with prior $\pi$ on $(0, 1)$. For $n$ readings, the joint density of $(s, y_1, \ldots, y_n)$ given $h$ is $\pi(s)\prod_i \varphi_s(y_i - h)$, which is at most $(2\pi)^{-n/2}\,\pi(s)\,s^{-n}$.
- For $\pi(s) \propto e^{-1/s}$, $\pi(s)\,s^{-n}$ is bounded on $(0, 1)$ for every $n$. By the joint-density clause of Lemma 3, the posterior over $(h, s)$ is then computable after any number of readings, although every interval $(0, d)$ has positive prior probability. The agent can be unsure how small its noise is and learn about it.
- The prior $\pi(s) = 2s$ shows that the tail matters. It gives a bounded density for one reading but not for two.

**The scale is substantive.** In one of AFR's constructions the exact conditional distribution is discontinuous on a set of measure one. AFR also remark that conditional distributions given continuous observations cannot in general be approximated uniformly by shrinking the noise. So the noise model is not, in general, an approximation to an exact target that the agent fails to compute. The agent's model of its channel is part of the content of its credal state, and it answers to evidence like any other part, as the learnability of $s$ shows.

# 6. Objections

**Finite precision.** A computable agent never receives an exact real. It receives finitely many approximations, that is, an interval. Is the followed rule then just ratio conditionalization on intervals, which makes noise unnecessary? Yes, this is one of the two inexact formats of N4, and the thesis welcomes it. A real-time learner that conditionalizes on the interval it has received represents its evidence as coarse, not as a point. What it cannot do, if it is to follow conditionalization across its format, is treat the limit of its intervals as an exact point to be conditioned on. Defenders of exact conditionalization may agree that bounded agents do something like this. The present result says why they must, and why exact conditionalization is not even the rule they approximate in a uniform way.

**From capacity to norm.** The conclusion is conditional. If conditionalization is to be a rule that a computable learner follows open-endedly, then the learner must represent continuous evidence as inexact. This does not tell an ideal reasoner with exact evidence to doubt it. It says what the followed rule can be. Exact deterministic source models are excluded from the inexact formats, and this exclusion is not grounded in evidence. That is a cost. It is the same kind of cost as the limits any representational system places on its hypotheses, and it can be reduced by placing the slack in the prior instead (Section 5.3). Scientific models do contain exact constraints, such as conservation laws. On the present view they have to be carried by the prior over hypotheses, not by the model of how readings arise.

**Total evidence.** The inexact learner still conditions on everything it receives: its reading, or its interval. What it does not assume is that the reading is a deterministic function of the hypotheses.

**The Dutch book.** Rescorla's theorems concern departures from Kolmogorov conditionalization of the agent's own prior. The inexact learner does not depart from it. It conditionalizes its own prior, channel model included, on what it learns. So the theorems do not expose it. Meehan and Zhang (2022) show that Kolmogorov conditionalizers can be Dutch booked if and only if they are evidentially uncertain. The inexact learner, conditioning on its reading with a proper version, gives the learned reading probability one, so by their criterion, as I understand it, it is not exposed either. If its evidence is in fact exact, its credences are inaccurate in a respect it cannot represent. That is a cost in accuracy, not in coherence.

**Digital evidence.** An agent whose evidence is the content of an input register has exact discrete evidence. The ratio formula applies, and nothing here bears on it.

**The evaluative ideal.** Kolmogorov conditionalization may never have been meant as an instruction. If so, it is untouched. The claim concerns the rule as followed.

# 7. Conclusion

The natural response to the noncomputability of conditioning constrains priors. Proposition 2 shows that this response is aimed at the wrong object. A family of individually tractable priors over hypotheses defeats any single updating procedure when evidence is modelled as an exact point, and yields to a single procedure when the same evidence is modelled as noisy or coarse. Read as a rule a computable learner follows, conditionalization is followable only relative to a format, and the format it needs is one in which continuous evidence is inexact. The slack can be arbitrarily small, its size can be uncertain and learned, and it can sit in the model of the source or, at a cost, in the prior. Exact conditionalization survives as an ideal. It is not the rule an open-ended computable learner follows.

# Appendix A. Proofs

**Lemma 1.** Run $M$ for $k$ steps. If it halted at some $n \le k$, output an approximation to $\mu_M$ within $2^{-k-1}$; this is possible because $f_n$ is computable. Otherwise output an approximation within $2^{-k-1}$ of $\delta_0 \otimes \mathrm{Leb}$. The total-variation error from ignoring the $I = 1$ component is $w_M < 2^{-k}$. This bounds the Prokhorov error, and everything is uniform in $M$ by the s-m-n theorem.

**Proposition 2.** Suppose $U$ is correct on every $\mu_M$ with the exact report. By the recursion theorem, let $M^*$ know its own index, and so a presentation $e^*$ of $\mu_{M^*}$. $M^*$ dovetails a search for a finite string $\sigma$ and a halting computation of $U$ that does three things: it runs on $e^*$; it reads only $\sigma$ from the oracle; and it outputs, at precision $2^{-4}$, a measure $m$ on $I$ with $d(m, \delta_0) < 1/8$. If the search succeeds after $t$ steps, $M^*$ continues idly and halts at step $n = \max(t, |\sigma| + 1) + 1$.

*The search succeeds.* Otherwise $M^*$ never halts, $w_{M^*} = 0$, and the true posterior is $\delta_0$ for almost every $z$. A correct $U$ then outputs, for almost every $z$, a measure within $1/16$ of $\delta_0$, and its computation reads a finite prefix of $z$. So some $\sigma$ and computation of the kind searched for exist, and dovetailing finds one.

*The computation is genuine.* The computation found was carried out within $M^*$'s first $t$ steps. Any simulation of $M^*$ inside it covers fewer than $t$ steps, in which $M^*$ has not halted. Since the computation reads only $e^*$ and $\sigma$, it is $U$'s actual computation on $e^*$ for every $z \in [\sigma]$.

*It is wrong.* Since $n - 1 \ge |\sigma|$, the digits of $z$ in positions $n$ to $2n$ are free inside $[\sigma]$. So $[\sigma]$ contains whole intervals of $E_n$, and the central halves of these intervals have positive measure. On them $f_n \ge 2^{n+1}$, so

$$P(I = 1 \mid z) \ge \frac{2^{-n}\,2^{n+1}}{1 + 2^{-n}\,2^{n+1}} = \frac{2}{3}.$$

The distance from $\delta_0$ is then at least $2/3$, while $d(m, \delta_0) < 1/8$. So $U$'s output at precision $2^{-4}$ is off by more than $1/16$ on a set of positive $P_Y$-measure, which contradicts correctness.

**Proposition 3 and Lemma 3.** The posterior expectation of a bounded continuous $g$ is a ratio of integrals of the bounded computable functions $g \cdot q(\cdot, y)$ and $q(\cdot, y)$ against the computable prior, where $q$ is the presented density with its bound. These integrals are computable relative to $y$, uniformly in the presentation and the bound. The denominator is positive for $P_Y$-almost every $y$. For the noise-scale case, $\sup_{0<s<1} e^{-1/s}\,s^{-n} = (n/e)^n$, attained at $s = 1/n$, and the density extends continuously by $0$ to $s = 0$.

# Appendix B. Non-recognisability

Let $B$ be an AFR pair $(X, Y)$, with no version of $B[X \mid Y]$ computable on a measure-one set. Let $\nu$ be a computable measure, and $I'$ a further bit. Define $P_M = (1 - w_M)(\delta_0 \otimes \nu \otimes B_Y) + w_M(\delta_1 \otimes B)$. Both components have $Y$-marginal $B_Y$.

- If $M$ never halts, $P_M$ has the computable constant kernel $\delta_0 \otimes \nu$.
- If $M$ halts, then restricting a computable version to $I' = 1$ and renormalising would yield a computable version of $B[X \mid Y]$. So $P_M$ is not updatable.

Hence the set of $M$ with $P_M$ updatable is the complement of the halting set, which is not computably enumerable. So no procedure that commits only to correct kernels commits on all the updatable members.

Now let $T$ be consistent, computably axiomatized, able to interpret arithmetic, and able to prove these facts. Let $M_T$ search for a proof of $0 = 1$ in $T$. Then $P_{M_T}$ is updatable, but $T$ cannot prove that it is. If it could, it would prove that $M_T$ never halts, that is, $\mathrm{Con}(T)$, which Gödel's second incompleteness theorem rules out.

# References

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2011. Noncomputable conditional distributions. In *Proceedings of the 26th Annual IEEE Symposium on Logic in Computer Science (LICS 2011)*, 107-116.

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2019. On the computability of conditional probability. *Journal of the ACM* 66(3), Article 23: 1-40.

Freer, Cameron E. and Daniel M. Roy. 2010. Posterior distributions are computable from predictive distributions. In *Proceedings of the 13th International Conference on Artificial Intelligence and Statistics (AISTATS 2010)*, PMLR 9: 233-240.

Garber, Daniel. 1983. Old evidence and logical omniscience in Bayesian confirmation theory. In John Earman (ed.), *Testing Scientific Theories*, Minnesota Studies in the Philosophy of Science 10, 99-131. Minneapolis: University of Minnesota Press.

Hacking, Ian. 1967. Slightly more realistic personal probability. *Philosophy of Science* 34(4): 311-325.

Huttegger, Simon M., Sean Walsh and Francesca Zaffora Blando. 2025. Bayesian convergence for computably bounded agents. *Philosophy and Phenomenological Research* 112(1): 307-324.

Kolmogorov, Andrei N. 1933. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Berlin: Springer.

Kripke, Saul A. 1982. *Wittgenstein on Rules and Private Language*. Cambridge, MA: Harvard University Press.

Lopez-Wild, Josiah. 2026. Computable Bayesian epistemology. *Philosophy of Science*. doi:10.1017/psa.2026.10273.

Mahtani, Anna. 2024. *The Objects of Credence*. Oxford: Oxford University Press.

Meehan, Alexander and Snow Zhang. 2022. Kolmogorov conditionalizers can be Dutch booked (if and only if they are evidentially uncertain). *The Review of Symbolic Logic* 15(3): 722-757.

Rescorla, Michael. 2018. A Dutch book theorem and converse Dutch book theorem for Kolmogorov conditionalization. *The Review of Symbolic Logic* 11(4): 705-735.

Rescorla, Michael. 2025. Non-factive Kolmogorov conditionalization. *The Review of Symbolic Logic* 18(1): 186-. doi:10.1017/S1755020323000345.

Weihrauch, Klaus. 2000. *Computable Analysis: An Introduction*. Berlin: Springer.
