## 5. Technical narrative: P2 (flood forecasting surrogates), part 1 of 2, baseline, advance and method

### 5.14 P2 overview

**Project reference and status.** Growth Fund paper GF-24-031. The project is a continuation of the surrogate-model programme that began in 2024, and it was carried forward into the accounting period with the same technical plan, the same testbed and the same competent professional. The work was delivered jointly by Excelcion's Water and Data Science teams and by Tarnbeck Modelling Services Ltd, which provided modelling staff under a services agreement. The competent professional is Ian Ritchie, Principal Data Scientist.

**Summary.** Flood forecasting for a river catchment depends on a model of how water moves across the floodplain. The model used for the detailed work is a two-dimensional hydrodynamic model, which solves the equations of shallow water flow on a grid that covers the floodplain and the channel. Such a model gives an accurate picture of the flood, including the depth, the velocity and the extent of inundation, but it is slow. A single event takes between two and six hours to run. An operational forecast during a flood needs an answer in minutes, and the model cannot give one. P2 sets out to build a surrogate: a model that learns the behaviour of the hydrodynamic model from many runs, and reproduces its output for a new event in seconds.

### 5.15 Baseline

The baseline is the state of published and practised work at the start of the project. Two-dimensional hydrodynamic models are the accepted tool for detailed flood risk assessment in the United Kingdom. They are calibrated to observed events and used to test the effect of flood defences, storage schemes and land-use change. Their run time has been the main barrier to using them for real-time forecasting, and forecasters have relied on simpler one-dimensional models or on empirical relationships for that purpose.

Machine-learning surrogates have been proposed in the literature as a way to reduce run time. The published work reports good accuracy on the catchments used to train the surrogate. It also reports that the surrogates struggle to generalise. A surrogate trained on one set of catchments performs poorly on a catchment it has not seen, and the errors grow where the flow is discontinuous, for example where an embankment overtops and water moves across the defence in a short period. The defended floodplains that matter most for forecasting are the places where overtopping occurs, so the limitation is a serious one for operational use.

On that basis the baseline was taken to be a published surrogate that reproduces the hydrodynamic model accurately on training catchments, does not generalise to unseen catchments, and does not represent overtopping reliably.

### 5.16 Advance sought

The advance sought was a surrogate that generalises to unseen catchments and represents overtopping, that reproduces the water levels of the hydrodynamic model within a stated error, and that runs in under 40 seconds for a single event. The surrogate was to be physics-informed, meaning that the form of the model respects the conservation of mass across the floodplain, rather than learning the relationship between inputs and outputs without constraint.

The target error was a root mean square error under 0.15 m on unseen events, measured against the water level from the hydrodynamic model on the same grid. The target was set so that the forecast would be useful to the operational forecaster in the sense that the uncertainty introduced by the surrogate is smaller than the uncertainty already present in the rainfall forecast.

### 5.17 Technical uncertainties

The following uncertainties were recorded in GF-24-031 at the start of the period.

**Uncertainty 1: generalisation to unseen catchments.** It was not known whether a surrogate trained on six catchments would reproduce the hydrodynamic model accurately on a catchment it had not seen, or whether the surrogate would need to be retrained for each new catchment.

**Uncertainty 2: representation of overtopping.** Overtopping produces a sudden change in the flow across an embankment. Surrogates trained on smooth fields tend to smooth over that change. It was not known whether a surrogate could represent overtopping with an error comparable to the error on the rest of the floodplain, or whether overtopping events would need a separate treatment.

**Uncertainty 3: accuracy on defended floodplains.** Defended floodplains combine embankments, storage and channel constraints, and the errors in each component may compound. It was not known whether the error target could be met on defended floodplains without a separate model for each defence.

**Uncertainty 4: run time at operational scale.** The surrogate must run quickly on the hardware available to the forecasting service. It was not known whether the physics-informed architecture would stay within the run-time target once the grid resolution required for the forecast was reached.

### 5.18 Experimental design

The surrogate was trained on synthetic events. The events were generated by running the hydrodynamic model on a range of rainfall and river inflow scenarios for six catchments, chosen to represent the range of catchment size, slope, land use and defence arrangement in the company's flood portfolio. Each event produced a time series of water levels and velocities across the grid. In total 4,100 synthetic events were generated and used. The generation and the quality checks on each event are recorded in the experiment register, which runs from TMS-SUR-001 to TMS-SUR-140.

The synthetic events were split by catchment. For the generalisation test a leave-one-catchment-out design was used. For each of the six catchments in turn, a surrogate was trained on the other five and tested on the held-out catchment, so that every catchment was tested as an unseen catchment once. The events of the held-out catchment were not used at any stage of training or model selection for that test. This is the most demanding test of the approach, because it addresses the uncertainty identified in section 5.17 (1) directly.

Observed events were used for calibration checks only. Where an observed flood event was available for a catchment, the hydrodynamic model was calibrated to it, and the surrogate was compared against the calibrated model. The observed data were supplied by the Environment Agency and by the flood risk teams of the catchment operators, under the terms of the data licences recorded in the project file.

### 5.19 Architecture of the surrogate

The surrogate represents the floodplain as a graph. Each node is a computational cell of the grid, and each edge connects two neighbouring cells across a face. The node features include the ground elevation, the roughness, the defence height where a defence is present, and the water level and velocity at the previous time step. The edge features include the length of the shared face, the elevation difference and the flow capacity of the face, which in the case of an embankment depends on whether the crest is overtopped.

The model passes messages along the edges and updates the node states over a sequence of steps that corresponds to the time step of the hydrodynamic model. The update rule is constrained so that the net flow into each node balances the change in storage over the time step. This is the physics-informed element of the architecture. It means that the surrogate cannot create or destroy water, which is a property the hydrodynamic model has by construction and which a surrogate trained without the constraint does not reliably have.

Overtopping is represented by a separate flow law across the crest of the embankment, applied when the water level exceeds the crest height. The flow law is a standard weir relationship. The surrogate learns the coefficient and the transition from the training events, and the constraint on mass balance applies across the transition.

### 5.20 Methodology

The methodology is in four parts: generation of the training events; development of the surrogate architecture; training and validation; and testing on unseen catchments and on defended floodplains.

Training events were generated and quality checked as described in section 5.18. Each event was checked for numerical stability, mass conservation within the tolerance of the hydrodynamic model, and the presence of the expected flow pattern. Events that failed a check were rerun or removed, and the reason was recorded in the register.

The surrogate architecture was developed in stages. A convolutional surrogate was tested first, because it is the architecture most often used in the published work. A graph-based surrogate was developed second, with the constraint on mass balance and the overtopping law described in section 5.19. Both were compared on the validation catchments using the same metrics: root mean square error of water level, the error on the overtopping cells, and the run time for a single event on the forecasting hardware.

Training used the five training catchments in each fold. Model selection used a validation split drawn from those catchments. The held-out catchment in each fold was used only after the architecture had been selected. The test on defended floodplains used the events in which an embankment overtops, which were identified in the register and held back from training for the purpose of the test.

### 5.21 Competent professional's approach to the methodology

Ian Ritchie designed the methodology and reviewed each stage. His approach was to test the architecture on the hardest case first, which is the overtopping event, and to hold back the unseen catchments until the architecture had been selected. This sequencing is recorded in the experiment register. Where a result was unexpected, the architecture was revised and the revision recorded, rather than the test being rerun on a different split. The register records the iterations that failed as well as those that passed, and the failures are described in the log in section 5.22.

The quality of the synthetic training data is central to the outcome. The events were generated to span the range of conditions the forecasting service is expected to meet, and the hydrodynamic model used to generate them was calibrated to observed events on each training catchment before generation began. The calibration records are held in the project file.

### 5.22 Technical approach to run time

Run time is part of the advance. The hydrodynamic model takes between two and six hours per event. The surrogate must produce a comparable output in under 40 seconds on the forecasting hardware. The graph structure lends itself to parallel evaluation, and the architecture was designed so that the message-passing steps can be evaluated in batches on a single graphics processor. The run time was measured on the forecasting hardware at each stage of development. The measurements show that the final architecture runs a single event in between 28 and 39 seconds across the six catchments, which is inside the target. The run-time figures in the register use the same grid resolution as the operational forecast.
