"""List adjacent prose items whose text looks like one paragraph split by the
two-column layout, so the coordinator can decide a join_previous value.

Read-only. Mirrors the builder's item ordering in reading_package.py:
  - kind == 'omit' items are dropped entirely
  - repeated margin headers/footers are auto-omitted and skipped without
    disturbing the previous prose item
so the "previous prose item" here is the one the builder would join onto.
"""
import json
import pathlib
import re
import sys
import collections

PROSE = {"text", "caption"}
# Sentence looks finished: ends with . ? ! : ; or a closing quote/bracket after one.
TERMINAL = re.compile(r'[.?!:;]["”’)\]]?\s*$')
# Trailing superscript reference marker after a terminal stop, e.g. "...matrix<sup>13,14</sup>"
SUP_TAIL = re.compile(r'</sup>\s*$')


def margin_omissions(pages, title):
    """Approximate compact_omission_reasons: short lines repeated on >=3 pages."""
    counts = collections.Counter()
    sig = {}
    for p in pages:
        for it in p["items"]:
            if it["kind"] != "text":
                continue
            md = (it.get("markdown") or "").strip()
            if not md or len(md) > 120 or "\n" in md:
                continue
            key = re.sub(r"\d+", "#", md.lower())
            counts[key] += 1
            sig[it["id"]] = key
    return {i for i, k in sig.items() if counts[k] >= 3}


def main(doc_dir):
    doc = pathlib.Path(doc_dir)
    plan = json.loads((doc / "plan.json").read_text(encoding="utf-8"))
    pages = [json.loads((doc / f"pages/page-{n:04d}.json").read_text(encoding="utf-8"))
             for n in range(1, plan["source"]["pages"] + 1)]
    auto = margin_omissions(pages, plan.get("title", ""))

    seq = []  # (page_no, item) in builder order
    for p in pages:
        for it in p["items"]:
            if it["kind"] == "omit" or it["id"] in auto:
                continue
            seq.append((p["page"], it))

    prev = None
    for page_no, it in seq:
        kind = it["kind"]
        md = (it.get("markdown") or "").strip()
        if kind in PROSE and prev is not None:
            ppage, pit = prev
            ptext = (pit.get("markdown") or "").strip()
            already = it.get("join_previous")
            finished = bool(TERMINAL.search(ptext)) or bool(SUP_TAIL.search(ptext))
            starts_lower = bool(re.match(r'^[a-zα-ω(]', md))
            hyphen_end = ptext.endswith("-")
            if already or (not finished) or starts_lower or hyphen_end:
                flag = []
                if already:
                    flag.append(f"SET={already}")
                if hyphen_end:
                    flag.append("HYPHEN-END")
                if not finished:
                    flag.append("NO-TERMINAL")
                if starts_lower:
                    flag.append("STARTS-LOWER")
                boundary = "PAGE" if ppage != page_no else "column"
                print(f"\n=== {boundary} {ppage}->{page_no} [{','.join(flag)}]")
                print(f"  prev {pit['id']} ({pit['kind']}): ...{ptext[-120:]!r}")
                print(f"  next {it['id']} ({kind}): {md[:120]!r}...")
        if kind in PROSE:
            prev = (page_no, it)
        elif kind in {"figure", "formula", "table", "code", "heading"}:
            prev = None  # builder cannot join across these


if __name__ == "__main__":
    main(sys.argv[1])
