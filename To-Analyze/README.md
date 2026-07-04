# To-Analyze

Queue of companies awaiting analysis. Populated primarily by the SCREENING AGENT (../screening.md — Part 1 of the pipeline), which writes `shortlist_YYYY-MM-DD.txt` files here in its documented format. Humans can also drop screener exports, annual reports, or a note naming a ticker.

Per company, the run follows strategy.md: 60-second glance (§1) → template dashboard (§16b, using ../DrVijayMalik_Screener_Excel_Template_v3.2.xlsx or the on-the-fly recipe) → §0 archetype triage + sixteen kill-tests (§0a) → full gates (§2–§11) → verdict. Finished analyses move to Holdings/ (if bought) or get archived with an AVOID/REJECT note.
