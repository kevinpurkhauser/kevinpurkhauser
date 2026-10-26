# Running log

Project: AI Philosophy Competition, Paper 1, Stage 2.
Thesis (from Stage 1, AI-generated): calibrationist reliabilism about justified credence fails, because by the Foster-Vohra theorem a process with no information about the world can be calibrated in every possible world; generalization via the expert-testing literature.

Human inputs so far: choice of area, choice of thesis among Stage 1 candidates, the step-by-step instructions (generic methods) in the task prompt. Everything below is done by the AI agent unless stated otherwise.

## Step 0 (setup)
- Created folder `calibration-essay/` in an empty repository, with `sources/` for downloaded or excerpted source material.

## Step 1 (novelty check) -> 01_novelty.md
- Tried to download full texts (Dunn 2015, Tang 2016, Pettigrew 2021, SEP, Belot 2013, expert-testing papers). All scholarly hosts are blocked by the environment's network policy (proxy 403 / DNS failure). Only a web-search tool returning summaries and verbatim snippets works. Recorded the snippets in sources/search_notes_step1.md.
- Ran about 25 searches: target papers, philosophy papers citing Foster-Vohra or Sandroni, calibrationism variants, multicalibration in philosophy.
- Result: no paper found that makes the argument. Precursors identified: Goldman's 70% case (via SEP), Tang's evidence-insensitivity objection, Seidenfeld 1985, Belot 2013. Room left: the theorem defeats the nearby-worlds/process reply; dominance point; generalization with exact limits; positive upshot.
- Change to thesis flagged: the Stage 1 generalization ("no purely outcome-based test separates informed from uninformed") is too strong; non-manipulable tests exist. To be restricted in Step 2.
- Policy adopted: attribute to authors only what the snippets show; mark secondary-report claims.

## Step 2 (mathematics) -> 02_math.md
- About 20 searches to check each theorem against abstracts or verbatim snippets (notes in sources/search_notes_step2.md). Corrected a reference error carried in the task prompt's background: Sandroni (2003) is IJGT 32: 151-159.
- Stated: Foster-Vohra with exact assumptions (randomization, finite grid, adaptive adversary blind to current coin, asymptotic; finite-sample rates T^{-1/3} average, lower bound T^{-0.47} approx); deterministic smooth calibration (Foster-Hart 2018) as a reply to the randomization objection; checking rules (SSV 2003, FRST 2011), multicalibration; manipulability (Sandroni 2003, Olszewski-Sandroni 2008 and 2009 MOR, Shmaya 2008); limits (Dekel-Feinberg, Olszewski-Sandroni 2009 AoS, Fortnow-Vohra, Hu-Shmaya, Al-Najjar et al. 2010, Al-Najjar-Weinstein comparative testing, Feinberg-Stewart).
- Added own elementary results: O1 anti-tracking world (any history-based process is, in some chance world, at least 0.4 from chance every day in expectation), O2 combination with calibration, O3 generalization to any manipulable standard, O4 dominance.
- Thesis restated: the generalization holds for future-independent / finite-horizon / Borel standards that the truth passes; not for all outcome-based tests.

## Step 3 (steelman) -> 03_steelman.md
- Three further searches (Brier decomposition, calibeating, expert-advice regret bounds; the last only partly verified, so its use is conditional).
- Stated 17 variants: actual-world, Dunn's nearby worlds, hypothetical frequency, normal worlds, conditional on evidence, reference classes, multicalibration, inclusive calibrationism (Wilcox), finite horizon, calibration plus sharpness, comparative, non-manipulable-test reliabilism, computationally bounded, chance given grounds (Tang type), plus three objections (the process is a learner; new evil demon; psychological reality).
- Survivors: chance given grounds (to be accommodated as positive view; Humean collapse worry to be answered); non-manipulable test reliabilism (not refuted; set aside with reasons, stated as a limit); comparative (collapses into chance view or fails in anti-tracking worlds).
- Change: the core argument now rests on (i) dominance (no restriction of worlds can rank the uninformed process lower) and (ii) the anti-tracking world (calibration ties a process that is always 0.4 from chance with the chance-matcher), not on the claim that the uninformed process's credences are always unjustified.

## Step 4 (outlines) -> 04a, 04b, 04c
- Round 1: target structure. Critique: maths split in two places, conditional calibration duplicated, CR not formulated, core argument rested on barometer case which the strongest view escapes; missing objections.
- Round 2: core argument recast as a schematic argument about "world-independently securable" standards plus the anti-tracking lemma; barometer demoted to illustration. Critique: availability clause in premise R unnecessary; probabilistic step sloppy; chance-sceptic version missing; length.
- Round 3: final outline with word budget; premise R freed of availability; deterministic variant; objections merged.

## Step 5 (draft) -> 05_draft_v1.md
- Full draft, about 5,270 words excluding references (appendix included). Core argument as nine numbered steps in section 4. Two small post-draft fixes (removed unverified claim that Tang did not give a certain reason; corrected lower-bound exponent wording).

## Step 6, round 1 (in progress)
- Launched three fresh referee subagents that saw only a copy of the draft (in the scratchpad, not the project folder).
- Referee A (formal epistemologist): major revision; originality 7, correctness 5, importance 7. Record in referee/r1_A_formal_epistemologist.md. Main points: expectation over past coins undermines the lemma for randomized witnesses (decisive A/B coin example); step 7 overgeneralized (process-relative classes, computable families, cross-world calibration); premise R not as neutral as claimed; chance-free variant reinstates the truth-closeness standard; measure in section 7 not novel.
- Referees B and C were interrupted by an API rate limit and resumed after the user asked to try again.
- Referee B (Dunn-sympathetic reliabilist): major revision; 8/5/7. Record in referee/r1_B_reliabilist.md. Main: process-relative (propensity) reference classes not securable; computable calibration for computable processes; reliability "in w" vs "at w"; R not weak, realized-Brier version; individuation of outset randomizers; false inheritance claim; false dilemma in comparative section; Al-Najjar-Weinstein mischaracterized.
- Referee C (technical): major revision; 7/5/7. Record in referee/r1_C_technical.md. Main: step 7 false as stated; OS 2008 needs finite-time rejection; Shmaya needs probability-one passing; OS 2009b mischaracterized; Al-Najjar-Weinstein caveat; rates outdated / wrong metric; lemma overstated; definitions; A4 liminf.
- Revision plan: 06a_revision_plan_round1.md. Searches for added literature: sources/search_notes_step6.md (plus Blackwell-Dubins, Fudenberg-Levine, Kakade-Foster verified at abstract/bibliographic level).

## Step 6, revision after round 1 -> 05_draft_v2.md (5,511 words excl. references)
- New thesis: a dilemma. Horn 1: securable standards (fixed, bounded families; positive tolerance or fixed-bandwidth smooth) are insufficient. Horn 2: unsecurable ones (propensity-binned, computable calibration, cross-world) are insufficient (new hidden-sequence lemma, A4) or owe their power to agreement with chances (Dawid 1985 asymptotic agreement; chance-weighted cross-world frequencies).
- Lemma now in two forms: expected distance (broad individuation) and run-level average distance with probability at least 2/7 (narrow individuation); world exogenous. R restated in average form with a same-input matcher; defended via D1-relative-to-inputs, merging (Blackwell-Dubins), realized Brier gap.
- CR-S restated with reflexivity at a normal actual world (answers in-w vs at-w).
- Theorem 2 hypotheses corrected; (G) restated; OS 2009b, Al-Najjar-Weinstein, Dekel-Feinberg, Al-Najjar et al. corrected; rates corrected; Humean third point dropped; inheritance claim replaced by a discussion of typing; comparative section rewritten (conditional on aggregator existence); positive measure credited to standard decomposition and Pettigrew 2016.
- Unresolvable: primary texts of Dunn and Tang cannot be read in this environment; essay keeps only verified quotations.

## Step 6, round 2 -> referee/r2_*.md
- Fresh referees (saw only v2). A: major, 7/5/8. B: major, 7/5/7. C: major, 7/6/7 ("none overturns the main thesis"). All concede the central negative point.
- New substantive objections: A3 false under exogenous reading (coin-at-outset counterexample, found independently by all three); quantifier gap for coin-fixed processes over rich ranges (A, C); R's same-input clause vacuous (B); normal-worlds misformulation and demon comparison wrong (B); Hu-Shmaya 2013 computability exception (C); order-of-explanation / Dawidian vindication reply (A, B); exhaustiveness gaps (A, B); missing literature (Putnam 1963, Seidenfeld 1985, Gneiting et al., Clifton).
- Verified at abstract/bibliographic level: Clifton (statistical reliabilism), Putnam 1963 pages, Hu-Shmaya pages. Murphy 1973 and DeGroot-Fienberg 1983 bibliographic details NOT verified, so not cited.
- Revision plan: 06b_revision_plan_round2.md.

## Revision after round 2 -> 05_draft_v3.md (5,493 words)
- History fixed (outcomes, labels, index); unconditional propensity; Lemma restated with Brier excess (a) and corrected 2/7 derivation (b).
- Calibration in a world = almost-sure calibration; main argument under broad individuation; R restated day-by-day with Brier excess and a resources clause (chance computable from inputs relative to the process's rule), which removes the vacuity and makes 5.1/5.2 consistent. Flagship: deterministic Foster-Hart case.
- A3 corrected (probability of propensity-binned calibration bounded below one). 5.2 adds an order-of-explanation argument and the reductive-Dawidian concession. 5.3 adds pooled cross-world calibration. New 5.4: refinement, deterministic sharp over rich ranges, rate-sensitive standards.
- Target restated: ranges containing @; normal-worlds calibrationism treated as a limit (6.4). Demon discussion corrected. Repertoire relativization added (6.1). Hu-Shmaya added; (G) proviso. Natural persistence-world case added. Humean section restated (finite-time rejection; Shmaya's probability-one hypothesis).
