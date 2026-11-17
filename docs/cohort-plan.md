# Cohort plan: 11 synthetic R&D claims

**Organiser-only.** This file reveals the intended grades. Give hackathon tools only `claims/*/claim.md`, never `docs/` or `plans/`.

All entities are fictional. Identifiers are deliberately invalid: company numbers use the non-existent `ZZ` prefix, UTRs are `99999…`, and postcodes use the non-existent `ZZ` area. Excelcion is the one company with a (synthetic) web presence: `www.excelcion.co.uk`.

| ID | Company | Sector / activity | Period | Scheme claimed | Agent | Grade | One-line story |
|---|---|---|---|---|---|---|---|
| C01 | Corvanta Bioscience Ltd | Biotech: immobilised enzymes for flow biocatalysis | Apr 24–Mar 25 | ERIS | Halyard & Finch LLP | **A** | Textbook: specific baseline, documented failures, timesheets, and conservative exclusions stated. |
| C02 | Thistlebrook Precision Engineering Ltd | Metal additive manufacturing: thin-wall Ti heat exchangers | Oct 24–Sep 25 | Merged (profit) | In-house | **B** | Genuine R&D. Production batches, an overseas CT lab and general software are left in the costs. |
| C03 | Marrowgate Software Ltd | Fintech SaaS: reconciliation | Jan–Dec 2024 | SME (pre-merged) | Vantrell Innovation | **C** | One strong ledger project, padded with a UI redesign, a cloud migration and an API integration. All AWS hosting is claimed. |
| C04 | Hollin & Rye Kitchens Ltd | Restaurants: menu development | Apr 24–Mar 25 | Merged (profit) | Quorlane R&D Partners | **D** | The chef is the "competent professional". Menu trials and food sold to customers are claimed. Only the shelf-life work is borderline. |
| C05 | Brackenmoor Groundworks Ltd | Construction: a client basement | Aug 24–Jul 25 | Merged (profit) | Quorlane R&D Partners | **D** | Client-funded routine engineering. The client's designer and building materials are claimed. **Late CNF, so the claim is invalid.** |
| C06 | Lantern Lane Joinery Ltd | Bespoke joinery | Apr 24–Mar 25 | Merged (profit) | Quorlane R&D Partners | **E** | Boilerplate. Dividends, a CNC machine, timber and a van are claimed. **No CNF on a first claim, so it is invalid.** |
| C07 | Quillon Hydrogen Ltd | Clean tech: low-iridium PEM electrolysers | Jan–Dec 2025 | ERIS | Osterby Tax Advisory | **B** | Excellent science. The ERIS intensity is gamed (the denominator is cut) and a Dutch test lab is included in breach of the overseas rule. The claimant should be on merged-loss. |
| C08 | Holt Freight Intelligence Ltd | Logistics ML: freight demand forecasting | Apr 24–Mar 25 | Merged (profit) | Vantrell Innovation | **E** | The legitimate customer for "Lodestar", but it claims the connected EPW at cost + 15% **and** a subcontract to C09 for the same work. |
| C09 | Holt Data Labs Ltd | Same project ("Polaris"/Lodestar) | Apr 24–Mar 25 | ERIS | Ferrowen R&D Consulting | **E** | Shell company incorporated days before the work. It is the contractor and claims as if independent, using "seconded" staff that C10 also claims. |
| C10 | Holt Engineering Services Ltd | Same project (staff provider) | Apr 24–Mar 25 | Merged (profit) | Tallowby & Crane | **E** | Claims the same 5 engineers at 95% as its own R&D, while recharging them to C08. |
| C11 | **Excelcion Limited** | Engineering consultancy: AI calculation checking, flood surrogates, cooling, ERP | Apr 25–Mar 26 | Merged (large) | Arbery Lisle LLP | **C** | Real Growth Fund research, inflated by the firm-wide AI assistant rollout, fee-earning client work, ERP IT and overseas US staff. **The claim contradicts the public website.** |

## Design coverage

- **Grade spread:** A×1, B×2, C×2, D×2, E×4 (three of the E grades are the Holt cluster).
- **Schemes:** ERIS ×3 (C01 correct, C07 wrong, C09 ineligible), merged profitable ×6, merged large ×1, legacy SME ×1.
- **Sectors:** biotech, advanced manufacturing, software/fintech, hospitality, construction, craft, clean energy, logistics/ML, engineering consultancy.
- **Cross-claim links to detect:**
  1. The **Holt cluster** (C08/C09/C10): shared address, director, Jira IDs, staff, Azure costs and near-duplicate sentences.
  2. The **Quorlane boilerplate** (C04/C05/C06): identical sentences across three unrelated claimants. Typical of agent-farmed claims.
  3. A weak, incidental link: the **Vantrell** agent is used by both C03 and C08. It is a red herring; not every shared agent means fraud.
- **Process validity:** C05 has a late CNF and C06 has no CNF, so both are invalid before merits are considered.
- **Web-footprint tests:** C11 Excelcion. Its website shows the Insights essays, AI-pilot news, leadership and markets. Use it to confirm or contradict claimed activity.

## Pipeline

1. `scripts/costs.py`: the deterministic cost schedules → `plans/costs/<ID>.md` and `docs/answer-key-figures.json`.
2. `plans/<ID>.md`: the per-claim plans (narrative content, planted issues, length). `plans/_writer-brief.md` holds the shared rules.
3. One Haiku agent per claim writes `claims/<ID>-<slug>/sections/*.md`.
4. `scripts/assemble.py`: concatenates the sections into `claims/<ID>-<slug>/claim.md`.

To regenerate one claim: re-run its writer agent with the same three input files.
