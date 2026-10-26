# Round 3, Referee C (fresh agent; technical)

Record (condensed by the author agent; all technical points retained). Verdict: MINOR REVISION (at the major end). Scores: originality 6, correctness 7, importance 6. Core sound: Lemma, Section 4, realized-Brier argument, A1, A2, A3 arithmetic.

## Errors (change claims)
1. 5.1 misreports A3: bound is 1/(2(0.9 - sqrt eps)), about 5/6 at eps about 0.09, tending to 5/9 only as eps -> 0.
2. (G)(iii): Shmaya's manipulator passes with probability >= 1 - eps, not one. Restate CR-S and (G) with explicit pass-probability thresholds; (i)/(ii): witness passes w.p. >= 1 - eta - delta.
3. A4 does not establish insufficiency in 5.1 and 5.4 because R is silent. Fix: for any uniformly computable countable family, construct a computable b (block by block, effective derandomization of the Fubini argument) such that every rule sees average b -> 1/2 a.s.; then R applies. Non-uniformly-computable family (all computable rules) is 5.2.
4. "Finitely many rational coins per day" excludes Theorem 2(b)/(c) witnesses. Generalize randomization; propensity as E[f_t | h] (Jensen unchanged). For (a) finite horizon, a finitely supported rational mixture suffices.

## Imprecisions
- "Same computational resources" true for computability, false for complexity (exponential averaging over coin paths).
- Computability of w_rho and of {f-bar < 1/2} needs rational-valued credences, or approximate threshold (0.39, 0.152).
- Flagship: Foster-Hart unconditional; for finitely many predictable forecast-independent classes, run separate copies on atoms of the generated partition (tolerance scaled); countable: no citable deterministic smooth result known (maybe Foster-Hart 2021 JPE "Forecast hedging and calibration").
- Rate-sensitive: sqrt T rate needs finitely many chance values; use a binned test sum over bins |sum (x_t - f_t)| <= C sqrt(T log(1/eta)); then Sandroni applies.
- Individuation and 4.1: "infinitely many horizons" (reverse Fatou), not "in the limit".
- Finite-horizon securability "with probability >= 1 - delta" for randomized witnesses.
- Dawid 1985: agreement pointwise |p_t - q_t| -> 0 (for computable forecasts, rules that see current forecast); intro "computable processes, a.s.".
- Cite Lehrer 2001 for zero tolerance with countable rules.
- 5.2 second point: computable witnesses exist for uniformly computable countable families too (summable weights, doubling); restrict or add.
- 6.5: standard result: Vovk aggregating algorithm / exponential weights with prior weights: regret O(log 1/pi_i) against each expert on every sequence (Cesa-Bianchi-Lugosi 2006); Foster-Hart 2023 multi-calibeating; calibeating = beating a forecaster's Brier by its calibration component.
- 2.1: state coin-weather conditional independence defining admissible worlds.
- Verify Oakes vs Dawid attribution; OS 2008 and 2009a quotations; Hu-Shmaya scope.
- 5.4: "certifies no deterministic process" not "counts none as justified".
- Deterministic witness realized gap liminf >= 0.16 a.s.; randomized P(avg >= 0.08) >= 0.11 per T.
