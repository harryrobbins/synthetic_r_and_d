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
