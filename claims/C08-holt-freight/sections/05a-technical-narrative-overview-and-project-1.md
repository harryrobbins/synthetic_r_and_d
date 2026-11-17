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
