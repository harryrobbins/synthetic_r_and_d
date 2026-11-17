"""Deterministic cost schedules for the synthetic R&D claim cohort.

Each claim has an AS-CLAIMED schedule (what the company submitted, including
planted errors) and a CORRECTED view (what an HMRC reviewer should arrive at).
Outputs plans/costs/<id>.md (for the writer agents) and docs/answer-key.json
figures. All companies/people are fictional.

Simplifications (documented in docs/cohort-plan.md):
- Employer NIC: 13.8% over £9,100 for periods ending on/before 31 Mar 2025,
  else 15% over £5,000 (blending ignored).
- Merged-scheme profitable companies: net benefit = 20% credit x (1 - 25%).
- Merged-scheme loss-makers: 20% credit less notional tax at 19% = 16.2%.
- ERIS / old SME: payable credit on surrendered loss = min(loss, 186% x QE).
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def nic(salary, regime_year):
    if regime_year == "2024-25":
        return round(max(0, salary - 9100) * 0.138)
    return round(max(0, salary - 5000) * 0.15)


def staff_row(name, role, salary, pct, regime_year, pension_pct=0.05, extra=None, ok_pct=None, note=""):
    n = nic(salary, regime_year)
    p = round(salary * pension_pct)
    total = salary + n + p
    claimed = round(total * pct)
    extra = extra or {}
    # extra = ineligible amounts bundled into claimed staff cost (dividends, BIK)
    claimed_extra = sum(round(v * pct) for v in extra.values())
    ok = round(total * (pct if ok_pct is None else ok_pct))
    return dict(name=name, role=role, salary=salary, nic=n, pension=p, total=total,
                pct=pct, claimed=claimed + claimed_extra, extra=extra, ok_pct=ok_pct, ok=ok, note=note)


def benefit(scheme, qe, loss=None):
    if scheme == "merged-profit":
        credit = qe * 0.20
        return dict(credit=round(credit), net=round(credit * 0.75),
                    desc="20% expenditure credit (taxable); net ~15% at 25% CT")
    if scheme == "merged-loss":
        credit = qe * 0.20
        return dict(credit=round(credit), notional_tax=round(credit * 0.19), net=round(credit * 0.81),
                    desc="20% credit less notional tax at 19% => 16.2% payable")
    if scheme in ("eris", "sme-2023"):
        rate = 0.145 if scheme == "eris" else 0.10
        extra = qe * 0.86
        surr = min(loss + extra, qe * 1.86)
        return dict(extra_deduction=round(extra), surrenderable_loss=round(surr),
                    payable_credit=round(surr * rate),
                    desc=f"86% additional deduction; {rate*100:.1f}% payable credit on surrendered loss")
    raise ValueError(scheme)


def line(cat, desc, claimed, ok, note=""):
    return dict(cat=cat, desc=desc, claimed=claimed, ok=ok, note=note)


CLAIMS = {}


def claim(cid, company, period, regime_year, scheme_claimed, scheme_ok, staff, lines,
          loss_claimed=None, loss_ok=None, turnover=None, total_expenditure=None, total_expenditure_ok=None, notes=None):
    CLAIMS[cid] = dict(company=company, period=period, regime_year=regime_year,
                       scheme_claimed=scheme_claimed, scheme_ok=scheme_ok, staff=staff, lines=lines,
                       loss_claimed=loss_claimed, loss_ok=loss_ok, turnover=turnover,
                       total_expenditure=total_expenditure, total_expenditure_ok=total_expenditure_ok, notes=notes or [])


Y1, Y2 = "2024-25", "2025-26"

# ---------------------------------------------------------------- C01 Corvanta (A)
claim("C01", "Corvanta Bioscience Ltd", "1 Apr 2024 – 31 Mar 2025", Y1, "eris", "eris",
      [staff_row("Dr Imogen Saltash", "CSO / competent professional", 92000, 0.85, Y1),
       staff_row("Dr Ravi Penhallow", "Senior Scientist, enzyme engineering", 61000, 0.95, Y1),
       staff_row("Dr Aoife Kernick", "Scientist, immobilisation chemistry", 52000, 0.95, Y1),
       staff_row("Tomasz Brell", "Research Associate", 36500, 1.00, Y1),
       staff_row("Hannah Quarles", "Research Associate", 34000, 1.00, Y1),
       staff_row("Leon Fairhurst", "Analytical Chemist (HPLC/GC)", 41000, 0.70, Y1),
       staff_row("Marcus Venn", "CEO", 98000, 0.10, Y1, note="technical planning meetings only"),
       staff_row("Priya Odedra", "Lab Manager (QIA: maintenance/safety)", 39000, 0.40, Y1)],
      [line("Consumables", "Enzymes, resins, substrates, solvents, chromatography columns", 148400, 148400),
       line("Consumables", "Lab utilities (metered, apportioned)", 11900, 11900),
       line("Subcontract (UK, unconnected)", "Univ. of Calderbridge – cryo-EM structural work £56,000 x 65%", 36400, 36400),
       line("EPW (unconnected)", "Agency lab technician £28,500 x 65%", 18525, 18525),
       line("Software", "Molecular modelling licence (100% R&D use)", 14200, 14200),
       line("Data & cloud", "GPU compute for structure prediction", 9300, 9300)],
      loss_claimed=1490000, loss_ok=1490000, turnover=210000, total_expenditure=1700000, total_expenditure_ok=1700000)

# ---------------------------------------------------------------- C02 Thistlebrook (B)
claim("C02", "Thistlebrook Precision Engineering Ltd", "1 Oct 2024 – 30 Sep 2025", Y2, "merged-profit", "merged-profit",
      [staff_row("Dr Callum Ashdown", "Head of AM Engineering / competent professional", 78000, 0.75, Y2),
       staff_row("Sophie Treleaven", "Process Engineer (LPBF)", 52000, 0.90, Y2),
       staff_row("Dev Mistry", "Simulation Engineer (FEA/distortion)", 56000, 0.90, Y2),
       staff_row("Gareth Pollock", "Machine Operator", 34000, 0.60, Y2, ok_pct=0.35, note="includes production builds"),
       staff_row("Lisa Okafor", "Metrology Technician", 36000, 0.50, Y2),
       staff_row("Neil Hambleton", "Managing Director", 110000, 0.25, Y2, ok_pct=0.10, note="mostly commercial")],
      [line("Consumables", "Ti-6Al-4V powder, build plates – R&D builds", 92000, 92000),
       line("Consumables", "Ti powder – validation builds B-423 to B-425", 61500, 0, "production stock; sold to customer"),
       line("Subcontract (unconnected)", "Präzisionsmesstechnik Halde GmbH – CT scanning £48,000 x 65%", 31200, 0, "overseas restriction; CT scanning available in UK"),
       line("Subcontract (UK, unconnected)", "Midshire AM Test Centre fatigue testing £40,000 x 65%", 26000, 26000),
       line("Software", "Build-simulation (FEA) software licences", 44000, 22000, "also used for routine customer quotes; 50%"),
       line("Software", "ERP / Microsoft 365 licences", 9800, 0, "general business software")],
      turnover=14800000)

# ---------------------------------------------------------------- C03 Marrowgate (C)
claim("C03", "Marrowgate Software Ltd", "1 Jan 2024 – 31 Dec 2024", Y1, "sme-2023", "sme-2023",
      [staff_row("Elena Varga", "CTO / competent professional", 105000, 0.70, Y1, ok_pct=0.35),
       staff_row("Kwame Asante", "Principal Engineer (ledger)", 88000, 0.90, Y1, ok_pct=0.60),
       staff_row("Rosie Tamworth", "Senior Engineer", 72000, 0.85, Y1, ok_pct=0.30),
       staff_row("Ben Lacey", "Engineer", 58000, 0.85, Y1, ok_pct=0.15),
       staff_row("Chen Wu", "Engineer", 56000, 0.85, Y1, ok_pct=0.15),
       staff_row("Freya Doyle", "Frontend Engineer", 54000, 0.80, Y1, ok_pct=0.0, note="UI redesign – routine"),
       staff_row("Sam Okoro", "DevOps Engineer", 64000, 0.75, Y1, ok_pct=0.10, note="cloud migration – routine"),
       staff_row("Jessica Harrow", "Product Manager", 70000, 0.60, Y1, ok_pct=0.0, note="product mgmt not QIA"),
       staff_row("Oliver Marrow", "CEO", 120000, 0.40, Y1, ok_pct=0.0)],
      [line("EPW (unconnected)", "Contract developers via agency £96,000 x 65%", 62400, 15600, "only 25% on ledger project"),
       line("Software", "JetBrains, GitHub, Jira, Figma, Slack, Salesforce", 38600, 6200, "Salesforce/Figma/Slack not R&D"),
       line("Data & cloud", "AWS cloud computing", 184000, 21000, "only test cluster for ledger experiments"),
       line("Subcontract (UK, unconnected)", "Open Banking aggregator integration – Plaidwise Ltd £30,000 x 65%", 19500, 0, "routine integration")],
      loss_claimed=1450000, loss_ok=1450000, turnover=3100000)

# ---------------------------------------------------------------- C04 Hollin & Rye (D)
claim("C04", "Hollin & Rye Kitchens Ltd", "1 Apr 2024 – 31 Mar 2025", Y1, "merged-profit", "merged-profit",
      [staff_row("Marcus Rye", "Executive Chef & Director", 85000, 0.60, Y1, ok_pct=0.0),
       staff_row("Isla Hollin", "Managing Director", 90000, 0.30, Y1, ok_pct=0.0),
       staff_row("Tobias Wren", "Head Chef, Leeds", 42000, 0.50, Y1, ok_pct=0.0),
       staff_row("Carmen Ruiz", "Head Chef, York", 41000, 0.50, Y1, ok_pct=0.0),
       staff_row("Kitchen brigade (14 FTE)", "Sous/line chefs", 378000, 0.25, Y1, ok_pct=0.0, pension_pct=0.03),
       staff_row("Ella Brandt", "Food Technologist (contract-to-perm)", 38000, 0.80, Y1, ok_pct=0.20, note="shelf-life work for retail range is borderline")],
      [line("Consumables", "Ingredients for menu development", 64000, 0, "food served/sold; menu dev not R&D"),
       line("Consumables", "Sous-vide and fermentation equipment", 22500, 0, "capital"),
       line("Subcontract (UK, unconnected)", "Shelf-life microbiology testing – Fenbridge Food Labs £12,000 x 65%", 7800, 7800, "borderline-qualifying")],
      turnover=6200000)

# ---------------------------------------------------------------- C05 Brackenmoor (D)
claim("C05", "Brackenmoor Groundworks Ltd", "1 Aug 2024 – 31 Jul 2025", Y2, "merged-profit", "merged-profit",
      [staff_row("Darren Kettlewell", "Director", 95000, 0.70, Y2, ok_pct=0.0),
       staff_row("Paul Kettlewell", "Director / Contracts Manager", 88000, 0.60, Y2, ok_pct=0.0),
       staff_row("Amira Saleh", "Site Engineer", 48000, 0.80, Y2, ok_pct=0.05),
       staff_row("Site operatives (11 FTE)", "Groundworkers", 396000, 0.20, Y2, ok_pct=0.0, pension_pct=0.03),
       staff_row("Jade Holroyd", "Estimator", 44000, 0.50, Y2, ok_pct=0.0)],
      [line("Subcontract (UK, unconnected)", "Pennine Structural Consultants – basement design £84,000 x 65%", 54600, 0, "design fee charged to client; routine engineering"),
       line("Consumables", "Concrete, sheet piles, rebar for Hallam Rd basement", 212000, 0, "materials incorporated in client's building"),
       line("Consumables", "Plant hire", 46000, 0, "not consumable")],
      turnover=11400000)

# ---------------------------------------------------------------- C06 Lantern Lane (E)
claim("C06", "Lantern Lane Joinery Ltd", "1 Apr 2024 – 31 Mar 2025", Y1, "merged-profit", "merged-profit",
      [staff_row("Craig Lantern", "Director", 12570, 1.00, Y1, ok_pct=0.0, pension_pct=0.0,
                 extra={"dividends": 48000}, note="salary + dividends claimed as staff cost"),
       staff_row("Michelle Lantern", "Director / Company Secretary", 12570, 0.80, Y1, ok_pct=0.0, pension_pct=0.0,
                 extra={"dividends": 30000}),
       staff_row("Josh Pearce", "Joiner", 31000, 0.70, Y1, ok_pct=0.0),
       staff_row("Kieran Doyle", "Apprentice Joiner", 16000, 0.70, Y1, ok_pct=0.0)],
      [line("Consumables", "CNC router (Bramwell 2030 Pro)", 38500, 0, "capital equipment"),
       line("Consumables", "Oak, walnut, MDF, finishes – prototype and development materials", 41200, 0, "used in sold furniture"),
       line("Software", "CAD/CAM licence", 2400, 0, "routine design"),
       line("Other", "Van lease & fuel", 9600, 0, "excluded")],
      turnover=640000, notes=["First claim – no Claim Notification Form filed (claim invalid)"])

# ---------------------------------------------------------------- C07 Quillon (B)
claim("C07", "Quillon Hydrogen Ltd", "1 Jan 2025 – 31 Dec 2025", Y2, "eris", "merged-loss",
      [staff_row("Dr Nadia Fenwick", "CTO / competent professional", 98000, 0.80, Y2),
       staff_row("Dr Joel Abernethy", "Electrochemist", 64000, 0.95, Y2),
       staff_row("Dr Sun-Hee Park", "Materials Scientist (ionomers)", 62000, 0.95, Y2),
       staff_row("Felix Morgan", "Test Engineer", 47000, 0.90, Y2),
       staff_row("Ruth Akinola", "Test Engineer", 45000, 0.90, Y2),
       staff_row("Harriet Lowe", "CEO", 115000, 0.15, Y2),
       staff_row("Owen Bryce", "Commercial Director", 90000, 0.10, Y2, ok_pct=0.0, note="sales only")],
      [line("Consumables", "Membranes, catalyst-coated substrates, PTL titanium, iridium", 236000, 236000),
       line("Subcontract (unconnected)", "Stichting Waterstof Testlab – accelerated stress testing £120,000 x 65%", 78000, 0, "overseas; 'only facility' is availability, not a permitted condition"),
       line("Subcontract (UK, unconnected)", "University of Tyneford XPS surface analysis £22,000 x 65%", 14300, 14300),
       line("Software", "COMSOL-style multiphysics licence", 18000, 18000),
       line("Data & cloud", "Test-rig telemetry storage", 4200, 4200)],
      loss_claimed=1900000, loss_ok=1900000, turnover=380000,
      total_expenditure=2250000, total_expenditure_ok=2670000,
      notes=["Claims ERIS at 31.8% intensity by excluding £420k of 'pilot plant' costs from the denominator; "
             "correct intensity is below 30% once denominator is restored AND overseas cost removed -> merged-loss (16.2%) not ERIS",
             "Innovate UK grant £450k – correctly noted; no restriction under merged scheme/ERIS"])

# ---------------------------------------------------------------- C08–C10 Holt group (E)
# The same five engineers work on 'Project Lodestar'. They are employed by Holt Engineering Services (C10),
# recharged at cost+15% to Holt Freight Intelligence (C08) who claims them as connected EPWs; Holt Data Labs (C09)
# claims as contractor for the same work; C10 also claims them as its own staff.
holt_staff = [("Dr Simon Achterberg", "Head of Data Science", 96000),
              ("Natasha Grieve", "ML Engineer", 74000),
              ("Imran Qadir", "ML Engineer", 71000),
              ("Bethany Coles", "Data Engineer", 63000),
              ("Luke Fensome", "Platform Engineer", 66000)]


def holt_cost(sal):
    return sal + nic(sal, Y1) + round(sal * 0.05)


holt_total = sum(holt_cost(s) for _, _, s in holt_staff)

claim("C08", "Holt Freight Intelligence Ltd", "1 Apr 2024 – 31 Mar 2025", Y1, "merged-profit", "merged-profit",
      [staff_row("Gavin Holt", "Director", 140000, 0.30, Y1, ok_pct=0.05),
       staff_row("Priyanka Mehta", "Product Owner, Lodestar", 68000, 0.70, Y1, ok_pct=0.20)],
      [line("EPW (connected)", "Holt Engineering Services Ltd – Lodestar engineering staff recharge (5 FTE)", round(holt_total * 1.15), round(holt_total * 0.35),
            "connected EPW = lower of payment and provider cost; and only genuinely-qualifying ~35% of Lodestar work (much is off-the-shelf model tuning)"),
       line("Subcontract (connected)", "Holt Data Labs – 'forecasting model development' £210,000", 210000, 0, "same work as EPW line – double count"),
       line("Data & cloud", "Azure ML compute & telematics dataset licence", 88000, 30000, "production inference excluded")],
      turnover=22500000)

claim("C09", "Holt Data Labs Ltd", "1 Apr 2024 – 31 Mar 2025", Y1, "eris", "none",
      [staff_row("Gavin Holt", "Director", 140000, 0.40, Y1, ok_pct=0.0),
       staff_row("Dr Simon Achterberg", "Chief Scientist (seconded)", 96000, 0.90, Y1, ok_pct=0.0, note="same person employed by C10"),
       staff_row("Natasha Grieve", "ML Engineer (seconded)", 74000, 0.90, Y1, ok_pct=0.0, note="same person employed by C10")],
      [line("Data & cloud", "Azure ML compute (recharged)", 88000, 0, "duplicate of C08 cost"),
       line("Subcontract (UK, connected)", "Holt Engineering Services – modelling support £140,000", 140000, 0, "same engineers again")],
      loss_claimed=410000, loss_ok=0, turnover=210000, total_expenditure=620000,
      notes=["C09 was contracted by C08 to do the work: under the merged scheme the customer (C08) claims, not the contractor",
             "Claims ERIS as a standalone SME; with the group linked it is not an SME-eligible standalone and is not loss-making on a group basis (ERIS group intensity test)",
             "Loss is artificial: intra-group fee to C10 creates the loss"])

claim("C10", "Holt Engineering Services Ltd", "1 Apr 2024 – 31 Mar 2025", Y1, "merged-profit", "none",
      [staff_row(n, r, s, 0.95, Y1, ok_pct=0.0, note="employed here; recharged to C08 and C09") for n, r, s in holt_staff]
      + [staff_row("Gavin Holt", "Director", 140000, 0.30, Y1, ok_pct=0.0)],
      [line("Software", "Databricks-style platform licence", 52000, 0, "recharged to C08")],
      turnover=1350000,
      notes=["C10 is a staff provider: it carries on no R&D of its own; the staff costs belong in the customer's claim (once)"])


# ---------------------------------------------------------------- C11 Excelcion (C)
claim("C11", "Excelcion Limited", "1 Apr 2025 – 31 Mar 2026", Y2, "merged-profit", "merged-profit",
      [staff_row("Scott Lam", "Head of Research and Innovation", 118000, 0.50, Y2, ok_pct=0.30, note="Growth Fund oversight"),
       staff_row("Dermot McGregor", "Chief Digital and Information Officer", 185000, 0.40, Y2, ok_pct=0.10),
       staff_row("Ewa Walsh", "Group Technical Director", 176000, 0.20, Y2, ok_pct=0.05),
       staff_row("Ian Ritchie", "Principal Data Scientist", 92000, 0.90, Y2, ok_pct=0.70),
       staff_row("Applied AI and Automation team (12 FTE)", "Engineers / data scientists", 912000, 0.85, Y2, ok_pct=0.35,
                 note="includes rollout & support of approved AI assistant"),
       staff_row("Digital Delivery – Keystone & Lighthouse (18 FTE)", "Developers / analysts", 1242000, 0.60, Y2, ok_pct=0.0,
                 note="ERP automation & data platform – routine IT"),
       staff_row("Water: hydraulic modelling (10 FTE)", "Hydraulic modellers", 640000, 0.55, Y2, ok_pct=0.20,
                 note="mostly fee-earning scheme modelling"),
       staff_row("Buildings: mechanical engineers, dense-compute cooling (9 FTE)", "Mechanical engineers", 621000, 0.50, Y2, ok_pct=0.05,
                 note="client data-centre design, billed")],
      [line("EPW (connected)", "Tarnbeck Modelling Services Ltd – surrogate-model modellers recharge", 482000, round(455000*0.6),
            "connected: lower of payment & provider cost; only surrogate R&D share"),
       line("EPW (connected)", "Halvorsen Pike Engineers Inc – data scientists, assistant evaluation", 310000, 0, "overseas restriction"),
       line("Software", "Approved AI assistant enterprise licences – 1,200 seats", 540000, 30000, "firm-wide productivity tool; only dev/eval seats"),
       line("Data & cloud", "Lighthouse data platform cloud consumption", 720000, 90000, "only experimental workloads"),
       line("Consumables", "Immersion-cooling test rig components & dielectric fluid", 38000, 38000),
       line("Subcontract (UK, unconnected)", "University of Weardale hydrology group – benchmark datasets £60,000 x 65%", 39000, 39000)],
      turnover=648000000,
      notes=["Cost history built from Keystone project codes via TAX_RD_EXTRACT; Growth Fund codes include fee-earning client work",
             "Narrative describes the approved third-party AI assistant as an in-house 'engineering reasoning engine'; the public website (Insights 2026-05-19) describes an approved assistant for drafting/summarising/calc-check support with 'uneven' results",
             "Prior enquiry into FY2022-23 claim closed with adjustment"])

# ---------------------------------------------------------------- output
def fmt(n):
    return f"£{n:,.0f}"


def render(cid, c):
    out = [f"# Cost schedule – {cid} {c['company']}", "",
           f"Period: {c['period']}  ·  NIC basis: {c['regime_year']}  ·  Scheme claimed: **{c['scheme_claimed']}**", ""]
    out += ["## Staff costs (as claimed)", "",
            "| Name | Role | Salary | Er NIC | Er pension | Total | R&D % | Claimed | Includes |",
            "|---|---|---:|---:|---:|---:|---:|---:|---|"]
    for s in c["staff"]:
        note = ("includes " + ", ".join(f"{k} {fmt(v)}" for k, v in s["extra"].items())) if s["extra"] else ""
        out.append(f"| {s['name']} | {s['role']} | {fmt(s['salary'])} | {fmt(s['nic'])} | {fmt(s['pension'])} | "
                   f"{fmt(s['total'])} | {s['pct']*100:.0f}% | {fmt(s['claimed'])} | {note} |")
    staff_claimed = sum(s["claimed"] for s in c["staff"])
    staff_ok = sum(s["ok"] for s in c["staff"])
    out += [f"| **Total staff** | | | | | | | **{fmt(staff_claimed)}** | |", ""]
    out += ["## Other qualifying expenditure (as claimed)", "", "| Category | Description | Claimed |", "|---|---|---:|"]
    for l in c["lines"]:
        out.append(f"| {l['cat']} | {l['desc']} | {fmt(l['claimed'])} |")
    other_claimed = sum(l["claimed"] for l in c["lines"])
    other_ok = sum(l["ok"] for l in c["lines"])
    qe_claimed = staff_claimed + other_claimed
    qe_ok = staff_ok + other_ok
    out += [f"| **Total other** | | **{fmt(other_claimed)}** |", "",
            f"## Total qualifying expenditure (as claimed): **{fmt(qe_claimed)}**", ""]
    b = benefit(c["scheme_claimed"], qe_claimed, c["loss_claimed"])
    out += [f"## Relief computation (as claimed) – {b.pop('desc')}", ""]
    for k, v in b.items():
        out.append(f"- {k.replace('_', ' ')}: {fmt(v)}")
    if c["turnover"]:
        out.append(f"- company turnover for context: {fmt(c['turnover'])}")
    if c["total_expenditure"]:
        out.append(f"- total relevant expenditure (claimed, for intensity): {fmt(c['total_expenditure'])}; "
                   f"intensity as claimed = {qe_claimed / c['total_expenditure'] * 100:.1f}%")
    if c["loss_claimed"]:
        out.append(f"- trading loss before R&D deduction: {fmt(c['loss_claimed'])}")
    out.append("")
    # corrected view
    if c["scheme_ok"] == "none":
        cb = {"desc": "no entitlement", "relief": 0}
        qe_ok = 0
    else:
        cb = benefit(c["scheme_ok"], qe_ok, c["loss_ok"])
    corrected = dict(staff_ok=staff_ok, other_ok=other_ok, qe_ok=qe_ok, scheme_ok=c["scheme_ok"], benefit_ok=cb)
    if c.get("total_expenditure_ok"):
        corrected["intensity_ok_pct"] = round(qe_ok / c["total_expenditure_ok"] * 100, 1)
    claimed = dict(staff=staff_claimed, other=other_claimed, qe=qe_claimed, scheme=c["scheme_claimed"],
                   benefit=benefit(c["scheme_claimed"], qe_claimed, c["loss_claimed"]))
    return "\n".join(out), claimed, corrected


def main():
    (ROOT / "plans/costs").mkdir(parents=True, exist_ok=True)
    key = {}
    for cid, c in CLAIMS.items():
        md, claimed, corrected = render(cid, c)
        (ROOT / f"plans/costs/{cid}.md").write_text(md + "\n")
        key[cid] = dict(company=c["company"], claimed=claimed, corrected=corrected, notes=c["notes"],
                        disallowed_lines=[l for l in c["lines"] if l["ok"] != l["claimed"]],
                        staff_adjustments=[{k: s[k] for k in ("name", "pct", "ok_pct", "claimed", "ok", "note", "extra")}
                                           for s in c["staff"] if s["ok"] != s["claimed"]])
        print(f"{cid} {c['company']:<40} QE claimed {fmt(claimed['qe']):>12}  ok {fmt(corrected['qe_ok']):>12}")
    (ROOT / "docs/answer-key-figures.json").write_text(json.dumps(key, indent=2))


if __name__ == "__main__":
    main()
