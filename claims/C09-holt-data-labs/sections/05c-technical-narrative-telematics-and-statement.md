## 5. Technical narrative (continued)

### 5.3 Project 2: Telematics Pipeline

#### 5.3.1 Context

Project 1 depends on features that describe how vehicles move: where they dwell, where they detour, and when they are loaded or empty. None of these features exists in the raw telematics stream. The stream consists of position pings, emitted by in-vehicle units at irregular intervals, with clock drift between devices and with frequent gaps where coverage is poor. The Telematics Pipeline was undertaken to derive dwell and detour features from that stream at a resolution sufficient for the forecasting models, and to do so at a cost that allows the features to be recomputed each day.

#### 5.3.2 Baseline

The baseline is standard batch processing of telematics pings into fixed-interval records. In that approach, pings are resampled to a regular grid, typically at one-minute or five-minute intervals, and the stop and movement states of each vehicle are inferred from the resampled series. These approaches cannot represent dwell and detour behaviour at the resolution the demand features require. A dwell of twelve minutes at a loading bay and a dwell of forty minutes in a fuel queue are indistinguishable on a five-minute grid, and the detours that signal a driver's diversion around a closed road are lost altogether.

Fixed-interval processing could be made finer, but only at a cost in compute that made daily recomputation across the full ping volume impractical. The company's assessment at the start of the project was that the baseline could not satisfy both the resolution and the cost requirement at once.

#### 5.3.3 Advance sought

The advance sought is a method for deriving dwell and detour features from irregular raw pings, with three properties. The first is that dwell and detour events are identified at their natural temporal resolution rather than on a fixed grid. The second is that the derivation tolerates irregular ping intervals and clock drift without a loss of accuracy. The third is that the derivation is efficient enough to be executed within the daily processing window, across the full set of vehicles in the licence.

#### 5.3.4 Uncertainties

The company identified two uncertainties at the outset.

The first concerned accuracy under irregular pings. Event-based dwell detection depends on the timing of pings near the start and end of a stop. Where pings are sparse, the start and end times are uncertain, and where clocks drift, pings from the same vehicle may be out of order. It was not known whether a derivation could be designed that remained accurate under these conditions without reverting to a fixed grid.

The second concerned efficiency. Event-based detection over a ping stream of approximately 3.2 billion records is a computationally demanding operation if implemented naively. It was not known whether the derivation could be restructured to run within the daily window, given the infrastructure available on Azure.

#### 5.3.5 Methodology

The methodology for the Telematics Pipeline combined controlled testing with iterative redesign. Accuracy was tested against a labelled sample, constructed from journeys for which the company held independent records of stops, including loading and unloading documents and driver-confirmed delivery times. The labelled sample comprised 1,840 journeys, selected to span the range of ping densities in the licence.

Accuracy was measured as the proportion of dwell events detected within a tolerance of two minutes of the labelled start and end times, and as the proportion of detour events matched to a labelled diversion. Efficiency was measured as wall-clock time and compute cost for a full daily recomputation on a representative day of pings.

The derivation method was developed in stages. The first stage cleaned and ordered the pings for each vehicle, correcting clock drift against a reference ping where one was available. The second stage identified candidate stops from runs of low speed and absence of movement. The third stage refined the start and end times of each candidate stop, using the nearest pings on either side. The fourth stage classified each stop by its dwell duration and location, and identified detours by comparing the vehicle's path against the expected route.

#### 5.3.6 Chronological work log

| Date | Reference | Iteration and result |
|---|---|---|
| 15 April 2024 | LDS-612 | Project opened, titled "Pipeline dwell features". Raw ping schema and clock drift characteristics documented from the licence sample. |
| 6 May 2024 | LDS-612 | Fixed-interval baseline implemented as a reference. Dwell detection on a five-minute grid recorded at 64% accuracy against the labelled sample. |
| 28 May 2024 | LDS-612 | First event-based stop detection implemented. Accuracy at the two-minute tolerance recorded at 71%. Failures concentrated on journeys with sparse pings. |
| 18 June 2024 | LDS-649 | Clock drift correction implemented against reference pings. Out-of-order pings reduced to 0.2% of the sample. |
| 9 July 2024 | LDS-649 | Start and end refinement introduced for candidate stops. Accuracy at the two-minute tolerance recorded at 88%. |
| 31 July 2024 | LDS-655 | Detour identification implemented by comparison of path against expected route. Initial match rate 52% of labelled diversions. |
| 22 August 2024 | LDS-655 | Route comparison redesigned to use a tolerance band that adapts to road class. Match rate recorded at 79%. |
| 16 September 2024 | LDS-661 | Efficiency work opened. Naive implementation required approximately nine hours for a daily recomputation on a representative day. |
| 11 October 2024 | LDS-661 | Stages restructured to process vehicles in partitioned batches with state carried between stages. Recomputation time reduced to approximately three hours and forty minutes. |
| 4 December 2024 | LDS-661 | Compute cost of the daily recomputation reduced below the level set at the outset of the project. Daily window met on all representative days tested. |
| 14 February 2025 | LDS-612 | Project closed for the period. Final derivation method documented. Dwell and detour features handed to Project 1 for use in the forecasting models. |

#### 5.3.7 Outcomes

The Telematics Pipeline delivered a method for deriving dwell and detour features from irregular raw pings. Dwell detection accuracy at the two-minute tolerance was 88% on the labelled sample, against 64% for the fixed-interval baseline. Detour matching reached 79% of labelled diversions. The derivation tolerates the clock drift and sparse pings present in the licence, and a full daily recomputation now completes within the daily processing window.

The features produced by the pipeline were used by Project 1 in the temporal fusion and gradient-boosted models described in section 5.2. The company's view is that the pipeline's advance is inseparable from the forecasting method it serves, and the two projects are presented together in this pack for that reason.

#### 5.3.8 Boundaries

The Telematics Pipeline began on 15 April 2024 and ended on 14 February 2025. Work on the production ingestion of the licence data after 14 February 2025 is operational and is excluded. Work that was required only to load and store the raw data, which was carried out by the company's contractors before the project opened, is excluded. The boundary of the project is the derivation of features whose accuracy and efficiency were uncertain at the outset.

### 5.4 Time apportionment and the seconded team

The research described in sections 5.2 and 5.3 was carried out by the company's research team. The team comprised Dr Simon Achterberg as Chief Scientist, Ms Natasha Grieve as Machine Learning Engineer and Mr Gavin Holt as director. Their time on each project is apportioned in the cost schedules at section 6, using the methodology described there.

Dr Achterberg and Ms Grieve work on the company's research on a full-time secondment basis and spend the large majority of their working time on the two projects. Mr Holt's time is divided between research direction, the commercial relationships of the company and the preparation of the company's accounts. The apportionment of his time has been set on the basis of an interview with him and of his calendar for the period.

The apportionments reflect the proportion of each person's time that was spent on the projects described in this section, as recorded in the timesheets and Jira history, and as confirmed in interviews with each individual. The apportionments are not intended to represent the full extent of each person's activity but only the portion that falls within the research.

### 5.5 Summary of the advance

Taken together, the two projects achieved an advance in the field of freight demand forecasting in three respects. They produced a hierarchical reconciliation procedure that is stable on sparse lanes, when published methods are not. They produced a calibrated temporal forecasting method for sparse lanes, with interval coverage that conventional approaches could not achieve on that population. They produced a cold-start method for new shippers, and a feature derivation method for irregular telematics pings that delivers the resolution and efficiency required by the forecasting models.

The company accepts that the forecasting models in the final system include established components, including gradient-boosted trees and a temporal fusion architecture, and that these components were tuned for the company's data. The advance lies in the reconciliation, calibration and cold-start methods, together with the means by which they were made to work with those components on sparse, physically constrained data. The company's view is that a competent professional in the field, faced with the uncertainties described above, would not have been able to achieve the outcomes recorded without carrying out the work described.

### 5.6 Evidence

The evidence supporting this section is held in the company's repository, in the Jira project LDS, in the experiment registry and in the minutes of the weekly technical review. Extracts from these sources are listed at section 7. The company will make the full records available to HMRC on request.

### 5.7 Competent professional statement

I, Dr Simon Achterberg, make the following statement in support of this claim.

I have worked in machine learning and statistical forecasting for more than fifteen years. My doctoral research concerned the reconciliation of hierarchical time-series forecasts, and I have published on the stability of constrained forecast adjustment. From 2017 to 2021 I led the data science function of a logistics technology business, where I was responsible for the design and evaluation of demand forecasting systems across a large network of road-haulage operations. Since 2021 I have worked as a principal data scientist, and I have been seconded to the research of Holt Data Labs Ltd since its programme began in April 2024. I am therefore familiar with the state of practice in freight demand forecasting and with the limitations of the methods in general use.

I was the competent professional for Project Polaris throughout the period, and I chaired the weekly technical review at which the results of the project were evaluated. In that capacity I had responsibility for the design of the experimental programme, for the assessment of whether each uncertainty had been resolved, and for approving the freeze of the reconciliation design on 21 October 2024.

In my professional judgement the uncertainties described in section 5.2.4 could not have been resolved by a competent professional working with the published methods and commercially available tools available at the start of the project. The reconciliation, calibration and cold-start methods were developed by the research team under my direction, and I was responsible for the backtesting design, the acceptance criteria and the decisions to adopt or reject each candidate method. I confirm that the descriptions in this narrative of what was known, what was attempted and what was learned are accurate to the best of my knowledge. The outcomes recorded in section 5.2.9 are, in my view, a genuine advance on the state of practice for sparse freight demand.

I also confirm that the work described in the Telematics Pipeline, which supports Project Polaris, was carried out under my technical oversight and that the uncertainties recorded for that project were, in my view, not resolvable from existing knowledge at its outset.

Signed: Dr Simon Achterberg
Position: Chief Scientist, Holt Data Labs Ltd
Date: 12 August 2025
