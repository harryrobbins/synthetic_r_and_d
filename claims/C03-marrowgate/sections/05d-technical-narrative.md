## 5. Technical Narrative (continued)

### 5.8 Project 4: Project Conduit

#### 5.8.1 Overview

Project Conduit connects LedgerLoom to thirty banks through a single open banking aggregator. Before the project, bank feeds were connected individually, with a separate connector for each institution, and each connector was maintained by hand. Project Conduit replaces that arrangement with one aggregator integration, a canonical data model into which the transaction, balance and reference data of each bank is normalised, and a set of mapping tables that record how each bank's fields correspond to the canonical model. The project ran from 22 July 2024 to 31 December 2024. Ben Lacey, Engineer, led the integration work, with Chen Wu, Engineer, supporting the mapping tables. The integration engineering for the aggregator was carried out under a subcontract with Plaidwise Ltd, which is described in Section 6.

Connecting thirty banks is a volume problem as much as a technical one. The value of the project to LedgerLoom customers is that a finance team can connect a new bank in days rather than months, and that the data from every connected bank arrives in the same shape.

#### 5.8.2 Baseline

Connection to bank data through open banking aggregator services is established practice in financial software. Aggregators provide a common API over the account information services of many institutions, and integration with an aggregator is documented and supported by the aggregator's own tooling. Each bank nevertheless presents its transaction data with its own field conventions, date formats, reference structures and treatment of pending items, and integration engineers typically handle these differences bank by bank. The baseline is therefore an integration built institution by institution, with a bespoke mapping for each.

#### 5.8.3 Advance sought

The advance sought was a single integration in which the data from thirty banks is normalised to one canonical model, with the mapping for each bank held as data rather than as code. The advance was to achieve connectivity to all thirty banks through that one arrangement, with the normalised data sufficient for the reconciliation engine described in Section 5.3 to operate on it without bank-specific logic.

#### 5.8.4 Uncertainties

The principal uncertainty recorded for the project was whether inconsistent bank data formats could be normalised to a single canonical model without losing information needed for reconciliation. The formats differ in structure, in field semantics and in the handling of pending and reversed transactions, and the Company did not know at the start of the project whether a single model could carry all the information the reconciliation engine required from each bank.

#### 5.8.5 Methodology

The canonical data model was defined in the first quarter of the project and reviewed against the data of the first five banks to be connected. Mappings for each bank were written as tables and tested against the aggregator's sandbox environment and, once live, against each bank's own transactions in a monitored onboarding period. Where a bank's data could not be mapped to the canonical model without loss, the gap was recorded and the canonical model was extended. Sprint reviews, recorded as MSL-SR-CND-01 to MSL-SR-CND-06, governed the work.

The subcontract with Plaidwise Ltd was signed on 15 July 2024, under agreement MSL-CT-0715, and covered the engineering of the aggregator integration and the testing of connectors for the thirty banks.

#### 5.8.6 Work log

| Date | Reference | Iteration and outcome |
|---|---|---|
| 15 July 2024 | MSL-CT-0715 | Integration subcontract signed with Plaidwise Ltd. |
| 22 July 2024 | Project charter | Project opened. Canonical model drafted. |
| 12 August 2024 | MSL-SR-CND-01 | Sandbox connection established. Mapping tables for the first five banks drafted. |
| 26 August 2024 | MSL-SR-CND-02 | First bank live. Pending and reversed transactions handled through the canonical status field. |
| 23 September 2024 | MSL-SR-CND-03 | Canonical model extended to carry bank reference structures that had not been mapped. |
| 21 October 2024 | MSL-SR-CND-04 | Fifteen banks live. Onboarding monitoring reviewed. |
| 18 November 2024 | MSL-SR-CND-05 | Mapping tables consolidated. Common validation rules applied to all banks. |
| 12 December 2024 | MSL-SR-CND-06 | All thirty banks live. Project review completed. |

#### 5.8.7 Outcomes

At the end of the period, LedgerLoom was connected to thirty banks through the aggregator, with bank data normalised to the canonical model. The mapping tables for each bank were held as data, and new bank connections were made without changes to the reconciliation engine. The canonical model was extended during the project, and the extensions are recorded in the sprint review minutes.

#### 5.8.8 Boundaries

The project started on 22 July 2024, when the project charter was approved, and ended on 31 December 2024. Further banks connected after the period end, and the maintenance of the mapping tables, are outside this claim.

#### 5.8.9 Competent professional statement

The competent professional for Project Conduit is Elena Varga, Chief Technology Officer, who reviewed the canonical model and approved the mapping approach. Ms Varga confirms that the question of whether thirty banks' differing data formats could be normalised to a single model without loss of information could not be answered from existing knowledge alone, and that it was resolved through the drafting, testing and extension of the canonical model described above.

### 5.9 Summary of the technical narrative

The four projects described in this section share a common purpose: to make LedgerLoom's reconciliation, hosting and data connectivity capable of operating at the scale and with the reliability that finance customers require. Project Weft is the principal project. It addresses a question that, on the Company's assessment, could not be answered from the published art at the start of 2024, and it produced a deterministic reconciliation core whose properties were demonstrated by measurement. Projects Lumen, Stratus and Conduit are supporting projects that adapt the surrounding product, infrastructure and data connectivity to that core, and their technical content is described above in the same terms as Project Weft.

The Company's engineering leadership, through Elena Varga as Chief Technology Officer, is responsible for the technical design of each project, and each project is supported by the sprint, design and measurement records indexed in Section 7. The staff and other costs of the four projects are set out in Section 6.
