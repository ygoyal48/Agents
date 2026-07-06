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
│   ├── credit-ratings/        <AGENCY>_<YYYY-MM-DD>.(pdf|html)+.txt  (ALL listed reports, all agencies; many are HTML rationale pages, not PDFs — save the .html and extract .txt from it)
│   ├── concalls/              Concall_<YYYY-MM>_<transcript|ppt|notes>.pdf/.txt (all listed; use the publish month — see §5 naming note)
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
  Shareholding Pattern, Peer comparison → scrape into `data/*.csv`.
- **"Documents" section** (public): → **Annual Reports** (links to BSE/NSE-hosted PDFs per FY — some NSE ones arrive
  as `.zip`; unzip and keep the inner PDF), **Credit ratings** (CRISIL/ICRA/CARE/India Ratings/Infomerics — often
  HTML rationale pages, not PDFs), **Concalls** (transcript/PPT/notes links).
- **Announcements**: the page's inline list is only the ~5 most recent items — NOT the 24-month window. For the full
  feed you MUST follow the BSE link and scrape BSE's announcements API/page (NSE times out in this environment; BSE
  works). Capture 24 months of metadata into `announcements/index.csv` (date, title, category, url), then download
  PDFs for MATERIAL items only (§5.4).
- **Export to Excel** (login only): if a session exists, fetch to `data/export.xlsx`. If not, skip silently —
  the CSVs carry the same numbers; note `"export": "skipped-no-login"` in collection_notes.md.

**LOGIN-DEPENDENT DATA (know this before you start):** anonymous scraping gets you the main financial tables, but
two contract items need a logged-in screener session (reuse the login recipe in `screening.md` §7):
- **Peer-comparison table** (`/api/company/<id>/peers/`) — 404s anonymously; `peers.csv` is otherwise a placeholder.
- **Promoter-pledge %** (the shareholding schedule sub-row) — not served anonymously; without login `shareholding.csv`
  carries promoter/FII/DII/public % but NOT pledge %. Record which you captured in `collection_notes.md`.
If no session is available, write these as best-effort with a note rather than failing the company.

**BSE returns HTTP 403 to non-browser requests.** Every BSE-hosted download (annual reports, announcement PDFs, some
concalls) fails silently unless you send a browser `User-Agent` (a normal Chrome UA string) AND a
`Referer: https://www.screener.in/` header. Set both on all BSE fetches. (The manifest's incremental-retry recovers
these on a re-run, but set the headers up front.)

If a link 404s or an agency page is paywalled, record `parse_status: skipped-paywall`/`download-failed` and move on —
never stall a whole run on one document. Note: SME RHP/DRHP documents on SEBI are usually behind a JS-rendered landing
page with no static PDF link — save the SEBI index page + note it in collection_notes.md; the offer doc may be
unreachable without a browser.

## 5. PER-COMPANY PROCEDURE

1. Resolve ticker → screener URL (try consolidated; fall back to standalone and set `consolidated_available: false`).
2. Create the folder tree (§2) if absent; load or initialize `manifest.json`.
3. **Refresh `data/*.csv`** from the page tables (every run).
4. **Diff the Documents section against the manifest** (§3 rule) and fetch what's new:
   - Annual reports: all listed FYs (target the last 10; take everything offered). Name `AR_FY<YYYY>.pdf`.
   - Credit ratings: every listed report. Name `<AGENCY>_<date>.pdf`.
   - Concalls: every listed transcript/PPT/notes. **Naming:** screener only exposes the publish month, and its
     FY-quarter mapping is ambiguous, so name by publish month — `Concall_<YYYY-MM>_<transcript|ppt|notes>.pdf` — not
     by FY-quarter. Audio/video ("REC" / YouTube) links are non-text: skip them, note in collection_notes.md.
   - Announcements: refresh `index.csv` (24-month window). Download the PDF for MATERIAL items only — title matches any of:
     `results | investor presentation | order | contract | acquisition | merger | demerger | scheme | preferential |
      warrant | rights issue | QIP | buyback | dividend | bonus | split | pledge | resignation | appointment of
      auditor | auditor | credit rating | SEBI | penalty | fine | clarification | restructuring | one time settlement |
      default | insolvency | NCLT | open offer | delisting | name change | object clause | MOU | joint venture`.
   - If tagged SME/RECENT-IPO: fetch the RHP/DRHP via the exchange/SEBI link into `docs/ipo/`.
5. **Extract text from every downloaded PDF** to a sibling `.txt` (same basename). Tooling is NOT preinstalled —
   bootstrap it first: `apt-get update && apt-get install -y poppler-utils` (gives `pdftotext`), or
   `pip install pdfplumber`. REQUIREMENTS: (a) preserve reading order; (b) insert page markers
   `[p.N]` at each page break — the analysis cites page numbers, this is not optional; (c) if a PDF is scanned/
   image-only and OCR is unavailable, keep the raw file, set `parse_status: text-extraction-failed` (no OCR fallback
   exists here). For HTML credit-rating pages, extract the visible text to `.txt` the same way.
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
- **STORAGE POLICY — do NOT commit raw binaries.** Raw PDFs/xlsx/zip/HTML are large (these grew to ~370 MB for just
  2 companies; all-23 would be multiple GB). The repo `.gitignore` excludes `To-Analyze/**/*.pdf`, `*.xlsx`, `*.zip`,
  and `docs/**/*.html`. **Commit only** the extracted `docs/**/*.txt`, `data/*.csv`, `manifest.json`,
  `collection_notes.md`, `announcements/index.csv`, and `collection_log.txt` — that is the entire corpus the analysis
  agent reads. The raw files stay on the local disk (re-fetchable any time from the manifest's `url` fields) but are
  never pushed. Do not `git add -f` a raw document.
- Commit at the end of the run if git access exists (message: `Collect docs: <tickers> (<N> new documents)`).

## 7. BOUNDARIES (what you must NOT do)

- No reading-for-meaning, no summaries, no red-flag hunting, no verdicts — text extraction is mechanical.
- No screening (Part 1), no analysis (`strategy.md`), no edits to any `.md` instruction file or the Excel template.
- Do not delete or rewrite previously collected files; new versions of a document get a new entry (URL-keyed).

**Handoff:** the analysis agent starts from `To-Analyze/<TICKER>/` — `manifest.json` tells it what exists and what's
fresh since its last look; `data/` gives it the 10-yr numbers for the dashboard; `docs/**/*.txt` gives it the
readable corpus with `[p.N]` citations. Your run ends when every queued company's manifest is up to date.
