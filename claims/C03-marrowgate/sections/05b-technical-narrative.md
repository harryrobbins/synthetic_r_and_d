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
