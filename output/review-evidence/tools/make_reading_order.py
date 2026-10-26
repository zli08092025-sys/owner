"""Build plan.json reading_order so floating figures/tables do not interrupt a
sentence, and so each figure sits immediately before its own caption.

In the printed two-column article a figure is typeset at the top of page N while
its caption is printed at the top of page N+1, with page N's body prose in
between. Emitted in raw page order the Markdown therefore separates a figure
from its caption by a column of unrelated prose, and splits paragraphs that run
across the float.

The skill sanctions exactly this repair: plan.json may carry a reading_order
array listing every non-omitted item id once, which moves items in the emitted
Markdown while leaving page evidence and review flags untouched.

Policy:
  * pair each figure/table with its caption (caption text beginning "Fig. N |")
  * drop the pair out of the stream, then reinsert it at the nearest paragraph
    boundary at or after the caption's original position, so no sentence is cut
  * never drop or duplicate an item; the result is asserted to be a permutation

Writes nothing unless --apply is given.
"""
import argparse
import json
import pathlib
import re

PROSE = {"text", "caption"}
FLOAT = {"figure", "table", "formula"}
TERMINAL = re.compile(r'[.?!]["”’)\]]?\s*$')
FIGNUM = re.compile(r'^\s*Fig\.?\s*(\d+)\s*\|')


def load(doc):
    plan = json.loads((doc / "plan.json").read_text(encoding="utf-8"))
    pages = [json.loads((doc / f"pages/page-{n:04d}.json").read_text(encoding="utf-8"))
             for n in range(1, plan["source"]["pages"] + 1)]
    return plan, pages


def build(doc):
    plan, pages = load(doc)
    stream = []  # [{id, kind, md, page, asset}]
    for p in pages:
        for it in p["items"]:
            if it["kind"] == "omit":
                continue
            stream.append({
                "id": it["id"], "kind": it["kind"], "page": p["page"],
                "md": (it.get("markdown") or "").strip(),
                "asset": it.get("asset_name"),
            })

    # caption id -> figure number
    cap_num = {}
    for e in stream:
        if e["kind"] == "caption":
            m = FIGNUM.match(e["md"])
            if m:
                cap_num[e["id"]] = int(m.group(1))
    # figure asset_name figure-N -> number
    fig_num = {}
    for e in stream:
        if e["kind"] in FLOAT and e["asset"]:
            m = re.match(r'^(?:figure|supplementary-figure|extended-data-figure)-(\d+)$', e["asset"])
            if m:
                fig_num[e["id"]] = int(m.group(1))

    pairs = {}  # figure id -> caption id
    for fid, n in fig_num.items():
        match = [cid for cid, cn in cap_num.items() if cn == n]
        if len(match) == 1:
            pairs[fid] = match[0]
    moved = set(pairs) | set(pairs.values())

    base = [e for e in stream if e["id"] not in moved]
    index = {e["id"]: i for i, e in enumerate(stream)}

    # Insert each pair at the nearest paragraph boundary at/after the caption.
    inserts = []  # (anchor_position_in_base, [figure, caption])
    for fid, cid in pairs.items():
        anchor = index[cid]
        # position in base = number of surviving items before the caption
        pos = sum(1 for e in stream[:anchor] if e["id"] not in moved)
        # if the item before pos does not end a sentence, walk forward
        while pos < len(base):
            prev = base[pos - 1] if pos > 0 else None
            if prev is None or prev["kind"] == "heading" or prev["kind"] in FLOAT:
                break
            if prev["kind"] in PROSE and TERMINAL.search(prev["md"]):
                break
            pos += 1
        inserts.append((pos, fid, cid))

    order, by_pos = [], {}
    for pos, fid, cid in inserts:
        by_pos.setdefault(pos, []).extend([fid, cid])
    for i, e in enumerate(base):
        for item_id in by_pos.pop(i, []):
            order.append(item_id)
        order.append(e["id"])
    for pos in sorted(by_pos):
        order.extend(by_pos[pos])

    all_ids = [e["id"] for e in stream]
    assert sorted(order) == sorted(all_ids), "reading_order must be a permutation"
    assert len(set(order)) == len(order), "duplicate id in reading_order"
    return plan, stream, order, pairs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("doc")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    doc = pathlib.Path(a.doc)
    plan, stream, order, pairs = build(doc)
    pos = {e["id"]: i for i, e in enumerate(stream)}
    byid = {e["id"]: e for e in stream}
    print(f"items={len(order)} pairs={len(pairs)}")
    for fid, cid in sorted(pairs.items(), key=lambda kv: pos[kv[0]]):
        print(f"  {byid[fid]['asset']}: figure {fid} (p{byid[fid]['page']}) + caption {cid} (p{byid[cid]['page']})"
              f"  -> emitted at slot {order.index(fid)}")
    print("\nmoves (item: old slot -> new slot), nonzero only:")
    for i, item_id in enumerate(order):
        if pos[item_id] != i:
            e = byid[item_id]
            print(f"  {item_id:18s} {e['kind']:8s} p{e['page']:02d}  {pos[item_id]:3d} -> {i:3d}")
    if a.apply:
        plan["reading_order"] = order
        (doc / "plan.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("\nwrote reading_order to plan.json")


if __name__ == "__main__":
    main()
