"""Coordinator pass: page-1 header omissions, affiliation relocation, and the
document-wide join_previous flags that reconnect prose split by the two-column
layout. Validates every join against the builder's own emission rules first.
"""
import collections
import json
import pathlib
import re
import sys

DOC = pathlib.Path(sys.argv[1])
APPLY = "--apply" in sys.argv

# id -> "space" | "none"; every one verified against the candidate listing.
JOINS = {
    "p0001-b006": "space", "p0002-b002": "space", "p0002-b008": "space",
    "p0003-b006": "space", "p0004-b005": "space", "p0005-b003": "space",
    "p0005-b009": "space", "p0006-b003": "space", "p0006-b004": "space",
    "p0007-b009": "space", "p0008-b003": "space", "p0008-b004": "space",
    "p0009-b003": "space", "p0009-b009": "space", "p0010-b003": "space",
    "p0010-b004": "space", "p0011-b003": "space", "p0011-b007": "space",
    "p0012-b003": "space", "p0012-b005": "space", "p0013-b003": "space",
    "p0014-b003": "space", "p0015-b003": "space", "p0015-b010": "none",
    "p0016-b003": "space", "p0016-b004": "space", "p0017-b010": "space",
    "p0018-b007": "none", "p0021-b018": "space",
}
# Blocks that merely lack terminal punctuation; they are not continuations.
NO_JOIN = {"p0001-b001", "p0001-b004b", "p0001-b004c", "p0001-b008",
           "p0004-b003", "p0021-b029"}
# Page-1 running header: the compact rule misses it because page 1's masthead
# pushes it out of the margin band that the other twenty pages share.
OMIT_P1 = {
    "p0001-b000": "Repeated page header ('Article'); identical furniture is auto-omitted on pages 2-21 "
                  "but falls outside the margin band on page 1 because the masthead shifts it down.",
    "p0001-b001": "Repeated page header (article DOI URL); identical furniture is auto-omitted on pages "
                  "2-21. The DOI is recorded in the package notes.",
}

pages = {n: json.loads((DOC / f"pages/page-{n:04d}.json").read_text(encoding="utf-8"))
         for n in range(1, 22)}
plan = json.loads((DOC / "plan.json").read_text(encoding="utf-8"))
items = {it["id"]: it for p in pages.values() for it in p["items"]}


def canonical(s):
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def auto_omitted(pages, title):
    cand = []
    for p in pages.values():
        h = float(p["height"])
        for it in p["items"]:
            if it["kind"] not in {"text", "heading", "caption"}:
                continue
            b = it["bbox"]
            if b[1] > 48 and b[3] < h - 30:
                continue
            sig = re.sub(r"\d+", "", canonical((it.get("markdown") or "").strip()))
            if 3 <= len(sig) <= 100:
                cand.append((sig, it["id"]))
    cnt = collections.Counter(s for s, _ in cand)
    out = {i for s, i in cand if cnt[s] >= 3}
    want = canonical(title)
    for it in pages[1]["items"]:
        if it["kind"] == "heading" and it["bbox"][1] <= 130:
            got = canonical(it.get("markdown") or "")
            if want and want in got and got != want:
                out.add(it["id"])
    return out


# --- mutate -----------------------------------------------------------------
for iid, reason in OMIT_P1.items():
    items[iid]["kind"] = "omit"
    items[iid]["reason"] = reason
    items[iid].pop("join_previous", None)

order = [i for i in plan["reading_order"] if i not in OMIT_P1]
order.remove("p0001-b008")
order.insert(order.index("p0001-b004b") + 1, "p0001-b008")

for iid in NO_JOIN:
    items[iid].pop("join_previous", None)
for iid, how in JOINS.items():
    items[iid]["join_previous"] = how

# --- validate exactly as the builder emits ----------------------------------
auto = auto_omitted(pages, plan["title"])
errors, checked = [], []
prev = None
for iid in order:
    if iid in auto:
        continue
    it = items[iid]
    k = it["kind"]
    if it.get("join_previous"):
        if prev is None or prev["kind"] not in {"text", "caption"} or k not in {"text", "caption"}:
            errors.append(f"{iid}: join onto {prev['id'] if prev else None} "
                          f"({prev['kind'] if prev else 'nothing'}) is invalid")
        else:
            sep = " " if it["join_previous"] == "space" else ""
            seam = (prev.get("markdown") or "").rstrip()[-38:] + "[" + sep + "]" + (it.get("markdown") or "").lstrip()[:38]
            checked.append(f"  {iid:14s} <- {prev['id']:14s} {seam!r}")
    prev = it

non_omit = [it["id"] for p in pages.values() for it in p["items"] if it["kind"] != "omit"]
if sorted(order) != sorted(non_omit):
    errors.append(f"reading_order mismatch: {len(order)} vs {len(non_omit)} non-omit items")

print(f"joins set: {len(JOINS)}   validated: {len(checked)}")
print("\n".join(checked))
if errors:
    print("\nERRORS:")
    print("\n".join(errors))
    sys.exit(1)
print("\nAll joins land on prose. reading_order covers every non-omitted item exactly once.")

if APPLY:
    plan["reading_order"] = order
    (DOC / "plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for n, p in pages.items():
        note = p.get("review_notes", "").rstrip()
        add = []
        if any(i["id"] in OMIT_P1 for i in p["items"]):
            add.append("Coordinator: page-1 running header and DOI set to omit to match the automatic "
                       "header removal applied to pages 2-21.")
        if any(i["id"] in JOINS for i in p["items"]):
            add.append("Coordinator: set join_previous where the two-column layout split a sentence, "
                       "verified against the source text on both sides of the break.")
        if add:
            p["review_notes"] = (note + " " + " ".join(add)).strip()
        (DOC / f"pages/page-{n:04d}.json").write_text(
            json.dumps(p, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("applied")
