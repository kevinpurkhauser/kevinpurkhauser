---
title: "Calibrated Everywhere: A Dilemma for Track-Record Reliabilism about Credence"
---

# 1. Introduction

A reliabilist about justified credence needs a measure of reliability for processes that output credences, not beliefs. Measuring credences by their closeness to the truth values, as the Brier score does, penalizes a process for producing middling credences even in a domain where nothing better is possible. The leading alternative, developed by Dunn (2015) from a suggestion of Ramsey's, is calibration: a process is well calibrated if, among the propositions to which it assigns credence $p$, a proportion $p$ are true. In the formulation of the *Stanford Encyclopedia* entry on reliabilism (Goldman and Beddor), a credence is justified iff it is produced by a well-calibrated process.

This paper argues for a dilemma. On the first horn, take any calibration standard whose reference classes are fixed independently of the process being assessed and are not too rich: countably many, or of bounded complexity. Assess it over any range of worlds, with any positive tolerance. Then some process that has no information about how the data are generated meets the standard in every world. This follows from a theorem of Foster and Vohra (1998) and its descendants. I add an elementary lemma: every process of the relevant kind has a world in which its credences are, on average, far from the chances given its own inputs, although another process with the same inputs matches those chances. So no such standard is sufficient for reliability. On the second horn, take the standards that cannot be met in every world. These fix their reference classes relative to the process assessed, or make them as rich as all computable classes, or assess calibration across worlds. They escape the first horn only by building in agreement with the chances. Calibration relative to all computable reference classes, for instance, forces asymptotic agreement with the chances in every world whose chances are computable (Dawid 1985). Either way, track-record calibration is not what makes a credence-forming process reliable. Through the expert-testing literature (Sandroni 2003; Olszewski and Sandroni 2008; Shmaya 2008), the first horn extends to every outcome-based standard of a precisely specified kind. The positive upshot is a chance-relative account of reliability for credence, close to Tang's (2016), with a graded measure taken from accuracy-first epistemology.

Section 2 states calibrationism. Section 3 states the mathematics. Section 4 gives the argument for the first horn, and Section 5 the second. Section 6 answers objections. Section 7 generalizes the first horn and marks its limits. Section 8 draws the positive conclusion.

# 2. Calibrationism

## 2.1 Definitions

Consider yes-or-no questions, one per day: will it rain on day $t$? Write $x_t \in \{0,1\}$. A *credence-forming process* issues on day $t$ a credence $f_t \in [0,1]$ that $x_t=1$. Its inputs may include the day's index, the history of earlier outcomes and of its own earlier credences, a label $z_t$ for the agent's other evidence (a barometer reading, a testimony), and a private randomizing device. Call a process *history-based* if these are its only inputs and its rule for turning them into credences is fixed in advance. Every inductive learner is history-based in this sense, including Bayesians with priors and frequentists. Such a process is *uninformed* if its rule does not encode any information about how the outcomes are generated.

Fix a finite grid of credence values. For each grid value $p$, let $N_T(p)$ be the number of days up to $T$ on which the process gave $p$, and $q_T(p)$ the proportion of them on which it rained. The calibration score is $C_T = \sum_p \frac{N_T(p)}{T}(q_T(p)-p)^2$. A process is *$\varepsilon$-calibrated* on a run if $\limsup_T C_T \leq \varepsilon$. A *reference class* is given by a predictable checking rule, which selects days on the basis of information available before the outcome (index, history, label, current credence). Calibration *relative to a family* $\mathcal R$ requires $\varepsilon$-calibration on each selected subsequence that is infinite. *Smooth* calibration, at bandwidth $\delta$, replaces the sharp grid cells by weighted averages over credences within $\delta$ of each other.

## 2.2 The schema

Let $X$ be a calibration standard (sharp or smooth, tolerance $\varepsilon$, family $\mathcal R$, limiting or over a finite horizon). Let $W(w,\rho)$ be the set of worlds relevant to assessing process $\rho$ at $w$: the actual world, the actual and nearby worlds, the normal worlds, or all worlds. The sufficiency half of calibrationist reliabilism is:

> **CR-S(X, W).** If $\rho$ is $X$-calibrated throughout $W(@,\rho)$, then $\rho$ is reliable in the actual world $@$, and its actual credences are justified.

I assume only that every range in question is *reflexive at a normal actual world*: if the actual world is one in which the agent's general beliefs about her environment are true, it belongs to $W(@,\rho)$. Actual-world, nearby-world and normal-world ranges all satisfy this. Necessity is not at issue. (Dorst 2023 argues, from another direction, that rational agents can be expected to be miscalibrated.)

## 2.3 How calibrationism answered its critics

The SEP entry reports Goldman's (1986) case of an agent seventy per cent of whose opinions are true and who is perfectly calibrated by giving everything credence 0.7. It also reports the reply: look across a range of nearby worlds. If it is "just a matter of chance" that seventy per cent are true, the process will be miscalibrated in nearby worlds. Dunn writes that "we should not merely look at the actual cases that these processes have performed on. We must also look at how they perform in nearby worlds." The SEP attributes to Tang (2016) a second objection: a process may be well calibrated while insensitive to relevant evidence. The natural reply is to condition calibration on the agent's evidence.

Both replies rest on one assumption. A process that reaches calibration without being suitably connected to the world reaches it by luck, so its calibration should be fragile under variation of the world or of the evidence cell. The theorems below show that this assumption is false.

## 2.4 What calibration was meant to secure

(D1) A process should not be penalized for middling credences where the truth is not more predictable *from the process's inputs*. (D2) Reliability should be a matter of the process's track record, actual and counterfactual. I keep (D1), stated with the italicized clause, which is the only form in which it is plausible. I reject (D2).

# 3. Calibration without information

## 3.1 Theorems

**Theorem 1** (Foster and Vohra 1998; see also Foster 1999). For every $\varepsilon>0$ there is a randomized, uninformed, history-based procedure with credences on a finite grid that is $\varepsilon$-calibrated, almost surely relative to its own randomization, against every sequence of outcomes. This includes sequences chosen by an adversary who sees past outcomes and past credences but not the current randomization.

Four qualifications. (i) Randomization is essential. For every deterministic procedure there is a sequence on which it is badly miscalibrated (Oakes 1985; Dawid 1985): let it rain exactly when the procedure's credence is below one half. (ii) "Every sequence" covers every chance process in which the weather is independent of the procedure's current coin given the past. (iii) A positive tolerance is needed. With a fixed finite grid, exact calibration is impossible in general for any procedure, informed or not, since the chance may lie off the grid. (iv) Finite versions exist. The expected $\ell_1$ calibration error after $T$ days can be kept, uniformly over sequences, slightly below order $T^{-1/3}$ (Dagan et al. 2025 improve the classical $T^{-1/3}$). No procedure can guarantee better than about $T^{-0.46}$ (Qiao and Valiant 2021; Dagan et al. 2025).

Three strengthenings matter.

*Deterministic procedures.* Kakade and Foster (2004) obtained deterministic weak calibration. Foster and Hart (2018) show that "smooth calibration can be guaranteed by deterministic procedures", even when forecasts are announced in advance, with finite recall, stationarity and a finite grid. The guarantee holds at a fixed bandwidth and a positive tolerance; as the bandwidth shrinks to zero, smooth calibration becomes sharp calibration, which no deterministic procedure can guarantee.

*Many reference classes.* For each countable family of checking rules there is a procedure calibrated on every rule in the family, for every sequence (Sandroni, Smorodinsky and Vohra 2003). Foster, Rakhlin, Sridharan and Tewari (2011) extend this to uncountable families of bounded complexity. Online multicalibration (Gupta et al. 2022) gives the analogous guarantee for calibration on each of a family of overlapping groups defined by labels, against adversarial data. The quantifiers matter: for each family there is a procedure, not one procedure for all families.

*Uninformedness.* In each case the procedure uses labels only as labels. It needs no information about how evidence bears on outcomes.

## 3.2 The anti-tracking lemma

Let $\rho$ be history-based. Write $\varphi_t(h,u)$ for its credence on day $t$ given history $h$ (including the current label) and coin sequence $u$. Let $\bar f_t(h)=\int \varphi_t(h,u)\,d\lambda(u)$ be its *propensity*: the average over coin sequences, a function of $h$ alone. Define the world $w_\rho$ as follows. Labels are generated by any fixed mechanism independent of the coins. The chance of rain on day $t$, given $h$, is $c_t = 0.9$ if $\bar f_t(h)<1/2$ and $c_t=0.1$ otherwise.

**Lemma.** In $w_\rho$:
(a) on every day and every history, the expected distance $\int|\varphi_t(h,u)-c_t|\,d\lambda(u)$ is at least 0.4;
(b) for every outcome path and every horizon $T$, the set of coin sequences $u$ on which the average distance $\frac1T\sum_{t\le T}|\varphi_t(h_t,u)-c_t|$ is at least 0.2 has probability at least $2/7$.

Proofs are in the Appendix. Three features matter. First, $w_\rho$ is an ordinary exogenous chance world: the chance of rain is a fixed function of the past weather and labels, and nothing in it reacts to the process. Second, the chances are 0.9 and 0.1, not middling. Third, the chance is a function of the very inputs $\rho$ uses. So the process $\rho^*$ with credence $c_t$ is itself history-based, with the same inputs as $\rho$. If $\rho$ is computable, with rational coin biases, then $w_\rho$ is a computable chance process. A Bayesian whose prior gives $w_\rho$ positive weight then merges with it (Blackwell and Dubins 1962), so its credences approach $c_t$. Reliability is attainable in $w_\rho$ from $\rho$'s inputs without antecedent knowledge of its chances.

What do the procedures of Section 3.1 do in their anti-tracking worlds? They are calibrated there, as everywhere, and the chance-matcher $\rho^*$ is calibrated too, almost surely (Appendix). The calibrated procedure keeps its credences near one half, mixing rainy days just below one half with dry days just above it. It is a near-constant one-half forecaster facing chances of 0.9 and 0.1 that are a fixed function of its own inputs.

# 4. The first horn

Call a standard $S$ *world-independently securable* if some history-based process $\sigma$ satisfies: in every world, $\sigma$'s record meets $S$ with probability at least $1-\eta$, for some $\eta<2/7$. Here "record" means the realized run, and the probability is taken over the world's chances and $\sigma$'s coins. The argument needs one normative premise.

> **(R)** Suppose that in world $w$, over horizons $T$ that grow without bound, the average distance between a process's credences and the chances of their contents given the process's inputs is at least 0.2, while some process with the same inputs has credences equal to those chances. Then the first process is not reliable in $w$.

1. For every history-based $\sigma$, there is a world $w_\sigma$ such that, with probability at least $2/7$, the realized run of $\sigma$ in $w_\sigma$ satisfies the antecedent of (R). (Lemma (b). Fix the coin sequence; the resulting deterministic process has the same inputs as $\rho^*$. A reverse-Fatou step gives "for unboundedly many $T$".)
2. Suppose $S$ is world-independently securable, witnessed by $\sigma$. In $w_\sigma$, the event that $\sigma$'s record meets $S$ has probability at least $1-\eta>5/7$. So it intersects the event in step 1 with probability at least $2/7-\eta>0$.
3. Suppose $S$ is sufficient for reliability: whenever a process's record in a world meets $S$, the process is reliable there. Then on that intersection, $\sigma$ (individuated by its coins) is reliable in $w_\sigma$, by this supposition, and not reliable in $w_\sigma$, by (R). Contradiction.
4. So no world-independently securable standard is sufficient for reliability.
5. Let $X$ have a positive tolerance (or be smooth at a fixed bandwidth), and let its family $\mathcal R$ be fixed independently of the assessed process and be countable or of bounded complexity. Let $W$ be any range. Then "$X$-calibrated throughout $W(@,\rho)$" is world-independently securable, with $\eta=0$. (Theorem 1 and its strengthenings. The witness is calibrated almost surely in every world, so in every world of every range. For the deterministic Foster-Hart witness no coins are involved, and Lemma (a) applies directly.)
6. Let $@=w_\sigma$ for the witness $\sigma$ of step 5. Since $w_\sigma$ can be a normal world, $@\in W(@,\sigma)$. If CR-S$(X,W)$ held, then whenever the actual record meets the standard, $\sigma$ would be reliable in $@$. By steps 2 and 3 this fails with positive probability. Since reliabilism grounds justification in reliability, CR-S$(X,W)$ is false.

For finite-horizon standards with a tolerance, step 5 holds only beyond a horizon that depends on the tolerance and on $\eta$, by high-probability versions of the finite-sample bounds. The range of worlds drops out because the witness is calibrated in every world. The family $\mathcal R$ drops out because the witnesses of Section 3.1 exist for each fixed family.

The rejected assumption of Section 2.3 is now visible. The uniform 0.7 process is calibrated by luck. The Foster-Vohra procedure is calibrated by design. No set of worlds over which a process $Q$ is calibrated is a set over which the procedure is not.

## 4.1 Defending (R)

(R) is chance-relative, and a calibrationist who identifies reliability with calibration will reject it. Section 6.1 considers that response. Here are the reasons to accept (R) in the cases at issue.

*It respects (D1).* (R) does not penalize a process for failing to match chances that are unpredictable from its inputs. It applies only when the chance is a function of the process's own inputs and a process using those inputs matches it. In $w_\rho$, moreover, a general-purpose learner with no antecedent knowledge of the chances converges to them.

*It is backed by the track record itself.* Let $\rho^*$ match the chances. On any run, the difference between the realized average Brier scores of $\rho$ and $\rho^*$ equals the average of $(f_t-c_t)^2$ plus an average of martingale differences, which tends to zero almost surely. So whenever $\rho$'s average distance from the chances is at least 0.2, its realized average Brier score exceeds $\rho^*$'s by at least about $0.04$. In expectation the gap is larger. Under every strictly proper scoring rule, a credence equal to the chance uniquely minimizes chance-expected inaccuracy. By Lemma (a), the randomized process's chance-expected Brier inaccuracy is at least $0.4^2+0.09=0.25$ every day, the same as always saying one half. The chance-matcher's is $0.09$. Both processes are calibrated. The track record that calibration consults separates them, but calibration does not.

*It is weak in the relevant sense.* (R) does not say that reliability is closeness to chance. It says only that large average distance from chances that a same-input process attains is a sufficient condition for unreliability.

# 5. The second horn

Step 5 needs the family $\mathcal R$ to be fixed independently of the process and to be countable or of bounded complexity. There are three ways to violate these conditions. Each escapes securability, and each escapes only by importing agreement with the chances.

## 5.1 Process-relative reference classes

Let $\mathcal R(\rho)$ include the classes $\{t:\bar f_t\in I\}$ for rational intervals $I$. These are calibration cells for the process's propensity rather than its realized output. This is a natural move: a process type is a map from inputs to output distributions, and for a randomizing agent the propensity is a candidate for the credence. No process is calibrated on $\{t:\bar f_t<1/2\}$ in its own anti-tracking world (Appendix A3), so propensity-binned calibration is not securable.

It is still not sufficient for reliability. Take the process that always says one half, and any countable family $\mathcal R$ of predictable rules, including rules relative to that process. There is a fixed binary sequence $b$ such that, in the world where the chance of rain on day $t$ is $0.1+0.8b_t$, the one-half process is calibrated on every rule in $\mathcal R$ almost surely (Appendix A4). Its distance from the chance is 0.4 every day. The chance is a function of the day's index, which is an input, so a same-input process with credence $0.1+0.8b_t$ exists, and (R) applies. The calibrationist can resist only by denying that this same-input process is a legitimate competitor, because it encodes an arbitrary sequence. The principled version of that denial restricts processes to computable ones, which leads to the next case.

## 5.2 Computable calibration

Restrict processes to computable ones and let $\mathcal R$ be the family of all computable checking rules. For a computable process, the class $\{t:\bar f_t<1/2\}$ is computable. So no computable process is calibrated on all computable rules in every world, and the standard is not securable by any process the view admits. (The procedure of Sandroni et al. for this countable family exists but is not computable.) This version, close to Dawid's (1985) calibration-based theory of empirical probability, is the strongest calibrationism I know of. But Dawid proves that any two sequences of forecasts that meet this criterion "must be in asymptotic agreement". In a world whose chances are computable, the chance-matcher meets it almost surely (by the argument of A2, applied to countably many rules). So a computable process meets it only if its credences agree asymptotically with the chances. Computable calibrationism escapes the first horn by becoming, in every computable-chance world, a criterion of asymptotic agreement with the chances. In worlds with non-computable chances it can approve processes far from the chances, as in 5.1. Where no admissible process could do better, that verdict is an application of (D1), not a rival to (R).

Two further limits remain. First, the criterion constrains only the limit. Any finite stretch of credences, and any set of occasions of density zero, is unconstrained. Second, any version that checks only a fixed finite set of computable rules over a finite horizon falls back onto the first horn, since a computable calibrated procedure exists for each finite family.

## 5.3 Cross-world calibration

Dunn's slogan can also be read synchronically. Among the nearby worlds that share the actual history and in which the process gives credence $p$, a proportion $p$ have rain. Such a proportion needs a measure on worlds. Counting is undefined over infinitely many worlds, and the natural measure is the chance distribution over continuations of the history. On that measure the cross-world proportion of rain at a history is the chance given the history. So cross-world calibration at each history is chance-matching given the inputs, and Theorem 1 says nothing about it.

## 5.4 The dilemma

Calibration standards that can be secured in every world are insufficient for reliability. Those that cannot be secured either remain insufficient (5.1) or owe their discriminating power to agreement with the chances, asymptotically (5.2) or directly (5.3). In no case is calibration as a track-record property, (D2), what reliability consists in.

# 6. Objections

## 6.1 Reliability just is calibration

The calibrationist may reject (R) and identify reliability with calibration. Then reliability is a property that one process has in every environment by design. It therefore says nothing about the fit between process and environment. Reliabilism explained justification by truth-conduciveness in the subject's environment, and the definitional reply gives this up. It also counts as maximally reliable a process whose realized Brier score exceeds a same-input competitor's in its environment by a fixed margin. Pettigrew (2021) presses a Connection Problem against existing reliabilist accounts of justified credence: it is unclear how justification so understood connects to anything of epistemic value. The definitional reply makes the problem acute. On it, maximal reliability is compatible with every degree of avoidable inaccuracy.

## 6.2 The witness is a learner

The Foster-Vohra procedure learns from outcomes. In worlds where days are independent, calibration forces its credences toward the frequencies. I grant this. The argument needs only that CR-S is wrong about the procedure in its anti-tracking world. There is also a reason to doubt that the procedure models evidential responsiveness. Dawid (1982) proved that a coherent Bayesian assigns probability one to being well calibrated. Oakes (1985) reports Dawid's observation that a coherent forecaster cannot adjust future forecasts to correct past miscalibration without sacrificing coherence. The Foster-Vohra procedure does exactly that, which is why its calibration holds in every world and is no evidence of fit with any.

## 6.3 Randomization, individuation, generality

One may doubt that a coin-fixed credence is a credence. The deterministic Foster-Hart procedure answers this for smooth calibration. For sharp calibration, Lemma (b) handles both individuations. Individuate the process broadly (the randomized rule), and Lemma (a) gives large expected distance every day. Individuate it narrowly (the rule with its coin sequence fixed, or with the theory drawn at the outset), and Lemma (b) gives, with probability at least $2/7$, a deterministic process that is calibrated and far from the chances on average. Identifying the credence with the propensity instead leads to 5.1.

The generality problem does not obviously help. A broad type such as "extrapolating from the weather record" contains processes that are miscalibrated in $w_\rho$, so a calibrationist who types broadly may condemn the procedure there. But then the verdict depends on the typing, not on the procedure's fit with the world. The algorithm itself is an admissible type for any agent who implements it. The calibrationist would need a principle that excludes it, and that principle would have to distinguish it from good learners by something other than calibration.

## 6.4 Demon worlds and normal worlds

$w_\rho$ resembles a demon world, and many think demon-world victims are justified. Is calibrationism's verdict about $w_\rho$ then a virtue? There are two differences. In $w_\rho$ the truth is predictable from the agent's inputs, and a same-input learner tracks it; a demon world is one where it is not. And the internalist intuition credits the victim's good response to her evidence, whereas unconditional calibrationism delivers its verdict whether or not the process uses the evidence at all (an agent who ignores an informative barometer is calibrated in every world). A reliabilist who wants the demon-world verdict can assess reliability in normal worlds. Step 6 shows that this does not save normal-worlds calibrationism, since $w_\sigma$ can be the actual, normal world.

## 6.5 Comparative calibrationism

Suppose a process is reliable only if it is calibrated and not beaten in realized accuracy by any member of a fixed countable class $\mathcal C$ of processes with the same inputs. If there is a calibrated aggregator of $\mathcal C$ whose realized score asymptotically matches the best member of $\mathcal C$ on every sequence, as the theory of prediction with expert advice suggests for square loss, the standard is securable. In the aggregator's anti-tracking world, the best member of $\mathcal C$ is then, on average, far from the chances. If instead $\mathcal C$ contains the chance-matcher of every world, the standard measures closeness to the chances by another name. Structurally this resembles meta-inductive optimality (Schurz 2019): a world-independent guarantee relative to accessible methods. By step 4, such a guarantee is a different virtue from reliability.

# 7. Beyond calibration

A *test* passes or fails a forecaster on the basis of forecasts and data. It *controls type I error* at level $\eta$ if a forecaster who forecasts by the true probabilities passes with probability at least $1-\eta$, whatever they are.

**Theorem 2.**
(a) (Sandroni 2003.) Over a finite horizon, every test that controls type I error at level $\eta$ can be passed by an uninformed forecaster with probability at least $1-\eta-\delta$, for any $\delta>0$, whatever the data. The forecaster draws a theory at the outset, by a distribution obtained from Fan's minimax theorem.
(b) (Olszewski and Sandroni 2008.) The same holds for future-independent tests that reject theories in finite time. In their words, "tests which cannot be ignorantly passed must rely on predictions about data not yet observed, and such tests cannot be run if forecasters report only the probability of the next period's events on the basis of the actually observed data."
(c) (Shmaya 2008.) If a test is Borel and a forecaster who knows the truth always passes it, then an ignorant forecaster can pass it with probability arbitrarily close to one.

These forecasters are history-based once their initial draw is counted as a coin, so the Lemma applies. A record of credences actually formed is exactly what Olszewski and Sandroni describe: next-period probabilities based on the observed data. Running the argument of Section 4 with Theorem 2 in place of step 5 gives:

> **(G)** No standard on the record of credences actually formed is sufficient for reliability if it is (i) finite-horizon, or (ii) future-independent and rejects in finite time, and is met by a chance-matcher with probability at least $1-\eta$ in every world, for some $\eta < 2/7$; or if it is (iii) Borel and met by a chance-matcher with probability one in every world.

(G) is narrower than "no outcome-based test separates informed from uninformed forecasters", which is false. The exceptions are instructive.

*Tests that use predictions about unobserved data.* Dekel and Feinberg (2006) give a test that the truth passes and that a false theory fails on all but a topologically small set of distributions; their strongest result uses the continuum hypothesis. Olszewski and Sandroni (2009b) give a test that controls type I error and is non-manipulable, without that hypothesis. Such tests can reject in finite time, but they do so on the basis of the theory's predictions about data not yet observed. A process's record of credences actually formed does not contain these predictions.

*Computational bounds.* Fortnow and Vohra (2009) give an efficient test that, under standard hardness assumptions, no efficient uninformed forecaster passes. Calibration, by contrast, is passed by efficient procedures, and their test is designed to make passing hard, not to measure reliability.

*Restricted theories.* If admissible theories are restricted to those with learnable and predictive representations, non-manipulable tests exist (Al-Najjar, Sandroni, Smorodinsky and Weinstein 2010). Olszewski and Sandroni (2009a) conclude that such restrictions help "only to a limited extent". The restriction concerns which chance processes are possible.

*Comparison.* Al-Najjar and Weinstein (2008) give a record-based test for two experts, one of whom knows the true distribution. It identifies the informed expert, or else finds that the two experts' forecasts are close, within any precision in finite time. The single-expert impossibility, they note, arises because nature's mixtures over distributions reduce to pure strategies, and the presence of an informed expert prevents this. The test is record-based, but its guarantee presupposes a competitor whose forecasts are the chances. Feinberg and Stewart (2008) obtain related results for several forecasters.

Each exception brings in something outside the record of credences actually formed: predictions about unobserved data, bounds on computation, a restriction on the possible chance processes, or a benchmark that knows the chances.

# 8. What reliability for credence must be

Tang's indicator view, as the SEP reports it, holds that a credence $C(p)$ is justified only if it is based on a ground $g$ such that the objective probability of $p$ given $g$ approximates $C(p)$. Both horns point to a view of this form, with the ground identified with what the process takes as input. The view can be graded with a standard tool of accuracy-first epistemology, in which chance-expected accuracy plays a central role (Pettigrew 2016 derives chance-credence norms from chance dominance). For the Brier score, the chance-expected inaccuracy of credence $f$ when the chance given the ground is $c_g$ is $(f-c_g)^2 + c_g(1-c_g)$. The second term is the inaccuracy that the ground leaves unavoidable. The first, the excess, is a natural measure of unreliability; for a general strictly proper score it is the associated divergence between $c_g$ and $f$. This measure satisfies (D1) in its plausible form: a process matching middling chances given its inputs incurs no excess. It connects reliability with accuracy, as Pettigrew's Connection Problem demands. It also makes the basing relation precise, because the ground is what the process uses. For the Foster-Vohra procedure that is the history and its coins, and in an exogenous world the chance given these is the world's chance, not the procedure's output.

This also explains why calibration seemed right. A chance-matching process is calibrated almost surely, in the sense of Section 2.1 when the chances lie on the grid, and in the averaged sense along every countable family of predictable rules in general (Appendix A2; the own-prior version is Dawid's 1982 theorem). Calibration is a symptom of reliability. The theorems show that the symptom can be produced without the condition, in every world. Pettigrew (2021) argues that Dunn's process view and Tang's indicator view, suitably understood, are extensionally equivalent, and offers a hybrid of his own. The present results show what the suitable understanding must exclude: calibration read as a track-record property is securable by an uninformed process, and chance given grounds is not.

*The Humean worry.* If chances supervene on the total pattern of outcomes, is the chance condition outcome-based after all, and so subject to (G)? The main answer is that type I error control presupposes chances given in advance of the data. The testing theorems quantify over fixed data-generating measures, and a Humean chance is not fixed in advance of the pattern it summarizes. So (G)'s hypotheses have no clear application to a Humean chance condition. A further point: a Humean chance on a given day depends on the whole pattern, including the future. That alone does not exempt the condition, since Shmaya's theorem needs no future-independence; whether it applies depends on whether the best-system map is Borel and well defined, which I leave open.

The view has a cost, and I accept it. Reliability so understood cannot be read off any finite record, and by (G) no record-based surrogate of the specified kinds can certify it.

# 9. Conclusion

Calibrationism answered its first critics by requiring calibration to be modally robust and conditioned on evidence. Both answers assumed that uninformed calibration is lucky and therefore fragile. The Foster-Vohra theorem and its descendants show that it can be secured in every world, for any fixed family of reference classes of bounded richness. Every history-based process has an exogenous world in which a same-input process matches the chances while it does not. So no securable standard is sufficient for reliability. The standards that resist securing do so by building in agreement with the chances. Reliability for credence is a relation to chances given grounds. Calibration is how such reliability shows up in the record, not what it consists in.

# Appendix

**A1. Proof of the Lemma.** $\bar f_t(h)$ is defined by integrating the rule over coin sequences, so it depends only on $h$, and $w_\rho$ is well defined by the Ionescu-Tulcea theorem. Outcomes and labels in $w_\rho$ depend only on the past and on the fixed label mechanism, so the coins are independent of the weather. For (a): if $\bar f_t(h)<1/2$, then $\int|\varphi_t-0.9|\,d\lambda \geq 0.9-\bar f_t(h) > 0.4$; otherwise $\int|\varphi_t-0.1|\,d\lambda\geq \bar f_t(h)-0.1\geq 0.4$. For (b): fix a path. The average distance $D_T(u)$ lies in $[0,0.9]$ and, by (a), has $\lambda$-mean at least 0.4. So $0.4 \leq 0.9\,\lambda(D_T\geq 0.2)+0.2$, giving $\lambda(D_T\geq0.2)\geq 2/7$. By reverse Fatou, the probability that $D_T\geq 0.2$ for infinitely many $T$ is also at least $2/7$. $\square$

**A2. Chance-matchers are calibrated.** Let a rule select days predictably. Then the differences $x_t-c_t$ on the selected days are bounded martingale differences. By the strong law for martingales, on the event that infinitely many days are selected, the average of $x_t - c_t$ over them tends to zero almost surely. Applied within the grid cells for 0.9 and 0.1, this gives calibration of $\rho^*$ in $w_\rho$; a countable union of null sets extends it to any countable family. With continuum-valued chances, the same argument gives, for each predictable rule, convergence of mean credence minus mean outcome on the selected days.

**A3. Propensity-binned calibration fails in the anti-tracking world.** On $\{t:\bar f_t<1/2\}$ the chance is 0.9, so the frequency of rain there tends to 0.9 almost surely (A2). The average realized credence there tracks the average propensity, by the martingale strong law applied to $\varphi_t-\bar f_t$, and so stays below one half. Hence calibration fails on this class whenever it has positive upper density. Otherwise its complement has density one, and the same argument with 0.1 applies.

**A4. The hidden-sequence world.** Let $B_1,B_2,\dots$ be independent fair bits and, given $B$, let $x_t$ be independent with chance $0.1+0.8B_t$. Unconditionally, $x_t$ given the past is a fair coin, and the one-half process's credences carry no information. So for each predictable rule the selected frequency of rain tends to one half almost surely (A2), and the one-half process is calibrated on any countable family almost surely. By Fubini's theorem, for almost every fixed sequence $b$, this holds almost surely in the world with chances $0.1+0.8b_t$. $\square$

# References

Al-Najjar, N. I., Sandroni, A., Smorodinsky, R. and Weinstein, J. (2010). Testing theories with learnable and predictive representations. *Journal of Economic Theory* 145(6): 2203-2217.

Al-Najjar, N. I. and Weinstein, J. (2008). Comparative testing of experts. *Econometrica* 76(3): 541-559.

Blackwell, D. and Dubins, L. (1962). Merging of opinions with increasing information. *Annals of Mathematical Statistics* 33: 882-886.

Dagan, Y., Daskalakis, C., Fishelson, M., Golowich, N., Kleinberg, R. and Okoroafor, P. (2025). Breaking the $T^{2/3}$ barrier for sequential calibration. *Proceedings of the 57th Annual ACM Symposium on Theory of Computing*, 2007-2018.

Dawid, A. P. (1982). The well-calibrated Bayesian. *Journal of the American Statistical Association* 77: 605-613.

Dawid, A. P. (1985). Calibration-based empirical probability. *Annals of Statistics* 13(4): 1251-1274.

Dekel, E. and Feinberg, Y. (2006). Non-Bayesian testing of a stochastic prediction. *Review of Economic Studies* 73(4): 893-906.

Dorst, K. (2023). Being rational and being wrong. *Philosophers' Imprint* 23.

Dunn, J. (2015). Reliability for degrees of belief. *Philosophical Studies* 172(7): 1929-1952.

Feinberg, Y. and Stewart, C. (2008). Testing multiple forecasters. *Econometrica* 76(3): 561-582.

Fortnow, L. and Vohra, R. V. (2009). The complexity of forecast testing. *Econometrica* 77(1): 93-105.

Foster, D. P. (1999). A proof of calibration via Blackwell's approachability theorem. *Games and Economic Behavior* 29: 73-78.

Foster, D. P. and Hart, S. (2018). Smooth calibration, leaky forecasts, finite recall, and Nash dynamics. *Games and Economic Behavior* 109: 271-293.

Foster, D. P., Rakhlin, A., Sridharan, K. and Tewari, A. (2011). Complexity-based approach to calibration with checking rules. *Proceedings of the 24th Annual Conference on Learning Theory*, PMLR 19: 293-314.

Foster, D. P. and Vohra, R. V. (1998). Asymptotic calibration. *Biometrika* 85(2): 379-390.

Goldman, A. (1986). *Epistemology and Cognition*. Cambridge, MA: Harvard University Press.

Goldman, A. and Beddor, B. Reliabilist epistemology. In E. N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy*.

Gupta, V., Jung, C., Noarov, G., Pai, M. M. and Roth, A. (2022). Online multivalid learning: means, moments, and prediction intervals. *13th Innovations in Theoretical Computer Science Conference*, LIPIcs 215: 82:1-82:24.

Kakade, S. M. and Foster, D. P. (2004). Deterministic calibration and Nash equilibrium. *Proceedings of the 17th Annual Conference on Learning Theory*, 33-48.

Oakes, D. (1985). Self-calibrating priors do not exist. *Journal of the American Statistical Association* 80: 339.

Olszewski, W. and Sandroni, A. (2008). Manipulability of future-independent tests. *Econometrica* 76(6): 1437-1466.

Olszewski, W. and Sandroni, A. (2009a). Strategic manipulation of empirical tests. *Mathematics of Operations Research* 34(1): 57-70.

Olszewski, W. and Sandroni, A. (2009b). A nonmanipulable test. *Annals of Statistics* 37(2): 1013-1039.

Pettigrew, R. (2016). *Accuracy and the Laws of Credence*. Oxford: Oxford University Press.

Pettigrew, R. (2021). What is justified credence? *Episteme* 18(1): 16-30.

Qiao, M. and Valiant, G. (2021). Stronger calibration lower bounds via sidestepping. *Proceedings of the 53rd Annual ACM Symposium on Theory of Computing*.

Sandroni, A. (2003). The reproducible properties of correct forecasts. *International Journal of Game Theory* 32: 151-159.

Sandroni, A., Smorodinsky, R. and Vohra, R. V. (2003). Calibration with many checking rules. *Mathematics of Operations Research* 28(1): 141-153.

Schurz, G. (2019). *Hume's Problem Solved: The Optimality of Meta-Induction*. Cambridge, MA: MIT Press.

Shmaya, E. (2008). Many inspections are manipulable. *Theoretical Economics* 3: 367-382.

Tang, W. H. (2016). Reliability theories of justified credence. *Mind* 125(497): 63-94.
