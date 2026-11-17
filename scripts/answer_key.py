"""Build docs/answer-key.{json,md} from the cost figures plus the planted issues. ORGANISER-ONLY."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
fig = json.loads((ROOT / "docs/answer-key-figures.json").read_text())

ISSUES = {
 "C01": dict(grade="A", valid=True, issues=[], strengths=[
    "Specific baseline (epoxy-resin transaminases lose 40-70% activity in 100-150 h)",
    "Documented failures (PEI-PLP route abandoned Aug 2024; variant aggregation)",
    "Honest partial outcome on P2 (rho 0.52 vs 0.6 target)",
    "Explicitly excludes paid feasibility studies, GMP docs, patent costs",
    "ELN timesheets reconciled; CEO/lab manager claimed as QIAs with minutes",
    "ERIS intensity 35.3% genuine"]),
 "C02": dict(grade="B", valid=True, issues=[
    "Post-resolution production batches B-423..425 (sold) claimed as 'validation builds': powder £61,500 + operator uplift",
    "Overseas subcontractor (German CT lab) chosen for cost/turnaround: breaches overseas restriction",
    "Simulation licences at 100% though also used for quoting",
    "ERP/Microsoft 365 licences claimed",
    "MD at 25% on the basis of 4 meetings",
    "Year-end manager estimates rather than timesheets (weak but acceptable)"]),
 "C03": dict(grade="C", valid=True, issues=[
    "Only P1 (Weft ledger) genuinely qualifies; P2 UI/LLM-API is UX/business uncertainty; P3 cloud migration routine (CIRD81980 CS1); P4 API integration routine",
    "Engineers at 85-90% from retrospective interviews (Sept 2025), no timesheets",
    "Product manager 60%, CEO 40%",
    "All production AWS hosting (£184k) claimed as cloud computing",
    "Salesforce/Figma/Slack in software",
    "Routine integration subcontract claimed",
    "Evidence quality drops sharply after P1 (Jira refs only for P1)"]),
 "C04": dict(grade="D", valid=True, issues=[
    "Competent professional is a chef with no scientific background",
    "Uncertainties are business/sensory (diner acceptance, food cost margins)",
    "Whole kitchen brigade at 25%; head chefs 50%",
    "Ingredients for food sold to customers claimed (£64k)",
    "Capital equipment (sous-vide, fermentation chamber) in consumables",
    "Evidence = menus, Instagram, WhatsApp",
    "Quorlane boilerplate shared verbatim with C05, C06",
    "Only P3 shelf-life work is borderline-qualifying"]),
 "C05": dict(grade="D", valid=False, issues=[
    "CNF filed 03/02/2026, after the 31/01/2026 deadline: claim invalid",
    "Client-funded fixed-price contract; routine engineering risk managed to established practice (Collins Construction pattern)",
    "Design by external consultant engaged for client, claimed as subcontracted R&D",
    "Materials incorporated into client's building and plant hire claimed as consumables",
    "Competent professional not an engineer; 'advance' is the company's own capability",
    "Directors 60-70%, site operatives 20%, estimator 50%, set in a workshop",
    "P2 = adoption of vendor apps",
    "Quorlane boilerplate shared with C04, C06"]),
 "C06": dict(grade="E", valid=False, issues=[
    "First claim with no CNF: invalid",
    "Dividends included in director staff costs (£78k gross)",
    "Company secretary at 80%",
    "CNC router (capital) claimed as consumable",
    "Timber for sold orders, van lease/fuel, CAD licence claimed",
    "No baseline, generic business uncertainties, no contemporaneous evidence",
    "Template narrative shared with C04/C05 (Quorlane); cold-call origin, 30% contingent fee",
    "Benefit disproportionate to a 4-person, £640k-turnover business"]),
 "C07": dict(grade="B", valid=True, issues=[
    "ERIS intensity inflated by excluding £420k pilot-plant costs from denominator: true ~23.5% < 30%, so merged-loss (16.2%) not ERIS",
    "Overseas Dutch AST lab justified by availability/time, which is not a permitted condition: £78k disallowed",
    "Commercial Director at 10%",
    "Science and evidence otherwise strong; grant handled correctly"]),
 "C08": dict(grade="E", valid=True, issues=[
    "Connected EPW (C10 staff) claimed at payment incl. 15% markup instead of lower of payment/provider cost",
    "£210k 'subcontract' to C09 for the same Lodestar work: double count within the claim",
    "Most Lodestar work is off-the-shelf model tuning (CIRD81980 CS2); ~35% qualifies",
    "Production inference cloud claimed",
    "Same engineers also claimed by C09 and C10"]),
 "C09": dict(grade="E", valid=True, issues=[
    "Contractor to C08: under merged scheme the customer (C08) claims, not C09",
    "Incorporated 3 Apr 2024, days before agreements: shell with 2 non-claimed employees",
    "Claims 'seconded' Achterberg/Grieve at 90%, who are employed and claimed by C10 (combined 185%)",
    "Connected 'modelling support' fee to C10 is the same engineers again",
    "Azure costs re-invoiced from C08: duplicate",
    "ERIS as standalone SME: ignores linked group; loss is artificial (intra-group fees)",
    "Omits group relationships; 'Polaris' = Lodestar"]),
 "C10": dict(grade="E", valid=True, issues=[
    "Staff provider bearing no R&D risk (reimbursed cost+15%), claims engineers as own R&D",
    "Same 5 engineers recharged to C08 (claimed there) and partly to C09",
    "Platform licence recharged to C08 and claimed here too"]),
 "C11": dict(grade="C", valid=True, issues=[
    "P1 folds firm-wide rollout of an approved third-party AI assistant (training, licences for 1,200 seats) into R&D",
    "Claim calls Edith 'proprietary' with 'reliability not previously achieved'; website Insights (2026-05-19) says approved assistant, results 'encouraging but uneven'",
    "Claim says P1 started Feb 2025, before May 2025 AI guidance and the 22 Sep 2025 first cohort",
    "US Halvorsen Pike data scientists (connected, overseas) claimed: £310k",
    "Hydraulic modellers at 55% incl. fee-earning scheme modelling; P2 core is genuine",
    "P3 mostly client data-centre design (billed); only the test rig qualifies",
    "P4 ERP/data platform routine IT; £720k cloud",
    "Connected EPW from Tarnbeck at recharge not provider cost",
    "Cost history from TAX_RD_EXTRACT with only a year-on-year totals check"],
    footprint_checks=[
    "insights/ai-assistance-for-engineers-lessons-so-far (2026-05-19, McGregor): contradicts 'proprietary'",
    "news 2025-09-22: first AI cohort date",
    "insights/what-data-science-can-do-for-an-engineer (2025-11-12, Ritchie): supports P2 competence, cautious tone",
    "insights/cooling-dense-computing (2025-06-10, Norris): design practice, not research",
    "leadership pages: Scott Lam Head of R&I, McGregor CDIO from Jan 2025",
    "projects: flood-storage-river-catchment (Rivenhaven-type client scheme)"]),
}

CROSS = [
 dict(link="Holt cluster", claims=["C08", "C09", "C10"],
      evidence=["Shared registered office Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS",
                "Director Gavin Holt on all three; parent Veridian Holt Holdings Ltd",
                "Same Jira IDs LDS-214, LDS-377, LDS-502",
                "Achterberg & Grieve: C10 95% + C09 90% = 185%",
                "C10 staff recharged to C08 at cost+15% and claimed there",
                "Azure subscription in C08 re-invoiced to C09",
                "Near-duplicate sentence on '8% of origin–destination pairs'",
                "Near-identical competent-professional judgement paragraph by Dr Achterberg in all three",
                "Achterberg CV inconsistent across packs (8 vs 14 vs 15+ years; different doctorate titles; three different employers/job titles)",
                "C09 statement dated 12 Aug 2025 vs C08 26 Mar 2026: same expert, different roles"],
      combined_claimed_net=None, legit_net=None),
 dict(link="Quorlane boilerplate", claims=["C04", "C05", "C06"],
      evidence=["Verbatim DSIT 'paragraphs 3, 6 and 13' sentence", "Verbatim AIF closing line",
                "Shared heading template", "Near-duplicate 'Prototypes were iteratively developed…' (C05/C06)"]),
 dict(link="Vantrell agent (red herring)", claims=["C03", "C08"], evidence=["Same agent, no substantive overlap"]),
]


def net(b):
    return b.get("net", b.get("payable_credit", b.get("relief", 0)))


out = {}
for cid, meta in ISSUES.items():
    f = fig[cid]
    out[cid] = dict(company=f["company"], **meta,
                    claimed_qe=f["claimed"]["qe"], correct_qe=f["corrected"]["qe_ok"],
                    claimed_scheme=f["claimed"]["scheme"], correct_scheme=f["corrected"]["scheme_ok"],
                    claimed_benefit=net(f["claimed"]["benefit"]), correct_benefit=net(f["corrected"]["benefit_ok"]) if meta["valid"] else 0,
                    corrected_intensity_pct=f["corrected"].get("intensity_ok_pct"),
                    disallowed_cost_lines=f["disallowed_lines"], staff_adjustments=f["staff_adjustments"])
holt = ["C08", "C09", "C10"]
CROSS[0]["combined_claimed_net"] = sum(out[c]["claimed_benefit"] for c in holt)
CROSS[0]["legit_net"] = sum(out[c]["correct_benefit"] for c in holt)
(ROOT / "docs/answer-key.json").write_text(json.dumps(dict(claims=out, cross_claim_links=CROSS), indent=2))

L = ["# Answer key (ORGANISER-ONLY: never expose to tools under test)", "",
     "Benefits are cash value: net credit after tax for merged-scheme claimants, or the payable credit for ERIS/SME claimants. Generated by `scripts/answer_key.py`.", "",
     "| ID | Company | Grade | Valid? | Scheme claimed → correct | QE claimed | QE correct | Benefit claimed | Benefit correct |",
     "|---|---|---|---|---|---:|---:|---:|---:|"]
for cid, o in out.items():
    L.append(f"| {cid} | {o['company']} | **{o['grade']}** | {'yes' if o['valid'] else '**no**'} | {o['claimed_scheme']} → {o['correct_scheme']} | "
             f"£{o['claimed_qe']:,} | £{o['correct_qe']:,} | £{o['claimed_benefit']:,} | £{o['correct_benefit']:,} |")
for cid, o in out.items():
    L += ["", f"## {cid}: {o['company']} (grade {o['grade']})", ""]
    for s in o.get("strengths", []):
        L.append(f"- ✅ {s}")
    for s in o["issues"]:
        L.append(f"- ⚠️ {s}")
    for s in o.get("footprint_checks", []):
        L.append(f"- 🌐 {s}")
    if o["corrected_intensity_pct"]:
        L.append(f"- Corrected R&D intensity: {o['corrected_intensity_pct']}%")
L += ["", "## Cross-claim links", ""]
for c in CROSS:
    L.append(f"### {c['link']} ({', '.join(c['claims'])})")
    L += [f"- {e}" for e in c["evidence"]]
    if c.get("combined_claimed_net") is not None:
        L.append(f"- Combined benefit claimed £{c['combined_claimed_net']:,} vs legitimate £{c['legit_net']:,}")
    L.append("")
(ROOT / "docs/answer-key.md").write_text("\n".join(L) + "\n")
print("\n".join(L[:18]))
