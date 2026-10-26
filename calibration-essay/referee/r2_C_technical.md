# Round 2, Referee C (fresh agent; technical)

Record of the report (condensed by the author agent; all technical points retained).

Verdict: MAJOR REVISION (technical). Scores: originality 7, correctness 6 (8-9 after fixes), importance 7. "None overturns the main thesis."

Correct: Theorem 1 and qualifications, Lemma (a), 2/7 bound statement, reverse Fatou, intersection bound, Brier decomposition, A2, A4, Theorem 2 attributions, Foster-Hart, SSV, FRST, multicalibration, Blackwell-Dubins (with prior containing w_rho).

## Errors (must fix)
1. A3 false: f-bar averages over past coins; phi_t - f-bar_t not a martingale difference. Counterexample: one initial coin, constant 0.1 or 0.9; f-bar = 1/2; class empty; complement calibrated w.p. 1/2. Corrected: P(propensity-binned eps-calibration in w_rho) <= 5/9 + O(sqrt eps) (< 5/7), and 0 when daily randomization is independent of past coins given h. Re-derive 5.2 from this or from Dawid + Lemma (b).
2. Step 5 quantifier swap (as referee A): for coin-fixed sigma_u, uncountable W or W containing its Oakes world fails. Use broad individuation with R in expected form and Lemma (a), or countable ranges; Foster-Hart unaffected.
3. Lemma (b) proof inequality wrong as displayed (gives 2/9); use E D <= 0.9P + 0.2(1 - P).
4. History definition conflicts with exogeneity: h = (outcomes, labels, index); phi recomputes past credences from u.
5. Hu and Shmaya 2013 (Expressible inspections, TE 8) omitted: computable test accepting true experts w.h.p., not manipulable by computable strategies; (G) fails under computability restriction; add to section 7 and 5.2.
6. Finite-horizon cases need finite-horizon version of R (Lemma (b) at T = T_0).

## Imprecisions
- Rates are l1 not squared score. Exact calibration with refining grids attainable (positive tolerance only for fixed grids).
- Dawid 1985: averaged zero-tolerance criterion; agreement in Dawid's asymptotic sense; "on almost every run"; qualify intro.
- Computability of w_rho needs finitely many rational coins per day.
- Blackwell-Dubins: prior must contain w_rho; no history-based learner merges with all anti-tracking worlds; Solomonoff mixture merges with all computable but is not computable; soften "without antecedent knowledge".
- 6.5: aggregator result is a theorem (calibeating; calibration w.r.t. expert level sets); quantitative claim: average |f_k - c| >~ 0.04 per member, not 0.2.
- 5.3: distinguish history-conditioned from pooled cross-world calibration (pooled is weaker, not chance-matching; fails per-day in w_rho by the n_p/h_p algebra).
- Checking-rule normalization; cite Lehrer 2001.
- Diagonal citation: Dawid's 1985 JASA comment ("The impossibility of inductive inference", JASA 80: 340-341).
- Verify quotations (OS 2008, OS 2009a, Dunn) and CH claim for Dekel-Feinberg.
- Humean: Shmaya's inspections are future-independent in OS sense; what Shmaya drops is finite-time rejection; real obstacle is probability-one passing under every measure, plausibly false for best-system chances.
- Add proof that calibrated forecasters in w_rho concentrate near 1/2: with n_p frequency of forecast p and h_p share of high-chance days, calibration gives p ~ 0.1 + 0.8 h_p; propensity constraints give sum n_p h_p (h_p - 1/2) <= 0 and sum n_p (1 - h_p)(h_p - 1/2) >= 0; subtracting, sum n_p (h_p - 1/2)^2 <= 0 up to O(sqrt eps).
- Tolerance eps < 0.16; 0.1 and 0.9 on grid. Theorem 2 without labels: flag extension. Run-relativity explicit.
- Fortnow-Vohra: expert submits an efficiently computable theory (predictions about unobserved data).
- 6.2: Dawid's correction point is in his 1985 JASA comment and Oakes's reply; i.i.d. vs independent non-identical.
