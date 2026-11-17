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
