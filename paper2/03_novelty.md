# 03. Novelty check (search results only)

Access: scholarly hosts blocked (human choice 8: finish on search results). About 12 searches. Everything below rests on abstracts and search snippets; this is weaker than the Phase 3 the prompt specifies.

## Working thesis (T2, developed from the C08/S5 line after the S5 refutation)

For computable agents who learn from continuous evidence:

1. **Non-certifiability (own result, elementary).** The set of programs for computable priors whose conditional distributions are computable is not computably enumerable. There is a prior, presented by a program, that is extensionally identical to a well-behaved prior (if ZFC is consistent), yet no ZFC proof shows that the presented prior can be updated by any computable procedure.
2. **Representation-dependence.** If updating norms bind a computable agent only through what it can do from its own representation of its prior (a restricted ought-implies-can for self-executed norms), then rational standing is not a function of the credence function alone.
3. **Inexact evidence.** The general certifiable route for continuous evidence is a channel model with a bounded computable density (Ackerman, Freer and Roy's noise corollary). It leaves the prior over the world unconstrained and constrains only the agent's model of how evidence reaches it. So certifiable computable rationality requires a small, nonzero doubt about the exactness of continuous evidence.

The S5 refutation is answered as follows. No claim is made that conditionalization is unsatisfiable (S5's quantifier shift). Noisy updating is not treated as a rival norm; it is exact conditionalization under a channel prior. The ought-implies-can premise is restricted and argued for.

## Closest work found

| Work | What it does (snippet level) | Room left |
|---|---|---|
| Ackerman, Freer and Roy, JACM 66(3) 2019 (arXiv 1005.3014; LICS 2011) | Computable (X,Y) whose conditional distribution is not computable on any measure-one set; the construction encodes halting times. Positive results: discrete or dominated settings; Corollary 9.7 (independent noise with bounded computable density gives a computable conditional distribution map); exchangeable case | No result on whether computable conditionability is certifiable from a program; no philosophical use |
| Ackerman, Freer and Roy, "On computability and disintegration", MSCS 27(8) 2017 | The disintegration operator, on measures with unique continuous disintegration, is strongly Weihrauch equivalent to Lim | Uniform-operator complexity. Not the index-set (certification) question; no representation-dependence |
| Lopez-Wild, "Computable Bayesian Epistemology" (forthcoming; PhilSci 23862) | Argues computable Bayesian epistemology models more realistic agents; proves there are no computable merely finitely additive measures, a case for countable additivity | Constrains priors via computability; does not discuss conditional distributions or certification (not seen in snippets) |
| Huttegger, Walsh and Zaffora Blando, PPR 112(1) 2026 (PhilSci 27049) | Computable probability as a framework for computationally bounded Bayesians; convergence to the truth tied to algorithmic randomness | Convergence, not executability of updating |
| Mercier, Lopez-Wild and Spiegel, "At the Edge of Putnam's Program" (arXiv 2606.00363, 2026) | Limitative results for computable inductive logics; notes that conditional probabilities given positive-probability evidence are ratios of Δ2 quantities | Discrete inductive logic; not continuous evidence or certification (abstract not seen) |
| Rescorla, Review of Symbolic Logic 2018 | Dutch book and converse Dutch book theorems for Kolmogorov conditionalization | Defends exact-evidence norm; no computability |
| Mahtani, The Objects of Credence (OUP 2024); List 2024 | Credences are hyperintensional (Hesperus/Phosphorus) | Content-level hyperintensionality, not representation of one and the same measure |

## Verdict

- No source found that (a) proves or states the non-certifiability of computable conditionability, (b) argues from it to representation-dependence of rational standing, or (c) argues that computable rationality requires a noise model of continuous evidence.
- The mathematics of (a) is elementary given AFR (a Rice-Shapiro style argument). The paper must present it as elementary and put the weight on the philosophical consequences.
- Risks: the full texts of AFR 2019 and Lopez-Wild may contain remarks close to (a) or (c). This cannot be checked. Recorded as a known limitation.
