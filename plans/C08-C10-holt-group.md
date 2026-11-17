# C08–C10: the Holt group (intended grade **E** for all three: the same project claimed three times)

Three companies, **all wholly owned by Veridian Holt Holdings Ltd** (company no. ZZ009931), which is 100% owned by Gavin Holt.
Each files its own claim for the period 1 Apr 2024 – 31 Mar 2025, through a **different agent**, so that no single adviser sees the overlap.
All three describe **"Project Lodestar"**: ML-based freight demand forecasting and dynamic load-matching for a road-haulage marketplace.
Each pack must read as plausible **on its own**. The fraud appears only when they are read together.

## Shared facts (must be consistent across the three packs)
- Shared registered office: **Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS** (all three companies, and the parent).
- Gavin Holt is a director of all three. Do not mention the other companies' claims.
- The 5 Lodestar engineers (Dr Simon Achterberg, Natasha Grieve, Imran Qadir, Bethany Coles, Luke Fensome) are **employed by Holt Engineering Services Ltd (C10)**.
- An intra-group services agreement dated 2 April 2024 has C10 supplying staff to C08 at cost + 15%. A "modelling services agreement" dated 15 April 2024 has C09 delivering "forecasting model development" to C08 for £210k.
- Jira project key **LDS** (tickets `LDS-101`…`LDS-640`). All three packs cite LDS tickets, some identical (e.g. `LDS-214 "Temporal fusion model – lane-level demand"`, `LDS-377 "Cold-start for new shippers"`, `LDS-502 "Hierarchical reconciliation of forecasts"`).
- Technical substance: about 35% genuinely qualifying. A novel hierarchical reconciliation for sparse lane-level forecasts with a cold-start for new shippers counts. Most of the rest is applying off-the-shelf gradient-boosting and temporal-fusion-transformer models with hyper-parameter tuning, which counts as routine per HMRC CIRD81980 Case Study 2. All three narratives overclaim the routine parts.
- Data: 3.2 bn GPS telematics pings licensed from a fictional provider ("TrakSure Data Ltd"). The Azure ML subscription is held by C08 and re-invoiced to C09.
- **Reuse "tell" phrases across the three packs with light rewording** (the agents were given the same internal technical write-up). For example, the base sentence: *"Existing forecasting approaches assume dense, stationary demand signals; at lane level fewer than 8% of origin–destination pairs exhibit weekly volume sufficient for conventional models."* C08 uses it verbatim. C09 rewords it to "…under 8% of O-D pairs show enough weekly volume…". C10 says "…only around 8% of lanes…". Also reuse the "Lodestar competent professional statement" by Dr Achterberg in all three, nearly identical.

---

## C08: Holt Freight Intelligence Ltd (the customer: legitimate claimant for the ~35%, but grossly inflated)
Folder: `claims/C08-holt-freight/` · Costs: `plans/costs/C08.md` · merged scheme, profitable.
- Company no. ZZ009945, UTR 9999994512. Operates "Holtline", a digital freight marketplace. 64 staff (mostly ops and sales), turnover £22.5m.
- Agent: Vantrell Innovation Ltd (also the agent for C03, but a different team; this is incidental).
- Senior officer: Gavin Holt. Competent professional: Dr Simon Achterberg, "Head of Data Science (provided under group services agreement)".
- Projects: P1 Lodestar demand forecasting, and P2 "Dynamic load-matching optimisation" (a mostly routine OR solver configuration).
- **Planted:** a connected EPW recharge claimed at the full cost + 15%; a separate £210k "subcontract" to C09 claimed for the same work; all Azure, including production inference; Gavin Holt at 30%.
- Narrative about 6,500 words.

## C09: Holt Data Labs Ltd (the contractor: should not claim at all)
Folder: `claims/C09-holt-data-labs/` · Costs: `plans/costs/C09.md` · ERIS claimed.
- Company no. ZZ010277, UTR 9999927783. Incorporated **3 April 2024**, days before the Lodestar agreements. 2 direct employees (an office administrator and a junior analyst, neither claimed) plus "seconded" staff. Turnover £210k (the first instalments of the intra-group fee).
- Agent: Ferrowen R&D Consulting Ltd.
- Presents itself as an independent "AI research lab" that "undertook R&D on its own account to develop proprietary forecasting IP, subsequently licensed to group companies".
- Claims ERIS as a standalone loss-making SME with 76% intensity. It **does not mention** the group, its linked enterprises or the C08 contract except as "commercial licensing income".
- **Planted:** Achterberg and Grieve are claimed at 90% as "seconded staff" although they are employed and claimed by C10. A £140k "modelling support" fee to C10 is claimed as a connected subcontract. Azure costs re-invoiced from C08 are claimed. The incorporation date is suspicious. The CNF was filed on 12 Aug 2025 (first claim): section 02 shows it.
- Narrative about 5,500 words. It relabels Lodestar as "Project Polaris" in some places. Use "Polaris (delivered to group under Lodestar programme)" once so the tie can be found.

## C10: Holt Engineering Services Ltd (the staff provider: claims the same engineers as its own R&D)
Folder: `claims/C10-holt-engineering/` · Costs: `plans/costs/C10.md` · merged scheme, profitable.
- Company no. ZZ009958, UTR 9999995866. Employs the group's engineers and IT staff. Turnover £1.35m, almost entirely intra-group recharges.
- Agent: Tallowby & Crane Accountants (a generalist; thin R&D knowledge).
- Narrative frames its work as an "in-house engineering capability developing advanced analytics on behalf of the group", describing Lodestar as its own R&D programme ("Engineering Services R&D Programme 2024/25, including the Lodestar workstream").
- **Planted:** all 5 engineers at 95%, so that combined with C09 Achterberg and Grieve are at 185%. The company bears no risk and is reimbursed at cost + 15% (state the recharge as a "revenue stream"). Its platform licence is recharged to C08.
- No CNF needed: it "claimed in FY2022-23" (for a different, small IT project).
- Narrative about 4,500 words, the weakest technically.

## Cross-claim detection keys (for the answer key only; do not write these into the packs)
Shared address; shared director; shared Jira LDS ticket IDs; overlapping staff names with combined apportionment above 100%; the services-agreement dates; the C09 incorporation date; the same Azure costs; near-duplicate sentences; a combined benefit of about £272k against a legitimate figure of about £31k.
