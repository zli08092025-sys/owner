# Shared review conventions — alpha-syn-mito-tnt-paper

Paper: "α-Synuclein aggregates induce mitochondrial damage and trigger innate immunity to
drive neuron–microglia communication", Nature Communications (2026) 17:6462,
https://doi.org/10.1038/s41467-026-73136-7. Main article PDF, 21 pages, two-column layout.

## Paths

- WORK  = /tmp/claude-0/-home-user-owner/2a8036d7-43c5-51a4-a12a-13d09f56561b/scratchpad/paper-review
- DOC   = $WORK/documents/s001-ebbd35bc-nc-alpha-syn-aggre-induce-mito-damage-a
- Pages    : $DOC/pages/page-NNNN.json   <- YOU EDIT ONLY YOUR ASSIGNED FILES
- Previews : $DOC/previews/page-NNNN.png <- read-only, this is the visual truth
- Evidence : $DOC/evidence/page-NNNN.json <- read-only raw extraction lines
- Source   : $DOC/source.pdf              <- read-only

Never edit previews, evidence, source.pdf, plan.json, bundle.json, or pages outside your
range. The coordinator owns plan.json, bundle.json and all build commands.

## How to review a page

1. Read the preview PNG with the Read tool (it renders images). Look at the actual page.
   If detail is too small, render a zoomed crop of the region with PyMuPDF from source.pdf
   into your own scratch directory and read that. Do not write into WORK.
2. Read the page JSON and compare every item against what you see.
3. Fix: reading order, item kind, heading level, text errors, figure bboxes, captions.
4. Set `reviewed: true` and write a specific `review_notes` string saying what you checked
   and what you changed. Never mark a page reviewed you did not look at.

Reading order = source logical order: full-width header items, then left column top to
bottom, then right column top to bottom. A full-width figure or caption goes at its
vertical position relative to the columns it interrupts.

## Item rules

- `markdown` is emitted verbatim for `heading`, `text`, `caption`. Correct OCR/extraction
  errors against the visible source. Do NOT paraphrase, summarise, shorten or re-word.
- `figure` / `formula`: the bbox is cropped to JPEG; `markdown` is ignored. Keep the caption
  as a separate `caption` item.
- `table`: `rows` (list of equal-length lists of STRINGS) becomes CSV. `markdown` ignored.
- `omit`: emits nothing and REQUIRES a nonempty `reason`. Only for page numbers and
  decorative logos, never for substantive content.
- IDs must stay unique within the document. Keep existing IDs where you can; if you split an
  item, give the new parts suffixed ids like `p0001-b004a`, `p0001-b004b`.
- `bbox` is `[left, top, right, bottom]` in PDF points, top-left origin, page is
  595.28 x 790.87 pt. Stay inside page bounds.

## Running header / footer — LEAVE THEM ALONE

Every page carries `Article` or the journal name, the DOI URL, the footer
`Nature Communications |  (2026) 17:6462`, and a page-number item already set to `omit`.
The compact builder removes repeated short margin headers/footers automatically and records
that in build.json. Leave those items as they are. Do not convert them to `omit` yourself.

## Heading hierarchy (apply exactly)

Level 1 (`#`) — only these top-level sections:
  Results, Discussion, Methods, Data availability, References, Acknowledgements,
  Author contributions, Competing interests, Additional information

Level 2 (`##`) — every subsection inside those, including every Results subsection
  (e.g. "α-Syn aggregates cause mitochondrial dysfunction", "α-Syn leads to BAX-mediated
  mtDNA release") and every Methods subsection (e.g. "Culture of cell lines",
  "Neuron generation", "Preparation of α-Syn aggregates", "qRT-PCR", "Western blotting",
  "Quantification and statistical analyses", "Reporting summary").

The extractor emitted several subsection headings at `#`. Demote them to `##`.
The page-1 article title stays a single `#` heading; the builder drops it as a duplicate
of the generated title.

Headings must be real section headings visible in the source. Never invent a heading from a
running header or from bold lead-in text inside a paragraph.

## Figure and table asset names (fixed map — use exactly these)

| Image on page | label        | asset_name | caption located on |
| --- | --- | --- | --- |
| 3  | Figure 1 | figure-1 | page 3  |
| 4  | Figure 2 | figure-2 | page 5  |
| 6  | Figure 3 | figure-3 | page 7  |
| 8  | Figure 4 | figure-4 | page 9  |
| 10 | Figure 5 | figure-5 | page 11 |
| 12 | Figure 6 | figure-6 | page 13 |
| 14 | Figure 7 | figure-7 | page 15 |
| 16 | Figure 8 | figure-8 | page 17 |
| 17 | Figure 9 | figure-9 | page 17 |
| 18 | Table 1  | table-1  | page 18 |

All nine figures are main-article figures: leave `asset_category` unset so they route to
`assets/figure/`. There are no extended-data figures in this PDF.

Figure bbox checks: the crop must contain every panel, every panel letter (a, b, c …), all
axis labels, the scale bars and the colour-channel legends. Panel letters sit close to the
left edge and are easy to clip. Verify the top, bottom, left and right edges against the
preview before you accept a bbox. Captions must NOT be inside the figure crop.

## Caption items

Each figure caption begins `Fig. N | <title>.` followed by panel descriptions. Set
`kind: "caption"` and transcribe the whole caption verbatim, including panel letters,
statistics, `N`/`n` values and p-values. Captions for figures whose image is on the previous
page belong at the TOP of their page, before the body text, matching the printed layout.

## Typography to preserve

- Greek: α β γ Δ Ψ μ (α-Syn, ΔΨm, μm, μM, μg, μl). Never write "a-Syn" or "u-m".
- `–` en dash in ranges and in "neuron–microglia", "cGAS–STING–NF-κB–IRF3".
- κ in NF-κB. β in β-actin, IFNβ, IL-1β.
- Superscript reference markers stay as `<sup>12</sup>` / `<sup>8–10</sup>`.
- Superscripts/subscripts in units and notation: `10<sup>4</sup>`, `CO<sub>2</sub>`.
- Gene symbols italicised in the source stay italicised: `*SNCA*`, `*PARKIN*`, `*PINK-1*`.
- Degree and plus-minus: °C, ±. Multiplication sign ×, not letter x.
- p-values such as `p = 0.0029`, `***p < 1×10<sup>-15</sup>` must match the source exactly.

## Cross-page prose

If a page's first text item continues a sentence from the previous page, set
`join_previous` to `"space"` (sentence continues after a space) or `"none"` (a single word
is split across the break). Check the visible source before joining. Do not delete a real
compound hyphen while repairing a line-wrap hyphen. Report any join you set.

## Your report

Write a markdown report to the path given in your task. Include:
- pages reviewed, and confirmation you looked at every preview
- every change you made, per page
- anything that belongs to the coordinator: cross-page joins, asset-name conflicts,
  suspected mis-splits spanning your range boundary, heading-hierarchy doubts
- limitations: anything you could not verify from the supplied PDF

Do not run the bundle build or verify commands. Do not git commit.
