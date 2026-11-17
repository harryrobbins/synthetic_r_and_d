# Guide & rubric: understanding UK R&D tax relief claims

> **Purpose.** A briefing for HMRC hackathon participants working with the synthetic claim cohort in `claims/`.
> It explains what a claim contains, what makes it qualify, and how to grade it.
> Every company, person, product and figure in the cohort is **fictional**.
> The one deliberate exception is **Excelcion**: a synthetic company with a real website
> (`www.excelcion.co.uk`), so tools can test whether a claimant's public footprint matches its claim.
>
> **The legal summary below is simplified for the hackathon.** Before you rely on a rate or rule,
> check it against the HMRC manuals (CIRD80000+) and GOV.UK guidance.

---

## 1. The scheme in one page

| Concept | What it means |
|---|---|
| **Definition of R&D** | Set by the *Guidelines on the Meaning of R&D for Tax Purposes* (DSIT, originally DTI 2004). A project counts as R&D if it **seeks an advance in science or technology** by **resolving scientific or technological uncertainty**. |
| **Advance** | Knowledge or capability that is *not readily deducible* by a **competent professional** in the field. It must be an advance in the overall field, not just for the company. Novel products built with existing tech are not, by themselves, an advance. |
| **Uncertainty** | The competent professional cannot readily know whether something is technically possible, or how to achieve it. *Business* uncertainty (will it sell? can we deliver on time or on budget?) does not count. |
| **Competent professional** | A named person with relevant, current expertise who can credibly judge the baseline. A director with no technical background is a weak competent professional. |
| **Project boundaries** | R&D starts when work to resolve the uncertainty begins. It ends when the uncertainty is resolved or the work is abandoned. Commercial production, routine testing, deployment, marketing and QA after resolution are out. |
| **Qualifying indirect activities (QIAs)** | Some support work counts, such as scientific or technical planning, information services and certain maintenance and security (Guidelines paras 31–33). General administration, HR and finance are out. |
| **Science** | Excludes arts, humanities and social sciences (including economics). Pure maths counts (from April 2023). |

### Regimes (by accounting period start date)

| Period starting | Scheme | Headline rates |
|---|---|---|
| Before 1 Apr 2023 | SME scheme / RDEC | SME: 130% extra deduction, 14.5% payable credit. RDEC 13%. |
| 1 Apr 2023 – 31 Mar 2024 | SME scheme / RDEC | SME: 86% extra deduction, 10% payable credit, or 14.5% for **R&D-intensive** loss-makers (≥40% intensity). RDEC 20%. |
| On/after 1 Apr 2024 | **Merged scheme** (RDEC-style) + **ERIS** | Merged: 20% taxable expenditure credit. Net about 15% at the 25% CT rate; notional 19% for loss-makers. **ERIS**: R&D-intensive loss-making SMEs (≥30% intensity) get an 86% extra deduction and a 14.5% payable credit. |

### Process requirements

- **Claim Notification Form (CNF):** needed for a first claim, or if no claim was made in the previous 3 years. It is due within 6 months of the period end (for periods from 1 Apr 2023). If it is missing, the claim is invalid.
- **Additional Information Form (AIF):** mandatory for all claims from 8 Aug 2023. It lists the projects (field of science, baseline, advance, uncertainty, how it was resolved), cost categories, the agent and the senior officer. If the AIF is missing, the claim is invalid.
- **CT600:** the claim figures go in the CT600 and its R&D supplement (CT600L).

### Qualifying cost categories

| Category | Rule of thumb | Common abuse |
|---|---|---|
| **Staff costs** | Salary, employer NIC and employer pension for time spent directly on R&D or QIAs. Benefits in kind and dividends are excluded. | Directors claimed at 80–100% when they also run sales. Dividends included. Office or admin staff included. Total apportionment above 100% across group companies. |
| **Externally provided workers (EPWs)** | Unconnected: 65% of the payment. Connected: the lower of the payment and the staff provider's cost. | Connected recharges with markup. The same people counted again as the provider's own staff. |
| **Subcontracted R&D** | Unconnected: 65% of the payment. Connected: the lower of the payment and the subcontractor's relevant cost. Merged scheme: the company that *decides to do the R&D* claims, not the contractor. From Apr 2024, the work must be done in the UK. The exceptions are narrow: geographic, environmental or legal conditions only, never cost or the availability of staff. | Contractor claims for work it was commissioned to do. Overseas developers included. Client-funded work claimed by the contractor. |
| **Consumables** | Materials consumed or transformed in R&D. Not production stock that is later sold. | Production runs or saleable goods included. |
| **Software** | Licences used directly in R&D, apportioned. | General Office or CRM licences included at 100%. |
| **Data & cloud** (from Apr 2023) | Datasets, and compute and storage used for R&D. Not general hosting. | All production AWS bills claimed. |
| **Excluded** | Capital items (these may qualify for capital allowances instead), rent, rates, patent costs, travel, entertainment, marketing. | CNC machines, laptops, rent and patent attorney fees slipped into "consumables". |

---

## 2. Anatomy of a claim pack in this cohort

Each claim in `claims/<claim-id>/` is a single markdown document (10–50 pages equivalent) with these parts:

1. **Cover & claim summary:** company, UTR (synthetic), period, scheme, the agent, and the headline figures as they would appear on the CT600/CT600L.
2. **Claim Notification Form** (where the claim needs one): may be missing or late in questionable claims.
3. **Additional Information Form:** structured fields per project.
4. **Company background:** business model, headcount, group structure, funding and grants.
5. **Technical narrative report:** per project, written as if by or with the competent professional. This is the bulk of the document.
6. **Cost methodology & schedules:** staff tables with apportionments, EPWs, subcontractors, consumables, software, data/cloud, and the computation of the relief.
7. **Appendices:** competent professional CV, evidence index (lab books, Jira, test logs), timesheet extract, invoice list and declarations.

The **ground truth** for each claim (its intended grade, the planted issues, and the evidence of each) is in `docs/answer-key.md` and `docs/answer-key.json`. **Keep these hidden from any tool being evaluated.**

---

## 3. Grading rubric

Each claim gets an overall grade from **A to E** on a legitimacy scale:

| Grade | Label | Description | Expected HMRC outcome |
|---|---|---|---|
| **A** | Exemplary | Clear baseline, a genuine advance and uncertainty, contemporaneous evidence, a credible competent professional, conservative apportionment, correct scheme and costs. | Accept. No enquiry, or a light-touch check. |
| **B** | Sound with errors | Genuine R&D, but with technical errors in the costs (wrong scheme, an ineligible category, overseas costs, over-generous boundaries). | Accept after adjusting the costs. |
| **C** | Mixed / overclaimed | Some genuine R&D, padded with routine work, commercial activity or an inflated apportionment. Large parts would be disallowed. | Enquiry. Partial disallowance. |
| **D** | Largely non-qualifying | Ordinary business or trade activity dressed in R&D language. Little or no true technological uncertainty, or the uncertainty is a business one. | Enquiry. Most or all disallowed. Possible careless-error penalties. |
| **E** | Abusive / fraudulent | Fabricated or duplicated activity, costs claimed twice across entities, invented staff, boilerplate narratives, deliberate misclassification. | Full disallowance. Deliberate-behaviour penalties. Possible criminal referral. |

### Scoring dimensions (score each from 0 to 3)

| # | Dimension | 3 = strong | 0 = absent/failing |
|---|---|---|---|
| D1 | **Baseline** | Specific state of the art, citing named public techniques and their limits. | Generic ("no existing solution did X"). |
| D2 | **Advance in the field** | Advance in the field, explained relative to the baseline. | Advance only for the company, or a new product rather than new knowledge. |
| D3 | **Technological uncertainty** | Specific technical unknowns a competent professional could not resolve. | Business, cost or timescale risk, or "it was challenging". |
| D4 | **Systematic resolution** | Hypotheses, experiments, iterations and failures documented with dates. | A success story with no failures, written after the event. |
| D5 | **Competent professional** | Named, qualified, active in the field, and credible about the baseline. | Not named, or the MD with no domain background. |
| D6 | **Boundaries** | Clear start and end points, with routine work excluded explicitly. | The whole commercial project is claimed. |
| D7 | **Cost accuracy** | Categories and apportionments are justified and add up. The correct scheme and rates are used. | Arithmetic errors, ineligible costs, apportionment above 100%. |
| D8 | **Evidence & consistency** | The evidence index matches the narrative. Dates, headcount and the public footprint are coherent. | Contradictions with the accounts, the website, Companies House or other claims. |

Rough mapping: a total of 21–24 is A, 16–20 B, 10–15 C, 5–9 D, and 0–4 E. **Any confirmed duplication or fabrication means grade E, whatever the score.**

---

## 4. Red-flag catalogue (what the cohort plants)

**Narrative signals**
- Boilerplate or template text reused across unrelated claimants, usually from the same agent.
- Buzzword density ("cutting-edge", "AI-driven", "revolutionary", "industry-first") with no technical specifics.
- Uncertainty described as cost, time, client demands or "unknown whether customers would adopt it".
- The baseline names no existing technique, product or paper.
- The advance is that the company built its own version of something already available.
- No failures, dead ends or abandoned approaches. Everything worked the first time.
- Mismatched field of science: a bakery claiming "food chemistry" without any chemists.

**Cost signals**
- Directors at ≥80% R&D time while also responsible for sales or operations.
- Dividends, benefits in kind or bonuses unrelated to R&D included in staff costs.
- Capital equipment, rent, travel or patent costs in "consumables" or "other".
- Overseas subcontractors or EPWs in a merged-scheme period.
- Contractor-side claims for client-commissioned work.
- Connected-party recharges with markup claimed in full.
- R&D intensity just over the ERIS threshold, with the denominator manipulated.
- Claim value disproportionate to turnover or headcount.

**Group / duplication signals**
- Several companies under common ownership describe the same project with reworded narratives.
- The same named staff appear in more than one company's staff schedule, with a combined apportionment above 100%.
- Intra-group invoices: the provider claims the staff as its own R&D, and the recipient claims the same cost as an EPW or subcontract.
- Each company claims SME status separately, although the linked group exceeds the thresholds.
- Shared directors, registered addresses, agents, project codes and evidence references.

**Footprint signals** (for web-search tools; Excelcion especially)
- The claimant's website, blog, job adverts and LinkedIn-style staff profiles do or do not show the sector and technical activity claimed.
- Claimed technical staff headcount against public team pages.
- Claimed product timelines against blog or press-release dates.

---

## 5. Cohort overview

See `docs/cohort-plan.md` for the full design: one row per claim, with its sector, scheme, grade and the issues it plants.
