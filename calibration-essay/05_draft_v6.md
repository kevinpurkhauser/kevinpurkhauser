---
title: "Calibrated Everywhere: A Dilemma for Track-Record Reliabilism about Credence"
---

**Abstract.** Calibrationist reliabilism holds that a credence is justified if it is produced by a well-calibrated process. Its defenders made calibration modally robust and conditioned it on evidence, assuming that calibration without connection to the world is lucky and fragile. Forecasting theory shows otherwise: for every countable family of reference classes fixed in advance, some process needing no assumption about how outcomes arise is calibrated in every world. Given a chance-relative premise and a diagonal lemma, no such standard suffices for reliability in the actual or nearby worlds. The standards that escape either fail otherwise or coincide with agreement with the chances.

# 1. Introduction

A reliabilist about justified credence needs a measure of reliability for processes that output credences. Measuring credences by their closeness to the truth values penalizes middling credences even where nothing better is possible. The leading alternative, due to Dunn (2015) and inspired by Ramsey, is calibration: a process is well calibrated if, among the propositions to which it assigns credence $p$, a proportion $p$ are true. The *Stanford Encyclopedia* entry on reliabilism (Goldman and Beddor) describes the calibration approach, on which a credence is justified iff it is produced by a well-calibrated process.

I argue for a dilemma.

*First horn.* The standards on this horn are calibration with a positive tolerance, or at a fixed smoothing bandwidth, relative to a family of reference classes fixed independently of the process assessed. The family may be countable, of finite combinatorial complexity, or, for deterministic witnesses, finitely many classes defined by the history. Each such standard is met in every world by a process that uses only the record and needs no assumption about how outcomes are generated (Foster and Vohra 1998 and descendants). Every history-based process has a chance world in which its credences are far from chances computable from its inputs relative to its own rule. Given a premise (R) linking reliability to such chances, no standard on the first horn suffices for reliability in the actual or nearby worlds. The core case is deterministic and needs only a feasible matching rule. The extension to sharp, binned calibration uses randomized witnesses and a stronger reading of (R).

*Second horn.* Standards escape the first horn by restricting processes to computable ones, by tying reference classes to the process, or by measuring calibration across worlds. These either remain insufficient or coincide with agreement with the chances. In the computable case the coincidence is asymptotic, in every world with computable chances (Dawid 1985a). Whether that vindicates calibration or chance depends on the metaphysics of chance. Even so, the limit standard fails for individual credences.

Via results on testing experts (Sandroni 2003; Olszewski and Sandroni 2008; Shmaya 2008), the first horn extends to tests of a specified kind. The positive upshot is a chance-relative account of reliability close to Tang (2016).

# 2. Calibrationism

## 2.1 Definitions

There is one yes-or-no question per day: will it rain on day $t$? Write $x_t \in \{0,1\}$. A *credence-forming process* issues a credence $f_t \in [0,1]$ that $x_t = 1$. Its *inputs* are the history $h$: the day's index, earlier outcomes, and labels $z_1, \dots, z_t$ for the agent's other evidence. It may also use a private randomizing device. Its earlier credences, if used, are recomputed from $h$ and its coins. A process is *history-based* if its rule from inputs and coins to credences is fixed in advance. *Worlds* are chance processes for outcomes and labels in which each day's outcome is independent of the process's current coin, given the past.

Fix a finite grid. With $N_T(p)$ the number of days up to $T$ with credence $p$, and $q_T(p)$ the proportion of them with rain, the calibration score is $C_T = \sum_p \frac{N_T(p)}{T}(q_T(p) - p)^2$. A run is *$\varepsilon$-calibrated* if $\limsup_T C_T \le \varepsilon$. A *reference class* is a predictable checking rule, which may consult the history and the current credence. Calibration relative to a family requires $\varepsilon$-calibration on each infinite selected subsequence, with scores normalized by the number of days selected. *Smooth* calibration at bandwidth $\delta$ replaces the grid cells by weighted averages over nearby credences. I regiment "calibrated in a world" as calibrated with probability one under that world's chances and the process's coins. Every range of worlds contains atypical runs, so read run by run not even a chance-matcher would be calibrated throughout a range.

## 2.2 The target

> **CR-S(X, W).** Necessarily: if $\rho$ is $X$-calibrated in every world of $W(@,\rho)$, then $\rho$ is reliable in the actual world $@$, and its credences are justified.

$W(@,\rho)$ is the set of worlds relevant to assessing $\rho$. The first horn concerns ranges that contain the actual world, as Dunn's do: he asks us to look at the actual cases as well as nearby worlds. Normal-worlds versions are discussed in 6.4. CR-S is a constitutive thesis: calibration is what reliability, and so justification, consists in. Dunn's own project is the measurement of reliability. If calibration is offered only as a contingent indicator of reliability in worlds like ours, my conclusion that calibration is a symptom of reliability is compatible with it. Necessity of calibration is not at issue.

## 2.3 How calibrationism answered its critics

The SEP reports Goldman's (1986) case: an agent seventy per cent of whose opinions are true is perfectly calibrated by giving every proposition credence 0.7. It also reports the reply that we should look across nearby worlds. If it is a matter of chance that seventy per cent are true, the process is miscalibrated in nearby worlds. Dunn likewise holds that a process must be assessed not only on the actual cases on which it has performed but also on its performance in nearby worlds. The SEP attributes to Tang (2016) the objection that a process may be calibrated while insensitive to relevant evidence. The natural reply is to condition calibration on evidence.

A natural case shows how far conditioning reaches. In the *persistence world*, the chance of rain is 0.9 after a rainy day and 0.1 after a dry day. The process that always says one half is calibrated there, and also on any class defined by labels or day indices independent of the weather. The rule "0.9 after rain, 0.1 otherwise" uses the same inputs and matches the chances. Conditioning on yesterday exposes the one-half process. The question is whether some process can be calibrated on that class, and on any other fixed class, in every world, and still fail to track the chances.

## 2.4 What calibration was meant to secure

Calibration was meant not to penalize middling credences where the truth is not more predictable (one half about a fair coin). I regiment this as (D1): a process should not be penalized where the truth is not more predictable *from its inputs, by a rule computable relative to its own*. The rider is mine. A stronger reading, (D1$_f$), replaces "computable" by "feasibly computable". (D2): reliability is a matter of track record, actual and counterfactual. I keep (D1) and reject (D2).

# 3. Calibration without information

## 3.1 Theorems

**Theorem 1** (Foster and Vohra 1998; Foster 1999). For every $\varepsilon > 0$ there is a randomized history-based procedure on a finite grid that is $\varepsilon$-calibrated, almost surely, against every sequence of outcomes, including sequences chosen by an adversary who sees past outcomes and credences but not the current coin.

Qualifications.

- *(i)* Randomization is essential for sharp calibration. Every deterministic procedure is miscalibrated on the sequence on which it rains exactly when its credence is below one half (Oakes 1985; Dawid 1985b), an argument in the line of Putnam's (1963) diagonal argument against universal inductive methods.
- *(ii)* On a fixed grid, positive tolerance is needed. With grids refined over time, every tolerance can be met.
- *(iii)* Rates. For unbinned $\ell_1$ calibration error, the best known uniform guarantee on cumulative error is slightly below $T^{2/3}$ (Dagan et al. 2025). No procedure guarantees better than about $T^{0.528}$ (Qiao and Valiant 2021), raised to about $T^{0.544}$ by Dagan et al. (2025).

*Deterministic procedures.* Kakade and Foster (2004) obtained deterministic weak calibration. Foster and Hart (2018) show that "smooth calibration can be guaranteed by deterministic procedures", even when forecasts are announced in advance, with finite recall and a finite grid, at each fixed bandwidth and positive tolerance. This is unconditional. For finitely many classes that depend only on the history, run a separate copy on each atom of the partition they generate (at most $2^K$ atoms for $K$ classes). Smooth calibration in its linear form requires that, for every Lipschitz weight $w$, the average of $w(f_t)(x_t - f_t)$ be small. This form is additive over atoms, so it holds on every union of atoms. The combined procedure no longer has finite recall, because each copy remembers its own atom's days.

*Randomized procedures and reference classes.* For each countable family of checking rules there is a procedure calibrated on all of them against every sequence (Sandroni, Smorodinsky and Vohra 2003). Foster, Rakhlin, Sridharan and Tewari (2011) treat families of finite sequential complexity, and online multicalibration (Gupta et al. 2022) treats overlapping groups defined by labels. For each family there is a procedure.

None of these procedures needs an assumption about how outcomes are generated.

## 3.2 The anti-tracking lemma

Let $\rho$ be history-based, with credence $\varphi_t(h,u)$ given history $h$ and randomization $u$ of law $\lambda$. Its *propensity* is $\bar f_t(h) = \int \varphi_t(h,u)\, d\lambda(u)$, a function of $h$ alone. Define $w_\rho$ as follows. Labels come from a fixed mechanism independent of the coins. The chance of rain given $h$ is $c_t = 0.9$ if $\bar f_t(h) < 1/2$, and $0.1$ otherwise. The outcome path in $w_\rho$ is then independent of $u$.

**Lemma.** In $w_\rho$:

- *(a)* on every day and history, $\int (\varphi_t - c_t)^2\, d\lambda \ge \left(\int |\varphi_t - c_t|\, d\lambda\right)^2 \ge 0.16$;
- *(b)* for every path and horizon $T$, with $\lambda$-probability at least $2/7$, the average of $|\varphi_t - c_t|$ over the first $T$ days is at least 0.2.

Features.

- *Exogeneity and extremity.* The chance is a fixed function of past weather and labels, nothing reacts to the process, and the chances are 0.9 and 0.1.
- *Matching.* With rational grid values and finitely many rational coins per day, the chance is computable from $h$ relative to $\rho$'s rule. For deterministic $\rho$ the matcher is "run $\rho$, then threshold at one half", which is feasible. For randomized $\rho$ the propensity averages over all coin paths and need not be feasible.
- *Learnability.* If $\rho$ is computable, so is $w_\rho$, and a Bayesian whose prior gives $w_\rho$ positive weight merges with it (Blackwell and Dubins 1962). No computable learner merges with every computable world of this kind, since its own anti-tracking world is among them.
- *Tie.* The procedures of 3.1 are calibrated in $w_\rho$. So is the process with credence $c_t$, almost surely (A2). In $w_\rho$, a calibrated deterministic witness must keep its credences near one half, where its kernel mixes the rainy and the dry regime. It behaves like the always-one-half process.
- *Ordinariness.* For the unconditional Foster-Hart witness, which has finite recall, $w_\rho$ is a finite-order chance process. Witnesses for conditional standards have anti-tracking worlds whose chances depend on unbounded stretches of history.

# 4. The first horn

> **(R)** Suppose that in world $w$ the chance of rain given $\rho$'s inputs is computable from those inputs relative to $\rho$'s rule. If, on every day, $\rho$'s chance-expected Brier inaccuracy (averaged over its coins) exceeds that of the chance by at least 0.16, then $\rho$ is not reliable in $w$.

Call a standard *world-independently securable* if some history-based process meets it in every world.

1. Every history-based $\sigma$ has a world $w_\sigma$ meeting the antecedent of (R). (Lemma (a); the excess Brier inaccuracy of $f$ over $c$ is $(f - c)^2$.)
2. So every history-based process has a world in which it is not reliable. (1, R)
3. So no world-independently securable standard is sufficient for reliability.
4. The following are world-independently securable, for every range $W$: "$X$-calibrated in every world of $W(@,\rho)$", where $X$ is sharp calibration with positive tolerance relative to a countable family of predictable rules fixed in advance, or relative to a family of finite sequential complexity; or smooth calibration at a fixed bandwidth relative to finitely many history-defined classes. (Section 3.1. The witness is calibrated in every world.)
5. Take $@ = w_\sigma$ for a witness $\sigma$ of step 4. If $@ \in W(@,\sigma)$, then CR-S$(X,W)$ says that $\sigma$ is reliable in $@$, contradicting 2. Since CR-S is claimed to hold necessarily, it is false.

Step 2 alone is a no-free-lunch fact (Putnam). The contribution is step 4: calibration can be met by design everywhere, so its satisfaction carries no information about fit with any world. Securability alone is no objection; step 2 supplies, for each process, a world where a matching rule exists.

*Deterministic core.* For smooth calibration, unconditionally or on finitely many history-defined classes, the witness is deterministic. In its world its distance from the chances is at least 0.4 on every day of every run, and the matcher is feasible. So (R) holds there even on the feasibility reading (D1$_f$). No question of individuation arises.

*Randomized extension.* Dunn's own notion is binned (sharp) calibration, and so are countable families. These need randomized witnesses. The argument then assesses the randomized rule as a rule. That is appropriate, since calibration in a world is itself an almost-sure property of the rule. It also uses the computability reading (D1), because the matcher averages over coin paths. On (D1$_f$) the extension lapses. Two observations limit the cost. First, binned calibration is a poor refuge: it is discontinuous in the credences, since credences of 0.49 and 0.51 fall into different cells, and smooth calibration is the more defensible standard. Second, a feasible variant exists if the world may react to the process's past announced credences, which is Theorem 1's own adversary model. Its chance is set by the process's current mixing probabilities, computed by the process itself. Reflexive domains, such as markets, contain worlds of that kind. On a narrow individuation fixing the coin sequence, Fubini gives calibration across any countable range for almost every coin sequence, and Lemma (b) with reverse Fatou gives, with probability at least $2/7$, an average excess of at least 0.04 along infinitely many horizons: enough against a necessary claim, given an averaged (R).

The assumption of Section 2.3 has failed. The uniform 0.7 process is calibrated by luck, the Foster-Vohra procedure by design. For any family within the scope of step 4, whatever set of worlds a process is calibrated across, the procedure is calibrated across it too, so modal robustness cannot favour any process over it.

## 4.1 Defending (R)

(R) is chance-relative, and a calibrationist who identifies reliability with calibration will reject it (6.1). Three considerations support it.

*It respects (D1).* It applies only where a rule computable relative to the process's own rule matches the chances. Where chances follow a random sequence that no such rule computes, (R) is silent.

*It is backed by the record.* Let $\rho^*$ have credence $c_t$. The difference between the realized average Brier scores of $\rho$ and $\rho^*$ equals the average of $(f_t - c_t)^2$ plus an average of bounded martingale differences, which tends to zero almost surely. For deterministic witnesses, the realized gap is eventually at least about 0.16 almost surely. For randomized ones, the available bound is the probabilistic one of Lemma (b). The chance-expected inaccuracy is at least $0.16 + 0.09 = 0.25$ every day, no better than always saying one half; $\rho^*$'s is 0.09. Both are calibrated. In terms of the standard decomposition of the Brier score into a calibration term and a refinement term (stated, for instance, in Foster and Hart 2023), the difference lies wholly in refinement. For other strictly proper scores, the excess is the score's divergence. It is bounded below by a multiple of $(f - c)^2$ when the generating function is strongly convex; for the log score, with credences bounded away from 0 and 1, Pinsker's inequality gives $2(f - c)^2$.

*Its scope.* (R) concerns reliability. Against conditional and multicalibrated calibrationism, the first horn reaches justification only through the calibrationist's own bridge from reliability to justification. I claim no independent intuition that the credences of an agent calibrated on every class she attends to are unjustified in her anti-tracking world. Against those views the result is a reclassification. Their standard is a world-independent guarantee relative to a class, not reliability in an environment.

# 5. The second horn

## 5.1 Restricted processes: computable calibration

The family of all computable checking rules is countable. By Sandroni, Smorodinsky and Vohra, some non-computable procedure is calibrated on it in every world, so unrestricted computable calibration lies on the first horn. It escapes only if processes are restricted to computable ones. For a computable $\rho$ with rational coins, $w_\rho$ and the class $\{t : \bar f_t < 1/2\}$ are computable. So, by A3, no computable process is calibrated on all computable rules in every world. This view is close to Dawid's (1985a) calibration-based theory of empirical probability, and it is the strongest calibrationism I know. Dawid shows that any two forecast sequences calibrated on all computable rules "must be in asymptotic agreement". The theorem is measure-free. With zero tolerance, and rules that can compare the forecasts, the agreement is pointwise. In a computable chance world the chance-matcher meets the criterion almost surely (A2). So a computable process that meets it agrees asymptotically with the chances on almost every run.

The first horn does not refute this view. Hu and Shmaya (2013) give a computable test that computable strategies cannot manipulate (Section 7). Three points remain.

*Finite records.* Calibration in the limit leaves every finite stretch of credences unconstrained. A computable process could issue arbitrary credences for its first $10^{100}$ days and then match the chances of the worlds in its range; CR-S would count its early credences as justified. A process reliabilist may answer that the early phase is a different process type. That answer turns on typing and applies to any limit-based measure. A finite-horizon computable calibrationism avoids the problem, but then its tests are finite games. Sandroni's manipulator for such a game can be found by solving it, so for computable finite tests it is computable, though not feasible (cf. Fortnow and Vohra 2009). So the computable calibrationist faces a sub-dilemma. Limit standards leave individual credences unconstrained. Finite ones are computably manipulable.

*Coextension.* Where the view is adequate, it agrees asymptotically with the chances. A non-reductive realist about chance will say that calibration is then the symptom and closeness to chance the condition: the chance-matcher is calibrated because its credences equal the chances and the law of large numbers holds. A reductive Dawidian, who defines chance as what computable calibration determines, may reverse the order. My conclusion against (D2) is therefore conditional on a non-reductive view of chance. On a reductive view the dispute concerns the nature of chance. A Humean reductionist faces the same question (Section 8).

*Feasibility.* Restricting further to feasible processes leads to outcome indistinguishability (Dwork, Kim, Reingold, Rothblum and Yona 2021): no efficient observer can tell real outcomes from outcomes drawn from the predictor's probabilities. This principled middle position measures closeness to the chances as seen by bounded observers; I take it to refine the chance-relative view, not to rival it.

## 5.2 Process-relative classes

For a randomizing agent, the propensity is a candidate for the credence. So let the family include $\{t : \bar f_t \in I\}$ for rational intervals $I$, among them $[0, 1/2)$ and $[1/2, 1]$. In $w_\rho$, with tolerance $\varepsilon$, the probability that $\rho$ is calibrated on these classes is at most $1/(2(0.9 - \sqrt\varepsilon))$ (A3). This is below one for $\varepsilon < 0.16$, so the standard is not securable at threshold zero. The bound is nearly tight (draw once between "0.9 on the class" and "0 on the class"). For deterministic processes, propensity binning adds nothing. Sufficiency then depends on the fixed classes, as the persistence world shows. A family whose classes are independent of the weather certifies the one-half process there, while (R) applies. To be sufficient across worlds with computable chances, the family must capture whatever structure a computable rule could exploit. That leads back to 5.1.

## 5.3 Cross-world calibration

Dunn's slogan can also be read synchronically: among nearby worlds that share the history and in which the process gives $p$, a proportion $p$ have rain. This needs a measure on worlds. Under the chance measure, the proportion at a history is the chance given that history, so calibration at each history just is chance-matching. Pooling across histories is weaker. Where the marginal chance is constant across days, announcing it meets the standard, which is Tang's insensitivity case again. A similarity measure not derived from chances would need its proportions to approximate the chances in order to expose the one-half process in the persistence world.

## 5.4 Other strengthenings

*Refinement.* Gneiting, Balabdaoui and Raftery (2007) propose the paradigm of "maximizing the sharpness of the predictive distributions subject to calibration" (cf. Seidenfeld 1985). An absolute sharpness threshold violates (D1). A comparative threshold ("calibrated and maximally refined among available processes") is the comparative view of 6.5. A threshold relative to what is attainable from the inputs is the chance condition.

*Rate-sensitive standards.* With fixed bins and error measured against the actual credences, Blackwell's approachability theorem (the method of Foster 1999) yields a uniform guarantee of order $\sqrt{T}$ on cumulative binned error in excess of any fixed tolerance, the chance-matcher's own order. So rate standards of this kind are securable, and they fall on the first horn. The lower bound of order $T^{0.54}$ concerns unbinned error. Against that measure a chance-matcher with continuum-valued chances does badly, so no rate test controls type I error there.

# 6. Objections

## 6.1 Reliability just is calibration

If reliability is calibration relative to the agent's repertoire of classes, then for each repertoire some process is maximally reliable in every environment; choosing the repertoire world-relatively reintroduces chance. The principled version replaces (D1) with (D1′): do not penalize a process where the truth is not more predictable by a process that presupposes nothing about how outcomes are generated. That motivates world-independent guarantees. Formal learning theory calls success across a range of possibilities "reliability". Meta-induction is presented as optimal "in all possible worlds among all prediction methods accessible to the epistemic agent" (publisher's description of Schurz 2019). These are coherent epistemic ideals, and against their proponents the dispute is partly verbal. But they are not the externalist notion at the core of process reliabilism, on which a process is reliable in an environment by fitting it, as a thermometer fits the temperature. By step 3, no world-independent guarantee is reliability in that sense. Pettigrew (2021) presses a Connection Problem: how does justification so understood connect to epistemic value? On the definitional reply, maximal reliability is compatible with avoidable chance-expected inaccuracy of any size.

## 6.2 Learner, coherence, self-monitoring

The Foster-Vohra procedure learns from outcomes, and in i.i.d. worlds its credences approach the frequencies. The argument needs only that CR-S is wrong about it in its anti-tracking world. Could calibrationists restrict CR-S to coherent processes? Dawid (1982) proved that a coherent Bayesian assigns probability one to being well calibrated. Oakes (1985) reports Dawid's observation that a coherent forecaster cannot correct past miscalibration without sacrificing coherence, which the randomized procedure does. But every deterministic history-based rule is a coherent Bayesian relative to the measure its forecasts induce, so the deterministic witness is coherent. Excluding processes that consult their own record fails too. Recalibration from feedback is a paradigm of epistemic improvement. And a deterministic rule's past forecasts are recomputable from the history, so the restriction is not well defined.

## 6.3 Generality

Broad typing ("extrapolating from the weather record") may condemn the procedure in $w_\rho$, but then the verdict depends on typing, not fit. Typing by the label classes an agent attends to is the process-relative move of 5.2.

## 6.4 Demon worlds and normal worlds

Is $w_\sigma$ a demon world for $\sigma$, where an internalist-friendly verdict of justification is welcome? The disanalogy is that in a demon world the inputs carry no information about the truth. In $w_\sigma$ the inputs carry it, and in the deterministic case a feasible same-input rule extracts it. $w_\sigma$ is a grue world for $\sigma$'s method, not a demon world. Reliabilists do not credit an inductive method with reliability in worlds where a rule exploiting its own inputs does better.

Normal-worlds calibrationism grounds justification in reliability across normal worlds, which Goldman (1986) characterizes by our general beliefs about the actual world. Step 5 requires $@ \in W$, so it does not refute that view. The first horn shows only that calibration across normal worlds does not secure reliability in each normal world. It does so where the unconditional deterministic witness's world, a finite-order chance process, is consistent with general beliefs about weather. Whether calibration secures reliability on aggregate across normal worlds depends on the weight of anti-tracking worlds. I leave this open.

## 6.5 Comparative calibrationism

Suppose reliability requires calibration and not being beaten in realized accuracy by any member of a fixed class $\mathcal C$ of same-input processes. For finite $\mathcal C$, calibeating methods (Foster and Hart 2023; Lee, Noarov, Pai and Roth 2022) produce a calibrated forecast whose Brier score is asymptotically no worse than each member's; for countable $\mathcal C$ one adds exponential weighting (Cesa-Bianchi and Lugosi 2006, chs. 2-3). So the standard is securable, and in the securing forecaster's anti-tracking world Lemma (b), reverse Fatou and the martingale argument of 4.1 give, with positive probability, every member an average excess of about 0.04 along infinitely many horizons. If instead $\mathcal C$ contains every world's chance-matcher, the standard measures closeness to chance under another name.

# 7. Beyond calibration

A *test* passes or fails a forecaster on the basis of the forecasts and the data. It *controls type I error* at level $\eta$ if a forecaster who forecasts by the true probabilities passes with probability at least $1 - \eta$, whatever they are.

**Theorem 2.**

- *(a)* (Sandroni 2003.) Over a finite horizon, every test controlling type I error at level $\eta$ can be passed, whatever the data, with probability arbitrarily close to $1 - \eta$ by an uninformed forecaster, who draws a theory at the outset by a distribution obtained from Fan's minimax theorem.
- *(b)* (Olszewski and Sandroni 2008.) The same holds for future-independent tests that reject in finite time. They conclude that a test which cannot be ignorantly passed must use predictions about data not yet observed when the forecasts are rejected, and so cannot be run on next-period forecasts alone.
- *(c)* (Shmaya 2008.) Consider a Borel test of the sequence of next-period forecasts and outcomes that a forecaster who knows the truth always passes. For every $\varepsilon > 0$, an ignorant forecaster passes it with probability at least $1 - \varepsilon$. (The proof uses Martin's determinacy theorem for Blackwell games; under the axiom of choice there are non-Borel exceptions.)

A record of credences actually formed is a sequence of next-period forecasts. The witnesses are history-based, with any initial draw counted as randomization, so the Lemma applies. This treats the initial draw as part of the rule. For a forecaster who draws a whole theory once, that individuation is more contestable than for daily coins, so the following is an extension of the randomized case of Section 4:

> **(G)** On the randomized-rule individuation, no standard on the record of credences actually formed is sufficient for reliability if it is (i) finite-horizon, or (ii) future-independent and rejecting in finite time, and in either case met by a chance-matcher with probability at least $1-\eta$ in every world (with "met" read at threshold $\eta + \delta$); or (iii) Borel and met by a chance-matcher with probability one (with "met" read at any positive threshold).

This presupposes admitting processes as powerful as the witnesses, which for (ii) and (iii) need not be computable. Each known exception to manipulability brings in something beyond the record: predictions about unobserved data (Dekel and Feinberg 2006, whose non-manipulability result assumes the continuum hypothesis; Olszewski and Sandroni 2009b, without it), computational bounds (Fortnow and Vohra 2009, under hardness assumptions; Hu and Shmaya 2013, whose computable test no computable strategy manipulates), restrictions on admissible theories (Al-Najjar, Sandroni, Smorodinsky and Weinstein 2010), which help "only to a limited extent" (Olszewski and Sandroni 2009a), or a competitor whose forecasts are the chances (Al-Najjar and Weinstein 2008; Feinberg and Stewart 2008).

# 8. What reliability for credence must be

Tang's indicator view, as the SEP reports it, holds that a credence $C(p)$ is justified only if it is based on a ground $g$ such that the objective probability of $p$ given $g$ approximates $C(p)$. The arguments point to a view of this kind with a process element: the ground is what the process uses. For the Brier score, the chance-expected inaccuracy of credence $f$, when the chance given $g$ is $c_g$, is $(f - c_g)^2 + c_g(1 - c_g)$. The second term is what the ground leaves unavoidable. The first, the excess, measures unreliability given the ground; for other strictly proper scores it is the divergence. The measure is not new. Chance-expected accuracy is central in accuracy-first epistemology (Pettigrew 2016 derives chance-credence norms from chance dominance). What is added here is the argument that the track-record alternative cannot do the job.

Clifton's statistical reliabilism, which ranks statistical credences by average closeness to objective probabilities relative to candidate models, is a comparative relative. Pettigrew (2021) argues that Dunn's and Tang's views are extensionally equivalent and offers a process-indicator hybrid connecting justification to accuracy. If his reading of Dunn is chance-based, his hybrid and the present view may coincide. On a track-record reading the equivalence cannot hold, since that reading is securable by an uninformed process and chance given grounds is not. So the thesis is: track-record calibrationism fails, and calibrationism on a chance reading is the chance view.

Four clarifications.

- *Grounds and resources.* (D1) restricts grounds to what a rule computable relative to the process's own could exploit. Under determinism with unrestricted grounds the chance is 0 or 1, so the restriction is needed. It brings with it the reference-class problem for coarse-grained chance (Hájek 2007), which is the main open problem for this view, as for any chance-relative account of everyday credence.
- *Basing.* Inputs a process receives but ignores are not its grounds.
- *The barometer.* Process reliability is separate from the agent's use of her evidence. An agent who ignores her barometer may have a process with small excess relative to its own coarse ground. Her fault is the one the alternative-process condition of Goldman (1979) addresses: a better process was available. Applying that condition requires ranking processes. Total chance-expected inaccuracy ranks the barometer-user higher, since her ground leaves less unavoidable. Calibration alone cannot rank them, since both processes are calibrated. A calibrationist who ranks by refinement, or by realized Brier score, can rank them too, but she then lets accuracy, not calibration, do the work.
- *Thresholds.* The measure is graded, whereas CR-S is a threshold claim. The arguments use only the threshold version.

Calibration seemed right because a chance-matching process is calibrated almost surely: in the sense of Section 2.1 when the chances lie on the grid, and in the averaged sense for every countable family of predictable rules (A2; the own-prior version is Dawid 1982). Calibration is how reliability shows up in the record. The theorems show that it can show up without reliability, in every world.

*The Humean worry.* If chances supervene on the total pattern, is the chance condition itself a test subject to (G)? Type I error control presupposes chances fixed in advance of the data, whereas a Humean chance is fixed by the pattern it summarizes. A Humean condition, a function of the whole record, is not a finite-time test, so (G)(i) and (ii) do not apply. Clause (iii) would apply only if the best-system map yielded a Borel test of next-period forecasts and outcomes, passed with probability one under every measure. That is doubtful, since best-system chances can diverge from non-ergodic measures. I flag this as the point where the positive view's independence from (G), like the conclusion of 5.1, depends most on the metaphysics of chance.

The cost of the view is that reliability cannot be read off a finite record. That is the externalist's standard situation: reliability need not be knowable to the agent for it to make her justified.

# 9. Conclusion

The modal and evidential defences of calibrationism assumed that uninformed calibration is lucky and fragile. It is not. For every reference family within the scope of Section 4, calibration can be secured by design in every world. Every history-based process also has a chance world in which a rule computable relative to its own matches the chances while it does not. So, given (R), no such standard suffices for reliability in the actual or nearby worlds. The core case is deterministic, feasible and set in an ordinary chance world; sharp calibration needs randomized witnesses and the computability reading. The standards that escape either remain insufficient or coincide with agreement with the chances, and in the computable case they leave individual credences unconstrained. Normal-worlds calibrationism remains open. On a non-reductive view of chance, reliability for credence is a relation to chances given grounds, and calibration is how it shows up in the record.

# Appendix

**A1. Lemma.** $\bar f_t(h)$ depends on $h$ alone, so $w_\rho$ is well defined (Ionescu-Tulcea). The path is independent of the randomization, so conditional on the path, $u$ has law $\lambda$.

- *(a)* If $\bar f_t < 1/2$, then $\int |\varphi_t - 0.9|\, d\lambda \ge 0.9 - \bar f_t > 0.4$; otherwise $\int |\varphi_t - 0.1|\, d\lambda \ge \bar f_t - 0.1 \ge 0.4$. Then apply Jensen.
- *(b)* Fix a path. The average distance $D_T$ lies in $[0, 0.9]$ and has mean at least 0.4. With $P = \lambda(D_T \ge 0.2)$, $0.4 \le 0.9P + 0.2(1 - P)$, so $P \ge 2/7$. $\square$

**A2. Chance-matchers are calibrated.** On days selected by a predictable rule, the $x_t - c_t$ are bounded martingale differences. By the martingale strong law, on the event that infinitely many days are selected, their average tends to zero almost surely. Within the grid cells this gives calibration of the chance-matcher, and countable unions extend it to countable families. With continuum-valued chances it gives, for each rule, convergence of mean credence minus mean outcome.

**A3. Propensity-binned calibration.** Fix an almost sure path in $w_\rho$. Let $G$ be the set of randomizations on which $\rho$ is $\varepsilon$-calibrated on the propensity classes, and let $s = \sqrt\varepsilon$. By Cauchy-Schwarz, on a calibrated class the mean credence and the mean outcome differ in the limit by at most $s$.

- *Case 1: $A = \{t : \bar f_t < 1/2\}$ is infinite.* There the frequency of rain tends to 0.9 (A2). On $G$, the liminf of the mean credence over $A$ is at least $0.9 - s$. Its average over randomizations is the mean propensity over $A$, which is below $1/2$. By Fatou, $(0.9 - s)\lambda(G) \le 1/2$.
- *Case 2: $A$ is finite.* Then the complement is cofinite, rain frequency there tends to 0.1, and on $G$ the limsup of the mean credence is at most $0.1 + s$. Its randomization average is at least $1/2$. By reverse Fatou, with credences bounded by one, $(0.1 + s)\lambda(G) + (1 - \lambda(G)) \ge 1/2$.

Either way, $\lambda(G) \le 1/(2(0.9 - s))$, which is below 1 when $s < 0.4$. $\square$

# References

Al-Najjar, N. I., Sandroni, A., Smorodinsky, R. and Weinstein, J. (2010). Testing theories with learnable and predictive representations. *Journal of Economic Theory* 145(6): 2203-2217.

Al-Najjar, N. I. and Weinstein, J. (2008). Comparative testing of experts. *Econometrica* 76(3): 541-559.

Blackwell, D. and Dubins, L. (1962). Merging of opinions with increasing information. *Annals of Mathematical Statistics* 33: 882-886.

Cesa-Bianchi, N. and Lugosi, G. (2006). *Prediction, Learning, and Games*. Cambridge: Cambridge University Press.

Clifton, J. (n.d.). Reliable credence and the foundations of statistics. Manuscript, PhilArchive, https://philarchive.org/rec/CLIRCA.

Dagan, Y., Daskalakis, C., Fishelson, M., Golowich, N., Kleinberg, R. and Okoroafor, P. (2025). Breaking the $T^{2/3}$ barrier for sequential calibration. *Proceedings of the 57th Annual ACM Symposium on Theory of Computing*, 2007-2018.

Dawid, A. P. (1982). The well-calibrated Bayesian. *Journal of the American Statistical Association* 77(379): 605-610.

Dawid, A. P. (1985a). Calibration-based empirical probability. *Annals of Statistics* 13(4): 1251-1274.

Dawid, A. P. (1985b). Comment [on Oakes]. *Journal of the American Statistical Association* 80: 340-341.

Dekel, E. and Feinberg, Y. (2006). Non-Bayesian testing of a stochastic prediction. *Review of Economic Studies* 73(4): 893-906.

Dunn, J. (2015). Reliability for degrees of belief. *Philosophical Studies* 172(7): 1929-1952.

Dwork, C., Kim, M. P., Reingold, O., Rothblum, G. N. and Yona, G. (2021). Outcome indistinguishability. *Proceedings of the 53rd Annual ACM Symposium on Theory of Computing*, 1095-1108.

Feinberg, Y. and Stewart, C. (2008). Testing multiple forecasters. *Econometrica* 76(3): 561-582.

Fortnow, L. and Vohra, R. V. (2009). The complexity of forecast testing. *Econometrica* 77(1): 93-105.

Foster, D. P. (1999). A proof of calibration via Blackwell's approachability theorem. *Games and Economic Behavior* 29: 73-78.

Foster, D. P. and Hart, S. (2018). Smooth calibration, leaky forecasts, finite recall, and Nash dynamics. *Games and Economic Behavior* 109: 271-293.

Foster, D. P. and Hart, S. (2023). "Calibeating": beating forecasters at their own game. *Theoretical Economics* 18(4): 1441-1474.

Foster, D. P., Rakhlin, A., Sridharan, K. and Tewari, A. (2011). Complexity-based approach to calibration with checking rules. *Proceedings of the 24th Annual Conference on Learning Theory*, PMLR 19: 293-314.

Foster, D. P. and Vohra, R. V. (1998). Asymptotic calibration. *Biometrika* 85(2): 379-390.

Gneiting, T., Balabdaoui, F. and Raftery, A. E. (2007). Probabilistic forecasts, calibration and sharpness. *Journal of the Royal Statistical Society B* 69(2): 243-268.

Goldman, A. (1979). What is justified belief? In G. Pappas (ed.), *Justification and Knowledge*, 1-23. Dordrecht: Reidel.

Goldman, A. (1986). *Epistemology and Cognition*. Cambridge, MA: Harvard University Press.

Goldman, A. and Beddor, B. (2019). Reliabilist epistemology. In E. N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy* (Fall 2019 Edition), https://plato.stanford.edu/archives/fall2019/entries/reliabilism/.

Gupta, V., Jung, C., Noarov, G., Pai, M. M. and Roth, A. (2022). Online multivalid learning: means, moments, and prediction intervals. *13th Innovations in Theoretical Computer Science Conference*, LIPIcs 215: 82:1-82:24.

Hájek, A. (2007). The reference class problem is your problem too. *Synthese* 156(3): 563-585.

Hu, T.-W. and Shmaya, E. (2013). Expressible inspections. *Theoretical Economics* 8(2): 263-280.

Kakade, S. M. and Foster, D. P. (2004). Deterministic calibration and Nash equilibrium. *Proceedings of the 17th Annual Conference on Learning Theory*, 33-48.

Lee, D., Noarov, G., Pai, M. and Roth, A. (2022). Online minimax multiobjective optimization: multicalibeating and other applications. *Advances in Neural Information Processing Systems* 35.

Oakes, D. (1985). Self-calibrating priors do not exist (with discussion). *Journal of the American Statistical Association* 80(390): 339-342.

Olszewski, W. and Sandroni, A. (2008). Manipulability of future-independent tests. *Econometrica* 76(6): 1437-1466.

Olszewski, W. and Sandroni, A. (2009a). Strategic manipulation of empirical tests. *Mathematics of Operations Research* 34(1): 57-70.

Olszewski, W. and Sandroni, A. (2009b). A nonmanipulable test. *Annals of Statistics* 37(2): 1013-1039.

Pettigrew, R. (2016). *Accuracy and the Laws of Credence*. Oxford: Oxford University Press.

Pettigrew, R. (2021). What is justified credence? *Episteme* 18(1): 16-30.

Putnam, H. (1963). "Degree of confirmation" and inductive logic. In P. A. Schilpp (ed.), *The Philosophy of Rudolf Carnap*, 761-783. La Salle, IL: Open Court.

Qiao, M. and Valiant, G. (2021). Stronger calibration lower bounds via sidestepping. *Proceedings of the 53rd Annual ACM Symposium on Theory of Computing*.

Sandroni, A. (2003). The reproducible properties of correct forecasts. *International Journal of Game Theory* 32(1): 151-159.

Sandroni, A., Smorodinsky, R. and Vohra, R. V. (2003). Calibration with many checking rules. *Mathematics of Operations Research* 28(1): 141-153.

Schurz, G. (2019). *Hume's Problem Solved: The Optimality of Meta-Induction*. Cambridge, MA: MIT Press.

Seidenfeld, T. (1985). Calibration, coherence, and scoring rules. *Philosophy of Science* 52(2): 274-294.

Shmaya, E. (2008). Many inspections are manipulable. *Theoretical Economics* 3(3): 367-382.

Tang, W. H. (2016). Reliability theories of justified credence. *Mind* 125(497): 63-94.
