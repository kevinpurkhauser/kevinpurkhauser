---
title: "Following Conditionalization: Why Computable Credence Needs Presented Densities"
---

**Abstract.** Ackerman, Freer and Roy showed that some computable priors have conditional distributions that no algorithm can compute. The natural response is to require that a rational computable agent's prior have computable conditional distributions. I argue that this response constrains the wrong object. I construct a uniformly computable family of priors, each a mixture of two laws with continuous bounded densities. Every member can be updated computably on an exact observation, yet no single procedure updates them all. The same family can be updated by one procedure as soon as each credal state is presented together with a density for the observed quantity relative to the rest, whether that density belongs to a model of the evidence source or to the prior. I draw three consequences for conditionalization understood as a rule that a computable agent follows, rather than as an evaluative ideal:
1. Constraints on credence functions do not make the rule followable. Constraints on how credal states are represented do.
2. Following the rule is therefore relative to a format of representation.
3. In the general format known to suffice, no continuous quantity the agent may learn is represented as an exact function of the other quantities it reasons about.

The ideal reading is untouched. Indeed, posteriors on ever finer intervals converge almost surely to the exact posterior, though not at any computable rate.

# 1. Introduction

When a Bayesian agent learns that a continuous quantity took the value $y$, the learned event has probability zero, and the ratio formula is silent. The standard answer is Kolmogorov conditionalization. The new credence is given by a regular conditional distribution, a kernel $y \mapsto P[\,\cdot \mid Y = y]$ that disintegrates the prior and is fixed up to observations of measure zero. (Kolmogorov 1933 gives the measure-theoretic notion; regular versions came later.) Rescorla (2018) proves Dutch book and converse Dutch book theorems for this rule, and Rescorla (2025) extends them to scenarios where the conditioning proposition may be false.

Ackerman, Freer and Roy (2011, 2019; hereafter AFR) showed that the rule can outrun computation. There are computable random variables $X$ and $Y$ such that no version of the conditional distribution of $X$ given $Y$ is computable on a set of measure one. The natural response is that the defect lies in particular priors. On this response, computable rationality should constrain the credence function, as computability considerations already do in other respects. For instance, Lopez-Wild (2026) argues that computable probability measures are automatically countably additive. Huttegger, Walsh and Zaffora Blando (2025) work in the same framework to study convergence to the truth. On this response, the agent should hold a prior whose conditional distributions are computable.

I argue that this constrains the wrong object. The thesis has three parts.

1. **Per-prior constraints do not suffice** (Proposition 2). There is a uniformly computable family of priors with these properties:
   - each member has continuous, bounded densities;
   - each member can be updated computably on an exact observation;
   - no single procedure performs all the updates.
2. **Presented densities do suffice** (Proposition 3). The same family can be updated by a single procedure once each credal state comes with a presented density for the observed quantity relative to the other variables. The density may come from a model of the evidence source or from the prior itself. So the constraint that makes conditionalization a rule a computable agent can follow is a constraint on the *representation* of credal states, not on credence functions.
3. **No exact dependence.** In the general format known to suffice, no continuous quantity the agent may learn is represented as an exact function of the other quantities it reasons about. Exact observation is allowed. Exact functional dependence of the observed quantity on the rest is not.

The mathematics is elementary. The dependence of computability on representation is a familiar fact of computable analysis (Weihrauch 2000). Proposition 2 is a close relative of the non-computability of the Radon-Nikodym operator (Hoyrup, Rojas and Weihrauch 2012), and the positive result is AFR's theorem for the dominated case. What is new is the epistemological reading. The debate about computable Bayesian agents has treated computability as a filter on credence functions. If conditionalization is to be a rule such agents follow, the filter must act instead on the structure in which credences are held.

The scope is limited in three ways.
- Nothing here concerns conditionalization as an evaluative ideal.
- Nothing here concerns discrete evidence.
- The conclusions depend on a principle about following rules (FOLLOW), stated in Section 2 and defended in Section 4.

# 2. Framework

I work in computable probability theory.

**Spaces and measures.** Spaces are computable metric spaces, such as the reals, Cantor space, and finite products of these. Points are given by Cauchy names, that is, streams of rational approximations. A probability measure is *computable* if some program, on input $k$, outputs a finitely supported measure with rational weights on ideal points, within Prokhorov distance $2^{-k}$ of it.

**Credal states.** A credal state is a probability measure on a product $H \times Y$. Here $H$ collects the hypothesis variables, the quantities the agent reasons about, and $Y$ is an observation variable, the quantity it is about to learn. The split is part of the state.

**Formats.** A *format* is a set of finite descriptions (presentations) together with a map that assigns to each presentation the credal state it presents. Two formats will matter.
- In the *measure format* $\mathcal{M}$, a presentation is a program computing the joint law.
- In the *density format* $\mathcal{D}$, a presentation consists of three parts: a program computing a measure $\rho$ on $H$; a program computing a function $q(h, y)$, continuous and bounded by a rational $c$ that is given; and a computable atomless reference measure $\lambda$ on $Y$. The state presented is $q(h, y)\,\rho(dh)\,\lambda(dy)$, with $\int q\,d(\rho\otimes\lambda) = 1$.

  The density $q$ may arise from a prior over $H$ times a likelihood of the source (a "channel" model). It may also arise from the prior alone, when the observation is an exact report of a hypothesis variable $Z$ and the prior gives $Z$ a density given the remaining hypotheses. In that case $H$ is the remaining hypotheses and $Y$ is $Z$.

**Updating and correctness.** An *updating procedure* for a format is an oracle program. Given a presentation and a name of the observation $y$, it outputs approximations to a posterior over $H$. It is *correct* on a presentation if, for $P_Y$-almost every $y$ and every name of $y$, its output is a version of the conditional distribution at $y$. Posteriors are then computable relative to $y$, and I treat the post-update state as a presentation relative to the evidence received.

**Two readings of the rule.** On the *ideal reading*, conditionalization is a standard: the correct kernel exists whether or not anyone computes it. On the *followed reading*, it is something the agent does, as someone adds by following the rule for addition. The followed reading is in play when a Bayesian model is offered as an algorithmic-level account of how a mind or machine learns, in the sense of Marr (1982). It is also in play for systems, such as probabilistic programming systems, that actually perform the updates. It is not in play for computational-level models, which specify only what is computed.

**FOLLOW.** A computable agent follows conditionalization only if three conditions hold:
- its credal states are presented in a format $F$;
- $F$ is closed under the agent's updating and belief-forming operations, so that it contains every state the agent can come to hold;
- a single procedure is correct on every presentation in $F$ whose state can be updated computably at all.

FOLLOW asks for no proof of correctness, and it makes no demand on states that nothing could update. The closure clause matters. Without it, any state could be placed in a one-element format, and FOLLOW would exclude nothing.

# 3. The results

## 3.1 A family of tractable priors

Let $Z \in [0,1]$ and $I \in \{0,1\}$. For $n \ge 2$, let $E_n$ be the set of $z$ whose binary digits in positions $n$ to $2n$ are all $0$. This is a union of $2^{n-1}$ intervals of length $2^{-2n}$. Let $f_n$ be the continuous density that places a tent of mass $2^{-(n-1)}$ on each of them. For a Turing machine $M$, let $n_M = m + 2$ if $M$ halts at step $m$. Define the prior $\mu_M$ as follows:
- if $M$ halts, $I = 1$ with probability $w_M = 2^{-n_M}$, and otherwise $I = 0$;
- if $M$ never halts, $I = 0$ with certainty;
- given $I = 0$, $Z$ is uniform;
- given $I = 1$, $Z$ has density $f_{n_M}$.

**Lemma 1.** $\mu_M$ is computable uniformly in $M$. To approximate it within $2^{-k}$, run $M$ for $k$ steps. If it has halted, approximate the mixture to within $2^{-k-1}$. Otherwise approximate the uniform law with $I = 0$ to within $2^{-k-1}$; the total-variation error from omitting the $I = 1$ component is then at most $2^{-k-1}$.

Each $\mu_M$ is unremarkable. It is a mixture of two laws with continuous bounded densities.

## 3.2 Exact observation in the measure format

Let the agent observe $Z$ exactly. Its credal state is $\mu_M$, with $H = I$ and $Y = Z$, presented in $\mathcal{M}$. For each fixed $M$ the posterior is

$$P_M(I = 1 \mid Z = z) = \frac{w_M f_{n_M}(z)}{(1 - w_M) + w_M f_{n_M}(z)},$$

which is a computable function of $z$. So every member can be updated computably.

**Proposition 2.** No single procedure is correct on every $\mu_M$ presented in $\mathcal{M}$ with the exact observation.

*Sketch.* Suppose $U$ were correct on every member. By the recursion theorem, build a machine $M^*$ that searches for three things:
- a finite initial segment of a name of an observation, which leaves open a rational interval $K$ of possible observations;
- a finite run of $U$ on the presentation of $\mu_{M^*}$, reading only that segment;
- in that run, an output close to "$I = 0$ for certain".

If the search succeeds, $M^*$ waits and halts so late that $n_{M^*}$ satisfies two conditions: it exceeds the length of the search, and $2^{-(n-1)}$ is less than half the width of $K$.

The search must succeed. If $M^*$ never halted, $I = 0$ would be certain, and a correct $U$ would output that posterior on almost every observation, after reading a finite segment.

So $M^*$ halts. $U$'s run is a fixed finite computation, so $U$ outputs "$I = 0$, nearly certainly" on every observation in $K$. But $K$ contains a dyadic interval of length $2^{-(n-1)}$, and this contains an interval of $E_n$ whose central half has positive measure. On that half the true posterior gives $I = 1$ probability at least $2/3$. So $U$ is wrong on a set of positive measure. Details are in the appendix.

## 3.3 The same family with presented densities

**Proposition 3.** There is a single procedure correct on every presentation in $\mathcal{D}$. In particular, there is a single procedure correct on every $\mu_M$ presented in either of the following ways.
- **(a) Exact observation, density in the prior.** $\rho$ is the law of $I$, $q(i, z)$ is the density of $Z$ given $I = i$ (that is, $1$ or $f_{n_M}$), and $\lambda$ is Lebesgue measure, with bound $c = 2^{n_M + 2}$.
- **(b) Noisy observation, density in the channel.** The reading is $Y = Z + \xi$, with $\xi$ independent and having a presented bounded computable density $\varphi$, for instance a Gaussian. Here $H = (I, Z)$, $\rho = \mu_M$, and $q(h, y) = \varphi(y - z)$.

For any presentation in $\mathcal{D}$, the posterior expectation of a bounded continuous $g$ is

$$\frac{\int g(h)\,q(h, y)\,\rho(dh)}{\int q(h, y)\,\rho(dh)}.$$

Both integrals are integrals of bounded computable functions, with a known bound, against a computable measure, so they are computable relative to $y$, uniformly in the presentation. The denominator is positive for $P_Y$-almost every $y$. This is AFR's argument for the dominated case (AFR 2019, Section 9.3).

In (a), the presentation of $\mu_M$ for each $M$ is a perfectly good computable presentation. It is just not computable *from $M$*, because it reveals the halting time.

The contrast between Propositions 2 and 3 locates the obstacle. The obstacle is not exactness of the observation, since (a) is exact. It is not the prior, since the credence functions are the same throughout. It is whether the credal state is held together with a density for the observed quantity relative to the rest.

# 4. Format-relativity, and what it shows

## 4.1 The argument

1. **(F1)** FOLLOW.
2. **(F2)** A format that contains every measure-presented state with an exact observation contains the family of Proposition 2. So no single procedure is correct on it.
3. **(F3)** The density format $\mathcal{D}$ has one correct procedure (Proposition 3). It is closed under updating relative to the evidence, under finite computable mixtures (adjoin the index to $H$ and take the larger bound), and under adding observations that are conditionally independent given $H$ (multiply the densities and the bounds).
4. **(F4)** Each $\mu_M$ is presented both in $\mathcal{M}$ and in $\mathcal{D}$.
5. **(F5)** So whether an agent can follow conditionalization when it holds these credences depends on the format in which it holds them. It is not settled by the credence function.

Given FOLLOW, F5 is a short step from Propositions 2 and 3. The weight rests on FOLLOW and on what F5 is taken to show.

## 4.2 Defending FOLLOW

**The single case.** Every updatable presentation has some procedure correct on it, for example one with the answer built in. A rule, however, is followed across cases. A child follows addition because her procedure handles the numerals she may be given. An updating rule is, moreover, applied again and again to whatever states the agent's own updating produces. That is why FOLLOW requires a format closed under those operations. A procedure correct on one presentation and silent or wrong on the others the agent may come to hold is a stored answer, not an implementation of conditionalization.

**Finitude.** Actual children fail on numerals too long to process. FOLLOW is a condition on what procedure the agent runs, not on its resources. Proposition 2 is not a failure of resources: no procedure, given unlimited time, is correct across the format. Kripke (1982) warns that appeals to idealised competence can presuppose the very rule in question. The present appeal does not need dispositions. For a computing system, which procedure it runs is a fact about its architecture. The probabilistic programming systems that perform such updates are given by their code. For human learners, which procedure is run is an empirical question, and FOLLOW says what the answer must be for conditionalization to be among the rules they follow.

**The bad-format reply.** Suppose numbers were given to the child as arbitrary programs that may or may not output a numeral. We would say that the format is bad, not that addition cannot be followed. I agree, and this is the thesis. Conditionalization can be followed on a good format and not on a bad one. Proposition 2 shows that the measure format with exact observation is a bad format. Proposition 3 shows that the density format is a good one.

**Formats and agents.** An agent whose states can come in several formats follows conditionalization on the part of its state space that lies in a good format. FOLLOW's second clause says that, if it follows the rule tout court, all its states must lie there.

## 4.3 Why this is more than representation-dependence

That computability depends on representation is a platitude of computable analysis. The epistemological content lies in which object the computability constraint attaches to.

The literature on computable Bayesian agents treats computability as a constraint on credence functions: which measures an agent may have. Proposition 2 shows that such a constraint, even in the strong form "every conditional distribution is computable, and the density is continuous and bounded", does not make conditionalization followable. What does is a constraint on the structure the agent holds: a presented density, with a bound, for each quantity it may learn, relative to the others.

Two consequences follow.
- **Credal states are not just measures.** For a follower of conditionalization, the credal state includes the density through which it is held, roughly a generative model rather than a bare probability function. Two agents with the same credence function can differ in whether they follow the rule.
- **The difference from logical non-omniscience.** The familiar representation-dependence, which concerns logically equivalent beliefs that differ in what can be inferred from them (Hacking 1967; Garber 1983), and Mahtani's (2024) case that the objects of credence are hyperintensional, both locate the variation in content. Here the content is fully given and computable. What varies is whether a norm can be executed on it.

# 5. No exact dependence

The density format has a structural feature that needs stating. In a presentation in $\mathcal{D}$, the observed quantity has a bounded density, relative to an atomless reference measure, given the hypotheses. So it is not, almost surely, a function of the hypotheses.

This holds wherever the density sits.
- **Channel models.** The reading is not a function of the quantities measured. It has slack, from noise or from omitted variables.
- **Exact report of a hypothesis variable $Z$.** $Z$ is not a function of the other hypothesis variables.

Whether we call the slack "noise" or "regularity of the prior" is a matter of labelling, since the constraint falls on the joint credal state either way. The label-free statement is this: *in the general format known to suffice, no continuous quantity the agent may learn is represented as an exact function of the other quantities it reasons about.*

Three remarks fix the scope of this claim.

**It is a sufficiency claim.** I have not shown that every format with a single correct procedure excludes exact dependence. Two facts make the claim more than an artefact of the chosen format. First, by AFR there are priors with exact dependence (their $Y$ is a function of the underlying randomness) whose conditional distributions are not computable at all. So a format admitting arbitrary exact dependence contains states that no one can update. Second, by Proposition 2, dominated priors without presented densities do not help. Whether some other uniformly updatable format admits a rich class of exact dependences is an open question.

**What it costs.** The cost falls on beliefs about exact relations among learnable quantities. Scientific models contain exact constraints, such as conservation laws, which tie observable quantities together. A follower can hold such a constraint only if it does not learn every constrained quantity as a continuous observation through the same model. For instance, it may observe the quantities through readings with slack, or learn one of them only as a function of the others that it has already learned. The cost is real. Where the constrained quantities are physical magnitudes measured with instruments, it is the familiar point that readings are not exact functions of what they measure.

**Uncertainty about the slack.** One might think a follower must be certain that its slack exceeds some fixed level. It need not be. Let the noise be Gaussian with unknown scale $s$, treated as a hypothesis variable with prior density $\pi$ on $(0, 1)$. For $n$ readings, the joint density of $(s, y_1, \ldots, y_n)$ given $h$ is bounded by $(2\pi)^{-n/2}\,\pi(s)\,s^{-n}$. For $\pi(s) \propto e^{-1/s}$ this is bounded for every $n$: the supremum of $e^{-1/s}s^{-n}$ is $(n/e)^n$. So the posterior over $(h, s)$ is computable, and every interval $(0, d)$ has positive prior probability. The probability is small, of order $e^{-1/d}$, so this is a soft floor rather than none. For $\pi(s) = 2s$ the bound holds for one reading but not for two. That shows only that this sufficient condition fails, not that updating is impossible.

# 6. Objections

**Finite precision.** A computable agent never receives an exact real, only finitely many approximations. So perhaps the rule it follows is ratio conditionalization on rational intervals, which is computable and needs no densities. Two replies.

First, that is discrete evidence: the agent conditions on a report drawn from a countable set. It is right to do so only if its model of how reports arise is non-informative, that is, coarsening at random (Heitjan and Rubin 1991). It is also right only if the reported intervals have null boundaries under its prior. For priors with atoms, the probability of a closed interval need not be computable. So the interval route is a further format with its own presentation conditions, and the present thesis does not exclude it. What it does not do is follow Kolmogorov conditionalization on continuous evidence. It replaces that rule.

Second, posteriors on nested intervals shrinking to $y$ converge, for almost every $y$, to a version of the exact posterior (Lévy's upward theorem). So the exact rule remains the almost-sure limit of followable interval updates, with no computable rate of convergence in general. This is how an orthodox theorist can say the ideal governs bounded agents, and I accept it. It concerns the ideal reading. The followed rule, on continuous evidence, needs presented densities.

**From capacity to norm.** The conclusion is conditional. If conditionalization on continuous evidence is to be a rule a computable learner follows, its credal states must be held in a format such as $\mathcal{D}$. Nothing here tells an ideal reasoner what to believe.

**Total evidence and the Dutch book.** A learner in $\mathcal{D}$ conditions on exactly what it learns. In case (a), what it learns is the exact value of $Z$. It Kolmogorov-conditionalizes its own prior on that value, so Rescorla's theorems give no handle against it. What the format restricts is the shape of the prior, not the evidence conditioned on.

**The evaluative ideal.** If Kolmogorov conditionalization was never meant as an instruction, nothing here touches it.

# 7. Conclusion

The natural response to the noncomputability of conditioning constrains credence functions. Proposition 2 shows that this is not enough. A uniformly presented family of individually tractable priors, each with continuous bounded densities, defeats every single updating procedure. Proposition 3 shows what is enough: holding each credal state together with a presented density for what is to be learned, relative to the rest. Read as a rule a computable learner follows, conditionalization therefore constrains how credences are represented, not only which credences there are. In the general format known to suffice, no learnable continuous quantity is an exact function of the others. Exact conditionalization survives as an ideal, approached almost surely by followable updates. It is not, on continuous evidence, the rule a computable learner follows unless its credences come with densities.

# Appendix. Proof of Proposition 2

Suppose $U$ is correct on every $\mu_M$ presented in $\mathcal{M}$. Measures on $\{0,1\}$ are compared in total variation.

**The machine.** By the recursion theorem, let $M^*$ know its own index, and so a presentation $e^*$ of $\mu_{M^*}$. $M^*$ dovetails a search for a finite sequence $\tau$ of rationals and a halting computation of $U$ with three properties:
- $\tau$ is an initial segment of a Cauchy name, and the set $O$ of reals that have a name extending $\tau$ (an open interval, the intersection of the balls named by $\tau$) has a rational subinterval $K$ of width $r > 0$, found in the search;
- the computation runs on $e^*$ and reads only $\tau$ from the oracle;
- the computation outputs, at precision $2^{-4}$, a measure $m$ on $\{0,1\}$ with $d(m, \delta_0) < 1/8$.

If the search succeeds after $t$ steps, $M^*$ idles and halts at a step $m^*$ such that $n = m^* + 2$ satisfies $n > t$ and $2^{-(n-1)} < r/2$.

**The search succeeds.** Otherwise $M^*$ never halts, and $\mu_{M^*}$ gives $I = 0$ with certainty. A correct $U$ outputs, for almost every $z$ and every name of $z$, a measure within $1/16$ of $\delta_0$, after reading a finite segment of the name. So some $\tau$ and some computation of the kind searched for exist, and the dovetailed search finds one.

**$U$ errs.** The computation found depends only on $e^*$ and $\tau$, so $U$ outputs $m$ on every name extending $\tau$, and hence for every $z \in K$. Since $2^{-(n-1)} < r/2$, $K$ contains a dyadic interval of length $2^{-(n-1)}$, which fixes binary digits $1$ to $n-1$. Inside it, the $z$ whose digits $n$ to $2n$ are $0$ form an interval of $E_n$. On the central half of that interval $f_n \ge 2^{n+1}$, so

$$P(I = 1 \mid z) \ge \frac{2^{-n}\,2^{n+1}}{(1 - 2^{-n}) + 2^{-n}\,2^{n+1}} > \frac{2}{3}.$$

So the true posterior is at distance more than $2/3$ from $\delta_0$, and $U$'s output is wrong by more than $2/3 - 1/8 > 1/16$ on a set of positive Lebesgue measure. Since $P_Z \ge (1 - 2^{-n})\,\mathrm{Leb}$, that set also has positive $P_Z$-measure, which contradicts correctness.

# References

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2011. Noncomputable conditional distributions. In *Proceedings of the 26th Annual IEEE Symposium on Logic in Computer Science (LICS 2011)*, 107-116.

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2019. On the computability of conditional probability. *Journal of the ACM* 66(3), Article 23: 1-40.

Garber, Daniel. 1983. Old evidence and logical omniscience in Bayesian confirmation theory. In John Earman (ed.), *Testing Scientific Theories*, Minnesota Studies in the Philosophy of Science 10, 99-131. Minneapolis: University of Minnesota Press.

Hacking, Ian. 1967. Slightly more realistic personal probability. *Philosophy of Science* 34(4): 311-325.

Heitjan, Daniel F. and Donald B. Rubin. 1991. Ignorability and coarse data. *The Annals of Statistics* 19(4): 2244-2253.

Hoyrup, Mathieu, Cristóbal Rojas and Klaus Weihrauch. 2012. Computability of the Radon-Nikodym derivative. *Computability* 1(1): 3-13.

Huttegger, Simon M., Sean Walsh and Francesca Zaffora Blando. 2025. Bayesian convergence for computably bounded agents. *Philosophy and Phenomenological Research* 112(1): 307-324.

Kolmogorov, Andrei N. 1933. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Berlin: Springer.

Kripke, Saul A. 1982. *Wittgenstein on Rules and Private Language*. Cambridge, MA: Harvard University Press.

Lopez-Wild, Josiah. 2026. Computable Bayesian epistemology. *Philosophy of Science*. doi:10.1017/psa.2026.10273.

Mahtani, Anna. 2024. *The Objects of Credence*. Oxford: Oxford University Press.

Marr, David. 1982. *Vision*. San Francisco: W. H. Freeman.

Rescorla, Michael. 2018. A Dutch book theorem and converse Dutch book theorem for Kolmogorov conditionalization. *The Review of Symbolic Logic* 11(4): 705-735.

Rescorla, Michael. 2025. Non-factive Kolmogorov conditionalization. *The Review of Symbolic Logic* 18(1): 186-212.

Weihrauch, Klaus. 2000. *Computable Analysis: An Introduction*. Berlin: Springer.
