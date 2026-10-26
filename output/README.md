# α-Synuclein / TNT paper agent

An agent-readable skill built from the Nature Communications article
**"α-Synuclein aggregates induce mitochondrial damage and trigger innate immunity to drive
neuron–microglia communication"**, (2026) 17:6462,
https://doi.org/10.1038/s41467-026-73136-7.

Produced with the `paper2agent` skill from https://github.com/jmiao24/Paper2Agent, Paper2Skill
route. Source PDF SHA-256 `e61f3331e348d50ee5bf756e25b6a7d7e592d2a2b59c3fe6b55a46f914432e48`.

## What is here

```
alpha-syn-mito-tnt-paper/     the skill — this is the deliverable
├── SKILL.md                  how an agent should read the paper
├── references/
│   ├── index.md              navigation index, 35 headings
│   ├── paper.md              the full article as one continuous document
│   └── supplement.md         records that no supplementary material was supplied
└── assets/
    ├── figure/figure-1 … figure-9.jpg
    └── table/table-1.csv     the qRT-PCR primer table

review-evidence/              provenance; NOT part of the skill
```

## Using it

Copy the skill folder into your agent's skills directory, for example
`~/.claude/skills/alpha-syn-mito-tnt-paper/` for Claude Code or
`~/.agents/skills/alpha-syn-mito-tnt-paper/` for Codex, then restart the agent and ask about the
paper. The skill tells the agent to start from `references/index.md`, locate an exact heading,
and read a bounded passage rather than loading the whole article.

No MCP server accompanies this skill. The article is wet-lab cell biology: it ships no analysis
code, its data availability statement names no repository, and none exists in this account, so
there is nothing for Paper2MCP to bind tools to. A paper-only conversion is a valid single-mode
run of the skill.

## Verification status

`reviewed_with_limitations` — the skill's successful reviewed state. Strict verification exits 0.

| Check | Result |
| --- | --- |
| Strict verification | pass, `reviewed_with_limitations` |
| Pages reviewed | 21 of 21 |
| Adjudications applied / stale | 23 / 0 |
| Assets matching source conversion | 10 of 10 |
| Line coverage | complete on all 21 pages |
| References present and in order | 1–101 |

How it was produced: five reviewers worked separate page ranges against rendered previews and
zoomed crops; a coordinator reconciled them; then an independent verifier, none of the above,
compared the built package against the original PDF. The verifier confirmed page order and
completeness in both directions, all nine figure crops, the primer table base by base, and every
one of 261 line-break hyphens in the document. Its findings were applied before the final build.

The 23 adjudicated diagnostics are all parser artefacts, each justified individually in
`review-evidence/documents/*/adjudications.json`, in two families: the flattened PDF text layer
concatenates a number with the superscript reference marker printed after it, so `HMC3` plus
marker 42 reads as one token `342`; and hyphens the extractor dropped at line breaks were
restored after checking the page, among them `JSH-23`, `HY-148045`, `PA5-17752` and the grant
number `PID2022-139546OB-I00`. A separate family affects only the second parser, pypdf, which
splits multi-digit numbers into single digits on this PDF's anonymised subset fonts. fontTools
was installed and the package rebuilt to rule out a missing dependency; the diagnostic was
unchanged.

## Limitations

- **Only the main article PDF was supplied.** The Supplementary Information, Reporting Summary,
  Peer Review file and Source Data are absent, so the many "Supplementary Fig." and
  "Supplementary Movie" callouts in the text cannot be resolved from this package.
- **Deep word-by-word verification was sampled**, covering pages 1, 5, 15, 18 and 20. The other
  sixteen pages were covered by the page reviewers and by document-wide automated checks, which
  are insensitive to whitespace-only differences and look-alike character substitutions.
- **Figure panels are embedded rasters**, so text painted inside them is not searchable. It was
  confirmed visually to lie inside the crops.
- **`SKILL.md`'s description is templated** and mentions "its supplementary information" although
  none was supplied. It cannot be hand-edited without breaking the build hashes.
- **Figure links follow print position**, so a figure and caption can sit under a later heading
  than the section that first cites it. Search `Fig. N |` to jump straight to a caption.
- Panel letters and the statistical `p` are bold and italic in the article but plain here.

## Printed defects deliberately preserved

The article itself contains errors. They were transcribed as printed rather than silently
corrected, and should not be "fixed" later: `cytochrome crelease` in reference 47; `mediatied` in
the Figure 9 caption; `HCI` where `HCl` is meant; `For h: PQ:` in the Figure 6 caption;
`p = 4,64 ×10–8` with a comma decimal separator; `Investigation: R.C., P.S., …` naming an
initial that matches no author; an unclosed parenthesis in the Acknowledgements; `300 x g`
printed with a letter x beside `800 × g`; and a mixture of `×` with `x` and of minus, hyphen and
en dash inside exponents. The reviewer reports in `review-evidence/reports/` record each one.

In four places the PDF's text layer is wrong and this package follows the rendered page instead:
`microglial cells` on page 5, `Institut Pasteur, for` on page 21, `Alexa Fluor™ 488` on page 15
and `Filcon™ Syringe-Type` on page 13.
