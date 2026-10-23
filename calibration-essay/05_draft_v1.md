---
title: "Calibrated Everywhere, Reliable Nowhere: A Theorem Against Track-Record Reliabilism about Credence"
---

# 1. Introduction

Process reliabilism says that a belief is justified when it is produced by a reliable process, and it measures reliability by the proportion of true beliefs a process produces. Credences are not true or false, so a reliabilist about justified credence needs another measure. Measuring credences by their closeness to the truth values, as the Brier score does, punishes a process that produces middling credences even in a domain where middling credences are all that anyone could reasonably have. The leading alternative, due to Dunn (2015) and following a suggestion of Ramsey's, is calibration: a process is well calibrated if, among the propositions to which it assigns credence $p$, a proportion $p$ are true. The resulting view, in the formulation of the *Stanford Encyclopedia* entry on reliabilism (Goldman and Beddor), is that a credence is justified iff it is produced by a well-calibrated process.

This paper argues that calibration cannot play this role, however it is strengthened, and that the reason is a theorem. Foster and Vohra (1998) showed that there is a forecasting procedure that uses no information about the process generating the data and is nonetheless calibrated, almost surely, on every sequence of outcomes. I add an elementary lemma: every procedure of this kind has a world in which its credences are, on every occasion, far from the chances. Put together, these facts show that calibration is a standard that a single process can meet in every world, while reliability is a standard that no such process meets in every world. So calibration is not sufficient for reliability. The argument does not depend on which reference classes calibration is relativized to, nor on which range of worlds it is assessed over. It extends, through the expert-testing literature in economics (Sandroni 2003; Olszewski and Sandroni 2008; Shmaya 2008), to every outcome-based standard of a broad and precisely specifiable kind. I state where the extension stops. The positive upshot is that reliability for credence is not a track-record property at all: it is a relation between credences and chances given grounds, of the kind Tang (2016) proposed on other grounds.

Section 2 states calibrationism in a parametrized form. Section 3 states the mathematics. Section 4 gives the argument. Section 5 answers objections. Section 6 generalizes it and marks its limits. Section 7 draws the positive conclusion.

# 2. Calibrationism

## 2.1 Definitions

Consider a sequence of yes-or-no questions, one per day: will it rain on day $t$? Write $x_t \in \{0,1\}$ for the answer. A *credence-forming process* $\rho$ issues on each day a credence $f_t \in [0,1]$ that $x_t = 1$. The process may take as input the history $h_t$ of earlier outcomes and of its own earlier credences, a label $z_t$ representing the agent's evidence on day $t$ (a barometer reading, a testimony), and the output of a private randomizing device. Call a process *history-based* if these are its only inputs and its rule for turning them into credences is fixed in advance. Every inductive learner is history-based in this sense: a Bayesian with a prior, a frequentist who adopts observed frequencies, and the procedures below.

Fix a finite grid of credence values. For each value $p$, consider the days up to $T$ on which the process assigned $p$, and let $q_T(p)$ be the proportion of those days on which it rained. The process is *calibrated* on a run if, for each $p$ used with positive long-run frequency, $q_T(p)$ tends to $p$; it is *$\varepsilon$-calibrated* if the frequency-weighted average of the squared gaps $(q_T(p)-p)^2$ is eventually below $\varepsilon$. Calibration can be *conditioned* on a family $\mathcal{R}$ of reference classes: the condition must then hold separately within each class, for instance on the days with barometer reading high, or on the days whose history matches a given pattern. *Smooth* calibration replaces the sharp bins by averages over nearby credence values.

## 2.2 The schema

Let $X$ be a calibration standard: sharp or smooth, limiting or finite with a tolerance, conditioned on some family $\mathcal{R}$. Let $W$ be a function assigning to each world $w$ and process $\rho$ a set $W(w,\rho)$ of worlds relevant to assessing $\rho$ at $w$: the actual world alone, the actual world and nearby worlds, the normal worlds, or all worlds. Calibrationist reliabilism, in its sufficiency half, is the schema:

> **CR-S(X, W).** If $\rho$ is $X$-calibrated throughout $W(w,\rho)$, then $\rho$ is reliable at $w$, and the credences it produces at $w$ are justified.

The schema is graded in obvious ways (degrees of calibration, degrees of justification). I target the sufficiency half only. Whether calibration is necessary for justification is a separate question, on which there is reason for doubt from another direction (Dorst 2023 argues that rational agents can be expected to be miscalibrated).

## 2.3 How calibrationism answered its critics

Two objections shaped the view. The first, reported in the SEP entry, is Goldman's (1986) case of an agent seventy per cent of whose opinions are true, who achieves perfect calibration by giving every proposition credence 0.7. Such calibration is achieved without good reasons and should not confer justification. The reply, again as the SEP entry reports it, is to look not only at the actual world but across a range of nearby worlds: if it is "just a matter of chance" that seventy per cent of the propositions are true, the process will be miscalibrated in nearby worlds, and the calibration approach avoids the counterintuitive verdict. Dunn's own statement is that "we should not merely look at the actual cases that these processes have performed on. We must also look at how they perform in nearby worlds" (Dunn 2015).

The second objection, attributed by the SEP entry to Tang (2016), is that a process can be well calibrated while insensitive to relevant evidence. The natural reply is to condition calibration on the agent's evidence. A process that ignores the barometer will be miscalibrated on the days when the barometer reads high, in worlds where the barometer is informative.

The strengthened view, conditioned on evidence and assessed across worlds, seems to answer both objections. Both answers rest on the same assumption: that a process which reaches calibration without being suitably connected to the world reaches it by luck, so that its calibration is fragile under variation of the world. The theorem shows that this assumption is false.

## 2.4 Two desiderata

Calibration was meant to meet two desiderata. (D1) It does not penalize a process for producing middling credences in a domain where the truth is not more predictable. (D2) It makes reliability a matter of the process's track record, actual and counterfactual: how its credences fare against the outcomes. The argument below respects (D1) and rejects (D2).

# 3. Calibration without information

## 3.1 The theorem

**Theorem 1** (Foster and Vohra 1998). For every $\varepsilon > 0$ there is a randomized history-based forecasting procedure, with credences on a finite grid, which is $\varepsilon$-calibrated with probability one against every sequence of outcomes.

The assumptions matter. (i) The procedure randomizes, and the guarantee holds with probability one relative to its own randomization. Randomization is essential: for every deterministic procedure there is a sequence on which it is badly miscalibrated (Oakes 1985; Dawid 1985), roughly the sequence on which it rains exactly when the procedure's credence is below one half. (ii) "Every sequence" includes sequences produced by an adversary who sees the past outcomes and the procedure's past credences, provided the adversary does not see the current randomization. It includes, a fortiori, every chance process. (iii) The procedure uses nothing but the past outcomes and its own past credences: it has no information about how the data are generated. (iv) The result is asymptotic, but finite versions exist: known procedures keep the average calibration error after $T$ days of order $T^{-1/3}$, uniformly over all sequences, and no procedure can guarantee much better than roughly $T^{-0.46}$ (Qiao and Valiant 2021; Dagan et al. 2025).

Three strengthenings matter for calibrationism.

*Deterministic procedures.* If calibration is measured smoothly, randomization is unnecessary. Foster and Hart (2018) show that "smooth calibration can be guaranteed by deterministic procedures", even when the procedure's forecasts are announced in advance, by a procedure that is stationary, has finite recall and uses a finite grid.

*Many reference classes.* Sandroni, Smorodinsky and Vohra (2003) show that for any countable collection of subsequences (checking rules, which may depend on the history and on labels such as the evidence) there is a procedure calibrated on every one of them, for every infinite sequence of outcomes. Foster, Rakhlin, Sridharan and Tewari (2011) extend this to uncountable families of bounded combinatorial complexity. The machine-learning notion of multicalibration (Hébert-Johnson et al. 2018), calibration on every subpopulation identifiable by a given class of computations, has online versions valid against adversarially chosen data (Gupta et al. 2022).

*Uninformedness.* In every case the procedure uses the labels only as labels. It needs no information about how the evidence bears on the outcomes, or about anything else in the world.

## 3.2 The anti-tracking lemma

**Lemma.** Let $\rho$ be any history-based process. Then there is a chance world $w_\rho$, in which the chance of rain on each day depends only on the history of outcomes (and labels), such that on every day $t$
$$\mathbb{E}\,|f_t - c_t| \;\geq\; 0.4,$$
where $c_t$ is the chance of rain on day $t$ given the history and the expectation is over the process's randomization.

The proof (Appendix) is a diagonal construction: let the chance of rain be 0.9 on days when the process's expected credence, given the history, is below one half, and 0.1 on the other days. Two features of $w_\rho$ matter. First, it is an ordinary, exogenous chance world: the chance of rain is a fixed function of the past weather. Nothing in it reacts to the process; the process simply happens to be anti-aligned with it. Second, the chances in $w_\rho$ are extreme (0.9 and 0.1), not middling.

The contrast that matters is this. A deterministic learner, such as a Bayesian with any prior, has an anti-tracking world too, and in that world it is miscalibrated: on the days it gives credence below one half it rains ninety per cent of the time. So calibration correctly condemns it there. The procedures of Section 3.1 are calibrated in their anti-tracking worlds as well, because they are calibrated in every world. In $w_\rho$ a chance-matching process, one whose credence on each day equals the chance, is also calibrated, with probability one (Appendix). Calibration ties them.

# 4. The argument

The argument needs one normative premise about reliability:

> **(R)** If, in world $w$, a process's credence on every occasion is, in expectation, at least 0.4 away from the chance of its content given everything the process takes as input, then the process is not reliable in $w$.

The argument then runs:

1. For every history-based process $\rho$ there is a world $w_\rho$ in which the antecedent of (R) holds for $\rho$. (Lemma; the chance given the history equals the chance given the history and the process's private randomization, which is independent of the weather.)
2. So for every history-based process there is a world in which it is not reliable. (1, R)
3. Call a standard $S$ *world-independently securable* if some history-based process meets $S$, in every world, with probability at least $1-\varepsilon$ for some $\varepsilon < 1$.
4. If $S$ is sufficient for reliability, then any process that meets $S$ in a world is reliable in that world.
5. Suppose $S$ is world-independently securable, witnessed by $\rho$, and sufficient for reliability. In $w_\rho$, $\rho$ meets $S$ with positive probability; so, by 4, there are runs of $w_\rho$ on which $\rho$ is reliable in $w_\rho$. But by 2, $\rho$ is not reliable in $w_\rho$; and whether $\rho$ is reliable in $w_\rho$ in the sense of (R) does not depend on the run. Contradiction.
6. So no world-independently securable standard is sufficient for reliability. (3 to 5)
7. For every calibration standard $X$ of Section 2 and every range function $W$, the standard "$X$-calibrated throughout $W(w,\rho)$" is world-independently securable. (Theorem 1 and its strengthenings: the witnessing procedure is $X$-calibrated in every world, so in every world of every $W(w,\rho)$.)
8. Reliabilism counts a credence as justified in virtue of the reliability of the process producing it; so a standard insufficient for reliability is insufficient, on reliabilist terms, for justification.
9. So for every $X$ and $W$, CR-S$(X, W)$ is false. (6, 7, 8)

Step 7 explains why the range of worlds drops out. The nearby-worlds reply to Goldman worked because the uniform 0.7 process is calibrated only by luck. The Foster-Vohra procedure is calibrated in every world, so no choice of relevant worlds can make it score worse than any other process. Indeed, if a process $Q$ is calibrated throughout some set of worlds, so is the procedure. Modal robustness, the feature added to defeat Goldman's case, can only favour it.

Step 7 also explains why conditioning drops out. Conditioning on the agent's evidence was the answer to Tang. But the procedures that are calibrated on every countable family of reference classes use the classes only as labels, and they are history-based, so the Lemma applies to them.

## 4.1 Defending (R)

(R) is the argument's only normative premise, and it is weak. It does not say that reliability is closeness to chance. It says only that a process uniformly and substantially far from the chances, on every occasion, is not reliable. Three considerations support it in the case at hand.

First, accuracy. On every day in $w_\rho$, the chance-matching credence is strictly better than $\rho$'s in chance-expected accuracy under every strictly proper scoring rule, since strict propriety means exactly that the credence equal to the chance uniquely minimizes chance-expected inaccuracy. With the Brier score, the chance-expected inaccuracy of a credence $f$ when the chance is $c$ is $(f-c)^2 + c(1-c)$. The chance-matcher's is $0.09$ every day. $\rho$'s is at least $0.4^2 + 0.09 = 0.25$, which is what a process that ignored everything and always said one half would get.

Second, anti-alignment. In $w_\rho$, $\rho$'s expected credence is below one half exactly on the days when rain is ninety per cent likely. Its credences point the wrong way, systematically.

Third, (D1) is idle. The calibrationist's reason for preferring calibration to accuracy was that accuracy measures penalize middling credences in domains where the truth is unpredictable. In $w_\rho$ the chances are 0.9 and 0.1. The chance-matcher is not producing middling credences, and the comparison with $\rho$ is not a comparison of a cautious process with a reckless one in a hard domain.

A reader who rejects objective chance can run the argument in a deterministic world: let it rain on day $t$ exactly when $\rho$'s expected credence is below one half. Then $\rho$'s expected credence is on the wrong side of one half every day, its expected Brier inaccuracy is at least 0.25 every day, and a process whose credence equals the truth value scores zero.

## 4.2 Two illustrations

The argument is schematic. Two cases show what it means for familiar versions.

*Barometer.* An agent has a barometer that in her world predicts rain well, and forms her credences by the Foster-Vohra procedure applied to the rain record alone, ignoring the barometer. Unconditional calibrationism, with any range of worlds, says her credences are justified. Conditional calibrationism rejects this verdict, but only because it conditions on the barometer reading.

*Testimony in a rare cell.* Conditional calibrationism faces a subtler version. Suppose the agent's evidence is fine-grained, so that most evidence states occur rarely, and on some day she learns from a reliable expert that the chance of rain is 0.9. A procedure calibrated on every evidence cell learns what this evidence indicates only by accumulating outcomes in that cell, and before it has done so its credence is fixed by its bookkeeping, not by what the expert said. It is calibrated in every world nonetheless, because calibration constrains only long-run frequencies within each cell.

Neither case is needed for the argument. Both show that the verdict CR-S delivers about the witnessing procedures is the verdict it delivers about agents.

# 5. Objections and replies

## 5.1 Is the witness really unreliable in $w_\rho$?

*First version: reliability for credence just is calibration.* The calibrationist may deny (R): to be reliable is to be calibrated, and closeness to chance is a different virtue. The cost is that reliability ceases to be a relation of fit between process and environment. A property that one process has in every environment, by design, carries no information about how that process is related to any environment. Reliabilism was attractive because it explained justification by truth-conduciveness in the subject's environment. On the definitional reply, a process can be maximally "reliable" in an environment in which it is dominated in expected accuracy, under every proper score, every day. Pettigrew (2021) presses a Connection Problem against existing reliabilist accounts of justified credence: it is unclear how justification so understood connects to anything of epistemic value. The definitional reply makes this problem acute, since the property it identifies with reliability is compatible with every degree of chance-expected inaccuracy above the minimum.

*Second version: the witness is an inductive learner, and its credences are justified.* The Foster-Vohra procedure learns from past outcomes, and past outcomes are evidence. In worlds where days are independent, calibration within each bin forces its credences toward the observed frequencies, as a sensible learner's would. I grant all this. The argument does not need the claim that the procedure's credences are never justified. It needs only the claim that CR-S is wrong to count the procedure as reliable in $w_\rho$, where it is anti-aligned with the chances on every day.

There is also a reason to doubt that the procedure models evidential responsiveness at all. Dawid (1982) proved that a coherent Bayesian assigns probability one to being well calibrated, and Dawid pointed out (as reported by Oakes 1985) that a coherent forecaster cannot adjust future predictions to correct past miscalibration without sacrificing coherence. The Foster-Vohra procedure does just this. Its credence on a given day is chosen to keep its calibration record in balance whatever happens. That is why it is calibrated in every world, and also why its calibration is no evidence of fit with any world.

## 5.2 Randomized credence is not credence

One may doubt that a credence fixed partly by an internal coin is a credence, or that reliabilists need to evaluate such processes. Two replies. First, the deterministic smooth-calibration procedure of Foster and Hart (2018) needs no coin, has finite recall and is stationary; it is no more exotic than any rule of thumb. The argument goes through for smooth calibration with that procedure as witness. Second, reliabilism is a theory of what makes any possible process justification-conferring. Whether human cognition implements such a procedure is irrelevant to whether calibration is sufficient for reliability. Nor does the generality problem help: the procedure is a single uniform rule, and any natural process type containing it inherits its calibration in every world.

## 5.3 $w_\rho$ is remote

It may be objected that $w_\rho$ is not among the worlds relevant to assessing the process. There are three replies. First, $w_\rho$ is an ordinary chance world, in which the chance of rain is a function of the past weather; there is nothing deviant about its laws. Second, the range of worlds drops out of the argument (step 7). The witness is calibrated in every world, so it meets the calibrationist standard in $w_\rho$ whatever range of worlds that standard consults; and $w_\rho$ could be actual. Third, on the account of nearby worlds that secondary reports attribute to Dunn, the relevant counterfactual circumstances hold fixed the regularities the process tracks and vary only accidental features. A process that tracks no regularity at all receives no restriction from this criterion.

## 5.4 Robustness as a virtue: the demon world

A calibrationist might welcome the result. An agent in a demon world, whose experiences are systematically misleading, seems justified. $w_\rho$ is a demon world for credence, and calibrationism says the witness's credences there are justified. Is this not the right verdict? The internalist intuition about the demon world credits the victim's good response to her evidence. Calibrationism delivers its verdict about $w_\rho$ whether or not the process responds to evidence at all. It counts the barometer-ignoring agent as justified for the same reason. So it reaches the demon-world verdict for the wrong reason and overgenerates it. A reliabilist who wants the demon-world verdict has other routes, such as assessing reliability in normal worlds, that do not have this consequence.

## 5.5 Comparative calibrationism

A more promising response replaces absolute standards with comparative ones: a process is reliable only if it is calibrated and no available process does better in accuracy. This handles the barometer case. But it faces a dilemma about the benchmark. If the benchmark processes are history-based and uninformed, then in an anti-tracking world for all of them (the Lemma applies to any history-based procedure that aggregates them), the best of them is certified while it is anti-aligned with the chances. If the benchmark is a process that matches the chances, the view is no longer a calibrationist or track-record view: it measures reliability against the chances, which is the view of Section 7.

# 6. Beyond calibration

The argument used one property of calibration: it is world-independently securable. Step 7 can be replaced by results from the literature on testing experts, where a test is a rule that passes or fails a forecaster on the basis of the forecasts and the data. A test *controls type I error* if a forecaster who forecasts by the true probabilities passes it with high probability, whatever those probabilities are. The question in that literature is whether a test that controls type I error can be passed by a forecaster who knows nothing about the true probabilities.

**Theorem 2.**
(a) (Sandroni 2003.) Over a finite horizon, every test that controls type I error can be passed by an uninformed forecaster with high probability, whatever the data. The forecaster draws a theory at random at the outset, by a distribution obtained from Fan's minimax theorem, and forecasts by its conditional probabilities.
(b) (Olszewski and Sandroni 2008.) The same holds over an infinite horizon for future-independent tests: tests whose verdict at a given time does not depend on the forecaster's predictions for later times. In their words, "tests which cannot be ignorantly passed must rely on predictions about data not yet observed, and such tests cannot be run if forecasters report only the probability of the next period's events on the basis of the actually observed data."
(c) (Shmaya 2008.) If a test is Borel and a forecaster who knows the truth always passes it, then an ignorant forecaster can pass it.

The forecasters in Theorem 2 are history-based in the sense of Section 2.1: once the random theory is drawn, each day's credence is a function of the history. So the Lemma applies to them. A record of credences actually formed, on the history actually observed, is exactly what Olszewski and Sandroni describe as forecasts that "report only the probability of the next period's events on the basis of the actually observed data". So the argument of Section 4 applies with Theorem 2 in place of step 7:

> **(G)** No outcome-based standard on credences actually formed which is finite-horizon, or future-independent, or Borel, and which a chance-matching process meets with high probability in every world, is sufficient for reliability.

This is the precise form of the generalization. It is narrower than the claim that no outcome-based test separates informed from uninformed forecasters, which is false. The literature identifies four ways out, and each shows something.

*Future-dependent tests with unbounded data.* Dekel and Feinberg (2006) and Olszewski and Sandroni (2009b) construct tests that control type I error and cannot be manipulated. These tests evaluate a forecaster's whole theory, including its predictions about data not yet observed, and they reach their verdicts in the limit; their separating power is measured topologically, by category. They do not deliver a graded measure of how far a process's credences are from the truth, and no finite stretch of a process's record bears on their verdict. They are not a candidate measure of degrees of reliability.

*Computational bounds.* Fortnow and Vohra (2009) give an efficient test which, under standard hardness assumptions, an efficient uninformed forecaster cannot pass. Calibration itself, however, is passed by efficient procedures, so this does not help calibrationism; and the test is specially designed to make passing it computationally hard, not a measure of reliability.

*Restricted domains.* If the possible data-generating processes are restricted to a learnable class, non-manipulable tests exist (Al-Najjar, Sandroni, Smorodinsky and Weinstein 2010); Olszewski and Sandroni (2009a) note that such restrictions help "only to a limited extent". A restriction to a class of possible chance processes is a restriction by chances, not by outcomes.

*Comparison.* Al-Najjar and Weinstein (2008) show that when two experts are compared, one of whom knows the true distribution, a simple test identifies the informed one with any desired precision in finite time. The impossibility in the single-expert case, they note, arises because nature's mixed strategies over distributions reduce to pure ones; the presence of an expert who knows the realized distribution removes this reduction. Comparison against a benchmark that knows the chances separates where no absolute test can. The benchmark, however, is defined by the chances, not by the record.

Each escape route brings in something that is not in the track record: predictions about unobserved data, a restriction on the possible chance processes, or a benchmark that knows the chances.

# 7. What reliability for credence must be

The lesson is that reliability for credence is a relation between credences and chances, not a property of records. Tang's indicator view, as the SEP reports it, says that a credence $C(p)$ is justified only if it is based on a ground $g$ such that the objective probability of $p$ given $g$ approximates $C(p)$. The argument gives a reason to think that a view of this form is forced: any condition that excludes the witnesses of Sections 3 and 6 must appeal to something beyond the record, and the chance given the ground is the natural candidate. It also suggests how to grade the view. Let the unreliability of a process in a world be the chance-expected excess inaccuracy of its credences over the chances given its grounds. With the Brier score this excess is $(f - c_g)^2$, where $c_g$ is the chance of the content given the ground. The measure meets (D1): a process whose credences match middling chances has zero excess. It connects reliability to accuracy, since it is the part of expected inaccuracy that the process could have avoided given what it used. And it makes the basing condition precise: the ground is what the process actually takes as input. For the Foster-Vohra procedure the ground is the history and its coin, and the chance given these is the world's chance, not the procedure's output.

The view also explains why calibration seemed right. A chance-matching process is calibrated with probability one (Dawid's theorem has this form for a forecaster whose probabilities are the true ones). So calibration is a symptom of reliability. The theorems show that the converse fails as badly as it could: the symptom can be produced without the condition, in every world.

*The Humean worry.* If chances supervene on the total pattern of outcomes, as Humeans hold, is the chance-given-grounds condition outcome-based after all, and so subject to (G)? No. First, Humean chances on a day depend on the whole pattern, including the future, so the condition is not future-independent. Second, the testing theorems quantify over fixed data-generating measures known to a "true expert"; Humean chances are not given in advance of the pattern. Third, the anti-tracking construction applies to Humeans too, provided the process's credences are part of the pattern: the regularity "rain is likely exactly when the process's expected credence is low" is then part of the world's pattern, and a best system that records it assigns the chances 0.9 and 0.1. I offer the third point as plausible, not proved, since it depends on details of best-system analyses.

The view has a cost that should be stated plainly. Reliability so understood is not verifiable from any finite record, and (G) shows that no outcome-based surrogate of the relevant kinds can certify it. This is the externalist's situation in any case. What the theorems add is that the calibrationist's hope of an externalism whose standard is fixed by outcomes alone cannot be realized.

# 8. Conclusion

Calibrationism was defended against its first critics by requiring calibration to be modally robust and conditioned on evidence. Both defences assumed that uninformed calibration is lucky and therefore fragile. The Foster-Vohra theorem and its strengthenings show that uninformed calibration can be secured in every world, for every countable family of reference classes. Since every history-based process has a world in which it is anti-aligned with the chances, no standard that can be secured in every world is sufficient for reliability. This covers every version of calibrationist reliabilism and, through the expert-testing theorems, every finite-horizon, future-independent or Borel outcome-based standard. What reliability for credence must include instead is a relation to the chances given the process's grounds. Calibration is what such reliability looks like from the outside; it is not what it is.

# Appendix

**A1.** In Theorem 1, $\varepsilon$-calibration on a run means: $\limsup_{T\to\infty} \sum_{p} \frac{N_T(p)}{T}\,(q_T(p) - p)^2 \leq \varepsilon$, where $N_T(p)$ is the number of days up to $T$ with credence $p$. The adversary may choose $x_t$ as any function of $x_1,\dots,x_{t-1}$ and $f_1,\dots,f_{t-1}$.

**A2. Proof of the Lemma.** Let $\rho$ be history-based. Write $\bar f_t(h) = \mathbb{E}[f_t \mid h]$ for its expected credence on day $t$ given outcome history $h$ (and labels), the expectation taken over its randomization, including past coins. $\bar f_t$ is a function of $h$ alone. Define the chance world $w_\rho$ by: the chance of $x_t = 1$ given history $h$ is $0.9$ if $\bar f_t(h) < 1/2$ and $0.1$ otherwise. This defines a probability measure on outcome sequences (by the Ionescu-Tulcea theorem), in which outcomes depend only on past outcomes, so the process's randomization is independent of the weather and the chance given $h$ and the process's coins is $c_t$. If $\bar f_t(h) < 1/2$ then $\mathbb{E}|f_t - 0.9| \geq 0.9 - \bar f_t(h) > 0.4$; otherwise $\mathbb{E}|f_t - 0.1| \geq \bar f_t(h) - 0.1 \geq 0.4$, using $\mathbb{E}|Y| \geq |\mathbb{E}Y|$. $\square$

**A3. The chance-matcher is calibrated in $w_\rho$.** Its credences take the values 0.9 and 0.1. On the days it assigns 0.9 (a set selected by the history, hence predictable), the differences $x_t - 0.9$ form a bounded martingale difference sequence, so by the strong law for martingales the proportion of rain on those days tends to 0.9 almost surely whenever there are infinitely many such days; likewise for 0.1. The same argument applies within any countable family of predictable reference classes.

**A4. A deterministic process is miscalibrated in its anti-tracking world.** If $\rho$ is deterministic, $\bar f_t = f_t$. On the days with $f_t < 1/2$ the frequency of rain tends almost surely to 0.9 (A3), so every bin below one half used infinitely often has a gap greater than 0.4; similarly above one half. Hence the calibration score is eventually at least $0.16$ times the proportion of days falling in such bins, which is one.

# References

Al-Najjar, N. I., Sandroni, A., Smorodinsky, R. and Weinstein, J. (2010). Testing theories with learnable and predictive representations. *Journal of Economic Theory* 145(6): 2203-2217.

Al-Najjar, N. I. and Weinstein, J. (2008). Comparative testing of experts. *Econometrica* 76(3): 541-559.

Dagan, Y., Daskalakis, C., Fishelson, M., Golowich, N., Kleinberg, R. and Okoroafor, P. (2025). Breaking the $T^{2/3}$ barrier for sequential calibration. *Proceedings of the 57th Annual ACM Symposium on Theory of Computing*, 2007-2018.

Dawid, A. P. (1982). The well-calibrated Bayesian. *Journal of the American Statistical Association* 77: 605-613.

Dawid, A. P. (1985). Calibration-based empirical probability. *Annals of Statistics* 13(4): 1251-1274.

Dekel, E. and Feinberg, Y. (2006). Non-Bayesian testing of a stochastic prediction. *Review of Economic Studies* 73(4): 893-906.

Dorst, K. (2023). Being rational and being wrong. *Philosophers' Imprint* 23.

Dunn, J. (2015). Reliability for degrees of belief. *Philosophical Studies* 172(7): 1929-1952.

Fortnow, L. and Vohra, R. V. (2009). The complexity of forecast testing. *Econometrica* 77(1): 93-105.

Foster, D. P. and Hart, S. (2018). Smooth calibration, leaky forecasts, finite recall, and Nash dynamics. *Games and Economic Behavior* 109: 271-293.

Foster, D. P., Rakhlin, A., Sridharan, K. and Tewari, A. (2011). Complexity-based approach to calibration with checking rules. *Proceedings of the 24th Annual Conference on Learning Theory*, PMLR 19: 293-314.

Foster, D. P. and Vohra, R. V. (1998). Asymptotic calibration. *Biometrika* 85(2): 379-390.

Goldman, A. (1986). *Epistemology and Cognition*. Cambridge, MA: Harvard University Press.

Goldman, A. and Beddor, B. Reliabilist epistemology. In E. N. Zalta (ed.), *The Stanford Encyclopedia of Philosophy*.

Gupta, V., Jung, C., Noarov, G., Pai, M. M. and Roth, A. (2022). Online multivalid learning: means, moments, and prediction intervals. *13th Innovations in Theoretical Computer Science Conference (ITCS 2022)*, LIPIcs 215: 82:1-82:24.

Hébert-Johnson, U., Kim, M. P., Reingold, O. and Rothblum, G. N. (2018). Multicalibration: calibration for the (computationally-identifiable) masses. *Proceedings of the 35th International Conference on Machine Learning*, PMLR 80: 1939-1948.

Oakes, D. (1985). Self-calibrating priors do not exist. *Journal of the American Statistical Association* 80: 339.

Olszewski, W. and Sandroni, A. (2008). Manipulability of future-independent tests. *Econometrica* 76(6): 1437-1466.

Olszewski, W. and Sandroni, A. (2009a). Strategic manipulation of empirical tests. *Mathematics of Operations Research* 34(1): 57-70.

Olszewski, W. and Sandroni, A. (2009b). A nonmanipulable test. *Annals of Statistics* 37(2): 1013-1039.

Pettigrew, R. (2021). What is justified credence? *Episteme* 18(1): 16-30.

Qiao, M. and Valiant, G. (2021). Stronger calibration lower bounds via sidestepping. *Proceedings of the 53rd Annual ACM Symposium on Theory of Computing*.

Sandroni, A. (2003). The reproducible properties of correct forecasts. *International Journal of Game Theory* 32: 151-159.

Sandroni, A., Smorodinsky, R. and Vohra, R. V. (2003). Calibration with many checking rules. *Mathematics of Operations Research* 28(1): 141-153.

Shmaya, E. (2008). Many inspections are manipulable. *Theoretical Economics* 3: 367-382.

Tang, W. H. (2016). Reliability theories of justified credence. *Mind* 125(497): 63-94.
