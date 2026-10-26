---
title: "Calibrated Everywhere: A Dilemma for Track-Record Reliabilism about Credence"
---

**Abstract.** Calibrationist reliabilism holds that a credence is justified if it is produced by a well-calibrated process. Its defenders answered early counterexamples by requiring calibration to be modally robust and conditioned on evidence. Both answers assume that calibration without connection to the world is lucky and fragile. Results in the theory of forecasting show that it is not: for any fixed family of reference classes of bounded richness, some process that needs no assumption about how outcomes are generated is calibrated in every world. Adding an elementary diagonal lemma, I show that no such standard suffices for reliability in the actual or nearby worlds. The standards that escape this construction either fail in other ways or are coextensive with agreement with the chances. Reliability for credence is better understood as a relation to chances given grounds.

# 1. Introduction

A reliabilist about justified credence needs a measure of reliability for processes that output credences. Measuring credences by their closeness to the truth values penalizes middling credences even where nothing better is possible. The leading alternative, due to Dunn (2015) and inspired by Ramsey, is calibration: a process is well calibrated if, among the propositions to which it assigns credence $p$, a proportion $p$ are true. In the formulation of the *Stanford Encyclopedia* entry on reliabilism (Goldman and Beddor), a credence is justified iff it is produced by a well-calibrated process.

I argue for a dilemma. On the first horn are calibration standards with a positive tolerance, or a fixed smoothing bandwidth, whose reference classes are fixed independently of the process assessed and are of bounded richness. Each is met in every world by a process that uses only the record and needs no assumption about how outcomes are generated (Foster and Vohra 1998 and descendants). Every such process has an ordinary chance world in which its credences are far from chances computable from its inputs relative to its own rule. So no standard on this horn is sufficient for reliability in the actual or nearby worlds. On the second horn are the standards that escape the construction: reference classes relative to the process, all computable classes, or calibration across worlds. These either remain insufficient, or are coextensive with agreement with the chances. In the computable case, coextension holds asymptotically, in every world with computable chances (Dawid 1985). Whether that vindicates calibration or the chances depends on the metaphysics of chance, and I argue that even then the limit standard fails for individual credences. Via results on testing experts (Sandroni 2003; Olszewski and Sandroni 2008; Shmaya 2008), the first horn extends to outcome-based tests of a specified kind. The positive upshot is a chance-relative account of reliability for credence, close to Tang (2016).

# 2. Calibrationism

## 2.1 Definitions

There is one yes-or-no question per day: will it rain on day $t$? Write $x_t \in \{0,1\}$. A *credence-forming process* issues credence $f_t \in [0,1]$ that $x_t = 1$. Its *inputs* are the history $h$: the day's index, earlier outcomes, and labels $z_1, \dots, z_t$ for the agent's other evidence. It may also use a private randomizing device. Its earlier credences, where it uses them, are recomputed from $h$ and its coins. A process is *history-based* if its rule from inputs and coins to credences is fixed in advance. Bayesians, frequentists and the procedures below are all history-based. *Worlds* are chance processes for outcomes and labels in which each day's outcome is independent of the process's current coin, given the past.

Fix a finite grid. With $N_T(p)$ the number of days up to $T$ with credence $p$, and $q_T(p)$ the proportion of them with rain, the calibration score is $C_T = \sum_p \frac{N_T(p)}{T}(q_T(p) - p)^2$. A run is *$\varepsilon$-calibrated* if $\limsup_T C_T \le \varepsilon$. A *reference class* is a predictable checking rule, which may consult the history and the current credence. Calibration relative to a family $\mathcal R$ requires $\varepsilon$-calibration on each infinite selected subsequence. *Smooth* calibration at bandwidth $\delta$ replaces grid cells by weighted averages over nearby credences. I regiment "calibrated in a world" as calibrated with probability at least $1-\kappa$ under that world's chances and the process's coins, for a threshold $\kappa$; the default is $\kappa = 0$. Any range of worlds contains atypical runs. So on a run-by-run reading not even a process whose credences equal the chances is calibrated throughout a range.

## 2.2 The target

> **CR-S(X, W).** Necessarily: if $\rho$ is $X$-calibrated in every world of $W(@,\rho)$, then $\rho$ is reliable in the actual world $@$, and its credences are justified.

The first horn concerns ranges that contain the actual world, such as actual-world and nearby-world ranges. Dunn asks us to look at "the actual cases" and at nearby worlds. Normal-worlds versions are discussed in 6.4. Necessity is not at issue. Dunn's own topic is the measurement of reliability; the step to justification is the SEP's formulation and the reliabilist's bridge.

## 2.3 How calibrationism answered its critics

The SEP reports Goldman's (1986) case: an agent seventy per cent of whose opinions are true is perfectly calibrated by giving every proposition credence 0.7. It also reports the reply that we should look across nearby worlds. If it is "just a matter of chance" that seventy per cent are true, the process is miscalibrated in nearby worlds. Dunn writes that "we should not merely look at the actual cases that these processes have performed on. We must also look at how they perform in nearby worlds." The SEP attributes to Tang (2016) the objection that a process may be calibrated while insensitive to relevant evidence. The natural reply is to condition calibration on evidence.

A natural case shows how far conditioning goes. In the *persistence world*, the chance of rain is 0.9 after a rainy day and 0.1 after a dry day. The process that always says one half is calibrated there, and in every symmetric variant, while the rule "0.9 after rain, 0.1 otherwise" uses the same inputs and matches the chances. Conditioning on yesterday exposes the one-half process. The question is whether some process can be calibrated on that class, and on any other fixed class, in every world, while failing to track the chances. The theorems below say yes.

## 2.4 What calibration was meant to secure

Calibration was meant to avoid penalizing middling credences where the truth is not more predictable. Dunn's motivating worry concerns credences like one half about a fair coin. I read this as (D1): a process should not be penalized where the truth is not more predictable *from its inputs, by a rule computable relative to its own*. The italicized rider is my regimentation, not Dunn's. (D2) Reliability is a matter of track record, actual and counterfactual. I keep (D1) and reject (D2).

# 3. Calibration without information

## 3.1 Theorems

**Theorem 1** (Foster and Vohra 1998; Foster 1999). For every $\varepsilon > 0$ there is a randomized history-based procedure on a finite grid that is $\varepsilon$-calibrated, almost surely, against every sequence of outcomes. This includes sequences chosen by an adversary who sees past outcomes and credences but not the current coin.

Qualifications. (i) Randomization is essential for sharp calibration. Every deterministic procedure is miscalibrated on the sequence on which it rains exactly when its credence is below one half (Oakes 1985; Dawid 1985). This is a descendant of Putnam's (1963) diagonal argument against universal inductive methods. (ii) On a fixed grid a positive tolerance is needed, since chances may lie off the grid. With grids refined over time, zero tolerance is attainable. (iii) Per day, the expected $\ell_1$ calibration error can be kept slightly below $T^{-1/3}$ uniformly (Dagan et al. 2025 improve the classical $T^{-1/3}$), and no procedure guarantees better than about $T^{-0.46}$ (Qiao and Valiant 2021; Dagan et al. 2025).

*Deterministic procedures.* Kakade and Foster (2004) obtained deterministic weak calibration. Foster and Hart (2018) show that "smooth calibration can be guaranteed by deterministic procedures", even when forecasts are announced in advance, with finite recall and a finite grid, at each fixed bandwidth and positive tolerance. Their result is unconditional. It extends to finitely many reference classes that depend only on the history (not on the current credence). Run a separate copy on each atom of the partition the classes generate; each copy faces a sequence and is smoothly calibrated on it, and each class is a union of atoms, with the tolerance scaled by the number of atoms.

*Randomized procedures and reference classes.* For each countable family of checking rules there is a procedure calibrated on all of them against every sequence (Sandroni, Smorodinsky and Vohra 2003). Foster, Rakhlin, Sridharan and Tewari (2011) treat families of bounded complexity, and online multicalibration (Gupta et al. 2022) treats overlapping groups defined by labels. For each family there is a procedure; no single procedure serves every family.

None of these procedures needs an assumption about how outcomes are generated. Labels enter only as labels.

## 3.2 The anti-tracking lemma

Let $\rho$ be history-based, with credence $\varphi_t(h,u)$ given history $h$ and randomization $u$, where $u$ has law $\lambda$. Its *propensity* is $\bar f_t(h) = \int \varphi_t(h,u)\, d\lambda(u)$, a function of $h$ alone. Define $w_\rho$ as follows. Labels come from any fixed mechanism independent of the coins, and the chance of rain given $h$ is $c_t = 0.9$ if $\bar f_t(h) < 1/2$, and $0.1$ otherwise.

**Lemma.** In $w_\rho$: (a) on every day and every history, $\int (\varphi_t - c_t)^2\, d\lambda \ge \left(\int |\varphi_t - c_t|\, d\lambda\right)^2 \ge 0.16$; (b) for every path and horizon $T$, with $\lambda$-probability at least $2/7$, the average of $|\varphi_t - c_t|$ over the first $T$ days is at least 0.2.

Features. *Exogeneity:* the chance is a fixed function of past weather and labels. Nothing reacts to the process, and its coins are independent of the weather. *Extremity:* the chances are 0.9 and 0.1. *Computability:* the chance is computable from $h$ relative to $\rho$'s rule, given rational credences and coin biases. This is computability, not feasibility, since the propensity averages over all coin paths. For a deterministic $\rho$, the matcher is literally "run $\rho$, then threshold at one half". *Learnability:* if $\rho$ is computable, so is $w_\rho$, and a Bayesian whose prior gives $w_\rho$ positive weight merges with it (Blackwell and Dubins 1962); no single learner merges with every such world. *Tie:* the procedures of 3.1 are calibrated in $w_\rho$, and the process with credence $c_t$ is calibrated there almost surely (A2). For the deterministic finite-recall witness, $w_\rho$ is a finite-order chance process, the kind of weather model one finds in textbooks. Witnesses for rich families have anti-tracking worlds whose chances depend on the whole history and are far from ordinary.

# 4. The first horn

> **(R)** Suppose that in world $w$ the chance of rain given $\rho$'s inputs is computable from those inputs relative to $\rho$'s rule. If on every day $\rho$'s chance-expected Brier inaccuracy, averaged over its coins, exceeds that of the chance by at least 0.16, then $\rho$ is not reliable in $w$.

Call a standard *world-independently securable* if some history-based process meets it in every world.

1. Every history-based $\sigma$ has a world $w_\sigma$ meeting the antecedent of (R). (Lemma (a). The excess Brier inaccuracy of $f$ over $c$ is $(f - c)^2$.)
2. So every history-based process has a world in which it is not reliable. (1, R)
3. So no world-independently securable standard is sufficient for reliability. (If $\sigma$ witnessed securability and the standard were sufficient, $\sigma$ would be reliable everywhere, contradicting 2.)
4. Let $X$ have a positive tolerance (or refining grids, or a fixed smoothing bandwidth), with a family fixed independently of the process and of bounded richness. Then for every range $W$, "$X$-calibrated in every world of $W(@,\rho)$" is world-independently securable. (Section 3.1: the witness is calibrated in every world.)
5. Take $@ = w_\sigma$ for a witness $\sigma$ of step 4. If $@ \in W(@,\sigma)$, then CR-S$(X,W)$ says that $\sigma$ is reliable in $@$, contradicting 2. Since CR-S is meant to hold necessarily, it is false.

Which witness supports which claim? Unconditional smooth calibration, and smooth calibration on finitely many history-defined classes, have deterministic witnesses. For these, the distance from the chances in $w_\sigma$ is at least 0.4 on every day of every run, and no question of individuation arises. Sharp calibration, and families with infinitely many classes, need randomized witnesses. For these, the argument assesses the randomized rule as a rule, for calibration (almost surely in each world) and for reliability (averaging over coins). A narrow individuation fixes the coin sequence. It still yields calibration across any countable range for almost every coin sequence, by Fubini. On the reliability side it yields only that, with probability at least $2/7$, the average excess is at least 0.04 along infinitely many horizons (Lemma (b) and reverse Fatou). It therefore needs an averaged version of (R), and computability relative to a rule that hard-codes the coins. On that individuation the conclusion is weaker, and I do not rely on it.

For a finite-horizon standard with tolerance, deterministic witnesses secure it beyond a horizon depending on the tolerance; randomized ones secure it with high probability. Theorem 2(a) below covers finite horizons generally.

The Section 2.3 assumption has failed. The uniform 0.7 process is calibrated by luck, the Foster-Vohra procedure by design. Whatever set of worlds a process is calibrated across, the procedure is calibrated across it too, so modal robustness cannot favour any process over the procedure.

## 4.1 Defending (R)

(R) is chance-relative, and a calibrationist who identifies reliability with calibration will reject it (6.1). Three considerations support it.

*It respects (D1).* It applies only where a rule computable relative to the process's own matches the chances. Where the chances follow a random sequence that no such rule computes, (R) is silent.

*It is backed by the record.* Let $\rho^*$ have credence $c_t$. The difference between the realized average Brier scores of $\rho$ and $\rho^*$ equals the average of $(f_t - c_t)^2$ plus an average of bounded martingale differences, which tends to zero almost surely. For the deterministic witness, the realized gap is eventually at least about 0.16 almost surely. Chance-expected inaccuracy averaged over coins is at least $0.16 + 0.09 = 0.25$ every day, no better than always saying one half; $\rho^*$'s is 0.09. Both processes are calibrated. The record separates them; calibration does not. For general strictly proper scores, the excess is the score's divergence between $c$ and $f$. A lower bound follows wherever the score's generating function is strongly convex; the log score's divergence, for instance, is at least $2(f - c)^2$.

*Its scope.* (R) concerns reliability. Against unconditional calibrationism there is also a clear verdict about justification. An agent with an informative barometer ignores it and keeps a calibrated record by the Foster-Vohra procedure; her process is calibrated in every world, and her credences are not justified. Against conditional and multicalibrated versions, the first horn concerns reliability. It reaches justification only through the calibrationist's own bridge from reliability to justification. An agent who uses her evidence as labels and is calibrated on every class does as well as any learner can without assumptions about the law, and I do not claim an independent intuition that her credences in her anti-tracking world are unjustified.

# 5. The second horn

Step 4 requires families fixed independently of the process and of bounded richness. The main ways to violate this are the following.

## 5.1 Propensity-binned classes

For a randomizing agent, the propensity is a candidate for the credence. So let $\mathcal R(\rho)$ include $\{t : \bar f_t \in I\}$ for rational intervals $I$. In $w_\rho$, with tolerance $\varepsilon$, the probability that $\rho$ is calibrated on these classes is at most $1/(2(0.9 - \sqrt\varepsilon))$ (A3). That is below one for $\varepsilon < 0.16$, about $5/6$ at $\varepsilon = 0.09$, and tends to $5/9$ as $\varepsilon \to 0$. So the standard is not securable. For deterministic processes, propensity binning adds nothing: the propensity is the credence. Sufficiency then depends on the fixed classes. A fixed family that lacks "yesterday's weather" certifies the one-half process in the persistence world, where the chances are computable from its inputs and (R) applies. In general, a fixed family suffices only if it captures every chance structure that a computable rule could exploit. That leads to the next case.

## 5.2 Computable calibration

Restrict processes to computable ones, and let the family be all computable rules. For a computable $\rho$ with rational coins, $w_\rho$ and $\{t : \bar f_t < 1/2\}$ are computable. So, by A3, no computable process is calibrated on all computable rules in every world. (The Sandroni-Smorodinsky-Vohra procedure for this countable family exists, but by the same argument it is not computable.) This view is close to Dawid's (1985) calibration-based theory of empirical probability, and it is the strongest calibrationism I know. Dawid shows that any two forecast sequences calibrated on all computable rules "must be in asymptotic agreement". The theorem is measure-free. For computable forecasts, with rules that can consult the forecasts, the agreement is pointwise. In a computable chance world, the chance-matcher meets the criterion almost surely (A2). So a computable process that meets it agrees asymptotically with the chances on almost every run.

This view is not refuted by the first horn, and by Hu and Shmaya (2013) its record-based tests can resist manipulation by computable forecasters (Section 7). What follows?

First, a sufficiency failure that needs neither (R) nor a diagonal world. Calibration is a limit property. A computable process that issues arbitrary credences for its first $10^{100}$ days and then matches the chances is computably calibrated, and CR-S counts its early credences as justified. A reliabilist may reply that reliability belongs to processes, not credences. But justification belongs to credences, and the chance-relative measure of Section 8 evaluates each credence against the chance given its ground.

Second, coextension. Where the view is extensionally adequate, it agrees asymptotically with the chances. A non-reductive realist about chance will say that calibration is then the symptom and closeness to chance the condition. The chance-matcher is calibrated because its credences equal the chances and the law of large numbers holds. A reductive Dawidian, who defines chance as what computable calibration determines, may reverse the order. My conclusion against (D2) is therefore conditional on a non-reductive view of chance. On a reductive view, the first horn and the initial-segment objection still stand, and the disagreement becomes one about the nature of chance.

## 5.3 Cross-world calibration

Dunn's slogan can be read synchronically: among the nearby worlds that share the history and in which the process gives $p$, a proportion $p$ have rain. That needs a measure on worlds. With the chance measure, the proportion at a history is the chance given the history, so calibration at each history is chance-matching. Pooling across histories (rain has probability $p$ given credence $p$) is weaker. It is met by announcing the marginal chance, which is Tang's insensitivity case. A measure not derived from chances gives the wrong verdict in the persistence world unless its proportions approximate the chances.

## 5.4 Other strengthenings

*Refinement.* Forecast verification has long required "maximizing the sharpness of the predictive distributions subject to calibration" (Gneiting, Balabdaoui and Raftery 2007; cf. Seidenfeld 1985). An absolute sharpness threshold violates (D1). A threshold relative to what is attainable from the inputs is the chance condition.

*Deterministic sharp calibration over rich ranges.* No deterministic process is sharply calibrated in its own diagonal world, so over ranges containing such worlds the standard certifies no deterministic process. Over ranges that fix the chance law, a fixed family of classes is exposed as in 5.1.

*Rate-sensitive standards.* With fixed bins, a chance-matcher's realized $\ell_1$ calibration error grows like $\sqrt{T}$, faster than any uniform guarantee. But a binned test requiring that rate controls type I error, so Sandroni's theorem supplies an uninformed passer, though not a feasible one.

# 6. Objections

## 6.1 Reliability just is calibration

The calibrationist may reject (R) and identify reliability with calibration, perhaps relative to the agent's repertoire of classes. Then for each repertoire some process is maximally reliable in every environment, and reliability says nothing about fit between process and environment. Choosing the repertoire world-relatively, to include whatever classes the chances depend on, reintroduces chance. The most principled version replaces (D1) with (D1′): do not penalize a process where the truth is not more predictable by a process that presupposes nothing about how outcomes are generated. That motivates world-independent guarantees of the kind studied in formal learning theory and meta-induction (Schurz 2019: optimality "in all possible worlds among all prediction methods accessible to the epistemic agent"). This is a coherent epistemic ideal, and against its proponent the dispute is partly verbal. But it gives up the externalist core of reliabilism, on which a process is reliable in an environment by fitting it, as a thermometer fits the temperature. By step 3, no world-independent guarantee is reliability in that sense. Pettigrew (2021) presses a Connection Problem: how does justification so understood connect to epistemic value? On the definitional reply, maximal reliability is compatible with avoidable chance-expected inaccuracy of any size. A regret-based reply connects calibration to accuracy in a minimax sense, not in the environment-relative sense reliabilism needs.

## 6.2 The witness is a learner, and coherent

The Foster-Vohra procedure learns from outcomes, and in i.i.d. worlds its credences approach the frequencies. I grant this; the argument needs only that CR-S is wrong about the procedure in its anti-tracking world. Might calibrationists restrict CR-S to coherent processes? Dawid (1982) proved that a coherent Bayesian assigns probability one to being well calibrated. Oakes (1985) reports Dawid's observation that a coherent forecaster cannot correct past miscalibration without sacrificing coherence, which the randomized procedure does. But the restriction excludes nothing relevant. Every deterministic history-based rule is a coherent Bayesian relative to the measure its forecasts induce. So the deterministic Foster-Hart witness is coherent. What it lacks is not coherence but fit.

## 6.3 Generality

A broad type such as "extrapolating from the weather record" contains processes that are miscalibrated in $w_\rho$, so broad typing may condemn the procedure there. But then the verdict depends on the typing, not on the procedure's fit with the world. The procedure is an admissible type for an agent who implements it. Excluding it would need a principle distinguishing it from good learners by something other than calibration.

## 6.4 Demon worlds and normal worlds

By (R), a demon victim's process is unreliable in the demon world. This is the standard reliabilist verdict, and reliabilists who want the victim justified assess reliability in normal worlds. Calibrationism's distinctive verdict is that the Foster-Vohra process is reliable even in its anti-tracking world, which extends to the barometer-ignorer. Normal-worlds calibrationism (Goldman 1986 characterizes normal worlds by our general beliefs about the actual world) is not refuted by step 5, which requires $@ \in W$. The first horn shows only that calibration across normal worlds does not secure reliability in each of them. It does so where the deterministic witness's world, a finite-order chance process, is consistent with general beliefs about weather. Whether calibration secures reliability on aggregate across normal worlds depends on the weight of anti-tracking worlds. I leave this open.

## 6.5 Comparative calibrationism

Suppose reliability requires calibration and not being beaten in realized accuracy by any member of a fixed finite class $\mathcal C$ of same-input processes. Calibeating methods (Foster and Hart 2023; Lee, Noarov, Pai and Roth 2022) combine given forecasters into a calibrated forecast whose Brier score is asymptotically no worse than each of theirs, and prediction with expert advice extends such guarantees to countable classes (Cesa-Bianchi and Lugosi 2006, ch. 3). So the standard is securable. In the securing forecaster's anti-tracking world, the chance-expected excess averages at least 0.16 per day. Realized scores track chance-expected scores up to martingale noise, so, with positive probability, every member of $\mathcal C$ has an average excess bounded away from zero along infinitely many horizons. If instead $\mathcal C$ contains every world's chance-matcher, the standard measures closeness to chance by another name.

# 7. Beyond calibration

A *test* passes or fails a forecaster on the forecasts and the data. It *controls type I error* at level $\eta$ if a forecaster who forecasts by the true probabilities passes with probability at least $1 - \eta$, whatever they are.

**Theorem 2.**

(a) (Sandroni 2003.) Over a finite horizon, every test controlling type I error at level $\eta$ can be passed, whatever the data, with probability at least $1 - \eta - \delta$ by an uninformed forecaster. The forecaster draws a theory at the outset, using Fan's minimax theorem.

(b) (Olszewski and Sandroni 2008.) The same holds for future-independent tests that reject theories in finite time. In their words, "tests which cannot be ignorantly passed must rely on predictions about data not yet observed, and such tests cannot be run if forecasters report only the probability of the next period's events on the basis of the actually observed data."

(c) (Shmaya 2008.) If a test is Borel and a forecaster who knows the truth always passes it, then for every $\varepsilon > 0$ an ignorant forecaster passes it with probability at least $1 - \varepsilon$.

A record of credences actually formed is what Olszewski and Sandroni describe. The witnesses are history-based, with their initial draw counted as randomization, so the Lemma applies with the propensity defined by the randomization measure. Running the first horn with these witnesses gives:

> **(G)** No standard on the record of credences actually formed is sufficient for reliability if it is: (i) finite-horizon, met by a chance-matcher with probability at least $1 - \eta$ in every world, with "met" read at threshold $\kappa = \eta + \delta$; or (ii) future-independent, rejecting in finite time, with the same thresholds; or (iii) Borel and met by a chance-matcher with probability one, with "met" read at any threshold $\kappa > 0$. This holds provided that processes as powerful as these witnesses are admitted, and that (R) is read relative to the witness's rule.

The proviso matters, since the witnesses need not be computable or feasible. Each exception to manipulability brings in something beyond the record.

*Predictions about unobserved data.* Dekel and Feinberg (2006) give a test that the truth passes and that false theories fail on all but a topologically small set; their strongest result uses the continuum hypothesis. Olszewski and Sandroni (2009b) give a non-manipulable test controlling type I error without it. Both use predictions about data not yet observed.

*Computational bounds.* Fortnow and Vohra (2009) give an efficient test that, under standard hardness assumptions, no efficient uninformed forecaster passes. Hu and Shmaya (2013) give a computable test that accepts true experts with high probability and that no computable strategy manipulates. So if only computable processes are admitted, (G) can fail. This is where calibrationism's remaining hope lies, and there it meets Dawid's agreement theorem (5.2).

*Restricted theories.* Restricting admissible theories to those with learnable and predictive representations yields non-manipulable tests (Al-Najjar, Sandroni, Smorodinsky and Weinstein 2010). Olszewski and Sandroni (2009a) conclude that such restrictions help "only to a limited extent".

*Comparison.* Al-Najjar and Weinstein (2008) give a record-based test for two experts, one of whom knows the true distribution. The test identifies the informed expert, or else finds the two experts' forecasts close. The single-expert impossibility, they note, arises because nature's mixtures over distributions reduce to pure strategies, and an informed expert prevents this. The guarantee presupposes a competitor whose forecasts are the chances. Feinberg and Stewart (2008) treat several forecasters.

# 8. What reliability for credence must be

Tang's indicator view, as the SEP reports it, holds that a credence $C(p)$ is justified only if it is based on a ground $g$ such that the objective probability of $p$ given $g$ approximates $C(p)$. The arguments point to a view of this kind, combined with a process element: the ground is what the process uses. For the Brier score, the chance-expected inaccuracy of credence $f$ when the chance given $g$ is $c_g$ is $(f - c_g)^2 + c_g(1 - c_g)$. The second term is what the ground leaves unavoidable. The first, the excess, measures the process's unreliability given its ground; for other strictly proper scores it is the divergence. I do not claim the measure is new. Chance-expected accuracy is central in accuracy-first epistemology (Pettigrew 2016 derives chance-credence norms from chance dominance). Clifton's statistical reliabilism ranks statistical credences by average closeness to objective probabilities, relative to candidate models and without requiring knowledge of them. That comparative structure resembles the standards of 6.5, so Clifton's view is a relative rather than an ally. Pettigrew's (2021) own proposal is both a process and an indicator view and aims to connect justification to accuracy. It may be a version of the present view. Whatever reading of Dunn underlies his claim that Dunn's and Tang's views are extensionally equivalent, the equivalence cannot hold on a track-record reading of calibration. That reading is securable by an uninformed process, while chance given grounds is not.

Four clarifications. First, (D1) restricts grounds to what a rule computable relative to the process's could exploit. Under determinism with unrestricted grounds the chance is 0 or 1, so the relativization is required, and it brings with it a reference-class problem for coarse-grained chance. Second, the view separates the reliability of a process from the agent's use of her evidence. The barometer-ignorer's process may have small excess relative to its own coarse ground. Her fault is the one Goldman's non-undermining condition addresses: a better process was available. Applying that condition requires ranking available processes, and the total chance-expected inaccuracy $(f - c_g)^2 + c_g(1 - c_g)$ ranks the barometer-using process higher, since its ground leaves less unavoidable. Calibration cannot do this ranking, because both processes are calibrated. Third, inputs a process receives but ignores are not its grounds; the basing relation selects them. Fourth, the measure is graded, whereas CR-S is a threshold claim. The arguments use only the threshold version.

Calibration seemed right because a chance-matching process is calibrated almost surely: in the sense of Section 2.1 when the chances lie on the grid, and in the averaged sense for every countable family of predictable rules (A2; the own-prior version is Dawid 1982). Calibration is how reliability shows up in the record, and the theorems show that it can show up without reliability, in every world.

*The Humean worry.* If chances supervene on the total pattern, is the chance condition itself a test subject to (G)? Type I error control presupposes chances fixed in advance of the data, while a Humean chance is fixed by the pattern it summarizes. As a function of the whole record, a Humean condition is not a finite-time test, so (G)(i) and (ii) do not apply. Shmaya's theorem would apply only if the best-system map were Borel and a forecaster who knows the truth passed with probability one under every measure. That is doubtful for best-system chances, which can diverge from non-ergodic measures. Even then, the witness would pass only with probability $1 - \varepsilon$. I flag this as the point where the positive view's independence from (G) is least secure.

The cost of the view is that reliability cannot be read off a finite record. That is the externalist's standard situation: reliability need not be knowable to the agent to make her justified.

# 9. Conclusion

The modal and evidential defences of calibrationism assumed that uninformed calibration is lucky and fragile. It is not. For any fixed family of reference classes of bounded richness, it can be secured by design in every world, and every history-based process has an ordinary chance world in which a rule computable relative to its own matches the chances while it does not. So no such standard is sufficient for reliability in the actual or nearby worlds. The standards that escape are either insufficient, or coextensive with agreement with the chances. In the latter case they still fail for individual credences, and their vindication of calibration over chance depends on a reductive theory of chance. On the non-reductive view, reliability for credence is a relation to chances given grounds, and calibration is how it shows up in the record.

# Appendix

**A1. Lemma.** $\bar f_t(h)$ depends on $h$ alone, so $w_\rho$ is well defined (Ionescu-Tulcea), and the randomization is independent of the weather. (a) If $\bar f_t < 1/2$, then $\int |\varphi_t - 0.9|\, d\lambda \ge 0.9 - \bar f_t > 0.4$. Otherwise $\int |\varphi_t - 0.1|\, d\lambda \ge \bar f_t - 0.1 \ge 0.4$. Then apply Jensen. (b) Fix a path. The average distance $D_T$ lies in $[0, 0.9]$ and has mean at least 0.4. With $P = \lambda(D_T \ge 0.2)$, we get $0.4 \le 0.9P + 0.2(1 - P)$, so $P \ge 2/7$. $\square$

**A2. Chance-matchers are calibrated.** On days selected by a predictable rule, the $x_t - c_t$ are bounded martingale differences. By the martingale strong law, on the event that infinitely many days are selected, their average tends to zero almost surely. Within the grid cells this gives calibration of the chance-matcher (for $w_\rho$, the cells for 0.9 and 0.1), and countable unions extend the result to countable families. With continuum-valued chances, the same argument gives, for each rule, convergence of mean credence minus mean outcome.

**A3. Propensity-binned calibration.** Fix an almost sure path in $w_\rho$. Let $G$ be the set of randomizations on which $\rho$ is $\varepsilon$-calibrated on the propensity classes. By Cauchy-Schwarz, on any calibrated class mean credence and mean outcome differ in the limit by at most $s = \sqrt\varepsilon$.

- *Case 1: $A = \{t : \bar f_t < 1/2\}$ is infinite.* There the frequency of rain tends to 0.9 (A2), so on $G$ the mean credence over $A$ is eventually at least $0.9 - s$. Its average over randomizations is the mean propensity over $A$, which is below $1/2$. Credences are non-negative, so by Fatou, $(0.9 - s)\lambda(G) \le 1/2$.
- *Case 2: $A$ is finite.* The complement is cofinite, rain frequency there tends to 0.1, and on $G$ the mean credence is eventually at most $0.1 + s$. Its randomization-average is at least $1/2$. By reverse Fatou, with credences bounded by one, $(0.1 + s)\lambda(G) + (1 - \lambda(G)) \ge 1/2$, so $\lambda(G) \le 1/(2(0.9 - s))$.

So in either case $\lambda(G) \le 1/(2(0.9 - s)) < 1$ when $s < 0.4$. $\square$

# References

Al-Najjar, N. I., Sandroni, A., Smorodinsky, R. and Weinstein, J. (2010). Testing theories with learnable and predictive representations. *Journal of Economic Theory* 145(6): 2203-2217.

Al-Najjar, N. I. and Weinstein, J. (2008). Comparative testing of experts. *Econometrica* 76(3): 541-559.

Blackwell, D. and Dubins, L. (1962). Merging of opinions with increasing information. *Annals of Mathematical Statistics* 33: 882-886.

Cesa-Bianchi, N. and Lugosi, G. (2006). *Prediction, Learning, and Games*. Cambridge: Cambridge University Press.

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

Lee, D., Noarov, G., Pai, M. and Roth, A. (2022). Online minimax multiobjective optimization: multicalibeating and other applications. *Advances in Neural Information Processing Systems* 35.

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
