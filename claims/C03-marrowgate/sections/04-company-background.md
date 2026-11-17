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
