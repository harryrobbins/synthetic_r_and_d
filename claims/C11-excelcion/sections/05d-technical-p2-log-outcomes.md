## 5. Technical narrative: P2 (flood forecasting surrogates), part 2 of 2, work log, testbed, outcomes and boundaries

### 5.23 Chronological work log, P2

The log records the iterations of the surrogate in the accounting period. Register references are to the surrogate model experiment register, TMS-SUR-001 to TMS-SUR-140.

| Date | Iteration or event | Result recorded |
|---|---|---|
| 1 April 2025 | Period begins. Training events for catchments 1 to 6 confirmed in the register (TMS-SUR-001 to TMS-SUR-038 cover the convolutional tests). | Training set frozen for the period |
| 14 April 2025 | Convolutional architecture, version 2, validated on catchments 1 to 4. Water level error on validation events recorded. | Root mean square error 0.11 m on validation events |
| 9 June 2025 | Convolutional architecture tested on overtopping events (TMS-SUR-031 to TMS-SUR-038). | Error on overtopping cells 0.62 m. Test failed. |
| 16 June 2025 | Benchmark dataset preparation begins under the subcontract with the University of Weardale hydrology group, for comparison of the hydrodynamic model against published observed events. | Datasets received in part |
| 2 July 2025 | Panel decision to pause the convolutional route for overtopping and to test a graph-based architecture. | Decision recorded in the Growth Fund minutes |
| 28 July 2025 | Graph architecture, version 0.1, run on catchment 2. | Run time 61 s on forecasting hardware, outside the target |
| 11 September 2025 | Graph architecture adopted. Mass balance constraint added to the update rule (TMS-SUR-071 to TMS-SUR-080). | Mass balance error within the hydrodynamic model tolerance |
| 29 September 2025 | Overtopping flow law added across embankment crests. Coefficient learned from training events. | Overtopping cell error reduced to 0.27 m on validation events |
| 14 October 2025 | Rivenhaven testbed events generated (TMS-SUR-096 to TMS-SUR-110). The Rivenhaven scheme model, which the team had developed for the environment agency client's flood-storage appraisal, provided the testbed for the defended floodplain test. | 620 events generated and checked |
| 3 December 2025 | Run-time optimisation: batched message passing on the forecasting hardware. | Run time 34 s for a single event |
| 20 January 2026 | Leave-one-catchment-out tests begin on catchments 1 to 6. | Results for catchments 1 to 3 recorded |
| 9 February 2026 | Leave-one-catchment-out tests complete. | Target met in four of the six catchments. Catchments 5 and 6 recorded an error above 0.15 m, both with significant overtopping. |
| 26 February 2026 | Defended floodplain test on the events held back for the purpose (overtopping events in the Rivenhaven testbed and the other defended catchment). | Results recorded and reviewed by Ian Ritchie |
| 18 March 2026 | Summary report to the Growth Fund panel. Next phase proposed for the two catchments not yet meeting the target. | Report accepted by the panel for the next phase |

### 5.24 The hydraulic modelling team and the Rivenhaven testbed

The hydrodynamic models used to generate the training events were built, calibrated and run by Excelcion's Water hydraulic modelling team, which comprises ten full-time equivalent modellers. The team's skills are the central technical resource for this project. They calibrated each catchment model to observed events, they checked the generated events for numerical stability, and they supplied the scheme models used as the testbed for the defended floodplain.

The team's time on P2 is recorded through Hourglass to the Keystone project code for GF-24-031 and to the associated scheme codes in Keystone under which the calibration and generation work was carried out. The 55% figure in section 6 is the average of those bookings across the team for the period. It reflects time recorded to Growth Fund and associated scheme codes in Keystone, and the team's work on the calibration and generation of events is the qualifying element of that time.

The Rivenhaven scheme provided the testbed for the defended floodplain test. The Rivenhaven model had been developed for an environment agency client's flood-storage appraisal, and it was used for P2 because it contains the embankment and storage arrangements the surrogate needed to be tested against. Its use in the test is described in the log at 14 October 2025 and 26 February 2026.

### 5.25 Outcome of P2 in the accounting period

At 31 March 2026 the surrogate meets the target for unseen events in four of the six catchments, with a root mean square error under 0.15 m and a run time between 28 and 39 seconds per event on the forecasting hardware. In the two catchments that do not meet the target, the errors arise where embankments overtop. The company's position is that the advance is demonstrated, in that a physics-informed graph surrogate now generalises to unseen catchments within the target for most of the portfolio, and that the remaining two catchments define the scope of the next phase of P2.

The advance is therefore a surrogate that reproduces the hydrodynamic model at the required accuracy on unseen catchments in four of six cases, that represents embankment overtopping with a mass-conserving flow law, and that runs at operational speed. The uncertainties in section 5.17 are resolved in part. Uncertainty 1 (generalisation) is resolved for four catchments. Uncertainty 2 (overtopping) is resolved for the flow law but its accuracy on the two remaining catchments is not yet within target. Uncertainty 3 (defended floodplains) is open. Uncertainty 4 (run time) is resolved.

### 5.26 Boundaries of P2

The qualifying work on P2 in this claim is the work carried out between 1 April 2025 and 31 March 2026. The surrogate programme began in 2024 under GF-24-031, and the earlier work is context for the baseline.

Within the period, the following activities are excluded from P2. Routine flood risk assessments delivered to clients using the hydrodynamic models, including the scheme appraisals for the environment agency client, are not claimed as part of P2 and are not included in the costs in section 6, other than the calibration and event generation work described in section 5.24. Operational forecasting of live flood events by the forecasting service, which uses the surrogate after the programme is complete, is not claimed. The benchmark dataset preparation under the Weardale subcontract is claimed to the extent described in section 6.

The end of the qualifying work in the period is 31 March 2026. The next phase of the programme, which addresses the two remaining catchments, is not claimed.

### 5.27 Competent professional statement, P2

I, Ian Ritchie, am Principal Data Scientist at Excelcion Limited. I lead the firm's data science practice and I have worked on statistical and machine-learning methods for engineering problems for more than fifteen years. I have a doctorate in applied mathematics, and I have published on the application of graph-based methods to scientific computing and on the limits of data-driven models in engineering.

I am the competent professional for P2. I designed the methodology in section 5.20, I reviewed each stage of the work and I reviewed the results recorded in the log in section 5.23. In my view the uncertainties in section 5.17 were genuine uncertainties to a competent professional in this field at the start of the work. The published surrogates available at the start of the period did not generalise to unseen catchments, and it could not be known in advance whether a physics-informed graph architecture would do so, whether it would represent overtopping, or whether it would meet the run-time target.

I have written elsewhere, in an Insights essay published on 12 November 2025, that data science helps an engineer to screen data and test relationships, but that engineering judgement has to decide what the results mean. The approach taken in P2 follows that view. The surrogate was tested against the hydrodynamic model, the physics of the flow was built into its structure, and the failures were recorded and analysed. The approach in P2 was not to rely on the surrogate's accuracy on the training data but to test it where the engineering risk is greatest.

I confirm that the hydraulic modelling team's time on P2 is correctly recorded in the way set out in section 5.24, and that the calibration and event generation work the team carried out is the qualifying element of that time.

Signed: Ian Ritchie, Principal Data Scientist
