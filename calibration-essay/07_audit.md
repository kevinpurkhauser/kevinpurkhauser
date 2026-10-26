# 07. Citation and attribution audit

Auditor: a fresh subagent that saw only the final draft (`05_draft_v5.md`, copied to the scratchpad), with web search only. Full-text access was blocked, so every verdict rests on search snippets, abstracts and publisher or index records. Below is a condensed record of its report (the full report is in the retained chat log), followed by the author agent's response to each required fix.

## References (40 entries)

- **Verified** against publisher or index records: 36 entries.
- **Partly verified** (4):
  - Clifton: no year; add first name and URL.
  - SEP entry: edition not given.
  - Oakes 1985: write 80(390): 339-342 (with discussion).
  - Qiao and Valiant 2021: no page range.

## In-text claims and quotations (47 items)

Verified items: T1, T3, T8, T10, T11 (Foster-Hart quotation), T13-T16, T18, T20, T24, T27, T28, T30-T36, T38-T41, T45, T46.

Partly verified or not verified, with the fix applied in `05_draft_v6.md`:

| Item | Problem | Fix applied |
|---|---|---|
| T2 | The SEP describes the calibration approach rather than asserting it | Reworded: "the SEP entry ... describes the calibration approach, on which ..." |
| T4 | Exact wording "just a matter of chance" unconfirmed | Quotation marks removed; paraphrased |
| T5 | Exact wording of the Dunn quotation unconfirmed; no page | Paraphrased without quotation marks; the "actual cases" fragment in 2.2 also paraphrased |
| T6 | Dawid's diagonal argument is in his 1985 JASA comment on Oakes, not in the Annals paper | Cited as Dawid 1985b (JASA 80: 340-341); the Annals paper is now 1985a |
| T7 | Putnam lineage is the author's interpretation | Kept, phrased as interpretation ("in the line of") |
| T9 | Lower bounds to be attributed separately | Qiao-Valiant T^{0.528}; Dagan et al. T^{0.544} |
| T12 | Atom construction is the author's own | Kept; marked as own construction |
| T17 | "Computable rules" not in Dawid's abstract | Kept: a secondary source confirms "Dawid's notion of computable calibration"; quotation verified |
| T19 | Computable manipulability of finite tests | Kept with "cf."; Hu-Shmaya's halting-problem converse not added (not verified by me) |
| T21 | "Has long required" overstates Gneiting et al. | Reworded: "Gneiting et al. (2007) propose the paradigm of ..." |
| T22 | Gneiting et al. is not the source for the calibration-refinement decomposition | Citation replaced by Foster and Hart 2023, whose abstract states the decomposition |
| T23 | The √T bound is on excess over the tolerance | Reworded |
| T25 | Chapter of Cesa-Bianchi and Lugosi | Changed to "chs. 2-3" |
| T26 | Exact 1 - η - δ bound not seen | Reworded: "with probability arbitrarily close to 1 - η" |
| T29 | Dekel-Feinberg's non-manipulability result needs the continuum hypothesis | Added |
| T37 | Schurz wording matches the publisher's blurb; book page unconfirmed | Attributed to the publisher's description |
| T42 | Goldman's normal worlds: no page | Kept without page (standard characterization; no page could be verified) |
| T43 | The available-better-process idea is Goldman's 1979 alternative-process clause, not the 1986 non-undermining condition | Reworded to "the alternative-process condition of Goldman (1979)"; Goldman 1979 added to References |
| T44 | Dunn's binned definition not seen in Dunn's own text | Kept; the definition in the text follows the footnote quoted in search results ("produces beliefs in P to degree n and n % of the propositions like P are true"), which is a binned notion |
| T47 | Oakes reporting Dawid's coherence observation not found by the auditor | Retained. The author agent's step-6 search notes contain a search summary of Oakes's full text stating that "Dawid notes that a forecaster cannot adjust his future predictions to correct for past empirical miscalibration without sacrificing coherence". Phrasing kept as a report by Oakes |

## Reference fixes applied

- SEP entry: Fall 2019 Edition (the edition whose section 5.3 snippets were used), with URL.
- Clifton: Jesse Clifton, n.d., with URL.
- Oakes: 80(390): 339-342 (with discussion).
- Qiao and Valiant: pages not added (unverified).
- Issue numbers added where verified: Dawid 1982 (379); Shmaya 3(3); Sandroni 32(1).
- Goldman 1979 added.
- Dawid 1985 split into 1985a and 1985b.
