# 10. Final checks

The final text is `07_draft_v10.md`. It is identical to v9, which is v8 plus the audit fixes, except that blank lines were inserted before list items so that pandoc renders them as lists. The PDF is `final.pdf`: 12 pages, A4, built with pandoc (MathML) and headless Chromium.

## Word count (bibliography excluded)

- Method 1: pandoc plain-text rendering of everything before "References" (title, abstract, body, appendix): **4,162 words**.
- Method 2: whitespace-separated tokens in the markdown source before "# References", which counts LaTeX tokens as words: **4,399 words**.
- PDF text layer, including the bibliography: 4,549 words.
- Both counts are well under 6,000.

## Anonymity

- The essay text contains no names, accounts or AI mentions. A case-insensitive search for the author's name, "claude", "anthropic", "AI", "language model" and "as an ai" found nothing.
- PDF metadata: the title is the essay title. Creator and Producer are the headless browser and Skia. There is no Author field.
- PDF text-layer search for the same strings: none found.

## Injection scan

- No HTML, no comments, no `<span>` or `<div>`.
- No zero-width or invisible characters. A codepoint scan found 0 of U+200B to U+200F, U+2060, U+FEFF and U+00AD.
- The only non-ASCII characters are é (Lévy) and ó (Cristóbal).
- No sentences are addressed to a reader, grader, reviewer or model. A search for "reviewer", "grader" and "ignore previous" found nothing.
- The text is black on white with no styling that hides text. The stylesheet sets only fonts, sizes and margins.
- The PDF text layer (4,549 words) matches the visible text. Pages 1, 4 and 11 were inspected visually.

## Visual inspection

- The title, abstract, sections, lists, displayed formulas, the appendix and the references render correctly.
- An earlier render (from v9) showed lists run into paragraphs. This was fixed in v10.

## Style

- No em dashes in the essay (count 0).
