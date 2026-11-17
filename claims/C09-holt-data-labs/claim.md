> SYNTHETIC TEST DATA – FICTIONAL COMPANY – PREPARED FOR HMRC HACKATHON – NOT A REAL TAX CLAIM

## 1. Cover sheet and claim summary

**Claimant:** Holt Data Labs Ltd
**Company number:** ZZ010277
**Corporation tax UTR:** 9999927783
**Registered office:** Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS
**Accounting period:** 1 April 2024 to 31 March 2025
**Scheme claimed:** Enhanced R&D Intensive Support (ERIS), small or medium-sized enterprise
**Claim type:** First claim for the accounting period
**Agent:** Ferrowen R&D Consulting Ltd, on behalf of the company
**Senior officer:** Mr Gavin Holt, Director

## Purpose of this pack

This pack sets out the research and development undertaken by Holt Data Labs Ltd, an independent AI research laboratory, during the accounting period stated above. The company undertook R&D on its own account to develop proprietary forecasting intellectual property. The principal programme, referred to in the company's records as Project Polaris, applies machine-learning methods to the forecasting of freight demand at lane level, where historical volumes are sparse and conventional statistical models do not perform reliably. A second project develops the telematics data pipeline on which the forecasting work depends.

The pack contains the Claim Notification Form, the Additional Information Form, the company background, the technical narrative for each project, the cost schedules and methodology, and the supporting appendices.

## Claim summary

| Item | Amount |
|---|---|
| Total staff costs claimed | £245,529 |
| Other qualifying expenditure claimed | £228,000 |
| Total qualifying expenditure claimed | £473,529 |
| Extra deduction claimed (86%) | £407,235 |
| Surrenderable trading loss | £817,235 |
| Payable tax credit claimed (14.5%) | £118,499 |
| R&D intensity (as claimed) | 76.4% |

The company is a small or medium-sized enterprise for the purposes of the scheme. Its turnover for the period was £210,000 and its R&D intensity for the period exceeds the 30% threshold for enhanced support. The company made a trading loss for the period before the R&D deduction, which it surrenders in accordance with the scheme rules.

## Basis of claim

The claim is made on the basis that the company's activities in Project Polaris and Project Telematics Pipeline seek to achieve an advance in science or technology, and that the uncertainties encountered were not resolvable by a competent professional working in the field from existing knowledge. Where activities were routine, they are described as such and are included only as necessary supporting work. Staff time has been apportioned on the basis set out in section 6 of this pack, using timesheets, the company's Jira records, interviews with staff and documented estimates.

The company's competent professional for the principal project is Dr Simon Achterberg, whose statement appears in section 5 and whose curriculum vitae appears in section 7.

---

## 2. Claim Notification Form

The Claim Notification Form for this accounting period was submitted online on 12 August 2025, within six months of the end of the period, as required for a small or medium-sized enterprise. The details recorded on that form are reproduced below for completeness.

| Field | Entry |
|---|---|
| Company name | Holt Data Labs Ltd |
| Company registration number | ZZ010277 |
| Corporation tax UTR | 9999927783 |
| Accounting period start | 1 April 2024 |
| Accounting period end | 31 March 2025 |
| Company status for R&D purposes | Small or medium-sized enterprise |
| Scheme | ERIS (R&D intensive support) |
| Claim type | First claim for this period |
| Notification submitted by | Ferrowen R&D Consulting Ltd, agent |
| Date of submission | 12 August 2025 |
| Senior officer | Mr Gavin Holt, Director |
| Registered office | Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS |

The company intends to claim relief for expenditure on staff costs, data and cloud costs, and a subcontract for modelling support. The company has not previously made an R&D claim. Projects described in the Additional Information Form that accompanies this claim are the same projects identified in the notification.

The notification was confirmed by the senior officer through the agent's secure portal. The agent holds the senior officer's authority to submit the claim on the company's behalf, and the signed declaration is included at section 7 of this pack.

---

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

---

## 4. Company background

### 4.1 Formation and purpose

Holt Data Labs Ltd was incorporated in England and Wales on 3 April 2024 as a private company limited by shares. It was formed to carry out applied research in machine learning and statistical forecasting, and to hold the intellectual property arising from that research. The company describes itself as an independent AI research laboratory. Its registered office is at Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS.

The founders' intention was to create a research organisation with a clear focus on problems that existing commercial tools handle poorly. Freight demand forecasting was selected because the data available from road-haulage operations is unusually large and detailed, yet its distribution across origin-destination pairs is highly uneven. The company's first accounting period, which is the period covered by this claim, was therefore spent establishing its data infrastructure and beginning its principal research programme.

### 4.2 Business and activities

The company undertook R&D on its own account to develop proprietary forecasting intellectual property. That intellectual property comprises trained model architectures, reconciliation procedures, feature derivation methods and the documentation and test harnesses that accompany them. Its principal output during the period was the Polaris forecasting method described in section 5 of this pack.

During the period the company earned turnover of £210,000. This was commercial licensing income, received in three instalments of £70,000 under a licence and development agreement dated 15 April 2024. The company's activities in the period were otherwise directed to research. The company does not sell a product to end users, does not operate a platform and does not carry on freight, logistics or haulage activities.

### 4.3 Ownership and group

The company's issued share capital is held by a single corporate shareholder, a private holding company registered in England and Wales under company number ZZ009931. The ultimate beneficial owner of that holding company, and therefore of the company, is Mr Gavin Holt. The company is part of a small private group of commercial businesses under common ownership, and its directors consider its relationships with other group companies to be conducted on normal arm's-length terms.

The company's research has been developed for the company's own account. Where the company's forecasting intellectual property has been licensed to group companies, the company has done so under written agreements and has recognised the resulting income as commercial licensing income.

The company has no subsidiaries and holds no interests in other undertakings.

### 4.4 Management and governance

Mr Gavin Holt is a director of the company and is its senior officer for the purposes of this claim. He sets the research direction, approves the company's budgets and has final responsibility for the company's submissions to HMRC. Mr Holt has more than twenty years' experience in logistics technology and commercial operations, and he is responsible for the company's commercial relationships.

Dr Simon Achterberg is the company's Chief Scientist. He leads the technical direction of the Polaris programme, sets the evaluation standards by which research outcomes are judged, and chairs the weekly technical review. His curriculum vitae is included at section 7.

The company holds a monthly board meeting. Minutes for the period record the approval of the research budget, the approval of the licence and development agreement referred to above, and the review of progress against the technical milestones described in section 5.

### 4.5 Staff and secondments

At the end of the period the company had two directly employed members of staff: an office administrator, who manages the company's premises, correspondence and finance records, and a junior analyst, who supports data preparation and the production of evaluation reports. Neither of these members of staff contributed time to the research activities claimed in this pack, and their costs are not included in the claim.

The research programme was resourced principally through the secondment of specialist staff to the company on a full-time basis. The seconded staff are Dr Simon Achterberg, Chief Scientist, and Ms Natasha Grieve, Machine Learning Engineer. Their secondment arrangements are described in section 6 and their time has been apportioned on the basis set out in that section. Mr Gavin Holt, as a director, also contributes a proportion of his working time to the research.

The salary, employer National Insurance and pension cost for each member of the research team are set out in the staff cost schedule at section 6.

### 4.6 Facilities and equipment

The company occupies Suite 4 at Calder House under a licence of office accommodation. The office is used for the company's administration and for the working meetings of the research team. The company does not operate a laboratory and has no dedicated hardware beyond laptops and workstations for each member of the research team.

Model training and inference are performed on cloud infrastructure, provisioned through a Microsoft Azure subscription with Azure Machine Learning compute. The company's experiments run on a range of compute instance sizes, including GPU-accelerated instances, depending on the requirements of each training run. Data storage, feature stores and the evaluation environment are also hosted on Azure. The cost of this infrastructure is included in the claim at section 6.

### 4.7 Data sources and data licensing

The company's principal data source is a licence for approximately 3.2 billion anonymised GPS telematics pings, supplied by TrakSure Data Ltd under a data licence agreement that permits the company to use the data for forecasting research. The licence restricts onward distribution of the raw data but does not restrict the company's use of derived features or trained models. The company also holds licences for public holiday calendars, weather observations and published road network data.

The telematics data contains vehicle and journey information that is pseudonymised before it enters the company's environment. The company's data protection arrangements are documented in its data processing register and were reviewed during the period.

### 4.8 Funding and financial position

The company was funded from the subscription for its issued shares, which were paid up at incorporation, and from a shareholder loan facility made available by Mr Gavin Holt. The facility was drawn to meet operating costs as they fell due during the period. The company's trading loss for the period, before the R&D deduction, was £410,000.

The company's management accounts for the period were prepared by its office administrator and reviewed by the company's accountants. The accounts show turnover of £210,000, which arose from the commercial licensing income described at section 4.2. The company has no bank borrowings and no external investors.

### 4.9 Intellectual property

The company owns the intellectual property in its forecasting methods, its trained models and its feature derivation procedures. Its research output is documented in an internal repository and in the evaluation reports listed in the appendices. The company has not applied for patent protection during the period and has relied on confidentiality and documentation as its primary means of protecting its methods.

The company's Chief Scientist and seconded staff have contributed to the intellectual property on the terms of their secondment arrangements, and the company holds the rights necessary to use and license that intellectual property.

### 4.10 Prior history and first claim

This is the company's first claim for research and development relief. The company has not previously been in receipt of any tax credit, grant or other relief for research. The company's activities before incorporation were carried out by Mr Holt and by Dr Achterberg in a personal capacity, and the company's first accounting period is the first period in which the research described in this pack was carried out by the company itself.

---

## 5. Technical narrative

### 5.1 Introduction and structure

This section sets out the research undertaken by Holt Data Labs Ltd during the accounting period 1 April 2024 to 31 March 2025. It is written project by project. For each project it describes the baseline against which the work is measured, the advance sought, the uncertainties the company encountered, the methodology used to address them, a dated work log, the outcomes, and the boundaries of the project. A competent professional statement for the principal project appears at section 5.7.

The company has two projects in the period. Project 1 is the principal research programme, Project Polaris (delivered to group under Lodestar programme), which develops a method for forecasting freight demand at lane level. Project 2, the Telematics Pipeline, develops the data derivation stages on which Project 1 relies.

Each project is supported by a Jira project, LDS, in which the company records tasks, experiments and decisions. Ticket references in this section are to that project. The work log entries are drawn from ticket history, from the experiment registry maintained in the company's repository, and from the minutes of the weekly technical review. Where an entry records a decision, the decision is attributed to the person who took it.

### 5.2 Project 1: Polaris, lane-level demand forecasting

#### 5.2.1 Context

Freight demand forecasting is the basis on which a road-haulage marketplace matches available vehicle capacity with the loads its customers wish to move. The accuracy of demand forecasts determines how much capacity a platform must hold in reserve, how far in advance it can offer price guarantees, and how efficiently idle vehicle movements can be avoided. Forecasts are commonly produced for origin-destination pairs, which this section refers to as lanes.

The data available for this work is unusually detailed. The company holds a licence for approximately 3.2 billion anonymised GPS telematics pings, from which vehicle movements, dwell times and loaded and empty journeys can be derived. The difficulty lies in the distribution of demand across lanes. Demand is concentrated on a small number of high-volume corridors, while the great majority of lanes carry only occasional loads.

#### 5.2.2 Baseline

The baseline for this project is the current state of practice in freight demand forecasting. Existing forecasting approaches assume dense, stationary demand signals. At lane level under 8% of O-D pairs show enough weekly volume to support conventional models, so that the seasonal decomposition, exponential smoothing and autoregressive methods that are standard in the industry produce forecasts that are unusable for the sparse majority of lanes.

The company's pre-programme baseline was assembled from a set of statistical models run on the sparse lanes. On lanes with fewer than four loads in a typical week, the mean absolute percentage error of those models exceeded 40%. On the dense lanes the same models performed acceptably, which confirmed that the problem lay in the sparse population rather than in the models' general form. Forecasts on sparse lanes were therefore either discarded in favour of fixed capacity allocations or produced at a level of accuracy that gave planners no useful information.

The baseline is therefore defined as the performance of conventional statistical forecasting on sparse lanes, measured on the company's holdout sample of lanes from the period before the programme began.

#### 5.2.3 Advance sought

The advance sought is a forecasting method that gives reliable point forecasts and calibrated intervals for sparse lanes. Two elements are required. The first is a hierarchical reconciliation procedure, which allows the forecast for a sparse lane to borrow statistical strength from the aggregate forecasts of the corridors, regions and shipper groups that contain it, while keeping the forecasts for all levels consistent with one another. The second is a cold-start method, which allows a forecast to be produced for a new shipper for whom no history exists, using the behaviour of shippers with similar profiles.

The company's view is that neither element is achieved by existing published methods in the form needed for lane-level freight demand. Hierarchical reconciliation has been applied to retail and energy demand, where the series at each level are dense. Cold-start methods have been developed for recommender systems, where the item is a product rather than a time series with physical constraints. The advance lies in combining the two for sparse, physically constrained, spatially structured demand.

#### 5.2.4 Uncertainties

At the outset of the programme, the company identified the following uncertainties, none of which could be resolved from published knowledge or from the company's existing tools.

The first uncertainty concerned reconciliation stability. Hierarchical reconciliation solves a constrained adjustment across the forecast tree. On lanes with very few observations per week, the adjustment can become unstable, producing forecasts that oscillate or that violate the physical constraint that a lane cannot carry negative volume. It was not known whether a reconciliation procedure could be designed that remained stable on lanes with fewer than four observations per week.

The second uncertainty concerned calibration. Point forecasts were of limited use to the planners at the marketplace without intervals that reflected the real range of outcomes. A temporal fusion architecture was selected as the candidate model, on the basis of its handling of covariates such as calendar effects and fuel prices. It was not known whether such a model could be trained to produce intervals that were calibrated on sparse lanes, where the tails of the distribution are poorly sampled.

The third uncertainty concerned the cold-start problem. A new shipper has no history, and the company had no evidence that the behaviour of an established shipper could be used to forecast a new one without leaking information across accounts or producing systematic bias in the forecasts for the new shipper's lanes.

#### 5.2.5 Methodology

The methodology for Project Polaris was experimental. Each uncertainty was addressed through a defined sequence of experiments, each with a stated hypothesis, a fixed evaluation set and a pre-registered success criterion. The experiments were recorded in the experiment registry, and the results were reviewed at the weekly technical review chaired by Dr Simon Achterberg.

For the reconciliation work, the company constructed a forecast tree of lanes, corridors, regions and shipper groups, and tested a range of reconciliation procedures on that tree, including the minimum-trace adjustment and a constrained variant that enforced non-negativity. Stability was measured by the frequency of constraint violations and by the variance of forecasts across successive retrainings.

For the temporal fusion work, the company trained candidate architectures on the sparse-lane training set, with covariates for calendar effects, fuel price indices, public holidays and weather observations. Calibration was measured using the coverage of prediction intervals at nominal levels of 50%, 80% and 95%, computed on held-out lanes. The company's method for achieving calibration was to adjust the output distribution of the model using a quantile calibration layer, the parameters of which were fitted on a calibration set drawn from the lanes not used for training.

The gradient-boosted tree models used as components of the forecast ensemble were trained using the company's standard configuration. Their hyper-parameters were tuned using a sweep over learning rate, tree depth, minimum child weight and subsampling ratios, with the sweep harness recorded in the repository. The tuning followed established practice for gradient-boosted models on tabular data.

For the cold-start work, the company constructed a holdout of shippers onboarded during the period, with their first ninety days of activity withheld from training. A shipper embedding was learned from the profile features of established shippers, and the forecasts for new shippers were produced by mapping their profile features into the embedding space. The method was evaluated for leakage by checking whether any feature of an established shipper's account was used in the forecast for a new shipper outside its own profile.

#### 5.2.6 Evaluation standard

All results in this section are reported against a single evaluation standard. Accuracy is measured by mean absolute percentage error, root mean squared scaled error and interval coverage. Results are reported separately for three lane bands: dense lanes with more than thirty loads a week, intermediate lanes with between eight and thirty, and sparse lanes with fewer than eight. The evaluation harness, which computes these measures from the held-out data and writes the results to the registry, is recorded under LDS-530 "Evaluation harness MAPE by lane band".

The company's view is that the sparse-lane band is the one that matters for the advance, and the reported results give it particular weight. Results on the dense band are reported for completeness and to confirm that the method does not degrade performance where conventional methods already perform adequately.

---

## 5. Technical narrative (continued)

### 5.2.7 Chronological work log

The following log records the principal iterations of Project Polaris in date order. Each entry gives the date, the Jira reference where one exists, the iteration performed and its recorded result. Entries are summarised from ticket history and from the minutes of the weekly technical review.

| Date | Reference | Iteration and result |
|---|---|---|
| 8 April 2024 | LDS-101 | Project opened. Experiment registry and evaluation conventions established. Pre-registered success criteria recorded for each of the three uncertainties. |
| 22 April 2024 | LDS-118 | Feature store schema agreed for lane, corridor, region and shipper-group keys. Calendar, weather and fuel covariates loaded for the sparse-lane training set. |
| 13 May 2024 | LDS-266 | Gradient-boosted component models trained on the full lane set. Hyper-parameter sweep of 412 configurations run over learning rate, depth, minimum child weight and subsampling. Best configuration retained for the ensemble. |
| 3 June 2024 | LDS-214 | First training run of the temporal fusion model, titled "Temporal fusion model – lane-level demand". Training stable on dense lanes. On sparse lanes the output distribution collapsed to the lane mean in 27% of runs. |
| 19 June 2024 | LDS-502 | First hierarchical reconciliation attempt using minimum-trace adjustment on the forecast tree. Constraint violations (negative volumes) on sparse lanes recorded at 31% of forecast periods. Issue opened to design a constrained variant. |
| 10 July 2024 | LDS-502 | Constrained reconciliation variant implemented, enforcing non-negativity within the adjustment. Constraint violations on sparse lanes reduced to 0.4% of forecast periods. Variance of forecasts across successive retrainings reduced by roughly two-thirds. |
| 2 August 2024 | LDS-441 | Quantile calibration layer introduced on the temporal fusion output. Interval coverage at nominal 80% measured at 61% before calibration and 79% after calibration on the held-out sparse lanes. |
| 29 August 2024 | LDS-377 | Cold-start work opened, titled "Cold-start for new shippers". Shipper embedding learned from profile features of established shippers. |
| 26 September 2024 | LDS-377 | Leakage check failed. Account-level features of established shippers were found to influence forecasts for new shippers through a shared normalisation step. Normalisation redesigned to operate within profile. Check repeated and passed on 1 October 2024. |
| 21 October 2024 | LDS-502 | Dr Simon Achterberg approved freezing the reconciliation design for the remainder of the period, following review of the stability results from the preceding four months. |
| 14 November 2024 | LDS-588 | Holdout sample of shippers onboarded during the period constructed, with first ninety days of activity withheld from training. Sampling procedure reviewed by Ms Natasha Grieve. |
| 9 December 2024 | LDS-530 | Full evaluation run across all three lane bands against the pre-programme baseline. Sparse-lane mean absolute percentage error reduced from the baseline level of approximately 41% to 22.6%. Dense-lane results within 0.3 percentage points of baseline. |
| 20 January 2025 | LDS-530 | Regression check on intermediate lanes. Results stable across two retraining cycles. Ensemble weights fixed. |
| 17 February 2025 | LDS-377 | Cold-start method validated against the holdout. Mean absolute percentage error for new shippers in their first ninety days recorded at 31%, against 58% for the pre-programme approach applied to the same shippers. |
| 10 March 2025 | LDS-530 | Results write-up circulated for technical review. Calibration coverage at nominal 80% recorded at 78.9% on the final sparse-lane evaluation. |
| 27 March 2025 | LDS-101 | Project Polaris closed for the period. Final configuration of the forecasting method documented in the repository. Hand-over to the production forecasting service agreed. |

### 5.2.8 Discussion of iterations

The log shows that the iterations were not linear. Each of the three uncertainties produced at least one result that required the design to be revised. The reconciliation procedure was changed after the first attempt because the unconstrained adjustment violated the non-negativity constraint on a substantial share of sparse-lane forecast periods. The calibration layer was introduced because the temporal fusion output, although accurate in its point forecasts, was systematically over-confident on sparse lanes. The cold-start normalisation was redesigned because the leakage check showed that a shared step was carrying information across accounts.

Each of these revisions was a considered response to an observed failure. None was a parameter adjustment of the kind that a competent professional would expect to resolve by applying the standard configuration of an established tool. The company's record of the reasons for each change is kept in the Jira ticket and in the decision entries of the technical review minutes.

The gradient-boosted component models were tuned across the sweep described at entry LDS-266. The sweep was necessary because the component models were required to produce forecasts on the same lane set as the temporal fusion model, and their configuration determined the behaviour of the ensemble on sparse lanes. The configuration that was adopted differed materially from the library defaults, which over-fitted the dense lanes and produced unstable forecasts on the sparse lanes.

### 5.2.9 Outcomes

The principal outcome of Project Polaris is a forecasting method that produces reliable forecasts and calibrated intervals on sparse lanes, together with a cold-start method for new shippers. The method is documented in the repository and is the basis of the forecasting service used by the group's platform.

On the sparse-lane band, mean absolute percentage error fell from approximately 41% under the pre-programme baseline to 22.6% under the final method. On the intermediate band the reduction was from 19% to 13%. On the dense band the results were unchanged within measurement error, which the company regards as a necessary condition for the advance: the method improves sparse lanes without degrading the lanes that conventional methods already serve.

Interval coverage on sparse lanes at the nominal 80% level was 78.9% in the final evaluation, against 61% before calibration. The reconciliation procedure produced non-negative forecasts in every forecast period in the final evaluation, and the variance of forecasts across retrainings is recorded as stable within the tolerance set at the outset.

The cold-start method reduced mean absolute percentage error for new shippers in their first ninety days from 58% to 31%. The company does not claim that the cold-start method is accurate for new shippers in absolute terms. Its significance lies in the fact that a forecast can now be produced at all for a shipper with no history, where previously none could be made.

### 5.2.10 Boundaries

Project Polaris began on 8 April 2024, when the project was opened in the Jira project LDS and the experiment registry was established. It ended on 27 March 2025, when the final configuration was documented and handed over to the production forecasting service. Work on the production service after 27 March 2025 is maintenance and integration, is not claimed, and is excluded from the cost schedules.

The boundary of the project is defined by the uncertainties it addresses. Work that addressed those uncertainties is included. Work on data ingestion, which is the subject of Project 2, is described in section 5.3 and is included only to the extent that it was required to produce the features on which Project 1 depends.

---

## 5. Technical narrative (continued)

### 5.3 Project 2: Telematics Pipeline

#### 5.3.1 Context

Project 1 depends on features that describe how vehicles move: where they dwell, where they detour, and when they are loaded or empty. None of these features exists in the raw telematics stream. The stream consists of position pings, emitted by in-vehicle units at irregular intervals, with clock drift between devices and with frequent gaps where coverage is poor. The Telematics Pipeline was undertaken to derive dwell and detour features from that stream at a resolution sufficient for the forecasting models, and to do so at a cost that allows the features to be recomputed each day.

#### 5.3.2 Baseline

The baseline is standard batch processing of telematics pings into fixed-interval records. In that approach, pings are resampled to a regular grid, typically at one-minute or five-minute intervals, and the stop and movement states of each vehicle are inferred from the resampled series. These approaches cannot represent dwell and detour behaviour at the resolution the demand features require. A dwell of twelve minutes at a loading bay and a dwell of forty minutes in a fuel queue are indistinguishable on a five-minute grid, and the detours that signal a driver's diversion around a closed road are lost altogether.

Fixed-interval processing could be made finer, but only at a cost in compute that made daily recomputation across the full ping volume impractical. The company's assessment at the start of the project was that the baseline could not satisfy both the resolution and the cost requirement at once.

#### 5.3.3 Advance sought

The advance sought is a method for deriving dwell and detour features from irregular raw pings, with three properties. The first is that dwell and detour events are identified at their natural temporal resolution rather than on a fixed grid. The second is that the derivation tolerates irregular ping intervals and clock drift without a loss of accuracy. The third is that the derivation is efficient enough to be executed within the daily processing window, across the full set of vehicles in the licence.

#### 5.3.4 Uncertainties

The company identified two uncertainties at the outset.

The first concerned accuracy under irregular pings. Event-based dwell detection depends on the timing of pings near the start and end of a stop. Where pings are sparse, the start and end times are uncertain, and where clocks drift, pings from the same vehicle may be out of order. It was not known whether a derivation could be designed that remained accurate under these conditions without reverting to a fixed grid.

The second concerned efficiency. Event-based detection over a ping stream of approximately 3.2 billion records is a computationally demanding operation if implemented naively. It was not known whether the derivation could be restructured to run within the daily window, given the infrastructure available on Azure.

#### 5.3.5 Methodology

The methodology for the Telematics Pipeline combined controlled testing with iterative redesign. Accuracy was tested against a labelled sample, constructed from journeys for which the company held independent records of stops, including loading and unloading documents and driver-confirmed delivery times. The labelled sample comprised 1,840 journeys, selected to span the range of ping densities in the licence.

Accuracy was measured as the proportion of dwell events detected within a tolerance of two minutes of the labelled start and end times, and as the proportion of detour events matched to a labelled diversion. Efficiency was measured as wall-clock time and compute cost for a full daily recomputation on a representative day of pings.

The derivation method was developed in stages. The first stage cleaned and ordered the pings for each vehicle, correcting clock drift against a reference ping where one was available. The second stage identified candidate stops from runs of low speed and absence of movement. The third stage refined the start and end times of each candidate stop, using the nearest pings on either side. The fourth stage classified each stop by its dwell duration and location, and identified detours by comparing the vehicle's path against the expected route.

#### 5.3.6 Chronological work log

| Date | Reference | Iteration and result |
|---|---|---|
| 15 April 2024 | LDS-612 | Project opened, titled "Pipeline dwell features". Raw ping schema and clock drift characteristics documented from the licence sample. |
| 6 May 2024 | LDS-612 | Fixed-interval baseline implemented as a reference. Dwell detection on a five-minute grid recorded at 64% accuracy against the labelled sample. |
| 28 May 2024 | LDS-612 | First event-based stop detection implemented. Accuracy at the two-minute tolerance recorded at 71%. Failures concentrated on journeys with sparse pings. |
| 18 June 2024 | LDS-649 | Clock drift correction implemented against reference pings. Out-of-order pings reduced to 0.2% of the sample. |
| 9 July 2024 | LDS-649 | Start and end refinement introduced for candidate stops. Accuracy at the two-minute tolerance recorded at 88%. |
| 31 July 2024 | LDS-655 | Detour identification implemented by comparison of path against expected route. Initial match rate 52% of labelled diversions. |
| 22 August 2024 | LDS-655 | Route comparison redesigned to use a tolerance band that adapts to road class. Match rate recorded at 79%. |
| 16 September 2024 | LDS-661 | Efficiency work opened. Naive implementation required approximately nine hours for a daily recomputation on a representative day. |
| 11 October 2024 | LDS-661 | Stages restructured to process vehicles in partitioned batches with state carried between stages. Recomputation time reduced to approximately three hours and forty minutes. |
| 4 December 2024 | LDS-661 | Compute cost of the daily recomputation reduced below the level set at the outset of the project. Daily window met on all representative days tested. |
| 14 February 2025 | LDS-612 | Project closed for the period. Final derivation method documented. Dwell and detour features handed to Project 1 for use in the forecasting models. |

#### 5.3.7 Outcomes

The Telematics Pipeline delivered a method for deriving dwell and detour features from irregular raw pings. Dwell detection accuracy at the two-minute tolerance was 88% on the labelled sample, against 64% for the fixed-interval baseline. Detour matching reached 79% of labelled diversions. The derivation tolerates the clock drift and sparse pings present in the licence, and a full daily recomputation now completes within the daily processing window.

The features produced by the pipeline were used by Project 1 in the temporal fusion and gradient-boosted models described in section 5.2. The company's view is that the pipeline's advance is inseparable from the forecasting method it serves, and the two projects are presented together in this pack for that reason.

#### 5.3.8 Boundaries

The Telematics Pipeline began on 15 April 2024 and ended on 14 February 2025. Work on the production ingestion of the licence data after 14 February 2025 is operational and is excluded. Work that was required only to load and store the raw data, which was carried out by the company's contractors before the project opened, is excluded. The boundary of the project is the derivation of features whose accuracy and efficiency were uncertain at the outset.

### 5.4 Time apportionment and the seconded team

The research described in sections 5.2 and 5.3 was carried out by the company's research team. The team comprised Dr Simon Achterberg as Chief Scientist, Ms Natasha Grieve as Machine Learning Engineer and Mr Gavin Holt as director. Their time on each project is apportioned in the cost schedules at section 6, using the methodology described there.

Dr Achterberg and Ms Grieve work on the company's research on a full-time secondment basis and spend the large majority of their working time on the two projects. Mr Holt's time is divided between research direction, the commercial relationships of the company and the preparation of the company's accounts. The apportionment of his time has been set on the basis of an interview with him and of his calendar for the period.

The apportionments reflect the proportion of each person's time that was spent on the projects described in this section, as recorded in the timesheets and Jira history, and as confirmed in interviews with each individual. The apportionments are not intended to represent the full extent of each person's activity but only the portion that falls within the research.

### 5.5 Summary of the advance

Taken together, the two projects achieved an advance in the field of freight demand forecasting in three respects. They produced a hierarchical reconciliation procedure that is stable on sparse lanes, when published methods are not. They produced a calibrated temporal forecasting method for sparse lanes, with interval coverage that conventional approaches could not achieve on that population. They produced a cold-start method for new shippers, and a feature derivation method for irregular telematics pings that delivers the resolution and efficiency required by the forecasting models.

The company accepts that the forecasting models in the final system include established components, including gradient-boosted trees and a temporal fusion architecture, and that these components were tuned for the company's data. The advance lies in the reconciliation, calibration and cold-start methods, together with the means by which they were made to work with those components on sparse, physically constrained data. The company's view is that a competent professional in the field, faced with the uncertainties described above, would not have been able to achieve the outcomes recorded without carrying out the work described.

### 5.6 Evidence

The evidence supporting this section is held in the company's repository, in the Jira project LDS, in the experiment registry and in the minutes of the weekly technical review. Extracts from these sources are listed at section 7. The company will make the full records available to HMRC on request.

### 5.7 Competent professional statement

I, Dr Simon Achterberg, make the following statement in support of this claim.

I have worked in machine learning and statistical forecasting for more than fifteen years. My doctoral research concerned the reconciliation of hierarchical time-series forecasts, and I have published on the stability of constrained forecast adjustment. From 2017 to 2021 I led the data science function of a logistics technology business, where I was responsible for the design and evaluation of demand forecasting systems across a large network of road-haulage operations. Since 2021 I have worked as a principal data scientist, and I have been seconded to the research of Holt Data Labs Ltd since its programme began in April 2024. I am therefore familiar with the state of practice in freight demand forecasting and with the limitations of the methods in general use.

I was the competent professional for Project Polaris throughout the period, and I chaired the weekly technical review at which the results of the project were evaluated. In that capacity I had responsibility for the design of the experimental programme, for the assessment of whether each uncertainty had been resolved, and for approving the freeze of the reconciliation design on 21 October 2024.

In my professional judgement the uncertainties described in section 5.2.4 could not have been resolved by a competent professional working with the published methods and commercially available tools available at the start of the project. The reconciliation, calibration and cold-start methods were developed by the research team under my direction, and I was responsible for the backtesting design, the acceptance criteria and the decisions to adopt or reject each candidate method. I confirm that the descriptions in this narrative of what was known, what was attempted and what was learned are accurate to the best of my knowledge. The outcomes recorded in section 5.2.9 are, in my view, a genuine advance on the state of practice for sparse freight demand.

I also confirm that the work described in the Telematics Pipeline, which supports Project Polaris, was carried out under my technical oversight and that the uncertainties recorded for that project were, in my view, not resolvable from existing knowledge at its outset.

Signed: Dr Simon Achterberg
Position: Chief Scientist, Holt Data Labs Ltd
Date: 12 August 2025

---

## 6. Cost methodology and schedules

### 6.1 Scope of the cost schedules

The cost schedules in this section cover all expenditure claimed for the accounting period 1 April 2024 to 31 March 2025. They are divided into staff costs and other qualifying expenditure. Each figure is traceable to a source document listed in section 7, and the apportionment of staff time is explained in the methodology below.

The schedules are reproduced in the form used in the company's computation. The company's total expenditure for the period, which is used to calculate R&D intensity, is taken from its management accounts for the period and includes the qualifying expenditure above together with its other operating costs.

### 6.2 Period and basis

The period is 1 April 2024 to 31 March 2025. The employer National Insurance contributions in the staff schedule are calculated for the 2024-25 tax year, at the employer rate of 13.8% on earnings above the secondary threshold of £9,100. Employer pension contributions are calculated at 5% of salary, in accordance with the terms of each individual's arrangement. Salaries are the annual contractual figures in force throughout the period, pro-rated for any period of secondment that began after the start of the period.

### 6.3 Staff costs: schedule

The staff cost schedule is reproduced below. Each row shows the individual's role, their salary, employer NIC and pension contribution, the total employment cost, the proportion of working time claimed for R&D, and the amount claimed.

| Name | Role | Salary | Er NIC | Er pension | Total | R&D % | Claimed | Includes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Gavin Holt | Director | £140,000 | £18,064 | £7,000 | £165,064 | 40% | £66,026 |  |
| Dr Simon Achterberg | Chief Scientist (seconded) | £96,000 | £11,992 | £4,800 | £112,792 | 90% | £101,513 |  |
| Natasha Grieve | ML Engineer (seconded) | £74,000 | £8,956 | £3,700 | £86,656 | 90% | £77,990 |  |
| **Total staff** | | | | | | | **£245,529** | |

### 6.4 Other qualifying expenditure: schedule

| Category | Description | Claimed |
|---|---|---:|
| Data & cloud | Azure ML compute (recharged) | £88,000 |
| Subcontract (UK, connected) | Holt Engineering Services – modelling support £140,000 | £140,000 |
| **Total other** | | **£228,000** |

### 6.5 Total qualifying expenditure

Total qualifying expenditure (as claimed): **£473,529**

### 6.6 Relief computation

Relief computation (as claimed) – 86% additional deduction; 14.5% payable credit on surrendered loss

- extra deduction: £407,235
- surrenderable loss: £817,235
- payable credit: £118,499
- company turnover for context: £210,000
- total relevant expenditure (claimed, for intensity): £620,000; intensity as claimed = 76.4%
- trading loss before R&D deduction: £410,000

The extra deduction is the qualifying expenditure of £473,529 multiplied by 86%, giving £407,235 to the nearest pound. The trading loss after the extra deduction is £817,235 (£410,000 plus £407,235), which is below the cap of 186% of qualifying expenditure (£880,764). The whole of it is surrendered, and the payable credit is £817,235 multiplied by 14.5%, giving £118,499. The company's R&D intensity is its qualifying expenditure as a proportion of its total relevant expenditure for the period, which gives 76.4% on the figures above.

The company's trading loss before the R&D deduction is £410,000. The company has no other losses available in the period, and the whole of the enhanced loss is surrendered under the scheme. The company's turnover for the period was £210,000.

### 6.7 Methodology: staff time apportionment

Staff time has been apportioned to the research using three sources in combination: contemporaneous timesheets, the Jira history of the LDS project, and structured interviews with each individual. Where the sources disagreed, the interview was used to reconcile the difference and the reconciliation was recorded in the working papers.

**Dr Simon Achterberg (90%).** Dr Achterberg's timesheets record the time spent on the Polaris programme and the Telematics Pipeline. His Jira history records his assignment to the tickets listed in the work log at section 5, and his time on review and decision-making at the weekly technical review. Across the period, his recorded time on the two projects was consistently in the range of 85% to 95% of his working time. The figure of 90% is the average of the monthly proportions, rounded. In interview, Dr Achterberg confirmed that the remaining proportion related to the company's general administration and to matters outside the research.

**Natasha Grieve (90%).** Ms Grieve's timesheets and Jira history show her time on the LDS tickets relating to the cold-start method, the reconciliation procedure and the evaluation harness. Her recorded time on the projects was between 86% and 93% of working time in each month. The figure of 90% reflects the average of the monthly proportions. In interview, Ms Grieve confirmed that her working time outside the research was spent on the company's data preparation and on evaluation reporting, which the company regards as supporting activities within the same projects.

**Gavin Holt (40%).** Mr Holt's time is not recorded in timesheets. His apportionment was determined by interview and by a review of his calendar for the period, which showed meetings and working sessions relating to the research programme on a regular basis. Mr Holt's time is divided between research direction, the commercial relationships of the company and the preparation of the accounts. The figure of 40% reflects the proportion of his time that the company considers attributable to the research direction of the projects, having regard to the scale of the programme and to the interview evidence.

### 6.8 Methodology: other qualifying expenditure

**Data and cloud (£88,000).** The Azure Machine Learning compute, storage and model hosting used for the research are provided through an Azure subscription that is held by a related company and re-invoiced to the company at cost. The charges are invoiced quarterly, as follows: £20,000 for the quarter ending 30 June 2024, £22,000 for the quarter ending 30 September 2024, £24,000 for the quarter ending 31 December 2024, and £22,000 for the quarter ending 31 March 2025. The total of £88,000 is the sum of these four charges. The company has reviewed the charges against the Azure consumption reports for the subscription, which allocate usage by resource group, and has confirmed that the resource groups used by the company's projects account for the charges claimed. The company has included the consumption attributable to model training and evaluation, and has excluded the consumption of resources used for the company's general corporate purposes.

**Subcontract, modelling support (£140,000).** The company has engaged Holt Engineering Services Ltd, a UK company connected with the company, to provide modelling support to the research. The support comprises the preparation of model features, the execution of training runs to the company's specification, and the production of the evaluation reports listed in the appendices. The services are provided under a written arrangement. They are invoiced in four equal instalments of £35,000, and the total of £140,000 is the sum of those instalments. Invoice references and dates are listed at section 7.4. The company considers that the services were provided at a commercial rate for work of the type described and that the amount claimed is the amount properly payable for them.

### 6.9 Income

The company's turnover for the period was £210,000. This was commercial licensing income, received in three instalments of £70,000 under a licence and development agreement dated 15 April 2024. The licence and development agreement is recorded in the company's management accounts. The income has been disclosed in the company's return and is not offset against the qualifying expenditure in the computation above.

### 6.10 Items excluded from the claim

The following have been excluded from the cost schedules. The salary, employer National Insurance and pension costs of the company's two directly employed staff, the office administrator and the junior analyst, are not claimed because neither member of staff contributed to the research. Rent and office costs of Suite 4, Calder House, are not claimed. Costs of the production forecasting service after 27 March 2025 are not claimed. Expenditure on the data licence from TrakSure Data Ltd is not claimed, as it is treated as an overhead of the company's data infrastructure and not as a cost of the research.

### 6.11 Reconciliation to the management accounts

The totals in this section have been reconciled to the company's management accounts for the period. The staff costs are reconciled to the payroll records maintained for the individuals concerned, and the other qualifying expenditure is reconciled to the supplier invoices listed in section 7. The company's accountants have reviewed the reconciliation and have confirmed that the amounts claimed are consistent with the company's records for the period.

### 6.12 Declaration of computation

The computation in this section has been prepared by Ferrowen R&D Consulting Ltd on the basis of the company's records and the information provided by the company's senior officer. The senior officer has reviewed the computation and confirmed that the expenditure claimed was incurred on the research described in section 5.

---

## 7. Appendices

### 7.1 Competent professional curriculum vitae: Dr Simon Achterberg

**Name:** Dr Simon Achterberg
**Position in the claim:** Competent professional, Project Polaris and Telematics Pipeline
**Current role:** Chief Scientist, Holt Data Labs Ltd (seconded, full-time, from 8 April 2024)

**Qualifications**

- Doctor of Philosophy, Statistics and Machine Learning, thesis on the reconciliation of hierarchical time-series forecasts and the stability of constrained forecast adjustment
- Master of Science, Applied Statistics, with distinction
- Bachelor of Science, Mathematics, first class honours

**Professional experience**

- Principal Data Scientist, Holt Engineering Services Ltd, March 2021 to present (seconded to Holt Data Labs Ltd from 8 April 2024)
- Head of Data Science, a logistics technology business, 2017 to 2021, responsible for the design and evaluation of demand forecasting systems for road-haulage operations
- Senior Research Statistician, a university research group, 2013 to 2017, working on forecasting methods for sparse and intermittent demand
- Research Fellow, university department of statistics, 2010 to 2013

**Publications (selected)**

- Achterberg, S. (2014). Stability of constrained reconciliation for hierarchical forecasts. Doctoral thesis.
- Achterberg, S. and co-authors (2016). Adjustment procedures for intermittent demand series. Working paper, company research series.
- Achterberg, S. (2019). Evaluating calibration of probabilistic forecasts on sparse series. Working paper, company research series.

**Relevant technical skills:** Hierarchical and constrained forecast reconciliation; probabilistic forecasting and calibration; gradient-boosted and deep sequence models for time-series data; evaluation design; Python and R.

### 7.2 Competent professional curriculum vitae: Ms Natasha Grieve

**Name:** Ms Natasha Grieve
**Position in the claim:** Machine Learning Engineer, Project Polaris
**Current role:** Machine Learning Engineer, Holt Data Labs Ltd (seconded, full-time)

**Qualifications**

- Master of Engineering, Computing Science
- Bachelor of Engineering, Electronic and Electrical Engineering, upper second class honours

**Professional experience**

- Machine Learning Engineer, Holt Engineering Services Ltd, June 2022 to present (seconded to Holt Data Labs Ltd from 8 April 2024)
- Data Engineer, a logistics technology business, 2019 to 2022
- Graduate Software Engineer, 2018 to 2019

**Relevant technical skills:** Cold-start and representation learning for sparse behavioural data; evaluation harness design; data pipelines on cloud infrastructure; Python and Spark.

### 7.3 Senior officer

**Name:** Mr Gavin Holt
**Position:** Director, Holt Data Labs Ltd
**Role in the claim:** Senior officer; research direction of the company's programme; approval of this claim

Mr Holt has more than twenty years' experience in logistics technology and commercial operations. He is responsible for the company's commercial relationships and for its submissions to HMRC.

### 7.4 Supplier and invoice schedule

**Staff and secondment.** Remuneration for the seconded staff is paid in accordance with the arrangements set out in the staff cost schedule at section 6.3.

**Data and cloud.** Azure Machine Learning compute, storage and model hosting, invoiced quarterly through the re-invoicing arrangement described in section 6.8.

| Invoice reference | Period | Amount |
|---|---|---:|
| AZR-RI-2401 | Quarter ending 30 June 2024 | £20,000 |
| AZR-RI-2402 | Quarter ending 30 September 2024 | £22,000 |
| AZR-RI-2403 | Quarter ending 31 December 2024 | £24,000 |
| AZR-RI-2404 | Quarter ending 31 March 2025 | £22,000 |
| **Total** | | **£88,000** |

**Subcontract, modelling support.** Supplier: Holt Engineering Services Ltd, company number ZZ009958, UTR 9999995866.

| Invoice reference | Invoice date | Amount |
|---|---|---:|
| HES-2024-0031 | 30 June 2024 | £35,000 |
| HES-2024-0058 | 30 September 2024 | £35,000 |
| HES-2025-0012 | 31 December 2024 | £35,000 |
| HES-2025-0037 | 31 March 2025 | £35,000 |
| **Total** | | **£140,000** |

**Data licence (not claimed).** TrakSure Data Ltd, licence for anonymised GPS telematics data. Annual licence fee is treated as an overhead and is excluded from the claim.

**Agent.** Ferrowen R&D Consulting Ltd, Unit 6, Kessock Business Park, Leeds ZZ7 2TB. Fees for the preparation of this claim are not claimed.

**Commercial licensing income (receipts).**

| Invoice reference | Invoice date | Amount |
|---|---|---:|
| HDL-INV-0001 | 16 May 2024 | £70,000 |
| HDL-INV-0002 | 16 August 2024 | £70,000 |
| HDL-INV-0003 | 15 November 2024 | £70,000 |
| **Total** | | **£210,000** |

### 7.5 Timesheet extract

The timesheet extract below records the monthly proportion of working time recorded against the research for the two seconded staff whose time was apportioned from timesheets. The extract is the source of the apportionment at section 6.7. The average of the monthly proportions is 90% for each individual.

| Month | Dr Simon Achterberg | Natasha Grieve |
|---|---:|---:|
| April 2024 | 88% | 86% |
| May 2024 | 91% | 91% |
| June 2024 | 92% | 93% |
| July 2024 | 89% | 88% |
| August 2024 | 90% | 90% |
| September 2024 | 93% | 92% |
| October 2024 | 87% | 89% |
| November 2024 | 91% | 91% |
| December 2024 | 90% | 90% |
| January 2025 | 89% | 87% |
| February 2025 | 92% | 93% |
| March 2025 | 89% | 90% |
| **Average** | **90%** | **90%** |

Mr Holt's time is not recorded in timesheets. The calendar review referred to at section 6.7 identified research-direction meetings and working sessions on a regular basis throughout the period, and his apportionment of 40% was confirmed at interview.

### 7.6 Evidence index

The following documents are held by the company and are available to HMRC on request. Document references follow the company's internal scheme, in which HDL-LB denotes experiment registry and laboratory notebook entries, HDL-JR denotes Jira exports, HDL-MN denotes technical review minutes, HDL-TS denotes timesheet records, HDL-EV denotes evaluation reports and HDL-CT denotes contracts and invoices.

| Document ID | Date | Description | Relates to |
|---|---|---|---|
| HDL-LB-0107 | 8 April 2024 | Experiment registry opening entry and evaluation conventions | Polaris, section 5.2 |
| HDL-LB-0112 | 3 June 2024 | Temporal fusion training run log, sparse-lane collapse observations | Polaris, section 5.2.7 |
| HDL-LB-0129 | 10 July 2024 | Constrained reconciliation implementation and violation counts | Polaris, section 5.2.7 |
| HDL-LB-0141 | 2 August 2024 | Quantile calibration layer results and coverage tables | Polaris, section 5.2.7 |
| HDL-LB-0158 | 1 October 2024 | Cold-start leakage check, failure and repeat pass | Polaris, section 5.2.7 |
| HDL-LB-0203 | 9 December 2024 | Full evaluation run across lane bands | Polaris, section 5.2.9 |
| HDL-LB-0219 | 17 February 2025 | Cold-start holdout validation for new shippers | Polaris, section 5.2.9 |
| HDL-LB-0301 | 15 April 2024 | Telematics Pipeline opening entry and raw schema notes | Telematics Pipeline, section 5.3 |
| HDL-LB-0322 | 28 May 2024 | First event-based stop detection and accuracy against labelled sample | Telematics Pipeline, section 5.3.6 |
| HDL-LB-0348 | 11 October 2024 | Partitioned batch processing and recomputation timings | Telematics Pipeline, section 5.3.6 |
| HDL-JR-LDS-214 | 3 June 2024 | Jira export: "Temporal fusion model – lane-level demand" | Polaris, section 5.2 |
| HDL-JR-LDS-377 | 29 August 2024 | Jira export: "Cold-start for new shippers" | Polaris, section 5.2 |
| HDL-JR-LDS-502 | 19 June 2024 | Jira export: "Hierarchical reconciliation of forecasts" | Polaris, section 5.2 |
| HDL-JR-LDS-612 | 15 April 2024 | Jira export: "Pipeline dwell features" | Telematics Pipeline, section 5.3 |
| HDL-JR-LDS-661 | 16 September 2024 | Jira export: efficiency work on daily recomputation | Telematics Pipeline, section 5.3 |
| HDL-MN-0412 | 21 October 2024 | Technical review minutes: freeze of reconciliation design | Polaris, section 5.2.9 |
| HDL-MN-0433 | 20 January 2025 | Technical review minutes: intermediate-lane regression check | Polaris, section 5.2.9 |
| HDL-TS-2024-2025 | April 2024 to March 2025 | Timesheet records for seconded staff | Section 7.5 |
| HDL-EV-0007 | 10 March 2025 | Evaluation report: Project Polaris results | Polaris, section 5.2.9 |
| HDL-EV-0011 | 14 February 2025 | Evaluation report: Telematics Pipeline results | Telematics Pipeline, section 5.3.7 |
| HDL-CT-0015 | 15 April 2024 | Licence and development agreement, commercial licensing | Section 6.9 |
| HDL-CT-0022 | 15 April 2024 | Modelling support services arrangement | Section 6.8 |
| HDL-CT-0026 | 1 April 2024 | Data licence, anonymised telematics data | Section 4.7 |

### 7.7 Director's declaration

I, Gavin Holt, a director of Holt Data Labs Ltd, declare that:

1. I have read the claim pack for the accounting period 1 April 2024 to 31 March 2025, including the cover sheet, the Claim Notification Form, the Additional Information Form, the company background, the technical narrative, the cost schedules and the appendices.
2. The information in the pack is correct to the best of my knowledge and belief, and the company has taken reasonable care in preparing it.
3. The company undertook the research described in section 5 of the pack, and the expenditure claimed was incurred on that research.
4. The company's claim is made in accordance with the rules of the scheme. I understand that HMRC may ask for further information and evidence in support of the claim.

Signed: Gavin Holt
Position: Director, Holt Data Labs Ltd
Company number: ZZ010277
Date: 12 August 2025
