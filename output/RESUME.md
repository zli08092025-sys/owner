# Paper2Agent conversion — paused, resumable

Paper: "α-Synuclein aggregates induce mitochondrial damage and trigger innate immunity to
drive neuron–microglia communication", Nature Communications (2026) 17:6462,
https://doi.org/10.1038/s41467-026-73136-7 (main article PDF, 21 pages).

Converted with the `paper2agent` skill from https://github.com/jmiao24/Paper2Agent,
Paper2Skill route. Paused at the owner's request before the billing mode was changed.

## Status

**The package in `alpha-syn-mito-tnt-paper/` is a staging build, not a verified
deliverable.** It builds cleanly and every mechanical check passes, but strict verification
still reports `unresolved_discrepancies` because 23 parser diagnostics have not yet been
adjudicated. Do not ship it as final until the remaining steps below are done.

Route: paper-only. This is a wet-lab cell-biology article with no analysis code. Its data
availability statement names no repository and none exists in this GitHub account, so there
is nothing for Paper2MCP to bind MCP tools to. The skill treats a single-mode run as valid.

## What is done

- All 21 pages reviewed page by page against rendered previews and zoomed crops, by five
  reviewers over separate page ranges plus a coordinator reconciliation pass.
- Figures 1–9 cropped, named and verified to contain every panel, panel letter, scale bar
  and legend. All nine JPEGs match their recorded source conversion.
- The qRT-PCR primer table transcribed to CSV, every base cross-checked by three
  independent methods. `assets/table/table-1.csv` matches its source conversion.
- References 1–101 verified present, in order, none missing or duplicated.
- Page 1 repaired: the masthead was misread as a scientific figure, and the dates, author
  list and abstract were merged into a fake table. The abstract is now searchable prose.
- Sentences split by the two-column layout reconnected with 29 `join_previous` flags.
- A `reading_order` in `plan.json` places each figure immediately before its own caption at
  a paragraph boundary, instead of a page of unrelated prose away.
- Line coverage is complete on 20 of 21 pages (page 1 is explained below).

## Remaining steps

1. **Adjudicate the 23 diagnostics.** They were analysed and all appear to be parser-only
   differences, but the adjudication entries were not written. The analysis:
   - *Superscript concatenation.* The flattened PDF text layer glues a trailing digit to the
     reference marker that follows it, so `HMC3<sup>42</sup>` reads as `342` and
     `ABT-737<sup>55</sup>` as `-73755`. The Markdown separates them correctly. Affects
     pages 2, 6, 7.
   - *Hyphens restored at line breaks*, each verified against the visible source:
     `JSH-23`, `HY-148045`, `PA5-17752`, `X0551-100`, `n = 18-21`, `5.64×10⁻⁵`, and the
     grant number `PID2022-139546OB-I00`. Affects pages 7, 11, 13, 15, 21.
   - *Page 1 only.* Two missing lines are the rotated `1234567890():,;` printer's font-test
     strings in the left margin, which are furniture rather than content. The two extra
     numbers are `15` and `2026` from "Published online: 15 May 2026", which is a rasterised
     image in the PDF, invisible to text extraction and transcribed from the visible page.
   - *`independent_parser_number_differences`.* pypdf splits numbers into single digits on
     this PDF's anonymised subset CFF fonts. `fonttools` was installed and the package
     rebuilt, but the effect on these diagnostics was not re-checked. **Re-read
     `verification-staging.json` after a rebuild before writing these adjudications** —
     some may have cleared on their own.

   Copy each exact `adjudication_entry` from `review-aid/review-queue.json` into
   `documents/<source-id>/adjudications.json` and replace the placeholder reason with the
   visible-source check. Fingerprints are bound to the exact diagnostic.

2. **Final build into a new directory, then `verify --strict`.** Target status is
   `reviewed_with_limitations`.
3. **Fresh-verifier pass.** The skill requires a verifier distinct from the reviewers and
   the coordinator to compare the assembled package against the visible originals, plus one
   realistic retrieval question answered using only the package.
4. Replace the staging package here with the verified build and delete `.review-state/`
   from the delivery, or move it outside it. Review evidence must not ship inside the skill.

## How to resume cheaply

`.review-state/` holds everything expensive. Re-running `prepare` and `extract` on the same
PDF is deterministic and fast; the slow part was the human-equivalent page review, which is
captured in `documents/<source-id>/pages/*.json` and `plan.json`.

```bash
uv run <skill>/paper2skill/scripts/paper_bundle.py prepare '<the same PDF>' \
  --work /path/to/new-review --name alpha-syn-mito-tnt-paper --main '<the same PDF>'
uv run <skill>/paper2skill/scripts/paper_bundle.py extract --work /path/to/new-review
# then copy bundle.json, plan.json and pages/ from .review-state over the fresh ones
```

Source PDF SHA-256: `e61f3331e348d50ee5bf756e25b6a7d7e592d2a2b59c3fe6b55a46f914432e48`.
The review decisions are valid only for that exact byte sequence.

`.review-state/reports/` holds the five reviewer reports, including deliberate decisions not
to "fix" genuine printed defects in the article. Read them before changing transcriptions:
several apparent errors (`cytochrome crelease`, `For h: PQ:`, `mediatied`, `300 x g` beside
`800 × g`, `HCI` for `HCl`) are what the published article actually prints.

## Known limitations of the package

- Only the main article PDF was supplied. The Supplementary Information, Reporting Summary,
  Peer Review file and Source Data are absent, so every "Supplementary Fig." callout in the
  text cannot be resolved from this package.
- Figure panels are embedded rasters, so text painted inside them is not searchable. It was
  confirmed visually to be inside the crops.
- The article mixes `×` with a letter `x`, and minus, hyphen and en dash in exponents.
  These were transcribed as printed rather than normalised.
- Panel letters and the statistical `p` are bold and italic in the source; they are plain in
  the Markdown.
