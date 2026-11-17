## 3. Additional Information Form

### 3.1 Company details

| Field | Entry |
|---|---|
| Company name | Holt Data Labs Ltd |
| Company number | ZZ010277 |
| Corporation tax UTR | 9999927783 |
| Date of incorporation | 3 April 2024 |
| Registered office | Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS |
| Trading address | As registered office |
| Accounting period | 1 April 2024 to 31 March 2025 |
| Size | Small or medium-sized enterprise |
| Turnover for the period | £210,000 |
| Employees (direct, average) | 2 |
| VAT registration | GB 999 412 087 |
| PAYE reference | 999/ZZ10277 |
| Bank sort code and account | 00-00-41 (account ending 6218) |

### 3.2 Company contact

| Field | Entry |
|---|---|
| Name | Mr Tobias Renwick |
| Role | Office Administrator and finance contact |
| Telephone | 01999 040 277 |
| Email | finance@holtdatalabs.zz |

### 3.3 Agent

| Field | Entry |
|---|---|
| Agent firm | Ferrowen R&D Consulting Ltd |
| Address | Unit 6, Kessock Business Park, Leeds ZZ7 2TB |
| Contact | Ms Helena Ferrowen, Director |
| Agent authority | Authorised to submit this claim and correspond with HMRC on the company's behalf |

### 3.4 Senior officer

| Field | Entry |
|---|---|
| Name | Mr Gavin Holt |
| Position | Director |
| Responsibility | Overall direction of the company's research programme and approval of this claim |

### 3.5 Cost totals by category

| Category | Amount claimed |
|---|---|
| Staff costs | £245,529 |
| Data and cloud | £88,000 |
| Subcontract (UK, connected) | £140,000 |
| Total qualifying expenditure | £473,529 |

Full cost schedules and the apportionment methodology are set out in section 6.

### 3.6 Project 1: Project Polaris, lane-level demand forecasting

**Main field of science or technology.** Computer science and artificial intelligence, specifically machine learning applied to time-series forecasting and hierarchical statistical reconciliation.

**Baseline.** Existing forecasting approaches assume dense, stationary demand signals. At lane level under 8% of O-D pairs show enough weekly volume to support conventional models, so that published methods based on seasonal decomposition, exponential smoothing and autoregression produce forecasts that are unusable for the sparse majority of lanes. Prior to the programme, the company's own baseline was a set of statistical models run on the sparse lanes, with mean absolute percentage error exceeding 40% on lanes carrying fewer than four loads in a typical week. On dense lanes the same models performed acceptably, so the difficulty lies in the sparse population rather than in the general form of the models. Sparse-lane forecasts were either discarded in favour of fixed capacity allocations or produced at a level of accuracy that gave planners no useful information.

**Advance sought.** An advance in the reliability of freight demand forecasts on sparse origin-destination lanes. The advance comprises two elements: a hierarchical reconciliation procedure that allows a sparse lane to borrow statistical strength from the corridors, regions and shipper groups that contain it, while keeping forecasts at every level consistent; and a cold-start method that produces forecasts for a new shipper with no history, using the behaviour of shippers with similar profiles. Neither element is achieved by published methods in the form needed for lane-level freight demand, where series are sparse, physically constrained and spatially structured.

**Uncertainties.** At the outset the company could not determine: whether a hierarchical reconciliation could be made stable on lanes with fewer than four observations per week, or whether the adjustment would produce negative volumes; whether a temporal fusion architecture could be trained to produce calibrated intervals on lane-level demand, given that the tails of the distribution are poorly sampled on sparse lanes; and whether a cold-start approach could generalise from established shippers to new shippers without leaking information across accounts or introducing systematic bias into the forecasts for the new shipper's lanes. None of these questions could be answered from published knowledge or from the company's existing tools.

**How and when uncertainties were resolved.** Reconciliation stability was resolved in the second and third quarters of the period, through a sequence of controlled experiments on held-out lanes. A constrained reconciliation variant, which enforces non-negativity within the adjustment, reduced constraint violations on sparse lanes to a level that the company regarded as acceptable. Calibration of intervals was resolved in the second quarter, by means of a quantile calibration layer fitted on a separate calibration set. The cold-start method was resolved in the second and third quarters after a leakage check failed and the normalisation step was redesigned. The method was validated in the final quarter against a holdout of shippers onboarded during the period, with their first ninety days withheld from training. Outcomes and the evaluation standard are recorded in section 5.2.9 of the technical narrative.

### 3.7 Project 2: Project Telematics Pipeline

**Main field of science or technology.** Computer science, specifically data engineering for large-scale spatio-temporal sensor data.

**Baseline.** Standard batch processing of telematics pings into fixed-interval records, typically at one-minute or five-minute intervals. Under that approach, dwell and detour behaviour cannot be represented at the resolution the demand features require: a twelve-minute loading dwell and a forty-minute fuel queue are indistinguishable on a five-minute grid, and detours around closed roads are lost altogether. Finer grids were tested by the company and found to be impractical to recompute daily across the full ping volume in the licence.

**Advance sought.** A method for deriving dwell and detour features from irregular raw GPS telematics pings, identifying events at their natural temporal resolution rather than on a fixed grid. The method must tolerate irregular ping intervals and clock drift between devices without loss of accuracy, and must be efficient enough to run across the full licensed data set within the daily processing window.

**Uncertainties.** Whether event-based dwell detection could remain accurate where pings are sparse, since the start and end times of a stop are then uncertain; whether clock drift between in-vehicle units could be corrected without a reference signal for every vehicle; whether detour identification by comparison with an expected route could be made reliable across road classes; and whether an event-based derivation over approximately 3.2 billion records could be restructured to run within the daily window on the infrastructure available.

**How and when uncertainties were resolved.** Accuracy under irregular pings was resolved in the second and third quarters through testing against a labelled sample of 1,840 journeys with independent records of stops. Clock drift was corrected against reference pings in the first quarter. Detour matching was resolved in the second quarter through a route tolerance band that adapts to road class. Efficiency was resolved in the third quarter following a redesign of the processing stages into partitioned batches, after which the daily recomputation met the processing window on all representative days tested. Outcomes are recorded in section 5.3.7 of the technical narrative.

### 3.8 Declaration by the senior officer

I confirm that the information in this form is correct to the best of my knowledge and belief, that the company has undertaken the research described, and that the expenditure claimed was incurred on that research.

Signed: Gavin Holt, Director
Date: 12 August 2025
