## 5. Technical Narrative

### 5.1 Introduction and structure

This section sets out the technical case for the two projects undertaken by Quillon Hydrogen Ltd in the accounting period 1 January 2025 to 31 December 2025. It follows the structure recommended in the DSIT Guidelines on R&D tax relief. For each project it states the baseline, the advance sought, the scientific and technological uncertainties, the methodology adopted to resolve them, a dated work log, the outcomes achieved, and the boundaries of the project in time.

The first project, QH-LOWIR, is the principal project and accounts for the large majority of the Company's R&D effort in the period. The second project, QH-DYNA, is smaller in scope but is a genuine project with its own advance and uncertainties, and is described in section 5.15 below.

Work on both projects began before the start of the period. Where this section refers to earlier work, it does so to establish the baseline and the state of knowledge at the start of 2025. Only work carried out within the period is claimed, and the boundaries are stated for each project.

### 5.2 Background to electrolyser catalysis

A proton exchange membrane electrolyser splits water into hydrogen and oxygen using an electric current. The membrane conducts protons from the anode to the cathode. At the anode, water is oxidised to oxygen, a reaction that is kinetically slow and that requires a catalyst. Iridium oxide is the catalyst of choice for PEM anodes because it combines reasonable activity with resistance to the strongly oxidising, acidic conditions in the anode. It is also among the scarcest of the platinum-group metals, and its supply is concentrated in a small number of producers.

The anode catalyst layer is deposited on a porous transport layer (PTL), which carries current from the bipolar plate to the membrane and carries water and oxygen away from the catalyst. The PTL is typically a sintered titanium material. Under the oxidising conditions at the anode, titanium is prone to forming a passive oxide layer that increases the electrical resistance at the PTL interface. Maintaining low and stable contact resistance between the PTL and the catalyst layer is therefore one of the central problems of PEM electrolyser design.

The catalyst layer is bonded to the membrane and combined with the cathode in a membrane electrode assembly (MEA). The ionomer, a perfluorosulfonic acid polymer, binds the catalyst particles together and provides the proton pathway within the catalyst layer. The ionomer and the catalyst interact at the surface of the iridium particles, and this interaction governs both the proton conductivity of the layer and the accessibility of the catalyst to the electrolyte.

### 5.3 Baseline

The commercial baseline for PEM anodes is well established. Commercial stacks currently use anode iridium loadings of between 1 and 2 mg/cm². At these loadings the catalyst layer is thick enough to provide a durable electrical and proton pathway, and degradation under dynamic load is adequately controlled for the operating life that commercial customers specify.

The published research baseline for low-loading anodes is less settled. Two families of approach have been reported in the literature. The first places iridium on doped titanium dioxide supports, which allows a much smaller quantity of iridium to be dispersed over a larger surface area. The second uses thin-film nanostructured catalysts, in which the iridium is deposited as a very thin, high-area structure. Both approaches reduce the iridium loading substantially. However, in the published accounts available to the Company at the start of 2025, both showed degradation rates above 30 µV/h under dynamic load. The degradation was attributed in the literature to two mechanisms: dissolution of the support material, and loss of contact between the catalyst layer and the PTL.

The Company therefore identified the baseline for QH-LOWIR as follows. A commercially acceptable anode is one with an iridium loading of 1 to 2 mg/cm² and a degradation rate that is low enough to meet the customer's warranty over the stack life. A low-loading anode published in the research literature has an iridium loading below 0.2 mg/cm² but has degradation above 30 µV/h under dynamic load. No published approach combined a loading below 0.2 mg/cm² with degradation below 10 µV/h at 2 A/cm² under dynamic conditions.

The Company's own preliminary work in 2024 confirmed the picture in the published accounts. Its first low-loading samples, built with a commercial support, showed degradation above the published threshold within the first several hundred hours of test. The Company therefore concluded at the start of 2025 that the target combination could not be reached by combining existing approaches, and that a new approach was required.

### 5.4 Advance sought

The advance sought by QH-LOWIR is a graded catalyst layer deposited on a coated porous transport layer, with interface engineering that keeps the contact resistance between the PTL and the catalyst layer stable over the operating life of the stack.

The graded layer varies the iridium loading and the ionomer content through the thickness of the catalyst layer. The loading is highest at the interface with the membrane, where the proton pathway and the electrochemical activity are concentrated, and lowest at the interface with the PTL, where the requirement is for electrical contact and mechanical stability. The intention is that the total loading is kept below 0.2 mg/cm² while the activity and durability of the layer are maintained.

The coated PTL is the second element of the advance. The Company has developed a coating for the titanium transport layer that is intended to prevent passive oxide formation at the PTL interface while remaining electrically conductive. The coating is applied before the catalyst layer is deposited and is designed to keep the interface resistance stable through the lifetime of the stack.

The combination is the advance. Neither the graded layer nor the coated PTL alone is novel in the literature in general terms. The advance lies in combining them at low loading so that the durability target is met under dynamic load, which the baseline shows is not achieved by the approaches that are published.

### 5.5 Scientific and technological uncertainties

At the start of 2025 the Company identified three principal uncertainties that could not be resolved from the published literature or from the Company's existing knowledge.

**Uncertainty 1: the dissolution mechanism under renewable load profiles.** The published degradation mechanisms were established under constant or step-change load. Renewable electricity supply produces load profiles that vary continuously, with rapid transients and periods at low current. The Company did not know whether the dissolution mechanism that governs support degradation under constant load would dominate under these profiles, or whether a different mechanism would take over. The answer determines which material properties must be controlled to meet the durability target.

**Uncertainty 2: survival of the PTL coating.** The coating that the Company proposed to apply to the PTL had not been tested over long durations at the current densities of interest. It was not known whether the coating would survive the combined effects of oxidation, mechanical stress from compression and gas evolution, and the electrochemical potentials at the anode. A coating that delaminated or cracked would expose the titanium and allow the passive layer to form.

**Uncertainty 3: ionomer-catalyst interaction at low loading.** At higher loadings, the ionomer can be distributed through the catalyst layer in a manner that is relatively insensitive to the detailed arrangement of catalyst particles. At low loading, the catalyst particles are sparser and the ionomer must bind to a smaller surface. It was not known whether the ionomer formulations used at higher loadings would provide adequate proton conductivity and adhesion at 0.2 mg/cm² or below, or whether the ionomer would need to be reformulated, and if so, how the reformulation would interact with the graded structure.

These uncertainties were recorded in the Company's project plan dated 6 January 2025, which is available in the evidence index at Appendix 7.2.

### 5.6 Methodology

The Company adopted a build-test-analyse methodology. Each iteration of the design was implemented as a numbered MEA build, from MEA-012 onwards for the period, with each build recorded in the laboratory notebook and assigned a unique identifier. Each build was tested in a single-cell test station under a defined protocol, and the results were analysed to decide the next iteration.

The test protocol had three elements. The first was a conditioning and polarisation sequence, used to establish the baseline electrochemical performance of each build at the start of test. The second was a dynamic load profile derived from the renewable supply data described in section 5.5, applied at 2 A/cm² for periods of up to 2,000 hours. The third was a set of electrochemical impedance spectroscopy measurements taken at regular intervals to track changes in the contact and charge transfer resistances. Degradation was measured as the rate of voltage increase at constant current, expressed in µV/h, after the first 100 hours of operation to remove the initial conditioning effect.

Surface and structural characterisation was carried out on selected builds at the start and end of test. The University of Tyneford provided XPS analysis of the catalyst surface, which identifies the oxidation state of the iridium and the chemical state of the support and coating. The Company's own scanning electron microscope was used for cross-section imaging of the catalyst layer and the PTL interface.

Accelerated stress tests (AST) were used to explore the failure modes more rapidly than the standard protocol allowed. The AST protocol applied repeated potential cycles, with high upper potentials, to the MEA, and was designed to drive support dissolution and PTL passivation in a time-compressed manner. The AST protocol was specific to the Company's cell geometry and to the targeted loading, and is described in more detail in section 5.12.

Each iteration was judged against three criteria: the degradation rate at 2 A/cm², the contact resistance measured by impedance, and the post-test characterisation of the catalyst layer. An iteration was taken forward only if it improved one of these criteria without degrading another. Iterations that failed were analysed to identify the cause of failure before the next build was designed.

### 5.7 Iterative design approach

The graded catalyst layer was developed through a series of variations on the layer structure: the number of grading steps, the loading at each step, the ionomer content at each step, and the method of deposition. The coated PTL was developed in parallel through variations of the coating composition, the coating thickness and the coating process. Two streams of work were run together, with the results of each stream feeding into the design of the other, because the performance of the graded layer depends on the properties of the PTL interface, and the interface properties depend on the catalyst layer that is deposited on them.

Ionomer formulations were developed by Dr Sun-Hee Park in parallel with the layer structure work. Each formulation was assessed for its proton conductivity and adhesion at the loading of the build in which it was used. Reformulations were introduced where the earlier formulation showed poor adhesion at low loading, and the effect of each reformulation on the durability of the layer was assessed in the following builds.

Dr Joel Abernethy led the electrochemical characterisation. His analysis of the polarisation and impedance data for each build formed the basis for the decision on the next iteration, and the interpretation of the dynamic test data was carried out under his direction and reviewed by the competent professional.

### 5.8 Use of the University of Tyneford

The University of Tyneford provided XPS analysis on a fee basis for selected MEA builds. The analysis was used to determine the oxidation state of the iridium at the surface of the catalyst layer after test, and to confirm whether the coating on the PTL remained intact. The analysis results were used directly in the interpretation of the failure modes described in section 5.10. The University had no role in the design of the MEAs or in the interpretation of the claim, and is not connected to the Company.
