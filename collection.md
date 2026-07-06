# COLLECTION — Part 2 of the Peaceful Investing pipeline (STANDALONE — for the collection agent)

> **READ THIS FIRST — who runs this file and what it produces.**
> This file is the COMPLETE instruction set for the COLLECTION AGENT. Do NOT read `strategy.md` (analysis is not your
> job) and do NOT re-run `screening.md` (the shortlist is your INPUT). Your entire mission:
> **for every company queued in `To-Analyze/`, fetch its four document types from screener.in (annual reports,
> credit-rating reports, concalls, material announcements), extract each to text, and APPEND that text into ONE
> aggregated `.txt` file per type — each file carrying a "last-saved" marker so the NEXT run only fetches documents
> published since the last run.**
> You do NOT scrape financial tables/CSVs, you do NOT fetch IPO/DRHP docs, and you make NO buy/sell/avoid judgements,
> extract NO conclusions, and write NO analysis. Collection is purely mechanical fetch + text-extract + append.

---

## 1. INPUT

- The newest `To-Analyze/shortlist_*.txt` (format: `Name | Ticker | Mcap | P/E | D/E | Sales10yCAGR | CFO | Tags`),
  plus any older shortlist files whose companies still lack a folder.
- A company may also be queued ad-hoc as a bare folder or note dropped in `To-Analyze/` by the user — treat any
  ticker it names identically.
- Process order: newest shortlist first; within a shortlist, top to bottom. Re-visit EVERY existing company folder
  at the end of each run to check for newly published documents (that check is the core of your job, not an extra).

## 2. FOLDER CONTRACT (create exactly this per company — four text files, nothing else)

```
To-Analyze/<TICKER>/
├── annual-reports.txt     ← every annual report, one section per FY (target the last 10 FYs, more if offered)
├── credit-ratings.txt     ← every rating report, all agencies, one section per report
├── concalls.txt           ← every concall transcript / PPT / notes, one section per call
├── announcements.txt      ← MATERIAL announcements only (§5.4), one section per announcement
└── collection_notes.md    ← free-form: what could not be fetched and why (paywalls, dead links, image-only PDFs)
```

No `data/`, no `manifest.json`, no per-document files, no raw PDFs in the repo. Raw downloads go to a scratch/temp
directory, get text-extracted, then are discarded — only the aggregated `.txt` files (+ notes) are kept and committed.

**Consolidated first:** read the Documents section from `screener.in/company/<TICKER>/consolidated/`; fall back to the
standalone page if consolidated does not exist, and say so in `collection_notes.md`.

### 2a. AGGREGATED FILE FORMAT (identical shape for all four files)

A header block, then one `=====` section per document, oldest first / newest last:

```
# <TICKER> — ANNUAL REPORTS
# last-saved: FY2025            ← the incremental checkpoint (newest doc key captured) — see §3
# last-run: 2026-07-06
# captured: 10 (FY2016 … FY2025)
# source: https://www.screener.in/company/<TICKER>/consolidated/

===== ANNUAL REPORT | key: FY2016 | title: <as listed> | url: <source url> | fetched: 2026-07-06 =====
[p.1] …extracted text…
[p.2] …
===== ANNUAL REPORT | key: FY2017 | title: … | url: … | fetched: 2026-07-06 =====
[p.1] …
```

- The `key: <…>` in each section header is the **dedupe key** (see §3 for the per-type key).
- Page markers `[p.N]` at every page break are MANDATORY — the analysis agent cites page numbers.
- Same layout for `credit-ratings.txt`, `concalls.txt`, `announcements.txt` (swap the section label and key type).

## 3. THE "LAST-SAVED" MARKER (the no-repeat mechanism — this replaces the old manifest)

Each aggregated file's `# last-saved:` header line is the checkpoint. **The dedupe key per type:**

| File | key format | example |
|---|---|---|
| annual-reports.txt | `FY<YYYY>` | `FY2025` |
| credit-ratings.txt | `<AGENCY>_<YYYY-MM-DD>` | `CRISIL_2025-03-14` |
| concalls.txt | `<YYYY-MM>_<kind>` (publish month; FY-quarter is ambiguous on screener) | `2025-05_transcript` |
| announcements.txt | `<YYYY-MM-DD>_<slug>` | `2025-01-15_order-win` |

**The incremental rule (the whole point) — for each of the four files, every run:**
1. If the file does not exist yet → first collection → fetch everything the source offers (up to the §5 limits).
2. If it exists → read `# last-saved:` (the newest key already captured). List what the source currently offers.
   Fetch only documents whose key is **newer than `last-saved`** AND whose `key:` does not already appear in a
   `=====` section header in the file. Skip everything else (never re-download, never re-parse).
3. Append each newly fetched document as a new `=====` section (keep sections in ascending key order).
4. Update the header: set `# last-saved:` to the newest key now in the file, refresh `# last-run:` and `# captured:`.

Never delete or rewrite existing sections. If a document later disappears from the source, its section stays (the
text is already saved). If a fetch fails, do NOT advance `last-saved` past it — record it in `collection_notes.md`
and retry next run (max 2 retries per run).

## 4. WHERE THINGS LIVE ON SCREENER (the source map)

Read the **"Documents" section** of `screener.in/company/<TICKER>/consolidated/` (public, no login needed):
- **Annual Reports** — links to BSE/NSE-hosted PDFs per FY. Some NSE ones arrive as `.zip`; unzip and keep the inner PDF.
- **Credit ratings** — CRISIL / ICRA / CARE / India Ratings / Infomerics. These are OFTEN HTML rationale pages, not
  PDFs — fetch the page and extract its visible text the same way.
- **Concalls** — transcript / PPT / notes links. Audio/video ("REC" / YouTube) links are non-text: skip them, note it.
- **Announcements** — the screener page shows only the ~5 most recent items, NOT the 24-month window. For the full
  feed you MUST follow the BSE link and scrape BSE's announcements feed (NSE times out in this environment; BSE works),
  then keep MATERIAL items only (§5.4).

**BSE returns HTTP 403 to non-browser requests.** Every BSE-hosted fetch (annual reports, announcement PDFs, some
concalls) fails silently unless you send a browser `User-Agent` (a normal Chrome UA string) AND a
`Referer: https://www.screener.in/` header. Set both up front on all BSE requests.

If a link 404s or a page is paywalled, record it in `collection_notes.md` and move on — never stall a whole run on
one document. (No login is required for any of the four document types; a screener login, per `screening.md` §7, is
only needed if you ever want financial tables/peers — which this pipeline no longer collects.)

## 5. PER-COMPANY PROCEDURE

1. Resolve ticker → screener URL (try `/consolidated/`; fall back to standalone, note it).
2. Ensure the company folder exists. For each of the four `.txt` files, read its `# last-saved:` marker (treat a
   missing file as "nothing saved yet").
3. **Bootstrap text tooling once** (not preinstalled): `apt-get update && apt-get install -y poppler-utils` (gives
   `pdftotext`), or `pip install pdfplumber`.
4. For each document type, list what the source offers and fetch only the NEW ones (§3 rule). Per type:
   - **Annual reports:** target the last 10 FYs (take everything offered beyond that if cheap). key `FY<YYYY>`.
   - **Credit ratings:** every listed report, all agencies. key `<AGENCY>_<YYYY-MM-DD>`.
   - **Concalls:** every listed transcript/PPT/notes. key `<YYYY-MM>_<kind>` (publish month). Skip audio/video links.
   - **Announcements:** from BSE's 24-month feed, keep only MATERIAL items — title matches any of:
     `results | investor presentation | order | contract | acquisition | merger | demerger | scheme | preferential |
      warrant | rights issue | QIP | buyback | dividend | bonus | split | pledge | resignation | appointment of
      auditor | auditor | credit rating | SEBI | penalty | fine | clarification | restructuring | one time settlement |
      default | insolvency | NCLT | open offer | delisting | name change | object clause | MOU | joint venture`.
     key `<YYYY-MM-DD>_<slug>`.
5. **Download each new document to a scratch dir, extract its text, then APPEND a `=====` section (§2a) to the
   matching aggregated `.txt`.** Text-extraction REQUIREMENTS: (a) preserve reading order; (b) insert `[p.N]` page
   markers at each page break — not optional; (c) if a PDF is scanned/image-only and OCR is unavailable, skip the
   text but still record the doc in `collection_notes.md` with reason `image-only` and do NOT advance `last-saved`
   past it. For HTML rating pages, extract the visible text.
6. Update each file's header marker (`last-saved`, `last-run`, `captured`) to reflect what is now in the file.
7. Append one line to `To-Analyze/collection_log.txt`:
   `YYYY-MM-DD | <TICKER> | new: AR=<n> CR=<n> CC=<n> ANN=<n> | status: complete|partial|failed`
   (`complete` = everything offered was fetched or already present; `partial` = some failures, listed in notes;
   `failed` = page unreachable).

## 6. RUN-LEVEL RULES

- **Scope: `To-Analyze/` companies only.** (Holdings monitoring is a different pipeline part; do not touch `Holdings/`.)
- A company folder whose analysis is finished may be moved out by other agents — if a folder named in an old
  shortlist no longer exists AND the name appears under `Holdings/`, skip it.
- Be polite to sources: sequential fetches, no hammering. The run is resume-safe — the `last-saved` markers make any
  interrupted run restartable; just run again.
- **STORAGE POLICY — only the four `.txt` files + `collection_notes.md` are committed.** Raw PDFs/HTML/zip are large
  (an earlier full-doc run grew to ~370 MB for just 2 companies) and are NEVER committed — download them to a scratch
  dir, extract, discard. The repo `.gitignore` excludes `To-Analyze/**/*.pdf`, `*.xlsx`, `*.zip`, `docs/**/*.html`
  as a safety net; do not `git add -f` a raw document.
- Commit at the end of the run if git access exists (message: `Collect docs: <tickers> (<N> new documents)`).

## 7. BOUNDARIES (what you must NOT do)

- No reading-for-meaning, no summaries, no red-flag hunting, no verdicts — text extraction is mechanical.
- No screening (Part 1), no analysis (`strategy.md`), no financial-table/CSV scraping, no IPO/DRHP fetching,
  no edits to any `.md` instruction file or the Excel template.
- Do not delete or rewrite previously saved sections; only APPEND new ones and update the header marker.

**Handoff:** the analysis agent starts from `To-Analyze/<TICKER>/` and reads the four aggregated `.txt` files —
`annual-reports.txt`, `credit-ratings.txt`, `concalls.txt`, `announcements.txt` — each a `[p.N]`-cited corpus whose
`# last-saved:` marker tells it (and your next run) how fresh the file is. Your run ends when every queued company's
four files are up to date.
