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
