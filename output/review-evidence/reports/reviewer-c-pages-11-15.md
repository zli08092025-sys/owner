# Reviewer C — pages 11–15

Document: `documents/s001-ebbd35bc-nc-alpha-syn-aggre-induce-mito-damage-a`
Pages edited: 11, 12, 13, 14, 15. Pages 10 and 16 read as context only, not modified.
All five preview PNGs (`previews/page-0011.png` … `page-0015.png`) were opened and
visually inspected, plus ~15 zoomed crops (4–6×) rendered from `source.pdf` with
PyMuPDF into my own scratch dir
(`/tmp/claude-0/-home-user-owner/2a8036d7-43c5-51a4-a12a-13d09f56561b/scratchpad/reviewer-c-scratch`).
Nothing was written inside `paper-review/`. No build, no verify, no commit.

Text was compared against a superscript-aware dump of the PDF text layer (spans under
7 pt flagged as super/subscript) so superscripts, subscripts and exact codepoints
(en dash vs em dash vs minus, × vs x, μ vs µ) could be checked rather than guessed.

---

## Page 11 — Fig. 5 caption + Discussion

- `p0011-b002` re-kinded `text` → `caption`.
- **Caption was split across both columns.** `p0011-b006` was the right-hand half of the
  same caption (it began mid-sentence: "…representation paradigm is" / "used: control = P…").
  I merged it into `p0011-b002`, widened the bbox to the full measure `[39, 49, 562, 226]`
  and **removed `p0011-b006`**. See "For the coordinator" below.
- Reading order fixed: headers → full-width caption → left column (`b003`, `b004`, `b005`)
  → right column (`b007`, `b008`, `b009`) → footer → page-number omit.
- Caption verified verbatim against the source, including panel letters a–j, `N = 3`,
  `n = 20–21 / 18-21 / 20-22`, the one-sided Brown-Forsythe and Welch One-Way ANOVA with
  Dunnett's T3, and every p-value: `5.57 × 10^-8`, `0.7503`, `0.9972`, `2.02 × 10^-9`,
  `< 1x10^-15`, `0.9309`, `0.9727`, `< 1× 10^-15`, `0.9997`, `0.9148`, `4.068 × 10^-9`,
  `3.18 × 10^-10`, `0.9163`, `0.2674`, `2.24 × 10^-8`, `3.36 × 10^-9`, `0.9989`, `0.9729`,
  `5.54 × 10^-11`, plus the BioRender credit.
- Caption repairs: `n = 1821` → `n = 18-21` (range dash dropped by the extractor);
  `P- R:` → `P-R:`; `phalloidinstained` → `phalloidin-stained`.
- Body repairs: `aggregatesinduced` → `aggregates-induced`; `of α- Syn` → `of α-Syn`;
  `tested —enabled` → `tested—enabled`; `alsobeen` → `also been` (confirmed "also been"
  on a 6× crop); `proinflammatory` → `pro-inflammatory`; `(JSH23)` → `(JSH-23)`.
- Removed the spurious space the extractor leaves between `</sup>` and the following
  comma/period (`<sup>70</sup> .` → `<sup>70</sup>.`), here and on all my pages.
- Deliberate source inconsistencies left verbatim: the paper really prints both
  `p < 1x10^-15` and `p < 1× 10^-15`, and both `For b—P-Q` (em dash) and `n = 20–21`
  (en dash). `in vitro` / `in vivo` are **not** italic in this paper — checked on a crop —
  so they were left upright.

## Page 12 — Figure 6 image

- `p0012-b002`: `label` = `Figure 6`, `asset_name` = `figure-6`; `asset_category` left
  unset (main-article figure).
- Bbox `[71, 46, 531, 654]` **kept** — verified by rendering exactly that rectangle at
  1.7×. It contains panels a–h, every panel letter, both micrograph blocks, every violin
  plot with its axis title, the diABZI / H-151 / JSH-23 condition rows, all significance
  bars, every `10 μm` scale bar, both
  `α-Syn WGA DAPI *HMC3 acceptor positive for α-Syn` legends, panel d's
  `SH-SY5Y^α-Syn ± STING modulators CM` label and the `(Secretion control)` line under h.
  No caption text inside the crop (Fig. 6's caption is on page 13). A content-extent scan
  of the region gives `[74.5, 50.0, 525.3, 648.9]`, i.e. inside the bbox with a small margin.
- Body prose under the figure preserved in left-then-right order and not swallowed by the crop.
- Repair: `α- Syn–stressed` → `α-Syn–stressed` (the en dash in `α-Syn–stressed` /
  `α-Syn–burdened` is genuine and was kept).

## Page 13 — Fig. 6 caption + start of Methods

- `p0013-b002` re-kinded `text` → `caption`; right-column half `p0013-b008` merged into it,
  bbox widened to `[39, 49, 562, 256]`, **`p0013-b008` removed**. Reading order fixed.
- Caption verified: panels a–h, `n = 25-26`, `106 / 177 / 92` cells, `n = 15`, `n = 24-25`,
  `n = 126 / 124 / 227 / 163 / 223 / 144 / 188 / 134`, `n = 14-16`, Kruskal-Wallis with
  Dunn's and Two-Way ANOVA with Šídák's, and every p-value.
- Caption repairs: `twosided` → `two-sided`; `+JSH23` → `+JSH-23`;
  `(TNFα + JSH23)` → `(TNFα + JSH-23)`; and three broken/missing superscripts —
  `5.64×10<sup>-</sup> 5` → `5.64×10<sup>-5</sup>`, `p < 1×10-15` → `p < 1×10<sup>-15</sup>`,
  `3.89×10-6` → `3.89×10<sup>-6</sup>`.
- `For h: PQ:` is **printed that way in the source** (no hyphen) — confirmed on a 6× crop
  and left verbatim.
- **Heading hierarchy was already correct on this page**: `# Methods` (top level) and
  `## Culture of cell lines`, `## Culture of hiPSC lines`, `## Microglia generation`.
  Verified against the page; no change needed.
- Methods reagents checked digit by digit: Euroclone ECB2000L, Sigma-Aldrich D6429,
  10% foetal calf serum, Eurobio Scientific CVFSVF00-01, 1% penicillin-streptomycin
  (Gibco, 15140-122; 100 units/mL), humidified CO2 at 37 °C, 0.05% Trypsin-EDTA
  (Gibco, 25300-054), Epredia CB00120RA120MNZ0, Ibidi GmbH 81156, passages 3–10,
  Matrigel (Corning, 354234), mTeSRTM1 (Stem Cell Technology, 85850), 80 ng/mL BMP-4
  (PeproTech, 120-05), StemProTM-34 SFM (Gibco™, 10639011), Cultek SV30010,
  Lonza LZBE17-605EU1, 80 ng/ml VEGF AF-100-20, 100 ng/ml SCF 300-07, 25 ng/ml FGF-2
  100-18B, 50 ng/ml Flt3-L (Humanzyme, HZ-1151), 50 ng/ml IL-3 200-03, 5 ng/ml TPO 300-18,
  50 ng/ml M-CSF 300-25, 25 ng/ml GM-CSF 300-03, every 3-4 days, day 35,
  70 μm Filcon™ Syringe-Type mesh (BD Biosciences, 10271120). All match.
- Repairs: `gap junctionmediated` → `gap junction-mediated`;
  `damageinduced` → `damage-induced`; `actinchromobody-RFP` → `actin-chromobody-RFP`;
  `penicillinstreptomycin` → `penicillin-streptomycin`; `fixedcell` → `fixed-cell`;
  `SyringeType` → `Syringe-Type`; `CO2` → `CO<sub>2</sub>` (subscript confirmed by font size).
- `mTeSRTM1` and `StemProTM-34` really are printed with full-size "TM" (unlike `Gibco™`
  two lines later) — confirmed on a 6× crop, kept verbatim. `(PeproTech,200-34)` on p14
  likewise has no space in the source.

## Page 14 — Figure 7 image + "Neuron generation"

- `p0014-b002`: `label` = `Figure 7`, `asset_name` = `figure-7`; `asset_category` unset.
- Bbox `[97, 46, 504, 654]` **kept** — rendered and inspected at 1.9×, plus a dedicated 4×
  crop of panel j, whose `SH-SY5Y culture paradigm:` label sits closest to the left edge
  and is fully inside. The crop holds panels a–j with all letters, the rotated
  `N^MitoDsRed + M` / `N^MitoDsRed α-Syn + M` row labels, the WGA/MitoDsRed/DAPI,
  TOMM20/MitoDsRed/DAPI and `α-Syn MitoDsRed LAMP1 DAPI` legends, every `10 μm` scale bar,
  pie charts e/f with `Isolated mitochondria` / `Overlap with host network` and
  `Total=148` / `Total=169`, the `Orthogonal views` insets with XZ/YZ labels, and all
  violin-plot axis titles. No caption text inside (Fig. 7's caption is on page 15).
  Content-extent scan: `[102.8, 49.9, 498.2, 648.8]`.
- **`# Neuron generation` → `## Neuron generation`** (Methods subsection).
- Repair: `24well plate` → `24-well plate`.
- `centrifuged at 300 x g` is printed with a **letter x** in the source while the right
  column uses `800 × g`; both left exactly as printed (verified on a 6× crop). `GibcoTM`
  here is likewise full-size TM in the source.
- Body prose below/beside the figure preserved in left-then-right order.

## Page 15 — Fig. 7 caption + three Methods subsections

- `p0015-b002` re-kinded `text` → `caption`; right-column half `p0015-b009` merged into it,
  bbox `[39, 49, 562, 226]`, **`p0015-b009` removed**. Reading order fixed.
- Caption verified: panels a–j, `n = 35 / 47 / 21 / 22`, `74 / 185 / 30 / 34`, `n = 50`,
  `n = 48-50`, `n = 50 cells per group`, `ns: p = 0.6621`, `****p < 1×10^-15`,
  `ns: p = 0.5655`, `***p = 0.000145`, `*p = 0.0109`, `****p < 1× 10^-15`,
  Uncorrected Fisher's LSD and Mann-Whitney.
- Caption repairs: `in coculture` → `in co-culture`; `α- Syn-burdened` → `α-Syn-burdened`;
  `MannWhitney` → `Mann-Whitney`; and five `(N<sup>MitoDsRed</sup> α-Syn` → `…</sup>α-Syn`
  (the source prints no space there, though it does print one in `N^MitoDsRed + M`).
- **Three headings demoted `#` → `##`**: `Preparation of α-Syn aggregates`,
  `Reagents and primary antibodies`, `Immunocytochemistry`.
- **Three catalogue/antibody errors fixed** (these were the materially misleading ones):
  - `HY148045` → `HY-148045` (TLR9-IN-1, MedChemExpress)
  - `PA517752` → `PA5-17752` (phospho-Ser3-Cofilin, Invitrogen)
  - `phosphoSer172-TBK1` → `phospho-Ser172-TBK1`
- Other repairs: `POLAMcoated` → `POLAM-coated`; `X0551100` → `X0551-100`;
  `NH4Cl` → `NH<sub>4</sub>Cl` (subscript confirmed by font size);
  `InvitroFit<sup>TM</sup> ,` → `InvitroFit<sup>TM</sup>,` (3×).
- Every remaining reagent/dilution checked against the page and found correct, including
  diABZI (SelleckChem, S8796; 2.5 μM/2 h), H-151 (inh-h151; 0.5 μg/mL/16 h, 24 h for
  transfer), JSH-23 (Sigma, J4455; 10 μM), G140 (inh-g140; 10 μM), ABT-737 (Sigma, 197333;
  10 μM for 6/12/24 h), Q-VD-OPh (Sigma, 551476, 10 μM), BAI1 (HY-103269, 1 μM then 100 nM/16 h),
  IL-1α (Sigma, I2778; 3 ng/mL), IL-1β (Sigma, H6291; 20 ng/mL), TNF-α (Merck Millipore,
  654205; 50 ng/mL), TAK-242 (Tocris, 6587; 10 μM), TL2-C29 (inh-C29; 100 μM),
  RIG012 (HY-147124, 0.1 μM), LLOMe (Sigma, L7393; 1 mM), CCCP (Sigma, C2759; 20 μM),
  MitoTracker Red CMX Ros (M7512; 500 nM/30 min/37 °C), TMRM (T668; 100 nM/30 min/37 °C),
  and the full antibody list with its 1:50 / 1:100 / 1:400 / 1:500 / 1:1000 / 1:5000 dilutions.
  `−80 °C` / `−20 °C` use a true minus sign; `5 s "on" / 2 s "off"` curly quotes intact;
  500 nM and 200 nM fibril concentrations correct.
- Normalised one MICRO SIGN (U+00B5) in `SB431542 10 µM (TOCRIS, 301836-41-9)` to Greek mu
  (U+03BC) so every μ in these pages is one codepoint. The source genuinely mixes the two.
- `Escherichia coli BL21 (DE3)` is **not italic** in the source (checked on a 5.5× crop), so
  it was left upright.

---

## For the coordinator

1. **Split captions were merged, and two item IDs were deleted.** `p0011-b006`,
   `p0013-b008` and `p0015-b009` no longer exist; their text now lives at the end of
   `p0011-b002`, `p0013-b002` and `p0015-b002` respectively, each now `kind: "caption"`
   with a full-width bbox. Every figure caption in this paper is typeset as one block
   across both columns and the extractor split each one at the column gutter, so
   **pages 5, 7, 9, 17 and 18 almost certainly have the same problem** (`p000N-bXXX` left
   half + a right-column sibling). If other reviewers left theirs as two items, the caption
   will be emitted as two paragraphs broken mid-sentence. Worth reconciling to one policy.
   IDs remain unique document-wide (checked across all 21 pages).

2. **No `join_previous` could be set anywhere in pages 11–15.** The builder
   (`reading_package.py`) joins onto `pieces[-1]` and raises unless both the item and the
   *immediately preceding emitted item* are `text`/`caption`. Every page in my range opens
   with either a caption or a figure, so the real cross-page continuations are unreachable:
   - p10 `b005` ends "…leading to extensive lysosomal damage. Besides" → p11 `b003`
     "lysosomes, α-Syn has been reported…" — blocked by the Fig. 5 caption at the top of p11.
   - p11 `b009` ends "…genetic deletions of cGAS" → p12 `b003` "or STING will better
     elucidate…" — blocked by the Figure 6 image.
   - p12 `b005` ends "…could arise because of a" → p13 `b003` "pro-inflammatory environment
     caused by…" — blocked by the Fig. 6 caption.
   - p13 `b014` ends "…Cells were counted and" → p14 `b003` "centrifuged at 300 x g…" —
     blocked by the Figure 7 image.
   - p14 `b005` ends "…Proneural [DMEM/F12 (Life, 21331-20)" → p15 `b003` "and Neurobasal
     (Life, 21103-049)—1:1…" — blocked by the Fig. 7 caption.
   - p15 `b014` ends "…solution for 15 min at" → p16 `b003` "RT to quench the fixative." —
     blocked by the Figure 8 image (page 16 is not mine).
   All six are genuine mid-sentence breaks, confirmed in the source. This is a structural
   consequence of the "caption at the top of its page" rule and of figure-page layout, not
   something I could fix inside one page. If you want these joined, it needs a
   builder-level change or a different item ordering, and it should be decided once for
   the whole document.

3. **Within-page column continuations are also mid-sentence but I did not join them**,
   because the brief scoped `join_previous` to page breaks. I did reorder items so each
   pair is now adjacent, making a later pass trivial:
   p11 `b005`→`b007` ("…nuclear DNA" / "damage has also been linked…"),
   p12 `b004`→`b005` ("…TNT-mediated transfer to" / "microglia likely serves…"),
   p15 `b008`→`b010` ("…STING activator—" / "diABZI (SelleckChem— compound 3…").
   Same pattern exists on essentially every text page of the paper. Your call whether to
   apply `join_previous: "space"` document-wide.

4. **A document-wide extraction artifact I fixed only on my pages**: the extractor emits
   `<sup>NN</sup> ,` / `<sup>NN</sup> .` with a space before the punctuation. I stripped it
   on 11–15. It is present on every page that carries reference markers.

5. **Panel letters are not bolded** in the markdown (the source prints `a`, `b`, `c` … in
   bold). I left them plain to match the rest of the extraction rather than diverge on five
   pages. Same for the italic `p` in p-values and the italic `g` in `300 x g` / `800 × g`.
   Flagging in case you want a uniform policy.

6. **Asset names**: `figure-6` (page 12) and `figure-7` (page 14) set per the fixed map; the
   extractor's placeholders `figure-p0012-002` / `figure-p0014-002` are gone. No conflicts
   with other pages. `asset_category` deliberately left unset on both.

## Limitations

- Figure bboxes were validated by rendering the exact rectangle and by a PyMuPDF
  content-extent scan, but graph panels are embedded raster images, so a label painted
  inside a raster at its very edge cannot be measured programmatically — I checked those
  visually instead (panel d's CM label on p12, panel j's axis labels on p14).
- Italic/bold runs cannot be read from font names in this PDF (all fonts are anonymised
  subsets such as `AdvOTdd63dae3`), so every italics question was settled by eye on a
  zoomed crop rather than from metadata.
- I did not verify the figure *contents* against the caption's panel descriptions beyond
  confirming that each lettered panel named in the caption is present in the crop.
