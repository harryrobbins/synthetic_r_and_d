# Synthetic R&D tax claims (HMRC hackathon dataset)

There are 11 fictional UK R&D tax relief claim packs (about 10–17k words each, roughly 20–40 pages). They range from exemplary to fraudulent, and include a group of three companies claiming the same project.

- `claims/<ID>-<slug>/claim.md` holds the claim packs. **These are the only files to give to tools under test.**
- `docs/guide-to-rd-claims.md` is the participant briefing: the scheme, the anatomy of a claim, the grading rubric and the red-flag catalogue.
- `docs/cohort-plan.md` and `docs/answer-key.{md,json}` are **organiser-only** ground truth.
- `plans/` holds the per-claim writing plans and cost schedules used to generate the packs.
- `scripts/`:
  - `costs.py` produces the cost schedules and figures.
  - `answer_key.py` builds the answer key.
  - `assemble.py` concatenates sections into `claim.md`.
  - `check.py` checks the packs for consistency and safety.

```
python3 scripts/costs.py && python3 scripts/answer_key.py
python3 scripts/assemble.py && python3 scripts/check.py
```

## Which claims are legitimate? (organiser-only spoiler)

**Do not give this README to tools under test.** Give them only `claims/*/claim.md`. The full ground truth, with every planted issue, is in `docs/answer-key.md` and `docs/answer-key.json`.

A claim can fail in two ways. It can be **procedurally invalid**: no valid claim notification, so nothing is payable whatever the merits. Or it can be **overclaimed**: some or all of the costs or activities do not qualify. "Correct benefit" is what HMRC should pay after both checks.

| ID | Company | Grade | Verdict | What is legitimate | What is not | Benefit claimed → correct |
|---|---|---|---|---|---|---:|
| C01 | Corvanta Bioscience | A | **Legitimate** | All of it. A specific baseline, documented failures, timesheets, conservative exclusions and a genuine ERIS intensity of 35.3%. | Nothing. | £161,742 → £161,742 |
| C02 | Thistlebrook Precision | B | **Legitimate, overclaimed** | The thin-wall titanium heat-exchanger R&D. | Sold production batches claimed as "validation builds", a German CT lab (breaches the overseas rule), and general ERP and Microsoft 365 licences. | £79,124 → £55,994 |
| C03 | Marrowgate Software | C | **Partly legitimate** | Project 1, the Weft ledger. | The UI and LLM-API work (product or UX uncertainty only), the cloud migration and the API integration (routine), and all AWS hosting. | £163,788 → £37,329 |
| C04 | Hollin & Rye Kitchens | D | **Mostly illegitimate** | Only the shelf-life work, and that is borderline. | Menu development (business and sensory uncertainty), a chef as the "competent professional", food sold to diners, and capital kit. | £56,858 → £2,487 |
| C05 | Brackenmoor Groundworks | D | **Illegitimate: invalid** | Nothing payable. The claim notification was filed late (3 Feb 2026, deadline 31 Jan 2026). On the merits only about £2.8k of spend would qualify anyway. | A client-funded basement built to established practice, the client's designer, and materials built into the client's building. | £92,939 → £0 |
| C06 | Lantern Lane Joinery | E | **Illegitimate: invalid** | Nothing. A first claim with no notification. | Dividends as staff costs, a CNC machine, timber for sold orders, and a van. Boilerplate narrative. | £33,677 → £0 |
| C07 | Quillon Hydrogen | B | **Legitimate, wrong scheme** | The low-iridium electrolyser science, which is excellent. | The R&D intensity is gamed (true figure about 23.5%, below the 30% ERIS threshold), so the claim belongs on merged-loss. A Dutch test lab is disallowed. | £192,975 → £101,541 |
| C08 | Holt Freight Intelligence | E | **Fraudulent cluster, small legitimate core** | About 35% of Project Lodestar, claimed by this company as the customer. | Connected-company staff at cost + 15%, a "subcontract" to C09 for the same work, and production cloud costs. | £135,219 → £30,871 |
| C09 | Holt Data Labs | E | **Illegitimate (duplicate)** | Nothing. As the contractor it cannot claim; C08 claims. | A shell company claiming the same project as "Polaris", with engineers that C10 also claims (185% combined) and a re-invoiced Azure bill. | £118,499 → £0 |
| C10 | Holt Engineering Services | E | **Illegitimate (duplicate)** | Nothing. It is a staff provider that bears no R&D risk. | The same engineers, already recharged to and claimed by C08. | £76,970 → £0 |
| C11 | Excelcion Limited | C | **Partly legitimate, contradicts its website** | The core of P2 (flood surrogate modelling) and the P3 test rig. | The firm-wide rollout of a third-party AI assistant presented as "proprietary" R&D, US overseas staff, fee-earning client work, and ERP IT with £720k of cloud. | £756,946 → £179,266 |

In short: **C01 is clean. C02 and C07 are genuine but overclaimed. C03 and C11 are padded around a real core. C04 is almost entirely ineligible. C05 and C06 are invalid outright. C08–C10 are one project claimed three times**, about £331k claimed against about £31k legitimate, all of it in C08.

**Cross-claim links to detect:** the Holt cluster (C08–C10) shares an address, a director, Jira IDs, engineers, an Azure bill and wording. C04–C06 share one agent's boilerplate. C03 and C08 share an agent too, but that is a deliberate red herring.

**Safety.** Every company, person, product and figure is invented. Identifiers are deliberately invalid: company numbers use the `ZZ` prefix, UTRs are `99999…`, and postcodes use the `ZZ` area. So none can match a real entity, and none would pass a real HMRC or Companies House check. Every pack carries a "SYNTHETIC TEST DATA" banner.

**The exception is Excelcion (C11).** It is a synthetic company with its own (access-controlled) website at `www.excelcion.co.uk`, so that web-search tools can test claims against a public footprint.
