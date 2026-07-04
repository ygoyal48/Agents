# COLLECTION — Part 2 of the Peaceful Investing pipeline (STANDALONE — for the collection agent)

> **READ THIS FIRST — who runs this file and what it produces.**
> This file is the COMPLETE instruction set for the COLLECTION AGENT. Do NOT read `strategy.md` (analysis is not your
> job) and do NOT re-run `screening.md` (the shortlist is your INPUT). Your entire mission:
> **for every company queued in `To-Analyze/`, download all decision-relevant documents and data from its
> screener.in page (and the exchange links it points to), save the raw files AND extracted text into that company's
> folder, and maintain a manifest so the NEXT run fetches only documents published since the last run.**
> You make NO buy/sell/avoid judgements, extract NO conclusions, and write NO analysis.

---

## 1. INPUT

- The newest `To-Analyze/shortlist_*.txt` (format: `Name | Ticker | Mcap | P/E | D/E | Sales10yCAGR | CFO | Tags`),
  plus any older shortlist files whose companies still lack a folder.
- A company may also be queued ad-hoc as a bare folder or note dropped in `To-Analyze/` by the user — treat any
  ticker it names identically.
- Process order: newest shortlist first; within a shortlist, top to bottom. Re-visit EVERY existing company folder
  at the end of each run to check for newly published documents (that check is the core of your job, not an extra).

## 2. FOLDER CONTRACT (create exactly this per company)

```
To-Analyze/<TICKER>/
├── manifest.json              ← the ledger (see §3) — the single source of truth for "already done"
├── data/                      ← machine-readable financials from the screener page
│   ├── pnl_annual.csv         (10-yr P&L rows as displayed, consolidated)
│   ├── balance_sheet.csv
│   ├── cash_flow.csv
│   ├── quarters.csv           (all quarterly rows shown)
│   ├── ratios.csv             (screener's ratio rows: ROCE/ROE/debtor days/etc.)
│   ├── shareholding.csv       (quarterly promoter/FII/DII/public %, PLUS promoter-pledge % — every quarter shown)
│   ├── peers.csv              (the peer-comparison table)
│   └── export.xlsx            (screener "Export to Excel" — ONLY if a logged-in session is available; else skip, note in manifest)
├── docs/
│   ├── annual-reports/        AR_FY2024.pdf + AR_FY2024.txt   (target: last 10 FYs, more if listed)
│   ├── credit-ratings/        <AGENCY>_<YYYY-MM-DD>.pdf/.txt  (ALL listed rating reports, all agencies)
│   ├── concalls/              Concall_<FYqQ>_<transcript|ppt|notes>.pdf/.txt (all listed)
│   ├── announcements/         index.csv (ALL announcements, 24 months) + <YYYY-MM-DD>_<slug>.pdf/.txt for MATERIAL ones (§5.4)
│   └── ipo/                   RHP/DRHP pdf+txt (only if Tags contain SME or RECENT-IPO — fetch from exchange/SEBI link)
└── collection_notes.md        ← free-form: what could not be fetched and why, paywalls, dead links, oddities
```

**Consolidated first:** wherever screener offers standalone vs consolidated, capture CONSOLIDATED (and note in
manifest if only standalone exists — the analysis agent needs to know that fact).

## 3. THE MANIFEST (the no-repeat mechanism — maintain it religiously)

`manifest.json` schema:

```json
{
  "company": "Vinati Organics Ltd",
  "ticker": "VINATIORGA",
  "screener_url": "https://www.screener.in/company/VINATIORGA/consolidated/",
  "tags": ["..."],
  "first_collected": "YYYY-MM-DD",
  "last_run": "YYYY-MM-DD",
  "collection_status": "complete | partial | failed",
  "consolidated_available": true,
  "documents": [
    {
      "url": "<canonical source URL — the dedupe KEY>",
      "type": "annual-report | credit-rating | concall-transcript | concall-ppt | announcement | rhp | data-page",
      "period": "FY2024 | 2024-Q3 | 2025-01-15",
      "title": "<as listed on screener/exchange>",
      "fetched_at": "YYYY-MM-DD",
      "sha256": "<hash of the downloaded file>",
      "bytes": 1234567,
      "saved_as": "docs/annual-reports/AR_FY2024.pdf",
      "text_as": "docs/annual-reports/AR_FY2024.txt",
      "parse_status": "ok | text-extraction-failed | download-failed | skipped-paywall"
    }
  ]
}
```

**The incremental rule (the whole point):** on every run, list the documents the screener page (and its Documents
section) CURRENTLY offers → compare each item's URL against `documents[].url` in the manifest →
- **URL present with `parse_status: ok`** → SKIP (never re-download, never re-parse).
- **URL present with a failed status** → retry (max 2 retries per run; leave the failure recorded if still failing).
- **URL absent** → NEW document → download, extract text, append a manifest entry.
- The `data/` tables are refreshed on EVERY run (they change with each quarter) — overwrite the CSVs, update the
  single `data-page` manifest entry's `fetched_at`. Financial-table refresh is cheap; documents are the expensive part.

Never delete manifest entries. If a document disappears from the source, keep the entry (the file is already saved).

## 4. WHERE THINGS LIVE ON SCREENER (the source map)

On `screener.in/company/<TICKER>/consolidated/`:
- **Financial tables** (public, no login): Quarterly Results, Profit & Loss, Balance Sheet, Cash Flows, Ratios,
  Shareholding Pattern (with quarterly pledge % under promoters), Peer comparison → scrape into `data/*.csv`.
- **"Documents" section** (public): → **Annual Reports** (links to BSE-hosted PDFs per FY), **Credit ratings**
  (links to CRISIL/ICRA/CARE/India Ratings/Infomerics report pages/PDFs), **Concalls** (transcript/PPT/notes links).
- **Announcements**: the page links recent ones; the full feed is on BSE/NSE (follow the BSE link on the page).
  Capture 24 months of metadata into `announcements/index.csv` (date, title, category, url).
- **Export to Excel** (login only): if a session exists, fetch to `data/export.xlsx`. If not, skip silently —
  the CSVs carry the same numbers; note `"export": "skipped-no-login"` in collection_notes.md.

If a link 404s or an agency page is paywalled, record `parse_status: skipped-paywall`/`download-failed` and move on —
never stall a whole run on one document.

## 5. PER-COMPANY PROCEDURE

1. Resolve ticker → screener URL (try consolidated; fall back to standalone and set `consolidated_available: false`).
2. Create the folder tree (§2) if absent; load or initialize `manifest.json`.
3. **Refresh `data/*.csv`** from the page tables (every run).
4. **Diff the Documents section against the manifest** (§3 rule) and fetch what's new:
   - Annual reports: all listed FYs (target the last 10; take everything offered). Name `AR_FY<YYYY>.pdf`.
   - Credit ratings: every listed report. Name `<AGENCY>_<date>.pdf`.
   - Concalls: every listed transcript/PPT/notes. Name `Concall_<FY><Q>_<kind>.pdf`.
   - Announcements: refresh `index.csv` (24-month window). Download the PDF for MATERIAL items only — title matches any of:
     `results | investor presentation | order | contract | acquisition | merger | demerger | scheme | preferential |
      warrant | rights issue | QIP | buyback | dividend | bonus | split | pledge | resignation | appointment of
      auditor | auditor | credit rating | SEBI | penalty | fine | clarification | restructuring | one time settlement |
      default | insolvency | NCLT | open offer | delisting | name change | object clause | MOU | joint venture`.
   - If tagged SME/RECENT-IPO: fetch the RHP/DRHP via the exchange/SEBI link into `docs/ipo/`.
5. **Extract text from every downloaded PDF** to a sibling `.txt` (same basename). Use any available tool
   (pdftotext / python pdfplumber / etc.). REQUIREMENTS: (a) preserve reading order; (b) insert page markers
   `[p.N]` at each page break — the analysis cites page numbers, this is not optional; (c) if a PDF is scanned/
   image-only and OCR is unavailable, keep the PDF, set `parse_status: text-extraction-failed`.
6. Update the manifest (every fetched doc gets an entry with sha256), set `last_run`, set `collection_status`:
   `complete` (everything listed was fetched or already present) / `partial` (some failures — list them in
   collection_notes.md) / `failed` (page unreachable).
7. Append one line to `To-Analyze/collection_log.txt`:
   `YYYY-MM-DD | <TICKER> | new-docs: N | refreshed-data: yes | status: complete|partial|failed`.

## 6. RUN-LEVEL RULES

- **Scope: `To-Analyze/` companies only.** (Holdings monitoring is a different pipeline part; do not touch `Holdings/`.)
- A company folder whose analysis is finished may be moved out by other agents — if a folder named in an old
  shortlist no longer exists AND the name appears under `Holdings/`, skip it.
- Be polite to sources: sequential fetches, no hammering; resume-safe (the manifest makes any interrupted run
  restartable — just run again).
- Everything you save is text/PDF/CSV — no screenshots needed. Keep file names EXACTLY per the patterns above;
  the analysis agent globs on them.
- Commit at the end of the run if git access exists (message: `Collect docs: <tickers> (<N> new documents)`).

## 7. BOUNDARIES (what you must NOT do)

- No reading-for-meaning, no summaries, no red-flag hunting, no verdicts — text extraction is mechanical.
- No screening (Part 1), no analysis (`strategy.md`), no edits to any `.md` instruction file or the Excel template.
- Do not delete or rewrite previously collected files; new versions of a document get a new entry (URL-keyed).

**Handoff:** the analysis agent starts from `To-Analyze/<TICKER>/` — `manifest.json` tells it what exists and what's
fresh since its last look; `data/` gives it the 10-yr numbers for the dashboard; `docs/**/*.txt` gives it the
readable corpus with `[p.N]` citations. Your run ends when every queued company's manifest is up to date.
