## 3. Additional Information Form

### 3.1 Company details

| Question | Response |
|---|---|
| Company name | Marrowgate Software Ltd |
| Company number | ZZ118842 |
| Corporation tax UTR | 9999942661 |
| Registered address | 3rd Floor, 22 Cotter Street, Manchester ZZ4 7QL |
| Date of incorporation | 14 March 2018 |
| Accounting period | 1 January 2024 to 31 December 2024 |
| VAT registration | GB 999 214 873 |
| PAYE scheme reference | 999/ZZ40618 |
| Bank details for repayment | Sort code 00-00-41, account ending 6630 |
| Number of employees at period end | 41 |
| Turnover for the period | £3,100,000 |
| Is the company R&D-intensive? | No |
| Scheme claimed | SME scheme: 86% enhancement; 10% payable credit |
| Relief previously claimed | Yes, for the accounting periods ending 31 December 2022 and 31 December 2023 |

### 3.2 Contact details

| Question | Response |
|---|---|
| Name | Ruth Ashdown |
| Position | Financial Controller |
| Telephone | 07700 900142 |
| Email | r.ashdown@marrowgate.example |
| Correspondence address | As registered address above |

### 3.3 Agent

| Question | Response |
|---|---|
| Agent firm | Vantrell Innovation Ltd |
| Agent contact | Dominic Pryce, Director |
| Agent address | Unit 4, Halvard Yard, Leeds ZZ2 1AB |
| Fee basis | Contingent, at 18% of the relief finally received |
| Authorisation | Agent authorised to act for the company in relation to this claim |

### 3.4 Senior officer

| Question | Response |
|---|---|
| Name | Oliver Marrow |
| Position | Chief Executive Officer and director |
| Responsibility for the claim | Approved the scope of each project, reviewed the claim and makes the director's declaration in Section 7 |

### 3.5 Competent professional

| Question | Response |
|---|---|
| Name | Elena Varga |
| Position | Chief Technology Officer |
| Qualifications | MSc in Distributed Systems |
| Prior experience | Staff engineer at a payments company, Tallowfield Payments Ltd |
| Role in the claim | Technical lead for Projects Weft, Stratus and Conduit, and the competent professional for all four projects |

### 3.6 Cost totals by category

| Category | Claimed |
|---|---:|
| Staff costs | £576,081 |
| Externally provided workers (unconnected) | £62,400 |
| Software | £38,600 |
| Data and cloud | £184,000 |
| Subcontract (UK, unconnected) | £19,500 |
| **Total qualifying expenditure** | **£880,581** |

### 3.7 Projects

The company has four projects for this period. The fields below are completed for each project in the same form. Technical detail is in Section 5.

#### 3.7.1 Project 1: Project Weft

**Main field of science or technology.** Computer science: distributed systems and data management, specifically event-sourced deterministic reconciliation.

**Baseline.** The established baseline for bank-to-ledger reconciliation is rule-based matching on amount, date and reference, with fuzzy tolerances and a manual exceptions queue. Such systems are order-dependent: the same bank and ledger events can yield different matches depending on arrival order. Re-issued bank transactions with changed identifiers are usually treated as new items, which creates duplicates or orphaned matches. Event sourcing and CRDT-style merge techniques are well documented, but no known approach at the start of the project gave a deterministic, replayable match result when upstream feeds re-issue transactions with mutated identifiers and partially settled splits, at the throughput and latency that LedgerLoom requires.

**Advance sought.** A reconciliation engine whose output is a deterministic function of the set of events received, independent of arrival order and duplication, with every match traceable to its derivation. The advance has three elements: lineage-aware merge semantics that tolerate identifier mutation without losing audit history; a two-phase match protocol that uses compensating events rather than in-place updates; and sustained throughput of approximately 50,000 events per second with p99 commit latency under 200 milliseconds.

**Uncertainties.** (1) Whether a deterministic merge function exists that preserves auditability when identifiers are mutated after the fact. (2) Whether probabilistic candidate scoring can complete inside the commit path within the latency budget.

**How and when the uncertainties were resolved.** Uncertainty 1 was resolved through a replay harness, property-based tests and three rejected designs, with determinism confirmed on 13 December 2024. Uncertainty 2 was resolved through benchmark runs on 15 July, 18 September and 14 October 2024. Evidence references are given in Section 5 and indexed in Section 7.

#### 3.7.2 Project 2: Project Lumen

**Main field of science or technology.** Computer science: human-computer interaction and front-end engineering.

**Baseline.** The reconciliation workspace was built on an earlier component kit, with inconsistent interaction patterns across screens. Standard practice is to redesign such screens using an established component library and to surface unmatched items through filters and tables. Generated explanations are a known capability of large language model APIs, but their use within a finance reconciliation workflow was not established practice at the start of the project.

**Advance sought.** A new React component library and redesigned workspace, together with a smart suggestions panel that calls a third-party large language model API to explain why an item remains unmatched and to suggest next steps.

**Uncertainties.** (1) Whether users would trust AI-generated explanations of unmatched items. (2) Achieving a seamless, intuitive experience across the full reconciliation workflow, given the density of information on each screen.

**How and when the uncertainties were resolved.** Both uncertainties were addressed through sprint reviews and user sessions held during the period. The redesigned workspace was released to beta customers on 28 October 2024, and the project ended on 30 November 2024. See the Project Lumen section of Section 5 and sprint review records MSL-SR-LUM-01 to MSL-SR-LUM-09.

#### 3.7.3 Project 3: Project Stratus

**Main field of science or technology.** Computer science: cloud computing and distributed infrastructure.

**Baseline.** LedgerLoom was hosted on virtual machines managed by configuration scripts. Migration of hosted software to container orchestration, using infrastructure-as-code, is a widely practised approach. The company's baseline was a single shared environment with limited isolation between customer tenants.

**Advance sought.** A re-architecture of the LedgerLoom hosting estate onto Kubernetes on AWS, with Terraform-managed infrastructure, a unified observability stack and a bespoke tenant-sharding scheme that places tenant data partitions onto node pools according to residency and load. The advance sought is a migration of live tenants with zero customer-visible downtime.

**Uncertainties.** Whether the platform could achieve zero-downtime migration of live tenants, given the stateful nature of the reconciliation store.

**How and when the uncertainties were resolved.** Through sprint reviews and the three tenant migration cohorts carried out between June and December 2024. The final cohort was migrated on 19 December 2024. See the Project Stratus section of Section 5 and sprint review records MSL-SR-STR-01 to MSL-SR-STR-08.

#### 3.7.4 Project 4: Project Conduit

**Main field of science or technology.** Computer science: data integration and financial services software.

**Baseline.** Connection to bank data through open banking aggregator services is established practice. Each bank presents transaction data in its own format and with its own field conventions, and integration is usually carried out bank by bank.

**Advance sought.** Connectivity to thirty banks through a single aggregator integration, with a canonical data model that normalises transaction, balance and reference data from each bank into the LedgerLoom event schema.

**Uncertainties.** The principal uncertainty was whether bank data formats, which differ in structure and field semantics between institutions, could be normalised to a single canonical model without loss of information needed for reconciliation.

**How and when the uncertainty was resolved.** Through sprint reviews and integration testing with each bank as it was connected. The first bank went live on 26 August 2024 and all thirty banks were live on 12 December 2024. See the Project Conduit section of Section 5 and sprint review records MSL-SR-CND-01 to MSL-SR-CND-06.

### 3.8 Declaration

The information in this form is given on behalf of Marrowgate Software Ltd. The director's declaration is set out in Section 7.
