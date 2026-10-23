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
