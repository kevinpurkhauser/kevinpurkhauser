# 08. Final checks

Final text: `05_draft_v6.md` (v5 plus the audit fixes of `07_audit.md`, plus a rendering fix for enumerated list items). PDF: `final.pdf` (15 pages, A4), built with pandoc (MathML) and headless Chromium.

## Word count (limit 6,000, excluding bibliography)
- Plain-text rendering of everything before the References (title, abstract, body, appendix), via pandoc: 5,744 words.
- Whitespace count of the Markdown source before the References (counts math tokens as words): about 5,960.
- Text extracted from the PDF before "References" (includes hyphenation splits and rendered math symbols): 5,977.
- All three measures are under 6,000.

## Anonymization
- Searched source and PDF text for the author's name, e-mail, "Claude", "Anthropic", "AI", "language model", "GPT", "prompt", "instruction": no hits in the essay. (AI involvement is described only in the separate methodology report, as the rules require.)
- PDF metadata: Title "Calibrated Everywhere"; no Author field; Creator/Producer are the generic Chromium/Skia strings.
- No self-citation, acknowledgements or identifying references.

## Hidden or instruction-like text
- No HTML comments, spans, divs, style attributes or colour/visibility markup in the source.
- No zero-width or soft-hyphen characters; the only non-ASCII characters are "á" (Hájek) and "′" (D1′).
- The PDF text layer matches the visible text (checked by extraction); fonts are ordinary embedded serif fonts; no white or invisible text.
- No sentence addressed to a reader, grader or model.

## Content checks
- Every quotation remaining in the text was confirmed at abstract or snippet level by the audit (Foster-Hart 2018; Dawid 1985a; Gneiting et al. 2007; Olszewski-Sandroni 2009a; Schurz 2019, attributed to the publisher's description). Unverifiable quotations were paraphrased (Dunn 2015; the SEP's "matter of chance"; Olszewski-Sandroni 2008).
- Rendering inspected on sample pages (math, lists, block quotes).
