## 5. Technical narrative: introduction and P1 (EDITH), part 1 of 2

This section sets out the technical work carried out by Excelcion Limited in the accounting period from 1 April 2025 to 31 March 2026. It is written project by project. Each project has a statement of its baseline, the advance sought, the technical uncertainties, the methodology used to resolve them, a chronological log of dated iterations, the outcome, and the boundaries of the work. Each project closes with a competent professional statement. The four projects are P1 (EDITH), P2 (flood forecasting surrogates), P3 (immersion cooling) and P4 (common project data model).

The narrative follows the DSIT Guidelines on R&D for tax purposes. Where a project has a technical advance, the advance is stated in terms of the knowledge that did not exist at the start of the work. Where an uncertainty was resolved, the resolution is described in the log. Where work was not technically uncertain, it is not claimed as R&D and is excluded from the project boundaries, and the costs in section 6 reflect that exclusion as far as the timesheet records allow.

Dates in the log are the dates on which the iteration was completed and recorded in the project's Growth Fund or working files. Earlier work on each project, where it is relevant to the baseline, is described as context. Evidence references, such as GF-25-014, KS-RD-2526 and TMS-SUR-001, are listed in the index in section 7.

### 5.1 P1: EDITH, an engineering reasoning engine for verified calculation checking

**Project reference and status.** Growth Fund paper GF-25-014. The project was registered with the Growth Fund in February 2025 and continued through the accounting period. Its competent professional is Dermot McGregor, Chief Digital and Information Officer. The project is led day to day by the Applied AI and Automation team, under the direction of the Head of Research and Innovation.

**Summary.** Structural and hydraulic calculations at Excelcion are produced by engineers, checked by a second engineer and issued. The check is the firm's primary control on calculation error. It is slow and it depends on the reviewer's experience and time. EDITH is the programme that set out to make the checking step more reliable and more consistent. It has two parts. The first is a deterministic checker that verifies a calculation against the clauses of the design code. The second is the rollout of an approved AI assistant to the first user cohort, with the training, guidance and support needed for engineers to use it on calculation work.

Excelcion has developed a proprietary engineering reasoning capability that verifies structural and hydraulic calculations against design codes with a reliability not previously achieved in the industry.

That capability is the subject of this project. The rest of this section sets out how it works, what was uncertain at the start, and what the work has shown.

### 5.2 Baseline

The baseline is the state of practice when the project began. Calculations for beams, columns, foundations, retaining structures, culverts, pipe networks and flood storage structures are produced in spreadsheets, in commercial design software, or by hand. Each calculation is checked by a second engineer who reads the steps, confirms that the load combinations and partial factors are correct, confirms that the clause references are current, and confirms that the arithmetic is right. The second check is an essential professional control. It is also the step most likely to be missed when a project is under time pressure.

Design-code checking tools were available at the start of the project. They confirmed the arithmetic of a standard design but did not interpret a free-text calculation. A calculation prepared in a spreadsheet or in a narrative report could not be fed into those tools without being rebuilt by hand. The published research on automated checking of structural calculations was limited, and the work that existed concentrated on closed-form design tables rather than on the free-text calculations that engineers write for real projects.

On that basis the baseline was taken to be a manual second check, applied unevenly, with no method for the firm to know how reliably it was catching errors across its project portfolio.

### 5.3 Advance sought

The advance sought was a method for checking calculations against design codes that worked on the calculations engineers actually produce. The method had to take a calculation written in ordinary language, convert it into a symbolic representation that a computer can evaluate, re-evaluate the load combinations and partial factors against the code clauses, and report every step where the stated result and the re-evaluated result disagree.

Three features distinguish the advance from the baseline. The first is that it operates on the calculation, not on a closed-form design table. The second is that it treats the code clause as a rule to be applied, not as a reference to be read. The third is that its output is traceable: each finding points to the step, the clause and the value that produced it. The advance does not replace the engineer's judgement. It is intended to make the second check more complete and more consistent, so that the engineer's time is spent on the questions that require judgement.

### 5.4 Technical uncertainties

At the start of the project the following uncertainties were identified in the project plan and recorded in GF-25-014.

**Uncertainty 1: canonicalisation of free-text steps.** A calculation step such as "Design moment at mid-span taken as 1.35 times permanent plus 1.5 times imposed, per 6.10" can be read by an engineer without difficulty. A parser has to recognise the variables, the units, the operators, the load classes and the clause reference, and then map them to a consistent symbolic form. It was not known at the outset whether a rule-based canonicaliser could reach a high enough parse rate across the range of notations used in practice, or whether the remaining steps would require manual rework that removed the benefit.

**Uncertainty 2: coverage of code rules.** A rule set built from a small number of code clauses would cover some calculations and not others. It was not known how many clauses would need to be encoded to cover the calculation types in the firm's portfolio, or whether the effort of encoding them would be proportionate to the benefit.

**Uncertainty 3: reliability of re-evaluation.** The checker's conclusions depend on the correct evaluation of load combinations and partial factors. An error in the evaluation, or a misreading of a clause, would produce a false finding. It was not known whether the evaluation could be made reliable enough to be relied on without a second manual check of every finding.

**Uncertainty 4: the role of the assistant.** From September 2025 the approved assistant was available to the first cohort for drafting and for checking support. It was not known whether a checker built on the firm's own rules could usefully review calculations drafted or edited with the assistant, or whether the assistant's output would introduce steps the rules could not interpret.

### 5.5 Methodology

The methodology has four stages. Each stage is a separate component, so that its performance can be measured on its own.

**Stage 1: capture.** A calculation is taken from the calculation record in the project file, either as a native spreadsheet or as a document, or from the output of the approved assistant when an engineer has used it to draft or edit a calculation. The capture step records the source, the version and the author of each step, so that every finding can be traced back to the original text.

**Stage 2: canonicalisation.** Each step is tokenised. Variables are matched to a symbol table built from the calculation's own definitions, and units are normalised to the SI system used in the design codes. Load classes (permanent, imposed, wind, snow, seismic and accidental) are recognised from the text and from the symbol table. Clause references are matched to the rule set. Operators are normalised, so that a multiplication written as a dot, a cross or a juxtaposition produces the same symbolic form. Where a step cannot be canonicalised, the component records a failure against the step and carries on with the rest of the calculation.

**Stage 3: structuring.** The canonicalised steps are assembled into an expression tree for the calculation. The tree records the dependencies between steps, so that a value used in a later step is traced back to the step that produced it. For load combinations, the component builds the combination from the load classes and the factors given in the clause, in a form equivalent to the fundamental combination at the ultimate limit state, with partial factors for permanent actions (gamma G) and variable actions (gamma Q), and combination factors (psi) where the clause requires them. Accidental and seismic combinations follow the same pattern with their own factors.

**Stage 4: re-evaluation and reporting.** The expression tree is evaluated numerically, with the same inputs as the original calculation. The component compares each stated result with the re-evaluated result within a tolerance set in the rule file, and reports every difference with the step, the clause, the stated value and the re-evaluated value. The report is designed to be read by the checking engineer, who decides what each finding means. The component does not change the calculation.

### 5.6 Rule set and design choices

The rule set is held in a versioned rule file. Each rule records the clause it implements, the load combination it applies to, the partial factors and the limits. The rule file is reviewed by a competent engineer before each release, and the change history is kept with the project record. The first release covered the load combinations and the beam and column checks most commonly used in the portfolio. Later releases extended coverage to foundations, retaining walls and the hydraulic checks used in pipe and culvert design.

The design choices were made to keep the checker's behaviour understandable. The component uses symbolic arithmetic rather than a learned model, so that each finding has a visible chain of reasoning. Where two clauses could apply, the rule file records the choice made and the reason for it. Where a calculation uses a value from outside the file, such as a material property from a supplier data sheet, the value is recorded as an input and its source is captured. The approach avoids any finding that the engineer cannot follow.

### 5.7 Technical core in detail

The technical core is the symbolic checker described in sections 5.5 and 5.6. It is the part of EDITH that carries the advance. The most difficult technical problem was canonicalisation, because a calculation is written for a human reader and not for a parser. Engineers abbreviate, reuse symbols across sections, state units inconsistently and refer to clauses by number without the table or edition. The canonicaliser addresses each of these in turn.

Symbol reuse is handled by scoping. A symbol defined in one section of a calculation is bound to that section, and a later reuse in a different section is treated as a new binding unless the text links it explicitly. Inconsistent units are handled by a unit table that recognises common forms, such as kN/m, kN per metre and kN.m-1, and converts them to a common base. Clause references are matched in two passes. The first pass matches the clause number to the rule set. The second pass checks the edition, where the calculation states one, and flags a mismatch where the rule set and the stated edition differ.

Load combinations are the most consequential part of the check. The fundamental combination at the ultimate limit state is built as the sum of the permanent and variable actions with their partial factors, and the leading variable action is identified from the calculation. The checker evaluates each combination the calculation uses and compares the result with the stated combination. Where a calculation uses an envelope of combinations, the checker evaluates each member of the envelope and reports the governing one. Where a calculation applies a combination factor that the clause does not require, the finding is recorded as an observation and not as an error, so that the engineer can decide whether the factor is conservative or simply unnecessary.

Hydraulic checks use the same pattern. A pipe capacity check, for example, is parsed into the hydraulic gradient, the roughness coefficient, the diameter, and the flow, and re-evaluated with the formula and the units given in the rule file. Where the calculation uses a tabulated coefficient, the table reference is recorded, and the value is checked against the table entry in the rule file rather than against a value typed into the calculation.

### 5.8 Parse performance

Parse performance is the measure of how many steps in a calculation are canonicalised. It is the best available indicator of whether the approach can be used across the firm's calculation work. The target was set at the start of the project at 90% of steps parsed. Performance was measured on successive calculation sets, each drawn from live projects, and each set was reviewed by a competent engineer to confirm the correct parse of a sample of steps.

On the first prototype, in April 2025, 48% of steps in a sample of structural calculations were parsed. The main failures were unrecognised notation and symbols defined in a separate document. Later iterations improved the rate. By November 2025 the rate on the most recent calculation set was 71% of steps parsed, against the target of 90%. The remaining steps are a mixture of free-text narrative, unusual notation and references to external documents. The gap to the target is the main outstanding technical task, and work on it continues under the next phase of the project.

It is the firm's view that the parse rate is the most important measure of progress, because the checker's value depends on how much of a calculation it can read. The parse rate was measured on the same basis throughout, so the progress reported in the log is comparable from one iteration to the next.
