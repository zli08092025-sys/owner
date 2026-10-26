# Reviewer E — pages 19, 20, 21

Paper: α-Synuclein aggregates induce mitochondrial damage… (Nat Commun 2026 17:6462)

## Previews inspected

I read all three preview PNGs with the Read tool (`previews/page-0019.png`,
`page-0020.png`, `page-0021.png`) before editing anything, and additionally rendered
6x zoom crops from `source.pdf` with PyMuPDF into my own scratch directory
(`/tmp/claude-0/-home-user-owner/2a8036d7-43c5-51a4-a12a-13d09f56561b/scratchpad/reviewer-e/`)
for every ambiguous spot (refs 12, 13, 47, 63, 70, the Acknowledgements line, and the
"Reprints and permissions information" block). Nothing was written inside the
paper-review directory except the three page JSONs I own. Page 18 was read only, not edited.

## Reference numbering — the headline result

**References 1–101 are present and in ascending order, none missing and none duplicated.**

| page | refs | count |
| --- | --- | --- |
| 18 (read-only context) | 1–2 | 2 |
| 19 | 3–43 (left col 3–24, right col 25–43) | 41 |
| 20 | 44–87 (left col 44–66, right col 67–87) | 44 |
| 21 | 88–101 (left col only) | 14 |

The sequence is unbroken across both page breaks: p18 ends at 2 → p19 starts at 3;
p19 ends at 43 → p20 starts at 44; p20 ends at 87 → p21 starts at 88; the list ends at 101.
I cross-checked the count independently against the PDF font spans: the semibold face used
for volume numbers occurs exactly 41 / 44 / 14 times on the three pages, matching the
reference counts.

After my edits each reference is exactly one `text` item — no item holds two references and
no reference spans two items. Reading order is left column top-to-bottom then right column
top-to-bottom on every page.

## Page 19 — changes

- **Split 7 merged extractor items into 15.** The extractor had glued multiple references
  into single blocks: 8+9, 10+11+12+13, 15+16, 17+18, 20+21, 29+30, 33+34. Each is now its
  own item with a suffixed id (`p0019-b007a/b`, `b008a..d`, `b010a/b`, `b011a/b`,
  `b013a/b`, `b021a/b`, `b024a/b`) and a bbox derived from the PDF line boxes.
- **Italics / bold restored** on all 41 references: journal names italicised
  (`*Brain Pathol.*`), volume numbers bolded (`**9**`). Verified against the actual font
  spans — italic face `AdvOT23e3f5cb.I`, semibold volume face `AdvOT13119950`.
- Text fixes against the visible source:
  - ref 12 `hallmark withtherapeutic` → `hallmark with therapeutic` (the space **is**
    printed; the PDF text layer dropped it — confirmed at 6x)
  - ref 13 `of α- synuclein` → `of α-synuclein`
  - ref 28 `bidirectional` → `bi-directional`
  - ref 29 `aggregateinduced` → `aggregate-induced`
  - ref 40 `alphasynuclein` → `alpha-synuclein`
  (all four are hard hyphens that happened to fall at a line break)
- Checked and left alone the genuine soft line-break hyphens: composi-tion, dys-function,
  mitochon-drial, Mito-chondrial, Immu-nol., neu-roinflammation, Tunnel-ling, Sci-ence,
  Tun-neling.
- Verified accented names (Burré, Martínez, Ramírez-Jarquín, Saffrich, Vignais), Greek α
  throughout, `5×FAD` with a multiplication sign, em dashes in refs 11 and 12, and an en
  dash in every page range (`721–732`, `342ra78–342ra78`, `3106–3125.e8`, …).
- Header, footer and the page-number `omit` item untouched.

## Page 20 — changes

- **Split 6 merged extractor items into 20.** Merged blocks were 48+49+50, 51+52+53+54,
  55+56+57+58+59, 60+61+62+63, 64+65+66, 80+81. Suffixed ids `b006a..c`, `b007a..d`,
  `b008a..e`, `b009a..d`, `b010a..c`, `b024a/b`.
- Italics / bold restored on all 44 references.
- Text fixes:
  - ref 44 `alphasynuclein` → `alpha-synuclein`
  - ref 48 `DEVDspecific` → `DEVD-specific`
  - ref 58 `smallmolecule` → `small-molecule`
  - ref 63 `α-synucleindependent` → `α-synuclein-dependent`
  - ref 84 `p65/ RelA` → `p65/RelA`
- Verified Kräusslich, Härtlova, Glück, Anandatheerthavarada, Cordelières (p21), κ in
  NF-κB / IκB / NFκB, `77A` volume, and every en dash.
- Soft hyphens correctly closed up and left alone: inter-ventions, phos-phorylation,
  mito-chondrial, recog-nition, Ana-ndatheerthavarada, segre-gation, propa-gation.

## Page 21 — changes

- References 88–101: italics / bold restored; ref 94 `iPSCbased` → `iPSC-based`. No merges
  or splits were needed here.
- Verified Sánchez-Danés, Tristán-Noguero, Sáenz-de-Santa-María, Cordelières; `amyloid
  β–induced` (en dash, as printed); `β-cells`; the italic journal names that cross a line
  break (`*Alzheimer's. Dement.*`, `*Nat. Biotechnol.*`, `*Am. J. Physiol. Endocrinol.
  Metab.*`).
- **Heading fix (the one you flagged).** `## Reprints and permissions information is
  available at` was **not** a printed heading. At 6x it is a bold run-in label
  ("Reprints and permissions information") followed by regular-weight body text
  ("is available at") on the *same line*, with the URL wrapping to the next line — exactly
  the same pattern as Supplementary information / Correspondence / Peer review information /
  Publisher's note / Open Access. It is now a `text` item, merged with the bare-URL item
  that followed it. **Item `p0021-b028` no longer exists** (folded into `p0021-b027`).
- Acknowledgements fixes: `Institut Pasteur,for` → `Institut Pasteur, for` (the space is
  printed; text layer lost it); `LCF/BQ/ DI21/11860038.` → `LCF/BQ/DI21/11860038.`;
  `PID2022139546OB-I00` → `PID2022-139546OB-I00`.
- Open Access licence paragraph transcribed verbatim, with the Creative Commons URL closed
  up across its line break: `http://creativecommons.org/licenses/by/4.0/`. Copyright line
  `© The Author(s) 2026` kept.
- Top-level headings on this page are exactly the four required: `# Acknowledgements`,
  `# Author contributions`, `# Competing interests`, `# Additional information`.

## For the coordinator

1. **Journal italics / volume bold on page 18.** I italicised journal names and bolded
   volume numbers for refs 3–101. References **1 and 2 live on page 18**, which I may not
   edit, and they are still plain text. Whoever owns page 18 should apply the same markup to
   `p0018-b022` (ref 1, *Cell Death Dis.* **14**, 1–16) and `p0018-b023` (ref 2, *Science*
   **282**, 1075–1079) so the bibliography is uniform. This is the only inconsistency I
   knowingly introduced.
2. **Heading hierarchy under "Additional information" — I did NOT promote these to `##`.**
   My brief listed Supplementary information / Correspondence / Peer review information /
   Reprints and permissions / Publisher's note / Open Access as `##`. On inspection they are
   all bold *run-in* lead-ins inside paragraphs, set in the same semibold face
   (`AdvOT13119950`) that the reference volume numbers use — a different face and size from
   the four real section headings, which use the true bold face. The conventions file
   explicitly forbids inventing a heading from bold lead-in text inside a paragraph, so I
   left all six as `text` with their labels bolded (`**Open Access** This article is
   licensed…`). If you want them as `##` anyway, it is a one-line change per item on page 21
   — say the word and I will not argue, but I believe `text` is correct.
3. **Printed defect kept verbatim: reference 47, page 20.** The article really prints
   "accompanies cytochrome crelease during apoptosis" with no space — confirmed at 6x, and
   contrast ref 48 on the same page which prints "cytochrome c release" correctly. Per the
   verbatim rule I left it as printed. If the bundle is meant to be *usable* for literature
   lookup rather than a facsimile, you may want to correct it to "cytochrome c release";
   that is your call, not mine.
4. **Literal asterisks escaped.** Refs 47 and 70 (page 20) and ref 98 (page 21) carry a
   printed footnote asterisk ("…in PC6 cells*.", "…disease brain*.", "…diseases*."). Because
   the next character sequence starts an italic journal name, an unescaped `*` would open
   markdown emphasis and corrupt the entry. I wrote them as `\*`. If the builder does not
   interpret markdown in these items, the backslashes should be stripped.
5. **No cross-page joins needed in my range.** Pages 19, 20 and 21 each open with a fresh
   numbered reference, so no `join_previous` was set on any of them.
6. **Acknowledgements paragraph spans both columns of page 21** (`p0021-b017` ends "sur le",
   `p0021-b018` begins "Cerveau (FRC 2023)"). I left it as two items to match how the same
   situation is handled elsewhere in the document (e.g. page 18 `b006`/`b007`). If the
   builder inserts a paragraph break between items, that sentence will be split — worth a
   document-wide decision rather than a page-21-only one.
7. **Unclosed parenthesis in the Acknowledgements** — "(code: LCF/BQ/DI21/11860038." never
   closes. That is how the article prints it; I did not "fix" it.

## Limitations

- Soft (line-break) vs hard hyphens cannot be distinguished from the PDF text layer alone,
  since both render as U+002D. For each of the 9 cases I restored a hyphen, I reasoned from
  the layout (a hyphen at a break where the word is not being syllabified must be a real
  hyphen) and cross-checked against the published title of the cited work. The five cases on
  pages 19–20 listed above are the ones I changed; everything else I left closed up.
- I did not run the bundle build or verify commands, and made no git commits.
