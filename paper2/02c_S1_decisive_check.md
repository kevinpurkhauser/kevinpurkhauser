# 02c. Decisive check on S1 (feasibility version), search snippets only

Scholarly hosts still blocked (curl to arxiv.org, philpapers.org, plato.stanford.edu, philsci-archive.pitt.edu: no connection). Four web searches.

Findings:
1. Confirmed at snippet level: the proof of MIP* = RE admits an explicit separating game, but the construction does not directly yield an explicit correlation in C_qc that is not in C_qa (snippet from arXiv:2307.02920v2). So the "piecemeal, game by game" claim of S1 is dead: one game suffices for the binary choice.
2. The sizes 184/235 inputs and 8/2 outputs belong to Slofstra's game (arXiv:1703.08618), which separates finite-dimensional from limit correlations (C_q vs C_qa), not C_qa from C_qc. Not usable for S1.
3. A preprint, arXiv:2610.10248, "An Explicit Counterexample to Tsirelson's Problem via a Linear System Game", is reported in one snippet to give an explicit counterexample with an explicit lower bound on the commuting/quantum gap and a Lean 4 verification. Its size and its exact content could not be confirmed. If it holds, the feasibility version of S1 loses its premise that no small explicit separation is known.

Status: S1-feasibility is unresolved and leans toward killed. Settling it needs the full text of arXiv:2610.10248.
