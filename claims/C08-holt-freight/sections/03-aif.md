## 3. Additional Information Form

### 3.1 Company details

| Field | Entry |
|---|---|
| Company name | Holt Freight Intelligence Ltd |
| Company number | ZZ009945 |
| Unique Taxpayer Reference | 9999994512 |
| Registered office | Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS |
| Accounting period | 1 April 2024 to 31 March 2025 |
| Scheme | Merged scheme |
| Company status | Profit-making company |
| Parent undertaking | Veridian Holt Holdings Ltd (company number ZZ009931), which owns 100% of the company's shares |
| Ultimate controlling party | Gavin Holt, who owns 100% of Veridian Holt Holdings Ltd |
| Employees at 31 March 2025 | 64 |
| Turnover for the period | £22,500,000 |
| PAYE scheme reference | 999/ZZ40417 |
| VAT registration number | GB 999 2214 67 |

### 3.2 Contact for this claim

| Field | Entry |
|---|---|
| Name | Helen Dray |
| Role | Financial Controller |
| Address | As registered office above |
| Email | claims@holtline-freight.zz |
| Telephone | 01632 960412 |

### 3.3 Agent

| Field | Entry |
|---|---|
| Agent name | Vantrell Innovation Ltd |
| Contact | Ruth Ansell, Senior Claims Manager |
| Address | Unit 3, Quayside Works, Wakefield ZZ2 8PL |
| Agent reference | VIL-HFI-2425 |
| Agent authorisation | Signed letter of authority held on file, dated 6 January 2026 |
| Evidence index | Section 7.2 |

### 3.4 Senior officer

| Field | Entry |
|---|---|
| Name | Gavin Holt |
| Role | Director (Group Chief Executive) |
| Responsibility for R&D | Sponsor of the Lodestar and load-matching programmes and approver of the company's research direction |

### 3.5 Competent professional

| Field | Entry |
|---|---|
| Name | Dr Simon Achterberg |
| Role within the claimant | Head of Data Science (provided under group services agreement) |
| Employer | Holt Engineering Services Ltd |
| Qualifications | PhD, computational statistics; MSc, machine learning |
| Competent professional statement | Given in section 5.4 and in the appendices at section 7.1 |

### 3.6 Cost totals by category

| Category | Amount (as claimed) |
|---|---|
| Staff costs | £105,189 |
| Externally provided workers | £498,272 |
| Subcontracted R&D | £210,000 |
| Data and cloud | £88,000 |
| Consumables and software | Nil |
| Total qualifying expenditure | £901,461 |

The totals above agree to the cost schedules in section 6.

### 3.7 Project 1: Project Lodestar

**Main field of science or technology:** Data science, with statistical machine learning and time-series forecasting for large-scale spatio-temporal demand data. The project also draws on operational research for the reconciliation of forecasts across a hierarchy of geographic and commercial aggregates.

**Baseline (what was known or current practice before the project).** Before Project Lodestar the company forecast demand on its corridors, meaning groups of lanes between regions, using seasonal averages and simple exponential smoothing. Forecasts were refreshed weekly. The corridor-level approach was adequate for capacity planning on the busiest corridors but gave no usable forecast for individual origin–destination lanes, and it could not be applied to shippers that had not yet booked. Existing forecasting approaches assume dense, stationary demand signals; at lane level fewer than 8% of origin–destination pairs exhibit weekly volume sufficient for conventional models. The company therefore regarded lane-level forecasting as an open problem for its own data.

**Advance sought.** The company claims an advance in the science of demand forecasting for sparse, hierarchical freight data. The advance is a hierarchical reconciliation method, applied to lane-level forecasts that are individually unreliable, which produces forecasts that are coherent across the lane, regional and national levels, combined with a cold-start procedure that forecasts demand for new shippers from the behaviour of shippers with similar profiles. Neither element was known to the company or, so far as the company could establish, available in the published literature for freight marketplaces with data of this sparsity.

**Scientific or technological uncertainties.** (1) Whether a lane-level forecast could be produced with an error sufficient to support dynamic pricing for sparse origin–destination pairs. (2) Whether forecasts at lane level could be reconciled to regional and national totals without destroying the lane-level signal. (3) Whether a forecast could be produced for a new shipper with no booking history, and at what point such a forecast could be trusted. (4) Whether these methods could operate within the latency and cost limits of production inference.

**How the uncertainties were resolved.** Uncertainty (1) was addressed by building a backtesting harness, LDS-289, and comparing candidate models on held-out weeks. Uncertainty (2) was resolved by the hierarchical reconciliation method under LDS-502 in the period October 2024 to January 2025. Uncertainty (3) was resolved by the cold-start procedure under LDS-377 between August and September 2024. Uncertainty (4) was resolved in the production deployment under LDS-408 and LDS-446 in February 2025. Dated iterations are given in the technical narrative and in the work log at section 5.5.

### 3.8 Project 2: Dynamic load-matching optimisation

**Main field of science or technology:** Operational research and combinatorial optimisation, applied to real-time vehicle and load assignment under regulatory and service constraints.

**Baseline.** The company's matching engine assigned each open booking to a vehicle using a greedy algorithm that considered proximity, vehicle type and the next available driver-hours window. The engine was reliable at moderate volumes but produced sub-optimal assignments in peak periods, and it had no formal treatment of multi-leg driver-hours rules. Practice in the industry is to treat matching as a static assignment problem solved overnight. Holtline required assignment in near real time.

**Advance sought.** The company claims an advance in the real-time assignment of loads subject to driver-hours and vehicle constraints, achieved by a constraint formulation and solver configuration that meet a latency target of under two seconds at peak volume.

**Scientific or technological uncertainties.** (1) Whether a constraint formulation of the driver-hours rules could be solved at peak volume within the latency target. (2) Whether the solver configuration could be made robust to the variation in booking volume across the week. (3) Whether the assignments produced would be accepted by operations staff in practice.

**How the uncertainties were resolved.** Uncertainty (1) was addressed by the formulation work under LDS-398 and LDS-433 and by latency benchmarking under LDS-477. Uncertainty (2) was addressed by the solver configuration sweep under LDS-421. Uncertainty (3) was resolved by a shadow-running period under LDS-523 in January and February 2025, after which the release went live.

### 3.9 Staff engaged on the projects

| Name | Role | Projects | Proportion of time on R&D |
|---|---|---|---|
| Gavin Holt | Group CEO and Director | Lodestar, load-matching | 30% |
| Priyanka Mehta | Product Owner, Lodestar | Lodestar | 70% |
| Dr Simon Achterberg | Head of Data Science (provided) | Lodestar | Staff provided under the group services arrangement, see section 6 |
| Natasha Grieve | Machine Learning Engineer (provided) | Lodestar | Staff provided under the group services arrangement, see section 6 |
| Imran Qadir | Data Engineer (provided) | Lodestar | Staff provided under the group services arrangement, see section 6 |
| Bethany Coles | Optimisation Engineer (provided) | Lodestar | Staff provided under the group services arrangement, see section 6 |
| Luke Fensome | Backend Engineer (provided) | Lodestar | Staff provided under the group services arrangement, see section 6 |
