# Round 2: role C (technical) on draft v3

Report reproduced verbatim from the subagent's hand-back.

REFEREE REPORT (technical and citation check)
Submission: "Following Conditionalization: Computable Agents and the Noise in Evidence"

Scope. I read only the submission file. I ran 9 web searches. Direct fetches of arxiv.org, dl.acm.org, cfreer.org and ar5iv were blocked by the session's network settings; those hosts would need to be allowed for a check of the exact theorem statements in AFR. Where I could not see a primary text, I say "plausible but unverified".

Summary of the paper. Using a mixture P_M of an AFR prior and a tractable product prior, weighted by a halting-time weight, the paper proves that no updater is both sound and complete on the computably updatable presentations in the family {P_M} (Prop 1'). It then argues: (a) whether an agent can "follow" conditionalization depends on its representational system (FOLLOW plus OIC); (b) an open-ended learner with unrestricted priors over hypotheses can follow the rule if its source models have bounded densities, and cannot if it admits exact source models. The mathematics is mostly correct and elementary, and the paper says it is elementary. The main problems are an overstated "only if" thesis, a false closure claim, an "open question" that the paper's own framework already answers, and some loose or over-general claims about AFR.

A. VERIFICATION OF TECHNICAL CLAIMS

A1. Definition of a computable measure (Sec 2: finitely supported rational measures within Prokhorov distance 2^-k). Verified. This is the standard definition (Hoyrup and Rojas style).

A2. Lemma 1 (P_M is computable uniformly in M). Verified. Run M for k steps and output 2^-n if it halted at some step n ≤ k, else 0. The true value is either 0 or 2^-n with n > k, so the error is below 2^-k. A mixture of computable measures with computable weights is computable, and the construction is uniform in M via s-m-n.

A3. Lemma 2 (the disintegration formula). Verified. Both components have Y-marginal B_Y, and the displayed integral identity checks out. The approximation step is also correct: since ε < 1/2 and the slices are at distance 1, the ε-enlargement of the slice {1}×X is the slice itself. So the approximant's slice mass lies within ε of w. Renormalising gives a Prokhorov error of about (8/3)ε/w, which is within the stated 4ε/w, and 4ε/w ≥ ε because w ≤ 1/2. There is one small gap. The paper says the derived kernel is computable "on S". In fact it is computable on the measure-one subset of S where κ' agrees with κ, since off that set the slice-1 mass can be 0 and renormalising fails. This does not change the conclusion. Fix: say "on a measure-one subset of S".

A4. Proposition 1. Verified, given the AFR theorem in the form stated (no version of B[X|Y] computable on a B_Y-measure-one set). That form matches AFR's notion of computability on a measure-one set, and AFR's construction does encode the halting problem (confirmed by search). The exact theorem number is not cited and I could not check it against the primary text.

A5. Proposition 1'. Verified. C is c.e. because "commits" is a finite-time event and P_M is uniformly computable from M. Completeness gives co-HALT ⊆ C. Soundness plus Prop 1 gives C ⊆ co-HALT. The quantifier order is correct: the claim is that no single procedure exists, not that each instance is unsolvable.

A6. Corollary 1. Verified, with one missing hypothesis. Gödel's second theorem needs T to contain enough arithmetic and to use a standard provability predicate. "Consistent, computably axiomatized and proves Proposition 1" does not formally guarantee this for an arbitrary theory, although it holds for ZFC and its extensions. The claim that ZFC + Con(ZFC) settles P_{M_ZFC} is correct. Fix: add "and interprets sufficient arithmetic (e.g. extends PA)", or restrict the corollary to extensions of ZFC.

A7. Corollary 2. Verified. ||P_w - Q||_TV ≤ w, and for computable w > 0 the argument of Lemma 2 goes through. But the appeal to "Rice-Shapiro style reasoning" is loose. Rice-Shapiro concerns c.e. index sets of partial computable functions. The relevant result for computable points of an effective Polish space, such as the space of measures with the Prokhorov metric, is Kreisel-Lacombe-Shoenfield/Ceitin (Moschovakis), and it concerns openness in the weak topology, not TV. The inference still works, because TV is finer than the weak topology, so failing to be TV-open at Q implies failing to be weakly open. The paper should say this, and name the correct theorem. Note also that this route gives a second proof of Prop 1', since the commit set of a sound and complete updater is extensional.

A8. Lemma 3, soundness and completeness on the channel class. Plausible but unverified at the level of the primary statement. The underlying mathematics is sound. With a bounded computable likelihood density and a known bound, the normaliser ∫p(y|h)μ(dh) is computable relative to y, positive for P_Y-almost every y, and Bayes' formula gives the posterior. The claim "uniformly in the presentation and the bound" is correct for this argument. AFR's Corollary 9.6 ("Density and independence") is the relevant result, and the paper should cite it by number alongside 9.7.

A9. Lemma 3, the other three clauses (any prior, finite mixtures with the largest bound, products of conditionally independent sources bounded by the product of the bounds). Verified.

A10. "The class is closed under the agent's updating" (Sec 4.1). WRONG as stated. The observation y is generally not computable, so the posterior is computable only relative to y. It is not a computable measure, and so not a member of the class of computable channel presentations the paper defines. Fix: define the representational system relativised to oracles, i.e. y-computable channel presentations, and require the procedure to be uniform in the oracle. The procedure as described already is, so this is a repair to the definition rather than to the result.

A11. Noise-scale computation (Sec 5, Appendix). Verified. φ_s(e) ≤ (s√(2π))^-1, so the n-reading density is at most (2π)^(-n/2) E_π[s^-n], with equality at y_i = h. Hence it is bounded if and only if that moment is finite. For π ∝ e^(-1/s) on (0,1), substituting t = 1/s gives ∫_1^∞ t^(n-2) e^(-t) dt < ∞, and every interval (0,d) has positive mass. For π(s) = 2s, E[s^-1] = 2 but E[s^-2] = ∫2/s ds diverges, so it covers one reading but not two. Correct. Two caveats:
- The n readings are not conditionally independent given h once s is integrated out. So "for any number of readings" relies on a batch joint density, not on Lemma 3's product clause. Sequential updating needs the predictive density p(y_{k+1} | h, y_1..k) to be bounded, with a supplied bound. I believe it is bounded for π ∝ e^(-1/s), but the paper should say how this case enters the channel format.
- See S3 below on "learning about s".

A12. "A source with a bounded density given the hypotheses is one whose reading is not a function of them" (N5). Verified for atomless (continuous) sources. If Y = f(H) almost surely and p(·|h) is a density with respect to a σ-finite λ, then each f(h) must be an atom of λ. So f takes countably many values and P_Y has atoms. The converse fails: a reading that is not a function of the hypotheses need not have a bounded density (e.g. unbounded or singular noise). So "noisy" is weaker than what is actually required.

B. VERIFICATION OF CLAIMS ABOUT SOURCES

B1. AFR main result (a computable pair whose conditional distribution encodes the halting problem). Verified.

B2. "In the AFR examples the exact conditional distribution is badly discontinuous" (Sec 5). PARTLY WRONG. AFR give two constructions. In one, the conditional is discontinuous on a measure-one set. In the other, it has an everywhere continuous version that is still noncomputable and still computes the halting set. The generalisation to "the AFR examples" is false for the second.

B3. "AFR note that conditional distributions cannot in general be approximated uniformly by shrinking the noise" (Sec 1, Sec 5). Plausible but unverified. A search found no such statement in AFR's abstract or summaries. Give a precise location, or rephrase as the paper's own observation.

B4. "Corollary 9.7 in the arXiv and journal numbering" (independent noise). Verified for the journal version (J. ACM): 9.7 is "Independent noise" and 9.6 is "Density and independence". But the numbering differs across versions. The circulated preprint numbers it 8.9 (with 8.8 for density), the LICS 2011 paper numbers it Corollary 36, and Roy's 2011 thesis numbers it III.25. "The arXiv numbering" is true only of the latest arXiv version, if it matches the journal. Fix: cite the J. ACM numbering and the arXiv version number.

B5. AFR describe the noise condition as "independent computable noise with a sufficiently smooth bounded density". The paper says "bounded computable density". These are probably equivalent here, since a computable density is continuous, but the paper should match AFR's hypotheses exactly.

B6. Freer and Roy 2010. Verified. AISTATS 2010, PMLR 9: 233-240; add the pages. The paraphrase is acceptable: posteriors over the directing random measure are computable from the predictive distributions.

B7. Rescorla 2018. Verified: RSL 11(4): 705-735, Dutch book and converse Dutch book theorems for Kolmogorov conditionalization.

B8. Rescorla 2025. Verified: RSL 18(1), doi 10.1017/S1755020323000345, non-factive extension. Add the page range (starts at p. 186).

B9. Huttegger, Walsh and Zaffora Blando 2025. Verified: PPR 112(1): 307-324, which proposes computable probability theory for bounded Bayesians.

B10. Lopez-Wild 2026. Verified only through an aggregator: Philosophy of Science, doi 10.1017/psa.2026.10273. The paraphrase is plausible (he argues there are no merely finitely additive computable measures, which is a computability constraint on priors).

B11. Mahtani 2024. Verified: OUP, which argues that the objects of credence are hyperintensional.

B12. Hacking 1967 (Phil Sci 34(4): 311-325) and Garber 1983 (Minnesota Studies 10: 99-131). Consistent with my knowledge; not searched. The attributions are accurate.

B13. Kolmogorov 1933, and the remark that regular versions came later. Correct.

B14. Omitted literature. Meehan and Zhang (2020, RSL), "Kolmogorov conditionalizers can be Dutch booked (if and only if they are evidentially uncertain)", bears directly on Sec 6's Dutch book reply and should be addressed. Ackerman, Freer and Roy, "On computability and disintegration" (arXiv 1509.02992), is relevant to Sec 2's definitions.

C. REFEREE POINTS

[S1] The "only if" thesis is not established. The abstract says the learner "can follow the rule only if it models each continuous source as having a bounded likelihood density ... or else restricts its priors". The conclusion says this is "the general way". But N3/N5 only compare two formats: exact source models fail and bounded densities succeed. They do not rule out other formats, such as unbounded but integrable likelihoods with certified moment or integrability data, sources that mix an exact component with a noisy one, or exchangeable predictive formats. Sec 5 itself concedes "It does not claim that no other route could exist". So the abstract and conclusion contradict the body. Fix: restate the thesis as a sufficiency claim plus a failure result for exact models, or prove a genuine necessity theorem for a precisely defined class of source formats.

[S2] The closure-under-updating claim is false as stated (see A10). This matters for R4: the channel agent's system must contain its own posteriors. Fix: relativise the representational system to oracles.

[S3] The "open question" about learning the noise scale is already answered by the paper's own second route. Sec 5 says learning about s is "not covered, since the density given (h,s) is unbounded", and leaves it open. But with π ∝ e^(-1/s), the joint density of (s, y) given h with respect to Lebesgue measure ⊗ Lebesgue measure is π(s)φ_s(y-h), and this is bounded (since s^(-1)e^(-1/s) is bounded on (0,1), and likewise s^(-n)e^(-1/s)). So the posterior over (h, s) is computable by the same Bayes-formula argument as Lemma 3. This is exactly the "slack moved into the prior" route of the paper's first qualification, so it is an instance of restricting the prior over the hypothesis s. Fix: state that the joint (h, s) posterior is computable under this prior, and either drop the open question or reformulate it for priors on s with heavier mass near 0. Doing so also strengthens the "no floor" point.

[S4] The characterisation of AFR's examples is partly wrong (see B2). This weakens the "scale is substantive" argument, which leans on discontinuity. Fix: restrict the claim to the discontinuous construction, or base the argument on noncomputability rather than discontinuity.

[S5] The claim that AFR say shrinking the noise does not uniformly approximate the conditional is unlocated (see B3). Both the Introduction's novelty statement and Sec 5 rely on it. Fix: give the theorem or page number, or prove the claim.

[S6] Corollary 1 is missing the arithmetic hypothesis for Gödel's second theorem (see A6). Fix: add it.

[S7] Corollary 2's appeal to Rice-Shapiro is misattributed (see A7). Fix: cite Kreisel-Lacombe-Shoenfield/Ceitin, and note the step from TV to the weak topology.

[S8] The Dutch book reply (Sec 6) does not engage Meehan and Zhang 2020, who show that Kolmogorov conditionalizers can be Dutch-booked exactly when they are evidentially uncertain. Fix: show that the channel-modeller's joint posterior gives the learned reading credence 1 (for a proper version), or address the result directly.

[S9] The dichotomy in N3/N4 is not exhaustive, and the slogan "must model as noisy" is weaker than what is needed. Not being a function of the hypotheses is necessary for a bounded density but not sufficient (see A12). Fix: state the requirement as "bounded certified density", and stop using "noisy" as a gloss for it.

[S10] Representation-dependence and novelty. Prop 1' is an instance of a well-known phenomenon in computable analysis: an operation that is computable given extra data (here, a density bound) is not computable uniformly without it. The same holds for integrating a computable function with or without a supplied bound. The philosophical thesis of Sec 4 then largely reduces to FOLLOW plus this non-uniformity. In particular, the channel agent can follow the rule precisely because its format carries a promise (the bound) that cannot be checked; Sec 5 concedes as much under "What the certificate is". The paper should acknowledge this and argue for why the promise-based format deserves to count as a representational system the agent "follows" within, rather than as a stipulation that makes completeness trivial. Without that argument, R4 is close to definitional.

[S11] The definition of a presentation does not say which coordinates are hypotheses and which are observations. Completeness ("has a computable conditional distribution map") depends on this split. Fix: make the split part of the presentation.

[P1] The conclusion's last sentence drops the "or restrict priors" disjunct that the abstract includes. Make them agree.

[P2] Bibliography: add pages for Freer and Roy 2010 (233-240) and Rescorla 2025 (from p. 186). Specify which arXiv version of AFR is used.

[P3] R3 (capacity suffices for being bound) is asserted without defence, even though R5 depends on it.

[P4] The perception-modelling claim at the end of Sec 5 is uncited.

D. VERDICT
Major revision. The formal core (Lemmas 1-2, Props 1 and 1', Corollaries 1-2, the moment computation) is correct, up to small repairs. The philosophical theses overstate what the formal results show: the "only if", the closure claim, the noise-scale "open question", and the AFR characterisations all need fixing.

Scores: originality 5, correctness 6, importance 5.

Sources consulted: PhilSci Archive 27049 (HWZB); citedrive listing for doi 10.1017/psa.2026.10273; Cambridge Core pages for Rescorla 2018 and 2025; search summaries of AFR (arXiv 1005.3014, J. ACM 10.1145/3321699, danroy.org preprint and LICS 2011 versions); proceedings.mlr.press/v9/freer10a.html; LSE Research Online record for Mahtani 2024.
