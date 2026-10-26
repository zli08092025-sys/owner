# Reviewer B — pages 6–10

Paper: α-Synuclein aggregates induce mitochondrial damage and trigger innate immunity to drive
neuron–microglia communication (Nat Commun 2026;17:6462).

Files edited (only these):
`documents/s001-ebbd35bc-nc-alpha-syn-aggre-induce-mito-damage-a/pages/page-0006.json` …
`page-0010.json`. Pages 5 and 11 read for context only and left untouched (mtimes unchanged).

## Visual inspection

I read all five preview PNGs with the Read tool: `previews/page-0006.png`, `page-0007.png`,
`page-0008.png`, `page-0009.png`, `page-0010.png`. In addition I rendered zoomed crops from
`source.pdf` with PyMuPDF into my own scratch dir
(`/tmp/claude-0/-home-user-owner/2a8036d7-43c5-51a4-a12a-13d09f56561b/scratchpad/revb/`) to read
fine detail: the Fig. 3 caption at 6×, the right edge of the Fig. 4 figure at 7×, the left and
right edges of the Fig. 5 figure at 9×, and two page-9 body segments at 8×. Nothing was written
inside the paper-review directory.

Figure bboxes were verified numerically as well: for each figure page I computed the union of the
embedded image bbox (`page.get_image_info`), all vector overlay text, and all vector drawings, and
checked that union sits strictly inside the JSON bbox and strictly above the first body/caption
text line (y = 669).

## Page 6 — Figure 3 image

- `p0006-b002`: set `label` = `Figure 3`, `asset_name` = `figure-3` (was `figure-p0006-002`).
- Bbox `[92, 46, 510, 653]` **kept** — verified correct. Image box is `[106.9, 61.2, 504.4, 629.5]`;
  content union incl. vector overlays is `[97.7, 49.9, 504.4, 648.0]`. Inside the crop: panel
  letters a–j, rotated SH-SY5Y / HMC3 row labels (left edge x = 97.7), both Control/α-Syn column
  headers, the MitoTracker Red / dsDNA / TFAM / DAPI and TOMM20 / BAX-6A7 channel legends, the
  `MitoTracker Red | DNA-in | DNA-out` Imaris legend bar, the DNA−TFAM / DNA+TFAM inset labels,
  all 5 µm scale bars, both line-profile graph sets with axis labels and the blue-asterisk keys
  ("* mtDNA outside mitochondria"), and the panel j schematic. No caption text inside the crop
  (Fig. 3's caption is on page 7).
- `p0006-b003`: **kind was wrongly `caption`** (source_class "caption") although it is ordinary
  left-column body prose → changed to `text`.
- `p0006-b003`: `join_previous: "space"` — page 5 ends "…we first asked" and page 6 opens
  "whether inhibiting its release could prevent…".
- Body prose below the figure verified complete and in left-then-right order (b003 left, b004
  right); en dashes in "Fig. 6g–i" / "Fig. 7a–c" and `<sup>55</sup>`, `<sup>56,57</sup>` intact.
- `reviewed: true` + specific `review_notes`.

## Page 7 — Figure 3 caption + two subsection headings

- **The Fig. 3 caption is a two-column block spanning the top of the page.** The extractor split it
  into `p0007-b002` (left half, ends "…for neuronal cells (d)") and `p0007-b008` (right half,
  starts "and microglial cells (e)."). Both retyped `text` → **`caption`**, and `b008` was moved in
  the item list to sit directly after `b002`, ahead of the body prose, matching the printed layout.
  Side effect: this also repairs the body column continuity, since `b007` ("…To elucidate the") now
  runs directly into `b009` ("roles of TLR9 and RIG-1…").
- Caption verified verbatim against a 6× crop: panel letters a–j, `N = 3 independent experiments`,
  `n = 40 cells`, two-sided Mann-Whitney test, "For both (b, c): p < 1× 10-15", "Data represented as
  median and quartiles", the blue-asterisk note, "For h, i AU=arbitrary units", and the BioRender
  credit + URL.
- Headings demoted `#` → `##` (both are Results subsections, confirmed visually as bold run-in
  subheads, not section heads):
  - `p0007-b005` → `## Inflammation arises intracellularly and is independent of cell-surface receptors`
  - `p0007-b010` → `## Inflammation-induced connections enable functional interactions between neuronal cells and microglia`
- Line-wrap repairs that had destroyed **real compound hyphens** (verified line-by-line against the
  PDF's hyphenated line ends):
  | item | was | now |
  | --- | --- | --- |
  | b005 (heading) | `cellsurface receptors` | `cell-surface receptors` |
  | b004 | `abolished by cotreatment` | `abolished by co-treatment` |
  | b004 | `JSH23 (Fig. 5h, i)` | `JSH-23 (Fig. 5h, i)` |
  | b006 | `with α- Syn aggregates` | `with α-Syn aggregates` |
  | b008 | `in α-Synburdened cells` | `in α-Syn-burdened cells` |
  | b011 | `led to functionalTNT connections` | `led to functional TNT connections` |
  | b012 | `through the proinflammatory cytokines` | `through the pro-inflammatory cytokines` |
  | b012 | `promoting TNTmediated α-Syn transfer` | `promoting TNT-mediated α-Syn transfer` |
  | b013 | `or cotreated with JSH23.` | `or cotreated with JSH-23.` |
  ("cotreated" in b013 is printed as one unhyphenated word mid-line in the source and was left
  alone; only the `JSH-23` hyphen was restored. "co-treatment" / "co-cultured" are the paper's
  house forms — confirmed by mid-line occurrences elsewhere in the PDF.)
- Verified: `cGAS–STING–NF-κB` (en dashes, matches source), `(Fig. 5j—left panel` (em dash, matches
  source), ranges `8a–c`, `9d–f`, `10a–d`, Greek α/κ/β, superscript markers 58–68.
- No `join_previous`: page 6 ends on a complete sentence and page 7 opens with the caption.

## Page 8 — Figure 4 image

- `p0008-b002`: set `label` = `Figure 4`, `asset_name` = `figure-4`.
- Bbox `[90, 45, 510, 654]` **kept** — verified. Image box `[106.8, 53.1, 504.9, 648.9]`; content
  union `[96.0, 49.9, 504.9, 648.9]`. A 7× crop of x = 480–575 pt confirms the rightmost violin
  plots (panels b, c, k) end at ≈ 505 pt, i.e. inside the crop. Inside: panel letters a–k, rotated
  SH-SY5Y / HMC3 / hN / hMG labels, Control / diABZI / α-Syn column headers, GM130-STING-DAPI and
  GM130-pTBK1-DAPI channel legends, 5 µm and 10 µm scale bars, all axis labels including
  `pTBK1 area per cell (µm²)`, the **** brackets and the diABZI / α-Syn condition dot rows. No
  caption inside (Fig. 4's caption is on page 9).
- `p0008-b003`: **kind was wrongly `caption`** → changed to `text`; also
  `abolished upon cotreatment with JSH-23` → `abolished upon co-treatment with JSH-23`.
- `p0008-b003`: `join_previous: "space"` — page 7 ends "…increased total cofilin (Supplementary
  Fig. 10e," and page 8 opens "g), and an even stronger increase…".
- Body prose below the figure complete, left-then-right; `<sup>69</sup>` intact.

## Page 9 — Figure 4 caption + heading levels

- Same two-column caption split: `p0009-b002` (left half, ends "…per group. Statistical") and
  `p0009-b008` (right half, starts "significance was analyzed…"). Both retyped `text` →
  **`caption`**, and `b008` moved directly after `b002`. This also makes `b007` ("…from
  α-Syn–stressed neuronal") run straight into `b009` ("cells but also actively clearing them").
- Caption verified verbatim: panel letters a–k, `N = 3`, all per-group n values (140/139/141,
  85/85/82, 60, 50), two-sided Mann-Whitney, `****p < 0.0001`, the X/Y/Z compact p-value paradigm
  and every exponent. I confirmed from the span metrics that these exponents **are** true
  superscripts in the PDF (size 4.2 on a raised baseline), so `<sup>` is correct here.
- Fixed `For (k)—XY:` → `For (k)—X-Y:` (hyphen lost to a line-wrap repair; source reads "X-" / "Y").
- Body compound-hyphen repairs: `α- Syn transfer` → `α-Syn transfer` (b003);
  `α-Synburdened` → `α-Syn-burdened` (b006); `neuronalderived` → `neuronal-derived` and
  `K63ubiquitinated` → `K63-ubiquitinated` (b007); `α- Syn-burdened` → `α-Syn-burdened`,
  `cocultured` → `co-cultured` (×2) and `aggregateladen` → `aggregate-laden` (b011).
- **Heading levels confirmed, no change needed**: `p0009-b004` "Neuronal cells transfer damaged
  mitochondria to microglia" and `p0009-b010` "α-Syn-burdened neuronal cells prime microglia
  towards inflammation" are already `##`; `p0009-b013` "Discussion" is already `#` and is visibly
  set in the larger section-head style in the preview.
- `p0009-b003`: `join_previous: "space"` — page 8 ends "…(Supplementary Fig. 6j, k)," and this item
  opens "consistent with the reduced intercellular connections…". **See caveat below.**

## Page 10 — Figure 5 image

- `p0010-b002`: set `label` = `Figure 5`, `asset_name` = `figure-5`.
- Bbox `[78, 46, 524, 654]` **kept** — verified. Image box `[93.8, 66.1, 518.4, 648.8]`; content
  union `[83.7, 50.0, 518.4, 648.8]`. 9× crops of both edges confirm the rotated SH-SY5Y/HMC3
  labels begin at x = 83.7 pt (inside the left edge, with ~6 pt of margin) and the rightmost graph
  axis ends at x = 518.3 pt. Inside: panel letters a–j, all eight condition headers (Control,
  α-Syn, H-151, α-Syn + H-151, JSH-23, α-Syn + JSH-23, diABZI, diABZI + H-151, diABZI + JSH-23),
  the "Phalloidin DAPI" channel legends, 10 µm scale bars, `ns` / `****` brackets, the
  α-Syn / H-151 / JSH-23 / diABZI dot-matrix condition rows and the panel j schematic with its
  STING / IRF3 / NF-κB nodes and "Type I IFN" / "IL-6, TNF" labels.
- **Confirmed Fig. 5's caption is NOT on this page** — it is on page 11 (`p0011-b002`), consistent
  with the fixed asset map.
- `p0010-b003`: `join_previous: "space"` — page 9 ends "…have been very well established. Neuronal
  cells" and page 10 opens "can transfer α-Syn aggregates…".
- All three body paragraphs below the figure complete and in order: b003 (left), then b004 and b005
  (right); left column ends "…the cGAS-STING-NF-κB" and runs into b004 "signaling axis…".
  `<sup>27</sup>`, `<sup>28,29</sup>`, `<sup>25,26</sup>`, `<sup>42</sup>` intact.

## For the coordinator

1. **Cross-page joins I set** (all four checked against the printed source):
   - `p0006-b003` ← page 5 (`p0005-b013`): "…we first asked" + "whether inhibiting its release…"
   - `p0008-b003` ← page 7 (`p0007-b013`): "…(Supplementary Fig. 10e," + "g), and an even stronger…"
   - `p0009-b003` ← page 8 (`p0008-b004`): "…(Supplementary Fig. 6j, k)," + "consistent with the…"
   - `p0010-b003` ← page 9 (`p0009-b014`): "…Neuronal cells" + "can transfer α-Syn aggregates…"
2. **Caveat on those joins — please check how the builder resolves `join_previous`.** On every one
   of these pages a non-prose item is emitted between the two halves of the sentence: a `figure`
   on pages 6, 8 and 10, and the two-part Fig. 4 `caption` on page 9. If `join_previous` splices
   onto the immediately preceding *emitted* item rather than the preceding *prose*, these will glue
   body text onto a figure or a caption. I set them because the sentences genuinely continue, but
   this is the one decision in my range that needs your call.
3. **Two-column captions.** Figure captions in this paper are single blocks typeset across both
   columns, and the extractor split each into two items. I merged the halves by adjacency rather
   than by concatenating the strings, keeping the existing IDs: page 7 = `p0007-b002` +
   `p0007-b008`, page 9 = `p0009-b002` + `p0009-b008`. If you would rather have one item per
   caption, these are the pairs to fuse (the join is "…for neuronal cells (d)" + " " + "and
   microglial cells (e)." and "…per group. Statistical" + " " + "significance was analyzed…").
   **Page 5 and page 11 very likely have the same split** — `p0005-b002`/`p0005-b008` (Fig. 2) and
   `p0011-b002`/`p0011-b006` (Fig. 5) look like the same pattern, and on page 11 `p0011-b002` is
   still `kind: "text"`. Those are outside my range; flagging for whoever owns them.
4. **Source inconsistency in one p-value, left verbatim.** The Fig. 3 caption (page 7) prints
   `p < 1× 10-15` with the exponent **on the baseline** — I checked the span metrics and it really
   is 7.0 pt unraised text in the PDF, not an extraction failure. The same quantity on page 9 *is*
   a true superscript and is marked `<sup>`. I left page 7 verbatim per the "p-values must match
   the source exactly" rule. If you want document-wide consistency, page 7 would become
   `p < 1× 10<sup>-15</sup>`.
5. **"cGAS–STING–NF-κB" dash inconsistency in the source.** Page 7 prints en dashes
   (`cGAS–STING–NF-κB`); page 10's Discussion prints plain hyphens (`cGAS-STING-NF-κB`). Both
   JSONs now match their own page. Normalising to en dashes everywhere would be a deviation from
   the source — your call.
6. **Source typos I deliberately did not "fix"** (both confirmed on the printed page at 8×):
   `Supplementary Fig. 12h, I, k, l, n, o, q, r` (capital `I` where `i` is meant) and
   `p = 4,64 ×10–8` (comma used as decimal separator), both in page 9.
7. **No asset-name conflicts.** `figure-3`, `figure-4`, `figure-5` set exactly per the fixed map;
   `asset_category` left unset on all three so they route to `assets/figure/`.
8. Running headers (`Article`, the DOI) and the `Nature Communications | (2026) 17:6462` footer
   were left exactly as extracted on all five pages, and the page-number `omit` items were left
   alone, per the conventions.

## Limitations

- I verified text only against this main-article PDF; Supplementary figure references
  (Supplementary Figs. 6–12) could not be checked against the supplementary file, which is not in
  the review directory.
- Figure bboxes were verified to contain all content and to exclude caption/body text, but I did
  not render the actual JPEG crops the builder will produce, so I cannot confirm the final
  downsampled legibility of the smallest in-panel labels (e.g. the axis tick numbers in the page-8
  violin plots).
- Garbled `markdown` strings inside the three `figure` items were left as-is, since `markdown` is
  ignored for figures.
- I did not run the bundle build or verify, and made no git commit.
