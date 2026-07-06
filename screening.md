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
