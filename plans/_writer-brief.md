# Writer brief (read first): synthetic R&D claim packs

You are writing **one synthetic UK R&D tax relief claim pack** for an HMRC hackathon. The pack will be used to test tools that triage and risk-assess claims.
Every company, person, product, address and number is **fictional**. Do not use real company names, real products or real people.
You may mention generic technologies (Python, Kubernetes, LPBF, HPLC, PEM electrolysis). Fictionalise any software vendor names that are not generic ("a COMSOL-style multiphysics package" is fine).

## Voice

Write **as the claimant and its R&D tax adviser would**: confident and persuasive, using the language of the DSIT Guidelines (advance, uncertainty, competent professional, baseline).
**Never** state, hint or admit that anything is wrong, overclaimed or questionable. The planted weaknesses in your claim plan must show up *naturally* in the content: vague baselines, business-type uncertainties, generous apportionments, ineligible costs listed with confidence. A reviewer must *find* them, not be told about them.
Use UK English and UK formats (£, dd Month yyyy, "programme", "organisation").

## Mandatory structure: one markdown file per section, in the claim's folder

Write these files to `claims/<CID>-<slug>/sections/` (the plan gives the exact folder):

| File | Section | Target length |
|---|---|---|
| `01-cover.md` | Cover sheet & claim summary | 300–500 words |
| `02-claim-notification.md` | Claim Notification Form, *or* a note on why one was not needed / is absent (follow the plan) | 150–400 words |
| `03-aif.md` | Additional Information Form: company, contact, agent, senior officer, cost totals by category, and per-project fields (main field of science/technology, baseline, advance sought, uncertainties, how and when resolved). AIF free-text fields are short (about 100–250 words each). | 1,200–2,500 words |
| `04-company-background.md` | Company background, ownership, group, funding, staff and facilities | 800–1,500 words |
| `05-technical-narrative.md` | Full technical report, project by project: baseline, advance, uncertainties, methodology, chronological work log with dated iterations, outcomes, boundaries (start/end), competent professional statement | **4,000–9,000 words** (the bulk; follow the plan's length) |
| `06-costs.md` | Cost methodology and schedules. **Reproduce the tables from `plans/costs/<CID>.md` exactly; do not change any figure.** Add methodology prose explaining apportionment (timesheets, Jira, interviews, estimates, per the plan) and the relief computation. | 1,200–2,500 words |
| `07-appendices.md` | Competent professional CV(s), evidence index (document IDs, dates, descriptions), timesheet extract (consistent with the apportionments), invoice/supplier list, director's declaration | 1,500–3,000 words |

Total: **9,000–18,000 words** (roughly 20–40 pages).

Headings: each file starts with an H2 (`## 3. Additional Information Form`). File 01 also starts with this banner line:
`> SYNTHETIC TEST DATA – FICTIONAL COMPANY – PREPARED FOR HMRC HACKATHON – NOT A REAL TAX CLAIM`

## Consistency rules

- Names, roles, salaries, percentages and totals must match `plans/costs/<CID>.md` and the claim plan everywhere they appear: the AIF, the narrative, the costs and the appendices.
- Dates must sit inside the accounting period, except background and "work started before the period" context.
- Synthetic identifiers are deliberately **invalid**, so they can never match a real entity. Company numbers use the non-existent prefix `ZZ` plus 6 digits. UTRs are `99999` plus 5 digits. Postcodes use the non-existent area `ZZ` (e.g. `ZZ24 9XQ`). Use exactly the identifiers in the plan. Invent any other identifier (VAT, PAYE ref, bank details) in the same spirit: VAT `GB 999 …`, PAYE `999/ZZ…`, sort code `00-00-xx`.
- Evidence references follow the plan's scheme (e.g. `CVB-LB-0412` for lab book pages).
- Do not write an answer key, a "risk" section or any meta-commentary. Do not mention the hackathon anywhere except the banner.

## Process

1. Read the claim plan (`plans/<CID>.md`) and its cost schedule (`plans/costs/<CID>.md`).
2. Write the section files one by one with the Write tool. Write the technical narrative in **two or more Write calls** if needed (for example `05a-…md` and `05b-…md`), so each call stays manageable.
3. When finished, run `python3 scripts/assemble.py <CID>`. It concatenates the sections into `claims/<CID>-<slug>/claim.md`.
4. Reply with a short summary: the files written, an approximate word count, and any plan detail you could not follow.
