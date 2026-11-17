> SYNTHETIC TEST DATA – FICTIONAL COMPANY – PREPARED FOR HMRC HACKATHON – NOT A REAL TAX CLAIM

## 1. Cover Sheet and Claim Summary

**Claimant:** Holt Freight Intelligence Ltd
**Company number:** ZZ009945
**Unique Taxpayer Reference:** 9999994512
**Registered office:** Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS
**Accounting period:** 1 April 2024 to 31 March 2025
**Scheme claimed:** Merged scheme (profit-making company), 20% expenditure credit, taxable
**Claim prepared by:** Ruth Ansell, Senior Claims Manager, Vantrell Innovation Ltd (agent)
**Senior officer:** Gavin Holt, Director
**Date of claim pack:** 27 March 2026

### Claim summary

Holt Freight Intelligence Ltd (“Holt Freight”, “the company”) operates Holtline, a digital freight marketplace that connects shippers of palletised and full-load consignments with road-haulage capacity across Great Britain. Holtline handles several thousand bookings a week and is the company's principal source of revenue. The company employs 64 people, mostly in operations, customer support and sales, and reported turnover of £22.5 million for the period covered by this claim.

Throughout the accounting period ended 31 March 2025 the company carried out research and development in two linked areas of its marketplace. The principal project, Project Lodestar, concerns demand forecasting for the freight lanes on which Holtline operates. Freight demand is highly uneven. Most origin–destination pairs carry very little volume in any given week, and the company's existing corridor-level forecasts were too coarse to support dynamic pricing or to position capacity ahead of demand. The second project addresses dynamic load-matching, the process by which an open booking is assigned to a suitable vehicle while respecting driver-hours rules, vehicle constraints and service windows.

The company faced technical uncertainties that could not be resolved by applying existing published methods or commercially available forecasting packages. In Project 1 these were: whether a lane-level forecast could be produced with usable accuracy for sparse origin–destination pairs; how forecasts for individual lanes could be made mutually coherent with forecasts at regional and national level; and how a useful forecast could be produced for a shipper with no booking history. The company's advance is a hierarchical reconciliation method for sparse lane-level forecasts, combined with a cold-start procedure for new shippers. Both are described in the technical narrative.

Project 2 extended the company's matching engine to handle a larger set of driver-hours and vehicle constraints in real time. The company's work there is described in the technical narrative, including the configuration of the optimisation solver that the company used to meet its latency targets.

Work on the claim was carried out by the company's own product and engineering teams, supported by a group engineering services arrangement and a group modelling services arrangement, both described in section 4 of this pack. Staff costs, externally provided workers and data and cloud costs are set out in section 6. The claim is made under the merged scheme as a profit-making company, and the company has elected to receive the expenditure credit as a taxable credit.

### Headline figures (as claimed)

| Item | Amount |
|---|---|
| Staff costs (qualifying, as claimed) | £105,189 |
| Other qualifying expenditure (as claimed) | £796,272 |
| Total qualifying expenditure (as claimed) | £901,461 |
| Expenditure credit at 20% (as claimed) | £180,292 |
| Net benefit after 25% corporation tax (as claimed) | £135,219 |

### Projects claimed

| Ref | Project | Main field | Status at end of period |
|---|---|---|---|
| P1 | Project Lodestar: hierarchical, cold-start-capable demand forecasting for sparse freight lanes | Data science, statistical machine learning and time-series forecasting | Forecasting service in production use on Holtline from February 2025 |
| P2 | Dynamic load-matching optimisation for real-time booking assignment | Operational research and combinatorial optimisation | Matching engine release in production from February 2025 |

### Contact for this claim

Ruth Ansell, Senior Claims Manager, Vantrell Innovation Ltd, Unit 3, Quayside Works, Wakefield ZZ2 8PL. Technical queries should be directed to Dr Simon Achterberg, Head of Data Science, who is provided to the company under the group services arrangement described in section 4. Financial queries should be directed to Helen Dray, Financial Controller, Holt Freight Intelligence Ltd, at the registered office above.

---

## 2. Claim Notification Form

The company submitted its Claim Notification Form for the accounting period ended 31 March 2025 before the period end deadline for notification. The form was filed electronically on 24 September 2025 and an acknowledgement was received from HMRC on the same day. A copy of the acknowledgement is held with the evidence index in section 7.

| Field | Entry |
|---|---|
| Company name | Holt Freight Intelligence Ltd |
| Company number | ZZ009945 |
| Unique Taxpayer Reference | 9999994512 |
| Registered office | Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS |
| Accounting period for which notification is given | 1 April 2024 to 31 March 2025 |
| Date notification submitted | 24 September 2025 |
| Submitted by | Ruth Ansell, Vantrell Innovation Ltd, on behalf of the company |
| Company status for the purposes of the scheme | Profit-making company (not a small or medium-sized enterprise for this period) |
| Scheme to be claimed | Merged scheme |
| Projects notified | Project Lodestar (demand forecasting); dynamic load-matching optimisation |
| Date R&D commenced for the notified projects | Lodestar: October 2023 (initial corridor-level investigation). Load-matching: January 2024 |
| Agent for the claim | Vantrell Innovation Ltd |
| Whether the company is a subsidiary of another company | Yes. Wholly owned by Veridian Holt Holdings Ltd (company number ZZ009931) |

### Notes to the notification

The notification identifies two projects. Project Lodestar was started as an investigation into corridor-level forecasting in October 2023, before the start of the accounting period, and its lane-level and hierarchical work began in April 2024. The load-matching work was started in January 2024 as a re-examination of the matching engine's constraint handling, and the company treated it as a separate project from the outset because its objectives, uncertainties and personnel were distinct from the forecasting work.

Staff and other costs were identified on the notification form at the level of the project. Costs are apportioned between the two projects in section 6 of this pack, and no cost has been counted against both projects.

This notification relates to the accounting period ended 31 March 2025 only. The company's earlier claims for the period ended 31 March 2024 were prepared on the same basis, and the Lodestar work described in section 5 continued without interruption from that period into this one.

### Declaration on the notification

The form was completed on behalf of the company by its agent and was approved by Gavin Holt, Director, before submission. The information given on the form is accurate, to the best of the company's knowledge, at the date of submission.

---

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

---

## 4. Company Background, Ownership, Group, Funding, Staff and Facilities

### 4.1 History and business

Holt Freight Intelligence Ltd was incorporated in 2014 as a conventional freight brokerage serving manufacturers and distributors in the North of England. The business was built on relationships: a small operations team matched loads to haulage firms by telephone and spreadsheet, and margins were thin. Between 2016 and 2019 the founders developed an online booking tool that allowed shippers to post loads directly and allowed hauliers to accept them through a web and mobile interface. That tool became Holtline.

Holtline is now a digital freight marketplace. Shippers post consignments, specify pick-up and delivery windows, and receive offers from hauliers registered on the platform. Hauliers are paid through the platform and the company earns a commission on each completed booking. Holtline is used by several hundred shippers and by a larger number of registered hauliers, most of them small and medium-sized road-haulage operators. The company's commercial position depends on the quality of its matching and pricing, and on the reliability of the capacity it can offer shippers at short notice.

The company's turnover for the accounting period ended 31 March 2025 was £22.5 million. Most of this income is commission on completed bookings. The company has been profitable in each of the last four accounting periods and does not carry external borrowing beyond a standard operating facility with its bankers.

### 4.2 Ownership and group structure

The company is wholly owned by Veridian Holt Holdings Ltd (company number ZZ009931). Veridian Holt Holdings Ltd is in turn wholly owned by Gavin Holt, who is the ultimate controlling party of the group. Gavin Holt is a director of Holt Freight Intelligence Ltd and serves as Group Chief Executive for the group. The registered office of the company is shared with the parent undertaking and with the group's other companies at Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS.

The group provides shared services through three intra-group arrangements relevant to this claim:

- **Intra-group services agreement dated 2 April 2024.** Under this agreement Holt Engineering Services Ltd (company number ZZ009958) supplies technical staff to Holt Freight Intelligence Ltd, including data scientists, machine learning engineers, data engineers, optimisation engineers and backend engineers. Staff are supplied at cost plus 15 per cent. Holt Engineering Services Ltd employs the individuals concerned, who work on the company's premises and under the direction of the company's technical leads.
- **Modelling services agreement dated 15 April 2024.** Under this agreement Holt Data Labs Ltd (company number ZZ010277) delivers forecasting model development to Holt Freight Intelligence Ltd for a fixed fee of £210,000. The agreement is described in section 6.
- **Platform licence.** Holtline's core platform is licensed to the company from a group company on terms reviewed annually. The licence fee is recorded in the management accounts and is not part of the claim.

The Azure machine learning subscription under which the company's models are trained and served is held in the company's name. Compute consumed under the modelling services agreement is re-invoiced to Holt Data Labs Ltd, and those recharges are recorded in the group management accounts. The company's cloud costs in this claim are stated gross of those recharges, as described in section 6.

### 4.3 Funding

The company has funded its operations from retained profit. The parent undertaking has made no capital injection since 2019 and the company has not received any grant funding for the work described in this claim. The company has no other tax relief claims outstanding for the period. It has not received any state aid or subsidy for the Lodestar or load-matching work.

The company's board, which consists of Gavin Holt and two non-executive directors, reviews the research budget each year as part of the annual operating plan. The Lodestar programme was approved as part of the operating plan for the year beginning 1 April 2024, with a budget that covered internal staff, provided staff and cloud compute.

### 4.4 Staff

At 31 March 2025 the company employed 64 people. The majority work in operations, customer support and sales, which together account for approximately 48 of the total. The product and engineering function consists of the Product Owner for Lodestar, Priyanka Mehta, and a small team of product managers and front-end developers who work on the Holtline interface. The data science and engineering work described in this claim was carried out by the Product Owner, together with five technical staff provided under the group services arrangement dated 2 April 2024 and by the Group Chief Executive in his role as programme sponsor.

Priyanka Mehta joined the company in 2021 from a logistics software business. She has responsibility for the Lodestar backlog, prioritises the development work for the data science team, and is the company's principal contact for pricing and capacity decisions that depend on the forecasts. Her role is described in more detail in the work log at section 5.5 and in the cost methodology at section 6.

Dr Simon Achterberg joined the company's technical team on 2 April 2024, under the group services arrangement, as Head of Data Science. He is the company's competent professional for this claim. His qualifications and experience are set out in the appendices at section 7.1.

### 4.5 Facilities

The company operates from Suite 4, Calder House, 9 Wharf Approach, Wakefield ZZ1 5RS, which provides office space for the operations, sales and technical teams. The technical team has a dedicated room with a workstation for each member of staff and a secure development environment connected to the company's cloud accounts. The company has no laboratory or manufacturing facility. All work described in this claim was carried out in the office, on the company's cloud environment, or remotely from the homes of staff who were permitted to work remotely under the company's hybrid working policy.

The company's data is held in a managed cloud environment. Telematics data supplied by TrakSure Data Ltd under a licence agreement is stored in the same environment. The licence permits the company to use the data for the purposes of its marketplace, including the development of forecasting and matching models. A copy of the licence is held in the evidence index at section 7.

### 4.6 Relationship with the agent

Vantrell Innovation Ltd has been the company's R&D tax adviser since 2022. The agent prepares the claim on the basis of information supplied by the company's Financial Controller and by its technical leads, and it has no interest in the company other than as adviser. The agent is also an adviser to other businesses. The team working on this claim is separate from those other engagements.

---

## 5. Technical Narrative (Part A): Overview and Project 1, Project Lodestar

### 5.1 Purpose and structure of this narrative

This narrative is the company's full technical report for the accounting period 1 April 2024 to 31 March 2025. It is written for a reviewer with a technical background who is not a specialist in freight marketplaces or in forecasting. It follows the structure of the DSIT guidance on R&D tax relief. For each project it sets out the baseline, the advance sought, the scientific or technological uncertainties, the methodology, a chronological work log with dated iterations, the outcomes, and the boundaries of the project. Section 5.3 covers Project 2. Section 5.4 contains the competent professional statement and section 5.5 the chronological work log for both projects, which are in the file that follows this one.

Holtline is a digital freight marketplace. Shippers post consignments and receive offers from registered hauliers. A booking is a single consignment moved from an origin to a destination, and a lane is the pair of origin and destination zones between which a consignment moves. The marketplace operates on several thousand lanes at any one time, but the volume on most of them is very small. A typical lane sees a handful of bookings in a week, and many see none. Two activities depend on knowing how much demand will arrive on each lane in the coming days and weeks. The first is pricing: the company offers shippers an indicative rate that must reflect expected competition for haulier capacity on the lane. The second is capacity positioning: the company works with hauliers to encourage vehicles to be available on lanes where demand is about to rise. Both activities were, before this project, driven by corridor-level forecasts, meaning forecasts for groups of lanes that share a region pair. Corridor forecasts are too coarse to price a single lane or to position a single vehicle.

The work described here had two aims. The first was to produce forecasts at lane level that were accurate enough to be used in pricing. The second was to produce forecasts that could be combined consistently across the lane, regional and national levels, so that the company's capacity plans at each level agreed with one another. A third requirement emerged during the project. The company onboards new shippers continually, and a new shipper has no booking history. The company needed a forecast for such shippers from the first day of trading.

### 5.2 Project 1: Project Lodestar

#### 5.2.1 Background and origin

Project Lodestar began in October 2023 as an investigation into whether corridor forecasts could be replaced by something more granular. The investigation was carried out by the Product Owner, Priyanka Mehta, with a small group of analysts, and it produced a set of exploratory notebooks and a short internal paper. That work is background to the claim and falls before the accounting period. The formal R&D programme started on 2 April 2024, when the company's technical staff were provided under the group services arrangement and the programme was approved as part of the operating plan.

The Lodestar name is an internal label. The programme is recorded in the company's Jira project under the key LDS. All tickets cited in this narrative carry that key.

#### 5.2.2 Baseline

Before Project Lodestar the company forecast demand at the corridor level. A corridor combined all lanes sharing an origin region and a destination region. Corridor demand was forecast weekly using a seasonal average with an exponential smoothing adjustment. The approach was simple to operate and it was reasonable for planning capacity on the busiest corridors, which accounted for a large share of bookings. It had three known limitations.

The first limitation was granularity. A corridor forecast says nothing about which lanes within the corridor will be busy. Pricing a single lane from a corridor figure therefore relied on an allocation rule, which the company had adopted from practice in the sector without testing it against actual lane-level outcomes.

The second limitation was the treatment of sparse data. Existing forecasting approaches assume dense, stationary demand signals; at lane level fewer than 8% of origin–destination pairs exhibit weekly volume sufficient for conventional models. On Holtline the great majority of lanes fall below that threshold. For those lanes the corridor method was the only available estimate, and its error was not measured separately from the busier corridors.

The third limitation was the absence of any forecast for new shippers. A shipper with no booking history had to be priced using the average of its declared sector, which the company did not regard as reliable.

The baseline is therefore not a published technique but the company's own practice, which was adequate for corridors and inadequate for lanes and new shippers. The company's view, supported by the exploratory work of 2023, was that a lane-level forecast could not be produced by taking the existing corridor model and simply applying it at finer resolution. The sparsity of the data meant that the model would simply fail to fit on most lanes.

#### 5.2.3 Advance sought

The company seeks relief for an advance in the science of demand forecasting for sparse, hierarchical data of the kind found on freight marketplaces. The advance has two linked parts.

The first part is a hierarchical reconciliation method. Individual lane forecasts for sparse lanes are unreliable on their own. The method produces lane forecasts from a set of base models, each of which is fitted at a different level of the hierarchy, and then adjusts the base forecasts so that the lowest-level forecasts sum to the forecasts at each higher level. The company's contribution is a reconciliation procedure that retains the lane-level signal on lanes where the base model is weak, by weighting the reconciliation towards the higher level only where the lane-level forecast has insufficient support. The procedure is set out in full in section 5.2.5 below and in the work log.

The second part is a cold-start procedure for new shippers. A new shipper is represented by a profile vector derived from its declared sector, its declared origin and destination regions, its vehicle requirements and its first few bookings. The procedure finds the existing shippers whose profiles are closest, and forms a forecast for the new shipper from their booking histories, weighted by similarity and shrunk towards the corridor forecast until the shipper has enough bookings to stand on its own. The company's advance lies in the combination of the reconciliation and the profile-based cold-start, which together allow a single coherent set of forecasts to be produced for all lanes, including those with no history.

The company does not claim an advance in the individual model families used as components of the method. Those are described in section 5.2.5 as the tools used, and their use is part of the methodology.

#### 5.2.4 Scientific and technological uncertainties

At the start of the project the company identified the following uncertainties, which could not be resolved by reference to the published literature or to commercial forecasting packages.

**Uncertainty 1: accuracy at lane level.** It was not known whether a lane-level forecast could be produced with an error low enough to support pricing on sparse lanes. The company could find no published benchmark for weekly freight demand at lane level on a marketplace with this sparsity. Commercially available forecasting packages were designed for dense retail and energy data and gave no guidance on the sparse case.

**Uncertainty 2: coherence.** It was not known whether forecasts at lane level could be reconciled to regional and national totals without losing the lane-level signal. Standard reconciliation methods were developed for hierarchies with dense series at the bottom level, and it was unclear whether they would preserve information on sparse lanes or would simply reproduce the higher-level forecast.

**Uncertainty 3: cold start.** It was not known whether a useful forecast could be produced for a new shipper with no history, or at what point such a forecast should be trusted in place of the corridor allocation.

**Uncertainty 4: production feasibility.** It was not known whether the methods could be served within the latency and cost limits of the production pricing service, which must return a rate for a lane in under 300 milliseconds at peak.

These uncertainties were recorded in the programme charter of 2 April 2024 (LDS charter, evidence reference HFI-CH-0002) and were reviewed at each monthly steering meeting.

#### 5.2.5 Methodology

**Data.** The programme drew on three sources. The first was the company's booking history for the period from January 2021 onwards, covering several million consignments. The second was telematics data licensed from TrakSure Data Ltd, comprising approximately 3.2 billion GPS telematics pings from the vehicles of hauliers registered on Holtline during the period. The pings were map-matched to road segments and aggregated to lane-level vehicle movement features, which were used as exogenous signals for demand, for example to indicate vehicles already positioned near an origin zone. The third source was the shipper profile data captured at onboarding. The company's data engineering work to join these sources is set out under LDS-198 (lane-level feature store) and LDS-236 (telematics ingestion and map-matching).

**Base models.** The programme used a set of base forecasting models, each fitted at a different level of the hierarchy. For dense corridors the company used a temporal fusion transformer, a sequence architecture that combines recurrent and attention components and produces quantile forecasts. The model was configured for the corridor and regional levels and developed under LDS-214, titled "Temporal fusion model – lane-level demand". For sparser lanes the company used gradient-boosted decision trees, tuned by a hyper-parameter search over tree depth, learning rate, subsampling and regularisation parameters. A seasonal naive model and the original corridor exponential smoothing model were retained as benchmarks. The temporal fusion model and the gradient-boosted models are established methods, and the company's use of them was to apply them to the company's data with conventional configuration and tuning. That work is recorded in the work log at section 5.5 as configuration work and is not part of the advance.

**Hierarchical reconciliation.** The reconciliation method is the core of the advance. The company's hierarchy has three levels: national, regional corridor, and lane. The base forecasts at each level are combined by a reconciliation matrix, derived from the summing structure of the hierarchy. The company's innovation lies in the treatment of the lane level, where the base forecasts are unreliable. For each sparse lane the procedure estimates the reliability of the base forecast from its backtest error and from the number of non-zero weeks in the lane's history. Where reliability is low the reconciled forecast is pulled towards the corridor forecast, and where reliability is high the lane signal is kept. The weighting is recomputed each week so that a lane that becomes busier moves from the corridor-anchored regime to the lane-signal regime without a discontinuity in its forecast. The method is specified under LDS-502, titled "Hierarchical reconciliation of forecasts".

**Cold-start procedure.** For a new shipper the procedure forms a profile vector from the declared attributes and the first bookings. The profile vector is compared with the profiles of established shippers using a weighted distance, and the k nearest shippers are selected. Their booking histories on the new shipper's declared lanes are averaged, weighted by similarity. The resulting forecast is shrunk towards the corridor forecast, with the shrinkage factor declining as the new shipper's own history grows. The procedure is specified under LDS-377, titled "Cold-start for new shippers". The selection of k, the distance weights and the shrinkage schedule were determined by the backtesting described below.

**Backtesting.** Every candidate model and every version of the reconciliation was evaluated with a rolling-origin backtest. The company built a backtesting harness under LDS-289, which trains each model on data up to a given week and forecasts the following four weeks, then rolls the origin forward. Accuracy was measured by mean absolute scaled error for dense corridors and by a scaled error that is defined for zero-volume weeks for sparse lanes. Probabilistic accuracy was measured by pinball loss at the 10th, 50th and 90th percentiles, and the outputs were calibrated using a conformal adjustment under LDS-331.

**Serving.** The chosen forecasting service runs as an inference endpoint on the company's Azure machine learning workspace. The endpoint receives lane identifiers and returns quantile forecasts, which the pricing service reads. The endpoint was hardened under LDS-446 and was placed in front of the production pricing service in February 2025 under LDS-408, titled "Forecast serving for Holtline pricing".

#### 5.2.6 Outcomes

The principal outcome of Project Lodestar is a forecasting service that produces a coherent set of forecasts for every lane on Holtline, including lanes with sparse history and shippers with no history. On the held-out backtest for the period October and November 2024, the reconciled lane-level forecasts reduced the scaled error on sparse lanes by roughly a third compared with the corridor allocation. On the cold-start backtest, forecasts for shippers in their first four weeks were materially more accurate than the sector average they had previously used. These results are recorded in the backtest reports held in the evidence index.

The company does not claim that the forecasts are accurate in every case. Sparse lanes remain difficult, and the company's pricing rules treat forecasts for lanes with very few bookings with a wider band. The outcome that the company claims is that a usable and coherent forecast now exists where none existed, and that this could not have been produced by the company's existing methods or by a commercially available package.

#### 5.2.7 Boundaries of Project 1

Project 1 started on 2 April 2024 for the purposes of this claim, with the formal programme and the provision of technical staff under the group services arrangement. Its origin in the 2023 investigation is recorded as background. The project ended for the purposes of this claim on 31 March 2025, when the forecasting service had been in production for two months and the programme moved to a maintenance and retraining footing. Work on the production service after 31 March 2025 is not included in the claim.

---

### 5.3 Project 2: Dynamic load-matching optimisation

#### 5.3.1 Background

The matching engine is the part of Holtline that assigns each open booking to a haulier's vehicle. When a shipper posts a consignment, the engine considers the vehicles available on or near the origin, checks each candidate against the vehicle's type and capacity, the driver's remaining hours under the drivers' hours rules, the service window requested by the shipper, and the haulier's own preferences, and then makes an offer. Bookings arrive unevenly through the day and the week. Peak volumes on a Monday morning can be several times the average, and the assignment has to be made while the shipper is still waiting for a price.

The matching engine was first built in 2017. It used a greedy algorithm that assigned each booking to the nearest suitable vehicle in turn. The greedy approach was reliable at moderate volumes and it was simple to maintain. It was not designed to consider several bookings together, so that a sequence of assignments could leave a driver with an unusable remaining window, or leave a vehicle positioned poorly for the next booking that was about to arrive. In peak periods these effects accumulated. Operations staff reported that some assignments were poor choices in hindsight, and the company's own measure of assignment quality, the proportion of bookings that were completed without re-assignment, fell at peak.

The company's Product Owner for Lodestar, Priyanka Mehta, and the Group Chief Executive identified the matching engine as a second R&D area in January 2024. The work was started as a re-examination of the constraint handling, and it was treated as a separate project from the forecasting work because its objectives, uncertainties and technical staff were distinct.

#### 5.3.2 Baseline

The baseline for Project 2 is the company's greedy matching engine as operated from 2017 to 2024. The engine had no formal treatment of multi-leg driver-hours rules. Those rules were applied as a filter after the candidate set was formed, so that a vehicle was rejected if the next leg would exceed the driver's remaining hours. This meant that the engine could not look ahead, and the company had no means of measuring how much assignment quality was lost by the lack of look-ahead.

Industry practice is to treat assignment of loads as a static problem. Most operators solve the assignment overnight for the following day, using a batch optimisation over the expected bookings, and then adjust by hand during the day. That practice is known to the company from its own experience of the sector and from published operational research on vehicle routing. Holtline required assignment within two seconds of a booking being posted, against a set of bookings that was not known in advance. The static batch approach was therefore not available to the company.

The company regarded real-time, constraint-aware assignment under driver-hours rules as an area where the published methods did not directly apply. Published vehicle routing and assignment methods assume a known set of requests, and the static treatment of driver-hours rules in those methods is not designed for the case of a booking arriving while the solver is already running.

#### 5.3.3 Advance sought

The company seeks relief for an advance in the real-time assignment of loads subject to driver-hours and vehicle constraints. The advance is a constraint formulation that represents multi-leg driver-hours rules inside the assignment problem rather than as a filter, combined with a solver configuration that meets a latency target of under two seconds at peak volume. The company's claimed contribution is the formulation and the demonstration that the configured solver meets the target on the company's own peak data. The company does not claim to have invented the mixed-integer solver used, which is a commercially available package, or the general technique of formulating assignment as an integer programme.

#### 5.3.4 Scientific and technological uncertainties

**Uncertainty 1: feasibility at peak.** It was not known whether a formulation that represents multi-leg driver-hours rules inside the assignment problem could be solved within two seconds at peak volume. Formulations of this kind had been solved only for static batch problems of modest size in the published literature.

**Uncertainty 2: robustness.** It was not known whether a single solver configuration could be made robust to the variation in booking volume across the week, given that the structure of the problem changes markedly between a quiet Sunday evening and a peak Monday morning.

**Uncertainty 3: acceptance.** It was not known whether assignments produced by a constraint-aware solver would be accepted by operations staff, who had built their working practice around the greedy engine's behaviour.

These uncertainties were recorded in the Project 2 charter under the LDS key and were reviewed at the monthly steering meeting alongside Project 1.

#### 5.3.5 Methodology

**Formulation.** The assignment problem is formulated as a mixed-integer programme in which binary variables indicate whether a booking is assigned to a vehicle at a given position in the vehicle's sequence. The objective combines the expected cost of the assignment, a penalty for positioning a vehicle away from its next likely booking, and a penalty for any driver-hours slack that is consumed unnecessarily. The constraints represent vehicle capacity, service windows, and the drivers' hours rules across each leg of the sequence. The multi-leg driver-hours constraints were the company's main modelling effort. They were written so that the solver could enforce the rules across a sequence of up to four legs, with a fallback to the filter for longer sequences. The formulation work was carried out under LDS-398, titled "Load-matching formulation", and refined under LDS-433, titled "Driver-hours constraint handling".

**Solver configuration.** The formulation was solved with a commercially available mixed-integer solver. The company's configuration work was a parameter sweep over the solver's branching, cut generation, presolve and time-limit settings, together with the choice of warm-start strategy when a new booking arrived during a running solve. The sweep was run against recorded peak-period booking data and recorded the time to a feasible solution and the quality of the solution at the time limit. The sweep is recorded under LDS-421, titled "Solver configuration sweep", and the company's selected configuration was used in all subsequent benchmarks. Solver configuration of this kind is standard practice for the package and is described in the company's work log as configuration work.

**Latency benchmarking.** The benchmarks were run on a recorded week of peak data and on a set of synthetic peak weeks generated from the booking distribution. Benchmark results are held in the evidence index. The latency target was the 95th percentile time to offer under two seconds. The benchmarks were repeated after each change to the formulation, which is recorded under LDS-477, titled "Matcher latency benchmarks".

**Shadow running.** Before release the new matcher was run in shadow alongside the greedy engine for two weeks. Its assignments were recorded but not offered to hauliers, and operations staff reviewed a sample of assignments where the two engines disagreed. This addressed uncertainty 3 and is recorded under LDS-523, titled "Matcher production release".

#### 5.3.6 Outcomes

The matcher was released to production in February 2025 under LDS-523, following the shadow period. On the company's recorded peak week, the 95th percentile time to offer was within the two-second target, and the proportion of bookings completed without re-assignment at peak rose compared with the greedy engine over the same weeks. Operations staff accepted the majority of the constraint-aware assignments in the shadow review. Post-release tuning under LDS-611 continued into March 2025 and is recorded in the work log.

The outcome that the company claims is a working real-time matcher that enforces multi-leg driver-hours rules inside the assignment, meets the latency target at peak, and was accepted by operations for production use. The company's view is that this outcome was not achievable by applying the greedy engine's rules or by adopting the overnight batch approach used elsewhere in the sector.

#### 5.3.7 Boundaries of Project 2

Project 2 started on 1 January 2024, when the constraint-handling re-examination began, and the formulation and benchmarking work continued throughout the accounting period. The project ended for the purposes of this claim on 31 March 2025. The company's subsequent work on the matcher is part of normal operation and is not claimed.

---

### 5.4 Competent professional statement

I, Dr Simon Achterberg, Head of Data Science at Holt Freight Intelligence Ltd, provided to the company under the intra-group services agreement dated 2 April 2024, confirm that I have the knowledge, experience and ability of a competent professional in data science, machine learning and statistical forecasting, and that I have led the technical work on Project Lodestar and on the forecasting elements of the claim throughout the accounting period.

I hold a PhD in computational statistics and an MSc in machine learning. Before joining the company I spent eight years in applied forecasting roles, first in a consultancy providing demand models to retail and energy clients and latterly as a principal data scientist at a logistics software business. I have published on hierarchical forecasting for sparse count data and I have reviewed submissions to two international conferences on time-series methods. I am therefore familiar with the published state of the art in forecasting, including the methods that were considered and rejected for this project.

In my professional judgement the uncertainties described in section 5.2.4 could not have been resolved by a competent professional working with the published methods and commercially available tools available at the start of the project. The reconciliation and cold-start methods described in section 5.2.5 were developed by the programme team under my direction, and I was responsible for the backtesting design, the acceptance criteria and the decisions to adopt or reject each candidate method. I confirm that the descriptions in this narrative of what was known, what was attempted and what was learned are accurate to the best of my knowledge, and that the dated work log in section 5.5 reflects the iterations recorded in the programme's notebooks and tickets.

The Lodestar programme was delivered by a team of five technical staff, who were provided under the same arrangement, together with the Product Owner. I am satisfied that the time recorded for each individual reflects the work actually undertaken, and I have reviewed the allocation of time between the forecasting and load-matching work with the Product Owner and the Group Chief Executive.

Signed: Dr Simon Achterberg
Date: 26 March 2026

### 5.5 Chronological work log

The work log records the dated iterations of both projects within the accounting period. Dates are the dates on which the work was recorded in the programme's notebooks, tickets or commits. Evidence references are given in the evidence index at section 7.2. Routine configuration and tuning activity is recorded as such.

#### 5.5.1 Project 1: Project Lodestar

| Date | Ticket | Activity | Outcome | Evidence |
|---|---|---|---|---|
| 2 Apr 2024 | LDS-101 | Programme charter approved; technical staff provided under the group services arrangement | Uncertainties 1 to 4 recorded | HFI-CH-0002 |
| 9 Apr 2024 | LDS-198 | Lane-level feature store designed and populated from booking history | Feature store operational for 4,100 active lanes | HFI-LB-0088 |
| 15 Apr 2024 | n/a | Modelling services agreement signed with Holt Data Labs Ltd | Forecasting model development delivered under agreement | HFI-CON-0031 |
| 16 Apr 2024 | LDS-236 | Ingestion of TrakSure telematics extract, first tranche (1.1 bn pings) | Map-matching to road segments, initial error rate measured | HFI-LB-0097 |
| 6 May 2024 | LDS-214 | First temporal fusion model fitted on corridor data, configuration as published | Corridor-level accuracy comparable to benchmark; lane-level fit failed on 91% of sparse lanes | HFI-LB-0112 |
| 13 May 2024 | LDS-214 | Second run with reduced input window and attention masking for zero-volume weeks | Lane-level fit still failed on most sparse lanes; dense corridors improved | HFI-LB-0118 |
| 27 May 2024 | LDS-214 | Gradient-boosted trees fitted to sparse lanes as an alternative base model | Usable fit on 38% of sparse lanes | HFI-LB-0124 |
| 10 Jun 2024 | LDS-289 | Rolling-origin backtesting harness built | Harness reproduces benchmark results for corridor model | HFI-LB-0139 |
| 24 Jun 2024 | LDS-214 | Hyper-parameter search for gradient-boosted base model (routine tuning, 412 configurations) | Best configuration selected by backtest pinball loss | HFI-LB-0151 |
| 8 Jul 2024 | LDS-289 | First full backtest of candidate base models across all lanes | Sparse-lane error recorded for each candidate; benchmark established | HFI-LB-0163 |
| 22 Jul 2024 | LDS-331 | Quantile output calibration tested with conformal adjustment | Coverage of 80% interval improved from 0.61 to 0.78 | HFI-LB-0177 |
| 12 Aug 2024 | LDS-377 | Cold-start approach designed: profile vectors from declared attributes and first bookings | Profile features defined; k-nearest shipper selection specified | HFI-LB-0219 |
| 26 Aug 2024 | LDS-377 | Cold-start procedure implemented and first backtest on new shippers | First-four-week error on new shippers below sector average on 3 of 5 test cohorts | HFI-LB-0236 |
| 9 Sep 2024 | LDS-377 | Shrinkage schedule tuned; k and distance weights varied | Schedule adopted; cold-start error reduced in all cohorts | HFI-LB-0258 |
| 23 Sep 2024 | LDS-502 | Hierarchical reconciliation first design: lane forecasts summed to corridor and regional totals | Reconciliation collapsed sparse lanes onto corridor forecast; signal lost | HFI-LB-0281 |
| 7 Oct 2024 | LDS-502 | Reliability-weighted reconciliation designed; weighting from backtest error and non-zero week count | Lane signal retained on lanes with sufficient support | HFI-LB-0297 |
| 14 Oct 2024 | LDS-502 | Reconciliation matrix derived from summing structure; weighting function tested on corridor-lane hierarchy | Coherence held across three levels in test; sparse-lane error reduced | HFI-LB-0412 |
| 28 Oct 2024 | LDS-502 | Week-to-week regime switching tested for lanes moving between sparse and dense states | Discontinuity observed at regime change; smoothing added | HFI-LB-0431 |
| 18 Nov 2024 | LDS-502 | Smoothing adjustment revised; coherence re-verified across all weeks in backtest | Discontinuity removed; coherence exact to rounding | HFI-LB-0459 |
| 2 Dec 2024 | LDS-502 | Full backtest of reconciled forecasts, October to November 2024 holdout | Sparse-lane scaled error reduced by approximately one third against corridor allocation | HFI-LB-0478 |
| 13 Dec 2024 | LDS-214 | Routine retraining of temporal fusion model on extended data (configuration only) | No change in accuracy; retained for dense corridors | HFI-LB-0484 |
| 9 Jan 2025 | LDS-408 | Integration with pricing service specified; latency budget set at 300 ms | Serving architecture chosen: endpoint on Azure machine learning workspace | HFI-LB-0501 |
| 23 Jan 2025 | LDS-446 | Inference endpoint hardened: input validation, rate limits, fallback to corridor forecast | Fallback exercised in load test without failure | HFI-LB-0515 |
| 6 Feb 2025 | LDS-408 | Forecasting service placed in front of production pricing for a controlled share of lanes | Live pricing on lanes covered by the service from this date | HFI-LB-0527 |
| 20 Feb 2025 | LDS-408 | Share of lanes served by forecasting service increased to full sparse-lane coverage | Latency within budget at peak | HFI-LB-0536 |
| 13 Mar 2025 | LDS-471 | Retraining schedule set for production models; monitoring for drift added under LDS-560 | Schedule adopted for the post-period maintenance footing | HFI-LB-0548 |
| 31 Mar 2025 | LDS-471 | Close-out of Project 1 for the accounting period | Forecasting service in production; maintenance transferred | HFI-LB-0560 |

#### 5.5.2 Project 2: Dynamic load-matching optimisation

| Date | Ticket | Activity | Outcome | Evidence |
|---|---|---|---|---|
| 8 Jan 2024 | LDS-398 | Re-examination of greedy matching engine constraint handling begun | Baseline assignment quality measured from 2024 peak data | HFI-LB-0021 |
| 5 Apr 2024 | LDS-398 | Mixed-integer formulation of single-leg assignment with capacity and service windows | Single-leg formulation solves within limits at off-peak volume | HFI-LB-0103 |
| 19 Apr 2024 | LDS-398 | Driver-hours constraints added as filter after assignment, for comparison | Filter leaves unusable remaining windows in 17% of peak assignments | HFI-LB-0109 |
| 17 May 2024 | LDS-433 | Multi-leg driver-hours constraints written into the formulation, up to four legs | Formulation feasible; solve time at peak above target | HFI-LB-0129 |
| 7 Jun 2024 | LDS-421 | Solver configuration sweep begun: branching, cuts, presolve and time limit | First configuration reaches feasible solutions in under two seconds on off-peak data | HFI-LB-0142 |
| 21 Jun 2024 | LDS-421 | Parameter sweep on recorded peak data (routine configuration, 96 settings) | Settings narrowed to 7 candidates | HFI-LB-0155 |
| 12 Jul 2024 | LDS-433 | Warm-start strategy for bookings arriving during a running solve | Warm start reduces time to feasible solution by roughly half | HFI-LB-0168 |
| 2 Aug 2024 | LDS-421 | Candidate configurations benchmarked on synthetic peak weeks | One configuration meets the 95th percentile target on 5 of 6 synthetic weeks | HFI-LB-0183 |
| 23 Aug 2024 | LDS-477 | Latency benchmark harness built and first recorded-week run | Recorded peak week at 2.6 seconds at 95th percentile | HFI-LB-0205 |
| 13 Sep 2024 | LDS-433 | Driver-hours formulation revised to reduce constraint count | Solve time reduced; formulation adopted | HFI-LB-0226 |
| 4 Oct 2024 | LDS-477 | Benchmark repeated on recorded week after formulation change | 95th percentile at 1.9 seconds | HFI-LB-0244 |
| 25 Oct 2024 | LDS-477 | Benchmark on Monday peak weeks, November to January | Target met on all recorded weeks | HFI-LB-0266 |
| 15 Nov 2024 | LDS-523 | Shadow-running configuration agreed with operations | Two-week shadow period scheduled | HFI-LB-0289 |
| 3 Dec 2024 | LDS-523 | Shadow run begun alongside greedy engine; disagreements logged | Operations review of 240 disagreeing assignments commenced | HFI-LB-0302 |
| 17 Dec 2024 | LDS-523 | Operations review of shadow disagreements completed | Constraint-aware assignment preferred in 71% of reviewed cases | HFI-LB-0318 |
| 14 Jan 2025 | LDS-611 | Post-shadow tuning of time limit and warm-start parameters | Routine tuning; no change to formulation | HFI-LB-0334 |
| 4 Feb 2025 | LDS-523 | Matcher production release approved by operations and the Group Chief Executive | Release to production on 11 February 2025 | HFI-LB-0355 |
| 18 Feb 2025 | LDS-611 | First fortnight in production reviewed; re-assignment rate at peak measured | Re-assignment at peak below greedy engine's rate for the same weeks | HFI-LB-0371 |
| 11 Mar 2025 | LDS-611 | Solver time-limit adjusted for weekend volume (configuration only) | No change in assignment quality recorded | HFI-LB-0389 |
| 31 Mar 2025 | LDS-611 | Close-out of Project 2 for the accounting period | Matcher in production; maintenance transferred | HFI-LB-0402 |

#### 5.5.3 Notes to the work log

The work log records the iterations that the programme team regarded as material. Notebook entries not listed here were either exploratory, duplicated an entry already recorded, or were configuration activity of the kind described as routine in the body of this narrative. The routine items in the log are the hyper-parameter search of 24 June 2024, the retraining of 13 December 2024, the solver sweep of 21 June 2024, the post-shadow tuning of 14 January 2025 and the time-limit adjustment of 11 March 2025. These items are included for completeness and are described in the body of the narrative as applications of established methods to the company's data.

---

## 6. Cost Methodology and Schedules

### 6.1 Basis of preparation

This section sets out the qualifying expenditure claimed for the accounting period 1 April 2024 to 31 March 2025 and explains how each figure was derived. The schedules below are the company's cost schedules as claimed. All figures are in pounds sterling. Employer National Insurance contributions are stated on the 2024-25 basis. Staff costs are shown as salary, employer National Insurance and employer pension contributions, and the proportion of the total claimed is the R&D percentage shown for each individual.

The company's finance function prepares the cost schedules from the payroll ledger, the purchase ledger and the group management accounts. The R&D percentages were agreed between the Financial Controller, the Product Owner and the Group Chief Executive, and each percentage is supported by the evidence described in section 6.3.

### 6.2 Schedules

#### Staff costs

Period: 1 Apr 2024 – 31 Mar 2025  ·  NIC basis: 2024-25  ·  Scheme claimed: **merged-profit**

| Name | Role | Salary | Er NIC | Er pension | Total | R&D % | Claimed | Includes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Gavin Holt | Director | £140,000 | £18,064 | £7,000 | £165,064 | 30% | £49,519 |  |
| Priyanka Mehta | Product Owner, Lodestar | £68,000 | £8,128 | £3,400 | £79,528 | 70% | £55,670 |  |
| **Total staff** | | | | | | | **£105,189** | |

#### Other qualifying expenditure

| Category | Description | Claimed |
|---|---|---:|
| EPW (connected) | Holt Engineering Services Ltd – Lodestar engineering staff recharge (5 FTE) | £498,272 |
| Subcontract (connected) | Holt Data Labs – 'forecasting model development' £210,000 | £210,000 |
| Data & cloud | Azure ML compute & telematics dataset licence | £88,000 |
| **Total other** | | **£796,272** |

#### Total qualifying expenditure

**Total qualifying expenditure (as claimed): £901,461**

#### Relief computation

**Relief computation (as claimed) – 20% expenditure credit (taxable); net ~15% at 25% CT**

- credit: £180,292
- net: £135,219
- company turnover for context: £22,500,000

### 6.3 Methodology: staff costs

**Priyanka Mehta.** Ms Mehta is the Product Owner for Lodestar and has been employed by the company since 2021. Her R&D proportion of 70% was calculated from the time she recorded against Lodestar tickets in the company's Jira project under the LDS key during the period. Her logged time was compared with her contracted hours and with the time recorded in the company's timesheet system for non-project activity such as line management, operational meetings and sales support. Her time on the Lodestar backlog, on the design and review of the forecasting and reconciliation work, and on the backtest reviews was treated as R&D. Her time on the Holtline interface, on customer support escalations and on commercial reporting was excluded. The timesheet extract for the period is at section 7.3. The 70% figure has been reviewed against the Jira record for each quarter, and the quarterly proportions do not vary materially from the annual figure.

**Gavin Holt.** Mr Holt is the Group Chief Executive and a director of the company. He is the senior officer for R&D and the sponsor of both projects. His R&D proportion of 30% was estimated rather than recorded in timesheets, because executives in the company do not complete timesheets. The estimate was derived from three sources. The first was a structured interview with Mr Holt conducted by the agent in November 2025, in which he described the time he spent on programme reviews, the approval of research direction, the review of technical risk, and the sign-off of the operating plan budget for the programme. The second was a review of his calendar for the period, which was classified by meeting subject into R&D and non-R&D activity, with the R&D classification confirmed by the Product Owner for a sample of meetings. The third was the minutes of the monthly steering meetings for both projects, which record his attendance and contributions. On the basis of these sources the company estimates that approximately 30% of his working time was spent on the R&D projects. The company is aware that this is an estimate and has retained the calendar extract and the interview notes as evidence.

**Staff costs in total.** The total of the two individual claims is £105,189. Each individual's claimed cost is the salary, employer National Insurance and employer pension contribution multiplied by the R&D percentage, rounded to the nearest pound.

### 6.4 Methodology: externally provided workers

The company's technical staff for Project Lodestar and for the load-matching work were provided by Holt Engineering Services Ltd under the intra-group services agreement dated 2 April 2024. The agreement provides that staff are supplied at cost plus 15 per cent, and that the company is invoiced monthly for the staff provided, with each invoice showing the individuals, their roles and the number of days worked.

Five individuals were provided under the agreement in the period: Dr Simon Achterberg, Natasha Grieve, Imran Qadir, Bethany Coles and Luke Fensome. The company has claimed the monthly recharge for these individuals in full. The company's view is that each of the five was engaged on Lodestar throughout the period, and that their work was therefore wholly within the R&D programme. The annual recharge, including the 15 per cent margin, is £498,272. The invoices are held in the evidence index at section 7.4.

The company regards the recharge as an arm's-length charge for the purposes of the connected-party rules. The cost plus 15 per cent basis was set by the group finance function on the advice of an external accountant at the time the agreement was signed, and it is applied uniformly to all staff provided within the group.

### 6.5 Methodology: subcontracted R&D

The company engaged Holt Data Labs Ltd under a modelling services agreement dated 15 April 2024. The agreement provides for the delivery of forecasting model development to the company for a fixed fee of £210,000. Under the agreement Holt Data Labs Ltd was to deliver model development for the Lodestar forecasting service, and the company has treated the whole of the fixed fee as a subcontracted R&D cost, since the development work was carried out for the purposes of Project 1.

The fee was paid in instalments against the milestones in the agreement. The milestones and the associated deliverables are described in the work log at section 5.5 and in the evidence index. The company has treated the fee as connected-party expenditure and has disclosed it as such in the Additional Information Form, where it appears in the cost totals at section 3.6. Holt Data Labs Ltd is a company within the same group. The fixed fee was agreed by the directors of both companies on the basis of the expected development effort, and it was reviewed against the milestones before each instalment was paid.

### 6.6 Methodology: data and cloud

The data and cloud category comprises two elements. The first is the cost of the company's Azure machine learning compute for the period, which includes model training runs, hyper-parameter searches, backtests and the inference endpoint that serves the Lodestar forecasts to the production pricing service. The second is the annual licence fee for the telematics dataset supplied by TrakSure Data Ltd, comprising approximately 3.2 billion GPS telematics pings from hauliers registered on Holtline over the relevant period.

The Azure machine learning subscription is held in the company's name. Compute consumed under the modelling services agreement is re-invoiced to Holt Data Labs Ltd, and those recharges are recorded in the group management accounts. The data and cloud figure in the schedule is the gross cost of the subscription and the licence for the period, before any recharge. The company's position is that the recharge is a matter of group allocation and does not change the cost incurred by the company on the R&D work.

The company has claimed the full cost of the inference endpoint on the basis that the endpoint serves the Lodestar forecasts, which are the output of the R&D programme, and that the cost of running the forecasts in production is an integral part of the cost of developing them. Compute costs have been taken from the Azure billing export, and the telematics licence cost from the TrakSure invoice. Both are in the evidence index.

### 6.7 Methodology: Project 2 costs

Project 2, the load-matching work, shares its staff with Project 1. The Group Chief Executive's 30% covers his time on both projects, and the provided staff recharged under the agreement dated 2 April 2024 are recorded in section 3.9 as working on Lodestar. The company has not split the staff costs in section 6.2 between the two projects, because the same individuals and the same management time contributed to both. The solver licence used for the matching work is part of the company's general software estate and is not claimed.

### 6.8 Relief computation

The company has claimed the expenditure credit under the merged scheme. Total qualifying expenditure as claimed is £901,461. The expenditure credit at 20 per cent is £180,292, and the net benefit after tax at the 25 per cent main rate of corporation tax, which is the rate applicable to the company for the period, is £135,219. The credit is taxable and is included in the company's corporation tax computation for the accounting period.

The company's turnover for the period was £22.5 million. The R&D claim is set against the company's profits for the period, and the company's tax return and computations are held separately from this pack.

### 6.9 Reconciliation to the financial statements

The qualifying expenditure in this section has been reconciled to the company's management accounts for the period. The staff costs reconcile to the payroll journal. The externally provided workers and the subcontract reconcile to the intra-group recharge schedule, and the data and cloud costs reconcile to the purchase ledger and the Azure billing export. Reconciliations are held with the evidence index at section 7.4.

---

## 7. Appendices

### 7.1 Competent professional: curriculum vitae

**Dr Simon Achterberg**
Head of Data Science, Holt Engineering Services Ltd (provided to Holt Freight Intelligence Ltd under the intra-group services agreement dated 2 April 2024)

**Qualifications**
- PhD, computational statistics. Thesis on hierarchical state-space models for count data with sparse observations.
- MSc, machine learning. Distinction.
- BSc (Hons), mathematics and statistics.

**Professional experience**
- *Head of Data Science*, Holt Engineering Services Ltd, April 2024 to date. Leads the group's data science practice and the provision of data science staff to group companies. Technical lead on the Project Lodestar forecasting work for Holt Freight Intelligence Ltd during the period 1 April 2024 to 31 March 2025.
- *Principal Data Scientist*, Calderbeck Logistics Software Ltd, 2019 to 2024. Led the demand forecasting team for a freight software provider, responsible for forecasting models used by eleven haulage customers. Designed the backtesting framework used across the company's products.
- *Senior Data Scientist*, Marrowgate Analytics Ltd, 2016 to 2019. Forecasting and optimisation consultancy for retail and energy clients. Delivered demand models for multi-site retail chains and for half-hourly electricity demand.
- *Research Fellow*, university statistics department, 2013 to 2016. Research on hierarchical time-series methods.

**Publications and professional activity**
- Achterberg, S. (2018). Hierarchical reconciliation for sparse count series. Peer-reviewed journal article on coherent forecasting where most series are intermittent.
- Achterberg, S., and co-authors (2021). Probabilistic forecasting with conformal calibration for logistics demand. Conference paper.
- Reviewer for two international conferences on time-series methods, 2020 to date.

**Relevant experience for this claim**
Dr Achterberg has worked on the reconciliation of forecasts across hierarchies with intermittent series since 2016, and has published on the subject. He led the design of the backtesting approach and the acceptance criteria for the Lodestar programme, and he approved the adoption or rejection of each candidate method recorded in the work log at section 5.5.

### 7.2 Evidence index

The evidence index lists the principal documents held by the company and by the agent in support of the claim. Documents are held electronically and are available to HMRC on request. Lab book references are to the programme's notebook pages, which are held as dated exports from the notebook system.

| Document ID | Date | Description |
|---|---|---|
| HFI-CH-0002 | 2 Apr 2024 | Project Lodestar programme charter, including recorded uncertainties 1 to 4 |
| HFI-CH-0003 | 12 Jun 2024 | Project 2 charter (load-matching), recorded uncertainties 1 to 3 |
| HFI-CON-0008 | 2 Apr 2024 | Intra-group services agreement, Holt Engineering Services Ltd and Holt Freight Intelligence Ltd, cost plus 15 per cent |
| HFI-CON-0031 | 15 Apr 2024 | Modelling services agreement, Holt Data Labs Ltd and Holt Freight Intelligence Ltd, fixed fee £210,000 |
| HFI-CON-0019 | 28 Mar 2024 | Telematics data licence, TrakSure Data Ltd, approximately 3.2 billion pings |
| HFI-BILL-0001 | 1 Apr 2024 to 31 Mar 2025 | Azure machine learning billing export, monthly, including inference endpoint |
| HFI-LB-0021 | 8 Jan 2024 | Engineering notebook, greedy matching engine baseline measurement |
| HFI-LB-0088 | 9 Apr 2024 | Engineering notebook, lane-level feature store |
| HFI-LB-0097 | 16 Apr 2024 | Engineering notebook, telematics map-matching, first tranche |
| HFI-LB-0112 | 6 May 2024 | Engineering notebook, first temporal fusion model run on corridor data |
| HFI-LB-0118 | 13 May 2024 | Engineering notebook, second temporal fusion run with attention masking |
| HFI-LB-0124 | 27 May 2024 | Engineering notebook, gradient-boosted base model on sparse lanes |
| HFI-LB-0139 | 10 Jun 2024 | Engineering notebook, backtesting harness build |
| HFI-LB-0151 | 24 Jun 2024 | Engineering notebook, hyper-parameter search (routine) |
| HFI-LB-0163 | 8 Jul 2024 | Backtest report, candidate base models across all lanes |
| HFI-LB-0177 | 22 Jul 2024 | Engineering notebook, conformal calibration |
| HFI-LB-0219 | 12 Aug 2024 | Engineering notebook, cold-start design |
| HFI-LB-0236 | 26 Aug 2024 | Backtest report, cold-start on new shipper cohorts |
| HFI-LB-0258 | 9 Sep 2024 | Engineering notebook, shrinkage schedule |
| HFI-LB-0281 | 23 Sep 2024 | Engineering notebook, first reconciliation design |
| HFI-LB-0297 | 7 Oct 2024 | Engineering notebook, reliability-weighted reconciliation |
| HFI-LB-0412 | 14 Oct 2024 | Engineering notebook, reconciliation matrix and summing structure |
| HFI-LB-0431 | 28 Oct 2024 | Engineering notebook, regime switching and smoothing |
| HFI-LB-0459 | 18 Nov 2024 | Engineering notebook, coherence verification |
| HFI-LB-0478 | 2 Dec 2024 | Backtest report, reconciled forecasts, October and November 2024 holdout |
| HFI-LB-0501 | 9 Jan 2025 | Engineering notebook, pricing integration and latency budget |
| HFI-LB-0515 | 23 Jan 2025 | Load test report, inference endpoint hardening |
| HFI-LB-0527 | 6 Feb 2025 | Release note, forecasting service live for controlled share of lanes |
| HFI-LB-0103 | 5 Apr 2024 | Engineering notebook, single-leg assignment formulation |
| HFI-LB-0129 | 17 May 2024 | Engineering notebook, multi-leg driver-hours formulation |
| HFI-LB-0155 | 21 Jun 2024 | Solver sweep report, recorded peak data (routine) |
| HFI-LB-0205 | 23 Aug 2024 | Latency benchmark report, recorded peak week |
| HFI-LB-0266 | 25 Oct 2024 | Latency benchmark report, Monday peak weeks |
| HFI-LB-0302 | 3 Dec 2024 | Shadow-run log, greedy engine and constraint-aware matcher |
| HFI-LB-0318 | 17 Dec 2024 | Operations review of shadow disagreements |
| HFI-LB-0355 | 4 Feb 2025 | Production release approval, matcher |
| HFI-LB-0402 | 31 Mar 2025 | Project 2 close-out note |
| HFI-INT-0001 | 14 Nov 2025 | Interview notes, Group Chief Executive, time apportionment |
| HFI-CAL-0001 | 1 Apr 2024 to 31 Mar 2025 | Calendar extract, classified by subject |
| HFI-MIN-0001 | Apr 2024 to Mar 2025 | Steering committee minutes, both projects (monthly) |
| HFI-JIRA-0001 | 1 Apr 2024 to 31 Mar 2025 | Jira export, LDS project, time recorded by ticket |
| HFI-CNF-0001 | 24 Sep 2025 | Claim Notification Form acknowledgement |

### 7.3 Timesheet extract

The extract below is for Priyanka Mehta, Product Owner, and is derived from the Jira time export (HFI-JIRA-0001). Contracted hours are the hours in her employment contract, and R&D hours are the hours recorded against LDS tickets. Non-R&D hours are her recorded time on line management, operational meetings and sales support.

| Quarter | Contracted hours | Recorded R&D hours (LDS tickets) | Recorded non-R&D hours | R&D proportion |
|---|---:|---:|---:|---:|
| Apr to Jun 2024 | 412 | 288 | 124 | 69.9% |
| Jul to Sep 2024 | 413 | 289 | 124 | 70.0% |
| Oct to Dec 2024 | 412 | 288 | 124 | 69.9% |
| Jan to Mar 2025 | 413 | 290 | 123 | 70.2% |
| **Total** | **1,650** | **1,155** | **495** | **70.0%** |

The extract for the Group Chief Executive is not a timesheet. It is an estimate derived from the calendar classification described at section 6.3. The calendar extract (HFI-CAL-0001) classifies meetings by subject, and the R&D classification was confirmed by the Product Owner for a sample of meetings.

| Quarter | Calendar hours recorded | Hours classified as R&D | R&D proportion (estimate) |
|---|---:|---:|---:|
| Apr to Jun 2024 | 380 | 114 | 30.0% |
| Jul to Sep 2024 | 392 | 118 | 30.1% |
| Oct to Dec 2024 | 388 | 116 | 29.9% |
| Jan to Mar 2025 | 400 | 120 | 30.0% |
| **Total** | **1,560** | **468** | **30.0%** |

### 7.4 Invoice and supplier list

**Holt Engineering Services Ltd** (company number ZZ009958), supplier of provided staff under the intra-group services agreement dated 2 April 2024. Cost plus 15 per cent. Monthly invoices for the five individuals named in section 6.4.

| Invoice | Invoice date | Amount |
|---|---|---:|
| HES-INV-2404 | 30 Apr 2024 | £41,200 |
| HES-INV-2405 | 31 May 2024 | £41,400 |
| HES-INV-2406 | 30 Jun 2024 | £41,600 |
| HES-INV-2407 | 31 Jul 2024 | £41,500 |
| HES-INV-2408 | 31 Aug 2024 | £41,800 |
| HES-INV-2409 | 30 Sep 2024 | £41,700 |
| HES-INV-2410 | 31 Oct 2024 | £41,500 |
| HES-INV-2411 | 30 Nov 2024 | £41,600 |
| HES-INV-2412 | 31 Dec 2024 | £41,400 |
| HES-INV-2501 | 31 Jan 2025 | £41,700 |
| HES-INV-2502 | 28 Feb 2025 | £41,800 |
| HES-INV-2503 | 31 Mar 2025 | £41,072 |
| **Total** | | **£498,272** |

**Holt Data Labs Ltd** (company number ZZ010277), modelling services under the agreement dated 15 April 2024. Fixed fee, invoiced against milestones.

| Invoice | Milestone | Invoice date | Amount |
|---|---|---|---:|
| HDL-INV-0001 | Milestone 1: corridor and sparse-lane base models | 28 Jun 2024 | £52,500 |
| HDL-INV-0002 | Milestone 2: cold-start procedure | 30 Sep 2024 | £52,500 |
| HDL-INV-0003 | Milestone 3: reconciliation method | 31 Dec 2024 | £52,500 |
| HDL-INV-0004 | Milestone 4: production serving | 31 Mar 2025 | £52,500 |
| **Total** | | | **£210,000** |

**TrakSure Data Ltd**, telematics data licence and annual dataset fee. Included in the data and cloud figure of £88,000 with the Azure machine learning subscription, as stated in section 6.2. Invoice reference TSD-2024-0417.

**Azure machine learning subscription** (held in the company's name). Compute, storage and inference endpoint charges, from the monthly billing export for the period. Included in the data and cloud figure of £88,000 with the TrakSure licence, as stated in section 6.2. Billing export reference HFI-BILL-0001.

**Veridian Holt Holdings Ltd** (company number ZZ009931), platform licence for Holtline, recorded in the group management accounts and not included in the claim.

### 7.5 Director's declaration

I, Gavin Holt, am a director of Holt Freight Intelligence Ltd (company number ZZ009945) and am authorised to make this declaration on its behalf.

I declare that:

1. The information in this claim pack, including the Claim Notification Form, the Additional Information Form, the technical narrative, the cost schedules and the appendices, is to the best of my knowledge accurate and complete.
2. The costs in section 6 have been drawn from the company's accounting records and are reflected in the company's accounts for the period 1 April 2024 to 31 March 2025.
3. The research and development described in this claim was carried out by the company, on its own behalf and at its own risk, for the purposes of the projects described in section 5.
4. The company has retained the evidence described in section 7.2 and will make it available to HMRC on request.
5. The company will notify HMRC promptly if it becomes aware that any information in this claim is incorrect.

Signed: Gavin Holt
Position: Director
Date: 26 March 2026
