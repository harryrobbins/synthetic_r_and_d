## 5. Technical narrative: P1 (EDITH), part 2 of 2, work log, rollout, outcomes and boundaries

### 5.9 Chronological work log, P1

The log records each iteration of the checker and each stage of the rollout in the accounting period. Dates are the dates the iteration was completed and recorded in the project file. Work before 1 April 2025 is summarised at the start of the log for context.

| Date | Iteration or event | Result recorded |
|---|---|---|
| 3 February 2025 (context) | Project registered under GF-25-014. Scope agreed with the Growth Fund panel. Baseline sample of 60 structural calculations collected. | Baseline set |
| 17 March 2025 (context) | Symbol table design reviewed. Decision to scope symbols by calculation section. | Design decision recorded |
| 22 April 2025 | Prototype parser, version 0.1, run on a sample of 40 steps from a steel column calculation. | 48% of steps parsed. Failures traced to unrecognised notation. |
| 13 May 2025 | Firm-wide AI guidance issued by the Chief Digital and Information Officer and the General Counsel. Checker work continues in the same team. | Guidance recorded in the project file |
| 27 May 2025 | Canonicalisation rules, version 0.3. Unit table extended. Clause edition check added. | Parse rate 58% on the same sample |
| 19 June 2025 | Load combination evaluator run against fundamental and accidental combinations for beams and columns. | Three evaluation defects found and corrected. Re-run gave consistent results on the test set. |
| 8 July 2025 | Pilot calculation set 1 (120 calculations, structural and hydraulic) canonicalised and re-evaluated. | Parse rate 63%. Pipe capacity checks added to the rule file. |
| 15 to 19 September 2025 | Training sessions for the first cohort on the approved assistant. Guidance and calculation-checking support notes issued. | 96 engineers and project managers trained across four sessions |
| 22 September 2025 | First cohort begins using the approved assistant on live project work. Ask Edith pilot interface made available alongside it. | Cohort in use. Usage logs started. |
| 6 October 2025 | Prompt library, version 1, published for the cohort. Prompts for drafting calculation notes and for summarising checking comments reviewed by the Applied AI and Automation team. | Library in use across three disciplines |
| 4 November 2025 | Pilot calculation set 2 (hydraulic and foundation calculations) canonicalised and re-evaluated. Rule file version 0.9 released. | Parse rate 71% against a target of 90% |
| 12 January 2026 | Halvorsen Pike Engineers Inc. data scientists begin evaluation of the assistant on North American design codes, using the same calculation sets adapted to the relevant standards. | Evaluation plan agreed |
| 9 February 2026 | Halvorsen Pike evaluation, first report. Canonicalisation of North American clause references tested on 35 calculations. | Parse rate on the North American sample recorded. Clause mapping work scheduled. |
| 2 March 2026 | Productivity evaluation of the first cohort, covering time taken on calculation checks and drafting before and after the rollout. | Evaluation of productivity benefits reported to the Growth Fund panel |
| 27 March 2026 | Rule file version 1.0 released. Parse performance and coverage summary issued for the period. | Coverage of 14 code clauses across beams, columns, foundations and pipe capacity |

### 5.10 The rollout of the approved assistant within P1

The rollout of the approved assistant to the first cohort is part of P1 because the calculation checker and the assistant share a single purpose, which is to make the checking of calculations more reliable. The assistant was adopted under the firm's AI guidance, and the cohort's use of it was designed as the basis for the checker's second-stage testing. Calculations drafted or edited with the assistant were used as test inputs for the parser, and the findings of the checker were compared with the findings of the engineer who reviewed each calculation.

The rollout involved the following work, which is recorded against P1 and is necessary for the advance to be tested in live use.

- **Training.** Four training sessions were designed and run by the Applied AI and Automation team for the first cohort. The sessions covered the approved uses, the rules on client data, the requirement to check outputs, and the handling of calculations that depend on context the tool does not hold.
- **Guidance.** Calculation-checking support notes were written to explain how the assistant's output should be reviewed before it enters a calculation record. The notes were issued with the firm's May 2025 guidance.
- **Prompt libraries.** Prompt libraries for drafting, summarising and calculation-checking support were built and maintained. Each prompt was tested against a sample of calculations before it was released.
- **Licence provisioning.** Enterprise licences for the approved assistant were provisioned for 1,200 seats across the UK and Ireland, under procurement order PROC-2025-0918, and assigned to users in the cohort and the Applied AI and Automation team.
- **Evaluation of productivity benefits.** The time taken on calculation checks and calculation drafting was recorded before and after the rollout, and the results were compared across disciplines. The evaluation is used to decide where the approved assistant is used next.
- **North American evaluation.** Halvorsen Pike Engineers Inc. data scientists evaluated the assistant on North American design codes, which the firm's cohort uses for its work in that region. The evaluation is recorded against P1 because the same calculation-checking requirements apply, and because the checker's rule set must be extended to the North American codes before it can be used for that work.

The rollout is a substantial piece of work. Its purpose is to bring the calculation checker and the approved assistant into the same workflow, so that the findings of the checker can be read alongside the assistant's output, and so that the evidence needed to decide the next step is collected in a consistent way.

### 5.11 Outcome of P1 in the accounting period

At 31 March 2026 the checker's rule file, version 1.0, covers fourteen code clauses across beams, columns, foundations and pipe capacity checks. The parse rate on the most recent calculation set is 71% of steps, against a target of 90%. The evaluation of load combinations has been consistent on the test sets, after the three defects found in June 2025 were corrected. The North American evaluation has recorded a parse rate and a list of clause mappings still to be built.

The outcome of the project is therefore a verified checking capability for the code clauses in the rule file, a parse capability that reaches 71% of steps on live calculations, and a rollout that has given the firm a consistent basis for measuring the productivity of calculation checks. The project did not achieve its parse target. The technical uncertainty on canonicalisation was reduced, but it is not fully resolved, and P1 will continue in the next phase.

### 5.12 Boundaries of P1

The start of P1 for the purposes of this claim is 3 February 2025, the date the project was registered under GF-25-014. The work carried out in that month and in March 2025 is context and is not claimed within this period.

The end of the qualifying work within this period is 31 March 2026. The work continued after that date and is not claimed.

Within the period, the following activities are excluded from P1 and are not claimed. Routine checking of live project calculations by engineers as part of ordinary design work. Routine provisioning of licences for users outside the first cohort. General IT support for the approved assistant, including helpdesk responses and account administration. Training for users outside the cohort, which was delivered as part of the firm's standard learning programme. Costs of the Ask Edith pilot interface infrastructure, which are not claimed.

The rollout activities listed in section 5.10 are claimed in the period in which they were carried out, because they were carried out to test the advance in live use. The company's view is that these activities form part of the systematic investigation of the uncertainties described in section 5.4.

### 5.13 Competent professional statement, P1

I, Dermot McGregor, am the Chief Digital and Information Officer of Excelcion Limited. I have held this role since January 2025. I am a chartered engineer and a member of the institution for civil engineering, and I have worked in digital engineering and information management for more than twenty years, including in the design and checking of structural and hydraulic calculations and in the leadership of digital engineering practices on major infrastructure programmes.

I am the competent professional for P1. I have oversight of the project's technical plan, its rule file and its evaluation, and I have reviewed each of the iterations listed in the work log in section 5.9. In my view the technical uncertainties described in section 5.4 were genuine uncertainties to a competent professional in this field at the start of the work, because no reliable method was available to the firm or to the wider profession for checking free-text calculations against design codes, and the outcome of each of the uncertainties could not be predicted from existing knowledge.

I have taken part in the rollout described in section 5.10 in an oversight capacity. The rollout is recorded against P1 for the reasons given in section 5.10 and in my view it forms part of the systematic work needed to test the advance in live use. I confirm that the time recorded to P1 by me is an average of my Hourglass timesheet bookings to the Keystone project codes for GF-25-014 and for the P4 digital programme, as set out in section 6.

Signed: Dermot McGregor, Chief Digital and Information Officer
