"""Sanity-check assembled claims against plans: banner, cost figures, planted strings, identifier safety."""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
fig = json.loads((ROOT / "docs/answer-key-figures.json").read_text())
BANNER = "SYNTHETIC TEST DATA"
QUORLANE = ["in accordance with paragraphs 3, 6 and 13 of the DSIT Guidelines",
            "All activities were undertaken in a systematic, iterative and controlled manner"]
MUST = {
    "C04": QUORLANE, "C05": QUORLANE + ["Prototypes were iteratively developed"],
    "C06": QUORLANE + ["Prototypes were iteratively developed", "Not applicable"],
    "C08": ["fewer than 8% of origin", "LDS-214", "LDS-502", "Wharf Approach"],
    "C09": ["8%", "Polaris", "LDS-", "Wharf Approach", "3 April 2024"],
    "C10": ["8%", "Lodestar", "LDS-", "Wharf Approach"],
    "C11": ["proprietary engineering reasoning capability", "Ask Edith", "Halvorsen Pike", "TAX_RD_EXTRACT", "Growth Fund"],
    "C07": ["31.8%", "Stichting Waterstof"], "C05": QUORLANE + ["03/02/2026"],
}
ok_all = True
for cid in sys.argv[1:] or sorted(fig):
    d = next((ROOT / "claims").glob(f"{cid}-*"), None)
    f = d / "claim.md" if d else None
    if not f or not f.exists():
        print(f"{cid}: not assembled"); ok_all = False; continue
    t = f.read_text()
    probs = []
    if BANNER not in t: probs.append("banner missing")
    costs = (ROOT / f"plans/costs/{cid}.md").read_text()
    totals = [m for m in re.findall(r"\*\*(£[\d,]+)\*\*", costs)]
    for tot in totals:
        if tot not in t: probs.append(f"total {tot} missing")
    for s in MUST.get(cid, []):
        if s not in t: probs.append(f"missing planted text: {s!r}")
    # identifier safety: real-looking company numbers / UTRs / postcodes
    for m in re.findall(r"\b(?:company (?:no\.?|number)[: ]*)(\d{8})\b", t, re.I):
        probs.append(f"real-format company number {m}")
    for m in re.findall(r"\bUTR[: ]*(\d{10})\b", t):
        if not m.startswith("99999"): probs.append(f"non-synthetic UTR {m}")
    pcs = set(re.findall(r"\b([A-Y]{1,2}\d{1,2}[A-Z]?) \d[A-Z]{2}\b", t))
    if pcs: probs.append(f"real-format postcodes {sorted(pcs)[:5]}")
    words = len(t.split())
    status = "OK" if not probs else "ISSUES"
    ok_all &= not probs
    print(f"{cid}: {words:,} words  {status}")
    for p in probs: print(f"    - {p}")
sys.exit(0 if ok_all else 1)
