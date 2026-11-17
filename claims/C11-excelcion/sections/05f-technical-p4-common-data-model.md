## 5. Technical narrative: P4 (common project data model and automated project set-up)

### 5.38 P4 overview

**Project reference and status.** P4 is carried out under the Excelcion 2030 digital programme. Its work is recorded to the Keystone project codes for the programme and to the Lighthouse delivery codes. The competent professional is Dermot McGregor, Chief Digital and Information Officer, who sponsors the programme.

**Summary.** Excelcion 2030 sets out the firm's ambition to deliver better and safer engineering, and to make its working practices more effective across the group. Digital transformation is one of its main strands. A large part of a project's early effort is spent establishing its records: the client, the programme, the cost codes, the design data, the document structure and the links between them. At present that work is carried out largely by hand, in Keystone and in the project file, and the structure of the records differs between projects and between business units. P4 sets out to create a common project data model for the firm, and to automate the set-up of a new project from that model across Keystone and Lighthouse.

### 5.39 Baseline

The baseline is the firm's practice in 2025. A new project is set up in Keystone by a project administrator, who creates the project record, assigns the cost codes, enters the client and programme data and links the project to the document structure. Design data is held in Lighthouse for analysis and in the project file for issue. Legacy project records from before the Keystone implementation are held in Ledgerline, which has been read-only since April 2021, and some of those records are still needed for live projects that began before the migration.

The set-up process takes time and introduces error. Records are entered more than once, the field definitions differ between business units, and a project that uses legacy data must be reconciled by hand. The firm's view is that automated set-up on a common model would reduce both the time and the error. It would also allow the data in Lighthouse to be used consistently across the group.

### 5.40 Advance sought

The advance sought was a common project data model for the firm, which defines the entities, relationships and field semantics of a project record in a single form, and a method for populating a new project from that model automatically across Keystone and Lighthouse. The model is intended to accept data from legacy records, so that the history of a project can be carried forward into the new structure without manual re-entry.

### 5.41 Technical uncertainties

**Uncertainty 1: integration of legacy data.** The central uncertainty is integrating heterogeneous legacy project data from Ledgerline and Keystone at enterprise scale. The project records were created over many years under different conventions. It was not known whether the records could be integrated into a single model without loss of meaning, or whether the mapping would need to be made by hand for each record type.

**Uncertainty 2: automation across project types.** The firm delivers a wide range of projects, from small design commissions to multi-year programmes. It was not known whether an automated set-up process could be relied on across that range, or whether it would need a separate procedure for each type of project.

**Uncertainty 3: scale.** Excelcion's records span many thousands of projects. It was not known whether the integration approach would work at enterprise scale, which is the level at which the model must operate to be useful.

### 5.42 Methodology

The methodology has three parts: analysis of the legacy data, design of the common model, and testing of the automated set-up.

The legacy data analysis examined the record types held in Ledgerline and Keystone, and the fields and codes used in each. The analysis produced a catalogue of fourteen record types, with the field definitions, the value sets and the relationships between them. Each record type was mapped to a candidate entity in the common model. Mappings were tested against a sample of records from each source, and the results were reviewed by the Digital Delivery team with the business units that own each record type.

The common model was designed as a set of entities and relationships, with each field given a single definition and a permitted set of values. The model is held in a versioned schema in Lighthouse. The first version was released in June 2025 and was tested against legacy data from the Ledgerline and Keystone sources. Later versions extended the model to cover design data and programme records.

The automated set-up was tested in three business units from January 2026. A project was set up by the automated process, and the result was compared with the record set up by hand for the same project. The comparison was recorded for each field, and each difference was reviewed with the business unit concerned.

### 5.43 Technical approach to integration

The integration of legacy data uses a set of transformation rules that map each source field to the common model. Where a source field maps to a single model field, the rule is a direct mapping with a value translation. Where a source field must be split or combined, the rule records the logic used. Where a source record has no equivalent in the model, the record is held in an archive table with its source reference, so that it can be retrieved if needed. The rules are versioned, and each change is reviewed by the Digital Delivery team.

The integration relies on the consistency of identifiers across the sources. Project identifiers are reconciled using the client, the programme and the start date, with a manual review step for ambiguous matches. The manual review is necessary because the same project may appear under different identifiers in the two systems, and the reconciliation is one of the main sources of uncertainty in the work.

### 5.44 Work log, P4

| Date | Iteration or event | Result recorded |
|---|---|---|
| 7 April 2025 | Keystone automation backlog reviewed. Set-up steps for a new project mapped against the Excelcion 2030 requirements. | Automation scope agreed |
| 16 June 2025 | Common project data model, version 0.1. Mapping of 14 record types from Ledgerline and Keystone to candidate entities. | Mapping coverage recorded for each record type |
| 28 July 2025 | Reconciliation of project identifiers across Ledgerline and Keystone on a sample of records. | Ambiguous matches reviewed manually |
| 18 September 2025 | Lighthouse ingestion pipeline for common model records completed for the first two record types. | Pipeline run on the sample |
| 10 November 2025 | Common model, version 0.5, adds design data and programme records. | Schema review complete |
| 14 January 2026 | Automated project set-up pilot begins in three business units. | Pilot scope and comparison method agreed |
| 25 February 2026 | Pilot comparison completed for the first business unit. Field differences reviewed. | Differences recorded and reviewed with the unit |
| 19 March 2026 | Integration approach confirmed for the common model. Extension to the wider firm planned for the next period. | Approach confirmed by the Excelcion 2030 steering group |

### 5.45 Outcome of P4 in the accounting period

At 31 March 2026 the common project data model is held in Lighthouse in a versioned schema, with fourteen record types mapped and design and programme records added. The automated set-up has been piloted in three business units, and the pilot comparison has been completed for one of them. The integration approach was confirmed in March 2026.

The outcome is that the firm has a common model that integrates legacy records into a single structure, and an automated set-up process that has been shown to work in the pilot. Uncertainty 1 is resolved for the record types in the catalogue. Uncertainty 2 is partly resolved and is being tested in the remaining two business units. Uncertainty 3 is open until the model is extended across the firm.

### 5.46 Boundaries of P4

The qualifying work on P4 is the work carried out between 1 April 2025 and 31 March 2026. Earlier work on the Keystone automation backlog and the Lighthouse platform is context and is not claimed.

Within the period, the following activities are excluded from P4 and are not claimed. The routine operation of Keystone and Lighthouse, including user support, incident response and scheduled maintenance. The ongoing hosting and storage charges of the data platform, other than the consumption described in section 6. The migration of records for live projects, where the migration is an operational task rather than a test of the model. Routine business-as-usual changes to Keystone configuration. The configuration of individual projects by administrators, outside the pilot.

The end of the qualifying work in the period is 31 March 2026. The extension of the model across the firm is planned for the next period and is not claimed.

### 5.47 Competent professional statement, P4

I, Dermot McGregor, am Chief Digital and Information Officer of Excelcion Limited. I sponsor the Excelcion 2030 digital programme and I am the competent professional for P4.

In my view the uncertainties in section 5.41 were genuine uncertainties to a competent professional in data engineering at the start of the work. The firm's legacy records had not been integrated into a common model before, and it could not be known in advance whether the integration would preserve the meaning of the records at enterprise scale, or whether an automated set-up could be relied on across the range of projects the firm delivers.

I have reviewed the work log in section 5.44 and the methodology in section 5.42. The work described is the systematic investigation of those uncertainties, and its outcome is recorded in section 5.45. I am satisfied that the work was carried out in a way that a competent data engineer would regard as an appropriate test of the uncertainties.

Signed: Dermot McGregor, Chief Digital and Information Officer
