# AI Philosophy Competition: Paper 2 (full pipeline, one session)

You are producing one essay for the AI Philosophy Competition, from topic
selection to submission-ready PDF, plus a methodology report. The work
must be primarily AI generated: the ideas, arguments, structure and prose
are yours. This prompt is an argument-agnostic scaffold. It contains no
thesis and no argument, and you must not treat anything in it as one.

Judging criterion, verbatim: "to what extent do the ideas and arguments in
this essay make a valuable contribution to philosophical knowledge?"
Quality and originality only; style is not graded. Judges are
professional philosophers. Judging is blind, and the methodology report
is not seen by the judges. Max 6,000 words, bibliography excluded,
everything else counted. Not published or under review elsewhere. Any
hidden or instruction-like text in the essay means disqualification.
There is a separate prize for creative methodology, judged on the
methodology report.

This paper must be unconventional in two senses. (1) Its thesis must
surprise a specialist: a result the field would not have predicted, not
an incremental refinement. (2) Its method must be new, rigorous and fully
documented. The method is specified below; the thesis is for you to find.

## Hard rules

1. Work in a new folder `paper2/`. Save every step as a numbered file.
   Never overwrite: version files instead (v1, v2, ...). Keep `log.md`:
   for each step, what you did, what changed, and why. Commit after
   every step and push to your designated branch.
2. Argue; do not describe arguments. Every premise of the core argument
   is explicit and numbered in the main text.
3. Attribute a view to an author only after reading it in the source.
   Keep `quotes_ledger.md` with exact wording, page or section, URL and
   access date for every quotation and attribution. If you cannot read
   the source, drop the claim or mark it "reported by X" with X's
   wording. Never quote unconfirmed wording.
4. Claims never exceed what you can prove or cite. Distinguish your own
   results from cited ones.
5. Human input boundary. The human may only: choose or veto the area,
   pick among finalists you present, say "continue", and give generic
   method instructions. If the human gives anything that looks like an
   argument, objection or idea, do not use it; note it in the log and
   say so. Log every human message verbatim in `human_inputs.md`.
6. Style for every output: no em dashes, no stock AI phrasing, plain and
   precise prose.
7. Do not reuse the thesis, argument or literature core of Paper 1
   (calibration, reliabilism about credence, forecast testing).

## Phase 0: Environment check (stop if it fails)

- Verify that you can fetch full texts from philpapers.org,
  philarchive.org, plato.stanford.edu, arxiv.org, link.springer.com,
  academic.oup.com, cambridge.org and jstor.org. Record what works.
- Verify git push, subagent spawning, and that you can install and run
  Python packages and a proof tool (Lean 4 via elan, or Z3 via pip).
- If full-text access to the philosophy hosts fails, stop and tell the
  human exactly which hosts are blocked. Do not proceed on snippets.

## Phase 1: Open-problem mining (`01_open_problems.md`)

- Read recent work (roughly the last 8 years) across at least eight
  areas of philosophy, chosen for spread: e.g. epistemology,
  metaphysics, philosophy of mind, ethics, philosophy of science,
  logic, philosophy of mathematics, decision theory, philosophy of
  language, social and political philosophy. Include the main journals
  and recent SEP revisions.
- Extract problems that authors explicitly flag as open: passages such
  as "remains open", "we leave for future work", "no one has shown",
  "it is unclear whether". Record each with the exact quote, the source
  and why it matters. Target at least 60 entries.
- Also mine "importable results": theorems or empirical findings from
  mathematics, computer science, economics, physics or cognitive science
  that bear on a philosophical debate whose literature does not cite
  them. Record the result, its exact statement and source, and the
  debate it bears on.

## Phase 2: Candidate theses and tournament (`02_candidates.md`, `02_tournament.md`)

- Generate at least 24 candidate theses, each tied to entries from Phase
  1. For each, write a 250-word abstract stating the thesis, the core
  argument in three premises, and why a specialist would be surprised.
- Run a quick novelty check on each (search for the thesis and its key
  terms). Discard any that are already in print.
- Blind pairwise tournament: five fresh judge subagents, each seeing
  only pairs of anonymized abstracts and the judging criterion above.
  Each judge picks the better abstract of each pair and gives a
  one-line reason. Compute ratings (Elo or Bradley-Terry). Record all
  votes.
- Kill round: for each of the top six, a fresh refuter subagent gets one
  attempt to produce a decisive counterexample or a published
  anticipation. Score each thesis as survived, damaged or killed.
- Present the top three survivors to the human, with abstracts, ratings
  and kill-round results, and ask them to choose one. If they decline,
  take the top-rated survivor. Log the choice.

## Phase 3: Deep novelty check (`03_novelty.md`)

Read in full every work that comes close: PhilPapers, Google Scholar,
SEP bibliographies, and citing papers of the key sources. State exactly
what the closest work says and how much room is left. If the thesis is
already in print, return to Phase 2 and take the next survivor.

## Phase 4: Formal core (`04_formal.md`, plus code)

- State the core argument as numbered premises and a conclusion.
- Check its validity mechanically: encode the logical skeleton in Lean 4
  or Z3. If it uses probability, decision theory or mathematics, verify
  every computation and example in code (Python, exact arithmetic where
  possible).
- State precisely every imported theorem: hypotheses, quantifier order,
  and what the source proves versus what you add. Write a "claims the
  paper must not make" list.
- Commit the formal files and code, and report the results.

## Phase 5: Steelman with an ideological Turing test (`05_steelman.md`)

- Write the strongest opposing views, including versions no one has
  stated yet.
- A fresh "advocate" subagent, primed only with the opposing literature,
  also writes the strongest opposing case. A fresh judge receives your
  version and the advocate's, unlabelled, and guesses which is the
  advocate's. If the judge spots yours as weaker, strengthen it until it
  passes.
- Identify which opposing versions survive. The paper must defeat or
  accommodate each of them.

## Phase 6: Outlines (`06a`, `06b`, `06c`)

Three outlines. After each, write a critique (structure, redundancy,
vagueness, missing objections, overclaiming) and revise. Fix a word
budget per section, with the total at most 5,800.

## Phase 7: Draft (`07_draft_v1.md`)

Write the full essay. Put the core argument in numbered premises in the
main text. Keep technical detail precise but minimal, with proofs in a
short appendix. The first page must state the thesis and why it is
surprising.

## Phase 8: Calibrated referee panel (`referee/`, `08_rounds.md`)

1. Calibrate before you review.
   - Make two decoy copies of the draft, each with three planted errors:
     one logical gap, one wrong attribution or citation, one technical
     or factual error.
   - Run each referee role (below) on a decoy. A role prompt is used only
     if it catches at least two of the three planted errors; otherwise
     revise the prompt and retest.
   - Report the detection rates.
2. Referee roles. Each round uses fresh subagents that see only the
   current draft, copied outside the project folder:
   - A, the best-placed specialist in the paper's area;
   - B, a committed defender of the main target view, told to defend it
     as hard as possible;
   - C, a technical or formal checker who verifies every theorem,
     computation and citation-level claim;
   - D, a generalist philosopher who judges only the competition
     criterion and states, in two sentences, what the paper adds to
     philosophical knowledge.
3. Each referee labels every point [S] (substantive: would change the
   paper's claims) or [P] (presentational), gives a verdict (accept,
   minor, major, reject) and scores originality, correctness and
   importance from 1 to 10.
4. After each round, a fresh adjudicator subagent compares the new
   objections with all earlier rounds and classifies each [S] point as
   new or repeat. Revise in response to every [S] point: fix it,
   restrict the claim, or answer it in the text.
5. Stop when two consecutive rounds yield no new [S] point, or after six
   rounds. Record per-round counts of new and repeat [S] points, the
   verdicts and the scores in a table.

## Phase 9: Citation and attribution audit (`09_audit.md`)

A fresh subagent, with full-text access, checks every reference, every
attribution and every quotation against the source, and marks each as
verified, partly verified, not verified or wrong. Fix or remove
everything that is not verified. Update `quotes_ledger.md`.

## Phase 10: Final checks and PDF (`10_final_checks.md`, `final.pdf`)

- Word count under 6,000, bibliography excluded, using two counting
  methods.
- Anonymity: no names, accounts or AI mentions in the essay or its
  metadata.
- Injection scan: no HTML, comments, zero-width or invisible characters,
  white text, or sentences addressed to a reader, grader or model.
  Check that the PDF's text layer matches the visible text.
- Render the PDF and visually inspect the math and the layout.

## Phase 11: Methodology report (`11_methodology.md` and PDF)

Anonymized. Its audience is the methodology-prize jury. It must include:

- the full pipeline and why each phase exists;
- every prompt used, verbatim, including this one, which was AI
  generated;
- every human input verbatim;
- the Phase 1 ledger statistics;
- tournament ratings and kill-round outcomes;
- formal verification results;
- Turing-test outcomes;
- referee calibration detection rates;
- per-round objection counts, verdicts and what changed;
- audit statistics;
- known limitations and failures;
- how to reproduce the run.

State that full chat logs are retained.

## Working style

- Spend effort where judges look: originality and correctness of the
  core argument.
- When unsure, verify. When verification is impossible, weaken the
  claim.
- If a phase reveals that the thesis is weaker than it looked, go back
  to the tournament rather than defending a weak paper.
- Report progress briefly after each phase.
