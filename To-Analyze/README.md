# To-Analyze

Queue of companies awaiting analysis. Contents:

- `shortlist_YYYY-MM-DD.txt` — written by the SCREENING AGENT (../screening.md, Part 1).
- `<TICKER>/` — one folder per queued company, built by the COLLECTION AGENT (../collection.md, Part 2): `manifest.json` (ledger of every fetched document — the no-repeat mechanism), `data/` (10-yr financial CSVs + optional export.xlsx), `docs/` (annual-reports / credit-ratings / concalls / announcements / ipo, each PDF with a sibling `.txt` carrying `[p.N]` page markers), `collection_notes.md`.
- `collection_log.txt` — one line per company per collection run.

Humans can also drop screener exports, annual reports, or a note naming a ticker.

Per company, the run follows strategy.md: 60-second glance (§1) → template dashboard (§16b, using ../DrVijayMalik_Screener_Excel_Template_v3.2.xlsx or the on-the-fly recipe) → §0 archetype triage + sixteen kill-tests (§0a) → full gates (§2–§11) → verdict. Finished analyses move to Holdings/ (if bought) or get archived with an AVOID/REJECT note.
