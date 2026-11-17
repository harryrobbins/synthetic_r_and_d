# Synthetic R&D tax claims (HMRC hackathon dataset)

There are 11 fictional UK R&D tax relief claim packs (about 10–17k words each, roughly 20–40 pages). They range from exemplary to fraudulent, and include a group of three companies claiming the same project.

- `claims/<ID>-<slug>/claim.md` holds the claim packs. **These are the only files to give to tools under test.**
- `docs/guide-to-rd-claims.md` is the participant briefing: the scheme, the anatomy of a claim, the grading rubric and the red-flag catalogue.
- `docs/cohort-plan.md` and `docs/answer-key.{md,json}` are **organiser-only** ground truth.
- `plans/` holds the per-claim writing plans and cost schedules used to generate the packs.
- `scripts/`:
  - `costs.py` produces the cost schedules and figures.
  - `answer_key.py` builds the answer key.
  - `assemble.py` concatenates sections into `claim.md`.
  - `check.py` checks the packs for consistency and safety.

```
python3 scripts/costs.py && python3 scripts/answer_key.py
python3 scripts/assemble.py && python3 scripts/check.py
```

**Safety.** Every company, person, product and figure is invented. Identifiers are deliberately invalid: company numbers use the `ZZ` prefix, UTRs are `99999…`, and postcodes use the `ZZ` area. So none can match a real entity, and none would pass a real HMRC or Companies House check. Every pack carries a "SYNTHETIC TEST DATA" banner.

**The exception is Excelcion (C11).** It is a synthetic company with its own (access-controlled) website at `www.excelcion.co.uk`, so that web-search tools can test claims against a public footprint.
