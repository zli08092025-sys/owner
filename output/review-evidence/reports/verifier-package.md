# Independent verification — alpha-syn-mito-tnt-paper

Verifier: independent agent (not one of the five page reviewers, not the coordinator).
Package: `/tmp/claude-0/-home-user-owner/2a8036d7-43c5-51a4-a12a-13d09f56561b/scratchpad/staging2/alpha-syn-mito-tnt-paper`
Source: `.../paper-review/documents/s001-ebbd35bc-nc-alpha-syn-aggre-induce-mito-damage-a/source.pdf` (21 pp.)
Nothing in the package or the review directory was modified. No build or verify was run. Renders were written only to my own scratch dir.

## Verdict by check

| # | Check | Result |
|---|---|---|
| 1 | Structural integrity (21 pages, order, no furniture) | **PASS** |
| 2 | Figure/caption pairing (9 figures) | **PASS** |
| 3 | Figure crops (9 JPEGs) | **PASS** |
| 4 | Primer table `table-1.csv` | **PASS** — all 16 primers base-exact |
| 5 | 29 repaired seams | **PASS** (plus a full 261-hyphen audit, clean) |
| 6 | Deep text comparison, pages 1 / 5 / 15 / 18 / 20 | **PASS** with 2 cosmetic notes |
| 7 | Navigation index headings | **1 defect** (`Document beginning`) |

---

## 1. Structural integrity — PASS

Method: extracted the full PDF text layer per page, normalised both sides (ligatures folded, non-alphanumerics stripped, case folded) and ran 100-character sliding windows at 50-character steps in **both directions** — every PDF page's prose against `paper.md`, and all of `paper.md` back against the PDF. Full coverage, no gaps.

- All 21 pages are represented. Every residual window "miss" sits exactly on a block junction (a heading inserted between two blocks, or a figure link/caption relocated by the reading order) or is text baked into a figure graphic (pages 3, 4, 6, 8, 10, 12, 14, 16 — e.g. Fig. 3's `* mtDNA outside mitochondria` legend, Fig. 5j's schematic labels). No prose is missing.
- **Order is strictly monotonic.** The first prose line of each PDF page lands at a strictly increasing offset in `paper.md` (p1 → 801, p2 → 2753, p3 → 9538, … p20 → 71031, p21 → 76390). No page is out of sequence.
- **No duplication.** A 120-character repeated-substring scan found only 5 hits, all inside the Fig. 5 caption, where the journal genuinely repeats the same boilerplate ("Statistical significance was analyzed using one-sided Brown-Forsythe and Welch One-Way ANOVA and Dunnett's T3 multiple comparison. To indicate p-values in a compact manner…") for panel pairs b/c and e/f.
- **Page furniture is absent.** Zero occurrences of the running header `Article` (`grep -c 'Article'` → 0), zero occurrences of the footer `Nature Communications | (2026) 17:6462`, zero bare page numbers, zero `1234567890():,;` artefacts. The DOI appears only twice, both legitimately: inside the printed **Additional information** section ("The online version contains supplementary material available at…") and in the package's own Conversion notes.
- Reference numbering is complete and gapless, 1 to 101.
- All internal links resolve: `SKILL.md` → `references/index.md`; `index.md` → `paper.md`, `supplement.md`; `paper.md` → the nine `assets/figure/figure-N.jpg` and `assets/table/table-1.csv`.

## 2. Figure/caption pairing — PASS

All nine links are followed, after exactly one blank line and with nothing else between, by the matching caption:

| Figure | link line | caption line | caption opens |
|---|---|---|---|
| 1 | 39 | 41 | `Fig. 1 \| α-Syn aggregates alter mitochondrial morphology.` |
| 2 | 47 | 49 | `Fig. 2 \| α-Syn exposure compromises mitochondrial functionality.` |
| 3 | 69 | 71 | `Fig. 3 \| α-Syn induces BAX-mediated mtDNA release in the cytoplasm.` |
| 4 | 89 | 91 | `Fig. 4 \| α-Syn aggregates activate STING.` |
| 5 | 113 | 115 | `Fig. 5 \| α-Syn-induced intercellular connections are inflammation-dependent.` |
| 6 | 127 | 129 | `Fig. 6 \| Inflammation promotes α-Syn spread to microglia via TNTs.` |
| 7 | 155 | 157 | `Fig. 7 \| Neuronal cells transfer damaged mitochondria to microglial cells for degradation.` |
| 8 | 179 | 181 | `Fig. 8 \| mtDNA status of transferred mitochondria and bystander inflammation.` |
| 9 | 183 | 185 | `Fig. 9 \| Working model.` |

Each caption is the right one for its figure (content cross-checked against the panel contents of the JPEG). Every figure link sits at a paragraph boundary, never mid-paragraph.

**Caption text is byte-faithful.** I normalised each caption and the PDF text layer and confirmed all nine captions are present in full — Fig. 1 (1254 normalised chars), 2 (1628), 3 (1125), 4 (1490), 5 (2160), 6 (2453), 7 (2238), 8 (1638), 9 (608) — with every line-break hyphen inside them resolved correctly (checked individually: `two-sided`, `X-Y`, `18-21`, `α-Syn-burdened`, `cofilin-mediatied` all correctly kept; `Morphological ana-lysis`, `Quantifica-tion`, `inflamma-tion`, `Statistical sig-nificance`, `mito-chondrial` etc. all correctly joined).

## 3. Figure crops — PASS

I read all nine JPEGs and compared each against its source page, and separately computed each figure's true extent on the page (raster bounding box unioned with the live text that belongs to the figure — panel letters, rotated axis titles, schematic labels) and compared aspect ratios.

| Fig | PDF page | figure extent on page | extent ratio | crop ratio | panels in caption | verdict |
|---|---|---|---|---|---|---|
| 1 | 3 | x[60.5, 540.5] y[50.1, 540.7] | 0.978 | 0.998 | a–d | complete |
| 2 | 4 | x[66.1, 534.8] y[50.1, 648.8] | 0.783 | 0.805 | a–n | complete |
| 3 | 6 | x[97.7, 504.3] y[49.9, 648.0] | 0.680 | 0.688 | a–j | complete |
| 4 | 8 | x[96.6, 504.9] y[49.9, 648.9] | 0.682 | 0.689 | a–k | complete |
| 5 | 10 | x[85.1, 518.3] y[50.0, 648.8] | 0.723 | 0.734 | a–j | complete |
| 6 | 12 | x[83.4, 525.3] y[50.0, 648.9] | 0.738 | 0.757 | a–h | complete |
| 7 | 14 | x[103.8, 498.2] y[49.9, 648.8] | 0.659 | 0.670 | a–j | complete |
| 8 | 16 | x[60.7, 540.5] y[48.6, 644.8] | 0.805 | 0.812 | a–h | complete |
| 9 | 17 | x[61.4, 539.6] y[208.2, 487.0] | 1.715 | 1.685 | schematic | complete |

Every crop is slightly *larger* than the figure's content extent — i.e. every one carries margin, none clips. Specifically confirmed present and uncut:

- **Fig. 1**: panel letters a/b; the `SH-SY5Y` / `HMC3` column headers above them; the rotated `Original image` and `TOMM20 Threshold` row labels; all six `10 µm` scale bars; the `Abundance:` cartoon row; all `****` significance bars; all rotated `Control / CCCP / α-Syn` x-labels on the bottom (d) row; all y-axis titles including `Mean Aspect Ratio (AU)` on the far right.
- **Fig. 2**: all 14 panels a–n; `TMRM`, `Cytochrome c TOMM20 DAPI` and `MitoTracker Red / Cytochrome c / DAPI` channel legends; `hN` / `hMG` row labels; `5 µm` and `10 µm` bars; panel n's full chart at the right edge.
- **Fig. 3**: `MitoTracker Red / dsDNA / TFAM / DAPI` legend, `DNA-in / DNA-out` legend, `Imaris 3D` labels, all line-profile charts with both axis titles, the `* mtDNA outside mitochondria` footnotes, and panel j's full schematic including the bottom-most `Mitochondrial damage (MOMP)` label.
- **Fig. 4**: a–k, the `diABZI / α-Syn` filled-circle condition matrices under every chart.
- **Fig. 5**: a–j, including the whole panel j schematic with its right-hand text block `STING activation + NF-κB inhibition – prevents intercellular connections`.
- **Fig. 6**: a–h, including the bottom-most two lines `SH-SY5Y^α-Syn ± Cytokines CM ▶ HMC3` / `(Secretion control)` (verified against a render of the page's bottom band).
- **Fig. 7**: a–j, including panel j's `SH-SY5Y culture paradigm:` row label and both category labels.
- **Fig. 8**: the `N^MitoDsRed α-Syn + M` title above panel a, the `i / ii / iii` inset column with its `mtDNA+ / mtDNA- / mtDNA extruding` labels, and panels c–h with the `SH-SY5Y:` condition rows.
- **Fig. 9** (schematic, checked label by label): numbered steps **1, 2, 3, 4, 5, 6, 7, 8, 9, 10a, 10b, 11, 12 all present and uncut**, plus `Neuronal cells`, `Microglia`, both `TNT` labels, `Nucleus`, `NF-κB`/`IRF3` boxes with their `P` badges, `Type I IFN`, `IL-6, TNF`, and the right-hand text `Clearance` / `+` / `Mild bystander inflammation - Microglial priming` (which lies *outside* the embedded raster — x out to 539.6 — and the crop correctly extends to include it).

**No caption text is inside any crop.** Checked tightest case: Fig. 1's caption block starts at y = 549.2 and the figure ends at y = 540.7; the crop stops in the gap.

## 4. Primer table — PASS (base-exact)

Verified twice: against the PDF text layer, and visually against a 7× render of the page-18 table region (two crops, header+rows 1–3 and rows 4–8).

Header row `Gene,Forward primer sequence,Reverse primer sequence` matches the printed `Gene` / `Forward primer sequence` / `Reverse primer sequence`.

Every cell wraps across two printed lines; all 16 joins verified base by base:

| Gene | printed line 1 + line 2 (forward) | CSV | printed line 1 + line 2 (reverse) | CSV |
|---|---|---|---|---|
| IL-1β | `CCACAGACCTTCCAGG` + `AGAATG` | ✓ `CCACAGACCTTCCAGGAGAATG` | `GTGCAGTTCAGTG` + `ATCGTACAGG` | ✓ `GTGCAGTTCAGTGATCGTACAGG` |
| TNF-α | `CTCTTCTGCCTG` + `CTGCACTTTG` | ✓ | `ATGGGCTACAGG` + `CTTGTCACTC` | ✓ |
| IL-6 | `AGACAGCCACT` + `CACCTCTTCAG` | ✓ | `TTCTGCCAGTG` + `CCTCTTTGCTG` | ✓ |
| CD68 | `CGAGCATCATT` + `CTTTCACCAGCT` | ✓ | `ATGAGAGGCAGCAAG` + `ATGGACC` | ✓ |
| IFNα | `AATGACAGAAT` + `TCATGAAAGCGT` | ✓ | `GGAGGTTGT` + `CAGAGCAGA` | ✓ |
| IFNβ | `CAACTTGCTTGGA` + `TTCCTACAAAG` | ✓ | `TATTCAAGCCT` + `CCCATTCAATTG` | ✓ |
| CXCL10 | `GGTGAGAAGAGAT` + `GTCTGAATCC` | ✓ | `GTCCATCCTTGGAA` + `GCACTGCA` | ✓ |
| CCL20 | `AAGTTGTCTG` + `TGTGCGCAAATCC` | ✓ | `CCATTCCAGA` + `AAAGCCACAGTTTT` | ✓ |

No base dropped, added, transposed or misread; no stray separator at any join; gene names exact (Greek β/α preserved, italics dropped as expected for CSV). The same eight rows are also mirrored as an inline Markdown table at `paper.md:197–205` and that copy is identical to the CSV.

## 5. The 29 seams — PASS

All 29 fragments from `seams.txt` were located in `paper.md` as continuous prose, with exactly one space at `[ ]` joins and no space at `[]` joins, no doubled space, no lost or invented hyphen. (Seam 1 is a true match; it only looked like a miss in my first automated pass because the fragment begins inside a `</sup>` tag — `…protein<sup>7</sup>, characterized by significant loss of dopaminergic neurons…` is correct at `paper.md:19`.)

The two no-space joins are both right:
- #24 `STING activator—` + `diABZI` → `STING activator—diABZI`, consistent with the same paragraph's `STING inhibitor—H-151`, `pan-caspase inhibitor—Q-VD-OPh`, `TLR4 inhibitor—TAK-242`.
- #28 `[Gibco, 15630-` + `080]` → `15630-080`, a real Gibco catalogue number.

**Beyond the 29, I audited every line-break hyphen in the whole document**: 261 occurrences, of which the package joined 189 and kept the hyphen in 71. Every one of the 261 is right. The 71 kept are all genuine compounds or identifiers (`α-Syn`, `two-sided`, `SH-SY5Y`, `X-Y`, `18-21`, `K63-ubiquitinated`, `gap junction-mediated`, `damage-induced`, `aggregates-induced`, `re-organization`, `Filcon™ Syringe-Type`, `Tris-HCI`, `15630-080`, `X0551-100`, `HY-148045`, `PA5-17752`, `phospho-Ser172`, `PID2022-139546OB`, `cofilin-mediatied`, and the split exponent `5.64×10-` + `5` → `5.64×10⁻⁵`). The single case where neither form appears in the package (`mtDNA-` / `mtDNA+`) is figure-embedded text inside the Figure 8 artwork, correctly not in the prose.

## 6. Deep text comparison on five sampled pages — PASS, 2 cosmetic notes

Method per page: word-level `difflib` alignment plus, document-wide, a character-class census (counts of `–` `—` `−` `×` `µ` `μ` `β` `κ` `α` `Δ` `Ψ` `™` `°` `’` `“` `”` and accented letters) in package vs PDF, and a full superscript/subscript audit driven by PDF span font sizes.

**Page 1** — title (en dash in `neuron–microglia` ✓), `Received: 14 July 2025`, `Accepted: 1 May 2026`, `Published online: 15 May 2026` (rasterised on the page; present and correct), `Check for updates`, the full author line and all six affiliation footnotes, `e-mail: chiara.zurzolo@pasteur.fr`, the whole abstract and the first two body paragraphs. Reference superscripts exact: `1–4`, `5,6`, `7`, `8–10`, `11,12` (en dashes, not hyphens). Gene italics `SNCA`, `PARKIN`, `PINK-1`, `DJ-1` all present. Ligature `Membrane Trafﬁc` correctly rendered `Membrane Traffic`.

**Page 5** — whole page verbatim, including the Fig. 2 caption. All p-values match the page character for character, mixed notation and all: `p < 1x10⁻¹⁵` (U+2212 minus) then `p < 1x10⁻¹⁵` (hyphen) in the same sentence; `p = 1.8x10-13`; `p < 1× 10–15`; `p < 1×10–15`; `p < 1 × 10–15`; `p = 7.008 × 10-10`. All `N = 3` / `n = 100` / `n = 75` / `n = 58 control and 49 α-Syn-treated` values match. `*p = 0.0169, ***p = 0.0002` match. Reference markers 42, 49–57, 50, 51, 52,53, 54, 58, 59, 60, 61 match. `(Fig.3h, i)` with the printed missing space after `Fig.` is preserved.
*Note:* the PDF text layer renders `microglialcells` on this page; the package writes `microglial cells`. I rendered the line at 9× — **the page prints a space**, so the package is right and the text layer is at fault.

**Page 15** — whole page verbatim, including the Fig. 7 caption. Catalogue numbers all exact: `21331-20`, `21103-049`, `17502048`, `12587-010`, `X0551-100`, `0503`, `31350-010`, `P4957`, `L2020`, `120-10 C`, `301836-41-9`, `100-45`, `100-25`, `17504-044`, `354234`, `450-02`, `450-10`, `S8796`, `inh-h151`, `J4455`, `inh-g140`, `197333`, `551476`, `HY-103269`, `I2778`, `H6291`, `654205`, `6587`, `inh-C29`, `HY-148045`, `HY-147124`, `L7393`, `C2759`, `M7512`, `T668`, `sc-17764`, `556432`, `690014`, `PA5-29571`, `610823`, `PA5-23381`, `D52C2`, `51-0500`, `Ma5-15160, T.849.2`, `D6I4C`, `E7J8G`, `sc23959`, `D11`, `H4A3`, `PA5-17372`, `PA5-17752`, `G9545`, `15710`, `A0171`. All concentrations/durations and all dilutions (`1:400`, `1:100`, `1:50`, `1:500`, `1:1000`, `1:5000`) match. `−80 °C` / `−20 °C` use U+2212 as printed. `InvitroFit^TM` correctly superscripted (verified at 11× — the page sets TM raised there, unlike `mTeSRTM1`/`StemProTM-34`/`GibcoTM` which really are full-size and are reproduced full-size).
*Note 1 (cosmetic):* the page's `SB431542 10 µM` uses MICRO SIGN U+00B5; the package writes GREEK SMALL LETTER MU U+03BC. Visually identical in the render; the package does preserve U+00B5 elsewhere (`Proteins (20 µg)`, p. 18), so this is a one-off inconsistency, not a misreading. **Low severity.**
*Note 2:* the PDF text layer renders `Alexa Fluor™488`; the package writes `Alexa Fluor™ 488`. Rendered at 11× — **the page prints the space**; the package is right.

**Page 18** — the primer table (see §4) plus the whole of Western blotting → References 1–2. `50 mM-Tris-HCI (pH 7.4)` with the printed `HCI` preserved; `Triton X-100`, `0.5%`, `0.1%`, `150 mM`, `2 mM`, `11836170001`, `20 µg` (micro sign preserved), `SDS (8%)`, `β-mercaptoethanol (5%)`, `95 °C`, `3-8% tris-acetate`, `Millipore, 1:5000`, `0.1% Tween-20`, `AI680`, `W32466; 3.33 μg/mL`, `G5882`, `A12380; 1:250`, `15630-080`, `405, 488, 561 and 640 nm`, `40X` / `0.8x` / `63X` / `1x` (letter x as printed), `1.3`/`1.4 numerical aperture`, `0.45 μm`, `7 and 13 μm`, `Plan-Apochromat 63×/1.4` (multiplication sign as printed), `1.518`, `0.133 μm`, `FACSymphony S6`, `GraphPad Prism 10.0`, refs 100/101 markers. Refs 1 and 2 exact (`Cell Death Dis. 14, 1–16 (2023)`, `Science 282, 1075–1079 (1998)`), en dashes correct.

**Page 20** — references 44 to 87, all 44 compared line by line. Every author string, journal abbreviation, bold volume, en-dashed page range and year matches, including `342ra78–342ra78`-style and `2203–2213.e5`, `280–291.e17`, `E87–E101`, `eaao6047`, `e99238`, `e2103585118`, `eadl0429`, `77A`, and the accented names `Kräusslich`, `Härtlova`, `Glück`, `Cordelières`, `Sáenz-de-Santa-María`, `Fédération`. Ref 47's printed `cytochrome crelease` is preserved; ref 47 and ref 70's trailing `*` are preserved (escaped as `\*`, which renders as `*`).

**Document-wide character census** (package vs PDF, after removing conversion notes and figure links): `—` 55/55, `−` 18/18, `×` 42/42, `β` 16/16, `κ` 44/44, `α` 222/222, `Δ` 6/6, `Ψ` 4/4, `™` 3/3, `°` 8/8, `’` 44/44, `“`/`”` 6/6 each, `í` 7/7, `ñ` 2/2, `ä` 2/2, `ü` 1/1. En dash `–` 156 PDF vs 152 package — the four-dash difference is entirely the Figure 5j schematic's baked-in labels (`Inhibition (H-151) – prevents…`, `Inhibition (JSH-23) – prevents…`, `Activation (diABZI) – promotes…`, `NF-κB inhibition – prevents…`), which live in the artwork. **Net: exactly one character in the whole document differs from the page, the U+00B5/U+03BC noted above.** The only characters in the package absent from the PDF are `#` (Markdown headings) and `\` (3 escapes).

**Superscript/subscript audit**: 183 superscript runs detected in the PDF by font-size; 179 `<sup>` in the package. Every difference reconciles: 2 are Figure 3/7/8 artwork labels, 1 is the split exponent `-` + `5` correctly merged to `<sup>-5</sup>`, and 1 is Chiara Zurzolo's affiliation `1` that my size heuristic missed in the PDF but the package has. Both subscripts are correct: `CO<sub>2</sub>` and `NH<sub>4</sub>Cl`.

## 7. Navigation index — 1 defect

`rg -n -F -x` over `references/paper.md`: **30 of 31** index headings exist verbatim (as `# <heading>` or `## <heading>`).

**DEFECT (minor).** `references/index.md`, the "Supplementary information — supplement.md" table, lists the exact heading **`Document beginning`**. `references/supplement.md` contains no such heading; its full contents are:

```
# Supplementary information

No corresponding materials were supplied.
```

An agent following the index with `rg -F -x 'Document beginning'` gets nothing. Fix is either to rename the index row to `Supplementary information` or to drop the row.

---

## Other findings

### Genuine, minor

1. **Four article sections are missing from the navigation index.** `paper.md` contains `## Reporting summary` (234), `# Acknowledgements` (446), `# Author contributions` (450) and `# Competing interests` (454); none appears in `index.md`. Funding, author roles and the competing-interests statement are therefore unreachable by index lookup. (`# Additional information` and `# Data availability` *are* indexed.)

### Cosmetic / judgement calls

2. **Index figure pointers describe the discussion, not the link location.** `index.md`'s "Look here for" column attributes Figure 1 to "α-Syn aggregates localize to mitochondria…", Figure 3 to "α-Syn leads to BAX-mediated mtDNA release", Figure 5 to "α-Syn-induced intercellular connections…", Figure 6 to "Inflammation-induced connections…", Figure 7 to "Neuronal cells transfer damaged mitochondria to microglia", Figure 8 to "α-Syn-burdened neuronal cells prime microglia…", Figure 9 to "Discussion". Those are the sections that *cite* each figure, which is semantically right, but because the reading order follows print position the actual link + caption for 7 of 9 figures sits under a different heading (Fig. 1 under "…cause mitochondrial dysfunction", Fig. 3 under "α-Syn-induced intercellular connections…", Fig. 4 under "Inflammation-induced connections…", Figs. 5–6 under "Discussion", Fig. 7 under Methods → "Neuron generation", Figs. 8–9 under Methods → "Immunocytochemistry"). Only Figs. 2 and 4's index rows coincide. Worth a one-line note in the index rather than a change to `paper.md`.

3. **Page 1 author line carries two interpolations that are not page text.** `paper.md:11` writes `Veronica Testa (ORCID)`, `Jara Montero-Muñoz (ORCID)`, `Masato Hasegawa (ORCID)`, `Antonella Consiglio (ORCID)`, `Chiara Zurzolo (ORCID)` and `(corresponding author)`. The page shows ORCID *icons* and an envelope glyph in those positions, with no such words. The mapping is faithful (exactly those five authors carry an ORCID icon; Zurzolo carries the envelope) and it is arguably a good accessibility rendering, but a word-level diff against the page flags six inserted tokens. Flagging so the choice is deliberate, not accidental.

4. **`SKILL.md` still carries a draft banner**: `**Draft: source review or verification remains unresolved.**` (line 8). If this package is meant to ship, that line needs to go.

5. **`assets/supp_figs/` and `assets/supp_table/` are empty** but both are advertised in `index.md`'s Assets section. The Conversion notes explain why (no Supplementary Information was supplied), so this is consistent, just worth a cross-reference.

---

## Printed defects correctly preserved (confirmed, NOT package errors)

All five from the brief confirmed verbatim in the package: `cytochrome crelease` (ref 47); `For h: PQ:` (Fig. 6 caption, page 13); `mediatied` (Fig. 9 caption); `HCI` for `HCl` (page 18); `(PeproTech,200-34)` with no space (verified at 11× — the page really has no space). Also confirmed: `300 x g` (letter x) alongside `800 × g` on the same methods run; the mixed `1x10-15` / `1× 10–15` / `7.008 × 10-10` exponent notation reproduced per instance; `mTeSRTM1`, `StemProTM-34`, `GibcoTM` with full-size TM — while `Gibco™` and `Alexa Fluor™` and `Filcon™` in the *same document* use a real ™, and the package reproduces each as printed.

Five further printed oddities I found and verified as faithfully reproduced (adding them so nobody "fixes" them later):

- **Fig. 3 caption, `p < 1× 10-15`** — this is the one place in the document where the package does *not* superscript an exponent (all 60 others are `<sup>`-wrapped). I rendered page 7 at 14× and inspected the PDF span font sizes: the journal genuinely sets this `-15` at full size (7.0 pt, same as the body) rather than as a 4.2 pt superscript. The package is correct and the inconsistency is the publisher's.
- **Page 21, Author contributions, `Investigation: R.C., P.S., V.T., and J.M.M.`** — `P.S.` matches no author on the paper (the author list is R.C., S.M., V.T., J.M.M., T.N., M.H., A.C., C.Z.). Printed as such; preserved.
- **Fig. 4 caption, `p = 4,64 ×10–8`** — comma as decimal separator, printed; preserved.
- **Page 5, `(Fig.3h, i)`** — no space after `Fig.`; printed; preserved.
- **Page 21, Acknowledgements, `(code: LCF/BQ/DI21/11860038.`** — unclosed parenthesis; printed; preserved.

Two places where the PDF *text layer* is wrong and the package correctly follows the rendered page (verified by zoomed render, so the reviewers' calls were right): `microglial cells` on page 5 (text layer says `microglialcells`), `Institut Pasteur, for` on page 21 (text layer says `Pasteur,for`), plus `Alexa Fluor™ 488` and `Filcon™ Syringe-Type` on pages 15 and 13.

---

## Scope statement

**Deep word-by-word text comparison covered five sampled pages, not all 21.** The sampled pages were **1, 5, 15, 18 and 20**.

The other sixteen pages (2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 19, 21) were covered by the document-wide automated checks only: two-directional 100-character normalised window coverage (confirming nothing is missing and nothing is invented), the 261-case line-break hyphen audit, the special-character census, the superscript/subscript audit, and — for the figure captions on those pages — a full-caption containment check against the PDF text layer. Those checks are insensitive to whitespace-only differences and to glyph substitutions that normalise to the same character, so an isolated spacing or look-alike-character error on an unsampled page would not necessarily have been caught.
