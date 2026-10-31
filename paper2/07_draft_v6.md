---
title: "Following Conditionalization: Computability Constrains Spaces of Credences, Not Credences"
---

**Abstract.** Ackerman, Freer and Roy showed that some computable priors have conditional distributions that no algorithm can compute. One natural response is that a rational computable agent must hold a prior whose conditional distributions are computable. I show that for an agent who may come to hold priors it did not have in advance, by adopting models, mixing hypotheses or accepting testimony, this per-prior requirement does not make conditionalization a rule the agent can follow. I construct a uniformly computable family of priors with three properties:
- each member is a mixture of laws with continuous bounded densities;
- each member has a continuous, computable posterior on an exact observation;
- no single procedure updates them all.

A single procedure becomes available once there is uniform information about regularity, which can come from any of three places:
- a restriction of the admissible priors to a class with fixed regularity constants;
- regularity data presented along with each prior;
- a model of the evidence source with a bounded density.

The lesson is that, read as a rule that a computable agent follows, conditionalization constrains the space of credal states the agent can reach, not credence functions one at a time. Whether holding a given credence function is compatible with following the rule depends on which other credence functions the agent could have held. Exact conditionalization as an evaluative ideal is untouched.

# 1. Introduction

When a Bayesian agent learns that a continuous quantity took the value $y$, the learned event has probability zero and the ratio formula is silent. The standard answer is Kolmogorov conditionalization. The new credence is given by a regular conditional distribution, a kernel $y \mapsto P[\,\cdot \mid Y = y]$ that disintegrates the prior and is fixed up to a set of observations of measure zero. (Kolmogorov 1933 gives the measure-theoretic notion of conditional probability; regular versions came later.) Rescorla (2018) proves Dutch book and converse Dutch book theorems for this rule, and Rescorla (2025) extends them to scenarios in which the conditioning proposition may be false.

Ackerman, Freer and Roy (2011, 2019; hereafter AFR) showed that the rule can outrun computation. There are computable random variables $X$ and $Y$ such that the conditional distribution of $X$ given $Y$ is not computable on any set of measure one. Computability has also been used to constrain credence functions in other respects. Lopez-Wild (2026) shows that, on countably generated spaces, there are no computable merely finitely additive probability measures. Huttegger, Walsh and Zaffora Blando (2025) study convergence to the truth for computable priors. Against this background a natural response to AFR suggests itself: a rational computable agent must hold a prior whose conditional distributions are computable. I call this the *per-prior response*. I treat it as a position one might hold, not one I attribute to these authors.

My thesis concerns conditionalization read as a rule that a computable agent follows. In outline:

1. **The per-prior response is insufficient for open agents.** An agent may come to hold priors it did not have in advance. If it can adopt priors from a class that includes the family constructed below, then no single procedure updates every state it can reach, although every such state satisfies the per-prior requirement (Proposition 2).
2. **Uniform regularity is what suffices.** A single procedure exists when the agent has uniform information about how regular its states are. That information can come from a class restriction with fixed constants (Proposition 4), from regularity data presented with each state, or from a regular model of the evidence source (Proposition 3).
3. **The constraint is global.** Computability, so understood, constrains the space of credal states the agent can reach, not individual credence functions. Every member of the family is unobjectionable on its own. Whether an agent may hold one of them while following conditionalization depends on what else it could have held.

The mathematics is elementary. Proposition 2 is a short diagonal argument. It is a close relative of the non-computability of the Radon-Nikodym operator (Hoyrup, Rojas and Weihrauch 2012), and of AFR's own results on the discontinuity of conditioning. The positive results apply AFR's theorem for bounded densities. Practitioners of probabilistic programming already condition on continuous data through likelihood densities (Shan and Ramsey 2017 build such densities by symbolic disintegration). What is new is the epistemological claim: computability bears on rational credence through properties of spaces of credal states.

The scope is limited in three ways.
- Nothing here concerns conditionalization as an evaluative ideal.
- Nothing here concerns discrete evidence.
- For an agent with one fixed prior that changes only by conditionalization, nothing here goes beyond the per-prior requirement (Section 4.2).

# 2. Framework

I work in computable probability theory.

**Spaces and computable measures.** Spaces are computable metric spaces. A point is given by a Cauchy name, a sequence of rationals $q_1, q_2, \ldots$ with $|q_i - x| < 2^{-i}$. A probability measure is *computable* if some program, on input $k$, outputs a finitely supported measure with rational weights on rational points within Prokhorov distance $2^{-k}$ of it. Such a program is a *measure presentation*.

**Credal states.** A credal state is a measure on $H \times Y$, where $H$ collects the hypothesis variables and $Y$ is the observation the agent is about to learn.

**Updating procedures and correctness.** An *updating procedure* is an oracle program. Given a presentation of a credal state and a name of $y$, it outputs approximations to a posterior over $H$. It is *correct* on a state if there is a version $\kappa$ of the conditional distribution such that, for $P_Y$-almost every $y$ and every name of $y$, the procedure's output is $\kappa(y)$. A state is *updatable* if some procedure is correct on it. Posteriors are computable relative to the observation, so the state after updating is presented relative to the evidence received.

**Two readings of the rule.** On the *ideal reading*, conditionalization is a standard: the correct kernel exists whether or not anyone computes it. On the *followed reading*, it is something the agent does, as someone adds by following the rule for addition. The followed reading is in play when a Bayesian model is offered as an algorithmic-level account of how a mind or machine learns, in the sense of Marr (1982), and for systems that actually perform the updates. It is not in play for computational-level models.

**Operations and reachable states.** Let an agent's *operations* be the ways its credal state can change. I consider three:
- **(U)** updating on an observation;
- **(A)** adopting a prior from a class $\mathcal{C}$ of measure presentations, for instance a model built from data or received from another agent;
- **(X)** forming finite or countable mixtures, with computable weights, of uniformly presented states it can hold, for instance to represent uncertainty about which of several models is right.

The *reachable states* are those obtainable from the agent's initial state by these operations.

**FOLLOW.** A computable agent follows conditionalization only if a single procedure is correct on every reachable state that is updatable.

FOLLOW asks for no proof of correctness, and it places no demand on states that no procedure could update. It quantifies over reachable states because the rule is applied to whatever states the agent's operations produce. That is why a procedure correct on one prior, and silent or wrong on priors the agent could equally come to hold, does not count as following the rule.

# 3. The family

## 3.1 Construction

Let $Z \in [0,1]$ and $I \in \{0,1\}$. For $n \ge 2$, let $E_n$ be the set of $z$ whose binary digits in positions $n$ to $2n$ are all $0$. $E_n$ is a union of $2^{n-1}$ intervals of length $2^{-2n}$. Let $f_n$ be the continuous density that places a tent of mass $2^{-(n-1)}$ on each of these intervals. Its peak height is $2^{n+2}$, and it is at least $2^{n+1}$ on the central half of each interval. Let $A = \delta_0 \otimes \mathrm{Leb}$ and $B_n = \delta_1 \otimes f_n\,\mathrm{Leb}$, both uniformly computable in $n$.

For a Turing machine $M$, define $\mu_M$ as follows.
- If $M$ halts at step $m$, let $n = m + 2$ and $\mu_M = (1 - 2^{-n})A + 2^{-n}B_n$.
- If $M$ never halts, $\mu_M = A$.

Equivalently, $\mu_M$ is a countable mixture $\sum_n p_n(M)\,B_n + \big(1 - \sum_n p_n(M)\big)A$, where $p_n(M) = 2^{-n}$ if $M$ halts at step $n - 2$ and $p_n(M) = 0$ otherwise. These weights are computable uniformly in $M$.

**Lemma 1.** $\mu_M$ is computable uniformly in $M$. To approximate it within $2^{-k}$, run $M$ for $k$ steps. If $M$ has halted, approximate the mixture within $2^{-k-1}$. Otherwise approximate $A$ within $2^{-k-1}$. In that case the omitted weight is at most $2^{-k-3}$, and total variation bounds the Prokhorov distance.

## 3.2 Every member is tractable, but no procedure handles them all

Let the agent observe $Z$ exactly, so that $H = I$ and $Y = Z$. For each $M$ the posterior is

$$P_M(I = 1 \mid Z = z) = \frac{2^{-n} f_n(z)}{(1 - 2^{-n}) + 2^{-n} f_n(z)}$$

if $M$ halts, and $0$ otherwise. In either case it is a continuous and computable function of $z$. So every $\mu_M$ satisfies the per-prior requirement.

**Proposition 2.** No single procedure is correct on every $\mu_M$ given by its measure presentation.

*Sketch.* Suppose $U$ were correct on every member. By the recursion theorem, build a machine $M^*$ that searches for a finite segment of a name of an observation that leaves a rational interval $K \subseteq [0,1]$ of possible values, together with a finite run of $U$ on the presentation of $\mu_{M^*}$ that reads only that segment and outputs a posterior within $1/8$ of "$I = 0$ for certain".

The search must succeed. If $M^*$ never halted, $I = 0$ would be certain, and a correct $U$ would output that posterior on almost every observation after reading a finite segment.

When the search succeeds, $M^*$ halts late enough that $2^{-(n-1)}$ is less than half the width of $K$. $U$'s run is a fixed finite computation, so it gives the same output on every observation in $K$. But $K$ contains an interval of $E_n$ whose central half has positive measure, and there the true posterior gives $I = 1$ probability greater than $2/3$. So $U$ is wrong on a set of positive measure. The appendix gives the details.

Two features of the family matter.
- Each member is built from the two most innocent laws there are: a uniform law, and a comb of tents.
- The family arises by operation (X) alone, from the uniformly presented components $A$ and $B_n$ with uniformly computable weights. So an agent that can form countable computable mixtures of states it can hold has the whole family among its reachable states. The same holds for an agent that can adopt arbitrary measure-presented priors with continuous bounded densities.

# 4. Three sources of uniformity

## 4.1 The positive results

What defeats $U$ is the absence of a uniform modulus. The densities $f_n$ have peak heights $2^{n+2}$ and Lipschitz constants that grow without bound in $n$. Nothing in the measure presentation of $\mu_M$ reveals which $n$ is in play. Each of the following three ways of supplying uniform regularity yields a single procedure.

**Proposition 3.**
- **(a) Presented regularity data.** Suppose each state is presented as a measure $\rho$ on $H$ together with a computable function $q(h, y)$, a rational bound $c \ge q$, and a computable atomless reference measure $\lambda$ on $Y$, so that the state is $q\,\rho \otimes \lambda$. Then one procedure is correct on every such presentation. The posterior expectation of a bounded continuous $g$ is $\int g q(\cdot, y)\,d\rho \,/\, \int q(\cdot, y)\,d\rho$. Both integrals involve bounded computable functions with a known bound, so they are computable relative to $y$, uniformly in the presentation. The denominator is positive for $P_Y$-almost every $y$. This is AFR's dominated-case argument (AFR 2019, Section 9).
- **(b) A regular model of the evidence source.** Suppose the reading is $Y = Z + \xi$, with $\xi$ independent and having a fixed, presented, bounded computable density $\varphi$. With $H = (I, Z)$, $\rho = \mu_M$ given only by its measure presentation, and $q(h, y) = \varphi(y - z)$, case (a) applies. This presentation is computable uniformly in $M$. So one procedure updates every member of the family of Proposition 2, on the noisy reading. This is AFR's noisy-observation result.

**Proposition 4 (fixed regularity constants).** Fix $C$ and $L$. Let $\mathcal{C}_{C,L}$ be the class of measures on $H \times [0,1]$ that have a density $q(h, y)$ with respect to $\rho \otimes \mathrm{Leb}$ satisfying $q \le C$ and $|q(h, y) - q(h, y')| \le L|y - y'|$, with $\rho$ the $H$-marginal. Then one procedure, given only measure presentations, is correct on every member of $\mathcal{C}_{C,L}$.

*Sketch.* For a ball $B$ of radius $\varepsilon$ around $y$, the probability that $Y$ lies within $\delta$ of the boundary of $B$ is at most $4C\delta$. So $P(g(H);\, Y \in B)$ and $P(Y \in B)$ are computable from the measure presentation, uniformly given $C$. By the Lipschitz bound, $P(g(H);\, Y \in B)/(2\varepsilon)$ differs from $\int g\,q(\cdot, y)\,d\rho$ by at most $\|g\| L\varepsilon$, and $P(Y \in B)/(2\varepsilon)$ differs from $p(y) = \int q(\cdot, y)\,d\rho$ by at most $L\varepsilon$. Where $p(y) > 0$, which holds $P_Y$-almost surely, a positive lower bound on $p(y)$ can be found from these approximations. The ratio then converges at a rate computable from $C$, $L$ and that bound.

The family of Proposition 2 lies in no single class $\mathcal{C}_{C,L}$. The Lipschitz constant of the $I = 1$ part, $2^{-n}f_n$, grows like $2^{2n}$.

## 4.2 What the results show

Combining FOLLOW with Propositions 2 to 4 gives the argument.

1. **(G1)** FOLLOW.
2. **(G2)** If an agent's operations put the family $\{\mu_M\}$ among its reachable states, which (X) does, as does (A) for any class $\mathcal{C}$ that contains the family, then no single procedure is correct on every reachable updatable state (Proposition 2). So such an agent does not follow conditionalization, although every state it can reach satisfies the per-prior requirement.
3. **(G3)** If the agent's reachable states all lie in a class with uniform regularity information, a single procedure exists (Propositions 3 and 4). The information can come from fixed constants, from presented data, or from a regular source model.
4. **(G4)** So whether an agent follows conditionalization is settled by which states it can reach, not by the credence function it currently has. The same credence function, for instance $\mu_{M_0}$ for a halting $M_0$, is compatible with following the rule for an agent confined to some $\mathcal{C}_{C,L}$ that contains it. It is not compatible for an agent whose operations reach the whole family.

G4 is the thesis. It needs FOLLOW, which quantifies over reachable states, and the propositions.

**The fixed-prior agent.** One might object that the inputs to conditionalization are pieces of evidence, not priors. A program that computes the kernel of a fixed prior is then a single procedure that handles every case, as an adding machine handles every pair of numbers. For an agent whose prior is fixed and changes only by (U), I agree. Its reachable states are the iterated posteriors of one prior, and FOLLOW asks only that these be computable relative to the evidence. That is the per-prior requirement, and nothing here goes beyond it.

The thesis concerns agents that also adopt and mix. A great deal of real learning is of that kind: forming a model from data, accepting a model from another agent, extending one's hypotheses when one becomes aware of new possibilities, or representing uncertainty among models as a mixture. For such agents the prior sits in the argument place of the updating procedure, because the procedure must run on priors the agent did not have when the procedure was fixed. A stored kernel for one prior is then exactly what is not enough.

**Why the operations matter.** Without a list of operations, FOLLOW could be trivialised. A format that stores a kernel with each state is closed under updating. But it is not closed under (X): re-weighting the components of a mixture requires the component densities of the observation, which a stored kernel does not provide. Proposition 2's family is itself a computable countable mixture of trivially updatable components. Which operations an agent has is a fact about its architecture, or, for human learners, an empirical question. FOLLOW says what must be true of the reachable space if conditionalization is to be among the rules the agent follows.

**Finitude.** Kripke (1982) warns that appeals to idealised competence can presuppose the rule in question. FOLLOW does not rely on dispositions. For an engineered system, which procedure runs is fixed by its code. For human learners the matter is left open here. Proposition 2 is not a failure of resources: no procedure, given unlimited time, is correct across the family.

## 4.3 Why "spaces of credences, not credences"

The per-prior response treats computability as a property of each credence function. Proposition 2 shows that this property, even in a strong form (continuous, bounded densities and a continuous computable posterior), is compatible with failure to follow the rule. Propositions 3 and 4 show what is needed: uniformity across the reachable space.

Three consequences follow.

**Admissibility is not intrinsic.** Whether an agent may hold $\mu_{M_0}$ while following conditionalization depends on the other credence functions it could have held. This is a kind of holism about rational credence that is new to this debate. It resembles the dependence of computability on representation familiar from computable analysis (Weihrauch 2000). It differs from the dependence of credence on modes of presentation (Mahtani 2024) and from logical non-omniscience (Hacking 1967; Garber 1983). In those cases what varies is content, or what can be inferred from it. Here what varies is the space the content belongs to.

**The orthodox constraint can be done properly.** A theorist who wants computability to constrain credence functions can have Proposition 4: restrict the admissible credence functions to a class with fixed regularity constants. That is a constraint on credence functions, but on all of them at once. It cannot be stated for one prior in isolation.

**The three routes differ in cost.**
- Fixed constants restrict which priors the agent may adopt.
- Presented data require the agent to obtain regularity information along with each prior. In Proposition 2's family that information encodes the halting time, so it cannot always be derived from the prior.
- A regular source model leaves the priors over hypotheses unrestricted and needs no extra information about them. The price is that the evidence is a reading with slack relative to the hypotheses.

For an agent that must be able to adopt any measure-presented prior, only the third route among these is available. That gives a computational reason, independent of physics, to model continuous evidence sources as regular channels. It is a reason only for such agents, and only among the known routes.

# 5. Objections

**Finite precision.** A computable agent never receives an exact real. Perhaps the rule it follows is ratio conditionalization on the rational intervals it receives. That is discrete evidence. It is correct if the agent's model of how intervals are reported is ignorable, for example under coarsening at random (Heitjan and Rubin 1991). It is computable if the intervals have null boundaries under the prior; for priors with atoms, the probability of a closed interval need not be computable. So this is a further route with its own conditions, and it replaces Kolmogorov conditionalization rather than following it.

Along a fixed nested partition, such as the dyadic intervals containing $y$, these posteriors converge almost surely to a version of the exact posterior (Lévy's upward theorem). This is how an orthodox theorist can say the ideal governs bounded agents, and I accept it. It concerns the ideal reading.

**From capacity to norm.** The conclusion is conditional. If conditionalization is to be a rule that an adopting and mixing computable learner follows, then its reachable space must be uniformly regular. Nothing here tells an ideal reasoner what to believe.

**The Dutch book.** Rescorla's theorems concern departures from Kolmogorov conditionalization of the agent's own prior. An agent using any of the three routes conditionalizes its own prior on what it learns, so the theorems give no handle against it.

**The evaluative ideal.** If Kolmogorov conditionalization was never meant as an instruction, nothing here touches it.

# 6. Conclusion

The noncomputability of conditioning invites a per-prior response: hold only priors whose conditional distributions are computable. For an agent that adopts and mixes priors, this response is not enough. A uniformly presented family of priors, each built from a uniform law and a comb of tents, each with a continuous computable posterior, defeats every single updating procedure. What is needed is uniform regularity across the states the agent can reach. It can come from fixed regularity constants, from presented data, or from a regular model of the evidence source. The constraint that computability places on a follower of conditionalization is therefore a constraint on the space of its credal states. Whether a credence function is fit to be held depends on what else could have been held. Exact conditionalization survives as an ideal, approached almost surely by followable updates.

# Appendix. Proof of Proposition 2

Let $U$ be correct on every $\mu_M$. Measures on $\{0,1\}$ are compared in total variation, and $U$'s output is projected onto $I$. Projection does not increase distances.

**The machine.** By the recursion theorem, let $M^*$ know its own index, and hence a presentation $e^*$ of $\mu_{M^*}$. $M^*$ dovetails a search for two things:
- a finite sequence $\tau$ of rationals, together with a rational interval $K \subseteq [0,1]$ of width $r > 0$, such that every point of $K$ has a name extending $\tau$;
- a halting computation of $U$ on $e^*$ that reads only $\tau$ from the oracle and outputs, at precision $2^{-4}$, a measure $m$ with $d(m, \delta_0) < 1/8$.

Whether every point of $K$ has a name extending $\tau$ is decidable from $\tau$ and $K$, since it means that $K$ lies inside each open ball $(q_i - 2^{-i}, q_i + 2^{-i})$. When the search succeeds, $M^*$ idles until a step $m^*$ such that $n = m^* + 2$ satisfies $2^{-(n-1)} < r/2$, and then halts.

**The search succeeds.** Otherwise $M^*$ never halts, $\mu_{M^*} = A$, and the true posterior is $\delta_0$. Take $z \in (0,1)$ in the measure-one set where $U$ is correct, and a name of $z$ with $|q_i - z| < 2^{-i-1}$. A correct $U$ outputs a measure within $1/16$ of $\delta_0$ after reading some finite segment $\tau$ of this name. Every point within $2^{-|\tau|-1}$ of $z$ lies in all the balls named by $\tau$, so a rational interval $K$ around $z$ inside $[0,1]$ qualifies. So the dovetailed search finds some pair.

**$U$ errs.** $U$'s computation depends only on $e^*$ and $\tau$, so $U$ outputs $m$ on every name extending $\tau$, and hence at every $z \in K$. Since $2^{-(n-1)} < r/2$, $K$ contains a dyadic interval of length $2^{-(n-1)}$, which fixes binary digits $1$ to $n-1$. Inside it lies an interval of $E_n$, on whose central half $f_n \ge 2^{n+1}$. There

$$P(I = 1 \mid z) \ge \frac{2^{-n}\,2^{n+1}}{(1 - 2^{-n}) + 2^{-n}\,2^{n+1}} > \frac{2}{3}.$$

So $U$'s output is wrong by more than $2/3 - 1/8 > 1/16$ on a set of positive Lebesgue measure. Since $P_Z \ge (1 - 2^{-n})\,\mathrm{Leb}$ on $[0,1]$, that set also has positive $P_Z$-measure, which contradicts correctness.

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

Shan, Chung-chieh and Norman Ramsey. 2017. Exact Bayesian inference by symbolic disintegration. In *Proceedings of the 44th ACM SIGPLAN Symposium on Principles of Programming Languages (POPL 2017)*, 130-144.

Weihrauch, Klaus. 2000. *Computable Analysis: An Introduction*. Berlin: Springer.
