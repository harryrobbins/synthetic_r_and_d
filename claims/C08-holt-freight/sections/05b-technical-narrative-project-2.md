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
