# Reviewer D — pages 16, 17, 18

Paper: α-Synuclein aggregates induce mitochondrial damage… Nat Commun (2026) 17:6462.

**Primer table: TRANSCRIBED, not preserved as an image.** See "Page 18 / Table 1" below for how
the bases were verified.

## Previews inspected

I read all three preview PNGs with the Read tool before editing:
`previews/page-0016.png`, `previews/page-0017.png`, `previews/page-0018.png`.

I additionally rendered zoomed crops from `source.pdf` with PyMuPDF into my own scratch directory
(`/tmp/claude-0/-home-user-owner/2a8036d7-43c5-51a4-a12a-13d09f56561b/scratchpad/reviewer-d-scratch/`)
and read those too:

- `tbl_top.png`, `tbl_bot.png`, `tbl_cd68.png` — primer table at 7x and 9x
- `fig8_bbox.png` — page 16 rendered at exactly the Figure 8 bbox, 2.4x
- `fig9_wide.png` — page 17 rendered 10 pt wider than the Figure 9 bbox on every side, 2.8x

Nothing was written inside the paper-review directory other than the three assigned page JSONs.

---

## Page 16

**Figure 8.** `p0016-b002` → `label: "Figure 8"`, `asset_name: "figure-8"`.

bbox `[55, 45, 546, 650]` kept. I computed the union of every image, drawing and text line in the
figure band from the PDF: `[60.4, 48.6, 540.5, 644.8]`, so the existing bbox clears all four edges.
The crop render confirms visually that it contains: panel letters **a–h**; the
`N^MitoDsRed α-Syn + M` header rule and title; the DNA / MitoDsRed / TOMM20 / DAPI channel legend;
the `Insets` column with rows i, ii, iii and their `mtDNA+`, `mtDNA-`, `mtDNA extruding` labels and
white arrowheads; the 5 µm and 10 µm scale bars; the `GM130 / STING / DAPI`, `NF-κB / DAPI`,
`IRF3 / DAPI` and `α-Syn` channel labels; all four graph panels with their y-axis titles, tick
labels, mean-value annotations, significance bars and the `SH-SY5Y: Control / α-Syn` group labels.
No caption text is inside the crop (the Fig. 8 caption is on page 17, as the asset map says).

**Methods prose.** Reading order was already correct (figure, then left column `b003`, then right
column `b004`). Two line-wrap hyphen losses fixed against the PDF text layer:

- `b004`: `[SigmaAldrich, D9542]` → `[Sigma-Aldrich, D9542]` (source prints `[Sigma-` / `Aldrich,`)
- `b004`: `Aqua-Poly/ Mount` → `Aqua-Poly/Mount` (Polysciences product name; break is after the `/`)

**Cross-page join set.** `p0016-b003` → `join_previous: "space"`. Page 15 `p0015-b014` ends
`…incubated in 50 mM ammonium chloride (NH4Cl [Sigma Aldrich, A0171]) solution for 15 min at` and
page 16 opens `RT to quench the fixative.` Verified in the source, not inferred.

Checked and correct as extracted: `9002-93-1`, `18606-20`, `1:500`, `1:1000`, `0.1% v/v`,
`2% w/v`, `1X DPBS`, `16 h`, `4 °C`, `5 min`, `1 h`.

---

## Page 17

**Item order was already true reading order** and was left unchanged: Fig. 8 caption left half
(`b002`) → Fig. 8 caption right half (`b003`) → full-width Fig. 9 image (`b004`) → Fig. 9 caption
left half (`b005`) → right half (`b006`) → left-column body (`b007`, `b008`, `b009`) →
right-column body (`b010`, `b011`, `b012`).

**1. Fig. 8 caption (`b002` + `b003`).** Verified word by word against the PDF spans.

- `b002`: fixed `from control or α- Syn-burdened` → `α-Syn-burdened`. The hyphen is the compound
  hyphen of "α-Syn", which happened to fall at a line end; the extractor inserted a space after it.
- `b003`: re-kinded from `text` to `caption` — it is the right-hand half of the same Fig. 8 legend,
  matching how `b005`/`b006` are both `caption` for Fig. 9.
- `b003`: removed the stray space the superscript extractor left before the full stop, twice:
  `1×10<sup>-15</sup> .` → `1×10<sup>-15</sup>.` and `4×10<sup>-15</sup> .` → `4×10<sup>-15</sup>.`

p-values checked against the source glyph by glyph:

| In source | Correct in JSON |
| --- | --- |
| `**p = 0.0029.` (panel d) | yes, two asterisks |
| `****p < 1×10` + superscript `-15` (panel f) | yes, **four** asterisks |
| `****p = 4×10` + superscript `-15` (panel h) | yes, **four** asterisks |

The task brief quoted these as `***p`; the printed page has four asterisks for f and h and two for
d, so I kept what is printed. Both exponents are real superscripts and remain `<sup>-15</sup>`.
`N = 3` / `n = 100` confirmed for d, f and h; both Mann-Whitney tests are "two-sided"; `×` is
U+00D7 throughout.

**2. Figure 9 (`b004`).** → `label: "Figure 9"`, `asset_name: "figure-9"`. bbox
`[56, 203, 545, 493]` kept. PDF content union for the band is `[61.4, 208.2, 539.6, 487.1]`
(raster schematic `[61.4, 208.2, 470.8, 487.1]` plus the live text block
"Clearance / + / Mild bystander inflammation - / Microglial priming" at `[461.2, 325.9, 539.6, 388.5]`
and the red dashed arrow at `[437.4, 326.6, 465.4, 331.3]`). The 10-pt-wider render shows nothing
sits outside the bbox. Present and unclipped: numbered steps 1–12, "Neuronal cells" and "Microglia"
labels at the top with their cell icons, "Nucleus" at bottom left, both "TNT" labels, the
NF-κB / IRF3 / P boxes, "10a. Cytokines" and "10b. Interferons", the bottom arrow, the red dashed
arrow and the "Clearance + Mild bystander inflammation - Microglial priming" text at the right.
Bottom edge 493 stops above the caption, which starts at y = 495.6 — no caption in the crop.

**3. Fig. 9 caption (`b005` + `b006`).** Fixed `neuronalderived` → `neuronal-derived` in `b006`
(compound hyphen lost at a line wrap). Kept the source's own misspelling **`mediatied`** verbatim.
BioRender attribution verified exactly: `Created in BioRender. MAYA, S. (2026)
https://BioRender.com/x5dad2t.`

**Headings demoted `#` → `##`:** `Mitophagy flux analysis` (`b008`), `qRT-PCR` (`b011`). Both are
Methods subsections (set in the source's subsection font, not the section font).

Checked and correct: `400 nM`, `Bafilomycin A1 (Sigma, SML1661)`, `4368814`, `1725124`, `1 μg`,
`20 ng per reaction`, `ΔΔCt`, `β-actin`, `9036-19-5`, `41105901`, `228549`, `1:5000`, `4 °C`.

---

## Page 18

### Table 1 — the qRT-PCR primer table: TRANSCRIBED

`p0018-b002` → `label: "Table 1"`, `asset_name: "table-1"`, `kind` stays `table`,
bbox `[37, 46, 297, 277]` kept, and `rows` populated as **9 rows × 3 columns of strings**, header
first. Each printed cell wraps over two typographic lines; I joined the two lines into one
continuous uppercase string with no space and no hyphen.

| Gene | Forward primer sequence | Reverse primer sequence |
| --- | --- | --- |
| IL-1β | CCACAGACCTTCCAGGAGAATG | GTGCAGTTCAGTGATCGTACAGG |
| TNF-α | CTCTTCTGCCTGCTGCACTTTG | ATGGGCTACAGGCTTGTCACTC |
| IL-6 | AGACAGCCACTCACCTCTTCAG | TTCTGCCAGTGCCTCTTTGCTG |
| CD68 | CGAGCATCATTCTTTCACCAGCT | ATGAGAGGCAGCAAGATGGACC |
| IFNα | AATGACAGAATTCATGAAAGCGT | GGAGGTTGTCAGAGCAGA |
| IFNβ | CAACTTGCTTGGATTCCTACAAAG | TATTCAAGCCTCCCATTCAATTG |
| CXCL10 | GGTGAGAAGAGATGTCTGAATCC | GTCCATCCTTGGAAGCACTGCA |
| CCL20 | AAGTTGTCTGTGTGCGCAAATCC | CCATTCCAGAAAAGCCACAGTTTT |

**How the bases were verified — three independent checks, all in agreement:**

1. **Zoomed render.** Three crops of the table region from `source.pdf` at 7x and 9x magnification
   (`tbl_top.png`, `tbl_bot.png`, `tbl_cd68.png`), read with the Read tool and transcribed by eye,
   base by base. At that magnification the glyphs are unambiguous; there was no base I could not
   read with confidence, so nothing had to be left out and nothing was guessed.
2. **PDF text layer.** Independently extracted the spans in the clip rect `[30, 40, 305, 285]` of
   page 18 with PyMuPDF. The text layer is clean (one span per printed half-line, embedded font
   `AdvOTdd63dae3`) and matches the visual transcription **character for character** on all 32
   half-lines. The visual read was done first; the text layer was used only to confirm it.
3. **Machine assertion.** Before writing, every joined sequence was asserted to consist only of
   `A`, `C`, `G`, `T` and every row asserted to have exactly 3 elements. The script fails loudly
   otherwise; it passed.

Sanity check, not used as a source: the joined IL-6 pair (`AGACAGCCACTCACCTCTTCAG` /
`TTCTGCCAGTGCCTCTTTGCTG`) and the TNF-α pair (`CTCTTCTGCCTGCTGCACTTTG` /
`ATGGGCTACAGGCTTGTCACTC`) are the standard published human primer pairs, which independently
confirms that the two printed lines per cell are a single wrapped sequence and that the join
direction is right.

**Note for the coordinator:** the gene symbols are italic in the source, but I wrote them **plain**
in `rows` (`IL-1β`, not `*IL-1β*`). `rows` is emitted as CSV, where literal asterisks would be data
corruption rather than formatting. Greek letters are preserved. The `markdown` field was also
regenerated to match `rows` (it is ignored for tables, but leaving the stale split-line version
would be confusing).

### Reading order fixed

The extractor had `TNT counting` (`b020`) and its paragraph (`b021`) *after* `References`, and the
right column's opening fragment `b007` before them. Items are now in true two-column order:

- header `b000`, `b001`
- **left column:** `b002` (table) → `b003` Western blotting → `b004` → `b005` α-Syn transfer assay
  → `b006` → `b020` TNT counting → `b021`
- **right column:** `b007` → `b008` Fixed-cell microscopy → `b009` → `b010` → `b011` FACS sample
  preparation and acquisition → `b012` → `b013` Quantification and statistical analyses → `b014` →
  `b015` Reporting summary → `b016` → `b017` Data availability → `b018` → `b019` References →
  `b022` (ref 1) → `b023` (ref 2)
- footer `b024`, `b025`

The left→right column join is mid-word by catalogue number: `b021` ends
`0.2 M HEPES buffer [Gibco, 15630-` and `b007` opens `080] in 1X DPBS)`. That hyphen is part of
catalogue number **15630-080**, not a line-wrap hyphen, so both halves keep it.

### Heading hierarchy (verified against the source's two heading fonts)

`##`: Western blotting, α-Syn transfer assay, TNT counting, Fixed-cell microscopy, FACS sample
preparation and acquisition, Quantification and statistical analyses, Reporting summary.
`#`: Data availability, References.
All were already at the right level in the extraction; I asserted rather than changed them.

### Text fixes

- `b004`: `50 mM-TrisHCI` → `50 mM-Tris-HCI` (compound hyphen lost at a line wrap). **The source
  really does print `HCI` with a capital letter I rather than `HCl`** — a typo in the published
  paper, kept verbatim. Flagging in case the coordinator prefers a silent correction.
- `b004`: `horseradish peroxidaseconjugated` → `horseradish peroxidase-conjugated`
- `b014`: `(https://icy. bioimageanalysis.org/plugin/manual-tnt-annotation/)` →
  `(https://icy.bioimageanalysis.org/plugin/manual-tnt-annotation/)` — the URL was broken by a
  line wrap after `icy.`
- `b014`: `FIJI<sup>100</sup> .` → `FIJI<sup>100</sup>.` and `FIJI<sup>101</sup> .` →
  `FIJI<sup>101</sup>.`
- `b021`: `protocols<sup>28,99</sup> .` → `protocols<sup>28,99</sup>.`
- `b022`, `b023`: italicised the journal titles — `*Cell Death Dis.*`, `*Science*`.

Checked and correct as extracted: `20 µg`, `95 °C`, `3-8% tris-acetate`, `11836170001`,
`cOmplete Mini, EDTA-free`, `1:5000`, `0.1% Tween-20`, `AI680`, `W32466`, `3.33 μg/mL`, `12 mm`,
`500 nM`, `G5882`, `A12380`, `1:250`, `63×/1.4`, `0.45 μm`, `0.133 μm`, `7 and 13 μm`, `40X`/`63X`,
`0.8x`/`1x` (lowercase x in the source for the zoom factors — kept), `"frame-fast"`,
`GraphPad Prism 10.0`, the em dash in `were used— fixative 1`, and the en dashes in `1–16` and
`1075–1079`.

---

## For the coordinator

1. **Document-wide: column fragments split mid-sentence.** The extractor emits each column of a
   paragraph as its own item, so a sentence that runs from the bottom of the left column to the top
   of the right column becomes two items. On my pages this affects:
   - p17 `b002` ends `…Statistical` / `b003` begins `significance was analyzed…`
   - p17 `b005` ends `…dependent on cofilin-` / `b006` begins `mediatied actin reorganization…`
     (a **word** split by a wrap hyphen)
   - p17 `b009` ends `…(mitophagosomes) or` / `b010` begins `TOMM20 and LAMP1…`
   - p18 `b021` ends `…[Gibco, 15630-` / `b007` begins `080] in 1X DPBS)`
   This is not specific to pages 16–18 — it is how every page in the document came out (e.g. p15
   `b002`/`b009`). **I deliberately did not merge them**, so my pages stay structurally consistent
   with the other 18. If the builder renders each item as its own paragraph, `cofilin-` /
   `mediatied` and `15630-` / `080]` will read as broken. This needs one document-wide decision
   (either an in-page continuation flag, or a merge pass) rather than three pages of local repair.
   I have fixed the *text* on my pages so that whichever way it is resolved, the characters are right.
2. **Exponent dash is genuinely inconsistent in the source.** Page 17 prints
   `****p < 1×10` + sup `-15` with a plain hyphen-minus and no space after `×`. Page 15
   (`p0015-b009`) prints `****p < 1× 10` + sup `–15` with an **en dash** and a space after `×`.
   Both are faithful to their own page. Do not normalise one to the other without re-checking.
3. **Asterisk counts.** The task brief described the Fig. 8 p-values as `***p`; the page prints
   `****p` for both 1×10⁻¹⁵ and 4×10⁻¹⁵, and `**p` for 0.0029. I followed the page.
4. **Superscript-plus-space artifact is document-wide.** The pattern `<sup>N</sup> .` (stray space
   before the following punctuation) appears on many pages, not just mine. I removed it on pages 17
   and 18 (5 occurrences). p15 `b004`, `b006`, `b009`, `b012` and most of pages 19–21 still have it;
   worth a global pass.
5. **Italic journal titles in references.** I italicised them for the two references on page 18
   (`*Cell Death Dis.*`, `*Science*`) per my brief. Pages 19–21 carry roughly 100 more references
   with the journal titles still plain, and the volume numbers are **bold** in the source on every
   reference (I left volumes plain to limit divergence). This needs to be applied consistently
   across the reference list or reverted on page 18.
6. **Table cells are not italicised** — see the note under Table 1 above.
7. **`HCI` vs `HCl`** on page 18 is a typo in the published paper; I kept it verbatim.
8. No asset-name conflicts: `figure-8` (p16), `figure-9` (p17), `table-1` (p18) match the fixed map,
   and `asset_category` was left unset on all three.
9. Header, footer and page-number `omit` items on all three pages were left exactly as they were.

## Limitations

- Figure and table *content* beyond what is printed (underlying data, raw images) cannot be checked
  from the PDF; I verified only that the crops are complete and the labels/values transcribed match.
- Page 16's Figure 8 and page 17's Figure 9 are single rasters with most of their internal labels
  baked into the image, so those internal labels cannot be corrected in text — they ride along in
  the crop. I confirmed visually that all of them are inside the crop.
- The `markdown` placeholder text inside the two `figure` items is the extractor's garbled
  "picture text" dump. It is ignored for figures, so I left it alone rather than hand-editing it.
