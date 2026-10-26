---
title: "Calibrated Everywhere: A Dilemma for Track-Record Reliabilism about Credence"
---

# 1. Introduction

A reliabilist about justified credence needs a measure of reliability for processes that output credences. Measuring credences by their closeness to the truth values, as the Brier score does, penalizes middling credences even where nothing better is possible. The leading alternative, developed by Dunn (2015) from a suggestion of Ramsey's, is calibration: a process is well calibrated if, among the propositions to which it assigns credence $p$, a proportion $p$ are true. In the formulation of the *Stanford Encyclopedia* entry on reliabilism (Goldman and Beddor), a credence is justified iff it is produced by a well-calibrated process.

Calibrationists answered their first critics by making calibration modally robust and conditioning it on evidence. Both answers assume that a process calibrated without being suitably connected to the world is calibrated by luck, and that its calibration is therefore fragile. I argue that this assumption is false, and that its failure yields a dilemma for the main forms of calibrationist reliabilism.

*First horn.* Take a calibration standard with a positive tolerance (or a fixed smoothing bandwidth) whose reference classes are fixed independently of the process assessed and are finitely many, countably many, or of bounded complexity. Then some process that uses only the record of outcomes, and needs no assumption about how they are generated, meets the standard in every world. This follows from Foster and Vohra (1998) and its descendants. I add an elementary lemma: every such process has an ordinary chance world in which its credences are far from chances that a process with the same inputs and the same computational resources could match. So no such standard is sufficient for reliability.

*Second horn.* The standards that resist this construction make the reference classes relative to the process, or as rich as all computable classes, or assess calibration across worlds. They either remain insufficient or owe their discriminating power to agreement with the chances. Calibration relative to all computable classes, for instance, forces asymptotic agreement with the chances in every world whose chances are computable (Dawid 1985).

Through results on testing experts (Sandroni 2003; Olszewski and Sandroni 2008; Shmaya 2008), the first horn extends to outcome-based standards of a precisely specified kind. The positive upshot is a chance-relative account of reliability for credence, of the kind Tang (2016) proposed, graded by a standard measure from accuracy-first epistemology.

# 2. Calibrationism

## 2.1 Definitions

There is one yes-or-no question per day: will it rain on day $t$? Write $x_t\in\{0,1\}$. A *credence-forming process* issues on day $t$ a credence $f_t\in[0,1]$ that $x_t=1$. Its *inputs* are the history $h$: the day's index, earlier outcomes, and labels $z_1,\dots,z_t$ for the agent's other evidence (a barometer reading, say). It may also use a private randomizing device, with finitely many coin flips of rational bias per day. A randomizing process may use its own earlier credences, but these are recomputed from $h$ and its coins. A *history-based* process is one whose rule from inputs and coins to credences is fixed in advance. Bayesians with priors, frequentists and the procedures below are all history-based.

Fix a finite grid. Let $N_T(p)$ be the number of days up to $T$ with credence $p$, and $q_T(p)$ the proportion of them with rain. The calibration score is $C_T=\sum_p \frac{N_T(p)}{T}(q_T(p)-p)^2$, and a run is *$\varepsilon$-calibrated* if $\limsup_T C_T\le\varepsilon$. A *reference class* is a predictable checking rule, selecting days on information available before the outcome. Calibration relative to a family $\mathcal R$ requires $\varepsilon$-calibration on each infinite selected subsequence. *Smooth* calibration at bandwidth $\delta$ replaces grid cells by weighted averages over credences within $\delta$ of one another. A process is *calibrated in a world* if its run is calibrated with probability one under that world's chances and the process's coins. This is the only reading on which any process, including one whose credences equal the chances, can be calibrated throughout a range of worlds, since every world contains atypical runs.

## 2.2 The target

Let $X$ be a calibration standard and $W(w,\rho)$ the worlds relevant to assessing process $\rho$ at $w$ (actual, nearby, normal or all). The sufficiency half of calibrationist reliabilism is:

> **CR-S(X, W).** If $\rho$ is $X$-calibrated in every world of $W(@,\rho)$, then $\rho$ is reliable in the actual world $@$, and its credences are justified.

The first horn targets ranges that contain the actual world, as the actual-world and nearby-world versions do; Dunn requires looking at "the actual cases" as well as nearby worlds. Normal-worlds versions, which ground justification in reliability across normal worlds rather than in $@$, are discussed in 6.4. Necessity is not at issue.

## 2.3 How calibrationism answered its critics

The SEP entry reports Goldman's (1986) case: an agent seventy per cent of whose opinions are true is perfectly calibrated by giving everything credence 0.7. It also reports the reply that one should look across nearby worlds: if it is "just a matter of chance" that seventy per cent are true, the process will be miscalibrated in nearby worlds. Dunn writes that "we should not merely look at the actual cases that these processes have performed on. We must also look at how they perform in nearby worlds." The SEP attributes to Tang (2016) the objection that a process may be well calibrated while insensitive to relevant evidence. The natural reply is to condition calibration on evidence.

A natural case shows how far conditioning goes. In the *persistence world*, the chance of rain is 0.9 on a day after rain and 0.1 on a day after a dry day, so rain is half the days in the long run. A process that always says one half is calibrated there, and in every symmetric variant of the world. Yet the simple rule "0.9 after rain, 0.1 otherwise" uses the same inputs and matches the chances. Conditioning on yesterday's weather exposes the one-half process. The question is whether some process can be calibrated on that class, and on any other fixed class, in every world while still failing to track the chances. The theorems below say yes.

## 2.4 What calibration was meant to secure

(D1) A process should not be penalized for middling credences where the truth is not more predictable *from its inputs, by a process with its resources*. (D2) Reliability should be a matter of the track record, actual and counterfactual. I keep (D1) in this form and reject (D2).

# 3. Calibration without information

## 3.1 Theorems

**Theorem 1** (Foster and Vohra 1998; Foster 1999). For every $\varepsilon>0$ there is a randomized, history-based procedure on a finite grid that is $\varepsilon$-calibrated, almost surely, against every sequence of outcomes, including sequences chosen by an adversary who sees past outcomes and credences but not the current coin.

Qualifications. (i) For sharp calibration randomization is essential: every deterministic procedure is badly miscalibrated on the sequence on which it rains exactly when its credence is below one half (Oakes 1985; Dawid 1985). This is a descendant of Putnam's (1963) diagonal argument against universal inductive methods. (ii) "Every sequence" covers every chance process in which the weather is independent of the procedure's current coin. (iii) On a fixed grid a positive tolerance is needed. With grids refined over time, zero tolerance is attainable, so such standards also fall on the first horn. (iv) The expected $\ell_1$ calibration error per day can be kept slightly below order $T^{-1/3}$ uniformly (Dagan et al. 2025 improve the classical $T^{-1/3}$), while no procedure guarantees better than about $T^{-0.46}$ (Qiao and Valiant 2021; Dagan et al. 2025).

*Deterministic procedures.* Kakade and Foster (2004) obtained deterministic weak calibration. Foster and Hart (2018) show that "smooth calibration can be guaranteed by deterministic procedures", even when forecasts are announced in advance, with finite recall and a finite grid, at each fixed bandwidth and positive tolerance.

*Reference classes.* For each countable family of checking rules there is a procedure calibrated on all of them, against every sequence (Sandroni, Smorodinsky and Vohra 2003). Foster, Rakhlin, Sridharan and Tewari (2011) treat uncountable families of bounded complexity, and online multicalibration (Gupta et al. 2022) treats families of overlapping groups defined by labels. The quantifiers matter: for each family there is a procedure.

None of these procedures needs any assumption about how outcomes are generated. Call a procedure *uninformed* in this sense. Labels enter only as labels. For finite families, the procedures are computable.

## 3.2 The anti-tracking lemma

Let $\rho$ be history-based, with credence $\varphi_t(h,u)$ given history $h$ and coins $u$. Its *propensity* is $\bar f_t(h)=\int\varphi_t(h,u)\,d\lambda(u)$, the average over all coins, a function of $h$ alone. The world $w_\rho$ is defined as follows. Labels come from any fixed mechanism independent of the coins. The chance of rain given $h$ is $c_t=0.9$ if $\bar f_t(h)<1/2$, and $c_t=0.1$ otherwise.

**Lemma.** In $w_\rho$: (a) on every day and history, $\int(\varphi_t-c_t)^2\,d\lambda\ge\left(\int|\varphi_t-c_t|\,d\lambda\right)^2\ge 0.16$; (b) for every path and horizon $T$, with probability at least $2/7$ over the coins, the average of $|\varphi_t-c_t|$ over the first $T$ days is at least 0.2.

Four features matter.

- *Exogeneity.* $w_\rho$ is an ordinary chance world: the chance of rain is a fixed function of past weather and labels, nothing in it reacts to the process, and the coins are independent of the weather.
- *Extremity.* The chances are 0.9 and 0.1, not middling.
- *Same inputs, same resources.* The chance is computable from $h$ relative to $\rho$'s own rule: average over the finitely many coin outcomes and compare with one half. So a process with $\rho$'s inputs and resources has credence $c_t$. If $\rho$ is computable, so is $w_\rho$, and a Bayesian whose prior gives $w_\rho$ positive weight merges with it (Blackwell and Dubins 1962). No single history-based learner merges with every such world, since each has its own.
- *Calibration ties.* The procedures of 3.1 are calibrated in their anti-tracking worlds, as everywhere. The process with credence $c_t$ is calibrated there too, almost surely (Appendix A2).

# 4. The first horn

The argument needs one normative premise.

> **(R)** Suppose that in world $w$ the chance of rain given $\rho$'s inputs is computable from those inputs relative to $\rho$'s rule. If on every day $\rho$'s chance-expected Brier inaccuracy exceeds that of the chance itself by at least 0.16, then $\rho$ is not reliable in $w$.

For a randomized rule, the chance-expected inaccuracy averages over its coins as well. Call a standard $S$ *world-independently securable* if some history-based process meets $S$ in every world.

1. For every history-based $\sigma$ there is a world $w_\sigma$ that meets the antecedent of (R) for $\sigma$. (Lemma (a), and the excess Brier inaccuracy of $f$ over $c$ is $(f-c)^2$.)
2. So every history-based process has a world in which it is not reliable. (1, R)
3. If $S$ is world-independently securable, witnessed by $\sigma$, and sufficient for reliability, then $\sigma$ is reliable in every world, contradicting 2.
4. So no world-independently securable standard is sufficient for reliability.
5. Let $X$ be sharp with positive tolerance, smooth at a fixed bandwidth, or zero-tolerance with refining grids. Let its family be fixed independently of the process and be finite, countable or of bounded complexity. Then for any range $W$, "$X$-calibrated in every world of $W(@,\rho)$" is world-independently securable. (Theorem 1 and its strengthenings: the witness is calibrated in every world.)
6. Let $@=w_\sigma$, where $\sigma$ witnesses step 5. If $W(@,\sigma)$ contains $@$, then CR-S$(X,W)$ says $\sigma$ is reliable in $@$, contradicting 2. Since calibrationists ground justification in reliability, CR-S$(X,W)$ is false for every such $W$.

Three remarks.

*The flagship case.* For smooth calibration the witness is the deterministic Foster-Hart procedure. Its distance from the chance in its world is at least 0.4 on every day of every run. No question of individuation or probability arises.

*Individuation.* For sharp calibration the witness is randomized. The argument assesses the randomized rule, both for calibration (almost surely, in each world) and for reliability (averaging over coins). One may instead individuate narrowly, fixing the coin sequence so that the process is deterministic. Narrow individuation makes sense only for standards evaluated on the actual run: each deterministic process is miscalibrated in its own diagonal world, so none is calibrated throughout a rich range. For actual-run standards, Lemma (b) gives a positive-probability set of runs on which the coin-fixed process is calibrated yet on average 0.2 from the chances. Identifying the credence with the propensity leads to 5.1.

*Finite horizons.* (R) is stated day by day, so the argument applies at any horizon. A finite-horizon standard with a tolerance is securable beyond a horizon that depends on the tolerance. Sandroni's theorem (Section 7) removes even this restriction, at the cost of an infeasible witness.

The assumption of Section 2.3 has now failed. The uniform 0.7 process is calibrated by luck, and the Foster-Vohra procedure by design. If any process $Q$ is calibrated throughout a set of worlds, so is the procedure. So modal robustness cannot favour $Q$ over it.

## 4.1 Defending (R)

(R) is chance-relative. A calibrationist who identifies reliability with calibration will reject it (6.1). There are three reasons to accept it.

*It respects (D1).* (R) applies only where a process with the same inputs and resources could match the chances. In the hidden-sequence world of 5.1, where the chances are fixed by a random sequence no such process can compute, (R) is silent.

*It is backed by the record.* Let $\rho^*$ have credence $c_t$. On every run, the difference between the realized average Brier scores of $\rho$ and $\rho^*$ equals the average of $(f_t-c_t)^2$ plus an average of bounded martingale differences, which tends to zero almost surely. So $\rho$'s realized score exceeds $\rho^*$'s by at least about 0.16 in the limit for the deterministic witness, and by a positive margin with positive probability for the randomized one. The randomized process's chance-expected inaccuracy is at least $0.16+0.09=0.25$ every day, as bad as always saying one half; $\rho^*$'s is $0.09$. Both are calibrated. The record that calibration consults separates them, but calibration does not.

*It concerns reliability, not yet justification.* (R) says nothing about justification. The step to justification in step 6 is the calibrationist's own: reliability grounds justification. Intuitive verdicts about justification are clearest in the unconditional case. An agent who has an informative barometer, ignores it, and keeps a calibrated record by the Foster-Vohra procedure is calibrated in every world. Unconditional calibrationism counts her credences as justified, and they plainly are not.

# 5. The second horn

Step 5 requires the family to be fixed independently of the process and to be of bounded richness. There are three ways to violate this. They are the main ways, though not the only conceivable ones.

## 5.1 Propensity-binned reference classes

For a randomizing agent, the propensity is a candidate for the credence. So let $\mathcal R(\rho)$ include the classes $\{t:\bar f_t\in I\}$ for rational intervals $I$. In $w_\rho$, with tolerance below about 0.1, the probability that $\rho$ is calibrated on these classes is at most $5/9$ (Appendix A3), so the standard is not securable. It still needs rich fixed classes to be sufficient. For any countable family $\mathcal R$, there is a sequence $b$ such that, in the world where the chance is $0.1+0.8b_t$, the always-one-half process is calibrated on every class in $\mathcal R$ almost surely (Appendix A4). Its distance from the chances is 0.4 every day. For such $b$, typically no process with the one-half process's resources could compute the chances, so (R) is silent. That is the right verdict by (D1). But it also means the always-one-half process passes. A propensity-binning calibrationist must therefore enrich the fixed classes until they capture every chance structure a process could compute. That is the next case.

## 5.2 Computable calibration

Restrict processes to computable ones, and let $\mathcal R$ be all computable checking rules. For a computable $\rho$, $w_\rho$ is computable, and so is the class $\{t:\bar f_t<1/2\}$. By A3, no computable process is calibrated on all computable rules in every world. (The Sandroni-Smorodinsky-Vohra procedure for this countable family exists, but by the same argument it is not computable.) This view is close to Dawid's (1985) calibration-based theory of empirical probability, and it is the strongest calibrationism I know. Dawid shows that any two forecast sequences calibrated, in his averaged sense, on all computable rules "must be in asymptotic agreement". In a computable chance world the chance-matcher meets that criterion almost surely (A2). So, on almost every run, a computable process that meets it agrees asymptotically with the chances. Computable calibrationism escapes the first horn by becoming, in computable worlds, a criterion of asymptotic agreement with the chances.

The Dawidian may welcome this as vindication: calibration reveals chance. Three points tell against reading it as vindication of (D2). First, the direction of derivation. The chance-matcher is calibrated because its credences equal the chances and the law of large numbers holds. Calibration discriminates in Dawid's theorem only because it pins down the forecasts of a process that matches the chances. Second, every restriction of the rule family that makes the standard checkable on a record of credences is a restriction to a fixed family of bounded richness, and so falls on the first horn. The calibration of a process on that record never settles its reliability, because the uninformed witness has the same record. Third, a reductive Dawidian who defines chance as what computable calibration determines thereby accepts the chance-relative view of Section 8, with a reductive theory of chance. The disagreement is then about chance, not about whether reliability is a track-record property.

## 5.3 Cross-world calibration

Dunn's slogan can be read synchronically: among nearby worlds sharing the history in which the process gives $p$, a proportion $p$ have rain. That needs a measure on worlds, and the natural one is the chance distribution over continuations. On it, the proportion at a history is the chance given the history, and calibration at each history is chance-matching. Pooling across histories (requiring only that rain have probability $p$ given credence $p$) is weaker. A process that always announces the marginal chance meets it, which is Tang's insensitivity case again, and the standard needs the chances anyway. A similarity measure not derived from chances would have to make cross-world proportions approximate chances to deliver the intended verdicts. Otherwise it is open to the same constructions.

## 5.4 Other strengthenings

*Calibration plus refinement.* Forecast verification has long required more than calibration: "maximizing the sharpness of the predictive distributions subject to calibration" (Gneiting, Balabdaoui and Raftery 2007; cf. Seidenfeld 1985). An absolute sharpness threshold violates (D1). A threshold relative to what is attainable from the inputs is the chance condition. Comparative versions are discussed in 6.5.

*Deterministic sharp calibration over rich ranges.* No deterministic process is sharply calibrated in its own diagonal world, so over ranges containing each process's diagonal world this standard counts no deterministic credence as justified. Over ranges that hold the chance law fixed, the persistence world and A4 show that it is insufficient.

*Rate-sensitive standards.* A chance-matcher's $\ell_1$ calibration error is of order $\sqrt{T}$ over $T$ days, faster than any uniform guarantee. A finite-horizon standard requiring that rate is, however, a test that the chance-matcher passes with high probability. Sandroni's theorem then supplies an uninformed passer, though no feasible one.

# 6. Objections

## 6.1 Reliability just is calibration, perhaps relative to a repertoire

The calibrationist may reject (R) and identify reliability with calibration, perhaps relative to the agent's repertoire of reference classes $\mathcal R$. Then for each $\mathcal R$ some process is maximally reliable in every environment, so reliability says nothing about the fit between process and environment. It also counts as maximally reliable a process whose realized Brier score exceeds, by a fixed margin, that of a same-resource process in the same environment. If instead $\mathcal R$ is chosen world-relatively, to include whatever classes the world's chances depend on, chance has been reintroduced. Pettigrew (2021) presses a Connection Problem against existing reliabilist accounts of justified credence: it is unclear how justification so understood connects to epistemic value. On the definitional reply, maximal reliability is compatible with every degree of avoidable inaccuracy, so the problem becomes acute.

## 6.2 The witness is a learner

The Foster-Vohra procedure learns from outcomes, and in i.i.d. worlds calibration forces its credences toward the frequencies. I grant this. The argument needs only that CR-S is wrong about it in its anti-tracking world. Is self-correction of one's record a cognitive virtue? Dawid (1982) proved that a coherent Bayesian assigns probability one to being well calibrated, and Oakes (1985) reports Dawid's observation that a coherent forecaster cannot correct past miscalibration without sacrificing coherence. The Foster-Vohra procedure does exactly that. Its calibration holds in every world because it is secured by bookkeeping rather than earned by fit, and so it is no evidence of fit with any world.

## 6.3 Generality

A broad type such as "extrapolating from the weather record" contains processes that are miscalibrated in $w_\rho$. A calibrationist who types broadly may therefore condemn the procedure there. But then the verdict depends on the typing, not on the procedure's fit with the world. The procedure is an admissible type for any agent who implements it. Excluding it would need a principle that distinguishes it from good learners by something other than calibration.

## 6.4 Demon worlds and normal worlds

By (R), a demon victim's process is unreliable in the demon world. That is the standard reliabilist verdict, and reliabilists who want to call the victim justified assess reliability in normal worlds. Calibrationism's distinctive verdict is that the Foster-Vohra process is reliable even in its anti-tracking world. That verdict extends to the agent who ignores her barometer, so it overgenerates.

Normal-worlds calibrationism (Goldman 1986 characterizes normal worlds by our general beliefs about the actual world) is not refuted by step 6. That step requires $@\in W$. The first horn shows that calibration across the normal worlds does not secure reliability in each of them, since $w_\sigma$, an exogenous chance process of a familiar kind, is consistent with general beliefs such as "tomorrow's weather depends on recent weather in some stable way". Whether calibration secures reliability on aggregate across normal worlds depends on how much weight anti-tracking worlds receive. I leave this open.

## 6.5 Comparative calibrationism

Suppose reliability requires being calibrated and not beaten in realized accuracy by any member of a fixed countable class $\mathcal C$ of same-input processes. Work on "calibeating" (Foster and Hart 2023) studies forecasters that beat a given forecaster's Brier score using calibration with respect to that forecaster's forecasts. If, as this suggests, some history-based forecaster's realized score is asymptotically no worse than that of each member of $\mathcal C$ on every sequence, the standard is securable. In that forecaster's anti-tracking world, every member of $\mathcal C$ then has average excess Brier inaccuracy bounded away from zero along unboundedly many horizons. If instead $\mathcal C$ contains every world's chance-matcher, the standard measures closeness to the chances by another name. A related structure is meta-inductive optimality (Schurz 2019): a world-independent guarantee relative to accessible methods. By step 4, a world-independent guarantee is a different virtue from reliability.

# 7. Beyond calibration

A *test* passes or fails a forecaster on the forecasts and the data. It *controls type I error* at level $\eta$ if a forecaster who forecasts by the true probabilities passes with probability at least $1-\eta$, whatever they are.

**Theorem 2.**
(a) (Sandroni 2003.) Over a finite horizon, every test controlling type I error at level $\eta$ can be passed, whatever the data, with probability at least $1-\eta-\delta$ by an uninformed forecaster. The forecaster draws a theory at the outset, by a distribution obtained from Fan's minimax theorem.
(b) (Olszewski and Sandroni 2008.) The same holds for future-independent tests that reject theories in finite time. In their words, "tests which cannot be ignorantly passed must rely on predictions about data not yet observed, and such tests cannot be run if forecasters report only the probability of the next period's events on the basis of the actually observed data."
(c) (Shmaya 2008.) If a test is Borel and a forecaster who knows the truth always passes it, an ignorant forecaster can pass it with probability arbitrarily close to one.

A record of credences actually formed is what Olszewski and Sandroni describe: next-period probabilities on the observed data. Running the first horn with Theorem 2 in place of step 5, using Lemma (a) for the randomized forecaster, gives:

> **(G)** Consider any standard on the record of credences actually formed that is (i) finite-horizon, or (ii) future-independent and rejecting in finite time, and is met by a chance-matcher with high probability in every world; or (iii) Borel and met by a chance-matcher with probability one in every world. No such standard is sufficient for reliability, provided processes as powerful as the witnesses of Theorem 2 are admitted.

The proviso matters. The witnesses need not be computable, and so (R) applies to them only relative to their own resources. The theorems are also stated without labels; with labels, the data must include them. (G) is narrower than "no outcome-based test separates informed from uninformed forecasters", which is false. Each exception brings in something beyond the record.

*Predictions about unobserved data.* Dekel and Feinberg (2006) give a test that the truth passes and that false theories fail on all but a topologically small set; their strongest result uses the continuum hypothesis. Olszewski and Sandroni (2009b) give a non-manipulable test that controls type I error without that hypothesis. Both use a theory's predictions about data not yet observed, which a record of credences does not contain.

*Computational bounds.* Fortnow and Vohra (2009) give an efficient test that, under standard hardness assumptions, no efficient uninformed forecaster passes. Hu and Shmaya (2013) give a computable test that accepts true experts with high probability and that no computable strategy manipulates. So if only computable processes are admitted, (G) fails. This fits Section 5.2: computational restrictions are where calibrationism's best hope lies, and there it meets Dawid's agreement theorem.

*Restricted theories.* Restricting admissible theories to those with learnable and predictive representations yields non-manipulable tests (Al-Najjar, Sandroni, Smorodinsky and Weinstein 2010). Olszewski and Sandroni (2009a) conclude that such restrictions help "only to a limited extent".

*Comparison.* Al-Najjar and Weinstein (2008) give a record-based test for two experts, one of whom knows the true distribution. It identifies the informed expert, or else finds the two experts' forecasts close. The single-expert impossibility, they note, arises because nature's mixtures over distributions reduce to pure strategies, and the presence of an informed expert prevents this. The test's guarantee presupposes a competitor whose forecasts are the chances. Feinberg and Stewart (2008) treat several forecasters.

# 8. What reliability for credence must be

Tang's indicator view, as the SEP reports it, holds that a credence $C(p)$ is justified only if it is based on a ground $g$ such that the objective probability of $p$ given $g$ approximates $C(p)$. Clifton's "statistical reliabilism" measures the justification of statistical credences by their average closeness to the corresponding objective probabilities. Both horns point to views of this kind, with the ground identified with what the process takes as input. I do not claim that the measure is new. For the Brier score, the chance-expected inaccuracy of credence $f$ when the chance given the ground is $c_g$ is $(f-c_g)^2+c_g(1-c_g)$. The second term is the inaccuracy the ground leaves unavoidable. The first, the excess, measures unreliability; for a general strictly proper score it is the associated divergence. Chance-expected accuracy is already central in accuracy-first epistemology (Pettigrew 2016 derives chance-credence norms from chance dominance). The measure satisfies (D1), since matching middling chances incurs no excess. And it connects reliability to accuracy, which the Connection Problem demands.

Three clarifications are needed. First, (D1) restricts the ground to what the process can use, and (R) restricts it to what the process could compute. Under determinism with fine-grained grounds the chance given the ground is 0 or 1, and the excess condemns any middling credence. The view must therefore relativize grounds to the process's resources, as (R) does. That is the version the arguments support. Second, inputs that a process receives but ignores are not grounds of its credences. The basing relation selects which inputs count. Third, Pettigrew (2021) argues that Dunn's process view and Tang's indicator view, suitably understood, are extensionally equivalent, and offers a hybrid. The present results constrain the suitable understanding: calibration read as a track-record property is securable by an uninformed process, and chance given grounds is not. So the equivalence cannot hold on the track-record reading.

Calibration seemed right because a chance-matching process is calibrated almost surely, in the sense of Section 2.1 when the chances lie on the grid, and in the averaged sense for every countable family of predictable rules (A2; the own-prior version is Dawid's 1982 theorem). Calibration is how reliability shows up in the record. The theorems show that it can show up without it, in every world.

*The Humean worry.* If chances supervene on the total pattern, is the chance condition itself a test subject to (G)? Type I error control presupposes chances fixed in advance of the data. The theorems quantify over fixed data-generating measures, whereas a Humean chance is fixed by the pattern it summarizes. A Humean chance-matching condition, as a function of the whole infinite record, is not a finite-time test, so (G)(i) and (G)(ii) do not apply. Shmaya's theorem could apply if the best-system map were Borel, but only if a forecaster who knows the truth passed with probability one under every measure. That is doubtful for best-system chances, which can diverge from a non-ergodic measure. I flag this as the point where the positive view's independence from (G) is least secure.

The view has a cost, and I accept it. Reliability cannot be read off a finite record, and by (G) no record-based surrogate of the specified kinds certifies it. This is the externalist's standard situation: reliability need not be knowable to the agent to make her justified.

# 9. Conclusion

The modal and evidential defences of calibrationism assumed that uninformed calibration is lucky and fragile. The Foster-Vohra theorem and its descendants show that it can be secured by design, in every world, for any fixed family of reference classes of bounded richness. Every history-based process has an exogenous world in which a process with its inputs and resources matches the chances while it does not. So no securable standard is sufficient for reliability. The standards that resist securing do so by building in agreement with the chances, or remain insufficient. Reliability for credence is a relation to chances given grounds. Calibration is how such reliability shows up in the record, not what it consists in.

# Appendix

**A1. Lemma.** The propensity $\bar f_t(h)$ is a finite average over coin outcomes, so it depends on $h$ alone, and $w_\rho$ is well defined (Ionescu-Tulcea). Outcomes and labels depend only on the past and on the label mechanism, so the coins are independent of the weather. (a) If $\bar f_t<1/2$ then $\int|\varphi_t-0.9|\,d\lambda\ge 0.9-\bar f_t>0.4$; otherwise $\int|\varphi_t-0.1|\,d\lambda\ge\bar f_t-0.1\ge0.4$; then apply Jensen. (b) Fix a path. The average distance $D_T$ lies in $[0,0.9]$ and has mean at least 0.4. With $P=\lambda(D_T\ge0.2)$, $0.4\le0.9P+0.2(1-P)$, so $P\ge2/7$. $\square$

**A2. Chance-matchers are calibrated.** On days selected by a predictable rule, the $x_t-c_t$ are bounded martingale differences. By the martingale strong law, on the event that infinitely many days are selected, their average tends to zero almost surely. Within the cells for 0.9 and 0.1 this gives calibration in $w_\rho$, and countable unions extend it to countable families. With continuum-valued chances it gives, for each rule, convergence of mean credence minus mean outcome.

**A3. Propensity-binned calibration.** Fix a path in $w_\rho$ and let $G$ be the set of coin sequences on which $\rho$ is calibrated on the propensity classes, with tolerance below about 0.1. Suppose $A=\{t:\bar f_t<1/2\}$ is infinite. There the frequency of rain tends to 0.9 (A2). So on $G$ the average realized credence over $A$ tends to within about 0.3 of 0.9, so it exceeds 0.6. Its coin-average equals the average propensity over $A$, which is below 1/2, and credences are non-negative. Hence $0.6\,\lambda(G)\le 1/2$ in the limit. If $A$ is finite, the complement is infinite, the frequency there tends to 0.1, and on $G$ the average credence is below 0.4. Its coin-average is at least 1/2, so $0.4\,\lambda(G)+(1-\lambda(G))\ge1/2$. Either way, $\lambda(G)\le 5/6$, and with smaller tolerances the bound approaches $5/9$. So the standard is not met in $w_\rho$ with probability one. $\square$

**A4. Hidden-sequence world.** Let $B_t$ be independent fair bits and, given $B$, let $x_t$ be independent with chance $0.1+0.8B_t$. Unconditionally, each $x_t$ given the past is a fair coin, so on every predictable rule the frequency of rain tends to one half almost surely (A2), and the one-half process is calibrated on any countable family. By Fubini, the same holds almost surely in the world with chances $0.1+0.8b_t$, for almost every fixed $b$. If the family contains all computable rules, such $b$ are not computable. $\square$

# References

Al-Najjar, N. I., Sandroni, A., Smorodinsky, R. and Weinstein, J. (2010). Testing theories with learnable and predictive representations. *Journal of Economic Theory* 145(6): 2203-2217.

Al-Najjar, N. I. and Weinstein, J. (2008). Comparative testing of experts. *Econometrica* 76(3): 541-559.

Blackwell, D. and Dubins, L. (1962). Merging of opinions with increasing information. *Annals of Mathematical Statistics* 33: 882-886.

Clifton, J. Reliable credence and the foundations of statistics. Manuscript, PhilArchive (CLIRCA).

Dagan, Y., Daskalakis, C., Fishelson, M., Golowich, N., Kleinberg, R. and Okoroafor, P. (2025). Breaking the $T^{2/3}$ barrier for sequential calibration. *Proceedings of the 57th Annual ACM Symposium on Theory of Computing*, 2007-2018.

Dawid, A. P. (1982). The well-calibrated Bayesian. *Journal of the American Statistical Association* 77: 605-610.

Dawid, A. P. (1985). Calibration-based empirical probability. *Annals of Statistics* 13(4): 1251-1274.

Dekel, E. and Feinberg, Y. (2006). Non-Bayesian testing of a stochastic prediction. *Review of Economic Studies* 73(4): 893-906.

Dunn, J. (2015). Reliability for degrees of belief. *Philosophical Studies* 172(7): 1929-1952.

Feinberg, Y. and Stewart, C. (2008). Testing multiple forecasters. *Econometrica* 76(3): 561-582.

Fortnow, L. and Vohra, R. V. (2009). The complexity of forecast testing. *Econometrica* 77(1): 93-105.

Foster, D. P. (1999). A proof of calibration via Blackwell's approachability theorem. *Games and Economic Behavior* 29: 73-78.

Foster, D. P. and Hart, S. (2018). Smooth calibration, leaky forecasts, finite recall, and Nash dynamics. *Games and Economic Behavior* 109: 271-293.

Foster, D. P. and Hart, S. (2023). "Calibeating": beating forecasters at their own game. *Theoretical Economics* 18(4): 1441-1474.

Foster, D. P., Rakhlin, A., Sridharan, K. and Tewari, A. (2011). Complexity-based approach to calibration with checking rules. *Proceedings of the 24th Annual Conference on Learning Theory*, PMLR 19: 293-314.

Foster, D. P. and Vohra, R. V. (1998). Asymptotic calibration. *Biometrika* 85(2): 379-390.

Gneiting, T., Balabdaoui, F. and Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. *Journal of the Royal Statistical Society B* 69(2): 243-268.

Goldman, A. (1986). *Epistemology and Cognition*. Cambridge, MA: Harvard University Press.

Goldman, A. and Beddor, B. Reliabilist epistemology. In E. N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy*.

Gupta, V., Jung, C., Noarov, G., Pai, M. M. and Roth, A. (2022). Online multivalid learning: means, moments, and prediction intervals. *13th Innovations in Theoretical Computer Science Conference*, LIPIcs 215: 82:1-82:24.

Hu, T.-W. and Shmaya, E. (2013). Expressible inspections. *Theoretical Economics* 8(2): 263-280.

Kakade, S. M. and Foster, D. P. (2004). Deterministic calibration and Nash equilibrium. *Proceedings of the 17th Annual Conference on Learning Theory*, 33-48.

Oakes, D. (1985). Self-calibrating priors do not exist. *Journal of the American Statistical Association* 80: 339.

Olszewski, W. and Sandroni, A. (2008). Manipulability of future-independent tests. *Econometrica* 76(6): 1437-1466.

Olszewski, W. and Sandroni, A. (2009a). Strategic manipulation of empirical tests. *Mathematics of Operations Research* 34(1): 57-70.

Olszewski, W. and Sandroni, A. (2009b). A nonmanipulable test. *Annals of Statistics* 37(2): 1013-1039.

Pettigrew, R. (2016). *Accuracy and the Laws of Credence*. Oxford: Oxford University Press.

Pettigrew, R. (2021). What is justified credence? *Episteme* 18(1): 16-30.

Putnam, H. (1963). "Degree of confirmation" and inductive logic. In P. A. Schilpp (ed.), *The Philosophy of Rudolf Carnap*, 761-783. La Salle, IL: Open Court.

Qiao, M. and Valiant, G. (2021). Stronger calibration lower bounds via sidestepping. *Proceedings of the 53rd Annual ACM Symposium on Theory of Computing*.

Sandroni, A. (2003). The reproducible properties of correct forecasts. *International Journal of Game Theory* 32: 151-159.

Sandroni, A., Smorodinsky, R. and Vohra, R. V. (2003). Calibration with many checking rules. *Mathematics of Operations Research* 28(1): 141-153.

Schurz, G. (2019). *Hume's Problem Solved: The Optimality of Meta-Induction*. Cambridge, MA: MIT Press.

Seidenfeld, T. (1985). Calibration, coherence, and scoring rules. *Philosophy of Science* 52(2): 274-294.

Shmaya, E. (2008). Many inspections are manipulable. *Theoretical Economics* 3: 367-382.

Tang, W. H. (2016). Reliability theories of justified credence. *Mind* 125(497): 63-94.
