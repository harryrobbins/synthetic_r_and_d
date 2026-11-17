## 3. Additional Information Form

### 3.1 Company details

| Field | Entry |
|---|---|
| Company name | Excelcion Limited |
| Company registration number | ZZ741102 |
| Corporation tax UTR | 9999974110 |
| Registered and head office | Marlowe House, 41 Fitzroy Square, London ZZ1T 6EX |
| Company formed | 11 February 1974, as Marlowe Reddish & Partners Limited; renamed Excelcion Limited in 1999 |
| Accounting period | 1 April 2025 to 31 March 2026 |
| Size for R&D purposes | Large company |
| Scheme | Merged scheme |
| Group parent | Excelcion Group Limited (formerly Marlowe Reddish Group Limited) |
| Ultimate owner | Excelcion Trust, an employee ownership trust, through Excelcion Trustees Limited |
| Is the company a member of a group? | Yes |
| Has the company claimed R&D relief in previous periods? | Yes, in each recent accounting period |
| Has the company been subject to an HMRC enquiry into an R&D claim? | Yes, the FY2022-23 claim, closed in 2024 |

### 3.2 Company contact

| Field | Entry |
|---|---|
| Name | Scott Lam |
| Position | Head of Research and Innovation |
| Telephone | 01632 960 412 |
| Address for correspondence | Marlowe House, 41 Fitzroy Square, London ZZ1T 6EX |

### 3.3 Agent

| Field | Entry |
|---|---|
| Name of agent | Arbery Lisle LLP |
| Contact | Thomas Arbery, partner, R&D incentives team |
| Address | 9 Quorn Lane, London ZZ1 2AB |
| Telephone | 01632 960 847 |
| Agent reference | AL/EXC/2026-11 |
| Authority | Arbery Lisle LLP acts for the company on this claim and works with Group Tax on the company's side |

### 3.4 Senior officer

| Field | Entry |
|---|---|
| Name | Hamza Kent |
| Position | Chief Executive |
| Declaration | The senior officer has reviewed this Additional Information Form and the technical narrative, and has confirmed the company's position on the projects described in section 5. |

### 3.5 Connected parties and overseas activity

| Party | Relationship | Location | Involved in |
|---|---|---|---|
| Tarnbeck Modelling Services Ltd | Subsidiary, acquired 2018 | United Kingdom | P2 surrogate-model development (externally provided staff) |
| Halvorsen Pike Engineers Inc | Group company, acquired 1 November 2024 | United States | P1 evaluation of the assistant on North American design codes |
| Corrowa Rail Partners Pty Ltd | Group company, acquired 2021 | Australia | Not involved in any project in this claim |
| Tarnbeck Hydro Ltd | Subsidiary | United Kingdom | Not involved in any project in this claim |
| University of Weardale, hydrology group | Unconnected | United Kingdom | P2 benchmark datasets (subcontract) |

Overseas staff costs in this claim relate only to Halvorsen Pike Engineers Inc. They are identified in section 6 as an externally provided worker cost and are flagged as overseas.

### 3.6 Cost totals by category

| Category | Amount claimed |
|---|---:|
| Staff costs | £2,917,305 |
| Externally provided workers: connected, UK (Tarnbeck Modelling Services Ltd) | £482,000 |
| Externally provided workers: connected, overseas (Halvorsen Pike Engineers Inc) | £310,000 |
| Software: approved AI assistant enterprise licences | £540,000 |
| Data and cloud: Lighthouse platform consumption | £720,000 |
| Consumables: immersion-cooling test rig components and dielectric fluid | £38,000 |
| Subcontracted expenditure: University of Weardale hydrology group | £39,000 |
| **Total qualifying expenditure** | **£5,046,305** |

### 3.7 Per-project fields

#### P1: EDITH: an engineering reasoning engine for verified calculation checking (GF-25-014)

**Main field of science or technology.** Computer science and information systems: software engineering and the verification of calculations. Civil and structural engineering: code compliance.

**Baseline.** Structural and hydraulic calculations are checked by a second engineer against the design code. The check is slow, depends on the reviewer's experience, and is applied unevenly across a large and growing volume of calculation work. No existing tool available to the company verified calculations against design codes with a documented reliability, and the published tools the company examined could not reliably interpret free-text calculation steps.

**Advance sought.** Development of a deterministic checker that parses a calculation into a symbolic representation and re-evaluates it against code-clause rules, including Eurocode-style load combinations. The advance is the proprietary engineering reasoning capability that results from this work, and the methods used to bring the assistant into the firm's calculation workflow.

**Technical uncertainties.** Whether free-text calculation steps, as written by engineers and by the approved assistant, can be canonicalised reliably enough for symbolic re-evaluation. Whether a rule set built from a small number of code clauses extends to the range of calculations in practice. Whether the checker's output can be trusted without a second manual check.

**How and when the uncertainties were resolved.** The parse rate was measured on successive calculation sets from April 2025. The rate reached 71% of steps parsed by November 2025, against a target of 90%. The uncertainty on canonicalisation is not yet fully resolved, and work to close the gap continues. The reliability of the rule evaluation was tested against pilot calculation sets in June and July 2025.

#### P2: Machine-learning surrogate models for real-time fluvial flood forecasting (GF-24-031)

**Main field of science or technology.** Environmental engineering: hydraulics and flood risk. Computer science: machine learning, graph neural networks and scientific computing.

**Baseline.** Two-dimensional hydrodynamic models of river and floodplain behaviour take between two and six hours to run for a single event. That is too slow for operational forecasting during a flood. Machine-learning surrogates published in the literature reproduce the outputs of such models, but they fail to generalise to catchments not seen in training, and they perform poorly where embankments overtop.

**Advance sought.** A physics-informed graph surrogate, trained on 4,100 synthetic events across six catchments, that reproduces water levels at the resolution of the hydrodynamic model. The target is a root mean square error under 0.15 m on unseen events, with run times under 40 seconds per event.

**Technical uncertainties.** Whether a surrogate trained on a set of catchments generalises to unseen catchments. Whether the surrogate can represent embankment overtopping, where the flow is discontinuous. Whether the error remains within the target on defended floodplains.

**How and when the uncertainties were resolved.** A convolutional surrogate was tested from April 2025 and failed on overtopping events. A graph-based surrogate was adopted in September 2025 and validated on unseen events from November 2025 to February 2026. The target was met in four of the six catchments. Work on the remaining catchments continues in the next programme phase.

#### P3: Two-phase immersion cooling heat rejection for high-density compute halls

**Main field of science or technology.** Mechanical engineering: heat transfer and two-phase flow. Building services engineering: data centre cooling.

**Baseline.** Published correlations for boiling heat-transfer coefficients in dielectric fluids were developed at lower heat fluxes than those now proposed for high-density compute halls. At elevated rack densities the correlations diverge, and the designer has no reliable basis for sizing the heat rejection plant at the design load.

**Advance sought.** Measured boiling heat-transfer coefficients for a dielectric fluid at elevated heat fluxes, from a purpose-built test rig, and a design approach that carries those coefficients into cooling strategy selection for high-density halls.

**Technical uncertainties.** Which of the available correlations, if any, represents the measured behaviour at elevated densities. Whether the coefficients measured at rig scale apply to a full-scale immersion tank. Whether the strategy approach can be applied across the range of design loads.

**How and when the uncertainties were resolved.** The rig was commissioned in April and May 2025. Measurements were taken on test sheets XC-IMM-01 to XC-IMM-22 between July 2025 and February 2026. The divergence between correlations was confirmed in December 2025. The full-scale question remains open and is noted as an uncertainty for future work.

#### P4: Common project data model and automated project set-up (Excelcion 2030 digital programme)

**Main field of science or technology.** Computer science and information systems: data engineering, data modelling and workflow automation.

**Baseline.** Project records at Excelcion are held across several systems. Setting up a new project requires manual re-entry of client, programme, cost and design data, which takes time, introduces error and delays the start of design work. Legacy project data in Ledgerline and Keystone does not share a common structure.

**Advance sought.** A common project data model for the firm, and automated project set-up that populates a new project from that model across the Keystone ERP and the Lighthouse data platform.

**Technical uncertainties.** Whether heterogeneous legacy project data can be integrated into a single model at enterprise scale without loss of meaning. Whether automated set-up can be relied upon across the range of project types the firm delivers.

**How and when the uncertainties were resolved.** A first version of the common model was tested against legacy data from June 2025. A pilot of automated set-up ran in three business units from January 2026. The integration approach was confirmed in March 2026, and work to extend it across the firm is planned for the next period.
