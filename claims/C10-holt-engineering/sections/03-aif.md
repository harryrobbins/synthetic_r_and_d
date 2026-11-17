## 3. Additional Information Form

### Part A: Company details

| Field | Entry |
|---|---|
| Company name | Holt Engineering Services Ltd |
| Company number | ZZ009958 |
| Corporation Tax UTR | 9999995866 |
| PAYE reference | 999/ZZ10958 |
| VAT registration | GB 999 1058 22 |
| Payment sort code | 00-00-58 |
| Registered office | Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS |
| Date of incorporation | 14 March 2016 |
| Accounting period | 1 April 2024 to 31 March 2025 |
| Average employees in period | 41 |
| Turnover for the period | £1,350,000 |
| Company size | Medium |
| Scheme claimed | Merged scheme |

### Part B: Group, contact, agent and senior officer

| Field | Entry |
|---|---|
| Parent undertaking | Veridian Holt Holdings Ltd (ZZ009931), which holds 100% of the issued shares |
| Ultimate controlling party | Gavin Holt, who holds 100% of the shares in the parent undertaking |
| Other companies in the group | Holt Freight Intelligence Ltd (ZZ009945); Holt Data Labs Ltd (ZZ010277) |
| Contact for this claim | Helen Marr, Finance Manager, Holt Engineering Services Ltd. Telephone 07700 900 412; email helen.marr@holt-engineering.example |
| Claim agent | Tallowby & Crane Accountants, Ashgrove House, 14 Mill Lane, Pontefract ZZ8 2LB. Contact: Peter Crane, Tax Manager. Telephone 07700 900 733 |
| Senior officer | Gavin Holt, Director, Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS |
| Competent professional | Dr Simon Achterberg, Head of Data Science, employed by the Company |

### Part C: Cost totals by category

| Category | Amount claimed |
|---|---|
| Staff costs (salary, employer's NIC and employer's pension, apportioned to the Programme) | £461,134 |
| Software (platform licence) | £52,000 |
| Consumables, externally provided workers, subcontracts and other costs | Nil |
| **Total qualifying expenditure** | **£513,134** |
| Expenditure credit at 20% (taxable) | £102,627 |

Further detail on each category is given in section 6.

### Part D: Project 1, Lodestar workstream

**Project title.** Lodestar: freight demand forecasting and dynamic load-matching (Engineering Services R&D Programme 2024/25).

**Main field of science or technology.** Computer science and data science: machine learning, temporal forecasting and statistical reconciliation applied to logistics.

**Start and end dates.** 1 April 2024 to 31 March 2025. The workstream was handed over to production operation in March 2025.

**Baseline.** The baseline is the state of freight demand forecasting as it stood on 1 April 2024. Existing forecasting approaches assume dense, stationary demand signals; at lane level only around 8% of lanes exhibit weekly volume sufficient for conventional models. The marketplace's forecasts at that time were produced by seasonal smoothing and regional aggregate models, which gave acceptable results for busy corridors and poor results for the long tail of origin–destination pairs. A competent professional in the field would have regarded that long tail as the principal unresolved problem, and the Company's baseline reflects that understanding.

**Advance sought.** The Company sought an advance in forecasting for sparse lane-level demand. The advance comprises: (a) a hierarchical reconciliation method that keeps lane-level forecasts coherent with regional and shipper-level totals when most lanes have little history; (b) a cold-start method that forecasts the demand of new shippers from the behaviour of comparable shippers; and (c) a calibrated uncertainty output that allows the load-matching service to act on forecasts with a known level of confidence.

**Scientific or technological uncertainties.** The uncertainties the Company faced at the outset were: whether reconciliation could be made coherent without degrading accuracy on dense corridors; whether information could be transferred from established shippers to new shippers without introducing systematic bias; whether temporal fusion models could be trained on sparse lane-level series to an accuracy that exceeded the baseline; whether calibrated intervals would be reliable enough to drive matching decisions; and whether the resulting improvement in forecast accuracy would translate into load-matching yield sufficient to justify the marketplace's pricing changes.

**How and when the uncertainties were resolved.** Each uncertainty was resolved through an iterative programme of backtesting against held-out periods, using a rolling-origin harness built in October 2024. Reconciliation and cold-start were resolved through the design, implementation and comparison of alternative methods between August 2024 and January 2025. Calibration was resolved in February 2025. The commercial uncertainty was resolved in March 2025 through a controlled comparison of matching yield with and without the new forecasts. Full detail is in sections 5.3.4 to 5.3.7 of the technical narrative.

**Staff engaged on the project.** Dr Simon Achterberg (Head of Data Science); Natasha Grieve (ML Engineer); Imran Qadir (ML Engineer); Bethany Coles (Data Engineer); Luke Fensome (Platform Engineer); Gavin Holt (Director, strategic and technical review).

### Part E: Project 2, platform workstream

**Project title.** Lakehouse platform configuration and extension for the Lodestar programme.

**Main field of science or technology.** Computer science: distributed data processing and orchestration.

**Start and end dates.** 1 April 2024 to 31 March 2025.

**Baseline.** The platform on which the Company's analytics pipelines ran at 1 April 2024 was a general-purpose data warehouse with batch extraction. It could not hold, version and serve the lane-level feature sets and model artefacts needed by the Lodestar workstream within the latency the load-matching service requires.

**Advance sought.** An advance in the orchestration of high-volume telematics ingestion (3.2 billion position records), feature computation and model inference on a single lakehouse, with reproducible versioning of data and models.

**Scientific or technological uncertainties.** Whether the platform could sustain the ingestion and feature computation within the required time window; whether model and feature versions could be reproduced exactly; and whether inference could be run in batch without compromising the freshness of the forecasts.

**How and when the uncertainties were resolved.** Through performance testing in June and July 2024, the design of versioned feature tables in July 2024, and production batch-inference trials in January and February 2025.

**Staff engaged on the project.** Luke Fensome (Platform Engineer); Bethany Coles (Data Engineer); Imran Qadir (ML Engineer).

### Part F: Other information

**Intra-group arrangements.** The Company's engineering staff work for several group companies under written services agreements. The principal agreement is dated 2 April 2024 and is with Holt Freight Intelligence Ltd. The Company's staff time on the Lodestar programme is recharged to that company and to Holt Data Labs Ltd. Platform costs are recharged in the same way. The arrangements are on an arm's length footing and are reviewed annually by the group board.

**Data used.** The telematics position data used by both projects is licensed from TrakSure Data Ltd under the group's data licence, held by Holt Freight Intelligence Ltd. The Company has access to the data for the purposes of the group's engineering services and does not hold a separate data licence. No cost for the data is included in the claim.

**Previous claims.** The Company made a claim for the accounting period ended 31 March 2023 in respect of a small internal IT project. No other claims have been made by the Company under the R&D schemes.

**Subsidies and grants.** No grant, subsidy or other external funding has been received for the R&D activities described in this claim.

### Part G: Declarations on this form

The information in this form is, to the best of the Company's knowledge, complete and accurate. The Company has retained the records supporting each entry, which are indexed in section 7 of this pack.
