# 02. Statement sheet: the mathematics, exactly

Verification key. [V-abs]: statement checked against the abstract or a verbatim snippet of the source (see sources/search_notes_step2.md). [V-sec]: checked only against a reliable secondary statement (survey, later paper citing it). [Own]: an elementary observation proved here, to be presented in the paper as the author's own and proved in the appendix. Nothing below goes beyond what the cited result gives. Where my recollection of a detail could not be checked, the detail is omitted or flagged.

## 0. Setting and notation

- Outcomes x_1, x_2, ... in {0,1} (x_t = 1: "it rains on day t"). History h_t = (x_1, ..., x_{t-1}), possibly enriched with covariates z_1, ..., z_t (the agent's other evidence on day t) and with the forecaster's past forecasts.
- A forecasting process (credence-forming process) F issues on each day t a forecast f_t in [0,1] (the credence that x_t = 1) as a function of h_t (and z_t) and, if randomized, of a private randomizing device r_t, independent of everything else.
- "Nature" or "the world" fixes outcomes. Three standard models of the world:
  (W1) a fixed individual sequence x (a deterministic world);
  (W2) a probability measure P on {0,1}^N (a chance world: P(x_t = 1 | h_t) is the chance on day t);
  (W3) an adaptive adversary: x_t may be any function (or randomized function) of h_t and of the forecaster's past forecasts f_1, ..., f_{t-1}, but not of the current randomization r_t.
  W3 includes W1 and W2. All "every world" claims below are claims over W3 unless stated.
- Calibration score with finite forecast grid G_k = {0, 1/k, ..., 1}: for each grid value p, let N_T(p) = number of days t <= T with f_t = p, and q_T(p) = fraction of those days with x_t = 1. Then
  C_T = sum over p of (N_T(p)/T) (q_T(p) - p)^2.
  F is epsilon-calibrated on a run if limsup_T C_T <= epsilon. (Foster and Vohra use a squared version restricted to a finite set of forecast values; an l1 version, sum over p of N_T(p)|q_T(p) - p| / T, is used in the rates literature. Asymptotic claims below hold for both; rate claims are for the l1 version as stated.)
- Checking rule: a function c_t that, given h_t (and past forecasts, covariates), selects or weights day t; calibration with respect to c means the calibration condition holds on the subsequence of days selected by c.

## 1. Background impossibility (deterministic forecasters)

**T1 (Oakes 1985; Dawid 1985).** No deterministic forecasting system is calibrated on every sequence. [V-sec: Oakes, "Self-calibrating priors do not exist", JASA 80: 339-342, as described in later papers; the diagonal sequence x_t = 1 iff f_t < 1/2 makes any deterministic forecaster miscalibrated with error of at least about 1/2 in the relevant bins.]

**T2 (Dawid 1982).** A coherent Bayesian forecaster assigns prior probability 1 to being well calibrated in the long run (calibration in the limit, along subsequences selected in a predictable way). [V-abs: "a coherent Bayesian expects to be well calibrated".] This is calibration by the forecaster's own lights, not in every world.

**T3 (Belot 2013).** For any forecasting system, the set of data sequences on which it is calibrated is topologically small (meagre); failure is typical. [V-abs.] Building on Schervish (1985), every forecasting system is uncalibrated for uncountably many sequences. These concern deterministic systems (Belot notes that randomization "in itself" makes no difference in his setting; context not fully verified, not to be relied on).

## 2. The Foster-Vohra theorem

**T4 (Foster and Vohra 1998, Biometrika 85: 379-390, "Asymptotic Calibration").** For every epsilon > 0 there is a randomized forecasting rule, with forecasts in a finite grid, that is epsilon-calibrated almost surely (with respect to its own randomization) against every sequence, including sequences chosen by an adaptive adversary who sees the past forecasts but not the current randomization. [V-abs/V-sec: "Foster and Vohra exhibit a randomized forecasting algorithm that almost surely will be calibrated on all sequences"; Theorem 1 snippet: "A randomized forecast using the mu_t defined by equation (2) with k approx 1/epsilon^2 is an epsilon-calibrated forecast" (exponent possibly an OCR artefact; not to be quoted).]

Assumptions to state in the paper:
1. **Randomization is essential** for (ordinary) calibration against every sequence (T1). The adversary must not see the current coin flip; if nature can condition on r_t, the guarantee fails.
2. **Finite grid**: forecasts take values in G_k; the epsilon depends on the grid. Standard constructions refine the grid over time to drive the error to 0 (the paper's title; I will state the epsilon form as the theorem and say "by refining the grid, the error can be made to vanish in the limit" only as a well-known corollary [V-sec: later papers state "calibration is almost surely guaranteed"]).
3. **Information used**: the forecaster uses only the past outcomes of the very sequence it forecasts (and its own past forecasts and coins). It uses no knowledge of the data-generating process. [V-sec: "asymptotic calibration can be achieved without any knowledge of what the state will be in each round".]
4. **Asymptotic vs finite sample**: the original is asymptotic. Finite-sample versions: the best known algorithms have expected l1 calibration error O(T^{2/3}) after T days (so the average error decays like T^{-1/3}) [V-sec: Qiao and Valiant 2021 cite O(T^{2/3}) as the long-standing upper bound], improved to O(T^{2/3 - c}) for a small constant c by Dagan, Daskalakis, Fishelson, Golowich, Kleinberg and Okoroafor (STOC 2025) [V-sec]; lower bound Omega(T^{0.528}) (Qiao and Valiant, STOC 2021) [V-abs], later Omega(T^{0.54389}) against an oblivious adversary [V-sec, reported in Dagan et al.]. Upshot for the paper: after T days, an uninformed process can guarantee average calibration error of order T^{-1/3} uniformly over all worlds; no process can guarantee much better than T^{-0.46}.

Other proofs (Hart's, Fudenberg and Levine 1999, Foster 1999 via Blackwell approachability) [V-abs: Foster's 1999 abstract lists them]. Not needed in the paper beyond one citation.

**T5 (deterministic weak/smooth calibration).** If calibration is measured with continuous (smoothed) test functions instead of sharp bins, deterministic procedures suffice: Kakade and Foster (COLT 2004; JCSS 2008) introduced weak calibration achieved deterministically [V-sec]; Foster and Hart (GEB 109 (2018): 271-293): "While regular calibration can be guaranteed only by randomized forecasting procedures, we show that smooth calibration can be guaranteed by deterministic procedures"; smooth calibration can be guaranteed even when forecasts are "leaked" (announced in advance), "while regular calibration cannot"; the procedure has finite recall, is stationary, forecasts on a finite grid. [V-abs.]

Use in the paper: blocks the objection that the counterexample depends on randomized credence formation. The smooth version is a slightly weaker notion than sharp-bin calibration; the paper must say so.

## 3. Calibration with checking rules, multicalibration

**T6 (Sandroni, Smorodinsky and Vohra 2003, Math. Oper. Res. 28: 141-153).** Given any countable partition of [0,1] and any countable collection of checking rules (subsequences), there is a forecasting scheme such that on every subsequence the long-run average forecast matches the long-run frequency of outcomes (cell by cell), for all infinite data strings. [V-abs: abstract wording "given any countable partition of [0,1] and any countable collection of subsequences ... for all infinite data strings".] Randomized.

**T7 (Foster, Rakhlin, Sridharan and Tewari 2011, COLT, PMLR 19: 293-314).** For possibly uncountable families of checking rules, calibration against the whole family is achievable when the family has bounded complexity, measured by a sequential cover (covering finite VC and Littlestone dimension cases); they prove bounds on the value of the associated game, certifying existence of a calibrated forecaster. [V-abs/V-sec: Semantic Scholar summary; NeurIPS 2024 description.] Do not claim specific rates.

**T8 (multicalibration).** Hebert-Johnson, Kim, Reingold and Rothblum (ICML 2018): predictors calibrated simultaneously on every subpopulation identifiable by a given class of computations [V-abs]; batch, statistical setting. Online, adversarial versions (calibration on every group in a family, against every sequence) are given by Gupta, Jung, Noarov, Pai and Roth (ITCS 2022, "Online multivalid learning", arXiv 2101.01739) [title and topic V-sec; details not verified; cite only for existence of online multicalibration in the adversarial setting].

Key structural fact for the paper: in all of T4, T6, T7, T8 the forecaster requires no knowledge of the data-generating process. The covariates (group membership, reference class) are used as labels only.

## 4. Manipulability of tests (the generalization)

A **test** maps (a theory or a sequence of forecasts, data) to {pass, fail}. It **controls type I error** (at level epsilon) if, whatever P is true, the forecaster who forecasts by P passes with P-probability at least 1 - epsilon. A test is **manipulable** if there is a randomized forecaster (a random generator of theories) that, for every world, passes with probability close to 1 - epsilon. "Uninformed" = the manipulator's strategy is fixed in advance and does not depend on which P is true.

**T9 (Lehrer 2001, Econometrica 69: 1333-1347, "Any inspection is manipulable").** Title claim; within his class of inspections. [Bibliographic V; abstract not read: cite only as the title result, or drop.]

**T10 (Sandroni 2003, IJGT 32: 151-159).** For finite horizon: any test that passes the truth with probability at least 1 - epsilon can be passed by an uninformed forecaster with probability at least 1 - epsilon, for every sequence of outcomes. Proof via Fan's minimax theorem; the uninformed forecaster randomizes over theories. [V-abs: "Based on Fan's (1953) Minimax theorem, I show that it is possible to produce forecasts that will not be rejected on any sequence of outcomes"; V-sec: Pomatto 2021: "any test that operates in finite time and is free of Type I errors can be passed by a strategic but uninformed forecaster".] Exact constants not verified; the paper will say "with probability at least 1 - epsilon - delta, for any delta > 0" only if needed, otherwise "with high probability".

**T11 (Olszewski and Sandroni 2009, Math. Oper. Res. 34: 57-70).** With no restriction on the permissible theories, strategic experts cannot be discredited over any given finite number of periods, whatever the test (provided it does not reject the true process). Ways around: unbounded data, or restricting the domain of theories, and then "only to a limited extent". [V-abs.]

**T12 (Olszewski and Sandroni 2008, Econometrica 76: 1437-1466, "Manipulability of Future-Independent Tests").** A test is future-independent if whether it rejects a theory at a given period does not depend on the theory's predictions for later periods. Future-independent tests that control type I error can be ignorantly passed. In the authors' words: "tests which cannot be ignorantly passed must rely on predictions about data not yet observed, and such tests cannot be run if forecasters report only the probability of the next period's events on the basis of the actually observed data". [V-abs.] This is the crucial result for credence-forming processes: a record of credences actually formed on the actual history is exactly "probability of next period's events on the basis of actually observed data".

**T13 (Shmaya 2008, Theoretical Economics 3: 367-382, "Many inspections are manipulable").** If the test function is Borel and a true expert always passes, then it is manipulable by an ignorant expert. Proof via Martin's determinacy of Blackwell games. Under the axiom of choice there are non-Borel test functions that are not manipulable. [V-abs.]

## 5. Limits: where tests can separate

**L1 (non-manipulable tests with infinite data and future-dependence).** Dekel and Feinberg (2006, RES 73: 893-906): a test of a stochastic prediction such that false experts fail on all but a small (category I) set of true distributions [V-sec, wording from Feinberg-Stewart's description]. Olszewski and Sandroni (2009, Annals of Statistics 37: 1013-1039): the "global category test", which controls type I error (does not reject the truth, with probability one) and is non-manipulable; unlike Dekel-Feinberg it does not assume the continuum hypothesis [V-abs: arXiv 0904.0338]. Both use predictions about the future (future-dependent) and infinite data; the smallness notion is topological (category), not measure-theoretic. Do not claim more precise content.

**L2 (computational limits).** Fortnow and Vohra (2009, Econometrica 77: 93-105): a linear-time test and a distribution of nature such that any forecaster who fools the test without knowledge of the future must solve computationally hard problems (PSPACE-hard in the technical report); so Sandroni's theorem fails if tester and forecaster are both efficiently computable, under standard hardness assumptions [V-abs + V-sec]. Hu and Shmaya (2013, TE 8): a computable test not manipulable by computable strategies that accepts true experts with high probability [V-sec].
Note: calibration itself (T4) is achieved by efficient algorithms, so L2 does not protect calibration; it only shows that specially designed tests can expose bounded manipulators.

**L3 (restricted domains).** Al-Najjar, Sandroni, Smorodinsky and Weinstein (2010, JET 145: 2203-2217): with theories restricted to a learnable and predictive class, a test (the expert names a date by which she will make a sharp forecast) accepts the informed expert and cannot be manipulated; no such test exists for the unrestricted class [V-abs]. T11 likewise: restriction helps "only to a limited extent".

**L4 (comparative testing).** Al-Najjar and Weinstein (2008, Econometrica 76: 541-559): with two experts, one of whom knows the true distribution, a simple test identifies the informed one within any precision in finite time, without counterfactual predictions; the single-expert impossibility rests on nature's mixed strategies being reducible to pure ones, and the presence of an informed expert eliminates this [V-abs]. Feinberg and Stewart (2008, Econometrica 76: 561-582), "Testing multiple forecasters" [V-sec]: cross-calibration test; false experts fail on all but a category I set when a true expert is present. Note: Olszewski and Sandroni have a paper "Manipulability of comparative tests" (PNAS 2009) [title V], which shows limits on comparative testing; not read, so not to be characterized beyond its title.

Use in the paper: L4 is the mathematical root of the positive proposal. Comparison against an informed benchmark separates where absolute tests cannot. But the comparison needs the benchmark (the chance or a process that tracks it), which is not itself an outcome-based standard.

## 6. Own elementary results [Own]

**O1 (Anti-tracking world).** Let F be any forecasting process whose forecast on day t depends only on the history h_t (outcomes, covariates, its own past forecasts) and its private randomization. Fix a < 1/2 < b in [0,1]. Define a chance world P_F by: P_F(x_t = 1 | h_t) = b if E[f_t | h_t] < 1/2, and = a otherwise, where E is over F's randomization given h_t. Then for every t, E|f_t - ch_t| >= min(1/2 - a, b - 1/2), where ch_t is the day-t chance.
Proof. If E[f_t | h_t] < 1/2, ch_t = b and E|f_t - b| >= b - E[f_t|h_t] > b - 1/2. Otherwise ch_t = a and E|f_t - a| >= E[f_t|h_t] - a >= 1/2 - a. (Jensen.) The world is well defined because E[f_t | h_t] is a function of h_t, and h_t is generated by P_F and F jointly; P_F is an adaptive world of type W3 (it depends on F's conditional forecast distribution, not on r_t). If one wants a world of type W2 independent of F's realized past forecasts, note E[f_t | h_t] can be taken conditional on outcome history only, by integrating over F's past randomization: then P_F is an ordinary measure on outcome sequences.
With a = 0.1, b = 0.9: F is always at least 0.4 from the chance in expectation, and F's expected Brier score per day is at least 0.4^2 + 0.09 = 0.25, while the chance-matching forecaster's is 0.09.

**O2 (Combination).** If F is the Foster-Vohra forecaster (T4), or a checking-rule calibrated forecaster (T6), or a smooth-calibrated deterministic forecaster (T5), then F is calibrated in the corresponding sense in P_F (as in every world). The chance-matching forecaster (forecast = ch_t) is also calibrated in P_F, almost surely, by the strong law for martingale differences (for any countable family of predictable checking rules whose selected subsequences are infinite). Hence calibration, in any of these senses, does not distinguish F from the chance-matcher in P_F, though F is uniformly further from chance by at least 0.4.
Caveat for the paper: the strong-law claim for the chance-matcher is standard (Dawid 1982 type; a martingale argument), but state it with the condition "on subsequences selected by predictable rules that select infinitely many days".

**O3 (Generalization).** Let S be any outcome-based standard to which T10, T12 or T13 applies (finite horizon and type I error control; future-independent with type I control; Borel and always passed by the truth). Then there is an uninformed process F_S that meets S with high probability in every world, and (by O1, since F_S forecasts by a randomly chosen theory conditional on the observed history, so its forecast depends only on h_t and its randomization) there is a world in which F_S is always at least 0.4 from chance in expectation, while the chance-matcher meets S there with probability at least 1 - epsilon.
Caveat: O1 requires F_S's day-t forecast to be a function of h_t and private randomness. In Sandroni-type constructions the forecaster draws a theory at time 0 and then forecasts by the theory's conditional probabilities, so this holds. State it this way.

**O4 (Dominance).** For any set W of worlds and any process Q: if Q is calibrated (in sense X) throughout W, then so is the Foster-Vohra-type process for X (almost surely in each world of W). Trivial from "every world". Consequence: no restriction of the range of worlds (actual, nearby, normal, all) can make the uninformed process score lower on calibration than any other process.

## 7. Claims the paper must NOT make
- That an uninformed process is calibrated "in every possible world" without qualification. Correct form: against every sequence (every world of type W3), almost surely with respect to its own randomization (T4), or deterministically for smooth calibration (T5).
- That no outcome-based test whatsoever separates informed from uninformed. Correct form: tests that are finite-horizon (T10), or future-independent (T12), or Borel (T13), and that the truth passes, are manipulable; non-manipulable tests exist but require future-dependence and unbounded data, use topological smallness (L1), or exploit computational bounds (L2), restricted domains (L3), or comparison with an informed expert (L4).
- That randomization is needed for the main counterexample (T5 removes this for smooth calibration).
- Specific constants or exponents beyond those stated in section 2.
- That Dawid 1982 says Bayesians are calibrated: it says they expect to be (prior probability one).
