## 5. Technical Narrative

### 5.1 Introduction and scope

This section is the full technical report for the research and development carried out by Thistlebrook Precision Engineering Ltd in the accounting period from 1 October 2024 to 30 September 2025. It is written to the standard set out in the DSIT Guidelines on R&D tax relief, and it is structured project by project. For each project it sets out the baseline, the advance sought, the scientific or technological uncertainties, the methodology, a chronological work log with dated iterations, the outcomes and the boundaries of the project. A competent professional statement is given at section 5.9.

Two projects are claimed. Project P1, THINFIN (internal reference TPE-2024-07), is the principal project and accounts for all of the staff, consumable, subcontract and software costs in the cost schedule. Project P2, powder reuse limits for Ti-6Al-4V under high recoat-frequency builds, is a smaller workstream carried out within the THINFIN programme. It has no separate cost line and its costs are included within those of P1. It is described at section 5.10.

The narrative uses the company's build-log references throughout. Each build is identified as TPE-BL-nnn, and where a laboratory book entry exists it is referenced in the format TPE-LB-nnnn. Build logs, laboratory book pages and the reports of external test providers are listed in the evidence index in the appendices.

### 5.2 Project P1: background to the THINFIN programme

Laser powder-bed fusion is a process in which a thin layer of metal powder is spread across a build plate and melted selectively by a laser, layer by layer, until a part is complete. The process allows internal geometries that cannot be produced by machining or casting, and it has become the preferred route for lightweight heat exchangers in the aerospace and motorsport sectors. A plate-fin heat exchanger, in which a stack of thin fins forms a set of narrow channels between flat plates, is a particularly demanding geometry for the process. The fins are the thinnest features in the part, and they are also the features that most need to be accurate, because their dimensions set the flow area and the heat-transfer surface.

Thistlebrook had produced plate-fin test articles in Ti-6Al-4V since 2021, with fin walls of 0.8 mm. At that thickness the company's pre-build simulation predicted the as-built wall position to within the tolerance required for the customer's assemblies, and the process could be run without internal supports. The customer, Corran Aero Systems, asked the company in 2024 to develop a heat exchanger design with walls of 0.35 mm, because a thinner wall increases the heat-transfer surface for a given envelope and reduces the mass of the unit. Corran Aero Systems' requirement was for a build height of 180 mm, a wall position tolerance of ±0.1 mm and no internal supports in the enclosed channels.

The THINFIN programme was opened to meet that requirement. The company's experience of the process told it that the requirement could not be met by extending the existing approach. The programme was therefore designed as a research effort, with a series of instrumented builds that would test a number of hypotheses about the behaviour of thin walls, and with clear go and no-go criteria for each stage.

### 5.3 Baseline

The baseline for P1 is the state of the art at the start of the period, as far as it was known to the company and to its competent professional. It has three parts.

The first part is the predictive capability of commercial build-simulation tools. The company's simulation workstation runs a thermo-mechanical package which models the build as a sequence of layer activations, with a moving heat source calibrated to the process parameters and a material model for Ti-6Al-4V over the temperature range of the process. Using that package with standard calibration, the company's experience and that of the wider industry is that macro-distortion of walls of 0.8 mm and above can be predicted to within about 0.1 mm. Below that thickness, the same tools give a useful qualitative prediction of distortion direction but their quantitative accuracy degrades considerably, and in the company's experience no published calibration had been demonstrated to predict wall position to better than 0.1 mm at 0.35 mm.

The second part is the behaviour of thin walls during the build. At wall thicknesses below about 0.5 mm, the walls are slender enough to buckle under the thermal stresses generated as each layer is melted, and they are also close enough to the recoater that the recoater blade can strike a wall that has moved out of position. Neither effect is captured fully by the simulation tools in their standard form. The recoater interaction in particular is not a thermo-mechanical effect that the standard models address.

The third part is industry practice. For thin-walled channels, practitioners in the field have two options. The first is to thicken the walls, which reduces the heat-transfer surface and so reduces the performance of the heat exchanger. The second is to use internal supports within the channels, which cannot be removed after the build and which therefore block the channel and compromise the function of the part. Neither option meets the customer's requirement, and the company was not aware of a published method that avoided both.

### 5.4 Advance sought

The advance sought was a method by which the distortion and wall position of 0.35 mm Ti-6Al-4V walls can be predicted and compensated to within ±0.06 mm over a build height of 180 mm, without internal supports and without thickening the walls.

The company's hypothesis was that the predictive gap at thin walls could be closed by a combination of two elements. The first was a calibration of the thermo-mechanical simulation against measured distortion from instrumented builds at the target wall thickness, so that the model's heat source and material parameters would reflect the real behaviour of thin walls rather than the behaviour of thick walls extrapolated downward. The second was a scan strategy that would suppress the buckling and recoater interaction by controlling the thermal history of each wall. The company's working name for the scan strategy elements was "variable contour power", in which the contour laser power is reduced in the thinnest walls to limit heat accumulation, and "stitched island orientation", in which the islands within each wall are sequenced and rotated so that the thermal gradients across the wall are balanced from one layer to the next.

The company did not believe that either element was new in isolation. Variable contour power is described in general terms in the literature on process parameter optimisation, and island scanning is established practice. The advance the company sought was the combination of a calibration that would make the simulation accurate at 0.35 mm with a scan strategy whose parameters could be selected by that simulation, so that the process could be designed rather than tuned by trial and error.

### 5.5 Scientific and technological uncertainties

The uncertainties for P1 were recorded in the programme register at the start of the programme. There were three.

The first uncertainty was whether thermal-stress models could be calibrated at a wall thickness of 0.35 mm at all. The calibration requires measured distortion with a precision well below the target tolerance. At 0.35 mm, the voxel size of the computed tomography data used to measure the walls approaches the melt-pool width, so that the measured wall geometry contains an error that is comparable to the quantity being measured. The company did not know whether a calibration could be extracted from such data, or whether a different measurement method would be needed.

The second uncertainty was whether a scan strategy that suppressed buckling and recoater interaction would also cause lack-of-fusion porosity. Reducing the contour power in thin walls reduces the energy delivered to the powder and so raises the risk of incomplete melting at the wall edges. The company did not know the energy window within which both buckling and porosity could be controlled, and it had no published data for Ti-6Al-4V at this geometry.

The third uncertainty was whether recoater collision could be predicted from the build geometry before a build was started. The recoater blade is a hard body that passes over the build surface at each layer, and a wall that has moved out of position by a fraction of a millimetre may strike the blade. The company did not know whether the wall position predicted by a calibrated simulation would be accurate enough to determine collision risk, or whether the risk depended on factors that the simulation would not capture.

### 5.6 Methodology

#### 5.6.1 Equipment and material

All builds in the programme were carried out on the company's first laser powder-bed fusion system, a machine with a 250 mm by 250 mm build plate, a single fibre laser of 500 W maximum power, inert-gas atmosphere control and in-situ layer imaging. The second system was used for builds TPE-BL-416 and TPE-BL-421 to confirm that the process transferred between machines. Both systems were calibrated to the same procedure before each build campaign.

The material was gas-atomised Ti-6Al-4V powder of 15 to 45 micron particle size, supplied with a certificate of analysis for each lot. Fresh powder was blended with reused powder in a ratio that was varied between builds according to the powder reuse study described at section 5.10. The layer thickness for all builds was 30 microns. The hatch spacing was 0.08 mm, and the laser scan speed was 900 mm/s for the bulk fill, with the contour parameters adjusted as described at section 5.6.3.

The build plate was cut from a wrought Ti-6Al-4V billet and was not re-used between builds.

#### 5.6.2 Simulation

The simulation workstation runs a thermo-mechanical build-simulation package. The package models each layer as a set of activated elements, applies a moving heat source to the activated elements and computes the temperature history and resulting stress and distortion. The company's simulation engineer, Dev Mistry, maintains the model library for the process and is responsible for the calibration work.

For the THINFIN programme, the simulation was set up with a double-ellipsoid heat source, with the heat source parameters calibrated against melt-pool dimensions measured in the in-situ layer images. The material model used the temperature-dependent properties of Ti-6Al-4V from the vendor's library, with the plastic hardening parameters adjusted to reproduce the distortion measured on the early calibration builds. The support of the build plate and the recoater contact were modelled in a simplified form.

The calibration method was iterative. Each build provided a measurement of the wall position at a set of control points, measured by coordinate measurement and, from build TPE-BL-405 onwards, by computed tomography. The simulation was run for the build geometry, the discrepancy between predicted and measured wall position was computed at each control point, and the heat source and hardening parameters were adjusted to reduce it. The adjusted model was then used to predict the next build, and the prediction was compared with the measurement.

#### 5.6.3 Scan strategy

The scan strategy for the THINFIN builds combined three elements.

The first was the variable contour power. In the initial builds, all contour passes were run at a single power of 280 W. From build TPE-BL-407 the contour power for walls below 0.5 mm was reduced to a value determined by the simulation for each wall's local thermal history, with a lower bound of 190 W.

The second was the stitched island orientation. Each wall was divided into islands of 2 mm length, and the islands were sequenced so that adjacent islands in the same layer were scanned with an orientation rotated by 67 degrees relative to their neighbours. The sequence was then offset from layer to layer so that the heat input from successive layers did not accumulate at a single location in the wall. The company's competent professional developed the sequencing rule, and the rule was first implemented in TPE-BL-410.

The third was the recoat protocol. Thin walls were treated by a short dwell of 4 seconds after each layer, to allow the wall to cool before the recoater passed, and by a recoater speed reduction of 35% in the upper third of the build height, where the walls were most at risk of contact.

#### 5.6.4 Measurement

Wall position was measured by three methods, selected according to the stage of the programme.

Coordinate measurement was used on all builds. Each build was measured on the metrology bench using a coordinate measuring machine with a probe calibrated to traceable standards. Measurements were taken at 24 control points per build, with the results recorded in the build log. The metrology technician, Lisa Okafor, carried out all coordinate measurements.

Computed tomography was used from build TPE-BL-405 onwards for the detailed characterisation of wall geometry and porosity. The company does not operate a computed tomography system in-house. CT scans were therefore obtained from an external provider, Präzisionsmesstechnik Halde GmbH, under a service arrangement that is described at section 5.12. The provider issued a report for each scan, with reference numbers in the PMH-CT-2025 series.

In-situ layer imaging was used on all builds to record the melt-pool and recoater behaviour in each layer. The images were analysed by the process engineer, Sophie Treleaven, who recorded each recoater event and each melt-pool anomaly in the build log.

#### 5.6.5 Acceptance criteria

The programme had four acceptance criteria, set at the start of the programme and recorded in the programme register. A build was accepted if the wall position was within ±0.06 mm of the predicted position at all 24 control points; if no recoater collision was recorded in the in-situ images; if porosity measured by computed tomography was below 0.3% by volume in the walls; and if the fatigue coupons cut from the build met the fatigue criteria in the customer's specification, with test results from the Midshire AM Test Centre. A build that failed any criterion was analysed and the next build was revised accordingly.

### 5.7 Chronological work log: phase 1 (builds TPE-BL-401 to TPE-BL-411)

The programme's first phase covered the period from October 2024 to February 2025. Its purpose was to establish the baseline behaviour of 0.35 mm walls on the first system, to calibrate the simulation and to identify the failure modes.

**3 October 2024: TPE-BL-401.** The first calibration build. A test article of six plate-fin sections at 0.35 mm wall thickness and 40 mm height was built with the standard contour power of 280 W. Wall position was measured at 24 control points after removal from the plate. The average wall deviation was 0.19 mm, outside the target tolerance, and the simulation had predicted a deviation of 0.21 mm at the same control points. The first comparison therefore showed that the simulation at standard calibration was broadly right about the direction and magnitude of distortion at this thickness, which was encouraging for the calibration approach. Build log TPE-LB-0412 records the set-up.

**17 October 2024: TPE-BL-402.** The same geometry at 80 mm height. Wall deviation increased to 0.27 mm at the top of the build. Layer imaging showed the first evidence of wall lean in the upper third of the build. The simulation under-predicted the lean by approximately 0.05 mm.

**31 October 2024: TPE-BL-403.** The heat source parameters were adjusted to reflect the melt-pool width measured in TPE-BL-402 images. The adjusted simulation predicted the wall position at 80 mm to within 0.08 mm. The build reproduced the calibration within 0.09 mm, and the company regarded the result as a first indication that the calibration approach could work at 0.35 mm.

**14 November 2024: TPE-BL-404.** The first attempt at the 120 mm build height. At approximately 118 mm the recoater blade struck a wall that had leaned by about 0.4 mm, and the build was stopped. The recoater was cleaned and the build plate was re-levelled. The incident was analysed by the process engineer and the simulation engineer, and the collision was attributed to the cumulative lean of the walls from the lower half of the build. The simulation had not predicted the collision because the recoater interaction was not modelled. The incident was recorded in the programme register as the first recoater event. TPE-LB-0413 records the analysis.

**28 November 2024: TPE-BL-405.** The first build to be measured by computed tomography. The CT scans identified a porosity level of 0.12% by volume in the walls, well within the acceptance criterion. The scans also showed that the walls at the top of the build had a rounded cross-section which the coordinate measurement had not detected. The simulation was updated to include the rounding in the wall geometry, and the revised model reduced the predicted error in the upper part of the build.

**12 December 2024: TPE-BL-406.** A repeat of TPE-BL-404 at 120 mm height, with the recoat dwell introduced at 4 seconds per layer above the 80 mm level. The build completed without recoater contact. Wall deviation was 0.11 mm at the top, which the company regarded as a significant improvement on the 0.4 mm lean recorded on TPE-BL-404. The dwell was retained for the remainder of the programme.

**9 January 2025: TPE-BL-407.** The first build with variable contour power. The contour power for walls below 0.5 mm was reduced from 280 W to 230 W on the upper half of the build, as determined by the simulation for the local thermal history. Layer imaging showed a reduction in the melt-pool anomalies recorded in the upper third of the build. Wall deviation at the top was 0.09 mm. CT porosity was 0.14% by volume.

**23 January 2025: TPE-BL-408.** A repeat of TPE-BL-407 with the contour power reduced to 210 W in the upper half of the build. The build showed a further reduction in lean, with a wall deviation of 0.08 mm, and the company recorded that the lower power was the most effective setting tested to that point.

**6 February 2025: TPE-BL-409.** A build of 150 mm height, the tallest attempted to that date, with the 210 W contour setting. A recoater collision occurred at approximately 146 mm, on a wall that had leaned by about 0.3 mm in the top 30 mm of the build. The build was stopped. Analysis showed that the simulation had predicted the lean correctly to within 0.05 mm, and that the collision occurred because the recoat speed had not been reduced in the upper third of the build. The company recorded the recoat speed reduction as a required element of the protocol from that point.

**20 February 2025: TPE-BL-410.** The first build using the stitched island orientation. The islands within each wall were sequenced and rotated as described at section 5.6.3, and the build was run to 150 mm with the recoat speed reduction in place. No recoater collision was recorded. Wall deviation was 0.07 mm at the top, and CT porosity was 0.16% by volume. The island sequencing rule, developed by the competent professional, was confirmed as the principal source of the improvement in wall position.

**27 February 2025: TPE-BL-411.** A repeat of TPE-BL-410 with a different island sequence, to test the sensitivity of the result to the sequencing rule. The second sequence gave a wall deviation of 0.10 mm, and the company concluded that the sequencing rule was a significant contributor to the result. The sequence used in TPE-BL-410 was retained as the reference.

The phase 1 builds established the baseline behaviour of the walls on the first system, showed that the simulation could be calibrated at 0.35 mm within the limits of the measurement, identified the recoater interaction as a distinct failure mode, and produced the first scan strategy that suppressed both buckling and collision up to 150 mm.

### 5.8 Chronological work log: phase 2 (builds TPE-BL-412 to TPE-BL-422)

The second phase covered the period from March to June 2025. Its purpose was to extend the process to the full 180 mm build height, to resolve the porosity question and to confirm the process on the second system.

**12 March 2025: TPE-BL-412.** The first full-height build, at 180 mm. The wall position was within tolerance over the full height, with a maximum deviation of 0.07 mm at the top. However, CT scanning recorded a porosity level of 0.62% by volume in the walls at the level of approximately 90 mm, above the 0.3% acceptance criterion. The porosity was located in the wall edges and was associated with the reduced contour power in the mid-height region. This was the first result to show that the energy window for the contour power was bounded by a porosity limit as well as by buckling. Build log TPE-LB-0420 records the CT result.

**26 March 2025: TPE-BL-413.** A build to isolate the porosity effect. The contour power in the mid-height region was restored to 230 W while the upper-height setting was retained at 210 W. The porosity at 90 mm fell to 0.21% by volume. The wall position was unchanged, with a maximum deviation of 0.08 mm.

**9 April 2025: TPE-BL-414.** The calibration series was completed with a new heat source calibration derived from the full set of melt-pool measurements from phase 1. The simulation predicted the wall position of TPE-BL-414 to within 0.06 mm at 24 of the 24 control points, and the build reproduced the prediction to within 0.07 mm. The company recorded the calibration as sufficient for the design of the production scan strategy, and the calibration series was closed on 14 April 2025 in the programme register.

**23 April 2025: TPE-BL-415.** A build of a complete plate-fin heat exchanger section at 180 mm, with the calibrated scan strategy and the mid-height contour power of 230 W. The build was the first to be run to the full acceptance criteria. Wall deviation was 0.07 mm, porosity was 0.19% by volume, and no recoater event was recorded.

**7 May 2025: TPE-BL-416.** A repeat of TPE-BL-415 on the second system. The purpose was to test whether the process transferred between machines. The second system is fitted with a different recoater blade and a different layer-imaging camera. The wall deviation was 0.09 mm, and the company recorded a small systematic offset on the second system, which was corrected by a recalibration of the build plate height.

**19 May 2025: TPE-BL-417.** A repeat of TPE-BL-415 with the contour power in the lower third of the build reduced to 220 W, to test the energy window at the base of the wall. Porosity at the base was 0.24% by volume and the wall position was unchanged. The 220 W setting was adopted as the lower-third reference.

**28 May 2025: TPE-BL-418.** The first build with all of the revised settings together, on the first system. The build was run to 180 mm height, with the contour power set to 220 W in the lower third, 230 W in the middle third and 210 W in the upper third. The wall deviation was 0.07 mm and porosity was 0.17% by volume.

**4 June 2025: TPE-BL-419.** A build with the stitched island sequence modified to test the sensitivity of the wall position to the island rotation angle. The rotation was changed from 67 degrees to 60 degrees. The wall deviation increased to 0.10 mm, confirming that the 67 degree rotation was the value to be used.

**6 June 2025: TPE-BL-420.** A build with the recoat dwell removed in the upper third to test whether the dwell was still required with the revised scan strategy. A recoater event was recorded at 171 mm and the build was stopped. The dwell was reinstated for the production scan strategy.

**10 June 2025: TPE-BL-421.** A build at the production settings on the second system, for the purpose of confirming the process on a second machine at full height. The wall deviation was 0.07 mm and porosity was 0.15% by volume. No recoater event was recorded.

**13 June 2025: TPE-BL-422.** The final build of the development series, at production settings on the first system with the reference island sequence and the full recoat protocol. The wall deviation at all 24 control points was within ±0.07 mm, the maximum porosity measured by CT was 0.16% by volume, and fatigue coupons cut from the build met the criteria in the customer's specification when tested by the Midshire AM Test Centre. The programme register records 16 June 2025 as the date on which the uncertainties of the programme were resolved.

The company's conclusion from phase 2 was that the THINFIN process achieves wall position of ±0.07 mm on 0.35 mm Ti-6Al-4V walls over a build height of 180 mm, without internal supports, and that the process is reproducible across both laser powder-bed fusion systems at the company's site.

### 5.9 Competent professional statement

Dr Callum Ashdown is Head of Additive Manufacturing Engineering at Thistlebrook Precision Engineering Ltd. He holds an EngD in additive manufacturing process modelling and has nine years' experience of laser powder-bed fusion process development. He has worked on laser powder-bed fusion of titanium since 2016, and on the distortion of thin-walled titanium structures since 2020, first at a national additive manufacturing catapult centre and since 2022 at Thistlebrook.

Dr Ashdown was the competent professional for the THINFIN programme throughout the period. He set the technical direction of the programme, designed the phase 1 and phase 2 build plans, developed the island sequencing rule and reviewed each build result against the acceptance criteria. He is qualified to form a view on the technical questions addressed by the programme, and the view he forms is that the uncertainties described at section 5.5 could not be resolved by a competent professional using the knowledge and tools available in the field at the start of the period.

Dr Ashdown's time on the programme is recorded at 75% for the period, as set out in the cost methodology at section 6.3. The percentage was estimated at year end by the Managing Director with reference to the build logs, in which Dr Ashdown is recorded as the authoring engineer for each phase 1 and phase 2 build plan.
