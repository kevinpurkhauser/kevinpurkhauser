---
title: "Following Conditionalization: Per-Prior Computability Is Not Enough"
---

**Abstract.** Ackerman, Freer and Roy showed that some computable priors have conditional distributions that no algorithm can compute. A natural response is to require that a computable agent's prior have computable conditional distributions. I show that, for an agent who may adopt new priors (for instance models given as programs) or form countable mixtures of priors, this per-prior requirement does not make conditionalization a rule the agent can follow. I construct a uniformly computable family of priors, built from a uniform law and a comb of tents. Each member has a continuous, computable posterior on an exact observation, yet no single procedure updates them all, and so any fixed updating procedure is, in some state the agent can reach, exposed to a Dutch book. What restores a single procedure is a regularity condition with fixed parameters. The thesis is about quantifier order. A condition of the form "each prior is regular to some degree" does not suffice. A condition of the form "there is a degree of regularity that every reachable prior meets" does. The uniformity can come from three sources:
- fixed constants in the class of admissible priors;
- regularity data supplied with each prior;
- a regular model of the evidence source, which changes the evidence.

So computability constrains rule-following credence only through conditions that are uniform across the states an agent can come to hold. The ideal reading of conditionalization is untouched.

# 1. Introduction

When a Bayesian agent learns that a continuous quantity took the value $y$, the learned event has probability zero and the ratio formula is silent. The standard answer is Kolmogorov conditionalization. The new credence is given by a regular conditional distribution: a kernel $y \mapsto P[\,\cdot \mid Y = y]$ that disintegrates the prior and is fixed up to observations of measure zero. (Kolmogorov 1933 gives the measure-theoretic notion of conditional probability; regular versions came later.) Rescorla (2018) proves Dutch book and converse Dutch book theorems for this rule, and Rescorla (2025) extends them to scenarios in which the conditioning proposition may be false.

Ackerman, Freer and Roy (2011, 2019; hereafter AFR) showed that the rule can outrun computation. There are computable random variables $X$ and $Y$ whose conditional distribution of $X$ given $Y$ is not computable on any set of measure one. Computability has been used to constrain credence functions in other respects. Lopez-Wild (2026) argues that there are no computable merely finitely additive probability measures, and Huttegger, Walsh and Zaffora Blando (2025) study convergence to the truth for computable priors.

A response to AFR then suggests itself: a computable agent must hold a prior whose conditional distributions are computable. I call this the *per-prior requirement*. I treat it as a natural position rather than one I attribute to the authors just cited. Specialists in computable analysis know that pointwise computability does not give uniform computability. The question here is what that distinction means for the epistemology of updating, which has not been asked.

The thesis has four parts.

1. **Failure of the per-prior requirement for open agents** (Proposition 2). Some agents can adopt priors presented as programs, or form countable computable mixtures of priors they can hold. For such agents the per-prior requirement can hold of every member of a reachable family while no single procedure updates them all.
2. **A Dutch book consequence.** It follows that any fixed updating procedure such an agent uses departs from Kolmogorov conditionalization, on a set of positive measure, in some reachable state. By Rescorla's theorem the agent is then exposed to a Dutch book in that state.
3. **What suffices** (Propositions 3 and 4). A single procedure exists when there is a fixed degree of regularity that every reachable state meets, or when equivalent information is supplied with each state, or when the evidence comes through a fixed regular channel.
4. **Quantifier order.** The computability condition that matters for a rule-following agent has the form "there are constants that every reachable state meets", not "every state meets some constants". Each of the paper's positive conditions is a property of individual credence functions, but with parameters fixed across the agent's reachable space.

The mathematics is elementary. Proposition 2 is a diagonal argument of a known kind: it is a close relative of the non-computability of the Radon-Nikodym operator (Hoyrup, Rojas and Weihrauch 2012) and of AFR's results on the discontinuity of conditioning (see also Ackerman, Freer and Roy 2017). The positive results apply AFR's theorem for bounded densities. Practitioners of probabilistic programming already condition on continuous data through likelihood densities. For instance, Shan and Ramsey (2017) construct such densities by symbolic disintegration. What is offered here is an epistemological consequence. A computability constraint on updating cannot be stated prior by prior with existential parameters. It needs fixed parameters, and so it is answerable to what else the agent could come to believe.

The scope is limited in four ways.
- Nothing here concerns conditionalization as an evaluative ideal.
- Nothing here concerns discrete evidence.
- For an agent with one fixed prior that changes only by conditionalization, nothing here goes beyond the per-prior requirement.
- I treat a single observation. Iterated observation raises further questions, which I leave aside.

# 2. Framework

**Computable measures.** I work in computable probability theory.
- Spaces are computable metric spaces.
- A point is given by a Cauchy name: rationals $q_1, q_2, \ldots$ with $|q_i - x| < 2^{-i}$.
- A probability measure is *computable* if some program, on input $k$, outputs a finitely supported measure with rational weights on ideal points within Prokhorov distance $2^{-k}$ of it. The index of such a program is a *measure presentation*.

**Credal states and updating.** A credal state is a measure on $H \times Y$, where $H$ collects the hypothesis variables and $Y$ is the observation the agent is about to learn.
- An *updating procedure* takes an index of a presentation of a credal state, possibly together with further data, and a name of $y$ as an oracle. It outputs approximations to a posterior over $H$.
- It is *correct* on a state if there is a version $\kappa$ of the conditional distribution such that, for $P_Y$-almost every $y$ and every name of $y$, its output converges to $\kappa(y)$ at the advertised precision.
- A state is *updatable* if some procedure is correct on it.

**Two readings of the rule.**
- On the *ideal reading*, conditionalization is a standard. The correct kernel exists whether or not anyone computes it.
- On the *followed reading*, it is something the agent does, in the way someone adds by following the rule for addition.

The followed reading is in play when a Bayesian model is offered as an algorithmic-level account of how a mind or machine learns, in the sense of Marr (1982). It is also in play for systems that actually perform the updates.

**Operations.** An agent's credal state can change in three ways:
- **(U)** updating;
- **(A)** adopting a prior from a class $\mathcal{C}$ of presentations, such as a model received as a program or built from data;
- **(X)** forming countable mixtures, with computable weights, of uniformly presented states the agent can hold.

The *reachable states* are those obtainable from the initial state by these operations.

**FOLLOW.** A computable agent follows conditionalization only if a single procedure, applied to its states in the form its operations deliver them, is correct on every reachable state that is updatable.

FOLLOW is a necessary condition only. It asks for no proof of correctness. It places no demand on states that no procedure could update. I take the form in which states are delivered, and the set of operations, to be facts about the agent's architecture. For engineered systems they are fixed by design. For human learners, which operations they have and in what form is an empirical question that I leave open. Kripke (1982) argued that a machine's program settles which function it computes only relative to its designer's intentions. I do not try to answer that worry. I stipulate the architecture, and ask what follows given it.

# 3. The family

## 3.1 Construction

Let $Z \in [0,1]$ and $I \in \{0,1\}$. For $n \ge 2$, let $E_n$ be the set of $z$ whose binary digits in positions $n$ to $2n$ are all $0$. $E_n$ is a union of $2^{n-1}$ intervals of length $2^{-2n}$. Let $f_n$ be the continuous density that places a tent of mass $2^{-(n-1)}$ on each of these intervals. The peak height of $f_n$ is $2^{n+2}$, its slope is $2^{3n+3}$, and on the central half of each interval its value is at least $2^{n+1}$.

Let $A = \delta_0 \otimes \mathrm{Leb}$ and $B_n = \delta_1 \otimes f_n\,\mathrm{Leb}$. Both are computable uniformly in $n$.

For a Turing machine $M$:
- if $M$ halts at step $m$, let $n = m + 2$ and $\mu_M = (1 - 2^{-n})A + 2^{-n}B_n$;
- if $M$ never halts, $\mu_M = A$.

Equivalently, $\mu_M$ is the countable mixture $\sum_n p_n(M)\,B_n + \big(1 - \sum_n p_n(M)\big)A$, where $p_n(M) = 2^{-n}$ if $M$ halts at step $n - 2$ and $p_n(M) = 0$ otherwise. Each $p_n(M)$ is decidable, and the residual weight is a computable real.

**Lemma 1.** $\mu_M$ is computable uniformly in $M$, and so is its mixture representation (the components $A, B_2, B_3, \ldots$ and the weights $p_n(M)$).

*Proof.* Run $M$ for $k$ steps. If $M$ has halted, approximate the mixture to within $2^{-k-1}$. If not, approximate $A$ to within $2^{-k-1}$; the omitted weight is at most $2^{-k-3}$, and total variation bounds Prokhorov distance.

## 3.2 Each member is tractable; no procedure handles them all

The agent observes $Z$ exactly, so $H = I$ and $Y = Z$. If $M$ halts, then for each $M$

$$P_M(I = 1 \mid Z = z) = \frac{2^{-n} f_n(z)}{(1 - 2^{-n}) + 2^{-n} f_n(z)}.$$

If $M$ never halts, the posterior is $0$. Either way it is a continuous and computable function of $z$. So every $\mu_M$ satisfies the per-prior requirement.

**Proposition 2.** Fix any representation of $\mu_M$ computable uniformly in $M$, such as the measure presentation or the mixture representation of Lemma 1. Then no single procedure taking that representation as input is correct on every $\mu_M$.

*Sketch.* Suppose $U$ were correct on every member. By the recursion theorem, build a machine $M^*$ that searches for two things:
- a finite segment of a name of an observation, leaving a rational interval $K \subseteq [0,1]$ of possible values;
- a finite run of $U$ on the representation of $\mu_{M^*}$ that reads only that segment and outputs a posterior within $1/8$ of "$I = 0$ for certain".

The search must succeed. If $M^*$ never halted, $I = 0$ would be certain, and a correct $U$ would output that posterior on almost every observation after reading a finite segment.

When the search succeeds, $M^*$ halts late enough that $2^{-(n-1)}$ is less than half the width of $K$. $U$'s run is a fixed finite computation, so it gives the same output on every observation in $K$. But $K$ contains an interval of $E_n$ whose central half has positive measure, and on that half the true posterior gives $I = 1$ probability above $2/3$. So $U$ is wrong on a set of positive measure. The appendix gives details.

Three remarks.
1. The marginal density of $Z$ is at most $5$ throughout the family, so a uniform density bound on the observation is not enough. What grows without bound is the modulus of continuity.
2. Any regularity data that would rescue a procedure, such as a bound on $f_{n}$, decide whether $M$ halts. Run $M$ for about $\log_2$ of the bound many steps: if it has not halted by then, it never will. So such data cannot be computed from $M$.
3. The family is reachable by (X), as a countable computable mixture of uniformly presented, trivially updatable components. It is reachable by (X) provided $A$ and the $B_n$ are themselves reachable, for instance as adoptable models. It is also reachable by (A) for any class $\mathcal{C}$ that contains it, for example the class of all measure-presented priors with continuous bounded densities. Finite mixing of finitely many known components does not generate the family. An agent that mixes finitely many models and keeps their densities can update the result (Proposition 3a). The result therefore concerns agents that can adopt priors given as programs, or mix countably.

## 3.3 The Dutch book consequence

Let an agent whose reachable states include the family use any fixed procedure $U$. By Proposition 2 there is a reachable state $\mu_M$ on which $U$'s update differs from every version of the conditional distribution, on a set of observations of positive probability. Rescorla's (2018) Dutch book theorem, as I read it, applies to an agent whose update rule departs from Kolmogorov conditionalization of its own prior on a set of positive prior probability. Such an agent is exposed to a Dutch book in that state.

So the failure of uniformity is not only a failure of rule-following. It has the pragmatic cost that the orthodox view itself recognises, located in a particular state. That location is the orthodox view's own, and I accept it. The present point is that no fixed procedure avoids every such state, although each state, taken alone, can be updated correctly.

# 4. What suffices

## 4.1 Three sources of uniformity

**Proposition 3.**
- **(a) Supplied regularity data.** Suppose each state is given as a measure $\rho$ on $H$, a computable function $q(h, y)$ with $\int q\,d(\rho \otimes \lambda) = 1$, a rational bound $c \ge q$, and a computable reference measure $\lambda$, so that the state is $q\,\rho \otimes \lambda$. Then one procedure is correct on all such states. The posterior expectation of a bounded continuous $g$ is $\int g q(\cdot, y)\,d\rho \,/\, \int q(\cdot, y)\,d\rho$. Both integrals involve bounded computable functions with known bounds, so they are computable relative to $y$, uniformly in the data. The denominator is positive for $P_Y$-almost every $y$. This is AFR's dominated-case argument (AFR 2019, the section on positive results for densities and noise). For Proposition 2's family these data are not computable from $M$ (remark 2 above).
- **(b) A fixed regular channel.** Suppose instead the agent learns a reading $Y = Z + \xi$, where $\xi$ is independent and has a fixed computable bounded density $\varphi$. Taking $H = (I, Z)$, $\rho = \mu_M$ and $q(h, y) = \varphi(y - z)$ places the state in case (a), with data computable uniformly in $M$. So one procedure updates every member of the family on the noisy reading. This is AFR's noisy-observation result. It does not update on the exact value of $Z$. It solves a different learning problem, in which what is learned is the reading.

**Proposition 4 (fixed constants).** Fix $L$. Let $\mathcal{C}_L$ be the class of measures on $H \times [0,1]$ whose density $q(h, \cdot)$ of $Y$ given $h$, with respect to Lebesgue measure, is $L$-Lipschitz for $\rho$-almost every $h$, where $\rho$ is the $H$-marginal. Then one procedure, given only measure presentations, is correct on every member of $\mathcal{C}_L$.

*Sketch.*
1. Each $q(h, \cdot)$ is a probability density that is $L$-Lipschitz, so it is bounded by $C = 1 + L/2$, and $P_Y$ has density at most $C$.
2. From the name of $y$, find $\delta > 0$ with $y \in (\delta, 1 - \delta)$. This is possible for every $y$ in the open interval, which has probability one. Take balls $B$ around $y$ of radius $\varepsilon < \delta$.
3. The probability of lying within $\eta$ of the boundary of $B$ is at most $4C\eta$. So $P(g(H);\, Y \in B)$ and $P(Y \in B)$ are computable from the measure presentation, uniformly in $L$.
4. By the Lipschitz bound, dividing these by $2\varepsilon$ approximates $\int g\,q(\cdot, y)\,d\rho$ and $p(y) = \int q(\cdot, y)\,d\rho$ to within $\|g\|L\varepsilon$ and $L\varepsilon$.
5. Where $p(y) > 0$, which holds $P_Y$-almost surely, a positive lower bound on $p(y)$ is found from these approximations, and the ratio then converges at a computable rate.
6. Since a probability measure is computable when its integrals of bounded Lipschitz test functions are uniformly computable, this yields the posterior.

$\mathcal{C}_L$ is closed under countable mixtures, because each mixture density is a pointwise convex combination of the component densities. So an agent confined to $\mathcal{C}_L$ stays there under (A) and (X), provided its adoptable class lies in $\mathcal{C}_L$. Proposition 2's family lies in no $\mathcal{C}_L$, since $q(1, \cdot) = f_n$ has slope $2^{3n+3}$.

## 4.2 Quantifier order

The argument combines FOLLOW with the propositions.

1. **(Q1)** FOLLOW.
2. **(Q2)** The per-prior requirement says that every reachable state is updatable. Equivalently, for each reachable state there is some degree of regularity it meets. By Proposition 2, an agent can satisfy this while failing FOLLOW.
3. **(Q3)** The condition "there is an $L$ such that every reachable state lies in $\mathcal{C}_L$" guarantees a single correct procedure (Proposition 4). So does a single regular channel for all reachable states (Proposition 3b), or supplied data with known bounds (Proposition 3a). These do not show that FOLLOW is satisfied, because FOLLOW is only necessary, but they remove the obstacle it records.
4. **(Q4)** So a computability condition on credence functions that is fit to secure rule-following has the form $\exists$ parameters $\forall$ reachable states, not $\forall$ states $\exists$ parameters.

Q4 is the thesis. The conditions in Q3 are properties of individual credence functions once the parameters are fixed. To that extent the orthodox claim that computability constraints attach to credence functions survives. What does not survive is the idea that they can be stated prior by prior with the parameters left open. The fixed parameters are answerable to the agent's whole reachable space. Strictly, the condition is a property of agents: of a procedure together with a reachable space. A given credence function, for instance $\mu_{M_0}$ for a halting $M_0$, lies in $\mathcal{C}_L$ for $L$ of order $2^{3n}$. So it can belong to an agent who satisfies the condition, and also to one who does not, according to what else each agent can reach.

**The fixed-prior agent.** For an agent whose prior is fixed and changes only by (U), the per-prior requirement is all that FOLLOW asks, since its reachable states are posteriors of one prior. A program computing that prior's kernel then updates every case, as an adding machine handles every pair of numbers. The present thesis concerns agents that adopt and mix. Much real learning is of this kind: forming a model from data, accepting a model from another agent, extending the hypothesis space when becoming aware of new possibilities, or averaging over a countable family of models. For such agents the prior is among the inputs to the updating procedure.

**Stored kernels.** A format that stores a kernel with each state is closed under (U), but not under (X). Re-weighting mixture components after an observation needs the components' densities for the observation, and a stored kernel does not provide them. Proposition 2's family is itself a computable countable mixture of components with trivial kernels.

**Is the thesis definitional?** Given FOLLOW, Q4 follows quickly. The substantive inputs are three. The first is FOLLOW's quantification over reachable states, which I have defended for adopting and mixing agents. The second is Proposition 2, which shows that the gap between the two quantifier orders is not empty for families of a natural kind. The third is Propositions 3 and 4, which show that each route across the gap has a recognisable epistemic cost:
- fixed constants restrict which priors may be adopted;
- supplied data must come with each prior and cannot always be computed from it;
- a regular channel changes what is learned.

None of the three is free. An agent that wants its priors over hypotheses unrestricted, and needs no extra data about them, must take the third route: it must learn only through fixed regular channels, and so treat what it learns as readings with slack.

# 5. Objections

**Finite precision.** A computable agent never receives an exact real, so perhaps the rule it follows is ratio conditionalization on the rational intervals it receives. That is discrete evidence. It is correct if the agent's model of how intervals are reported is ignorable, for example under coarsening at random (Heitjan and Rubin 1991). It is computable if the intervals have null boundaries under the prior; for priors with atoms, the probability of a closed interval need not be computable. Along a fixed nested partition, such as the dyadic intervals containing $y$, the resulting posteriors converge almost surely to a version of the exact posterior (Lévy's upward theorem). The intervals an agent actually receives from a Cauchy name are not those of a fixed filtration, so for them a differentiation theorem is needed, for instance Besicovitch's theorem for centred intervals. On Proposition 2's family the rate of convergence depends on the halting time, so it is not computable uniformly. I accept the convergence result as the sense in which the exact rule governs bounded agents as an ideal. It does not supply a uniform procedure for the exact rule, which is what following it would require.

**From capacity to norm.** The conclusion is conditional. If conditionalization is to be a rule that an adopting or mixing computable agent follows, then any computability condition that secures this must have fixed parameters across its reachable states. Nothing here tells an ideal reasoner what to believe. Section 3.3 shows, however, that the failure has a cost the orthodox view itself counts.

**Dutch books for the positive routes.** On routes (a) and Proposition 4, the agent Kolmogorov-conditionalizes its own prior on what it learns, so Rescorla's theorems give no handle against it. On route (b), the agent conditionalizes on the reading. If what it really learns is the exact value of $Z$, route (b) is not conditionalization on its total evidence, and the Dutch book theorem does apply. Route (b) is a solution only for an agent whose evidence really is the reading.

**The evaluative ideal.** If Kolmogorov conditionalization was never meant as an instruction, nothing here touches it.

# 6. Conclusion

The noncomputability of conditioning invites the per-prior requirement: hold only priors whose conditional distributions are computable. For an agent that can adopt priors given as programs, or mix them countably, this requirement can hold of every reachable prior while no single procedure updates them all. Such an agent, whatever fixed procedure it uses, is exposed to a Dutch book in some reachable state. What restores a single procedure is regularity with fixed parameters: a class with a fixed modulus, data supplied with each prior, or a fixed regular channel. The computability condition fit for a rule-following agent has the form "some parameters suffice for every reachable state". The weaker form, "every state meets some parameters", does not. Exact conditionalization survives as an ideal, approached almost surely by followable updates.

# Appendix. Proof of Proposition 2

Let $R$ be a representation of $\mu_M$ computable uniformly in $M$, and let $U$ be correct on every $\mu_M$ given by $R$. Measures on $\{0,1\}$ are compared in total variation, and $U$'s output is projected onto $I$. Projection does not increase distances.

**The machine.** By the recursion theorem, let $M^*$ know its own index, and hence $e^* = R(M^*)$. $M^*$ dovetails a search for two things:
- a finite sequence $\tau$ of rationals, together with a rational interval $K \subseteq [0,1]$ of width $r > 0$, lying inside every ball $(q_i - 2^{-i}, q_i + 2^{-i})$ for $q_i$ in $\tau$, so that every point of $K$ has a name extending $\tau$ (a decidable condition);
- a halting computation of $U$ on $e^*$ that reads only $\tau$ from the oracle and outputs, at precision $2^{-4}$, a measure $m$ with $d(m, \delta_0) < 1/8$.

When the search succeeds, $M^*$ idles until a step $m^*$ such that $n = m^* + 2$ satisfies $2^{-(n-1)} < r/2$, and then halts. Any part of $e^*$ that the found computation evaluated simulates $M^*$ only for fewer steps than $M^*$ had run when the search ended, and so for fewer than $m^*$ steps. That computation is therefore also $U$'s computation on the actual $\mu_{M^*}$.

**The search succeeds.** Otherwise $M^*$ never halts, $\mu_{M^*} = A$, and the true posterior is $\delta_0$.
- Take $z \in (0,1)$ in the measure-one set where $U$ is correct, and a name of $z$ with $|q_i - z| < 2^{-i-1}$.
- $U$ outputs, at precision $2^{-4}$, a measure within $1/16$ of $\delta_0$, after reading a finite segment $\tau$ of this name.
- Every $x$ with $|x - z| < 2^{-|\tau|-1}$ lies in every ball named by $\tau$.
- So a rational interval $K \subseteq [0,1]$ around $z$ qualifies, and the dovetailed search finds some pair.

**$U$ errs.**
- $U$'s computation depends only on $e^*$ and $\tau$, so $U$ outputs $m$ on every name extending $\tau$, and hence at every $z \in K$.
- Since $2^{-(n-1)} < r/2$, $K$ contains a dyadic interval of length $2^{-(n-1)}$, which fixes binary digits $1$ to $n-1$. Inside it lies an interval of $E_n$, on whose central half $f_n \ge 2^{n+1}$.
- There, $P(I = 1 \mid z) \ge 2/\big((1 - 2^{-n}) + 2\big) > 2/3$.
- The output $m$ is within $1/8$ of $\delta_0$, so it is more than $2/3 - 1/8$ from the truth. $U$'s limiting output is within $1/16$ of $m$, so it is more than $2/3 - 1/8 - 1/16 > 0$ from the truth.
- This happens on a set of positive Lebesgue measure. Since $P_Z \ge (1 - 2^{-n})\,\mathrm{Leb}$ on $[0,1]$, the set also has positive $P_Z$-measure, which contradicts correctness.

# References

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2011. Noncomputable conditional distributions. In *Proceedings of the 26th Annual IEEE Symposium on Logic in Computer Science (LICS 2011)*, 107-116.

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2017. On computability and disintegration. *Mathematical Structures in Computer Science* 27(8): 1287-1314.

Ackerman, Nathanael L., Cameron E. Freer and Daniel M. Roy. 2019. On the computability of conditional probability. *Journal of the ACM* 66(3), Article 23: 1-40.

Garber, Daniel. 1983. Old evidence and logical omniscience in Bayesian confirmation theory. In John Earman (ed.), *Testing Scientific Theories*, Minnesota Studies in the Philosophy of Science 10, 99-131. Minneapolis: University of Minnesota Press.

Hacking, Ian. 1967. Slightly more realistic personal probability. *Philosophy of Science* 34(4): 311-325.

Heitjan, Daniel F. and Donald B. Rubin. 1991. Ignorability and coarse data. *The Annals of Statistics* 19(4): 2244-2253.

Hoyrup, Mathieu, Cristóbal Rojas and Klaus Weihrauch. 2012. Computability of the Radon-Nikodym derivative. *Computability* 1(1): 3-13.

Huttegger, Simon M., Sean Walsh and Francesca Zaffora Blando. 2025. Bayesian convergence for computably bounded agents. *Philosophy and Phenomenological Research* 112(1): 307-324.

Kolmogorov, Andrei N. 1933. *Grundbegriffe der Wahrscheinlichkeitsrechnung*. Berlin: Springer.

Kripke, Saul A. 1982. *Wittgenstein on Rules and Private Language*. Cambridge, MA: Harvard University Press.

Lopez-Wild, Josiah. 2026. Computable Bayesian epistemology. *Philosophy of Science*. doi:10.1017/psa.2026.10273.

Marr, David. 1982. *Vision*. San Francisco: W. H. Freeman.

Rescorla, Michael. 2018. A Dutch book theorem and converse Dutch book theorem for Kolmogorov conditionalization. *The Review of Symbolic Logic* 11(4): 705-735.

Rescorla, Michael. 2025. Non-factive Kolmogorov conditionalization. *The Review of Symbolic Logic* 18(1): 186-212.

Shan, Chung-chieh and Norman Ramsey. 2017. Exact Bayesian inference by symbolic disintegration. In *Proceedings of the 44th ACM SIGPLAN Symposium on Principles of Programming Languages (POPL 2017)*, 130-144.

Weihrauch, Klaus. 2000. *Computable Analysis: An Introduction*. Berlin: Springer.
