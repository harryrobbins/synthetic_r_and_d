### 5.10 Chronological work log, QH-LOWIR: first half of 2025

The work log below records each dated iteration of QH-LOWIR in the first half of the period. Each entry gives the MEA build identifier, the design change tested, the principal result and the evidence reference. Evidence references are to the laboratory notebook (QHL-LB series), test data exports (QHL-TD series) and project tickets (QHL-JR series), which are indexed at Appendix 7.2.

Builds MEA-001 to MEA-011 were made during 2024 and are part of the baseline described in section 5.3. Those builds are not claimed. Work in 2025 begins with MEA-012.

#### 5.10.1 January 2025

The project plan for QH-LOWIR was approved on 6 January 2025 (QHL-JR-2201). It set out the target loading below 0.2 mg/cm², the target degradation below 10 µV/h at 2 A/cm², the three uncertainties described in section 5.5, and the test protocol described in section 5.6.

On 8 January the first build of the period, MEA-012, was made with a two-step graded catalyst layer on the Company's standard titanium PTL, using the ionomer designated IF-3. The total loading was 0.31 mg/cm². The build was tested from 10 January under the conditioning sequence and then under a dynamic profile at 2 A/cm². The degradation rate after 100 hours was 14.2 µV/h, which confirmed the baseline behaviour of uncoated titanium: the contact resistance rose steadily from around 180 hours (QHL-LB-0412, QHL-TD-0412).

MEA-013, built on 15 January, used a three-step grading with the same loading as MEA-012 at the outer steps and a higher loading at the membrane interface. It was intended to test whether a stronger activity gradient reduced the degradation rate. The degradation rate was 11.6 µV/h. The improvement was real but insufficient, and the test showed that the catalyst layer alone could not control the PTL interface (QHL-LB-0418).

On 20 January the Company began a design review of the PTL interface, led by Dr Nadia Fenwick. The review concluded that a coating on the PTL was necessary, and that the coating would need to be tested in the first instance on the same catalyst layer used in MEA-013 so that the effect could be separated from the effect of the layer (QHL-JR-2214).

#### 5.10.2 February 2025

The dynamic load emulator at the Tyneford stack test facility was commissioned on 3 February. The emulator reproduces the current profile recorded from the Company's pilot customer's renewable supply, scaled to the single-cell active area. From this date all dynamic tests on QH-LOWIR used the emulator in preference to the earlier step-change profile, which had been used in 2024 and which the Company considered to under-represent the transients of renewable supply (QHL-LB-0424).

MEA-014 was built on 6 February using the three-step layer from MEA-013 on a PTL with a first-generation coating. The coating was a thin conductive oxide film. The degradation rate under the emulator profile was 8.9 µV/h at a total loading of 0.27 mg/cm². This was the first build of the period to fall below the 10 µV/h threshold, although the loading remained above the 0.2 mg/cm² target. The result was attributed to the coating, which reduced the rise in contact resistance seen in MEA-012 and MEA-013 (QHL-TD-0427).

Between 12 and 20 February the Company built MEA-015 and MEA-016 to test the ionomer. Dr Sun-Hee Park found that IF-3 showed adhesion loss at loadings below 0.25 mg/cm², visible in the cross-section images from the scanning electron microscope as a separation between the catalyst layer and the membrane at the outer step. A reformulation designated IF-4 was prepared, with a higher proportion of the sulfonated backbone (QHL-LB-0431, QHL-LB-0436).

#### 5.10.3 March 2025

MEA-017, built on 4 March, was the first build with IF-4. The loading was 0.22 mg/cm². The adhesion problem was no longer visible in the cross-section, and the degradation rate was 7.7 µV/h over 600 hours. The proton resistance at 2 A/cm² was 12% lower than in MEA-014. The result was reported to the Board at its meeting of 11 March, where the Company's position was recorded that the ionomer reformulation was a material step in the advance (QHL-MIN-0311).

Between 17 and 28 March the Company built MEA-018 and MEA-019 on a second-generation coated PTL. This coating was a thicker film with a higher proportion of conductive dopant. Both builds were tested for 500 hours. The degradation rates were 6.4 µV/h and 6.9 µV/h respectively, but the impedance data for both builds showed a slow increase in the high-frequency resistance after 300 hours, which Dr Joel Abernethy interpreted as an early sign of passive oxide formation at the PTL interface. The interpretation was not confirmed at this stage, and the post-test characterisation was scheduled for the next review (QHL-LB-0449, QHL-TD-0455).

#### 5.10.4 April 2025

MEA-020 to MEA-022 were built between 7 and 25 April. These builds combined the IF-4 ionomer, the second-generation coating and the three-step layer at a loading of 0.24 mg/cm². MEA-021 was run for 1,000 hours. Its degradation rate over that period was 5.8 µV/h, which was the lowest measured to that date for a build at this loading. The Company judged the result to be a significant step towards the target, and the loading was reduced in the following builds.

The XPS analysis of MEA-022 was requested from the University of Tyneford on 24 April, following the earlier observation in the impedance data. The request was made to establish whether the PTL interface had oxidised after test, since the impedance data could not distinguish between a change in the coating and a change in the catalyst layer (QHL-JR-2246).

#### 5.10.5 May 2025

The XPS report for MEA-022 was received on 9 May 2025 (QHL-AN-0509). It identified a titanium oxide film at the PTL interface, of a thickness and oxidation state consistent with passive oxide formation, on the area of the PTL beneath the outer step of the catalyst layer. The film was not present on the area beneath the inner step, which had been protected by the ionomer. The report therefore identified passivation of the titanium PTL at the interface as the failure mode behind the slow rise in high-frequency resistance seen in MEA-018, MEA-019 and MEA-022.

The finding was reviewed on 14 May at a technical meeting chaired by Dr Nadia Fenwick. The meeting concluded that the second-generation coating did not fully protect the titanium at the outer step, where the local potential and the current density were highest. This conclusion was recorded as a failure mode of the coating, and the coating was placed on the list of items for redesign (QHL-JR-2261, QHL-MIN-0514).

The passivation failure was identified in May 2025 and was the first of the failure modes seen in the programme that had not been anticipated in the project plan. It changed the direction of the work for the rest of the period, because the graded layer could not be optimised further until the PTL interface was stable.

#### 5.10.6 June 2025

Between 2 and 13 June the Company built MEA-023 to MEA-025 to test candidate coatings intended to address the passivation. Three approaches were tested: an increased thickness of the existing coating, a coating doped with niobium, and a bilayer with a conductive oxide underlayer. The bilayer was tested first, on MEA-023, and showed high initial resistance that did not decline during the conditioning sequence. It was discarded on 16 June.

The niobium-doped coating was tested on MEA-024 and MEA-025, built on 10 and 13 June. Both were tested for 300 hours under the emulator profile. The degradation rates were 6.1 µV/h and 5.9 µV/h, and the post-test XPS analysis of MEA-024 showed no passive oxide at the outer step (QHL-AN-0621). The niobium-doped coating was the candidate taken forward.

On 27 June the Company decided to proceed with the niobium-doped coating as the basis of the coated PTL for the remainder of the period. This decision is recorded in the project ticket QHL-JR-2274, and it is the reason for the change of coating described in the second half of the work log.
