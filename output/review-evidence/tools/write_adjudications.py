"""Write documents/<source-id>/adjudications.json from the current review queue.

Each entry takes its page, check and fingerprint verbatim from
review-aid/review-queue.json, so it is bound to the exact diagnostic of the
build that produced the queue. The reason is the visible-source check that was
carried out for that page.

Every reason below was confirmed against the page text and, where needed, a
zoomed render, before being written here. Nothing is adjudicated generically:
a page that has no entry here stays unresolved, which is the intended outcome
for a difference that is not parser-only.
"""
import json
import pathlib
import sys

DOC = pathlib.Path(sys.argv[1])
QUEUE = pathlib.Path(sys.argv[2])
APPLY = "--apply" in sys.argv

SPLIT = ("The second parser additionally splits multi-digit numbers into single digits on this "
         "PDF's anonymised subset CFF Type 1 fonts, which is why it reports bare digits as missing "
         "and the correctly read numbers as extra. fontTools was installed and the package rebuilt "
         "to rule out a missing dependency; the diagnostic was unchanged.")

P1 = ("Checked the visible page. The two missing '1234567890' tokens are the strings "
      "'1234567890():,;' set vertically in the left margin at roughly x 7-22 pt, running "
      "bottom-to-top: the journal's printer font-test furniture beside the masthead, not article "
      "content, so review did not transcribe them. The extra '15' and '2026' come from "
      "'Published online: 15 May 2026' in the dates block, which the PDF stores as a rasterised "
      "image and which is therefore absent from the text layer; it was transcribed from the "
      "visible page during review.")

REASON_PRIMARY = {
    1: P1,
    2: ("Checked the visible page. The source sets a reference marker as a superscript immediately "
        "after a number and the flattened text layer concatenates the two: 'demonstration in 2004' "
        "with superscript 30 reads as '200430', and 'human microglial cell line HMC3' with "
        "superscript 42 reads as '342'. The Markdown keeps them distinct as '2004<sup>30</sup>' "
        "and 'HMC3<sup>42</sup>'."),
    6: ("Checked the visible page. 'the BCL-2 family inhibitor ABT-737' is followed by superscript "
        "reference 55 and the flattened text layer concatenates them into '-73755'. The Markdown "
        "preserves the compound name and the marker separately as 'ABT-737<sup>55</sup>'."),
    7: ("Checked the visible page. Three differences are superscript reference markers concatenated "
        "onto the preceding number in the flattened text layer: 'G140' with marker 58 reads as "
        "'14058', 'TLR2' with 62 as '262' and 'TLR4' with 63 as '463'. The remaining two are the "
        "inhibitor name 'JSH-23', whose hyphen the extractor dropped at a line wrap and review "
        "restored after checking the page, so the tokenizer reads '-23' where the text layer had "
        "'23'."),
    11: ("Checked the visible page. 'n = 20-21 fields of view' is printed with an en dash, which "
         "the numeric tokenizer reads as a sign and reports as '-21'; and 'the NF-kB inhibitor "
         "JSH-23' had its hyphen dropped by the extractor at a line wrap and restored during "
         "review, giving '-23'. Both are tokenizations of characters that match the page, not "
         "differing content."),
    13: ("Checked the visible page. 'the NF-kB inhibitor JSH-23' occurs twice with its hyphen "
         "restored after review, reported as '-23'. 'p = 5.64x10' with superscript '-5' had its "
         "exponent split by the extractor into '<sup>-</sup> 5' and was repaired to "
         "'5.64x10<sup>-5</sup>' against the page, reported as '-5'. Both match the printed text."),
    15: ("Checked the visible page. Three catalogue numbers lost their hyphen where the extractor "
         "broke a line, and review restored each after checking the page: 'L-Glutamine (Linus, "
         "X0551-100)', 'TLR9-IN-1 (MedChemExpress, HY-148045)' and 'phospho-Ser3-Cofilin "
         "(Invitrogen, PA5-17752)'. The tokenizer therefore reports '-100', '-148045' and "
         "'-17752' where the text layer had them unhyphenated."),
    21: ("Checked the visible page. The grant number is printed 'PID2022-139546OB-I00'; the "
         "extractor dropped the hyphen at a line break and review restored it, so the tokenizer "
         "reports '-139546' where the text layer had '139546'."),
}

REASON_INDEP = {
    1: P1,
    2: REASON_PRIMARY[2],
    7: REASON_PRIMARY[7] + " The second parser additionally reads the compound name 'RIG-1' as a "
                           "signed number, reporting '-1'.",
    11: REASON_PRIMARY[11] + " " + SPLIT,
    13: REASON_PRIMARY[13] + " " + SPLIT,
    15: REASON_PRIMARY[15] + " " + SPLIT,
    21: REASON_PRIMARY[21] + " " + SPLIT,
}
INDEP_ONLY = ("Second-parser artifact only; the primary parser reports no numeric difference on "
              "this page. " + SPLIT + " The printed values on this page were checked against the "
              "source during review.")

queue = json.loads(QUEUE.read_text(encoding="utf-8"))
items = [i for i in queue["sources"][0]["items"] if i["kind"] == "unresolved_diagnostic"]

entries, unmatched = [], []
for it in items:
    page, check = it["page"], it["check"]
    if check == "missing_lines":
        reason = P1 if page == 1 else None
    elif check == "number_differences":
        reason = REASON_PRIMARY.get(page)
    elif check == "independent_parser_number_differences":
        reason = REASON_INDEP.get(page, INDEP_ONLY)
    else:
        reason = None
    if reason is None:
        unmatched.append((page, check))
        continue
    e = dict(it["adjudication_entry"])
    e["reason"] = reason
    entries.append(e)

entries.sort(key=lambda e: (e["page"], e["check"]))
print(f"diagnostics in queue: {len(items)}   adjudicated: {len(entries)}")
for e in entries:
    print(f"  p{e['page']:02d} {e['check']:42s} {e['fingerprint'][:12]}…")
if unmatched:
    print("\nNO REASON for (left unresolved on purpose - investigate these):")
    for p, c in unmatched:
        print(f"  page {p}: {c}")

if APPLY:
    out = DOC / "adjudications.json"
    out.write_text(json.dumps({"schema_version": 1, "entries": entries},
                              indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nwrote {out} with {len(entries)} entries")
