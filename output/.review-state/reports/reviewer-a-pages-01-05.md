# Reviewer A — pages 1–5

Document: `documents/s001-ebbd35bc-nc-alpha-syn-aggre-induce-mito-damage-a`

I visually inspected all five preview PNGs (`previews/page-0001.png` … `page-0005.png`) with the
image reader, plus ~15 zoomed crops (2×–7×) rendered from `source.pdf` with PyMuPDF into my own
scratch dir `/tmp/claude-0/-home-user-owner/2a8036d7-43c5-51a4-a12a-13d09f56561b/scratchpad/reviewer-a/crops/`.
Nothing was written inside `paper-review/` except the five assigned page JSONs. Pages 6 and 7 were
read only, for boundary checks. No build, no verify, no commit.

---

## Page 1

* **`p0001-b002` figure → `omit`.** It is the decorative journal masthead (red rule, "nature
  communications" wordmark, open-access icon). Set `reason`; **removed `label` and `asset_name`**
  so no stray `figure-p0001-002` asset is emitted.
* **`p0001-b004` "table" → three `text` items** in printed reading order:
  * `p0001-b004a` [39,256,190,334] — dates block. **Adds the line `Published online: 15 May 2026`,
    which the extractor dropped entirely**: it is a raster image (xref 108) in the PDF, not text.
    Also carries `Check for updates`.
  * `p0001-b004b` [217,256,509,300] — author list, superscripts as `<sup>1,2</sup>` etc., ORCID
    badges written as plain `(ORCID)` and the envelope on Zurzolo as `(corresponding author)`.
  * `p0001-b004c` [217,320,562,558] — the **abstract as ordinary prose** (no Markdown table).
    Line-wrap hyphens joined (`macro-molecules`→`macromolecules`), `ﬁ`/`ﬂ` ligatures normalised,
    and the spaces the extractor ate restored: `While α-synuclein`, `show that α-Syn`,
    `transfer of α-Syn`, `formation and α-Syn`, `Our findings`. En dashes kept in
    `cGAS–STING–NF-κB–IRF3`; `Neuron-to-microglia` is a hyphen in the source.
* Reading order now: masthead `omit`, running header, DOI, **title heading `p0001-b003`**, dates,
  authors, abstract, body, affiliations, footer. This matches the printed page (title at y≈113,
  masthead box at y≈255).
* **`p0001-b008`** — blockquote `>` removed; glued affiliation digits converted to
  `<sup>1</sup>Institut Pasteur, …` through `<sup>6</sup>These authors contributed equally…`,
  ending `e-mail: chiara.zurzolo@pasteur.fr`. Affiliation numbers verified 1–6 against a 3.6× crop.
* Gene symbols italicised per the source's italic font runs: `*SNCA*` in `p0001-b005`, `*SNCA*`,
  `*PARKIN*`, `*PINK-1*`, `*DJ-1*` in `p0001-b007`. Stray spaces before the period after
  `<sup>1–4</sup>`, `<sup>5,6</sup>`, `<sup>8–10</sup>`, `<sup>11,12</sup>` removed.
* Header/footer `p0001-b000/b001/b009` and page-number `omit` `p0001-b010` untouched.

## Page 2

* Two-column reading order **verified correct as emitted** — left `b002…b007` (including
  `# Results` and both `##` subsection headings), then right `b008…b011`. No interleaving.
* Heading hierarchy already correct: `Results` = `#`; "α-Syn aggregates localize to mitochondria
  and disrupt their morphology" and "α-Syn aggregates cause mitochondrial dysfunction" = `##`.
* Text fixes (15 replacements): stray space between every `<sup>ref</sup>` and the following
  `.`/`,`; `oligomeric α- Syn`→`α-Syn`; `mitochondrial damage— induced`→`damage—induced`;
  `α-Synburdened`→`α-Syn-burdened`; `neurodegenerationassociated`→`neurodegeneration-associated`;
  `TOMM20stained`→`TOMM20-stained`; `exposed to α- Syn`→`exposed to α-Syn`.
* Verified against raw PDF text that `α-Syn-mitochondria` and `neuron-astrocyte co-culture` are
  **hyphens**, while `α-Syn–TOMM20`, `glia<sup>27–29</sup>`, `Fig. 1f–h`, `1i–k`, `2d–f` and
  `neuron–microglia communication` are **en dashes**. ΔΨm, NF-κB, `16 h`, `TOMM20+` all correct.
* **Cross-page join set:** `p0002-b002` `join_previous: "space"` — page 1 ends
  "…translocate to the matrix in a concentration-dependent", page 2 opens "manner, leading to…".

## Page 3

* `p0003-b002`: `label` = **Figure 1**, `asset_name` = **figure-1**.
  bbox widened `[55,45,546,546]` → **`[48,42,552,547]`**. Verified on a 2× render of the bbox:
  panels a–d, all four panel letters (c and d sit at x≈64 pt, only 9 pt inside the old left edge),
  row labels "Original image"/"TOMM20 Threshold"/"Abundance:", every y-axis title, every rotated
  x-tick label and all six `10 µm` scale bars are inside, with margin. First caption baseline is at
  y = 548.5, so bottom 547 keeps the caption **out** of the crop.
* **Merged the Fig. 1 caption.** The extractor split it across columns: `p0003-b003` (left,
  `caption`) and `p0003-b004` (right, wrongly `text`). Merged into one `caption` item
  `p0003-b003` at `[39,548,562,657]`; **id `p0003-b004` removed.**
* Caption fix: `in a compactmanner` → `in a compact manner` (the PDF text layer drops the space;
  the page prints one). All p-values left exactly as printed — see the note below on glyphs.
  `N = 3`, `n = 50`, one-sided Brown-Forsythe and Welch ANOVA, Dunnett's T3, em dashes in
  `For c—mitochondrial count` / `For d—`, hyphen in `(c-d)` all confirmed.
* Stray `<sup> .` spaces removed here and in body items `b005`/`b006`. ΔΨm preserved.
* No cross-page join: page 2 ends on a complete sentence and `p0003-b005` starts a new paragraph.

## Page 4

* `p0004-b002`: `label` = **Figure 2**, `asset_name` = **figure-2**.
  bbox widened `[61,46,540,654]` → **`[52,42,548,658]`**. Verified on a 1.8× render: all 14 panels
  a–n, every panel letter, the rotated row labels SH-SY5Y / HMC3 / hN / hMG, the
  `Cytochrome c | TOMM20 | DAPI` and `MitoTracker Red | Cytochrome c | DAPI` channel legends, all
  y-axis titles and all `10 µm` / `5 µm` scale bars are inside. Body text starts at y = 669.4, so
  bottom 658 is clean. **Figure 2 has no caption on page 4** — it is on page 5, where I put it.
* Stray `<sup> .` spaces removed in `b003`/`b004`/`b005`. Reading order (left `b003`,`b004`, then
  right `b005`) verified.
* **Cross-page join set:** `p0004-b003` `join_previous: "space"` — see the caveat below.

## Page 5

* **Reading order fixed.** The extractor emitted the right-hand half of the full-width Fig. 2
  caption (`p0005-b008`) *after the entire left body column*. 
* **`p0005-b002` `text` → `caption`**, and merged with `p0005-b008` into a single caption item at
  `[39,45,562,190]`, placed at the top of the page before the body. **Id `p0005-b008` removed.**
  Body order is now left `b003…b007`, then right `b009…b013`.
* **Three headings demoted `#` → `##`** (all Results subsections):
  `p0005-b004` "α-Syn leads to BAX-mediated mtDNA release";
  `p0005-b006` "α-Syn activates the STING pathway and inflammation";
  `p0005-b012` "α-Syn-induced intercellular connections are dependent on mtDNA release and
  inflammation" (full two-line text verified against the page — it was already complete).
* Caption transcribed verbatim through `AU=arbitrary units.`: panel letters a–n, `N = 3`,
  `n = 100` / `n = 75` / `n = 58 control and 49`, Kruskal-Wallis with Dunn's multiple comparison,
  two-sided Mann-Whitney, `*p = 0.0169`, `***p = 0.0002`, every p-value exact.
* Text fixes: `twosided`→`two-sided`; `microglialcells`→`microglial cells` (verified at 7× that the
  page prints a space); `STINGTBK1`→`STING-TBK1`; `SHSY5Y`→`SH-SY5Y`; stray `<sup>` spacing.
  **`(Fig.3h, i)` left without a space** — verified at 7× that the page genuinely prints it closed
  up (a typo in the published article, not an extraction error).
* Verified em dashes in `STING—NF-κB and IRF3—revealed` and `For b—control-CCCP`; en dashes in
  `Fig. 4a–c`, `5a–f`, `5i–n`, `6a–c`, `6d–f`, `For f–k`; κ/β/α in NF-κB, IL-1β, TNF-α, IFNα, IFNβ.

---

## For the coordinator

1. **Caption-merge inconsistency with pages 6–7 (already reviewed).** I merged each column-split
   figure caption into one `caption` item (pages 3 and 5, removing ids `p0003-b004` and
   `p0005-b008`). Page 7 was reviewed the other way: `p0007-b002` and `p0007-b008` were both left
   as separate `caption` items and reordered. Page 7's split cuts mid-sentence
   ("…(bottom panels)" / "and microglial cells (e)."), which emits as two paragraphs. **Pick one
   convention and align page 7 (and any later page with the same split) with it.** I recommend the
   merge.
2. **`join_previous` deliberately NOT set on `p0005-b003`, and this needs a ruling.** The
   page 4 → 5 sentence break is genuine and mid-sentence: page 4 ends
   "…we performed co-immunostaining against TOMM20 and LC3 (to detect mitophagosomes;
   Supplementary Fig. 3a) and against TOMM20" and page 5 continues "and LAMP1 (to detect
   mitolysosomes; Supplementary Fig. 3d)…". But the full-width Fig. 2 caption must sit at the top
   of page 5, so it is emitted *between* them. If `join_previous` joins to the previous **emitted**
   item, setting it would glue body prose onto the end of the caption. Note the precedent on
   page 6: `p0006-b003` *does* carry `join_previous: "space"` with the Figure 3 image emitted
   before it — a figure emits no prose, so that case is harmless; mine is not. Please decide the
   builder semantics and set it if safe.
3. **`p0004-b003` `join_previous: "space"` is a paragraph join, not a mid-sentence one.** Page 3
   ends with a complete sentence ("…following α-Syn exposure."), but page 4's first line
   "Similar experiments in hNeurons and hMG also revealed a reduction of" is **flush left with no
   paragraph indent**, i.e. the same paragraph continues. I set `"space"` so the paragraph is not
   broken. Revert if the convention is strictly sentence-level.
4. **Mixed multiplication/minus glyphs in p-values are the source's own.** The published PDF
   really does mix them within one caption, e.g. on page 5: `p < 1x10−15` (U+2212),
   `p < 1x10-15` (hyphen), `p < 1× 10–15` (en dash, with a space after ×), `p = 7.008 × 10-10`;
   and on page 3 `p < 1x10−15` alongside `p = 4.798×10−12`. Per "p-values must match the source
   exactly" I transcribed them verbatim rather than normalising to `×` and `−`. This conflicts with
   the blanket "Multiplication sign ×, not letter x" typography rule — **if you want them
   normalised document-wide, say so and I/another pass can sweep them.**
5. **Page 1 `Published online: 15 May 2026` was invisible to the extractor** because it is a
   rasterised image. Worth checking whether any other page has image-only text (I found none on
   pages 2–5).
6. Minor, not changed: `p0001-b005` ends "…characterized by significant" and `p0001-b006` begins
   "loss of dopaminergic neurons…" — one paragraph split by the column break into two items.
   Same pattern at `p0002-b007`/`p0002-b008`. Nothing is dropped; they will just emit as two
   paragraphs. Flagging in case you want intra-page column joins handled too.

## Limitations

* `asset_category` left unset on figure-1 and figure-2, per the convention that all nine are
  main-article figures.
* I did not verify the supplementary-figure call-outs against the supplementary PDF (not supplied);
  they were transcribed as printed.
* Panel-internal text inside the figure crops (axis numbers, in-panel means) was read only well
  enough to confirm it is inside the bbox, not transcribed — the `markdown` of a `figure` item is
  ignored by the builder, so I left the extractor's picture-text comments as they were.
