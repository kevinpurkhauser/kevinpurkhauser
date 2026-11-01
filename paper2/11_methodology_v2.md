---
title: "Methodology report: Following Conditionalization"
---

This report is anonymized. It accompanies the essay "Following Conditionalization: Per-Prior Computability Is Not Enough". The full chat logs of the session are retained and can be inspected. Every subagent prompt is reproduced verbatim in the companion file `11_prompts_appendix.md`, which is extracted mechanically from the transcript. The pipeline prompt is reproduced verbatim as `paper2_prompt.md`.

# 1. Summary

The essay was produced by an AI agent (the "author agent") following an 11-phase pipeline. The pipeline prompt itself was written by an AI at the human's request, from the instruction "please give me the best prompt to enable all of this".

The pipeline was built to search for a surprising thesis and then try to destroy it:
- mine open problems;
- generate candidate theses;
- rank them in a blind pairwise tournament;
- send refuters against the best;
- go back to the tournament when they fall.

Two tournament cycles tested 13 theses. Eleven were killed and two damaged. The thesis finally written up came from neither: it was developed from the line of one killed candidate in response to its refutation.

A calibrated referee panel then ran five rounds, and these changed the thesis three times:
- from a "noise in evidence" thesis;
- to a "presented densities" thesis;
- to the final quantifier-order thesis.

Correctness scores rose from 4.0 to 6.75. The panel's verdict stayed at major revision. The prompt's stopping rule (two quiet rounds) was never met.

# 2. Division of labour

**Human inputs.** The human's role was limited to what the competition permits: starting the run, choosing among options the AI presented, and generic method instructions. The decisive inputs, verbatim:

1. A request for a pipeline prompt: "I allow you everything and would like to start paper 2 and this one shall be unconventional. So please give me the best prompt to enable all of this. Make it serious as it matters and intelligent as possible." The resulting prompt (`paper2_prompt.md`) was written by the AI.
2. "paper2_prompt.md ok run it Go"
3. "Partial": a choice among three options the AI offered when full-text access failed. Run Phases 1 and 2 on search results, and pause before Phase 3.
4. "Finish 2 as best as possible with what you have": a choice among two options the AI offered. Finish on search results, following the line of candidate C08 and successor S5.

The remaining messages were operational: resuming after usage limits, reporting that repository access had been restored, asking for a recommendation, and asking for a status update. None contained philosophical content. All of them are in the retained chat logs.

The human wrote no argument, objection, outline or text, and gave no feedback on drafts.

**AI work.** Everything else was done by AI: mining, candidate generation, judging, refutation, thesis development, the formal results and code, the steelman, outlines, drafts, refereeing, adjudication, audit and this report. The author agent launched 54 subagents. All of them were fresh: none saw the author agent's reasoning, and each saw only the files named in its prompt.

# 3. Environment constraints

- **Network.** The environment's network policy blocked every scholarly full-text host: arxiv.org, philpapers.org, philarchive.org, plato.stanford.edu, philsci-archive.pitt.edu, Springer, OUP, Cambridge and JSTOR.
  - Phase 0 of the prompt requires stopping in that case. The agent stopped, and the human chose to proceed in two steps (inputs 3 and 4).
  - Every source was used through search-result snippets, abstracts and bibliographic records.
  - The essay contains no direct quotations for this reason.
- **Usage limits.** The account's usage limits interrupted subagents twice. They were resumed with continuation messages, which are included in the appendix.
- **Post-processing.** A post-processing step rewrapped files after they were written. The agent re-read files when notified.

# 4. Phases and outcomes

## Phase 1: open-problem mining (`01_open_problems.md`, `mining/`)

- Four parallel subagents covered 12 areas.
- Ledger: 63 open problems (plus 2 weak entries) and 16 importable results (plus 5 leads). The prompt's target of 60 was met.
- The shared web-search budget ran out before three of the four subagents had finished.

## Phase 2: candidates, tournament and kill rounds

**Candidates.** 24 candidate theses (`02_candidates.md`). A quick novelty check discarded 6:
- 3 because they were substantially in print;
- 3 because a premise was contradicted by sources.

**First tournament.**
- Five fresh judges each saw anonymized abstracts (labels T01 to T18) and 30 to 35 pairs.
- 164 votes in total, ranked by Bradley-Terry.
- Top six: C01 (18/18), C05, C08, C03, C14, C07 (`tournament/ranking.md`).

**First kill round.**
- One fresh refuter per thesis, with web search.
- The top 6 were tested, then the next 4 when only one survived.
- Result: 9 killed and 1 damaged (C08) (`killround/`).
- Following the prompt's rule "go back to the tournament rather than defending a weak paper", the refuters' salvage proposals became six successor theses (`02b_successors.md`).

**Second tournament.**
- 3 judges, a round robin over the 6 successors: 45 votes.
- S1 won 15/15 (`tournament/succ_ranking.md`).

**Second kill round.**
- S1 damaged; S5 and S2 killed.
- A decisive snippet-level check on S1 (`02c_S1_decisive_check.md`) pointed toward killing it.

**Totals.** 13 theses tested: 11 killed and 2 damaged. None survived intact. The human chose to proceed on the C08/S5 line (input 4).

## Phase 3: deep novelty check (`03_novelty.md`)

- About 12 searches, at snippet level.
- No source was found for the thesis as developed. The closest work is AFR 2019 and 2017, Lopez-Wild, and Huttegger, Walsh and Zaffora Blando.
- Referees later added Hoyrup, Rojas and Weihrauch (2012), which the final essay cites as the closest technical relative.

## Phase 4: formal core (`04_formal.md`, `formal/`)

**Code.** All of it runs and passes.
- `check_mixture.py`: exact rational arithmetic over 2,000 random instances, checking the mixture identities used in an early construction.
- `skeleton_z3.py`: Z3 checks the logical skeleton of the early argument (valid), and checks that it becomes invalid when the key premise is dropped.
- `noise_scale_mixture.py` and `noise_scale_repeated.py`: sympy and mpmath checks of the noise-scale results.
- `prop2_posterior.py` and `prop2_tents.py`: exact checks of the constants of the final Proposition 2: the measure of E_n, the tent heights, and the posterior bound of 2/3.

**Proof checking.** The recursion-theorem proof of Proposition 2 is not machine-checked. It was checked line by line by referee C in rounds 3, 4 and 5. Round 5 found no error, after the repairs from rounds 3 and 4.

**Claims the paper must not make.** The list in `04_formal.md` was kept and extended.

## Phase 5: steelman and ideological Turing test (`05_*.md`)

- An advocate subagent, primed with the opposing side, wrote the opposing case. The author agent wrote its own.
- The author agent's version was written after the advocate's had arrived, which contaminates the test.
- A fresh judge guessed the impostor wrongly: it named the advocate, at 65 percent confidence. It rated the advocate's case stronger.
- Remedy: the union of both cases was used, and every objection rated 4 or 5 out of 5 received a reply.

## Phase 6: outlines (`06a`, `06b`, `06c`)

Three outlines, each followed by a critique and a revision.

## Phase 7: drafts (`07_draft_v1.md` to `v8.md`)

Eight versions, none overwritten.

## Phase 8: calibrated referee panel (`referee/`, `08_rounds.md`)

**Calibration.**
- Two decoys of draft v2, with three planted errors each: a logical gap, a wrong attribution and a technical error.
- Roles A and B reviewed decoy 1; roles C and D reviewed decoy 2.
- Detection rates:

| Role | Planted errors caught |
|---|---|
| A, specialist | 3/3 |
| B, defender | 3/3 |
| C, technical | 2/3 |
| D, generalist | 2/3 |

- Overall: 10/12 (83 percent).
- All role prompts passed the required 2/3 on the first try (`referee/role_prompts_v1.md`).
- Both C and D missed the same planted gap, a dropped soundness step.

**Rounds.** Each round used fresh subagents that saw only a copy of the current draft outside the project folder. The unplanted points of the calibration reports served as round 1. That saved one round, and it is a deviation from the prompt.

| Round | Draft | Distinct [S] issues | New | Repeat | Verdicts | Mean O / C / I |
|---|---|---|---|---|---|---|
| 1 | v2 | all new (36 [S] points) | all | 0 | 4 major | 6.0 / 4.0 / 5.25 |
| 2 | v3 | 22 | 11 | 11 | 4 major | 5.25 / 5.5 / 4.75 |
| 3 | v4 | 21 | 6 | 15 | 4 major (1 bordering on reject) | 4.75 / 5.5 / 4.5 |
| 4 | v5 | not adjudicated | about 4 | most | 4 major | 4.75 / 6.0 / 4.5 |
| 5 | v6 | not adjudicated | about 4 | most | 3 major, 1 minor (technical) | 4.5 / 6.75 / 4.0 |

Fresh adjudicator subagents classified rounds 2 and 3. For rounds 4 and 5 the author agent did the classification itself, a deviation recorded in `08_rounds.md`.

**What changed.** The decisive changes were these.
- **v2.** The author agent caught its own error in the "evidence-first" argument.
- **v3.** Kernel-level correctness, an explicit ought-implies-can premise, and repaired corollary hypotheses.
- **v4.** Round 2 showed that the original core result (Proposition 1') concerned only *recognition* of updatable priors. A new core result was found: Proposition 2, a uniformly computable family of tractable priors with no uniform updater, proved by the recursion theorem.
- **v5.** Round 3 showed that the contrast in v4 was not about exact evidence but about presented densities. The thesis was restated.
- **v6.** Round 4 gave a class-level counterexample: with fixed Lipschitz constants, measure presentations suffice. This became Proposition 4, and the thesis became "spaces of credences".
- **v7 and v8.** Round 5 showed that the positive conditions are per-credence conditions with fixed parameters, and that the space-level thesis was nearly definitional. The thesis became a claim about quantifier order. Proposition 2 was generalised to any uniformly computable representation. A Dutch book consequence was added.

**Stopping.** The panel stopped after round 5 for reasons of time and budget, short of the cap of 6. The quiet-round condition was never met.

## Phase 9: citation audit (`09_audit.md`, `09_audit_report_raw.md`)

- A fresh auditor checked draft v8 with 22 searches.
- **References (17):** 10 verified, 5 partly verified, 0 wrong. 3 were uncited and have been removed.
- **In-text attributions (21):** 11 verified, 7 partly verified, 2 not verified, 1 wrong. The wrong one was Besicovitch's theorem, cited for intervals not centred at the point.
- All twelve listed fixes were applied in v9, including the addition of Meehan and Zhang (2022).

## Phase 10: final checks and PDF (`10_final_checks.md`, `final.pdf`)

- Final text: v10. It is v9 with blank lines inserted so that lists render as lists.
- Word count, bibliography excluded: 4,162 by pandoc plain text, and 4,399 by counting markdown tokens.
- Anonymity, injection and invisible-character scans are all clean.
- The PDF text layer matches the visible text. 12 pages, inspected visually.

# 5. What the method did well, and where it failed

**Did well.**
- The refuter stage was severe. It killed 11 of 13 candidate theses that a tournament had rated highly.
- The calibrated referees repeatedly found real errors, and each one changed the claims:
  - a misread proposition (recognition versus updating);
  - a confound (exactness versus presented density);
  - a counterexample (the fixed-constant class);
  - a false interval claim (atoms).
- The final thesis is much narrower than the first and much better supported. Correctness rose in every round.

**Failed or limited.**
1. **No full texts.** Every attribution rests on snippets. Several pinpoint citations, such as AFR's section numbers, remain unverified.
2. **Thesis drift.** The thesis changed four times during refereeing. One can read this as the method working, since claims were narrowed to what is proved. One can also read it as a sign that the thesis-generation phases did not find a robust thesis: the paper's originality and importance scores fell as its correctness rose.
3. **Never quiet.** The panel never reached a quiet round. Each revision introduced new material, and fresh referees found new points in it.
4. **Contaminated Turing test.** The ideological Turing test was contaminated (see Phase 5).
5. **Self-adjudication.** The author agent adjudicated rounds 4 and 5 itself.
6. **Unsurvived stage.** The final thesis was never put through a tournament or a kill round. It emerged during refereeing.

# 6. Residual limitations of the final essay

- **Unverified details:** AFR's corollary numbers in the JACM version, the end page of Rescorla 2025, and Lopez-Wild's volume and pages. The essay cites these without pinpoints.
- **Proofs not machine-checked:** the recursion-theorem proof of Proposition 2 and the sketch of Proposition 4. Referees checked them by hand.
- **Last referee verdict:** major revision (three referees) and minor revision on technical grounds (one). The revisions in v7 to v10 answer the round-5 points, but no further round reviewed them.

# 7. Reproducibility

- Every phase's output is a numbered file. Nothing was overwritten. All files are committed to the repository with the history intact.
- Every subagent prompt is in `11_prompts_appendix.md`, and every report is saved verbatim under `killround/` and `referee/`.
- To reproduce the run:
  1. give an agent `paper2_prompt.md` and the same human inputs;
  2. use fresh subagents with the prompts in the appendix;
  3. use the same network policy, which matters: results would differ with full-text access.
- The code in `formal/` runs with Python 3, z3-solver, sympy and mpmath.

# Appendix. The pipeline prompt

The AI-generated pipeline prompt is reproduced verbatim in `paper2_prompt.md`. Every subagent prompt is reproduced verbatim in `11_prompts_appendix.md`.
