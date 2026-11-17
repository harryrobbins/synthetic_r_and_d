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
