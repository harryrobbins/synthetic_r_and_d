### 5.15 Project 2: QH-DYNA, stack-level thermal management for dynamic operation

#### 5.15.1 Overview

QH-DYNA addresses the thermal behaviour of a full electrolyser stack when its current is changed rapidly. It is a smaller project than QH-LOWIR and draws on a smaller part of the team's time. It is, however, a separate project with its own baseline, advance and uncertainties, and its work was carried out in a separate test programme on the Company's stack test benches.

The project is a consequence of the same operating requirement that drives QH-LOWIR. Electrolysers paired with renewable generation must follow the output of wind and solar plant, which can change current by large amounts within minutes. The stack's thermal behaviour under these conditions determines the membrane hydration, the local temperature at the catalyst layer and therefore the rate at which the layer degrades. QH-LOWIR's durability results depend on the thermal boundary that the stack provides, and QH-DYNA was established to address that boundary at stack level.

#### 5.15.2 Baseline

Electrolyser stacks are normally designed and controlled for steady operation at a fixed current. The thermal management strategy for a stack is typically based on a coolant flow rate set to the mean heat load, with a control loop that responds to the outlet temperature. Such strategies have been shown in the Company's own earlier work, and in the published operating experience of stack manufacturers, to be adequate for steady operation.

Under rapid current changes, the same strategies do not respond adequately. The outlet temperature lags the local temperature in the stack, so that the control loop reacts after the local temperature has already risen or fallen. The published accounts of such operation describe local temperature excursions of several degrees across the active area, with corresponding variations in membrane hydration. The baseline for QH-DYNA is therefore a stack that is controlled for steady operation and that shows local temperature excursions during rapid current changes of the magnitude seen in the renewable supply profile.

The Company's stack test benches confirmed this baseline in early 2025. A stack operated on the steady-state control strategy showed an outlet temperature that tracked the load with a lag of approximately 40 seconds, and a spread of local temperatures across the active area that increased from around 2 °C at steady state to around 7 °C during the fastest ramp in the profile.

#### 5.15.3 Advance sought

The advance sought by QH-DYNA is a stack-level thermal management approach that holds temperature uniformity across the active area during rapid current changes without a significant increase in parasitic load. The Company's approach combines a predictive model of the stack thermal response with a coolant flow plan that is adjusted ahead of the expected current change, rather than in reaction to the outlet temperature.

The coolant flow plan is derived from a thermal model of the stack that predicts the local temperature response to a given change in current. The model is calibrated against the stack test bench data and is used to set the coolant flow for each ramp in the profile. The advance lies in using a predictive, stack-level plan for coolant flow during dynamic operation, which the baseline control strategy does not do.

The Company has not, in its review of the published literature, identified a published approach that uses a calibrated stack-level thermal model to set the coolant flow plan ahead of the current change for PEM stacks of the Company's design. The Company's view is that the approach is not obvious to a competent professional in the field, because the thermal model must capture the coupling between the electrochemical heat generation and the coolant flow in a stack whose heat generation varies across the active area.

#### 5.15.4 Uncertainties

Three uncertainties were identified for QH-DYNA at the start of the project in February 2025.

**Uncertainty 1: the thermal response under the fastest ramps.** The Company did not know whether a stack-level model calibrated at moderate ramp rates would predict the thermal response at the fastest ramps seen in the renewable supply profile, where the heat generation changes faster than the thermal mass of the stack can follow.

**Uncertainty 2: the effect of local excursions on membrane life.** The published literature on membrane degradation links membrane hydration cycles to mechanical fatigue, but the link has not been quantified for the local excursions produced by the Company's stack under dynamic load. It was not known whether the excursions that could be reduced by the coolant plan were large enough to change the membrane life materially.

**Uncertainty 3: the trade-off between coolant flow and parasitic power.** A coolant plan that holds temperature uniformity by increasing coolant flow increases the parasitic load of the stack, and the increase may offset the efficiency gain from the more uniform operation. The Company did not know at the start of the project where the optimum lay for its stack design.

#### 5.15.5 Methodology

The project used three elements. The first was a thermal model of the stack, developed by the Company in the first quarter of 2025 and calibrated against the test bench data from the steady-state tests. The model is a lumped-parameter representation of the stack, divided into sections across the active area, with each section having its own heat generation and heat transfer terms. The model was validated against the measured local temperatures at four points in the stack, instrumented with thermocouples during the test programme.

The second element was instrumented stack testing. The test programme applied the renewable supply profile to the stack at three ramp rates, and recorded the outlet temperature, the local temperatures at the four instrumented points, the coolant flow and the parasitic power at a sampling rate of one reading per second. Each test was repeated with the steady-state control strategy and with the predictive coolant plan, so that the difference between the two could be attributed to the plan.

The third element was iteration of the coolant flow plan. Each plan was derived from the model, tested on the stack, and compared with the measured local temperature spread and parasitic power. Plans that reduced the local spread but increased the parasitic power by more than the efficiency gain were rejected. The iterations were recorded in the project tickets with the model version and the test data reference.

Dr Joel Abernethy led the stack testing and the validation of the model against the thermocouple data. The coolant plan was developed by Dr Nadia Fenwick, who reviewed each iteration.

#### 5.15.6 Work log

The work log for QH-DYNA is set out below.

**February 2025.** The project was opened on 10 February (QHL-JR-2230). The first stack test on the steady-state control strategy was run on 24 February, confirming the baseline in section 5.15.2 (QHL-TD-0224).

**March 2025.** The first version of the thermal model was completed on 14 March. It was calibrated against the steady-state data and predicted the outlet temperature to within 0.6 °C at steady state. The first predictive coolant plan, designated CP-1, was derived from the model on 20 March and tested on the stack on 27 March (QHL-LB-0320, QHL-TD-0327).

**April 2025.** CP-1 reduced the local temperature spread during the slowest ramp, but at the fastest ramp the model under-predicted the local excursion by about 1.8 °C. The model was revised on 9 April to include the thermal mass of the coolant manifold, which had been omitted from the first version. The revised model was used to derive CP-2 on 16 April (QHL-LB-0417).

**May 2025.** CP-2 was tested on 6 and 12 May at the three ramp rates. The local temperature spread was reduced at all three ramp rates, but the parasitic power increased by a margin that was judged to offset part of the efficiency gain. The Company considered that the coolant flow ramp should be made less aggressive at the start of each ramp (QHL-TD-0512).

**June 2025.** CP-3 was derived on 3 June with a ramp-rate dependent coolant schedule. It was tested on 10 and 19 June. The parasitic power was reduced relative to CP-2, and the local spread at the fastest ramp was within the 3 °C figure that the Company had set as its working threshold for membrane fatigue. This threshold was taken from the Company's own accelerated membrane fatigue data and not from the published literature (QHL-TD-0619).

**July to September 2025.** The work was suspended for part of July while the stack test benches were used for QH-LOWIR. It resumed on 4 August with CP-4, a refinement of CP-3 in which the coolant schedule at the lowest ramp rate was simplified. CP-4 was tested on 11 and 18 August and on 2 September. The results were consistent with CP-3 and showed no further reduction in the parasitic power at the same local spread. The Company selected CP-4 as the plan for the remainder of the period on 9 September (QHL-JR-2265).

**October to December 2025.** The Company used CP-4 in a series of endurance runs on the stack, with the renewable supply profile applied for periods of 300 hours in total. The local temperature spread remained within the working threshold throughout. The endurance runs produced no evidence of performance change in the stack that could be attributed to the thermal regime, and the results were recorded in QHL-TD-1204. A final validation of the model against the endurance data was completed on 15 December (QHL-LB-1215).

#### 5.15.7 Outcomes

The principal outcome of QH-DYNA is a validated thermal model and a coolant flow plan, CP-4, that reduces the local temperature spread across the active area of the Company's stack during rapid current changes, without the parasitic power penalty of the steady-state approach at the fastest ramp. The Company has also established the local temperature threshold for membrane fatigue in its own design, which it had not previously been able to specify.

The uncertainty on the effect of local excursions on membrane life is not fully resolved. The endurance runs did not reach the membrane life targeted in the Company's specification, and the quantitative link between the excursions and membrane life remains to be established.

#### 5.15.8 Boundaries of QH-DYNA

The work claimed for QH-DYNA starts on 10 February 2025, when the project was opened, and ends on 31 December 2025, the end of the period. The work on the thermal model before February 2025, which was part of the Company's 2024 stack development, is not claimed.

### 5.16 Competent professional statement

Dr Nadia Fenwick is the Company's Chief Technology Officer and the competent professional for this claim. She holds a PhD in electrochemistry and has twelve years' experience in fuel cells and electrolysers. Before joining the Company she led research into stack design and durability at a German stack manufacturer. Her experience covers the design and testing of MEAs, the characterisation of catalyst layers and porous transport layers, and the thermal and electrochemical management of stacks under variable load. She is familiar with the published literature on PEM electrolyser catalysis, durability and thermal management, and has published on the mechanisms of PTL passivation.

Dr Fenwick supervised both projects in the period. Her position is that the knowledge available at the start of 2025 did not enable a competent professional in PEM electrolysis to meet the combined targets of QH-LOWIR, or to establish the stack-level thermal approach of QH-DYNA, without the investigation described in this section. In forming that view she has relied on her knowledge of the published work, on the Company's own results from 2024, and on the baseline evidence described in sections 5.3 and 5.15.2.

Dr Fenwick confirms that she has reviewed the work log, the outcomes and the boundaries set out in this section, and that the work described was carried out by the Company's staff in the manner described. Her curriculum vitae is at Appendix 7.1.

Signed: Dr Nadia Fenwick, Chief Technology Officer
Date: 27 October 2026
