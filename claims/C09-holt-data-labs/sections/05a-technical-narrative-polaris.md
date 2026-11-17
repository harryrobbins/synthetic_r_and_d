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
