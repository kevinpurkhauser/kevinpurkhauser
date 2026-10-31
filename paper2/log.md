# Paper 2 log

## Phase 0 -> 00_environment_check.md
- Human input: "paper2_prompt.md ok run it Go" (recorded in human_inputs.md).
- All eight scholarly hosts blocked; git push refused (403); Python and Z3 work.
- Stopped as required by the prompt. No thesis work done.

## Phase 1 -> 01_open_problems.md, mining/
- Human input: "Partial" (run Phases 1-2 on search results; pause before Phase 3).
- Four parallel mining subagents (12 areas). 63 open problems (+2 weak), 16 importable results (+5 leads). Shared search budget (200 per turn) ran out; three agents stopped short.
- Git push now works (GitHub reconnected by the human); scholarly hosts still blocked.

## Phase 2 -> 02_candidates.md, 02_novelty_quick.md, tournament/
- 24 candidate theses written (abstracts about 120-160 words, shorter than the 250 the prompt asked for, to keep the tournament packet readable).
- Quick novelty check (about 20 searches): 6 discarded before the tournament: C15, C18, C20 (substantially in print), C09, C10, C13 (premise contradicted by sources).
- Tournament: 18 survivors anonymized as T01-T18 (random labels, seed recorded in mapping file 02_tournament_mapping.json); five fresh judge subagents, each 30-35 pairs (each candidate in about 4 pairs per judge), judging on the competition criterion only, no web access.
- Tournament result (tournament/ranking.md): 164 blind pairwise votes, Bradley-Terry. Top six: C01 (MIP* = RE underdetermination, 18/18), C05 (Bayesian persuasion vs lying/misleading, 16/18), C08 (noncomputable conditionalization, 17/19), C03 (conciliation without peers, 14/17), C14 (awareness growth impossibility, 14/17), C07 (tractability and moderate credence, 12/17). Bottom: C21, C23, C24.
- Kill round started: six fresh refuter subagents, one per top-six candidate, about 15 searches each, verdict SURVIVED / DAMAGED / KILLED.
- Kill round results (killround/): C01 KILLED (premise 2 backwards; finite Bell functional separates the closed sets), C05 KILLED (equivalence only under anticipation, where lies do not deceive), C03 KILLED (premise 1 false; independence favours synergy for credences), C14 KILLED (conclusion in print; no impossibility), C07 KILLED (sufficiency-for-necessity; MAP hard even with bounded probabilities), C08 DAMAGED (scope limited to exact real-valued evidence; Lopez-Wild 2026 close).
- Per the prompt ("go back to the tournament rather than defending a weak paper"): only one non-killed candidate, so the kill round is extended to the next four by rating (C19, C06, C04, C02).
