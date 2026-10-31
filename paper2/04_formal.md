# 04. Formal core

Code: `formal/check_mixture.py`, `formal/skeleton_z3.py`, `formal/noise_scale_mixture.py`. All three run and pass (outputs below).

## Setting

- Computable metric spaces; probability measures on them carry the weak topology. A measure is computable if a program outputs, on input k, a finitely supported rational measure within Prokhorov distance 2^-k of it. A *presentation* of a prior is such a program.
- Hidden variable H (the world), observation Y (real-valued or in R^d). A *conditional distribution map* is a measurable y -> P[H | Y = y] that disintegrates P. It is *computable* if some version of it is computable on a set of P_Y-measure one.

## Imported results (reported, not read in full)

- **AFR-neg** (Ackerman, Freer and Roy, JACM 2019; LICS 2011). There are computable random variables (X, Y) whose conditional distribution P[X | Y] is not computable on any P_Y-measure-one set. The construction encodes the halting times of all Turing machines. Source: search snippets of arXiv 1005.3014 and secondary descriptions.
- **AFR-noise** (same paper, Corollary 9.7 in the arXiv and journal versions, reported). If ξ is independent of the other variables and absolutely continuous with a bounded computable density, then the conditional distribution given a computable (even almost computable) quantity corrupted by ξ is computable.
- **AFR-dens** (same paper, reported; also used in the probabilistic programming literature). In the dominated setting, if P[Y | H] has a bounded computable density, the conditional distribution map is computable.

## Own results (elementary)

**Lemma 1 (uniform weights).** For a Turing machine M, let w_M = 2^-n if M halts at step n, and w_M = 0 otherwise. Then w_M is a computable real, uniformly in M.
*Proof.* To within 2^-k: run M for k steps. Output 2^-n if it halted at step n <= k, else 0. The error is at most 2^-k. (Checked on toy machines in `check_mixture.py`.)

**Construction.** Fix B, the AFR-neg pair (X, Y), and a computable ν on the X-space. Let I take values in {0, 1}. Define
P_M = (1 - w_M) (δ_0 ⊗ ν ⊗ B_Y) + w_M (δ_1 ⊗ B), on I × X × Y.
B_Y is computable as the image of a computable measure under a computable projection. So P_M is computable uniformly in M (Lemma 1, plus mixing with computable weights).

**Lemma 2 (recovery).** If w_M > 0, then:
- P_{M,Y} = B_Y;
- for B_Y-almost every y, P_M[(I, X) | Y = y] = (1 - w_M) δ_0 ⊗ ν + w_M δ_1 ⊗ B[X | Y = y];
- hence, from any version κ of P_M[(I, X) | Y] that is computable on a measure-one set S, the map y -> (1/w_M) κ(y) restricted to {1} × X is a version of B[X | Y] that is computable on S.

*Proof.* The displayed kernel disintegrates P_M, and disintegrations are unique almost everywhere. For restriction: {1} × X is clopen and at distance 1 from its complement. A Prokhorov approximation within ε < 1/2 therefore restricts to an approximation of the restricted measure within ε in mass and position. Dividing by the computable constant w_M > 0 is computable. (Finite analogue checked in exact arithmetic over 2,000 random instances in `check_mixture.py`.)

**Proposition 1 (non-certifiability).** Let GOOD be the set of M such that P_M has a computable conditional distribution map for (I, X) given Y. Then GOOD is exactly the set of machines that never halt. Hence GOOD is not computably enumerable.
*Proof.* If M never halts, P_M = δ_0 ⊗ ν ⊗ B_Y, whose conditional is the constant δ_0 ⊗ ν, which is computable. If M halts, w_M > 0. By Lemma 2, a computable conditional for P_M would give one for B, contradicting AFR-neg. The complement of the halting set is not c.e.

**Corollary 1 (no sound certifier).** For any consistent c.e. theory T extending a weak arithmetic, let M_T search for a T-proof of 0 = 1. Then P_{M_T} = δ_0 ⊗ ν ⊗ B_Y (its conditional is computable), but T does not prove that the presented prior has a computable conditional. If T proved it, T would prove that M_T never halts, that is, Con(T), against Gödel's second theorem. More generally, no c.e. procedure accepts exactly the programs in the family {P_M} whose priors can be updated computably.

**Corollary 2 (fragility).** The well-behaved prior Q = δ_0 ⊗ ν ⊗ B_Y is the total-variation limit, as w -> 0, of priors (1 - w)Q + w(δ_1 ⊗ B) that have no computable conditional (Lemma 2 for each fixed w > 0). So within this family, being computably updatable is not stable under small perturbation.

**Lemma 3 (channel class: closure).** Call a presentation a *channel presentation* if it consists of:
- a program for the world prior μ on H;
- a program for a likelihood density p(y | h) with respect to a computable reference measure;
- a rational bound c with p <= c.

Then:
- By AFR-dens (or AFR-noise for additive noise), the conditional distribution map is computable. A certificate is part of the presentation, namely the bound c.
- Channel presentations are closed under:
  - finite mixtures with computable weights (put the mixture index into H; the bound is the maximum of the component bounds);
  - any finite sequence of observations whose channels are conditionally independent given H (the joint likelihood is the product, bounded by the product of the bounds).
- Every computable world prior μ has a channel presentation, for example Gaussian noise of any fixed scale, or any bounded computable noise.

**Lemma 4 (noise floors are not needed).** Take Gaussian noise of unknown scale s with prior π on (0, 1). The mixed noise density is bounded if and only if E_π[1/s] < ∞.
- This allows positive prior weight on every interval (0, d), for example π(s) = 2s, for which E[1/s] = 2.
- The uniform prior on (0, 1) gives E[1/s] = ∞, so it is excluded.
- Checked symbolically in `noise_scale_mixture.py`.

So certifiability does not require a floor on noise, only a finite expected inverse scale.

## Logical skeleton (Z3, `skeleton_z3.py`)

**Argument 1** (VALID; becomes invalid without P1):
- **P1 (FOLLOW).** If an agent is bound by the conditionalization rule *as a rule it follows*, it can execute the rule from its own representation, with justification.
- **P2.** Agents that hold a prior, receive continuous evidence and can so execute the rule are bound by it.
- **P3.** There are agents a1, a2 with the same credence function such that a1 can and a2 cannot (Proposition 1, Corollary 1).
- **C1.** Being bound by the rule is not a function of the credence function.

**Argument 2** (VALID; becomes invalid without P4):
- **P2.** As above.
- **P4.** Channel presentations can execute the rule with justification (Lemma 3).
- **P5.** Every world prior has a channel presentation (Lemma 3).
- **C2.** For every world prior, some agent holding it is bound by the rule as a rule it follows.

## Claims the paper must not make

1. That conditionalization is unsatisfiable by computable agents. Proposition 1 concerns certification, not existence.
2. That noisy updating is a different norm. It is exact conditionalization under a channel prior.
3. That the channel class is the only certifiable class. The defensible claim is: every certifiable route known to the author for continuous observations is dominated, so the observation is not an exact function of the world.
4. That the non-certifiability result is deep. It is an elementary Rice-Shapiro style consequence of AFR-neg. The novelty lies in its philosophical use.
5. That AFR state Corollary 9.7 in exactly the form given. It is reported from snippets. The paper says "reported".
6. That the conclusions touch the evaluative ideal. They concern conditionalization as a rule followed by a computable agent.
7. That the requirement constrains no belief about the world. It constrains beliefs about the agent's own evidential channel, which are beliefs about the world.
8. That digital or finite-precision evidence is affected. Ratio conditionalization on positive-probability events is unaffected.

## Outputs

```
mixture identities: 2000 random exact instances OK
w_M approximation error <= 2^-k for all toy machines and k < 45: OK
Argument 1 (representation-dependence): VALID
Argument 2 (no constraint on world-priors): VALID
Argument 1 without P1 (expected NOT VALID): NOT VALID (sat)
Argument 2 without P4 (expected NOT VALID): NOT VALID (sat)
uniform on (0,1): E[1/s] = oo; density 2s: E[1/s] = 2; density 3s^2: E[1/s] = 3/2
```

## Addendum after Phase 5 (reformulation forced by objection O2)

**Proposition 1' (no sound general updater).**
- *Definition.* A sound general updater is a procedure U with this behaviour on a presentation e. It either never commits, or at some finite stage commits to a program c that computes a version of the conditional distribution map of P_e on a measure-one set.
- *Claim.* No sound general updater commits on every P_M with M in GOOD.
- *Proof.* By the s-m-n theorem, a program for P_M is computable from M. If U committed on all of GOOD, then the set {M : U commits on P_M} would be c.e. By soundness and Lemma 2 it would equal GOOD, that is, the complement of the halting set, which is not c.e.
- *Validity check.* The step from "commits on all of GOOD" plus soundness to "the commit set equals GOOD" is a pure set inclusion. Soundness gives commit set ⊆ GOOD, and the hypothesis gives GOOD ⊆ commit set.

Contrast (Lemma 3): on channel presentations the updater that reads the bound c and applies the AFR-dens algorithm commits on every input, and is sound.
