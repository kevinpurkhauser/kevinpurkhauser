# 01. Final novelty check

## Method and its limits

Full-text download was blocked by the environment's network policy for every scholarly host tried (arxiv.org, philpapers.org, philarchive.org, plato.stanford.edu, core.ac.uk, link.springer.com, cambridge.org, faculty pages). The only readable channel was a web-search tool that returns summaries plus verbatim snippets of the pages it reads. Everything below is therefore based on abstracts, snippets and secondary reports, recorded verbatim where possible in `sources/search_notes_step1.md`. Consequences:

1. Claims about what an author holds are limited to what those snippets show. Where a claim rests only on a secondary report (for example the SEP's report of Dunn's reply to Goldman), it is marked as such and will be stated in the paper only in that form.
2. A negative novelty result ("no paper makes this argument") is less secure than it would be with full-text access, because a footnote in a paper I could not open (Dunn 2015, Tang 2016, Pettigrew 2021) might mention Foster and Vohra. I searched specifically for co-occurrence of these names with calibrationist reliabilism and found none.

## What was located and what each says (as far as verified)

| Work | Verified content relevant to the thesis |
|---|---|
| Dunn 2015, *Phil. Studies* 172: 1929-52 | Reliability and truth-possession part ways for credence; proposes a Ramsey-inspired calibration measure. Calibration defined (footnote): a process is well calibrated if it produces beliefs in P to degree n and n% of the propositions like P are true. Requires looking at performance "in nearby worlds", not only actual cases. Secondary reports: says little about which counterfactual circumstances count ("a difficult question in general"). |
| Tang 2016, *Mind* 125: 63-94 | Reliabilism as it stands cannot account for justified credence; considers three reliabilist strategies; defends a hybrid with evidentialist elements. As reported by SEP: objects that a process can be well calibrated while insensitive to relevant evidence; own condition: C(p) justified only if based on a ground g such that the objective probability of p given g approximates C(p). |
| Pettigrew 2021, *Episteme* 18: 16-30 | Dunn's view is process reliabilism, Tang's indicator reliabilism; they are extensionally equivalent (on the right reading); both face the Connection Problem; offers a view that is both process and indicator. SEP: an evidence-relative calibration approach turns out extensionally equivalent to a version of Tang's. Details of his positive account not verified. |
| SEP, "Reliabilist Epistemology", sec. on degrees of belief | Calibration approach: a credence is justified iff produced by a well-calibrated process; motivates it against the Brier approach. Reports Goldman's (1986) case: an agent 70% of whose opinions are true can be perfectly calibrated by assigning .7 to everything; reports the nearby-worlds and process-level replies, and Tang's evidence-insensitivity objection. No mention of Foster, Vohra, Sandroni, Dawid or Belot found. |
| Dawid 1982, *JASA* | A coherent Bayesian assigns probability one to being well calibrated (by its own lights). |
| Oakes 1985; Dawid 1985 | No deterministic forecasting system is calibrated on every sequence. |
| Seidenfeld 1985, *Phil. Sci.* 52: 274-94 | Long-run calibration under feedback is "otiose" and gives no ground for preferring one coherent opinion over another; short-run calibration rewards hedging and is improper. |
| Belot 2013, *Stat. Prob. Letters* 83: 2316-18 | Calibration failure is topologically typical for any forecasting system; Bayesian forecasters are certain of their calibration; this "invites worries about the connection between Bayesianism and rationality". Cites Foster-Vohra randomization. |
| Wilcox 2024, *Rev. Phil. Psych.* 16: 305-44 | "Inclusive calibrationism": probability judgments are trustworthy only to the extent one has good reason to think they come from maximally inclusive, well-calibrated processes. |
| Williams and Pettigrew, "Consequences of Calibration", *BJPS* | Calibration as a test on accuracy measures; yields strict propriety. Different question. |
| Levinstein, "Accuracy Uncomposed", *Episteme* | Against calibration in the decomposition of inaccuracy. Different question. |
| Dorst 2023, *Phil. Imprint* 23 | Rational agents can be expected to be miscalibrated. Converse direction (calibration not necessary). |
| Isaacs 2021, Schoenfield, Ye 2023 | "Calibrationism" in the higher-order evidence sense. Different view sharing the name. |
| Phil. Studies 2025, "Does calibration mean what they say it means" | Reference-class problem for calibration and multicalibration. Relevant to Step 3 only. |
| Olszewski, "Calibration and expert testing" (Handbook of Game Theory 4) | Economics survey; draws a moral about Popperian falsifiability and strategic experts, not about justification. |

Searches for philosophy papers citing Foster and Vohra (1998) or Sandroni (2003) returned only Belot (statistics venue, topic: Bayesian calibration) and economics, statistics and machine-learning work. Google Scholar and PhilPapers could not be queried directly; the search tool reached PhilPapers and PhilArchive record pages only through its own index.

## Verdict

No located paper makes the argument. Specifically, none argues that the Foster-Vohra theorem refutes the sufficiency of (process-level, counterfactually robust) calibration for justified credence, and none uses the expert-testing manipulability results against reliabilism about credence.

## Precursors and how much room is left

The thesis has close precursors, and the paper must position itself against them rather than present the general worry as new:

1. **Goldman's 70% case** (as reported in SEP): calibration in the actual world can be had without good reasons. Calibrationists answer by moving to processes and to nearby worlds. The SEP statement of the reply is explicit: if it is "just a matter of chance" that 70% are true, looking across nearby worlds avoids the consequence.
2. **Tang's objection**: a process can be well calibrated while insensitive to relevant evidence. Stated, as far as verified, as a possibility claim with examples, not via any theorem about robust calibration.
3. **Seidenfeld 1985**: long-run calibration cannot discriminate between coherent opinions. This is about coherent Bayesians under feedback, not about uninformed processes or reliabilism.
4. **Belot 2013**: about Bayesian certainty of calibration versus topological typicality of failure. Different conclusion (about Bayesian orgulity, not reliabilism).

What remains open, and is the paper's contribution:

- (a) **The theorem defeats exactly the reply that saved calibrationism from Goldman and Tang.** The nearby-worlds and process-level replies work only if trivial calibration is accidental. Foster-Vohra shows there is a process whose calibration is not accidental in any world: it is calibrated, almost surely relative to its own randomization, against every sequence. Counterfactual robustness therefore cannot exclude it, whatever set of worlds is chosen.
- (b) **A dominance or inversion point**: such a process is at least as well calibrated as any process over any set of worlds, so modal robustness, the feature added to fix the Goldman case, can only favor it.
- (c) **Generalization with exact limits**: from calibration to any outcome-based standard, via Sandroni (2003) and Olszewski and Sandroni (2008), together with a precise account of where the generalization stops (non-manipulable tests of Dekel and Feinberg 2006, Olszewski and Sandroni 2009; computational limits of Fortnow and Vohra 2009). The Stage 1 formulation "no purely outcome-based test separates informed from uninformed" is too strong as it stands and must be restricted (see Step 2).
- (d) **Diagnosis and positive upshot**: the calibrationist's notion of reliability is a property of track records, actual or counterfactual; the theorems show track-record reliability, so understood, cannot be what makes credence justified. What survives is close to Tang's grounds-and-chance condition, which is not outcome-based. The paper can argue that this is forced, not optional, and must address whether it collapses back into an outcome-based condition if chances are Humean.

Room left: substantial for (a) to (d). The paper must cite Goldman (via SEP or the original), Tang and Pettigrew as precursors and present (a) as a sharpening that defeats the standard reply, not as the first statement of the worry.

## Open risks recorded for later steps
- Dunn's full text might contain a specific answer (for example, a restriction on randomizing processes or on which inputs a process may use). Not verifiable here; the paper should not claim Dunn has no answer, only that the reply reported in the literature fails.
- Pettigrew's evidence-relative calibration must be treated in Step 3 as a strong opponent.
