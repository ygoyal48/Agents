---
name: screener-index-screen
description: Run an authenticated screener.in stock screen (any query in screener's query language — dividend yield, P/E, ROCE, debt/equity, sales growth, etc.) and filter the results down to the constituents of a specific NSE index (Nifty 50, Nifty Next 50, Nifty 100, Nifty 500, Nifty Bank, sector indices, ...). Use this whenever the user asks for stocks matching some financial criterion that are "part of" / "in" / "from" an index — e.g. "dividend yield above 2% in Nifty50", "low P/E stocks in Nifty Bank", "high ROCE Nifty500 companies" — or more generally whenever they want to "use my screener id/pass" or "screener.in login" to pull a list of stocks. Also use this to extend or automate the manual login+query recipe documented in this repo's screening.md (Part 1 of the Peaceful Investing pipeline) — that file's baseline growth screen is one fixed query; this skill is the general, parameterized, reusable version for any query + any index.
---

# Screener.in index-filtered stock screen

## What this does

Logs into screener.in with the user's own credentials (screener.in query language
only returns full/custom results to logged-in users — anonymous requests redirect
to `/login/`), runs an arbitrary query against screener's **entire ~5,000-company
universe**, paginates through every results page, then intersects the results
against the official NSE constituent list for a chosen index (Nifty 50 by default).
screener.in has no native "restrict to index X" filter, so the index membership
check happens as a second step against niftyindices.com's own published CSVs —
not by guessing or hardcoding a stock list that will go stale.

Everything is done via `scripts/screen_by_index.py`, which encodes every gotcha
discovered by running this manually (see "Why a script, not ad-hoc curl" below).
**Always run the script rather than re-deriving the login/pagination/parsing
logic from scratch** — it already handles the header-row-repeats-mid-table trap,
the need-all-pages trap, and the niftyindices-blocks-default-user-agent trap.

## How to run it

1. **Get credentials.** Check `SCREENER_USER` / `SCREENER_PASS` in the environment
   first. If unset, ask the user for their screener.in email + password (a free
   account is enough — the login just needs to succeed, no paid features are used).
   Tell them plainly: used only for this run, exported as local env vars, never
   written to any file or committed. A user may instead prefer to run the screen
   in their own browser and paste you the results — that's a legitimate zero-secret
   alternative if they're hesitant to share credentials.

2. **Pick the query.** Translate the user's ask into screener's query language.
   Common fields: `Dividend yield`, `Price to Earning`, `Debt to equity`,
   `Return on capital employed`, `Sales growth 10Years`, `Market Capitalization`,
   `Return on equity`. Combine with `AND`. If a field name errors, screener.in's
   own query-builder autocomplete (at `/screen/new/`, browser only) shows the exact
   current name — field names occasionally get renamed.

3. **Pick the index.** `--index nifty50` covers the common ones out of the box
   (see `KNOWN_INDEXES` in the script). For anything else, niftyindices.com hosts
   a CSV for essentially every NSE index at a predictable URL
   (`https://niftyindices.com/IndexConstituent/ind_nifty<name>list.csv`) — pass it
   directly via `--index-url` if it's not in the known list. Verify an unfamiliar
   URL guess actually returns CSV (not an HTML error page) before relying on it.

4. **Run it:**

   ```bash
   export SCREENER_USER='user@example.com'
   export SCREENER_PASS='their-password'
   python3 scripts/screen_by_index.py \
     --query "Dividend yield > 2" \
     --index nifty50 \
     --sort "Div Yld%" \
     --format markdown
   unset SCREENER_USER SCREENER_PASS
   ```

   Requires `requests` and `beautifulsoup4` (`pip install requests beautifulsoup4`
   if missing). `--sort` must match one of the column headers the script prints
   to stderr on the run (headers are read live from screener's own table, not
   hardcoded, since they can shift slightly depending on the query) — omit it to
   leave results in screener's default order.

5. **Present the output** as a markdown table (the script's default format
   already is one). Report the three summary lines the script prints to stderr
   (universe size, index size, match count) so the user can see the funnel, not
   just the final list.

6. **State the caveat every time:** this is a screen, not a recommendation — it
   surfaces companies that pass a mechanical filter, not a buy/sell judgment.
   (Same convention this repo's `screening.md` uses: "a screen is a funnel, not
   a buy signal.")

7. **No manual cleanup needed** — the script keeps the session cookie in memory
   only (a `requests.Session`, never written to disk) and calls `/logout/` in a
   `finally` block before exiting, so nothing lingers on disk or server-side.

## Why a script, not ad-hoc curl (gotchas already solved here)

- **Playwright/headless Chromium is a dead end in this sandbox** — the outbound
  proxy's CA can't be made trusted by headless Chromium, only by CA-aware HTTP
  clients like `curl`/`requests`. Don't try browser automation; screening.md hit
  this too. `requests` works fine through the proxy.
- **Pagination is mandatory, not optional.** screener.in shows 50 rows/page; a
  query with hundreds of hits silently truncates to page 1 unless you page
  through to the count in the "Showing page X of Y" footer text.
- **The results `<table>`'s header row repeats mid-table** (screener re-injects
  it periodically down the page) — filtering rows to "has a `<td>` with an
  `<a href>` containing `/company/`" is what correctly separates real data rows
  from repeated header rows.
- **niftyindices.com blocks/redirects requests without a browser-like
  `User-Agent`** — a bare `curl` or `requests.get` with no UA header can fail
  silently; the script always sends one.
- **Column headers aren't hardcoded** — they're parsed from the table's own
  `<th>` row each run, since the exact set of default display columns is a
  screener.in implementation detail that could shift.

## Relationship to this repo's other pipeline files

`screening.md` documents one fixed baseline query (growth/value screen) run
manually by a human or an agent following its step-by-step curl recipe, feeding
`To-Analyze/`. This skill is a general tool for one-off or repeated
query-plus-index questions — it doesn't replace or modify that pipeline, and it
doesn't write into `To-Analyze/` automatically. If the user wants a screen result
saved into the pipeline's queue, follow `screening.md`'s output contract
separately after getting results here.
