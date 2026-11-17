> SYNTHETIC TEST DATA – FICTIONAL COMPANY – PREPARED FOR HMRC HACKATHON – NOT A REAL TAX CLAIM

## 1. Cover sheet and claim summary

| Item | Detail |
|---|---|
| Claimant | Holt Engineering Services Ltd |
| Company number | ZZ009958 |
| Corporation Tax UTR | 9999995866 |
| Registered office | Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS |
| Parent undertaking | Veridian Holt Holdings Ltd (ZZ009931) |
| Accounting period | 1 April 2024 to 31 March 2025 |
| Scheme claimed | Merged scheme (R&D expenditure credit, taxable) |
| Claim agent | Tallowby & Crane Accountants |
| Senior officer | Gavin Holt, Director |
| Date of submission | 26 September 2025 |

### Claim summary

Holt Engineering Services Ltd ("the Company") claims research and development relief under the merged scheme for its accounting period from 1 April 2024 to 31 March 2025. The claim concerns the Company's Engineering Services R&D Programme 2024/25 ("the Programme"), which has two workstreams. The principal workstream is Lodestar, a programme of work developing machine-learning freight demand forecasting and dynamic load-matching for a road-haulage marketplace. The second is a platform workstream, which configured and extended the lakehouse data platform on which Lodestar runs.

The Company is the in-house engineering services function of the Holt group. Its engineers design, build and operate advanced analytics and data platforms, and during the period they devoted the majority of their working time to the Programme. The Programme was carried out to resolve scientific and technical uncertainties in forecasting sparse, lane-level freight demand, and in producing reliable forecasts at a scale and speed that a conventional approach could not deliver.

The principal advances sought are a hierarchical reconciliation method for sparse lane-level forecasts, and a cold-start method for forecasting the demand of shippers with no history on the platform. Both were developed, tested against backtesting harnesses, and handed over to production in the period.

### Summary of figures

| Item | Amount |
|---|---|
| Total qualifying expenditure | £513,134 |
| Expenditure credit at 20% (taxable) | £102,627 |
| Net benefit after Corporation Tax at 25% | £76,970 |

### Contents of this pack

1. Cover sheet and claim summary (this section)
2. Claim Notification Form: not required for this period (see section 2)
3. Additional Information Form
4. Company background, ownership, group, funding, staff and facilities
5. Technical narrative: the Programme, project by project
6. Cost methodology and schedules, and relief computation
7. Appendices: competent professional CV, evidence index, timesheet extract, supplier and invoice list, and director's declaration

All amounts are stated in pounds sterling and exclude VAT. Staff costs include employer's National Insurance contributions and employer's pension contributions, as shown in section 6.

---

## 2. Claim Notification Form

No Claim Notification Form is submitted with this claim. The Company's advisers are satisfied that a notification is not required for this accounting period, for the reasons set out below.

The Company claimed R&D relief for its accounting period ended 31 March 2023. That claim related to a small internal project to upgrade the Company's time-recording and purchasing system, and a notification was submitted for it and accepted. The Company has since claimed under the same scheme and has made a claim within each of the three accounting periods preceding this one. On that basis, the Company's understanding is that a further notification is not required for the accounting period 1 April 2024 to 31 March 2025.

The Company's prior-year notification and the signed computation for the 2022-23 claim are held on file under company number ZZ009958 and are available to HMRC on request.

For completeness, the R&D activities carried out in this period are described in full in section 5 of this pack. The technical information that a notification would otherwise provide, including the project titles, the nature of the work and the staff involved, is therefore available in the Additional Information Form in section 3 and the technical narrative in section 5.

Notification reference (prior period): held on HMRC file against ZZ009958.

---

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

---

## 4. Company background, ownership, group, funding, staff and facilities

### 4.1 Overview

Holt Engineering Services Ltd was incorporated on 14 March 2016 and has its registered office at Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS. The Company is the engineering services function of the Holt group. It employs the group's software engineers, data engineers, data scientists and IT staff, and makes their capability available to the group's operating companies.

The Company's business is the design, build, operation and support of data, analytics and digital platforms. Its work for the group falls into three areas: custom software and data engineering; analytics and machine-learning development; and the operation of the shared cloud data platform on which the group's operating companies depend. The Company has no external customers of any significance. Its activities are organised around the needs of the group's marketplace business and its other operating companies.

### 4.2 Ownership and group structure

The Company is wholly owned by Veridian Holt Holdings Ltd (company number ZZ009931), the group's parent undertaking. Veridian Holt Holdings Ltd is in turn wholly owned by Gavin Holt, who is the ultimate controlling party of the group. Gavin Holt is a director of the Company, of Veridian Holt Holdings Ltd, and of the group's operating companies.

The principal operating companies in the group are:

| Company | Company number | Business |
|---|---|---|
| Holt Freight Intelligence Ltd | ZZ009945 | Operates Holtline, a digital freight marketplace |
| Holt Data Labs Ltd | ZZ010277 | Data and analytics services, including the forecasting models used by the marketplace |
| Holt Engineering Services Ltd | ZZ009958 | Engineering and platform services (the Company) |

All group companies share the registered office at Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS. The group's operating decisions are taken at the level of the parent, and the directors of each company meet regularly as a group board.

### 4.3 Revenue and intra-group arrangements

The Company's turnover for the period was £1,350,000. Almost all of that turnover is recharge income from group companies, earned under written intra-group services agreements. The Company describes this income as the group engineering services revenue stream.

The principal agreement is an intra-group services agreement dated 2 April 2024 between the Company and Holt Freight Intelligence Ltd, under which the Company provides engineering staff and services to that company. Under the agreement, the services are recharged at cost plus a 15 per cent margin. Staff time and the platform licence used in the services are recharged through the same mechanism. Other group companies, including Holt Data Labs Ltd, receive engineering services under similar written arrangements. Copies of the agreements are indexed in section 7.

The revenue stream is stable and predictable. It is reviewed annually by the group board, and the cost base and margin are agreed in advance for each financial year.

### 4.4 Staff

At 31 March 2025 the Company employed 41 people, of whom 34 were engineering, data or platform staff, four were IT and service-desk staff, and three were in finance, administration and management. The average number of employees during the period was 41.

The engineers and data staff are based at Calder House. Their work for the group is organised into teams aligned to the group's operating companies. Staff time is recorded in the Company's Jira instance and in its timesheet system, which is the basis of the apportionments set out in section 6.

The Programme's technical staff are: Dr Simon Achterberg, Head of Data Science (salary £96,000); Natasha Grieve, ML Engineer (£74,000); Imran Qadir, ML Engineer (£71,000); Bethany Coles, Data Engineer (£63,000); and Luke Fensome, Platform Engineer (£66,000). All five are full-time employees of the Company on permanent contracts. Their employment, pay and benefits are administered by the Company's finance team. Gavin Holt, Director, provides strategic and technical oversight of the group's engineering work and is paid a director's salary of £140,000.

### 4.5 Facilities

The Company occupies Suite 4 at Calder House, a serviced office building in Wakefield, under a lease with the parent undertaking. The suite includes engineering workspaces, a secure development environment, and a small server room used for on-premise monitoring. The Company's production workloads run on a cloud platform. The platform licence used for the Programme is a subscription to a managed lakehouse service, which is described in section 5 and in the supplier list in section 7.

Development and test environments for the Lodestar workstream are provisioned on the same cloud platform and are isolated from production. Source code is held in the group's private source repository and is backed up daily.

### 4.6 Funding

The Company is funded from its trading income, which is principally the intra-group recharge revenue described above, together with retained earnings from previous years. The Company has an intra-group working capital facility with its parent undertaking, which it has not drawn on during the period. No external borrowing has been taken out, and no grants or other public funding have been received for the Programme.

### 4.7 Previous R&D activity

The Company claimed R&D relief for its accounting period ended 31 March 2023. That claim related to a small internal project to upgrade the time-recording and purchasing system used across the group. The project was modest in scale, and the claim was made under the same scheme. The Company's prior-year claim file is held on the Company's records and is referred to in section 2.

The Programme described in this pack is the Company's principal R&D activity for the accounting period 1 April 2024 to 31 March 2025. The Company's engineers have worked on technical problems of this kind since the group began operating its marketplace, and the Company considers the Programme to be a continuation of that established engineering capability.

### 4.8 Relationship between the Company and the Lodestar programme

The Lodestar programme originated within the group's marketplace business, which operates the forecasting and load-matching services the programme develops. The Company was asked to develop and operate those services on behalf of the group, and it provided the engineering capability to do so. The Company's engineers are employed by the Company and work under its direction, and the Company's technical plan for the programme sets out the research objectives, the methods and the outputs.

The Company is the in-house engineering capability for the group. It develops advanced analytics on behalf of the group, and the Lodestar workstream is its own R&D programme, which it manages and for which it holds the technical records and the results.

---

## 5. Technical narrative

### 5.1 Introduction and scope

This section sets out the technical work of the Company's Engineering Services R&D Programme 2024/25 ("the Programme") for the accounting period 1 April 2024 to 31 March 2025. It is written project by project, in the order set out in the Additional Information Form in section 3. For each project it describes the baseline, the advance sought, the scientific and technological uncertainties, the methodology, a chronological work log with dated iterations, the outcomes, and the boundaries of the work claimed.

The Programme has two projects. Project 1 is the Lodestar workstream, which develops machine-learning freight demand forecasting and dynamic load-matching for the road-haulage marketplace operated by the group. Project 2 is the platform workstream, which configures and extends the lakehouse data platform on which Lodestar runs. Work tracking uses the Jira project key LDS. Tickets are cited in this section by their key and title, and the Jira export for each ticket is indexed in section 7.

The Company is the in-house engineering capability for the group, and it develops advanced analytics on behalf of the group. The Lodestar workstream is the Company's own R&D programme. The Company set its research objectives, owned its methods, and holds the technical records and results of the work.

### 5.2 Context

The group operates a digital freight marketplace in which shippers post loads and hauliers bid to move them. The marketplace serves a few thousand registered hauliers and several hundred shippers, and its volumes are concentrated in a small number of corridors between major distribution centres. Its operating model depends on accurate expectations of demand, because capacity is sought in advance of the loads it is intended to carry. Forecasts of demand on each lane, meaning each origin–destination pair, inform how capacity is sought, how loads are priced, and how loads are matched to available vehicles. Accurate forecasts matter most where demand is most uncertain, and that is where the marketplace's existing methods performed least well.

The marketplace generates position data from vehicles equipped with GPS telematics. The Company's data set for the Programme comprises 3.2 billion telematics position records, licensed from TrakSure Data Ltd and provided to the Company under the group's data licence held by Holt Freight Intelligence Ltd. The records cover 2021 to early 2024 and were combined with shipper, load and lane records from the marketplace. The raw data was loaded, deduplicated and joined to produce the lane-level demand history on which the Programme's models are trained and evaluated.

### 5.3 Project 1: the Lodestar workstream

#### 5.3.1 Background and problem

Freight demand is not evenly distributed. A small number of corridors carry a large share of the marketplace's volume, and those corridors have long, dense histories that support reliable forecasting. Most origin–destination pairs are different. They carry occasional loads, their history is short, and their demand is intermittent. For the great majority of these lanes, the marketplace had no forecast it could rely on, and load-matching for those lanes was largely reactive.

The problem the Programme addresses is therefore the forecasting of demand where data is sparse, and the production of forecasts for shippers the platform has not yet seen. Both problems are difficult, and neither is addressed well by the methods the marketplace used at the start of the period.

#### 5.3.2 Baseline

The baseline for Project 1 is the state of freight demand forecasting as it stood on 1 April 2024. Existing forecasting approaches assume dense, stationary demand signals; at lane level only around 8% of lanes exhibit weekly volume sufficient for conventional models. For the remaining lanes, a seasonal smoothing model fitted at regional level and disaggregated to lanes by share was used. That approach produced usable results on busy corridors but gave poor results on the long tail, where disaggregation spread a regional total across many lanes that had no history of their own.

A competent professional in freight analytics at that date would have recognised the long tail as the principal unresolved problem, and would have identified two gaps: the absence of a principled way to keep lane-level forecasts consistent with aggregate totals when most lanes are sparse, and the absence of any method for new shippers with no history. The Company's baseline accordingly reflects the state of the art for those two problems as a competent professional would have understood it, and not merely the marketplace's own methods.

#### 5.3.3 Advance sought

The Company sought an advance in three linked respects.

First, a hierarchical reconciliation method for sparse lane-level forecasts. The method forecasts at several levels of the hierarchy of lanes, regions and shippers, and then reconciles those forecasts so that lower-level forecasts sum to their parents. The Company's advance is an adaptation of reconciliation to the case where most of the lowest-level series are too sparse to forecast on their own, so that the reconciliation must draw strength from the levels above them without distorting the dense corridors.

Second, a cold-start method for new shippers. The method represents each shipper by a profile built from its declared load types, its geography and its early bookings, and forecasts a new shipper's demand from the behaviour of established shippers with the nearest profiles. The advance lies in combining that profile-based transfer with the reconciliation hierarchy, so that a new shipper's forecast is coherent with the lanes it uses.

Third, calibrated uncertainty output. The load-matching service needs to know not only the expected demand on a lane but how confident the forecast is. The Company sought a method of producing calibrated prediction intervals for sparse series, so that the matching service could act on a forecast with a stated confidence.

#### 5.3.4 Scientific and technological uncertainties

At the outset of the Programme the Company identified the following uncertainties, which could not be resolved from published practice and which the work was designed to resolve.

Uncertainty 1: whether reconciliation could be made coherent for sparse lanes without degrading accuracy on dense corridors. A reconciliation that works well for dense series may distort sparse ones, and the Company did not know whether a single scheme could serve both.

Uncertainty 2: whether information could be transferred from established shippers to new shippers without introducing systematic bias. Profile-based transfer can work well on average and still produce biased forecasts for particular profiles, and the Company did not know whether the bias could be controlled.

Uncertainty 3: whether temporal fusion models could be trained on sparse lane-level series to an accuracy that exceeded the baseline. Such models were developed for dense, multivariate series, and their behaviour on intermittent demand was not established.

Uncertainty 4: whether calibrated intervals would be reliable enough to drive matching decisions, given the small number of observations on most lanes.

Uncertainty 5: whether the resulting improvement in forecast accuracy would translate into load-matching yield sufficient to justify the marketplace's pricing changes. This uncertainty is commercial in character, but it bears directly on whether the forecasts can be used in production, and the Company resolved it by controlled comparison.

#### 5.3.5 Methodology

The methodology followed a staged design. Each stage produced a backtested result that informed the next.

Data preparation. Telematics records were deduplicated, matched to loads, and aggregated to daily and weekly volumes per lane. Lanes were defined by origin and destination regions, and a lane was retained in the hierarchy whether or not it met the density threshold. Feature tables were built for shippers, lanes and regions, covering load type, seasonality, distance band, and recent booking activity. The feature tables are versioned so that every model can be reproduced from its inputs.

Baseline models. Gradient-boosted decision trees were fitted to the lane-level series, using the lane, region and shipper features. The models were tuned for the Company's data, with a hyperparameter search over tree depth, learning rate, regularisation and subsampling. The tuned models served as the comparator for the advance, and as the working models for the dense corridors.

Temporal fusion models. A temporal fusion transformer was configured for the multivariate lane series. The network was trained on the shared feature set, with static covariates for shipper and lane, and with known future inputs for calendar effects. The Company adapted the architecture's quantile output to produce the prediction intervals described in section 5.3.3.

Reconciliation. The Company implemented a hierarchical reconciliation for the lane, region and shipper levels. Base forecasts were produced at each level and reconciled to be coherent with the hierarchy. The Company's adaptation for sparse series weights each level's contribution by the amount of history available at that level, so that a lane with little history draws more strength from its region. The Company regards this weighting as the central technical contribution of the advance, because it allows coherence to be maintained without distorting dense corridors.

Cold-start. A profile was built for each shipper from its declared load types, geography and early bookings. For a new shipper, the method selects the nearest established shippers by profile distance and uses their reconciled forecasts as a prior, which is then updated as bookings arrive. Bias was monitored by comparing forecasts for held-out shippers against their realised demand.

Evaluation. A rolling-origin backtesting harness was built to evaluate each method on several held-out windows. Accuracy was measured by weighted mean absolute percentage error across lanes, with separate reporting for the dense corridors and for the sparse tail. Calibration was measured by the coverage of the prediction intervals. The matching yield test compared load-matching outcomes with and without the new forecasts over a controlled period.

Feature selection and tuning. The feature set for the lane models was reduced from an initial 140 candidate features to 38 by a combination of importance ranking and correlation pruning. Each retained feature was checked for leakage by confirming that it was available at the forecast origin. The tuning procedure fixed the training window at 104 weeks for dense lanes and extended it to 156 weeks for lanes in the sparse tail, where longer history was needed to estimate seasonality. Early stopping was applied to every run on the validation window, and the final configuration for each tier was frozen before the held-out windows were scored, so that the reported results are not affected by selection on the test periods.

Residual analysis. After each candidate was scored, residuals were examined by lane tier, by season, and by shipper. Where residuals showed systematic structure, the feature set or the reconciliation weights were revised and the candidate was rescored on all six windows. The record of each revision is kept in the Jira ticket for the relevant iteration, and the design record HES-DR-0715 sets out the reasons for the weighting scheme adopted.

Infrastructure and reproducibility. Training runs were executed on managed compute sized to the data, with each run logged to the lakehouse together with its feature version, configuration and random seed. A rerun from the same inputs was required to reproduce the reported metrics before a result was accepted into the backtesting report.

#### 5.3.6 Chronological work log

The work log below records the iterations of Project 1 in date order. Each entry cites the Jira ticket under which the work was carried out.

- **8 April 2024. LDS-118, Telematics ingestion and deduplication.** The raw position records were loaded and deduplicated. Duplicate records from overlapping device transmissions were identified and removed. Ingestion ran for the full 3.2 billion records.
- **22 April 2024. LDS-118 (continued).** Load-matching joins were validated against a sample of 4,000 completed loads. A small number of mismatched timestamps were traced to the device clock offset and corrected.
- **13 May 2024. LDS-146, Lane definition and origin–destination aggregation.** Lanes were defined by origin and destination region. The density of each lane was profiled, and the proportion of lanes with weekly volume above the density threshold was confirmed at under 8%.
- **3 June 2024. LDS-233, Gradient-boosted baseline, lane-level.** The first gradient-boosted model was fitted to the lane series. Results on the dense corridors were encouraging, and results on the sparse tail were used to set the reconciliation requirements.
- **19 June 2024. LDS-214, Temporal fusion model, lane-level demand.** A temporal fusion transformer was configured for the lane series. Initial training runs failed to converge on sparse series and were repeated with revised loss weighting.
- **11 July 2024. LDS-290, Feature store for shipper and lane attributes.** Versioned feature tables were created. Every training run was linked to a feature version so that results could be reproduced.
- **29 July 2024. LDS-214 (continued).** The temporal fusion model was retrained with the revised loss. Accuracy on the dense corridors matched the gradient-boosted baseline, and accuracy on the sparse tail was not yet better than the baseline.
- **16 August 2024. LDS-377, Cold-start for new shippers.** A profile-based cold-start method was designed. The first version selected nearest shippers by profile distance and used their forecasts as the prior.
- **9 September 2024. LDS-318, Hyperparameter sweep, gradient-boosted models, lane tier 2.** A sweep of 240 configurations was run over the second tier of lanes. The best configuration improved weighted error on that tier by a margin the Company regarded as material.
- **30 September 2024. LDS-412, Backtesting harness, rolling origin.** A rolling-origin harness was built with six held-out windows. All candidate methods were evaluated on the same windows.
- **14 October 2024. LDS-455, Evaluation against weighted MAPE.** The evaluation was run across all methods. The comparison established that conventional models performed well on the dense corridors and poorly on the sparse tail, as expected.
- **4 November 2024. LDS-502, Hierarchical reconciliation of forecasts.** The reconciliation method was implemented. The first version treated all levels equally and distorted the dense corridors. The weighting described in section 5.3.5 was introduced, and the distortion was removed.
- **2 December 2024. LDS-377 (continued).** The cold-start method was extended to use the reconciled forecasts as its prior. Bias was measured on twelve held-out shippers and was found to be within the tolerance set for the matching service.
- **13 January 2025. LDS-502 (continued).** Reconciliation was rerun across all six backtesting windows. Coherence was maintained on every window and accuracy on the sparse tail improved against the baseline.
- **27 January 2025. LDS-566, Production inference pipeline, batch.** The model pipeline was packaged for nightly batch inference and tested against the production data volumes.
- **17 February 2025. LDS-611, Calibration and drift monitoring.** Prediction intervals were calibrated on the held-out windows, and drift alerts were configured for coverage and bias.
- **10 March 2025. LDS-566 and LDS-611 (controlled comparison).** A controlled comparison of load-matching yield was run for three weeks, with and without the new forecasts. Yield improved in the forecast group.
- **24 March 2025. LDS-640, Handover and documentation.** The Lodestar workstream was handed over to production operation, with documentation of the models, the reconciliation method, the cold-start method and the monitoring.

#### 5.3.7 Outcomes

The principal outcomes of Project 1 are as follows.

On the dense corridors, the reconciled forecasts were within a fraction of a percentage point of the tuned gradient-boosted baseline, and the reconciliation kept them coherent with their parents.

On the sparse tail, which comprises most lanes, weighted mean absolute percentage error fell from 31% under the regional disaggregation baseline to 19% under the reconciled and cold-start forecasts, across the six backtesting windows. The Company regards that improvement as the principal technical result of the advance.

The cold-start method produced forecasts for twelve held-out shippers with bias inside the tolerance set for the matching service. The calibrated intervals covered the realised demand in the stated proportion on the held-out windows, and the drift alerts were in place from the handover.

In the controlled matching comparison, the forecast group showed a higher share of loads matched within the target window. The Company regards this as confirmation that improved forecast accuracy translates into operational benefit.

The outcomes also include several results that the Company did not anticipate at the outset. The sparse-tail gains were largest for lanes with between four and nine weeks of history, which the Company had not expected to be the most responsive group. The reconciliation weighting, which was introduced to protect the dense corridors, turned out to be the element of the advance that most affected the cold-start forecasts, because it governed how strongly a new shipper's prior was tied to its lanes. The Company records these observations as evidence that the advance was not a foregone conclusion, and that the results depended on design choices that the Company had to make and test.

Finally, the handover documentation establishes that the outputs can be reproduced by an engineer who was not involved in the original work. That was an explicit requirement of the Programme, and it was met in the reproducibility test recorded under LDS-478.

#### 5.3.8 Boundaries of the work

The work claimed for Project 1 starts on 1 April 2024, when the Company's engineers began the telematics ingestion work recorded under LDS-118. The Company's scoping of the data pipeline in February 2024 is background context and is not claimed. The work ends on 31 March 2025, when the workstream was handed over to production operation. Routine production monitoring after handover is not claimed.

### 5.4 Project 2: the platform workstream

#### 5.4.1 Background and baseline

The platform on which the Company's analytics pipelines ran at 1 April 2024 was a general-purpose data warehouse with batch extraction from source systems. It was adequate for reporting. It was not designed to hold, version and serve the lane-level feature sets and model artefacts required by Lodestar, nor to run high-volume telematics ingestion, feature computation and inference within the latency the load-matching service requires.

The baseline for the platform workstream is therefore the warehouse and batch architecture as it stood at 1 April 2024. A competent professional in data engineering would have regarded a warehouse of that kind as unsuitable for the combined requirements of versioned features, reproducible models and high-volume inference, and would have sought a lakehouse architecture for them.

#### 5.4.2 Advance sought

The advance sought was in the orchestration of high-volume telematics ingestion, feature computation and model inference on a single lakehouse, with reproducible versioning of data, features and models. The Company's specific contribution is the combination of those elements into one orchestrated pipeline that can be rerun exactly from any version of its inputs, and that serves the forecast outputs within the matching service's time window.

#### 5.4.3 Uncertainties

Whether the platform could sustain ingestion and feature computation for 3.2 billion records within the required time window. Whether model and feature versions could be reproduced exactly from their inputs. Whether batch inference could be run nightly without compromising the freshness of the forecasts.

#### 5.4.4 Methodology and work log

The platform was configured on a managed lakehouse service, selected for its support of versioned tables and its batch and streaming interfaces. The Company built the ingestion, feature and inference pipelines, the orchestration between them, and the access controls and monitoring.

- **1 May 2024. LDS-160, Orchestration of nightly pipelines.** The orchestration framework was selected and configured. Dependencies between ingestion, feature and inference jobs were defined.
- **18 June 2024. LDS-188, Performance testing of ingestion.** Ingestion throughput was measured on a representative sample. Partitioning was changed to improve throughput, and the full ingestion run was brought within the window.
- **9 July 2024. LDS-290 (platform).** Versioned feature tables were implemented on the lakehouse, so that each feature set could be reproduced from the inputs and version identifiers.
- **22 August 2024. LDS-335, Access controls and data lineage.** Access controls were implemented by role, and lineage was recorded for each table and feature.
- **12 December 2024. LDS-478, Reproducibility test.** A complete rerun of the pipeline from a fixed input version was compared with the original outputs and found identical.
- **21 February 2025. LDS-566 (platform).** Batch inference was run in production trials on successive nights. Freshness of the forecasts was measured and found to be within the matching service's requirement.
- **28 March 2025. LDS-640 (platform).** The platform configuration and pipeline documentation were handed over with the Lodestar workstream.

#### 5.4.5 Outcomes and boundaries

The platform reproduces any model run from a fixed input version, and it completes nightly ingestion and inference within the window. The Company regards the combination as a novel orchestration of these elements at this scale. The work claimed for Project 2 runs from 1 April 2024 to 31 March 2025.

Sizing and tests. Cluster sizes for ingestion and feature computation were chosen by a sequence of load tests, which increased the input volume in steps until the ingestion window was exceeded and then identified the configuration that met it with margin. The partitioning scheme was chosen by testing three alternatives on the same sample, and the scheme that gave the best throughput for the telematics data was adopted. Access controls were tested by role, and lineage was checked by tracing a sample of forecast outputs back to their source records. Each test result is held in the Jira ticket for the relevant work item.

Operational risks. The Company's engineers identified the main operational risks of nightly batch inference as late-arriving telematics data, schema changes in the source systems, and failure of a dependent job. Each was addressed in the orchestration design by dependency checks, schema validation on ingestion, and automatic retry with alerting. The design of those controls is a part of the platform advance, because the combination of reproducibility and nightly freshness had not previously been achieved on the group's data.

### 5.5 Competent professional statement

I am the Head of Data Science at Holt Engineering Services Ltd. I have worked in data science and machine learning for more than fourteen years, including applied work on demand forecasting, optimisation and large-scale data platforms. I hold a doctorate in statistics and have published on hierarchical forecasting and on the evaluation of probabilistic forecasts.

In my professional judgement, the state of knowledge in freight demand forecasting at 1 April 2024 did not allow a competent professional to forecast sparse lane-level demand reliably, or to forecast the demand of new shippers from first principles. Those problems were not resolved by existing published practice. The methods the Lodestar workstream developed resolved them in the manner described in section 5.3, and the work was carried out by the Company's engineers under my direction and under the technical plan for the Programme.

In my professional judgement the uncertainties described in this narrative could not have been resolved by a competent professional working with the published methods and commercially available tools available at the start of the project. The reconciliation and cold-start methods were developed by the Company's engineers under my direction, and I was responsible for the backtesting design, the acceptance criteria and the decisions to adopt or reject each candidate method. I confirm that the descriptions in this narrative of what was known, what was attempted and what was learned are accurate to the best of my knowledge.

Dr Simon Achterberg, Head of Data Science, Holt Engineering Services Ltd.

### 5.6 Summary

The Programme addressed the forecasting of sparse freight demand and the reproducibility of data-driven forecasts at scale. Project 1 produced a hierarchical reconciliation method and a cold-start method for sparse lane-level forecasting, with calibrated intervals, and brought the forecasts into production. Project 2 produced a reproducible lakehouse pipeline that serves those forecasts within the required window. Each project's boundaries are stated above, and the work is evidenced in the Jira export, the backtesting records and the timesheet extract in section 7.

---

## 6. Cost methodology and schedules

### 6.1 Basis of preparation

This section sets out the qualifying expenditure claimed by Holt Engineering Services Ltd for the accounting period 1 April 2024 to 31 March 2025, under the merged scheme. Staff costs are for the 2024-25 National Insurance year. All figures are in pounds sterling and exclude VAT. The schedules below are prepared from the Company's payroll records, its general ledger, and the apportionment records described in section 6.3.

Qualifying expenditure is limited to staff costs and software costs that are directly attributable to the Programme. Staff costs comprise salary, employer's National Insurance contributions and employer's pension contributions. Each figure in the staff schedule is the apportioned amount of the total cost of the employee for the period.

### 6.2 Staff costs schedule

The table below shows, for each employee whose time is claimed, the annual cost of the employee, the proportion of the employee's time attributed to the Programme, and the amount claimed.

| Name | Role | Salary | Er NIC | Er pension | Total | R&D % | Claimed | Includes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Dr Simon Achterberg | Head of Data Science | £96,000 | £11,992 | £4,800 | £112,792 | 95% | £107,152 |  |
| Natasha Grieve | ML Engineer | £74,000 | £8,956 | £3,700 | £86,656 | 95% | £82,323 |  |
| Imran Qadir | ML Engineer | £71,000 | £8,542 | £3,550 | £83,092 | 95% | £78,937 |  |
| Bethany Coles | Data Engineer | £63,000 | £7,438 | £3,150 | £73,588 | 95% | £69,909 |  |
| Luke Fensome | Platform Engineer | £66,000 | £7,852 | £3,300 | £77,152 | 95% | £73,294 |  |
| Gavin Holt | Director | £140,000 | £18,064 | £7,000 | £165,064 | 30% | £49,519 |  |
| **Total staff** | | | | | | | **£461,134** | |

### 6.3 Apportionment methodology

The apportionment of staff time to the Programme rests on two sources of evidence, according to the role of the employee.

For the five technical staff, the apportionment is based on time recorded in the Company's timesheet system against Jira tickets in the LDS project. Each employee records time against the ticket on which the work was done, and time is recorded against the group's operational tickets separately. For the period, the time recorded against LDS tickets averaged 95% of total hours for each of the five employees. The Company applied that proportion to the full cost of each employee, including employer's National Insurance and pension contributions. The timesheet extract in section 7 shows the hours recorded for each employee. The 5% of time not attributed to the Programme is support work, including recruitment, training, and the group's operational incident rota.

The Head of Data Science reviewed the 95% figure for each technical employee at the end of the period, and confirmed that it reflected the work carried out. His review is recorded in the Company's internal records.

For Gavin Holt, Director, the apportionment is an estimate made by the director himself, on the basis of his time spent in technical review of the Programme, in decisions on its architecture and in the approval of its outputs. The 30% figure reflects the director's estimate of the proportion of his working time that related to the Programme, and it has been reviewed with the Company's finance team. The director's remaining time is spent on the group's operational and commercial matters, and on the management of the parent undertaking.

### 6.4 Software costs schedule

| Category | Description | Claimed |
|---|---|---:|
| Software | Databricks-style platform licence | £52,000 |
| **Total other** | | **£52,000** |

The platform licence is a subscription to a managed lakehouse service, provided by Meridian Lakehouse Ltd. The subscription is used throughout the period for the ingestion, feature and inference pipelines of Project 1 and for the platform work of Project 2. The full annual subscription is included in qualifying expenditure because the platform is used for the Programme's R&D work throughout the period. The same platform also supports the group services described in section 4.3, and the cost of the subscription is recovered through those recharges in the Company's turnover.

The invoice for the subscription is listed in the supplier and invoice list in section 7.

### 6.5 Total qualifying expenditure

| Category | Amount |
|---|---|
| Staff costs | £461,134 |
| Software | £52,000 |
| **Total qualifying expenditure (as claimed)** | **£513,134** |

### 6.6 Relief computation

The Company claims the merged scheme's expenditure credit at the rate of 20% of qualifying expenditure. The expenditure credit is taxable, and is brought into account in the Company's Corporation Tax computation for the period. The net benefit is calculated after Corporation Tax at the main rate of 25%.

Expenditure credit at 20% of £513,134 is £102,627 (rounded to the nearest pound).

Net benefit after Corporation Tax at 25% of the expenditure credit is £76,970 (rounded to the nearest pound).

The computation is summarised below.

- credit: £102,627
- net: £76,970
- company turnover for context: £1,350,000

The Company's turnover is shown for context only. It does not affect the expenditure credit computed on the qualifying expenditure above.

### 6.7 Other costs

No consumables, externally provided workers, subcontract costs or other costs are claimed. No subsidy or grant has been received in respect of the expenditure claimed, and none falls to be deducted under the scheme rules.

### 6.8 Reconciliation to the general ledger

The staff costs in the schedule have been reconciled to the Company's payroll ledger for the period, after adding employer's National Insurance and pension contributions, and after applying the apportionment percentages set out in section 6.3. The software cost has been agreed to the subscription invoice for the period, net of VAT. The reconciliations are held on file and are available on request.

### 6.9 Review of apportionments

The apportionments in section 6.2 were reviewed by the Company's finance team and by the Head of Data Science before the claim was prepared. The review compared the timesheet hours with the Jira activity for each technical employee, and confirmed that the time recorded against LDS tickets matched the work described in the work log in section 5.3.6. Where a ticket was recorded against more than one workstream, the time was allocated to the workstream recorded in the ticket's own description.

The Company's finance team also considered whether the apportionment of the director's time was consistent with the director's role. The 30% figure was agreed on the basis of the director's estimate, which was tested against his calendar for the period and the decisions recorded in the Programme's meeting records, including HES-MR-0317.

The Company will retain the timesheets, the Jira exports and the review records for the period required by the scheme rules, and will make them available to HMRC on request.

### 6.10 Timing and presentation

The claim is made for the accounting period ended 31 March 2025 and is submitted within the period permitted for amendment and submission under the scheme rules. The expenditure credit is brought into account in the Company's Corporation Tax return for the same period. The Company has not claimed relief for any expenditure incurred before 1 April 2024 or after 31 March 2025.

---

## 7. Appendices

### Appendix A: Competent professional, curriculum vitae

**Dr Simon Achterberg**
Head of Data Science, Holt Engineering Services Ltd (since 2019)

**Profile.** Data scientist with more than fourteen years' experience in machine learning, demand forecasting, optimisation and large-scale data platforms, in logistics, transport and retail. Leads the Company's data science function and its technical plan for the Engineering Services R&D Programme.

**Qualifications**
- Doctor of Philosophy (PhD), Statistics, University of Northmoor, 2011. Thesis: "Hierarchical structures for sparse count series".
- Master of Science, Applied Statistics, University of Northmoor, 2007.
- Bachelor of Science (Honours), Mathematics, University of Northmoor, 2006.

**Employment history**
- 2019 to date: Head of Data Science, Holt Engineering Services Ltd. Leads the data science function, sets technical direction for the Company's analytics work, and is responsible for the Lodestar workstream's technical plan.
- 2016 to 2019: Lead Data Scientist, Brackwater Logistics Ltd. Built demand forecasting for a regional distribution network.
- 2012 to 2016: Senior Data Scientist, Fennick Retail Analytics Ltd. Developed replenishment forecasting and optimisation models for multi-site retail.
- 2010 to 2012: Research Associate, Department of Statistics, University of Northmoor. Research on hierarchical and probabilistic forecasting.

**Publications (selected)**
- Achterberg, S. (2014). "Hierarchical forecasting under sparsity." Journal of Logistics Analytics, 6(2), 117–139.
- Achterberg, S. and Ruddock, P. (2017). "Evaluating probabilistic forecasts for intermittent demand." Proceedings of the Northmoor Forecasting Symposium.

**Professional memberships.** Member of the Royal Statistical Society. Member of the British Computer Society.

### Appendix B: Evidence index

The following records are held by the Company and are available to HMRC on request. Jira references are to the LDS project.

| Reference | Date | Description |
|---|---|---|
| LDS-118 | 8 April 2024 to 22 April 2024 | Telematics ingestion and deduplication, with join validation (Jira export) |
| LDS-146 | 13 May 2024 | Lane definition and origin–destination aggregation (Jira export) |
| LDS-160 | 1 May 2024 | Orchestration of nightly pipelines (Jira export) |
| LDS-188 | 18 June 2024 | Performance testing of ingestion (Jira export) |
| LDS-214 | 19 June 2024 to 29 July 2024 | Temporal fusion model, lane-level demand (Jira export) |
| LDS-233 | 3 June 2024 | Gradient-boosted baseline, lane-level (Jira export) |
| LDS-290 | 11 July 2024 | Feature store for shipper and lane attributes (Jira export) |
| LDS-318 | 9 September 2024 | Hyperparameter sweep, gradient-boosted models, lane tier 2 (Jira export) |
| LDS-335 | 22 August 2024 | Access controls and data lineage (Jira export) |
| LDS-377 | 16 August 2024 to 2 December 2024 | Cold-start for new shippers (Jira export) |
| LDS-412 | 30 September 2024 | Backtesting harness, rolling origin (Jira export) |
| LDS-455 | 14 October 2024 | Evaluation against weighted MAPE (Jira export) |
| LDS-478 | 12 December 2024 | Reproducibility test for pipeline reruns (Jira export) |
| LDS-502 | 4 November 2024 to 13 January 2025 | Hierarchical reconciliation of forecasts (Jira export) |
| LDS-566 | 27 January 2025 to 10 March 2025 | Production inference pipeline, batch; controlled matching comparison (Jira export) |
| LDS-611 | 17 February 2025 | Calibration and drift monitoring (Jira export) |
| LDS-640 | 24 March 2025 to 28 March 2025 | Handover and documentation (Jira export) |
| HES-DR-0715 | 4 November 2024 | Design record: weighting scheme for hierarchical reconciliation of sparse series |
| HES-BT-1014 | 13 January 2025 | Backtesting report, six rolling-origin windows |
| HES-MR-0317 | 17 March 2025 | Meeting record: matching yield comparison and go-live decision |
| HES-PC-0226 | 26 February 2025 | Platform performance and freshness trial results |
| HES-SA-0402 | 2 April 2024 | Intra-group services agreement, Holt Engineering Services Ltd and Holt Freight Intelligence Ltd (copy) |
| HES-TS-2425 | 1 April 2024 to 31 March 2025 | Timesheet export for the five technical staff (see Appendix C) |
| HES-PR-2425 | 1 April 2024 to 31 March 2025 | Payroll ledger extract, employer's NIC and pension |
| HES-SW-0871 | 30 April 2024 | Platform subscription invoice (see Appendix D) |

### Appendix C: Timesheet extract

The extract below summarises the hours recorded by the five technical staff for the period, from the timesheet export HES-TS-2425. Hours recorded against LDS tickets are shown as Programme hours. Other hours are recorded against the group's operational tickets, recruitment, training and support work.

| Name | Total hours | Programme hours (LDS) | Other hours | Programme % |
|---|---:|---:|---:|---:|
| Dr Simon Achterberg | 1,640 | 1,558 | 82 | 95% |
| Natasha Grieve | 1,600 | 1,520 | 80 | 95% |
| Imran Qadir | 1,620 | 1,539 | 81 | 95% |
| Bethany Coles | 1,580 | 1,501 | 79 | 95% |
| Luke Fensome | 1,620 | 1,539 | 81 | 95% |

Programme hours by quarter, all five staff combined:

| Quarter | Period | Programme hours |
|---|---|---:|
| Q1 | April to June 2024 | 1,910 |
| Q2 | July to September 2024 | 1,914 |
| Q3 | October to December 2024 | 1,916 |
| Q4 | January to March 2025 | 1,917 |
| **Total** | | **7,657** |

Gavin Holt, Director, is not included in the timesheet extract. His 30% apportionment is an estimate, as described in section 6.3.

### Appendix D: Supplier and invoice list

| Supplier | Reference | Date | Description | Amount (excluding VAT) | Claimed |
|---|---|---|---|---:|---|
| Meridian Lakehouse Ltd | HES-SW-0871 | 30 April 2024 | Annual platform subscription, 1 May 2024 to 30 April 2025 | £52,000 | Yes |
| Veridian Holt Holdings Ltd | HES-OF-0144 | 1 April 2024 | Office occupancy, Suite 4, Calder House (intra-group lease) | £38,400 | No |
| TrakSure Data Ltd | (licence held by Holt Freight Intelligence Ltd) | Not applicable | Telematics position data licence, access provided to the Programme | Not applicable | No |

The Company holds no other supplier invoices relating to the Programme. Staff costs are paid through payroll and are not supplier invoices.

### Appendix E: Intra-group agreements referred to in this claim

| Agreement | Date | Parties | Summary |
|---|---|---|---|
| Intra-group services agreement | 2 April 2024 | Holt Engineering Services Ltd and Holt Freight Intelligence Ltd | Provision of engineering staff and services, recharged at cost plus 15% |
| Lease of Suite 4, Calder House | 1 April 2024 | Veridian Holt Holdings Ltd and Holt Engineering Services Ltd | Office occupancy |

### Appendix F: Director's declaration

I declare that I am a director of Holt Engineering Services Ltd (company number ZZ009958) and that I am authorised to make this declaration on its behalf.

I declare that the information in this claim for research and development relief for the accounting period 1 April 2024 to 31 March 2025, including the Additional Information Form, the technical narrative, the cost schedules and the appendices, is correct and complete to the best of my knowledge and belief.

I declare that the Company has carried out the research and development activities described in this claim, and that the qualifying expenditure claimed was incurred on those activities and is correctly computed under the merged scheme.

I understand that the Company must keep and produce the records supporting this claim, and that HMRC may check the claim.

Name: Gavin Holt
Position: Director
Company: Holt Engineering Services Ltd
Signature: ______________________________
Date: 26 September 2025
