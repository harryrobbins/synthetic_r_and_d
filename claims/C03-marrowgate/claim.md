> SYNTHETIC TEST DATA – FICTIONAL COMPANY – PREPARED FOR HMRC HACKATHON – NOT A REAL TAX CLAIM

## 1. Cover Sheet and Claim Summary

| Field | Detail |
|---|---|
| Claimant | Marrowgate Software Ltd |
| Company number | ZZ118842 |
| Corporation tax UTR | 9999942661 |
| Registered and trading address | 3rd Floor, 22 Cotter Street, Manchester ZZ4 7QL |
| Accounting period | 1 January 2024 to 31 December 2024 |
| Relief claimed | Research and development tax relief, SME scheme |
| Enhancement rate | 86% |
| Payable credit rate | 10% (company not R&D-intensive) |
| Projects claimed | Four: Project Weft, Project Lumen, Project Stratus, Project Conduit |
| Agent | Vantrell Innovation Ltd |
| Senior officer | Oliver Marrow, Chief Executive Officer |
| Competent professional | Elena Varga, Chief Technology Officer |
| Date of claim | 14 October 2026 |

### Claim summary

| Item | Amount |
|---|---|
| Total qualifying expenditure | £880,581 |
| Extra deduction (86%) | £757,300 |
| Surrenderable loss | £1,637,881 |
| Payable credit (10%) | £163,788 |
| Trading loss before R&D deduction | £1,450,000 |
| Company turnover for the period | £3,100,000 |

Marrowgate Software Ltd ("Marrowgate" or "the Company") is a business-to-business financial technology company based in Manchester. Founded in 2018, it provides LedgerLoom, a software-as-a-service platform that automates reconciliation for mid-market finance teams. LedgerLoom connects bank feeds, enterprise resource planning systems and payment processor settlement reports into a single auditable ledger, so that finance staff can see, at any moment, which bank movements correspond to which invoices, payments and journals. The Company employed 41 people at the end of the period and reported turnover of £3.1 million.

This claim covers the Company's research and development activity during calendar year 2024. Four projects are claimed. Project Weft is the principal project and is the subject of the most detailed technical narrative in Section 5. It addresses a problem that, to the Company's knowledge at the start of the project, was not solved in the published literature or in commercial practice: producing a reconciliation result that is a deterministic, replayable function of the events received, when upstream bank feeds re-issue transactions with mutated identifiers and when a single bank credit settles several ledger items in part. Project Weft met its technical success criteria during the period, sustaining approximately 50,000 events per second with a p99 commit latency below 200 milliseconds.

Projects Lumen, Stratus and Conduit are supporting projects. Project Lumen is a redesign of the reconciliation workspace, using a new React component library and a suggestions panel that draws on a third-party large language model API to explain unmatched items. Project Stratus is the re-architecture of the LedgerLoom hosting estate from virtual machines onto Kubernetes on AWS, including a bespoke tenant-sharding scheme. Project Conduit is the connection of LedgerLoom to thirty banks through a single open banking aggregator, using a canonical data model for bank transaction formats.

Qualifying expenditure is set out by category in Section 6, and the supporting records are indexed in Section 7. The Company has claimed relief in each of the two previous accounting periods, so a Claim Notification Form is not included (Section 2). The director's declaration is made by the Chief Executive Officer.

---

## 2. Claim Notification Form

A Claim Notification Form (CNF) is not included in this claim pack, because one was not required for this accounting period.

Marrowgate Software Ltd notified its research and development activity on a CNF for its first claim, which related to the accounting period ending 31 December 2022, and has claimed relief in each subsequent accounting period, including the period ending 31 December 2023. The company has therefore been claiming without interruption, and the activity described in this claim is a continuation of the activity notified in those earlier claims. The reconciliation engine that forms the subject of Project Weft was the same LedgerLoom reconciliation core described in the 2023 claim, and the work carried out in 2024 extends that core rather than starting a new area of activity.

The company's notification position for the period is therefore that a further CNF is not required. The Company's agent, Vantrell Innovation Ltd, has confirmed this position against the notification rules in force for the period, and the company has no record of any change of trade, change of ownership or change of accounting reference date that would give rise to a new notification obligation.

Copies of the 2022 and 2023 claim submissions are held on the Company's files and are available to HMRC on request. The Company's Chief Executive Officer, Oliver Marrow, is the named contact for any notification queries.

---

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

---

## 4. Company Background

### 4.1 Overview

Marrowgate Software Ltd was incorporated on 14 March 2018 by Oliver Marrow and a small group of former colleagues from a Manchester-based payments business. The Company builds and operates LedgerLoom, a software-as-a-service platform for automated reconciliation. Its customers are mid-market finance teams, typically in organisations with between 200 and 2,000 employees, that need to match large volumes of bank movements against invoices, payments, payroll and journal entries every day.

The Company's central proposition is that reconciliation should be automatic, complete and auditable. Finance teams should not have to choose between speed and control. LedgerLoom connects three types of input: bank feeds, which arrive from many institutions in many formats and at irregular times; enterprise resource planning (ERP) systems, from which invoices, payments and journals are posted; and payment processors, whose settlement reports describe how card and digital payments are paid out, often net of fees and in batches. The platform brings these together into a single event-sourced ledger, and matches the events it holds into a reconciliation graph that customers can inspect at any point.

LedgerLoom has been commercially available since 2019. It is used by customers in the United Kingdom, Ireland and the Netherlands. The Company's revenue is recurring and subscription-based, with customers paying for the number of bank accounts and ERP connections they use.

### 4.2 History

The Company began as a consultancy engagement for a regional wholesale business, building a bespoke reconciliation script to match its bank statements against its sales ledger. That engagement established the core idea of matching bank events to ledger postings by means of an immutable event log. Oliver Marrow and the founding engineers turned the script into a product, and the first commercial release of LedgerLoom was made in 2019.

Elena Varga joined the Company in 2019 as Head of Engineering, and was appointed Chief Technology Officer in 2021. Her background includes an MSc in Distributed Systems and several years as a staff engineer at a payments company, Tallowfield Payments Ltd, where she worked on settlement and reconciliation services for high-volume card acquiring. Kwame Asante joined in 2020 as a senior engineer and is now Principal Engineer responsible for the ledger core.

In 2021 and 2022 the Company's growth was focused on onboarding customers and extending the number of ERP and bank connections. From 2022 the Company's engineering effort moved towards the deeper problems of determinism, scale and multi-tenant operation, which form the basis of the projects in this claim.

### 4.3 Ownership

The Company's issued share capital is held as follows.

| Shareholder | Holding |
|---|---:|
| Fenwick Growth Partners LLP (Series A lead, 2023) | 44% |
| Oliver Marrow | 28% |
| Elena Varga | 9% |
| Other institutional and employee shareholders | 19% |
| **Total** | **100%** |

Fenwick Growth Partners LLP is an independent venture capital investor. It holds no board seat in its own name but nominates one non-executive director. The Company is not a member of a group and has no subsidiaries, associated companies or joint ventures.

### 4.4 Funding

The Company raised a Series A round of £9 million in 2023. The round was led by Fenwick Growth Partners LLP and funded product development, the expansion of the engineering team and the growth of the customer base in the Netherlands. Before the Series A, the Company was funded through a seed round in 2020 and through revenue. The Company has not received grant funding for its research and development activities and has not received any state aid other than the relief claimed in this pack and in previous claims.

The Company has been loss-making in each year since incorporation. Its losses reflect continued investment in engineering, the cost of hosting customer data and the cost of selling into the mid-market. The trading loss for the period is stated in Section 6.

### 4.5 Staff and organisation

At the end of the period the Company employed 41 people, organised into four functions.

| Function | Headcount |
|---|---:|
| Engineering (including platform, data and DevOps) | 22 |
| Product and design | 4 |
| Customer success and implementation | 9 |
| Finance, people and operations | 6 |
| **Total** | **41** |

The engineering function is led by Elena Varga as Chief Technology Officer. Kwame Asante leads the ledger core, Rosie Tamworth leads the platform and tenant services, and Sam Okoro leads DevOps and the hosting estate. The product function is led by Jessica Harrow as Product Manager, who maintains the LedgerLoom roadmap and works closely with customers and engineers on the design of new capabilities. Oliver Marrow, as Chief Executive Officer, sets the Company's strategy and takes responsibility for its commercial and research direction.

The Company operates a hybrid working model. Most staff work from the Manchester office at 3rd Floor, 22 Cotter Street, with some engineers working remotely from elsewhere in the United Kingdom. The Company uses external contract developers through an agency, Northgate Contract Resourcing Ltd, to supplement its engineering capacity for defined pieces of work.

### 4.6 Facilities

The Company occupies the third floor of 22 Cotter Street, Manchester, on a lease that runs to 2029. The office accommodates the engineering, product and customer teams and includes a dedicated lab room for the replay and benchmark infrastructure described in Section 5. That room houses a set of physical machines used for performance testing, which the Company operates alongside its cloud environments.

Production hosting for LedgerLoom runs on AWS, in the London region, and is managed by the DevOps team. Non-production environments, including the replay harness and the benchmark clusters, also run on AWS. The Company has no data centre of its own.

### 4.7 Research and development history

The Company has claimed research and development relief for the accounting periods ending 31 December 2022 and 31 December 2023. Both claims were prepared with the assistance of Vantrell Innovation Ltd. The 2023 claim related to the early development of the deterministic ledger core, which is the foundation for Project Weft. The Company's engineering roadmap has been organised around that core since 2022, and the work described in this claim continues the same line of development.

The Company maintains an engineering notebook system, in which engineers record experiments, design decisions, measurements and outcomes on dated pages. Jira is used to track work items, and sprint reviews are held every two weeks for each product area. Design notes and architecture decision records are kept in the Company's document repository. The records referred to in Section 5 are indexed in Section 7.

### 4.8 Summary

Marrowgate is a Manchester-based software company with a clear product, a growing customer base and a sustained programme of engineering investment. Its research and development in 2024 was focused on the question of how a financial ledger can be both fast and fully deterministic, and on the connected problems of operating that ledger safely across many tenants and many banks. The sections that follow describe that work in detail.

---

## 5. Technical Narrative

### 5.1 Purpose and structure

This section sets out the technical work carried out by Marrowgate Software Ltd ("the Company") during the accounting period 1 January 2024 to 31 December 2024. It is organised project by project. Each project section follows the same headings: overview, baseline, advance sought, uncertainties, methodology, work log, outcomes, boundaries and competent professional statement. Project 1 (Project Weft) is described in three parts, 5.3, 5.4 and 5.5, because it is the Company's principal project and the one on which the claim relies most heavily. Projects 2, 3 and 4 are described in Sections 5.6, 5.7 and 5.8.

Technical references are to Jira work items (for example WEFT-112), design notes (for example MSL-DN-0003), architecture decision records (for example MSL-ADR-014), engineering notebook pages (for example MSL-EN-0412), benchmark reports (for example MSL-BM-0021) and sprint review minutes. All references are indexed in Section 7.

### 5.2 Context: the LedgerLoom platform

LedgerLoom is built around an append-only event log. Every fact that enters the system, whether a bank transaction observed by a feed, a settlement split reported by a payment processor, an invoice posting from an ERP system or a manual journal entered by a customer, is recorded as an immutable event with a source identifier, a sequence number within that source, a timestamp supplied by the source and a timestamp of receipt. Events are partitioned by tenant and by bank account or ledger account. Nothing in the event log is updated or deleted. Corrections are represented as new events that refer to the events they correct.

On top of the event log sits the reconciliation layer. Its job is to take the events in each partition and produce a reconciliation graph: a set of matches between bank-side items and ledger-side items, with each match carrying the amounts matched, the rule or model that proposed it and the events from which it was derived. Finance teams act on that graph. An unmatched bank item becomes an exception; a matched item is cleared; a partially matched item shows the residual amount still to be explained.

Reconciliation is harder than it looks for three reasons that recur throughout this section.

First, bank feeds are not stable. A transaction that appears as pending may later be posted under a different identifier, with a changed reference string or with its amount adjusted for fees. Feeds also re-issue transactions after corrections, sometimes weeks later, and the re-issued record may not be recognisably the same item to a simple matching rule.

Second, settlement is not one-to-one. A single bank credit from a payment processor may settle dozens of customer payments, net of fees and chargebacks, and the processor's settlement report, which arrives separately, is the only source that explains how the credit breaks down. A ledger item may likewise be settled in several bank payments over time.

Third, events arrive out of order and sometimes more than once. Two feeds may report the same transaction. A settlement report may arrive before the bank credit it describes, or after it. Any reconciliation result that depends on arrival order is, for a finance team, a result they cannot defend to an auditor, because re-running the same process on the same data may produce a different answer.

The Company's engineering goal, from 2022 onwards, was therefore to make the reconciliation layer a deterministic function of the set of events it holds. Given the same set of events, in any order and with any duplication, the reconciliation graph must be identical, and every edge in it must be traceable to its derivation. Project Weft is the 2024 programme of work to deliver that property at production scale.

### 5.3 Project 1: Project Weft (part 1 of 3)

#### 5.3.1 Overview

Project Weft is the deterministic reconciliation engine for LedgerLoom. It replaces the order-dependent matching core used in production in 2023 with a matching core whose output is a function of the event set alone. The project was opened on 8 January 2024 as Jira epic WEFT-100 and ran to the end of the period. Its technical lead is Elena Varga, Chief Technology Officer, and its principal engineer is Kwame Asante, Principal Engineer, who led the ledger core. Jessica Harrow contributed product requirements for matching rules and customer exception handling.

The project's central question is whether a reconciliation engine can be simultaneously deterministic, auditable, tolerant of identifier mutation and fast enough to sit in the commit path of a live finance system. Each of those properties is individually achievable with known techniques. The Company's assessment, reached in January 2024, was that no known technique combined them, and that combining them would require new merge semantics and a new matching protocol.

#### 5.3.2 Baseline

The baseline against which the project's advance is measured is the state of the art in bank-to-ledger reconciliation as it stood at the start of 2024. In that baseline, a reconciliation engine typically matches a bank item to a ledger item by testing a sequence of rules: exact match on amount, date and reference; match on amount and reference with a date tolerance of a few days; match on amount with a fuzzy comparison of reference text; and so on. Matches are made greedily as items arrive. Items that fail every rule enter a manual exceptions queue, which accountants clear by hand.

That baseline has three known weaknesses. It is order-dependent, because a greedy rule-based engine can make an early match that a later event would have made differently, and it has no mechanism for revisiting the match without manual intervention. It is identifier-dependent, because a re-issued bank transaction with a changed identifier is usually treated as a new item, creating a duplicate that must be matched or cleared by hand. And it is not split-aware in a principled way, because settlement splits are handled by special-case rules that are difficult to audit.

Event sourcing is an established architectural pattern, and the Company's use of an append-only log is consistent with it. Conflict-free replicated data types (CRDTs), including grow-only counters, observed-remove sets and vector-clock-based merges, are well documented. Both are used in the Company's wider platform for other purposes. But to the Company's knowledge in January 2024, neither event sourcing nor CRDT-style merging had been applied to a reconciliation problem in which the identity of an item can change after it has been matched, and in which the match itself must be auditable at the level of the individual event. Published approaches tend to assume stable identifiers, or accept eventual consistency in place of determinism. Neither assumption is acceptable for a reconciliation product.

The baseline performance requirement was equally specific. LedgerLoom's largest customers generate bank and settlement events at rates that peak at around 20,000 events per second when several large tenants are active. The commit path must complete within the customer-facing latency budget, which the Company set at 200 milliseconds at the 99th percentile. The 2023 engine achieved the latency budget only by making matching decisions before all related events had arrived, which is the root of its order-dependence.

#### 5.3.3 Advance sought

The advance sought by Project Weft has three components.

The first is lineage-aware merge semantics. Each bank-side item is associated with a lineage: the set of identifiers that have been observed to refer to the same underlying transaction. Lineage is established by evidence in the event stream, such as a feed's report that transaction A has been re-issued as transaction B with an identical amount and value date. The merge function that combines the lineage state of two replicas must be commutative, associative and idempotent, so that any two replicas that have seen the same events agree on the lineage, whatever the order in which they saw them. The advance is that this merge preserves the full history of identifiers and does not overwrite an earlier identifier when a later one is observed.

The second is a two-phase match protocol that uses compensating events. In the baseline, a match that turns out to be wrong is corrected by editing the match record. In the advance sought, a committed match is never edited. A later event that invalidates a match generates a compensating event that refers to the original match, and the reconciliation graph is recomputed as a function of the full event set. This gives a complete audit trail and makes the reconciliation result reproducible from the log.

The third is performance. The advance sought is sustained throughput of about 50,000 events per second, which is roughly two and a half times the observed peak of the 2023 engine, together with a p99 commit latency below 200 milliseconds. The Company's view was that achieving this with a deterministic protocol would be the clearest demonstration that the advance was practical rather than theoretical.

Together these components give the Company a reconciliation engine whose output is a deterministic, replayable function of its events, with identifier mutation handled through lineage, matching corrections handled through compensation and performance adequate for production. The Company regarded this as a combination of properties not available in the published art at the start of the period.

#### 5.3.4 Uncertainties

The project addressed two technical uncertainties, which were stated at the start of the project and recorded in the project's technical charter on 12 January 2024.

The first uncertainty was whether a deterministic merge function exists that preserves auditability when identifiers are mutated after an item has been matched. A merge function of the kind required must be commutative, associative and idempotent over lineage state, and must never discard an identifier from the history. The Company did not know, at the start of the project, whether such a function could be defined over the lineage structure that bank feeds actually produce, in which an identifier may be re-issued more than once and may, in rare cases, be re-issued with a different amount. If no such function existed, the audit property would have to be given up, or determinism would have to be given up, and neither was acceptable.

The second uncertainty was whether probabilistic candidate scoring could be carried out within the commit path inside the 200 millisecond budget. Candidate scoring, in which a bank item is compared against plausible ledger items and each candidate receives a score, is the step that makes fuzzy matching possible. In the baseline it runs before the commit. In the advance sought, the Company intended to keep scoring inside the commit path, so that every committed match was the product of a scored candidate, while holding the commit until the causal horizon for the partition was complete. The Company did not know whether scoring at that point, against tenants with large and contended partitions, could meet the latency budget at the 99th percentile.

Neither uncertainty could be resolved by reading the literature, because the combination of properties had not been demonstrated elsewhere. Both could be resolved by building and measuring a prototype, which is what the project did.

#### 5.3.5 Methodology

The project followed an iterative prototyping method, with each iteration designed to test one of the two uncertainties or one of the design choices that followed from it. Each iteration had a written hypothesis, a prototype, a measurement against a recorded event corpus and a decision recorded in the engineering notebook. Iterations that failed were recorded in the same way as those that succeeded.

The method depended on three tools that the Company built during the period. The first was a replay harness, which takes a recorded event corpus and feeds it into the reconciliation engine in a chosen order, with a chosen duplication pattern, and then produces a digest of the resulting reconciliation graph. Two runs with the same events and different orders should produce the same digest. The harness was built in May and June 2024 (WEFT-198) and was the principal instrument for testing determinism. The second tool was a generator of adversarial event corpora, which produces feeds with the properties LedgerLoom has seen in production: identifier re-issue, partial settlement splits, duplicates across feeds and late settlement reports. The corpora were built from anonymised test tenants and from synthetic variants of those tenants, and were versioned in the repository. The third tool was a benchmark harness, which measures throughput and commit latency on a cluster of three nodes configured to match the production instance type.

The design of the protocol proceeded in four strands, described below and in Section 5.4.

**Event model and causal horizon.** Every event carries its source identifier, its per-source sequence number and a lineage epoch, which is an integer incremented each time the source re-issues an identifier. The causal horizon for a partition is the point up to which every expected source has reported. Matches are held in a provisional state until the causal horizon has passed the events on which they depend. This is the mechanism that allows matching to be deterministic, because a match is never committed on the basis of an incomplete event set.

**Lineage clocks.** The lineage state is a variant of a vector clock. A standard vector clock records, for each process, the latest sequence number seen from that process, and it orders events by causality. That is not sufficient for bank feeds, because a re-issued transaction is not a new event from the same source in the causal sense. It is the same underlying fact observed under a new identifier. The Company's variant, which it calls a lineage clock, is a vector indexed by source and lineage epoch rather than by source alone. Each entry records the highest sequence number seen from a source within a given epoch. A re-issue increments the epoch and, crucially, adds an alias edge from the old lineage identifier to the new one. Alias edges are themselves events, so they are merged like any other event. Where two replicas hold conflicting alias edges, the merge keeps the set union of edges and resolves any choice of canonical identifier by taking the lexicographically smallest identifier in the lineage. That rule is deterministic and independent of the order in which edges were received.

The lineage clock was defined in engineering notebook page MSL-EN-0438, dated 29 April 2024, and implemented under WEFT-147 (alias edges) and WEFT-151 (epoch-indexed clocks). It was the first design element to be proven correct by property testing, using generated sequences of observations under random permutation, which confirmed that the merge was commutative, associative and idempotent over the generated space.

**Matching state machine.** Each bank-side item moves through a finite set of states: UNMATCHED, CANDIDATE, PROVISIONAL, COMMITTED, REOPENED and SUPERSEDED. Transitions are driven only by events and by the causal horizon. A bank item enters CANDIDATE when a ledger item with a score above the threshold is found. It enters PROVISIONAL when a candidate is selected and the selection is recorded. It enters COMMITTED when the causal horizon has passed every event on which the selection depends. A COMMITTED item enters REOPENED when a compensating event refers to its match, and SUPERSEDED when its lineage has been merged into another lineage by an alias edge. The state machine is a pure function of the event set: given the same events, every item reaches the same state. The design of the state machine was recorded in engineering notebook page MSL-EN-0412, dated 22 April 2024, and the transition table was reviewed by the engineering team on 26 April 2024.

**Two-phase match with compensating events.** The matching protocol has two phases. In the first phase, the engine proposes a match. It identifies the candidate ledger items for a bank item, scores them, and selects the highest-scoring candidate, with ties broken by the canonical identifier of the candidate. The selection is written as a PROPOSED event. In the second phase, once the causal horizon has passed the events that the proposal depends on, the engine confirms the match by writing a CONFIRMED event. If a later event changes the set of candidates, for example because a settlement report arrives that splits a bank credit differently, the engine does not alter the earlier PROPOSED or CONFIRMED event. It writes a compensating event that refers to the earlier match and reopens the item, and the new state of the graph is computed from the complete log. The protocol was defined in architecture decision record MSL-ADR-014, approved on 9 April 2024, after the two alternatives described in Section 5.4 were rejected.

**Determinism and numeric discipline.** Determinism depends on details as well as on the high-level design. Scores are computed in fixed-point arithmetic, quantised to integer basis points, so that the same inputs produce the same score on every node and in every order of evaluation. Candidate ordering is a total order: by score descending, then by canonical identifier ascending, then by event sequence number. The replay harness checks each of these properties on every build. The Company treated any non-determinism found by the harness as a defect of the highest severity, and no such defect was accepted into a release during the period.

These design choices were developed in parallel and reviewed together. The Company's assessment is that each choice was necessary, and that the combination constitutes the project's advance. Section 5.4 describes the work log and the failed designs that shaped the final protocol.

---

## 5. Technical Narrative (continued)

### 5.4 Project 1: Project Weft (part 2 of 3): work log, rejected designs and measurements

#### 5.4.1 Rejected designs

Three designs were considered and tested before the final protocol was adopted. Each was taken to the point of a working prototype and a measurement, and each was rejected on evidence. The rejections are the principal reason the Company's view of the uncertainties changed during the project.

**Design A: exactly-once delivery from the event transport.** The first design considered was to rely on the exactly-once semantics offered by the Kafka event transport, on the expectation that transactional producers and consumers would guarantee that each event was processed exactly once, and that determinism would follow. The design note MSL-DN-0003, dated 19 February 2024, records why this was rejected. Exactly-once semantics apply to records within the transport system. They guarantee that a message written in a transaction is read and processed once, and they do not address the case that matters for bank feeds, in which the external source issues two records for one underlying transaction under different identifiers. The transport cannot know that the two records are the same item. A prototype was built to test this. It processed a corpus of re-issued transactions with exactly-once settings enabled, and produced two different matches for the same underlying item depending on which identifier was seen first. The design was therefore rejected as insufficient for the problem, and the lineage layer described in Section 5.3.5 was introduced to supply the missing semantics.

**Design B: probabilistic de-duplication with a Bloom filter.** The second design used a Bloom filter to detect duplicate events cheaply in the commit path. The attraction was memory and speed: a filter of modest size could recognise previously seen event keys with a very low error rate. The design note MSL-DN-0007, dated 12 March 2024, records the evaluation. At the key counts expected in the largest tenant clusters, the measured false-positive rate was 0.8%. A false positive in a de-duplication filter causes a genuine event to be discarded as a duplicate. That creates a mismatch which a finance team would see as a missing bank item, and the error is silent, because the discarded event leaves no trace in the output. The Company concluded that a design with a non-zero, silent error rate was incompatible with the audit property, and rejected it. The prototype filter was retained in the replay harness for performance comparisons only.

**Design C: two-phase matching with compensating events.** The third design, and the one adopted, was the two-phase protocol described in Section 5.3.5. Its key property is that a committed match is never edited. Compensating events are added to the log, and the reconciliation graph is recomputed from the complete event set. The first prototype, built under WEFT-203 and benchmarked on 15 July 2024, was slower than the target, because scoring ran synchronously on every event, which is the cause of the first benchmark result described in Section 5.4.3. The protocol was therefore kept, and its scoring step was restructured, as recorded in the work log below. Architecture decision record MSL-ADR-014, approved on 9 April 2024, records the adoption of the two-phase design and the rejection of the alternatives.

#### 5.4.2 Chronological work log

The work log below records each dated iteration, with its hypothesis, the work carried out and the outcome. Jira references are to the WEFT project. Engineering notebook references are to the Company's notebook system.

| Date | Reference | Iteration and outcome |
|---|---|---|
| 8 January 2024 | WEFT-100 | Project opened as an epic. Technical charter recorded with the two uncertainties in Section 5.3.4. |
| 22 January 2024 | WEFT-112 | Deterministic match key derivation. Iteration 1 derived a match key from amount, value date and normalised reference. The key was stable under reordering but changed on re-issue, so re-issued items were not linked. Iteration 1 abandoned on 29 January 2024. |
| 5 February 2024 | WEFT-112 | Iteration 2 kept an explicit list of identifiers per item. Stable under reordering for single re-issues, but the list merge was not commutative when two replicas received different re-issues of the same item. Noted for the lineage design. |
| 19 February 2024 | MSL-DN-0003 | Design A evaluated and rejected (Section 5.4.1). |
| 12 March 2024 | MSL-DN-0007 | Design B evaluated and rejected (Section 5.4.1). |
| 9 April 2024 | MSL-ADR-014 | Two-phase matching with compensating events approved as the protocol. |
| 22 April 2024 | MSL-EN-0412 | Matching state machine designed. Transition table reviewed on 26 April 2024. |
| 29 April 2024 | MSL-EN-0438 | Lineage clocks defined, including the epoch-indexed vector and alias edges. Property tests written for commutativity, associativity and idempotence. First run found a failure in the case of two re-issues delivered in reverse order; the merge rule was corrected on 1 May 2024. |
| 3 May 2024 | WEFT-147 | Alias edges implemented as events in the log. Canonical identifier selection by lexicographic minimum adopted. |
| 14 May 2024 | WEFT-151 | Epoch-indexed lineage clocks implemented in the reconciliation core. |
| 14 May to 6 June 2024 | WEFT-198 | Replay harness built. On 30 May 2024 the first determinism test failed: three replays of the same corpus produced three different digests. The cause was floating-point score comparison. Scores were converted to fixed-point, quantised to basis points, on 6 June 2024, and the test passed on all corpora. |
| 17 June 2024 | WEFT-205 | Adversarial corpus generator, version 1, released to the repository. Generates identifier re-issue, partial settlement splits, cross-feed duplicates and late settlement reports. |
| 1 July 2024 | WEFT-203 | Two-phase proposal and confirm steps implemented as a prototype and run on the generator corpora. |
| 15 July 2024 | MSL-BM-0021 | Benchmark run 1 (Section 5.4.3). Throughput 31,200 events per second; p99 commit latency 318 milliseconds. Latency above budget, attributed to synchronous scoring. |
| 2 August 2024 | WEFT-203 | Compensating event type and reopen path added. Item closed after the compensating path passed the generator corpora. |
| 16 September 2024 | WEFT-219 | Determinism tests extended to shuffled orders and duplication patterns in each corpus. All corpora passed. |
| 18 September 2024 | MSL-BM-0034 | Benchmark run 2. Scoring restructured to run once per causal horizon window, rather than per event. Throughput 47,600 events per second; p99 191 milliseconds. Budget met. |
| 14 October 2024 | MSL-BM-0041 | Six-hour soak test on the three-node cluster. Sustained throughput 50,300 events per second; p99 184 milliseconds. |
| 4 November 2024 | WEFT-260 | Shadow mode established for two production tenants. The engine runs alongside the 2023 engine, and its output is recorded but not shown to customers. |
| 13 December 2024 | MSL-BM-0048 | Determinism report. Fourteen replays of a 2.1-million-event corpus, each with a different order and duplication pattern, produced identical graph digests in every case. |
| 31 December 2024 | n/a | Period end. Shadow mode continued into 2025 and is outside this claim. |

The log shows that the project did not follow a straight line. Two designs were rejected outright, the lineage merge required a correction after property testing, the determinism harness found a defect that the team had not anticipated, and the first benchmark missed the latency budget. Each of these was recorded, and each shaped the design that followed.

#### 5.4.3 Measurements

Three benchmark runs were carried out on the three-node cluster configured to match the production instance type. The table below records the results. All runs used the adversarial corpus generator with the same parameters, and the latency figure is the 99th percentile commit latency measured at the customer-facing interface.

| Run | Date | Change under test | Throughput (events/s) | p99 commit latency (ms) |
|---|---|---|---:|---:|
| MSL-BM-0021 | 15 July 2024 | Synchronous scoring per event | 31,200 | 318 |
| MSL-BM-0034 | 18 September 2024 | Scoring once per causal horizon window | 47,600 | 191 |
| MSL-BM-0041 | 14 October 2024 | Six-hour soak, same configuration as run 2 | 50,300 | 184 |

The run 1 result was the most important technical finding of the period, because it showed that the protocol as first implemented could not meet the latency budget. The team's response was to restructure scoring so that candidate scores were computed once per causal horizon window and reused for all events in that window, which preserved determinism because the window boundaries are themselves determined by the event set. The restructured design met the budget in run 2 and sustained it over the soak test in run 3.

#### 5.4.4 Determinism measurement

Determinism was measured by the replay harness using the digest of the reconciliation graph. Report MSL-BM-0048 records fourteen replays of a single corpus of 2.1 million events. Each replay used a different permutation of the events and a different duplication pattern, generated from a fixed seed so that the set of replays could be reproduced. All fourteen produced the same graph digest. The Company regards this as the definitive test of the deterministic property, and it is the test on which the audit claim rests.

### 5.5 Project 1: Project Weft (part 3 of 3): outcomes, boundaries and competent professional statement

#### 5.5.1 Outcomes

At the end of the period, Project Weft had delivered the following outcomes.

The reconciliation core was deterministic in the sense defined in Section 5.3.5. Given the same event set, in any order and with any duplication, it produced the same reconciliation graph, and every edge was traceable to its proposal and confirmation events. The determinism report MSL-BM-0048 is the record of this outcome.

Lineage was handled through alias edges and epoch-indexed clocks. Identifier mutation no longer created duplicates, and the audit history of each item retained every identifier under which it had been reported.

Matching corrections were made by compensating events. No committed match was edited in the period, and the reconciliation graph could be reproduced from the log at any point.

Throughput and latency met the targets set in the technical charter, as recorded in the benchmark reports. Scoring at causal horizon windows was retained in the design.

Shadow mode had been established for two production tenants by the end of the period, and the output of the new engine was being compared with the output of the 2023 engine. The comparison is a continuing activity, and the general release of the engine is not part of this claim.

Two of the three designs in Section 5.4.1 were rejected on evidence, and the protocol that was adopted differs materially from the design considered at the start of the project. The Company regards these as the outputs of the research, because they establish what does not work as well as what does.

#### 5.5.2 Boundaries

The start of Project Weft is 8 January 2024, the date on which epic WEFT-100 was opened and the technical charter was recorded. Work carried out before that date, including the 2023 work on the deterministic ledger core that is covered by the Company's previous claim, is not claimed for in this project.

The end of Project Weft for the purposes of this claim is 31 December 2024. Work after that date, including the general release of the engine, the continuing shadow-mode comparison and any further optimisation, is outside the boundaries of this claim.

#### 5.5.3 Competent professional statement

Elena Varga is Chief Technology Officer of the Company and holds an MSc in Distributed Systems. She has worked on the design of distributed data systems for payments and reconciliation for more than a decade, including several years as a staff engineer at Tallowfield Payments Ltd, where she worked on settlement and reconciliation services for high-volume card acquiring. She is therefore a competent professional in the field of distributed systems and financial data reconciliation.

In her statement, Ms Varga confirms that, at the start of Project Weft in January 2024, she was not aware of any technique in the published literature or in commercial practice that gave a deterministic, replayable reconciliation result when upstream feeds re-issued transactions with mutated identifiers and when settlement was partial. She confirms that the two uncertainties in Section 5.3.4 could not be resolved by a competent professional from existing knowledge, and that they were resolved only by the prototyping and measurement described in this section.

Ms Varga led the technical design of the project and reviewed each of the design notes and decision records referred to above. Kwame Asante, Principal Engineer, led the implementation of the ledger core and the replay harness, and his contribution to the lineage design and the determinism tests is recorded in the Jira and notebook references. Both are named as the principal contributors to Project Weft in Section 6.

---

## 5. Technical Narrative (continued)

### 5.6 Project 2: Project Lumen

#### 5.6.1 Overview

Project Lumen is the Company's programme to redesign the LedgerLoom reconciliation workspace. The workspace is where finance users review bank items, inspect matches, clear exceptions and export their reconciliation. Project Lumen introduced a new React component library, which the Company calls the Lumen design system, and a redesigned workspace built on it. It also introduced a smart suggestions panel that uses a third-party large language model API to explain why an item remains unmatched and to propose next steps. The project ran from 1 April 2024 to 30 November 2024. Freya Doyle, Frontend Engineer, led the front-end work. Chen Wu, Engineer, led the integration with the language model API. Jessica Harrow, Product Manager, led the product definition and the customer sessions.

The project is an exercise in making a complex, data-dense workflow feel simple to people who spend their working day inside it. Finance users process many hundreds of items in a session, and the difference between a workspace that encourages them and one that slows them down is measured in hours each month. Lumen was designed to make that difference.

#### 5.6.2 Baseline

The reconciliation workspace in 2023 was built on an earlier component kit. Its interaction patterns had grown organically across screens, so that filtering, sorting, selection and exception handling behaved differently on each. Standard practice for such a problem is to adopt an established component library, define a consistent set of interaction patterns and surface unmatched items through filters and tables, with the user supplying the reasoning. That is the baseline against which the project's advance is measured.

Large language model APIs are known to be capable of producing natural-language explanations of structured data. Their use inside a finance application is, however, an area in which practice was not established at the start of the project. Finance users and their auditors have particular expectations about the provenance of explanations, and a generated explanation is not an audit record. The baseline position was therefore that generated explanations of unmatched items were a plausible feature but had not been demonstrated to be useful, trusted or consistent with reconciliation practice.

#### 5.6.3 Advance sought

The advance sought has two components. The first is a component library and redesigned workspace that present reconciliation information with a consistent set of interaction patterns, sufficient to reduce the number of steps needed to clear a typical exception. The second is a suggestions panel that explains each unmatched item in plain language, using the structured data for that item and its nearest candidates, and that suggests a next action. The explanation is advisory. It does not change the reconciliation graph, which remains determined by the engine described in Section 5.3.

The advance sought is therefore a new interaction model for reconciliation, in which the user is supported by generated explanation without the explanation being mistaken for a record.

#### 5.6.4 Uncertainties

The project addressed two uncertainties, recorded in the project charter on 1 April 2024.

The first was whether users would trust AI-generated explanations of unmatched items. The Company did not know whether finance users, who are accustomed to rule-based exception codes, would accept a generated explanation as a reasonable basis for action, or would regard it as unreliable and disregard the panel.

The second was achieving a seamless, intuitive experience across the full reconciliation workflow. Each screen in the workspace carries a large amount of information, and the Company did not know whether a redesigned set of components, combined with a suggestions panel, could present that information clearly enough for users to move through a session without friction.

Both uncertainties concern how users respond to a design, and they could be resolved only by building the design and observing users with it.

#### 5.6.5 Methodology

The project followed a sprint cycle of two weeks, with a sprint review at the end of each cycle. Each review considered a working build, the user feedback gathered during the sprint and the decisions to be taken for the next. The minutes of the nine sprint reviews held during the period are recorded as MSL-SR-LUM-01 to MSL-SR-LUM-09.

The component library was developed in a separate repository with its own build and test pipeline. Each component was specified with its states, its keyboard behaviour and its accessibility requirements, and was reviewed against those requirements before it was used in the workspace.

The suggestions panel was built against a language model API through a thin integration layer. Before any item's data is sent to the API, the integration layer removes account numbers and personal names from the payload, and it limits the payload to the fields needed for the explanation. Prompts were iterated during the sprint cycle, and the explanations produced were reviewed by the product team against a set of sample unmatched items drawn from the test tenants.

User sessions were held with finance users from beta customers throughout the period. The Company's product team ran fourteen sessions in total, in which users worked through a reconciliation using the new workspace and the panel, and their responses were recorded in the sprint review minutes.

#### 5.6.6 Work log

| Date | Reference | Iteration and outcome |
|---|---|---|
| 1 April 2024 | Project charter | Project opened. Uncertainties recorded as in Section 5.6.4. |
| 15 April 2024 | MSL-SR-LUM-01 | First sprint review. Component library scope agreed. Filter and table components built. |
| 29 April 2024 | MSL-SR-LUM-02 | Selection and exception-handling components reviewed. Users found the exception flow hard to follow. Redesigned in the following sprint. |
| 27 May 2024 | MSL-SR-LUM-03 | Language model integration prototyped. First explanations judged too generic by the product team. Prompt revised. |
| 24 June 2024 | MSL-SR-LUM-04 | Redaction layer added to the integration. Explanation quality reviewed against sample items. |
| 22 July 2024 | MSL-SR-LUM-05 | First user session. Users were positive about the component layout but cautious about explanations. |
| 19 August 2024 | MSL-SR-LUM-06 | Suggestions panel redesigned to show explanation and source fields side by side. |
| 16 September 2024 | MSL-SR-LUM-07 | Second round of user sessions. Trust in explanations reported as improved. |
| 28 October 2024 | MSL-SR-LUM-08 | Redesigned workspace released to beta customers. |
| 25 November 2024 | MSL-SR-LUM-09 | Final review of the project. Lumen components adopted as the standard for the workspace. |

#### 5.6.7 Outcomes

At the end of the project the Lumen design system was in use across the reconciliation workspace, and the redesigned workspace had been released to beta customers. The suggestions panel was in beta, and the sprint reviews record the Company's view that users had come to rely on its explanations as a starting point for their own judgement. The project's outcomes are recorded in the sprint review minutes listed above.

#### 5.6.8 Boundaries

The project started on 1 April 2024, when the project charter was approved, and ended on 30 November 2024, following the final sprint review. Work on the component library after that date, and the general release of the suggestions panel, are outside this claim.

#### 5.6.9 Competent professional statement

The competent professional for Project Lumen is Elena Varga, Chief Technology Officer, who approved the technical design of the integration layer and the redaction approach. Ms Varga confirms that at the start of the project a competent professional could not determine from existing knowledge whether finance users would trust generated explanations, or whether a redesigned workspace would be seamless to use. These questions required building and testing, which the project carried out.

### 5.7 Project 3: Project Stratus

#### 5.7.1 Overview

Project Stratus is the re-architecture of the LedgerLoom hosting estate. Until the start of the project, LedgerLoom ran on virtual machines configured by scripts, with a shared environment that gave limited isolation between customer tenants. Project Stratus moved the estate onto Kubernetes on AWS, with the infrastructure defined in Terraform, a unified observability stack for metrics, logs and tracing, and a tenant-sharding scheme that places each tenant's data partitions onto node pools according to data residency and load. The project ran from 2 January 2024 to 31 December 2024. Sam Okoro, DevOps Engineer, led the infrastructure and migration work. Rosie Tamworth, Senior Engineer, led the platform and tenant services, including the sharding scheme.

#### 5.7.2 Baseline

The baseline for hosting a multi-tenant software service is well established. Containerised workloads, managed by an orchestration system such as Kubernetes, are commonly deployed on public cloud infrastructure using infrastructure-as-code tools such as Terraform, and observability is provided by a standard metrics, logging and tracing stack. Migration from virtual machines to containers is a widely documented activity, and the published guidance on it is extensive. The Company's own baseline was a shared environment with configuration held in scripts, which made per-tenant isolation and rolling change difficult to manage.

#### 5.7.3 Advance sought

The advance sought was a migration of the whole estate, including its stateful reconciliation stores, to the new architecture with no customer-visible downtime. The tenant-sharding scheme was intended to allow tenants to be moved between node pools individually, which is what made a cohort-by-cohort migration possible.

#### 5.7.4 Uncertainties

The principal uncertainty recorded for the project was whether the platform could achieve zero-downtime migration of live tenants. The LedgerLoom reconciliation store is stateful, and moving a tenant's store between hosts while reconciliation continues is not a routine operation. The Company did not know, at the start of the project, whether the migration procedure would hold for the full range of tenant sizes in production.

#### 5.7.5 Methodology

The project was carried out in three tenant migration cohorts, each preceded by a rehearsal in the non-production environment and followed by a review. The migration procedure for each cohort was documented in a runbook. Each cohort was migrated in a window chosen by the customer success team, and each migration was monitored with the new observability stack. Sprint reviews, recorded as MSL-SR-STR-01 to MSL-SR-STR-08, governed the work between cohorts.

The tenant-sharding scheme was developed by Rosie Tamworth in the second quarter of 2024. It assigns each tenant partition a shard key derived from the tenant identifier and a residency tag, and it maps shard keys to node pools using a placement table that is updated when load changes. The scheme was tested against simulated tenant populations before it was used in production.

#### 5.7.6 Work log

| Date | Reference | Iteration and outcome |
|---|---|---|
| 2 January 2024 | Project charter | Project opened. Migration plan drafted with three cohorts. |
| 26 February 2024 | MSL-SR-STR-01 | Infrastructure defined in Terraform for the non-production environment. Cluster build completed. |
| 22 April 2024 | MSL-SR-STR-02 | Observability stack deployed to non-production. Dashboards agreed with the customer success team. |
| 3 June 2024 | MSL-SR-STR-03 | Tenant-sharding scheme design reviewed. Placement table format agreed. |
| 18 June 2024 | MSL-SR-STR-04 | First tenant migration cohort completed. One rollback was carried out on a tenant whose store was larger than the rehearsal. The procedure was revised. |
| 16 July 2024 | MSL-SR-STR-05 | Revised procedure rehearsed against the largest tenant store. Rehearsal completed without rollback. |
| 10 September 2024 | MSL-SR-STR-06 | Second cohort migrated. No customer-visible downtime recorded. |
| 22 October 2024 | MSL-SR-STR-07 | Placement table extended to cover load-based rebalancing. |
| 19 December 2024 | MSL-SR-STR-08 | Final cohort migrated. The last virtual machine retired. |

#### 5.7.7 Outcomes

At the end of the period, the LedgerLoom estate ran on Kubernetes on AWS, the infrastructure was defined in Terraform, and the observability stack covered all tenants. The three cohorts had been migrated, and the Company recorded no customer-visible downtime in the second and third cohorts. The first cohort included a rollback, which is recorded in MSL-SR-STR-04 and led to the revised procedure used thereafter. The tenant-sharding scheme was in production for all tenants at the end of the period.

#### 5.7.8 Boundaries

The project started on 2 January 2024 and ended on 31 December 2024. Work on the estate after the period end, including the retirement of the remaining legacy tooling, is outside this claim.

#### 5.7.9 Competent professional statement

The competent professional for Project Stratus is Elena Varga, Chief Technology Officer. Ms Varga confirms that, at the start of the project, the question of whether the stateful reconciliation store could be migrated with zero downtime could not be answered from published guidance alone, because the reconciliation store has properties that general migration guidance does not cover. The question was resolved by rehearsal and by the measured outcomes of the three cohorts described above.

---

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

---

## 6. Cost Schedules and Methodology

### 6.1 Basis of preparation

The costs in this section relate to the accounting period 1 January 2024 to 31 December 2024. The staff costs are the total employment costs of each named employee for the period, taken from the Company's payroll records, and comprise gross salary, employer's National Insurance contributions calculated on the 2024-25 basis, and employer's pension contributions. The other categories are taken from the Company's purchase ledger, supplier invoices and subcontract agreements. The schedules below reproduce the figures in the cost schedule for this claim.

The period is subject to the SME scheme rules, under which the Company claims an enhancement of 86% of qualifying expenditure and a payable credit of 10% on the surrenderable loss. The scheme label shown in the cost schedule header is reproduced as it appears on the schedule.

### 6.2 Cost schedule: staff costs (as claimed)

Period: 1 Jan 2024 – 31 Dec 2024  ·  NIC basis: 2024-25  ·  Scheme claimed: **sme-2023**

| Name | Role | Salary | Er NIC | Er pension | Total | R&D % | Claimed | Includes |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Elena Varga | CTO / competent professional | £105,000 | £13,234 | £5,250 | £123,484 | 70% | £86,439 |  |
| Kwame Asante | Principal Engineer (ledger) | £88,000 | £10,888 | £4,400 | £103,288 | 90% | £92,959 |  |
| Rosie Tamworth | Senior Engineer | £72,000 | £8,680 | £3,600 | £84,280 | 85% | £71,638 |  |
| Ben Lacey | Engineer | £58,000 | £6,748 | £2,900 | £67,648 | 85% | £57,501 |  |
| Chen Wu | Engineer | £56,000 | £6,472 | £2,800 | £65,272 | 85% | £55,481 |  |
| Freya Doyle | Frontend Engineer | £54,000 | £6,196 | £2,700 | £62,896 | 80% | £50,317 |  |
| Sam Okoro | DevOps Engineer | £64,000 | £7,576 | £3,200 | £74,776 | 75% | £56,082 |  |
| Jessica Harrow | Product Manager | £70,000 | £8,404 | £3,500 | £81,904 | 60% | £49,142 |  |
| Oliver Marrow | CEO | £120,000 | £15,304 | £6,000 | £141,304 | 40% | £56,522 |  |
| **Total staff** | | | | | | | **£576,081** | |

### 6.3 Cost schedule: other qualifying expenditure (as claimed)

| Category | Description | Claimed |
|---|---|---:|
| EPW (unconnected) | Contract developers via agency £96,000 x 65% | £62,400 |
| Software | JetBrains, GitHub, Jira, Figma, Slack, Salesforce | £38,600 |
| Data & cloud | AWS cloud computing | £184,000 |
| Subcontract (UK, unconnected) | Open Banking aggregator integration – Plaidwise Ltd £30,000 x 65% | £19,500 |
| **Total other** | | **£304,500** |

### 6.4 Total qualifying expenditure

Total qualifying expenditure (as claimed): **£880,581**

### 6.5 Relief computation

Relief computation (as claimed): 86% additional deduction; 10.0% payable credit on surrendered loss

- extra deduction: £757,300
- surrenderable loss: £1,637,881
- payable credit: £163,788
- company turnover for context: £3,100,000
- trading loss before R&D deduction: £1,450,000

### 6.6 Methodology: staff costs

The staff costs in Section 6.2 are apportioned to the four projects on the basis of the proportion of each employee's working time spent on activities within those projects. Each employee's total employment cost is multiplied by the R&D percentage to give the claimed amount. For example, Elena Varga's total employment cost of £123,484 at 70% gives £86,439 after rounding to the nearest pound.

Time was not recorded against individual projects in a timesheet system for 2024. The apportionments were therefore determined through structured interviews with team leads, conducted in September 2025, in which each team lead was asked to describe the working time of each member of their team across the period and to state the proportion that related to the four projects. The interview notes are indexed as MSL-IN-2509-01 to MSL-IN-2509-06. Each percentage was agreed with the team lead and with the employee concerned, and was checked for consistency with the projects described in Section 5.

The engineering percentages reflect the team leads' view that the Company's engineering work is directed at resolving technical uncertainty in the design, building and operation of LedgerLoom, so that the majority of engineering time is research and development in nature. On that basis the engineering staff were allocated between 75% and 90% of their time, with the highest allocations given to those working on the ledger core. The Chief Technology Officer's allocation of 70% reflects her technical leadership across Projects Weft, Stratus and Conduit, and her competent professional role.

The Product Manager's allocation of 60% reflects her time on the definition of matching rules, the design of the customer exception workflow and the product requirements for Projects Weft and Lumen. The Chief Executive Officer's allocation of 40% reflects his time on the strategic direction of the research programme, the approval of project scope and the commercial review of the outcomes of each project.

Jira worklog records exist for the work items in the WEFT project, principally for the Chief Technology Officer and the Principal Engineer. Those records corroborate the allocations for those two individuals and are reproduced as an extract in Section 7.

### 6.7 Methodology: externally provided workers

Contract developers were supplied to the Company through Northgate Contract Resourcing Ltd during the period, at a total agency cost of £96,000. The contract developers worked alongside the Company's own engineers on defined pieces of work, principally on the ledger core and on the Lumen component library. The proportion claimed, 65%, is the share of the agency work estimated to relate to the four projects, based on the work items to which the contract developers were assigned. The agency invoices and the statement of work are indexed in Section 7.

### 6.8 Methodology: software

The software costs are for the tools used in the conduct of the four projects during the period. They comprise development environments and source control (JetBrains and GitHub), the issue tracking system used for each project (Jira), the design tool used for prototyping the Lumen interface (Figma), the messaging system used by the engineering and product teams (Slack) and a Salesforce sandbox used to test the behaviour of customer data connectors. The costs are claimed in full on the basis that each tool was used in the conduct of the projects. The licence and subscription invoices are indexed in Section 7.

### 6.9 Methodology: data and cloud

The data and cloud costs are for AWS hosting in the London region for the period. This comprises the production hosting for LedgerLoom, together with the non-production environments used by the replay harness and the benchmark clusters described in Section 5. The costs are claimed in full as cloud computing used in research and development. The Company's position is that the production environment is the environment in which the outputs of the projects are operated, tested and measured, and that the cloud resources consumed by the projects cannot be separated from the operation of the platform on which they run. The AWS invoices for the period are indexed in Section 7.

### 6.10 Methodology: subcontract

The subcontract with Plaidwise Ltd, a UK company, was signed on 15 July 2024 under agreement MSL-CT-0715. Its total value for the period was £30,000. The subcontract covered the engineering of the aggregator integration and the testing of connectors for the thirty banks connected under Project Conduit. The proportion claimed, 65%, is the share of the subcontracted work estimated to relate to the development of the bank connectors and the canonical data model, which the Company treats as the research element of the subcontract. The subcontract agreement and the invoices are indexed in Section 7.

### 6.11 Relief computation

The additional deduction is calculated at 86% of total qualifying expenditure of £880,581, giving an extra deduction of £757,300 after rounding. After the additional deduction the trading loss for the period is £2,207,300 (£1,450,000 plus £757,300). The surrenderable loss is the lower of that loss and 186% of qualifying expenditure (£1,637,881), and is therefore £1,637,881. The payable credit is calculated at 10% of the surrenderable loss, giving £163,788. The remaining loss of £569,419 is carried forward. The company's turnover for the period was £3,100,000.

### 6.12 Summary

The total qualifying expenditure of £880,581 is made up of staff costs of £576,081 and other qualifying expenditure of £304,500. The Company's principal costs are staff costs, which account for the greater part of the claim, and the methodology for each category is set out above. Each figure in this section is taken from the cost schedule for the claim, and the supporting records are indexed in Section 7.

---

## 7. Appendices

### Appendix A: Competent professional curriculum vitae

**Elena Varga**
Chief Technology Officer, Marrowgate Software Ltd (from 2021). Head of Engineering, Marrowgate Software Ltd (2019 to 2021).

**Qualifications**
MSc in Distributed Systems, awarded with distinction. BSc in Computer Science, awarded with first-class honours.

**Experience**

*Marrowgate Software Ltd, Manchester, 2019 to present.* Chief Technology Officer, responsible for the engineering, data and platform functions of a 22-person engineering organisation. Technical lead for the LedgerLoom reconciliation platform, including the deterministic ledger core, the multi-tenant hosting estate and the bank and ERP connectivity layer. Competent professional for the Company's research and development projects in 2024: Project Weft, Project Lumen, Project Stratus and Project Conduit. Author of the architecture decision records for the reconciliation protocol and the lineage design.

*Tallowfield Payments Ltd, Manchester, 2015 to 2019.* Staff engineer, settlement and reconciliation services for a high-volume card acquiring business. Designed and operated the services that matched card scheme settlement files against merchant ledgers, with responsibility for correctness, throughput and audit.

*Earlier roles, 2011 to 2015.* Software engineer and senior software engineer in financial data and integration projects for two UK software companies.

**Professional activities**
Speaker on event-sourced financial systems at two UK engineering conferences. Member of the programme committee for a regional distributed systems meetup. Reviewer of technical submissions for a UK software engineering journal.

**Kwame Asante**
Principal Engineer (ledger core), Marrowgate Software Ltd (from 2020, Principal Engineer since 2023).

**Qualifications**
BEng in Electrical and Electronic Engineering, with a postgraduate certificate in Software Engineering.

**Experience**

*Marrowgate Software Ltd, Manchester, 2020 to present.* Senior engineer and then Principal Engineer responsible for the LedgerLoom ledger core. Principal implementer of the replay harness, the adversarial corpus generator and the determinism tests described in Section 5.4 of this claim. Co-author of the lineage clock implementation and of the two-phase matching protocol.

*Previous roles, 2012 to 2020.* Software engineer in payments and settlement systems, followed by senior engineer on a distributed messaging platform for a UK financial data provider.

### Appendix B: Evidence index

The records below are held on the Company's files and are available to HMRC on request. Document identifiers follow the Company's evidence scheme. Jira references are to the WEFT, LUM, STR and CND projects.

| Reference | Date | Description | Project |
|---|---|---|---|
| WEFT-100 | 8 January 2024 | Jira epic opened, including technical charter | Weft |
| WEFT-112 | 22 January to 5 February 2024 | Deterministic match key derivation: export of work item history | Weft |
| MSL-DN-0003 | 19 February 2024 | Design note: evaluation of exactly-once delivery from the event transport | Weft |
| MSL-DN-0007 | 12 March 2024 | Design note: evaluation of Bloom filter de-duplication | Weft |
| MSL-ADR-014 | 9 April 2024 | Architecture decision record: two-phase matching with compensating events | Weft |
| MSL-EN-0412 | 22 April 2024 | Engineering notebook: matching state machine, with review on 26 April 2024 | Weft |
| MSL-EN-0438 | 29 April 2024 | Engineering notebook: lineage clocks and property test results | Weft |
| WEFT-147 | 3 May 2024 | Alias edges implemented as events | Weft |
| WEFT-151 | 14 May 2024 | Epoch-indexed lineage clocks implemented | Weft |
| WEFT-198 | 14 May to 6 June 2024 | Replay harness: build record and first determinism failure | Weft |
| WEFT-205 | 17 June 2024 | Adversarial corpus generator, version 1 | Weft |
| WEFT-203 | 1 July to 2 August 2024 | Two-phase proposal, confirm and compensating event | Weft |
| MSL-BM-0021 | 15 July 2024 | Benchmark report, run 1 | Weft |
| MSL-BM-0034 | 18 September 2024 | Benchmark report, run 2 | Weft |
| MSL-BM-0041 | 14 October 2024 | Benchmark report, six-hour soak test | Weft |
| WEFT-219 | 16 September 2024 | Determinism tests extended to shuffled orders | Weft |
| WEFT-260 | 4 November 2024 | Shadow mode established for two tenants | Weft |
| MSL-BM-0048 | 13 December 2024 | Determinism report: fourteen replays of a 2.1-million-event corpus | Weft |
| MSL-SR-LUM-01 to 09 | 15 April to 25 November 2024 | Sprint review minutes | Lumen |
| MSL-SR-STR-01 to 08 | 26 February to 19 December 2024 | Sprint review minutes and cohort migration records | Stratus |
| MSL-SR-CND-01 to 06 | 12 August to 12 December 2024 | Sprint review minutes and bank onboarding records | Conduit |
| MSL-CT-0102 | 15 January 2024 | Framework agreement with Northgate Contract Resourcing Ltd | Weft, Lumen |
| MSL-CT-0715 | 15 July 2024 | Integration subcontract with Plaidwise Ltd | Conduit |
| MSL-TS-0701 | Exported 14 October 2024 | Jira worklog extract, WEFT project, 1 July to 30 September 2024 (Appendix C) | Weft |
| MSL-IN-2509-01 to 06 | September 2025 | Structured interview notes with team leads on staff allocations | All |

### Appendix C: Time-recording extract

The extract below is taken from Jira worklog records for the WEFT project, for the period 1 July 2024 to 30 September 2024. It covers the two individuals who logged time against WEFT work items during that quarter. The share is the proportion of each individual's recorded hours in the quarter that relate to WEFT work items.

| Name | Role | Total hours recorded, Q3 2024 | Hours on WEFT work items | WEFT share |
|---|---|---:|---:|---:|
| Elena Varga | CTO / competent professional | 440 | 310 | 70% |
| Kwame Asante | Principal Engineer (ledger) | 440 | 396 | 90% |

Worklog records for the other members of staff in the table at Section 6.2 relate to work items outside the WEFT project and are not reproduced in this extract.

### Appendix D: Invoice and supplier list

| Supplier | Document reference | Date | Net amount | Cost line |
|---|---|---|---:|---|
| Northgate Contract Resourcing Ltd | INV-NCR-2024-0011 | 31 January 2024 | £24,000 | EPW (unconnected) |
| Northgate Contract Resourcing Ltd | INV-NCR-2024-0047 | 30 April 2024 | £24,000 | EPW (unconnected) |
| Northgate Contract Resourcing Ltd | INV-NCR-2024-0083 | 31 July 2024 | £24,000 | EPW (unconnected) |
| Northgate Contract Resourcing Ltd | INV-NCR-2024-0121 | 31 October 2024 | £24,000 | EPW (unconnected) |
| JetBrains | Annual licence renewals, 2024 | Various | £7,200 | Software |
| GitHub | Organisation subscription, 2024 | Various | £9,600 | Software |
| Jira | Cloud subscription, 2024 | Various | £6,800 | Software |
| Figma | Organisation subscription, 2024 | Various | £5,400 | Software |
| Slack | Workspace subscription, 2024 | Various | £8,900 | Software |
| Salesforce | Sandbox subscription, 2024 | Various | £700 | Software |
| AWS | Monthly invoices, January to December 2024 (twelve invoices) | Various | £184,000 | Data and cloud |
| Plaidwise Ltd | INV-PW-2024-0004 | 30 September 2024 | £15,000 | Subcontract |
| Plaidwise Ltd | INV-PW-2024-0009 | 20 December 2024 | £15,000 | Subcontract |

Software subscriptions total £38,600. Agency invoices total £96,000. Subcontract invoices total £30,000.

### Appendix E: Director's declaration

I confirm that I am a director of Marrowgate Software Ltd and that I have reviewed the claim for research and development tax relief for the accounting period 1 January 2024 to 31 December 2024, together with the supporting narrative, cost schedules and records indexed in this pack. I confirm that, to the best of my knowledge and belief, the information given is correct and complete, that the projects described were carried out by the Company, and that the costs claimed were incurred by the Company in carrying out those projects. I confirm that the Company will keep the records referred to in this claim for the period required by law and will make them available on request.

Signed:

Oliver Marrow
Chief Executive Officer and director, Marrowgate Software Ltd

Date: 14 October 2026
