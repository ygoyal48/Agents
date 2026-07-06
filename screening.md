# SCREENING — Part 1 of the Peaceful Investing pipeline (STANDALONE — for the screening agent)

> **READ THIS FIRST — who runs this file and what it produces.**
> This file is the COMPLETE instruction set for the SCREENING AGENT. It is deliberately self-contained:
> do NOT read `strategy.md` — analysis is not your job. Your entire mission:
> **(1) run the screen query on screener.in → (2) collect the passing companies → (3) save them as a
> txt file in `To-Analyze/`.** The analysis agent (running `strategy.md`, Part 2) picks up from that file.
> You make NO buy/sell/avoid judgements and do NO per-company analysis. A screen is a **funnel, not a buy signal**.

---

## 1. THE BASELINE QUERY (the author's default — start here every run)

Run on **screener.in** (free account suffices; log in → *Screens* → *Create new screen*). Query, in screener's query language:

```
Sales growth 10Years > 15 AND
Price to Earning < 10 AND
Debt to equity < 1 AND
Cash from operations last year > 0 AND
Market Capitalization > 25
```

(If a field name errors, pick the matching field from screener's query-builder autocomplete — names occasionally change;
the INTENT of each line is fixed and listed below.)

| Filter | Why it exists (one line — do not re-derive) |
|---|---|
| Sales growth 10 Yrs > 15% | only proven long-period growers deserve analysis time |
| P/E < 10 | margin of safety in price; earnings yield ≥ ~10% vs G-Sec |
| D/E < 1 | leverage kills small companies; debt-funded growth is the trap |
| CFO latest year > 0 | profits must arrive as cash at least in the latest year |
| Mcap > ₹25cr | below this, liquidity/manipulation risk dominates |

**Calibration facts:** this exact screen returned **~56 companies out of ~5,471** on the author's run — a ~1% pass rate is
the DESIGNED outcome. An empty or tiny result set is a *valid* result. **Never relax the criteria to force candidates**
("when in doubt, reject" is the house rule; finding ~1 good stock a year is plenty).

## 2. ADJUSTMENT KNOBS (only these, only in this direction)

- **Too many results (>~60):** tighten — `Price to Earning < 9` (then 8, 7…) and/or `Debt to equity < 0.5`,
  and/or `Sales growth 10Years > 18`. Tighten one knob at a time; note the final query in the output header.
- **Too few results:** report the small list as-is. Do NOT loosen P/E above 10, D/E above 1, or sales growth below 15
  to manufacture candidates. (The analysis agent has its own valuation gates; feeding it overpriced names wastes the pipeline.)
- **Optional supplementary screens** (run AFTER the baseline, results tagged accordingly, never replacing it):
  - *Watch-only variant* for quality-at-any-price tracking: same query but `Price to Earning < 25` — tag every extra name
    `WATCH-PRICEY` (these are for the analyst's watchlist, not for buying at current prices).
  - *Idea intake:* names from media/magazines/TV/"hot product" chatter may be APPENDED to the output tagged `IDEA-ONLY`
    — they carry zero screen credibility and are never a buy reason; they merely enter the same analysis queue.

## 3. UNIVERSE HYGIENE (apply to the raw result list before saving)

1. **Prefer micro/small/mid-cap** — room to re-rate into large-cap. Famous, fully-discovered mega-names may be dropped
   or tagged `DISCOVERED` (they rarely pass the analyst's price gate anyway).
2. **Deduplicate against work already done:** skip any company already present in `Holdings/` (owned — it is being
   monitored, not re-screened) or already listed in an existing `To-Analyze/*.txt` from a previous run (still queued).
3. **Tag SME-exchange listings** (`NSE Emerge` / `BSE SME`) with `SME` — the analysis agent routes these to a special
   fraud screen first; your job is only the tag.
4. **Tag recent listings** (<3 yrs of trading history) with `RECENT-IPO` — same reason.
5. **Do not filter on sector, story, or news** — that judgement belongs to the analysis agent.

## 4. PROCEDURE (step by step)

1. Log in to screener.in → *Screens* → *Create new screen* → paste the baseline query → run.
2. If result count ≫ 60, apply §2 knobs; record the FINAL query text.
3. Page through ALL results. For each company capture: **Name · NSE/BSE ticker · Mcap (₹cr) · P/E ·
   D/E · 10-yr sales growth % · latest-year CFO (₹cr) · exchange (main/SME)**. (Screener's column
   settings can add these columns; or export and read off the list page.)
4. Apply §3 hygiene (dedupe, tags).
5. Write the output file (§5) into `To-Analyze/`.
6. Optionally save the screen on screener.in as `PI-Baseline` and enable its email alert — future runs
   then also get "new stock entered the screen" signals; mention in the header if enabled.

## 5. OUTPUT CONTRACT (exactly this format)

**File:** `To-Analyze/shortlist_YYYY-MM-DD.txt` (date = run date; if a same-day file exists, suffix `_2`).

```
# PI screening run
# date: YYYY-MM-DD
# query: <final query text used>
# universe: <total companies screener reports> | passed: <N> | after dedupe: <M>
# tags: SME | RECENT-IPO | WATCH-PRICEY | IDEA-ONLY | DISCOVERED (absence of tag = clean main-board name)
#
# Name | Ticker | Mcap(cr) | P/E | D/E | Sales10yCAGR% | CFO-latest(cr) | Tags
Vinati Organics | VINATIORGA | 1850 | 9.4 | 0.4 | 34 | 88 |
Some SME Corp | XYZ | 95 | 8.1 | 0.7 | 22 | 12 | SME,RECENT-IPO
```

One line per company. No commentary, no verdicts, no ranking — the queue is unordered by design.

## 6. BOUNDARIES (what you must NOT do)

- No financial analysis, no ratio deep-dives, no annual-report reading, no verdicts — that is `strategy.md` (Part 2).
- No portfolio actions of any kind.
- No editing of `strategy.md`, `Holdings/`, or the analysis template.
- If screener.in is unreachable or the query language has changed beyond repair, write the output file with a header
  line `# STATUS: FAILED — <reason>` so the pipeline knows the queue was not refreshed, rather than silently doing nothing.

**Handoff:** the COLLECTION agent (Part 2, `collection.md`) consumes the newest `To-Analyze/shortlist_*.txt` and builds a
document folder per company; the analysis agent (`strategy.md`) then works from those folders. Your run ends when the
shortlist file is saved (and committed, if you have git access).

---

## 7. FAST-PATH: AUTOMATED RUN RECIPE (proven working — do this, skip the trial-and-error)

> This appendix records exactly how the screen was run end-to-end on 2026-07-06 so future runs go straight to the
> working path. **screener.in requires login for custom queries** (anonymous requests redirect to `/login/`), so
> there is a login step. Read the whole section before starting; the two gotchas (browser dead-end, CFO not in the
> table) waste the most time if rediscovered.

### 7.0 Credentials — how to supply them (NEVER hardcode them here)

The login needs a screener.in email + password. **Do not write them into this file or any committed file** — a
plaintext secret in git history is permanent and readable by anyone with repo access. Instead read them from the
environment at run time:

```bash
export SCREENER_USER='you@example.com'
export SCREENER_PASS='your-password'      # set in your shell, a local .env that is .gitignored, or a secret store
```

If you (a human) prefer, run the screen in your own browser and paste/export the results to the agent instead — then
no credentials touch the automation at all. That is the zero-secret fallback and is always acceptable.

### 7.1 Environment gotcha — the headless browser is a DEAD END here, don't try it

In this sandbox all outbound HTTPS goes through an agent proxy whose CA is at `/root/.ccr/ca-bundle.crt`. Playwright /
headless Chromium **cannot be made to trust that CA** — adding it to the NSS DB (`certutil`), the system store
(`update-ca-certificates`), and passing `--proxy-server` all still end in `net::ERR_CONNECTION_RESET` /
`handshake failed`. **Do not spend time on Playwright.** Plain HTTP via `curl` or Python `requests` honours the
standard CA env vars and works fine through the proxy. Use that.

### 7.2 Log in (get a session cookie)

Django login with CSRF. Two requests: GET the form to obtain `csrfmiddlewaretoken` (hidden field) + the `csrftoken`
cookie, then POST them back with the credentials. A **302 redirect to `/dash/`** means success; a 200 that still shows
the login form (`errorlist`) means the credentials were rejected.

```bash
# scratch dir for the cookie jar (keep it out of the repo)
JAR=/tmp/screener_cookies.txt
rm -f "$JAR"

# 1. GET the login page -> csrftoken cookie + csrfmiddlewaretoken field
curl -sS -c "$JAR" https://www.screener.in/login/ -o /tmp/login.html
CSRF=$(grep -o 'csrfmiddlewaretoken[^>]*value="[^"]*"' /tmp/login.html | grep -o 'value="[^"]*"' | cut -d'"' -f2)

# 2. POST credentials (Referer + Origin headers are required)
curl -sS -c "$JAR" -b "$JAR" \
  -H "Referer: https://www.screener.in/login/" \
  -H "Origin: https://www.screener.in" \
  --data-urlencode "csrfmiddlewaretoken=$CSRF" \
  --data-urlencode "username=$SCREENER_USER" \
  --data-urlencode "password=$SCREENER_PASS" \
  --data-urlencode "next=" \
  -D /tmp/login_headers.txt -o /dev/null \
  https://www.screener.in/login/
grep -i '^location' /tmp/login_headers.txt   # expect: location: /dash/
```

### 7.3 Run the query

The screen-builder form (`/screen/new/`) POSTs to a **GET** endpoint `/screen/raw/`. Just hit it directly with the
baseline query from §1:

```bash
Q='Sales growth 10Years > 15 AND Price to Earning < 10 AND Debt to equity < 1 AND Cash from operations last year > 0 AND Market Capitalization > 25'
curl -sS -G -c "$JAR" -b "$JAR" https://www.screener.in/screen/raw/ \
  --data-urlencode "query=$Q" --data-urlencode "sort=" --data-urlencode "order=" \
  -o /tmp/results.html
```

Parse the single `<table>` in the result. **Column order** (per `<td>`, after skipping non-`/company/` rows):
`S.No | Name | CMP | P/E | Mar Cap | Div Yld% | NP Qtr | Qtr Profit Var% | Sales Qtr | Qtr Sales Var% | ROCE% | ROE% |
Sales Var 10Yrs% | Debt/Eq`. Gotchas: the header row repeats once mid-table (so 23 companies came back as 25 `<tr>`s —
filter to rows whose first `<a href>` starts with `/company/`); the page footer shows the passing count (`"23 results"`)
but **does not** report the total universe size, so leave that field `N/A` in the output header.

### 7.4 The CFO gotcha — it is NOT a screen column

`Cash from operations last year` is a *filter*, but the value is **not** shown in the results table. To fill the
`CFO-latest(cr)` output column you must open each company page and read it off the cash-flow statement:

```
GET https://www.screener.in/company/<TICKER>/            (add /consolidated/ if the results link did)
```

`<TICKER>` is whatever the results-table link uses — either the NSE symbol (e.g. `NMDC`) or the numeric BSE code
(e.g. `521178`). In the page, find the `id="cash-flow"` section, the row starting `Cash from Operating Activity`, and
take its **last** cell (latest year).

### 7.5 Tag heuristics that worked (see §3)

- **SME:** screener.in exposes no direct board-type field. A reliable tell is a **half-yearly-only reporting cadence**
  (quarters header shows only Mar/Sep, not all four quarters) — SME-platform issuers file half-yearly under SEBI rules.
  Tag those `SME`; the analysis agent confirms.
- **DISCOVERED:** obvious mega-caps (e.g. NMDC, ONGC) — tag and expect the analyst's price gate to drop them.
- **RECENT-IPO:** check listing history; if <3 yrs of data, tag it. (None qualified on the 2026-07-06 run.)

### 7.6 Tooling notes

- Python parsing used `requests` + `beautifulsoup4` (`pip install beautifulsoup4`; `requests` was already present).
  Load the cookie jar with `http.cookiejar.MozillaCookieJar(JAR); .load(ignore_discard=True, ignore_expires=True)`.
- **Downstream reuse:** the COLLECTION agent (`collection.md`) reuses this same login — a logged-in session is what
  unlocks the peer-comparison table, promoter-pledge %, and Export-to-Excel (all 404 anonymously). Also note for any
  BSE-hosted fetch: BSE returns **403 to non-browser requests** — send a Chrome `User-Agent` + `Referer: https://www.screener.in/`.
- **Log out when done** (`GET /logout/`) and delete the cookie jar — it is a live session token; keep it in a scratch
  dir, never in the repo.
- If login starts failing (2FA/CAPTCHA introduced, or the query language changes), fall back to the human-runs-it path
  (§7.0) and, per §6, write the output file with a `# STATUS: FAILED — <reason>` header rather than doing nothing.
