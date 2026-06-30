# STOCK ANALYSIS STRATEGY — Decision Engine (Peaceful Investing / Vijay Malik method)

> **READ THIS FIRST — what this file is.**
> This is my (Claude's) operating manual for deciding whether to BUY, HOLD, AVOID, or SELL a stock.
> It is a *mechanical decision system*, not an essay. I do **not** need to reason from first principles or
> "use my brain" on philosophy — I apply the rules, thresholds, and worked examples below and reach a verdict.
> Every parameter has: (a) an exact numeric threshold, (b) the formula, (c) a "GOOD looks like / BAD looks like"
> worked example with real numbers so I can pattern-match fast, and (d) what the verdict contribution is.
>
> **Philosophy deliberately omitted.** Arguments for long-term vs trading, "stocks are businesses," motivational
> content, why-fundamental-beats-technical, marketing of paid services — all skipped. Only decision-relevant content is here.
>
> **Context of the source:** Indian equities (BSE/NSE), bottom-up fundamental value investing, retail/long-term horizon,
> data source = screener.in. Currency ₹. "cr" = crore = 10 million. "lakh" = 0.1 million. Numbers in examples are circa 2014–2020.
> Interest-rate / G-Sec numbers must be refreshed to current values at decision time (see §5).
>
> **Built from three sources:** (1) the *Peaceful Investing* method book (framework — §1–§16); (2) the *Case Studies* ebook
> (20 worked verdicts — **§17**); and (3) the *Company Analyses Vol. 1* ebook (11 forensic deep-dives — **§18**, with a full
> forensic red-flag catalog). §17–§18 are my fast pattern-match reference: when analyzing any company, find the closest case and
> copy its reasoning. Refinements discovered in the case books are folded into §1–§16 and tagged **[CS]** (Case Studies) or **[V1]** (Vol 1).
>
> **Always, before computing anything:** (a) use **CONSOLIDATED** financials, not standalone — standalone hides subsidiary debt
> (MRF standalone missed ₹400cr of subsidiary debt, distorting D/E and interest coverage). (b) **Normalize fiscal-year changes** —
> if a company reports an 18-month (or 9-month) period to align to Apr–Mar, convert to 12 months (×2/3 etc.) before computing growth
> and turnover ratios, else growth/turnover look inflated and receivable-days look low (MRF 2016 = 18 months). (c) Pull **10 years**.

---

## 0. THE ONE-PAGE VERDICT ALGORITHM (run this top to bottom)

A stock is a **BUY** only if it passes **ALL** of: Financial gate, Fraud gate, Business/Moat gate, Management gate, Valuation/MoS gate.
Failing **any single gate = REJECT** (management and fraud gates are hard vetoes — no amount of cheapness compensates).

```
STEP 1  SCREEN (shortlist)            → §1
STEP 2  FINANCIAL ANALYSIS (8 params) → §2   gate: must pass ≥ all core thresholds
STEP 3  FRAUD / SHENANIGAN SCAN       → §3   gate: any hard red flag = REJECT
STEP 4  SSGR (inherent growth)        → §4   informs moat + premium
STEP 5  VALUATION + INVESTABLE P/E    → §5   gate: price ≤ target P/E (Margin of Safety in price)
STEP 6  BUSINESS / MOAT (5 tests)     → §6   gate: must show a moat
STEP 7  MANAGEMENT (10 checks)        → §7   gate: HARD VETO — any integrity red flag = REJECT
STEP 8  MARGIN OF SAFETY (3 pillars)  → §8   gate: MoS in price AND business
STEP 9  CREDIT RATING                 → §9   gate: ≥ BBB- and improving trend
STEP 10 OPERATING PERFORMANCE (5)     → §10  confirms trend is intact
STEP 11 FINAL CHECKLIST               → §11  the consolidated pass/fail table
→ BUY SIZING & PORTFOLIO              → §12
→ MONITOR                            → §13
→ SELL RULES                          → §14
WORKED-EXAMPLE LIBRARY (pattern match)→ §15
FORMULA APPENDIX                      → §16
```

**Master mental model of an ideal buy (memorize this archetype):**
> A **small/mid-cap**, **pure-play**, **debt-free** company, growing **sales >15% for 10 yrs**, with **NPM >8%**,
> growing **profits ≥ as fast as sales**, **converting profits to cash** (cPAT≈cCFO), generating **positive Free Cash Flow**,
> whose **SSGR > its sales growth** (so growth is self-funded), run by an **honest, minority-friendly promoter** holding **>50%**
> and **not** extracting via salary/related-party/warrants — and available at **P/E < 10** (EY > G-Sec yield).
> Buy it, hold for decades, buy MORE when price falls and fundamentals are intact. **Never sell a good business on price.**

**Hit-rate expectation:** rejection rate is *supposed* to be very high. Finding ~1 good stock/year is plenty.
"10 good stocks in a lifetime can make one a billionaire." Never relax criteria to force a buy. When in doubt → REJECT.

---

## 1. SHORTLISTING / SCREENING (Stage 0 — narrow the universe)

**Goal:** cut thousands of stocks to a handful worth deep analysis. Use a screener (screener.in) with a hard quantitative query.

**Baseline screen query (the author's default — use as the starting filter):**
```
Sales growth 10 Years > 15%   AND
Price to Earnings        < 10  AND
Debt to Equity           < 1   AND
Cash from operations latest year > 0  AND
Market Capitalization    > 25 cr
```
- This is *deliberately strict* (the author's run returned ~56 companies out of ~5,471). Good.
- A screen is a *funnel, not a buy signal*. Anything passing the screen still must pass §2–§11.
- Media tips / magazines / TV / "hot products" are valid *idea sources* only — never a buy reason. Always do own analysis.
- Prefer **micro/small/mid-cap** (room to re-rate into large-cap). Avoid already-famous, fully-discovered names.

**My action:** if given a ticker, pull 10-yr data first (P&L, Balance Sheet, Cash Flow, Quarterly). If asked to *find* candidates, apply the screen above (tightening P/E or D/E if too many results).

---

## 2. FINANCIAL ANALYSIS — the 8 core parameters (Stage 1 GATE)

> Financial analysis = the first hard filter. The *whole* of it is just **ratios** and **growth rates** over **10 years**.
> Read the *trend* over 10 yrs, not a single year. A company must clear these to deserve further time.

| # | Parameter | PASS threshold | Formula | Verdict role |
|---|-----------|----------------|---------|--------------|
| 1 | **Sales growth** | **CAGR > 15%** over 7–10 yrs, *consistent* | (Sales_end/Sales_start)^(1/yrs) − 1 | Reject if low/erratic. >50% = unsustainable, distrust |
| 2 | **Profitability (NPM)** | **NPM > 8%**, OPM & NPM stable/rising | NPM = PAT/Sales; OPM = OperatingProfit/Sales | Reject if thin/falling margins |
| 3 | **Tax payout** | **≈ 30%+** (near statutory corp rate) | Tax/PBT | Abnormally low tax (no stated incentive) = RED FLAG |
| 4 | **Interest coverage** | **> 3** | Operating Profit / Interest expense | <3 = fragile to downturns |
| 5 | **Debt/Equity** | **< 0.5** (ideal = 0, debt-free) | Total Debt / Shareholder funds | High debt = bankruptcy risk → reject/penalize |
| 6 | **Current ratio** | **> 1.25** | Current Assets / Current Liabilities | <1.25 = liquidity stress |
| 7 | **Cash flow** | **CFO > 0** every year; ideal CFO ≥ CFI+CFF outflow | from Cash Flow statement | Negative CFO = serious concern |
| 8 | **Cumulative PAT vs CFO** | **cPAT ≈ cCFO** over 10 yrs | Σ PAT(10y) vs Σ CFO(10y) | cCFO << cPAT = profits not real/uncollected → REJECT |

**Notes / refinements:**
- Indian corp tax ≈ 30% (foreign cos 40%) at time of writing; tax incentives (SEZ, area-based) legitimately lower it — verify a *stated* reason.
- Interest coverage: use **operating** profit only (exclude non-operating/other income) for conservatism.
- D/E: use **total** debt (not just long-term/secured). A one-off spike during a funded capacity expansion that is later repaid is acceptable (see VOL below).
- Current ratio components: CA = inventory + cash/equivalents + receivables + short-term loans; CL = payables + short-term provisions.
- #8 is **mandatory for every company.** Over 1 year PAT≠CFO (credit sales), but over 10 yrs they must converge. If CFO chronically lags PAT → either uncollectable receivables or fictitious profit → avoid.

**[CS] Field-tested refinements (from the case-study ebook — apply these every time):**
- **Distrust OPM vs NPM divergence.** Stable OPM but *low/volatile NPM* means interest (debt) and/or tax is eating equity returns — the business runs for lenders/government, not shareholders. *Meghmani:* OPM 14–16% stable but NPM only 2–3% (interest ₹16cr→₹75cr). → weak.
- **Strip non-operating income before trusting NPM.** Forex gains, interest/dividend on cash, one-offs inflate reported NPM. Recompute NPM on operating profit only. *Torrent Pharma:* ₹253cr forex gain = 27% of PBT; reported NPM 16% but true ~11.8%.
- **Normalize NPM for tax incentives.** A very low tax rate (SEZ/area-based/sector incentive) inflates NPM and is *temporary*. Recompute NPM at full ~30% tax and ask "is it still good when the incentive expires?" *Kaveri* tax 3–5%, *Emami* 12–18%, *Torrent* 20–25%. Flag incentive expiry dates.
- **Low NPM + Low Fixed-Asset-Turnover = capital-intensive debt trap.** This combo means each rupee of growth needs heavy capex but throws off little profit → must borrow → debt spiral. *Meghmani, Fiem, Sarla* all followed this into rising debt. Avoid unless efficiency is durably improving.
- **PBT/NFA test (earns-less-than-an-FD).** Compute Profit-Before-Tax ÷ Net Fixed Assets. If it's **below the bank fixed-deposit rate**, the company earns less by operating a whole business than the assets would in a deposit → structurally poor. *Meghmani:* PBT/NFA <9% (below FD). Strong reject signal even at low P/E.
- **Tax in P&L vs tax in cash flow.** Cross-check the P&L tax charge is actually *paid out* as cash tax in the cash-flow statement (not just an accrual). Persistent gap = aggressive accounting.

**[V1] Field-tested refinements (forensic, from the deep-dive ebook):**
- **Working-capital days = inventory days + receivable days — EXCLUDE payable days.** Rising payables is usually a *stress* signal (the company delays vendors when liquidity is tight), so subtracting payables would make a *deteriorating* position look like it's *improving*. Compute WC days the conservative way and compare to peers.
- **Decompose CFO before trusting it.** A high CFO (or high cCFO/cPAT) can be an artifact, not strength: (a) inflated by a big *rise in payables* (Omkar: ₹37cr of ₹67cr CFO was just payables); (b) inflated by large *depreciation* add-back in a capital-intensive firm (Machino: cCFO ₹153cr vs cPAT ₹23cr almost entirely depreciation ₹115cr + interest). Strong CFO only counts if it comes from real margin + working-capital discipline.
- **Physical input-vs-output cross-check.** Compare units/value of raw material *consumed* against units/value of product *sold*. If product sales rise while the matching raw-material consumption falls (Omkar: Iodine/Selenium product sales up, crude-Iodine/Selenium consumption down), or freight falls while sales rise, suspect fabricated sales. Pull these from the annual-report schedules.
- **True debt is bigger than the summary balance sheet shows.** Current Maturity of Long-Term Debt (CMLTD) sits inside "other current liabilities" and isn't broken out in quarterly/half-year summary balance sheets. For real debt/leverage, use the detailed notes in the annual report.
- **Cross-check the cash-flow statement against balance-sheet changes.** If CFO ignores working-capital movements, or CFF omits a debt inflow that the indebtedness table shows (Ishan Dyes), the accounts are unreliable → raise the bar.
- **Watch interim (half-year) balance sheets** for sudden jumps in receivables/debt that the annual narrative hides (Machino: receivables ₹11cr→₹32cr in H1 forced ₹21cr capex onto debt ₹34cr→₹66cr).

**GOOD looks like — Vinati Organics (VOL), the archetypal pass:**
- Sales ₹49cr (2005) → ₹696cr (2014) = **34% CAGR** ✓ (and quantity-driven, see §6)
- OPM rose 15%→24% then stable ~22%; NPM 7%→17% then stable ~12% ✓ (>8%)
- Tax ≈ corporate rate ✓
- Interest coverage ~10–15 ✓ (Op profit grew 7→153; interest 1→18)
- D/E consistently <1; spiked to ~0.8 in FY12-13 for a *funded expansion*, then repaid debt ₹201cr→₹122cr, D/E back to **0.4** ✓
- Current ratio 1.4–2.5 ✓
- CFO grew ₹4cr→₹134cr, funded its own expansion ✓
- cPAT ₹351cr ≈ cCFO ₹353cr over the decade ✓ → **profits are real.** PASS all 8.

**BAD looks like:**
- Sales growing but **profits flat/erratic** (Tata Steel: sales 28% CAGR, profit 0% over 10 yrs, even losses) → no pass.
- **cCFO << cPAT**, rising receivables, rising debt → fraud archetype (see §3).
- Debt spiraling to fund growth (Amtek debt ₹156cr→₹5,186cr) → reject.

---

## 3. FRAUD / FINANCIAL-SHENANIGAN SCAN (Stage 2 — HARD VETO GATE)

> Managements dress up books (Enron, Satyam, WorldCom, Toshiba…). The three statements *talk to each other*; if one is
> manipulated, signs leak into the others. Scan for these. **Any hard red flag = REJECT** (or exit if held), regardless of how good the story is.

**The detection toolkit (compute/scan all of these):**

1. **cCFO < cPAT over 10 yrs** — the master fraud tell. Inflated/bogus revenue isn't collected in cash. → enhanced diligence; large persistent gap = REJECT.
2. **Rising Receivable Days / DSO** — DSO = (avg receivables/Sales)×365. Receivables growing *faster than sales* = aggressive/bogus revenue. Also beware large **unbilled receivables** (EPC/infra). **A sudden big DROP in DSO** after a rise is *also* suspicious (receivables sold/reclassified to hide them).
3. **Inventory buildup / falling inventory turnover** — ITR = Sales/avg inventory. Falling ITR = old/obsolete inventory not written off (deferred impairment). → diligence.
4. **Use Free Cash Flow, not CFO** — FCF = CFO − Capex. Companies capitalize normal opex to inflate both profit AND CFO. Red flag: **declining FCF while CFO looks strong.**
5. **Frequent / serial acquisitions** — acquisitions legally boost CFO (acquired co's receivables flow through CFO; the cost flows through CFI). Mixing of accounts hides everything. Counter-metric: **CFO − Capex − Cash paid for acquisitions.** Serial acquirers ≈ avoid.
6. **Abnormal/supernormal performance** — implausibly smooth earnings through volatile times; *always* meeting estimates. → managed numbers likely.
7. **Changes in accounting policy/disclosure** — revenue recognition, capitalization, **changed fiscal year**, depreciation/pension/lease assumptions. Ask "why this change, why now?" Beware when a company **stops disclosing a previously-reported metric**, hides off-B/S items / contingent liabilities / corporate guarantees. New disclosures should answer questions, not create them.

**Balance-sheet specific red-flag combos (also under §7 management):**
- **Rising Sales + Rising Receivables + Rising Debt** together = booking aggressive/fictitious sales, funding opex with debt → classic fraud pattern → REJECT.
- **High cash AND high debt simultaneously** = paying interest to hold idle cash makes no sense; in frauds the *debt is real but the cash is fictitious/siphoned.* → deep scrutiny; usually avoid.
- **Non-standard "vanity" metrics** as headline (same-store-sales, ARPU, subscriber adds, order book, EBITDA-instead-of-PAT, "cash earnings") — definitions get bent. Trust standard PAT/CFO/FCF.

**Verdict rule:** Treat #1 (cCFO<cPAT), the Rising-Sales+Receivables+Debt combo, High-cash+High-debt, and serial acquisitions as **near-automatic rejects**. Never rely on awards/ratings to vouch integrity (Satyam won a Golden Peacock governance award before its fraud broke).

**[CS] Field-tested refinements:**
- **High cash + rising debt = treasury arbitrage or fictitious cash.** Paying ~10% interest while sitting on idle cash is irrational; either the "cash" is fake/siphoned, or the company is playing a treasury game it shouldn't. *Torrent:* ~₹900cr debt rise mirrored by ~₹900cr cash/investment rise (~₹100cr/yr avoidable interest). *Hindustan Media:* ₹587cr cash yet raised ₹78cr fresh debt. Non-financial companies should deploy cash in the business, not arbitrage. → deep scrutiny.
- **Read the receivables AGEING, not just DSO.** Pull the schedule: what % is outstanding **>6 months**, and is the company **writing receivables off**? *Kaveri:* 68% (₹120cr of ₹176.8cr) >6 months, writing off ₹4–4.5cr/yr. → cash never coming.
- **Standalone vs consolidated receivables.** If standalone receivables >> consolidated, the parent is selling to its own subsidiaries that collect from end-customers but **don't remit cash back**. *Torrent:* ₹222cr standalone >6-month receivables, only ₹16cr consolidated → US/Brazil/Romania subs parking cash abroad while India borrows.
- **Contingent liabilities / off-balance-sheet guarantees.** Corporate guarantees given for loans of *non-subsidiary group companies* = the company is on the hook with no benefit to its shareholders. *Virat Crane:* guarantees ₹10cr + ₹13.24cr for group cos. Read the contingent-liability note every time.
- **Annual-report quality is a tell.** Auditor's report omitting disputed dues the company itself disclosed (*Kaveri*), unspent mandatory CSR with a frivolous excuse (*Kaveri*), missing company secretary / auditor-flagged Companies-Act non-compliance left unfixed for years (*Rexnord §178, Virat Crane §203*), even spelling mistakes in the AR (*Virat Crane*) → low governance quality. Company-secretary *resignation* often precedes trouble.

---

## 4. SELF-SUSTAINABLE GROWTH RATE (SSGR) — inherent growth engine (Stage 3)

> SSGR = the sales growth a company can fund **purely from its own profits**, with **zero new debt or equity**.
> It's the single best test of whether growth is *self-financing* (safe) or *debt-financed* (fragile). Central to moat + premium decisions.

**Formula (two equivalent forms):**
```
SSGR (%) = NFAT × NPM × (1 − DPR) − Dep
         = [(1 − Dep) + NFAT × NPM × (1 − DPR)] − 1
```
Where (use **3-year averages** of each input to smooth one-year noise):
- **NFAT** = Net Fixed Asset Turnover = Sales / avg Net Fixed Assets
- **NPM** = Net Profit Margin = PAT / Sales
- **DPR** = Dividend Payout Ratio = Dividends / PAT
- **Dep** = Depreciation as % of Net Fixed Assets

**Drivers:** SSGR rises with **higher NPM**, **higher NFAT** (asset-light/efficient), **lower DPR**, **lower depreciation.**

**The decision — compare SSGR vs the company's actual past sales-growth (3/5/7/10-yr CAGR):**

| Case | Meaning | Verdict |
|------|---------|---------|
| **SSGR > sales growth** | Self-funds its growth; can cut price/dividend/invest in downturn without debt. Will accumulate cash / stay debt-free. | **GOOD — margin of safety in business. Eligible for a P/E premium.** |
| **SSGR < sales growth** | Growing beyond its means; must raise debt/dilute equity → debt spirals. | **AVOID** (unless temporary, see next row). |
| **SSGR < growth BUT debt falling** | Funded by *releasing working capital* (rising ITR / falling DSO → cCFO>cPAT) or *selling assets* (positive CFI). Temporary relief. | **CAUTION** — runs out once efficiency maxes/assets sold; debt will rise later. |
| **SSGR ≈ sales growth** | At maximum business potential. Check cPAT vs cCFO: if cCFO<<cPAT, can't sustain without new funds. | Borderline; require strong cPAT≈cCFO. |

**Worked examples (pattern-match these — full input layout per the source tables):**

*GOOD (SSGR >> growth, debt-free):*
- **FDC Ltd:** SSGR ~30–40%, actual growth 8–10% → entirely self-funded, near-nil debt. ✓
- **Container Corp:** SSGR ~22–25%, growth 8–11% → debt-free. ✓
- **VST Tillers Tractors:** SSGR ~46–72%, growth 9–17% → grows with no debt. ✓
- **Tide Water Oil:** SSGR ~60–95%, growth 6–15% → huge cushion, debt → 0. ✓

*BAD (SSGR << growth, debt explodes):*
- **Amtek India/Castex:** SSGR ~0–1% (NFAT only 0.6–0.7), growth 25–30% → debt ₹156cr → ₹5,186cr. ✗
- **Glenmark Pharma:** SSGR ~15–18%, growth 25–30% → excess 8–10% debt-funded → debt ₹437cr → ₹3,267cr. ✗
- **Pratibha Industries:** SSGR ~1–5%, growth 28–38% → debt ₹50cr → ₹2,283cr. ✗
- **Jaiprakash Power:** SSGR ~0%, growth 35–45% → debt ₹1,081cr → ₹22,901cr (had to sell assets). ✗
- **LT Foods:** SSGR ~0–7%, growth 22–23% → debt ₹224cr → ₹1,692cr. ✗

*CAUTION (SSGR<growth but debt fell via efficiency):*
- **Fiem Industries:** SSGR ~1–2%, growth ~25%; ITR improved 12.0→15.8 released working capital, cCFO ₹148cr > cPAT ₹64cr (2 yrs), debt ₹139cr→₹87cr. Temporary — debt will rise once efficiency peaks.

**My action:** compute SSGR (3-yr avg inputs). If SSGR > 10-yr sales CAGR → tick the "moat/margin-of-safety" box and allow a P/E premium (§5). If SSGR << growth AND debt rising → **reject.**

---

## 5. VALUATION ANALYSIS + INVESTABLE P/E (Stage 4 — price GATE)

> Even a great business is a bad investment if overpaid for. Valuation is the second filter. **Never overpay.**
> P/E is the primary lens. Target: **P/E < 10** for the margin of safety, then adjust the *allowable* P/E with the 4 Principles.

### 5a. The valuation ratios & thresholds

| Ratio | Formula | BUY threshold | Notes |
|-------|---------|---------------|-------|
| **P/E** | CMP / EPS | **< 10** (preferred) | Single most important. Low P/E = high margin of safety + P/E-expansion upside. |
| **PEG** | P/E / EPS growth% | **< 1** | P/E should be ≤ earnings growth rate. |
| **Earnings Yield (EY)** | EPS / CMP = 1/PE | **> 10-yr G-Sec yield** | Graham's MoS. Compare to bond/FD yield. |
| **P/B** | CMP / Book value per share | **< 1** | *Mostly ignore* except **financial sector** (banks/NBFCs) where book value is meaningful. |
| **P/S** | CMP / Sales per share | **Buy < 1.5, Sell > 3** | O'Shaughnessy. |
| **Dividend Yield** | Dividend / CMP | Higher better; **>5% very attractive** | Ignore for fast-growth cos reinvesting profits well. |
| **EV/EBITDA** | (MCap+Debt−Cash)/EBITDA | Lower = cheaper | For whole-company / capital-structure-neutral view. |
| **Graham combo** | P/E × P/B | **< 22.5** | Optional cross-check. |

- **EY vs G-Sec example:** if G-Sec yield ≈ 8%, a stock needs EY ≥ 8% i.e. **P/E ≤ 12.5** to beat bonds. Higher EY−G-Sec gap = bigger cushion (buy at ₹100, EPS ₹10 → P/E 10, EY 10%; if price halves to ₹50, EY 20% attracts buyers and limits the fall — that *is* the margin of safety).
- **High-P/E trap (why I avoid P/E >20–25):** capital gain = earnings growth + P/E change. If P/E is already high, future P/E *expansion* is ~nil and P/E *contraction* risk is large. Even a flawless 25% grower bought at P/E 50 returns only ~17%/yr for a decade *if everything goes right* — and collapses if growth disappoints. **Low P/E is where high-return-low-risk lives.**
- **Why low P/E wins (quantified):** Mayur Uniquoters bought at P/E 6.6 → IRR 136%, of which earnings growth = 32% and **P/E expansion = 104%** (≈75% of return). Vinati at P/E 7.7 → IRR 143%, earnings 27% + **P/E expansion 116%** (≈81%). The re-rating from cheap→fair (driven by analyst coverage, credit upgrades, institutional buying) is the bulk of the return. Buy *before* discovery.
- **Industry P/E is IRRELEVANT** as a valuation anchor. Spread *within* an industry is enormous — e.g. Cement-Major "industry P/E 38.76" spans Prism 396 down to Saurashtra 5.7; Private Banks "18.36" spans Kotak 63 down to Karnataka 4.1; Cigarettes "26.42" spans Godfrey 34 down to Raghunath 3.8. Good companies trade richer than poor ones in the *same* industry. Do **not** assume a stock "deserves" the industry P/E (mean reversion often fails). Judge each company on its own P/E vs its own fundamentals.
- **[CS] Beware the VALUE TRAP — a low P/E is not automatically a buy.** Cheap P/E + high dividend yield can hide a business whose value is *eroding*. Cross-check: is market cap *growing* over 10 yrs (value-creation ≥ ₹1 per ₹1 retained), or shrinking? *Noida Toll Bridge:* P/E 5.6, DY ~12% — looks great, but MCap *fell* ₹189cr over 10 yrs (vs ₹214cr retained) and faces competing-bridge threats → value trap, the capital loss swamps the dividend. *Meghmani:* P/E 9.9 but PBT/NFA below FD rate → cheap for a reason. Low P/E only wins on a *fundamentally sound* company temporarily undiscovered — not on a structurally weak/declining one. Don't be lured by dividend yield alone while capital erodes.

### 5b. The 4 Principles — compute the *target investable P/E*

Start from a base P/E set by interest rates, then add premiums/discounts:

1. **Interest rate (base P/E):** Base P/E = **1 / (10-yr G-Sec yield)**.
   - G-Sec 10% → base P/E 10. G-Sec 8% → base P/E 12.5. G-Sec 12.5% → base P/E 8.
   - Lower rates justify higher P/E (and vice-versa). *Refresh G-Sec to the live value at decision time.*
2. **Competitive advantage (moat) → premium:**
   - **SSGR > sales growth** → pay a premium. Rough guide: **+1 P/E for every 5–10% that SSGR exceeds sales growth.** (Examples: VST Tillers, Tide Water.) Avoid (no premium / discount) if SSGR << growth & debt rising.
   - **High FCF% = FCF/CFO** → pay a premium. Rough guide: **+1 P/E for every 5–10% of FCF% cushion** (for cos growing sales >15% for 10 yrs). Positive FCF is a *necessity*; the higher FCF/CFO, the bigger the safety. (Atul Auto FCF% 48%, TTK 42% → premium-worthy; Bhushan Steel FCF% −300%, NFL negative → avoid.)
3. **Circle of competence → small premium:** if no new opportunity is available at target P/E, may pay a *small* premium to add to an *existing, well-understood* holding or a stock from an industry I know deeply.
4. **Stable-business premium → +10–15 P/E:** once a fundamentally strong company crosses **~₹10,000 cr market cap** ("existential-threat" barrier cleared — established model, distribution, crisis-survivability, takes share in downturns), the market awards a **+10–15 P/E** premium. So: pay it for large quality cos; *or* buy a small quality co and ride the re-rating as it crosses ₹10,000cr.

**Target P/E = base P/E (from G-Sec) + moat premium (SSGR/FCF) + circle-of-competence premium + stable-business premium.**
**Price GATE:** BUY only if current P/E ≤ target P/E. If price has run above target, HOLD (don't add) rather than chase.

---

## 6. BUSINESS & INDUSTRY ANALYSIS / MOAT (Stage 5 GATE)

> Bottom-up: the *company's* advantage matters far more than its industry ("moderately fast growers 20–25% in non-growth
> industries are ideal" — Lynch). The proxy for moat (without field research) is **consistent high sales growth, validated by 5 tests.**

**Entry condition:** company has shown **sales growth >15–20% YoY for ~10 yrs.** (Flat/no growth for 10 yrs = *certainly no moat*.)
High growth alone is NOT enough — it must pass **all 5 moat tests** (else it's price-hikes / unnecessary expansion / aggression / fraud):

| Test | What to verify | Threshold | GOOD (Vinati) | BAD (Tata Steel) |
|------|----------------|-----------|---------------|------------------|
| **1. Beats peers** | Sales growth > industry peers | growth > peers | Vinati 34% vs Clariant 14%, Anil 19% ✓ | (commodity, no edge) |
| **2. Volume-led growth** | Growth from higher *volume*, not just price | volume CAGR ≈ sales CAGR; price hikes ≈ inflation | Capacity 7,000→63,500 t (28%), volume 6,167→54,737 t (27%), price +5% (≈inflation) ✓ | — |
| **3. Sales→Profit** | Profit grows ≥ as fast as sales | Profit CAGR ≥ Sales CAGR | Sales 34%, **Profit 44%**, NPM 7%→12% ✓ | Sales 28%, **Profit 0%**, NPM 23%→2%, losses ✗ |
| **4. Profit→Cash** | cPAT ≈ cCFO (profits collected) | cPAT ≈ cCFO | Vinati profits collected in cash ✓ | — |
| **5. Value creation** | ₹ MCap created per ₹ retained (Buffett $1 test) | **≥ ₹1 per ₹1 retained** | Vinati **₹7.13** per ₹1 (retained 305→MCap +2,174) ✓ | Tata Steel **₹0.81** (retained 28,228→MCap +22,780) — *destroyed value* ✗ |

**Contrast anchor:** SCI (Shipping Corp) sales 2% CAGR over 10 yrs, MCap fell ₹4,000cr→₹3,000cr — no moat, wealth destroyer. Vinati 34% CAGR, MCap ₹18cr→₹2,200cr. ₹1,000 invested 2005→ SCI ₹746 vs Vinati ₹120,000.

**Verdict:** require **all 5** tests. Sales growth that fails test 3 (no profit) or test 5 (destroys value) = **no moat → reject**, however fast the topline. ROE/ROCE are *optional* extras — the 5 tests above are sufficient.

**Other business parameters (from final checklist):**
- **Product diversification → prefer PURE PLAY** (one segment, or closely-related products). Unrelated diversification (conglomerate sprawl) = **strict NO** (buy different stocks for diversification, don't want it inside one company).
- **No government interference in pricing/profitability** — avoid (or sell) companies whose prices/margins are capped by regulators or who are *forced to supply* certain clients (e.g. PNGRB gas-price/allocation actions hurting Gujarat State Petronet, IGL, Haldyn Glass).

**[CS] Field-tested refinements:**
- **Check the FX direction of the business model.** Importing inputs in USD and selling output domestically in INR is a *structural loser* when INR depreciates (costs rise, prices can't). The winning model is the reverse: source in India, sell/export in USD. *Merck India* (import raw material in USD, sell in INR) saw OPM collapse 24–26%→7% as INR fell 60%, while Indian pharma exporters thrived on the same move. Read the import%/export% split.
- **Verify "macro headwind" excuses against PEERS.** When management blames the economy for weak results, compare with industry peers. If peers slumped too, management is probably right; if only this company slumped, it's an execution/competitiveness problem. (*Supreme Industries* — peers also slowed, so the macro excuse held.)
- **Regulatory-dependent / one-shot-demand businesses are speculation, not investment.** Growth driven by subsidies/policy (and >30–35% spikes) reverses violently when policy turns. *Ujaas Energy:* solar sales spiked 7× then crashed 80% on policy change; CFO went negative; debt ₹2cr→₹120cr. Wide swings in efficiency ratios = business model not yet established → wait for stability.
- **A brand is only a moat if it shows up as *higher, consistent margins than peers*.** Don't credit "brand value" abstractly — verify superior OPM/NPM vs competitors, year on year. (Asked of *Supreme*; demonstrated by *Emami* brand shares 49–76% with 24–25% OPM, *KRBL* India Gate premium with stable 14–15% OPM.)

**[V1] Field-tested refinements (moat / business quality):**
- **OPM-vs-raw-material-price test (the commodity tell).** Chart OPM against the key input's price. If OPM rises and falls *with* input prices, the company has **no pricing power** — it's a commodity business whose recent margin expansion is just cheap inputs, NOT a moat. *MRF* OPM tracks rubber/crude; *Nile* OPM tracks lead; *Nandan* OPM tracks cotton. A stable OPM *through* an input-price cycle is the real moat signal. Marketing spend that lifts volume but not pricing power ≠ moat (MRF).
- **NFAT cuts BOTH ways — don't blindly cheer high asset turnover.** *Very high* NFAT (>5, e.g. Nile 10–16, Bhageria up to 62) usually means *low capital intensity / a trading business* → low entry barriers → commodity competition and price-taking (unless protected by patent/brand). *Very low* NFAT (<1, Wonderla) means >₹1 of fixed assets is needed per ₹1 of incremental sales — viable only with high profitability + cash-basis collection, else a debt trap (Amtek/Ahmednagar). The sweet spot is a *moderate, stable-or-rising* NFAT backed by pricing power.
- **Abnormally-high margin vs peers → investigate, don't celebrate.** *Divi's* OPM 37–40% vs peers 20–25% (NPM even exceeded peers' OPM) — dig for the durable reason; unexplained excess margin invites competition or hides manipulation.
- **Margin windfalls from a foreign government's policy are fragile, not moats.** *AksharChem*'s Vinyl Sulphone was loss-making for years; it only turned highly profitable when China's environmental crackdown removed Chinese competition — a windfall that reverses if policy reverses. Estimate the *normalized* segment margin (use a pure-play sister/peer as proxy — Asahi Songwon for AksharChem's pigment).
- **"Price-benchmarking"/cost-plus contracts don't guarantee stable margins** unless they include a *fixed-INR* premium. A percentage-only premium over a commodity input still collapses when the input price falls (Nile: lead-linked %-premium → losses at low lead prices).
- **Single-customer concentration (≥~80% one client) = weak pricing power + dependency**; track any competitor setting up near that customer (Nile → Amara Raja, threatened by Gravita).
- **Negative-working-capital model is a strong moat** — when customer *advances* + supplier *credit* fund operations, a company can grow *above* its SSGR and stay debt-free (Caplin: advances ₹57cr; payables ₹78cr funded inventory+receivables ₹55cr). Refines §4: SSGR can be exceeded safely when cCFO > cPAT.
- **Long-term ABOVE-market contracts get renegotiated/reneged** — never bank on them. *Bhageria* solar PPA at ₹4.41/unit when market fell to ₹2.44 (buyers renege; cf. Petronet–RasGas LNG forced from $12–13 to $6–7 + penalty waiver). Model the renegotiated/lower number.
- **Capacity-utilization → growth-runway.** If plants run near their ceiling (e.g. denim ~84–85%), further growth needs a fresh debt-funded capex round — no operating leverage left (Nandan). Also: distrust headline "volumetric/installed" capacity; use *rated/effective* capacity (Omkar 5,400 vs 2,315 TPA).

---

## 7. MANAGEMENT ANALYSIS (Stage 6 — HARD VETO GATE, the MOST important factor)

> **Management is ~90% of the decision.** A retail holder owns a fraction-of-a-percent and cannot control anything — a stock is
> "**faith in the management, a partnership with the promoter, trust in the majority shareholder.**" A crook will *always* find a way
> to extract value, however good the business. **Any genuine integrity red flag = REJECT/EXIT immediately**, no matter how cheap or fast-growing.

### 7a. Subjective checks
1. **Background check — "Just Google It."** Search promoter/company + keywords: **"fraud, SEBI, dispute, court, penalty, issues, Moneylife."** Focus on *past decisions/integrity*, **not** degrees (education ≠ integrity/competence).
   - **BAD:** Brooks Laboratories — great financials (sales +23%, profit +36%, debt-free) but promoters found by SEBI to have defrauded IPO investors → **REJECT despite perfect numbers.**
   - **GOOD:** Manappuram Finance — when RBI flagged a related deposit scheme, promoter complied within ~1 month, sold personal stake to honor depositors, set up a governance committee. History repeats: post-1995-IPO he bought back shares at ₹10 when market was ₹8 to keep his word. Good habits persist.
2. **Succession plan** — promoter should have groomed next-gen/professionals; **successors' salaries should be modest/in-line with experience** (a values signal). *Good sign example:* Ambika Cotton paid promoter's daughter (executive director) only ~₹1.5 lakh/yr while company made ₹31cr profit.

### 7b. Objective red-flag checks (compute/scan each)

| Check | GOOD | RED FLAG (penalize / veto) |
|-------|------|----------------------------|
| **Promoter salary vs PAT** | **2–4% of PAT**; rises *only* when profits rise | **Salary rising while profits fall**, or **>10% of PAT.** *ESS DEE Aluminium:* promoter pay ₹3cr→₹9.5cr (2%→**12%** of PAT) as profit fell ₹182cr→₹76cr → later ~₹500cr debt, losses, stock ₹750→₹90. **vs Ambika Cotton:** pay 2–4% of PAT, up only with profit; promoter even *waived* his 2% commission to be "at par with shareholders." |
| **Related-party transactions (RPT)** | minimal; arm's-length | Loans/inter-corporate deposits to promoter entities; buying/leasing from promoter firms above market; commissions to promoter-family firms. *Gujarat Automotive Gears:* new promoter (HIM Teknoforge) made the cash-rich debt-free company lend its cash + profits + new debt back to HIM (₹9cr→₹17cr) — made the company pay for its own acquisition. *Rexnord:* paid sales commission (up to ₹2cr/yr) to "Excelum Enterprises," the son-in-law's firm (he'd just moved off Rexnord's payroll). → **VETO.** |
| **Warrants to promoters** | none, or at/above market | Warrants issued to promoters **at a discount to market price**, immediately convertible = risk-free gain + backdoor stake increase. *Rexnord:* 3,478,800 warrants @ ₹13.40 vs market ₹23.34 → ₹3.36cr free gain; lifted promoter stake 46%→51% at a deep discount, subsidized by other holders. → red flag. **Compare allotment price to market price.** |
| **Short-term share-price obsession** | bold long-term decisions | Reversing sound long-term strategy due to analyst/price reaction; large ESOPs driving short-termism. *DCB Bank:* announced a long-term branch-expansion plan, stock fell 30%, then **U-turned** within days (≈₹45cr of management ESOP value had evaporated). → distrust. |
| **Dividends funded by debt** | dividends from **FCF** | Paying dividends while FCF negative = debt-funded, unsustainable. *Tata Steel:* 10-yr FCF **−₹20,508cr** yet paid ₹9,547cr dividends → debt ₹3,377cr→₹80,701cr. Dividend consistency means nothing if debt-funded. **Verify dividends ≤ FCF.** |
| **Accounting juggleries** | clean | Rising Sales+Receivables+Debt together; High cash + High debt; serial acquisitions (see §3). |
| **Competence (project execution)** | on-time, on-budget *organic* (greenfield/brownfield) capacity adds | Abandoned/cancelled projects, expelled from projects, repeated delays & cost overruns. (Judge organic execution; *exclude* M&A-driven capacity.) |
| **Promoter shareholding LEVEL** | **>50%** (ideal); higher better | Trend matters more than level; concern if **<25%.** |
| **Promoter shareholding TREND** | **increasing** stake | **Decreasing** stake → scrutinize even if >50% (selling can be benign/personal, but investigate). |
| **Promoter buying shares** | insider buying = strong BUY signal (follow them in) | (selling not necessarily negative — shares are often the promoter's biggest asset) |
| **FII/institutional shareholding** | per checklist, *lower the better* (undiscovered = re-rating upside) | (note: once an institution crosses **25%** it gains strategic influence — track it) |
| **Pledged promoter shares** | **0%** | **Any pledge = caution** (first sign of promoter/company financial stress; forced selling risk). Generally avoid pledged-promoter companies. |

**[CS] Field-tested refinements (management — these caught real problems in the case studies):**
- **Test "independent" directors for *real* independence.** Cross-check each independent director against the promoters' private companies via the MCA / **Zauba Corp** database. If the "independent" director sits on the promoters' private entities, he is independent only on paper. *National Fittings:* "independent" director Loganathan was a director on nearly all the promoter's private companies; effectively 3 of 4 directors were promoter-aligned (75%). Also discount long-time-employee directors as non-independent.
- **Related-party purchasing/sourcing from promoter entities = quiet leakage.** Buying raw material / leasing premises from holding/promoter companies routes margin out of the listed company. *National Fittings:* bought ₹19.86cr rough castings from holding co Interfit + leased land from it (~₹2cr/yr leakage) and gave ₹2.7cr interest-free advances to related parties. Quantify the leakage (assume ~10% margin on RPT purchases).
- **MNC subsidiary milked by the parent.** A foreign-parent subsidiary can be drained via dividends exceeding FCF and via stingy India capex. *Merck India:* paid ₹341cr dividends on only ₹167cr FCF (funded by liquidating its own FDs; FY2010 div ₹158cr vs PAT ₹63cr) — parent Merck Group the main beneficiary, minimal India growth investment. Also watch **brand-buy-from-parent** RPTs (*Hindustan Media* paying ₹62cr to parent HT Media for brands it licensed for ₹1 lakh).
- **Promoter salary near the statutory ceiling / ~15% of PAT = red flag even in a good company.** *Ratnamani:* gross management salary ₹26.94cr vs Companies-Act ceiling ₹28.44cr, on PAT ₹172cr (~15.7%) — the one weak spot in an otherwise strong company. (Norm is 2–4% of PAT.)
- **Declining promoter stake → investigate before buying.** *Kaveri:* promoters cut stake 63.64%→57.49%. Get a credible reason.
- **Idle cash + falling dividend payout = capital-allocation question.** *Hindustan Media:* ₹587cr cash pile yet DPR fell 11%→5% — where is the cash going?
- **ROE alone is NOT meaningful — decompose it.** ROE = profitability × asset-turnover × leverage. A high ROE built on *leverage* is bad. Require the good kind: **high NPM + high asset turnover + LOW debt.** Don't reward a company for a high ROE that comes from borrowing.

**[V1] Field-tested governance red flags (each caught a real problem in the deep-dives):**
- **Credit-rating shopping** — a company that gets downgraded and then *switches rating agency* to get a better grade is hiding weakness. *Omkar:* CRISIL cut it 3 notches BBB+→BB+ (junk); it dropped CRISIL and moved to Brickwork (BBB). A rating *withdrawn* "for lack of information" = company stonewalling. (Use the rating *direction*; a downgrade to junk is a near-veto.)
- **Management that repeatedly misses its own stated commitments** (deadlines, "we won't sell/pledge more" then does) = competence + credibility failure (Omkar: pledge-release deadlines missed 3×; "won't sell stake" → stake fell 58%→41%).
- **Signs of fundraising desperation:** very high IPO/issue cost as % of proceeds (Omkar 14%, Wonderla 6.25%); loan-against-promoter-shares from NBFCs at 18–19%; heavy promoter pledging; opaque shareholding disclosure that obscures the true pledged/owned split.
- **Promoter running a PARALLEL or COMPETING business** (or chasing unrelated ventures while the company is stressed). Verify via MCA/Zauba. *Divi's:* the promoters (Murali Divi, N.V. Ramana) are directors of "Divi's Pharmaceuticals Pvt Ltd," a separate USFDA-inspected pharma exporter — divided loyalty + potential competition, despite ₹45cr/₹23cr salaries. *Omkar:* promoter's son chasing a brokerage open-offer mid-crisis.
- **Pharma/regulated-industry data-integrity findings = integrity veto.** USFDA "data falsification" observations (*Divi's*) directly question management honesty (cf. Ranbaxy, GVK Bio).
- **Demerger/asset transfer at fair value < book value** moves value out of the listed entity and flatters the receiving entity's ratios (Omkar→Lasa: ₹63cr loss to Omkar shareholders; Lasa then shows higher asset-turnover/PAT at listing).
- **Check the promoter's OTHER group companies** for SEBI/fraud history. *Nandan Denim:* chairman also chaired Nova Petrochemicals (SEBI case: bogus expansion announcement + misleading results where *quarterly profits summed to a profit but the audited annual showed a loss* — a manipulation tell); group cos had books-violation fines and other FIRs.
- **Warrants — read the issue price vs market.** Below market to promoters = a gift / backdoor stake (Rexnord ₹13.40 vs ₹23.34). *Above* market (Nandan ₹200 vs market ₹100–160) is counter-intuitive → suspect parking/round-tripping. **Preferential equity is better than warrants** (equity = 100% cash to company upfront; a warrant gives the company only 25% upfront, the other 75% is the promoter's option — so warrants are ~25% for the company, ~75% for the promoter).
- **Reverse-RPT extraction:** the company *paying* related parties above-market — interest-bearing deposits *from* related parties at 10–12% when banks lend at ~8.85% (Nile); or being **squeezed from both ends** (Machino: customer-shareholder Maruti blocks cost pass-through *to* it, while supplier-shareholder Machino Polymers passes all cost rises *onto* it).
- **Non-core capital misallocation:** a manufacturer running a **stock-market trading book** (Bhageria ₹33cr equities > ₹27cr operating assets, booking short-term gains), holding junk/delisted quoted shares (AksharChem), buying & selling subsidiaries in quick succession, or unrelated **diworsification** into capital-intensive lines (Bhageria → solar).
- **Remuneration above the statutory ceiling** (auditor qualification / clawback / AGM resolution to keep pay high even if profits are inadequate) = greedy (AksharChem clawback; Machino qualification). Salary *at* the exact Companies-Act ceiling is also a flag (Nile).
- **Unexplained "Others" loans & advances** to undisclosed parties (Ishan: ₹3cr ≈ 75% of PAT to "Others") — possible siphoning.
- **Submitting financial projections/targets to exchanges** = pressure to hit numbers by shortcuts (Machino) — a subtle negative, not a positive.
- **Statutory non-compliance & AR sloppiness:** missing woman director (BSE fine) / company secretary / valid N&R committee; AR arithmetic that doesn't tally (MRF indebtedness), copy-pasted sections (Ishan), factual howlers ("agriculture is India's largest GDP contributor" — Nandan), in-house Registrar & Transfer Agent instead of an independent one (MRF). Individually minor; collectively a governance-quality signal.
- **Low *reported* promoter stake can be benign** — large "public" holders are often promoter friends/family who vote with them. Probe surnames/relationships; a "public" holder *gifting* shares to a promoter (reclassified as promoter) confirms the link (Ishan: ~28% with "Patel" families). Low stake isn't automatically a control risk, but a *falling* stake still is.
- **Positive management signals to credit (Caplin is the model):** founder takes **zero salary**, successor (Harvard MBA) paid a *nominal* ₹1.5L/mo (below market), innovative/risk-taking track record, clear succession. Contrast Ruchira Papers paying 8 relatives (29–69 yrs, 8–23 yrs exp) the *identical* salary — pay unlinked to contribution = flag.

**Verdict:** management is a **hard veto.** If integrity is in any doubt (fraud history, self-dealing RPT, warrant abuse, debt-funded dividends to self, fake-independent boards, parallel competing businesses, data falsification, rating-shopping) → **REJECT**, even with flawless financials/valuation. "Investment in a great business is futile if management isn't shareholder-friendly." Never trust awards/ratings as proof of integrity.
Note the nuance from the cases: management red flags are often a matter of *degree* — National Fittings/Kaveri/Ratnamani have strong businesses with *some* governance blemishes (not outright fraud), so the verdict is "get comfortable with management first," whereas Rexnord-style warrant abuse + backdoor control is a clean reject. Weight integrity breaches (self-dealing, fabrication) as vetoes; weight blemishes (one high salary, minor RPT) as cautions to price in.

---

## 8. MARGIN OF SAFETY — the cornerstone (Stage 7 GATE: need BOTH kinds)

MoS = the cushion for being wrong. A buy needs MoS in **price** AND in **business**:

**A) MoS in the PURCHASE PRICE (1 test):**
- **Earnings Yield (EY = EPS/CMP) > 10-yr G-Sec/Treasury yield.** Bigger gap = bigger cushion. → keep P/E < 10.

**B) MoS in the BUSINESS MODEL (2 tests):**
- **SSGR > achieved sales growth** (self-funded growth — §4). Higher = safer.
- **Positive Free Cash Flow, high FCF/CFO** (§5b). Higher FCF% = safer.
  - FCF = CFO − Capex. Capex = Δ(GFA+CWIP) over year, or Δ(NFA+CWIP)+Depreciation.
  - Logic: in a downturn, a high-FCF, high-SSGR firm can cut prices/dividends, extend customer credit, pay suppliers fast — *all without new debt*. (HUL: 10-yr CFO ₹26,298cr, capex only ₹3,718cr → **86% FCF**, dividends ₹20,543cr, debt-free → trades P/E ~40s. Atul Auto FCF% 48%, TTK 42%.) A 0%/negative-FCF firm (Bhushan Steel FCF% −300%; NFL negative) cracks at the first downturn.

**The rare jackpot = BOTH high MoS-in-business AND low P/E (cheap).** Most great-business names are already expensive (no price MoS); most cheap names are weak businesses (no business MoS). The whole game is finding the overlap. Only a handful in a lifetime are needed.

---

## 9. CREDIT RATING CHECK (Stage 8 GATE)

> Read **all** credit-rating reports (CRISIL/ICRA/CARE/India Ratings), latest *and historical*. Even free summary reports carry
> management-private info (customer names, contract terms, capacity utilization, expansion status, key risks) and a 3rd-party
> verification of the financials and of my own thesis.

- **Threshold:** current rating **≥ BBB-** AND **trend improving** over the years.
- **Direction > level:** prefer a co rated **BBB-→A-** (improving) over one **AA+→A** (deteriorating) even though the latter's absolute rating is higher. Rating *movement* is a clean proxy for fundamental trajectory.
- A *falling* rating while you think fundamentals are *improving* = recheck your analysis (you're likely missing something).
- Example arc: Oriental Carbon & Chemicals BBB (2008) → A (2015) tracked its real improvement (margins 12%→25%+, debt down), and reports explained the *why* (quarterly contracts to pass on raw-material costs; new customer approvals; value-added grades) that the annual report alone didn't reveal.

---

## 10. OPERATING-PERFORMANCE TREND (Stage 9 — confirm the engine, 5 steps over 10 yrs)

Confirms the business is *improving*, not decaying. Each should be **stable or improving**; multi-year deterioration = caution/avoid (and is also the SELL trigger §14).

1. **Sales growth** — consistent CAGR, no one-year spikes masking weak years.
2. **Profitability** — OPM & NPM stable/rising (not wild swings / steady decline).
3. **Operating efficiency:**
   - **Inventory Turnover = Sales/avg inventory** — stable/↑ (↓ = capital stuck / obsolete stock).
   - **Receivable Days = avg receivables/Sales ×365** — stable/↓ (↑ = can't collect → working-capital/interest drag).
   - **Fixed-Asset Turnover = Sales/Net Fixed Assets** — stable/↑ (↓ = capital-guzzling; e.g. Amtek's very low turnover drove its debt up 33×). FAT of 2 = each ₹1 of plant yields ₹2 sales.
4. **Profits → free cash** — cumulative **CFO should exceed cumulative PAT** (add-back of interest+depreciation should make CFO>PAT if working capital is managed). cCFO<cPAT = profit stuck in working capital.
5. **Free cash funds growth** — expansion funded by internal cash, **not spiraling debt.** (*Honda SIEL* = grew sales at the cost of profitability + falling inventory turnover + rising receivables + no free cash → avoid pattern.)

Note: compare a company to **its own** history (trend) rather than across industries — an infra co may run higher debt than a pharma co, but *rising* debt without matching sales/net-worth growth is bad in *both*.

---

## 11. THE FINAL CHECKLIST (consolidated PASS/FAIL — apply before any BUY)

> A stock should clear essentially all of these. Treat **Financial #8, all Management, Fraud flags, and Valuation price-gate** as
> non-negotiable. (No checklist is exhaustive — but anything failing here needs an explicit, strong reason to override.)

**FINANCIAL ANALYSIS**
- [ ] 1. Sales growth: **CAGR >15% for 7–10 yrs**, consistent (ignore 1-yr spikes; >50% = unsustainable)
- [ ] 2. Profitability: **NPM >8%**, sustained OPM & NPM
- [ ] 3. Tax payout: **≈ >30%** (near corp rate unless a stated incentive)
- [ ] 4. Interest coverage: **>3**
- [ ] 5. Debt/Equity: **< 0.5** (preferably 0)
- [ ] 6. Current ratio: **>1.25**
- [ ] 7. Cash flow: **CFO > 0** (great if CFO covers CFI+CFF)
- [ ] 8. **cPAT ≈ cCFO** over 10 yrs

**VALUATION**
- [ ] P/E: per the **4 Principles** target (base = 1/G-Sec, + moat/FCF/stable premiums); prefer **<10**
- [ ] PEG: **<1**
- [ ] EY: **> 10-yr G-Sec yield**
- [ ] P/B: **<1** (only weighted for financial sector)
- [ ] P/S: buy **<1.5**, sell **>3**
- [ ] Dividend Yield: **>0** (>5% attractive; ignore for fast-growers)

**BUSINESS & INDUSTRY (moat)**
- [ ] Sales growth **> peers**
- [ ] Production capacity & **volume** CAGR ≈ sales CAGR (volume-led, not price-led)
- [ ] **Profit CAGR ≈/≥ Sales CAGR**
- [ ] **cPAT ≈ cCFO** (profit collected as cash)
- [ ] **ΔMCap(10y) > retained profits(10y)** (creates, not destroys, value)
- [ ] Product: **pure play / related** (no unrelated diversification)
- [ ] **No govt interference** in pricing/profit

**MARGIN OF SAFETY**
- [ ] Price: **EY > 10-yr G-Sec**
- [ ] Business: **SSGR > achieved sales growth**
- [ ] Business: **FCF/CFO >> 0** (positive, high)

**MANAGEMENT — subjective**
- [ ] Background check: **nothing** questioning promoter/director integrity
- [ ] Succession plan in place; successor salaries modest/in-line

**MANAGEMENT — objective**
- [ ] Promoter salary: **no rise during declining profits/losses** (2–4% of PAT norm)
- [ ] Project execution: good, **no cost/time overruns** (exclude M&A)
- [ ] Dividend CAGR **>0** (rising with profits) **and funded by FCF (not debt)**
- [ ] Promoter shareholding **≈/>51%** (higher better)
- [ ] Promoter **buying** shares (insider buying = + ; follow them)
- [ ] **FII shareholding low** (undiscovered = re-rating upside)
- [ ] **No pledged** promoter shares
- [ ] No abusive **warrants**, no value-extracting **RPTs**

**CREDIT RATING**
- [ ] **≥ BBB-** and **improving** trend

→ **All clear → BUY** (size per §12). **Any hard veto (fraud/management/price) → REJECT.**

---

## 12. BUY DECISION & PORTFOLIO CONSTRUCTION (Stage 10)

**Buy decision = passes §11 + price ≤ target P/E (§5b).** Then:

**Portfolio sizing rules:**
- **Number of stocks: between 2 and 30.** Min 2 (from different industries) for any diversification; beyond ~30 adds *no* further risk reduction and dilutes winners. **Keep the number as LOW as comfortable** (concentrate in best ideas — Buffett: "buy worthwhile amounts when convinced").
- Cap the count by **monitoring bandwidth**: each stock/yr ≈ 4 quarterly results + 4 shareholding disclosures + 1 annual report + 1 credit report + exchange filings + news alerts. (25 stocks ≈ 100 quarterlies, 25 annual reports, etc.) Hold only as many as can be monitored well.
- **New investor:** keep it *small*; park excess in index/MF until stock-picking skill is proven. (Large portfolio ≠ safety; it's harder to monitor.)

**Capital-allocation order (every time new cash arrives):**
1. **First, add to existing well-understood holdings** that still pass the test and are below target P/E (lowest research cost, known management).
2. **Sell** any holding that has **failed the test for 2 consecutive years** (purge laggards).
3. **Only if** nothing in the portfolio is investable → search for a NEW stock.

**Behavioral execution rules (these *are* decision rules):**
- After a clean buy, **price declines on intact fundamentals = BUY MORE** (groceries-on-sale). Recessions reliably recover. (JK Lakshmi fell ₹80→₹32, then IRR 115%; Allahabad Bank ₹70→₹37 then IRR 102%; Haldyn ₹16.5→₹10.3 then IRR 70% — author *added* on the dips.)
- **Hold through stagnation** if fundamentals intact (Mayur flat ₹100–120 for ~1 yr, then +400% in 10 months).
- **Don't chase** above target P/E — wait/hold rather than overpay; the market re-rates in unpredictable spurts.
- Trade as little as possible (cost + peace).
- Retail edge to exploit: monthly fresh savings (buy in bear markets when institutions can't), no redemption pressure, true long-horizon, can sit in cash when nothing is cheap. Use these.

---

## 13. MONITORING (after buying — keep the thesis alive)

Track **business/operating/management** parameters, **not** daily price. Cadence:
- **Ongoing:** Google Alerts for each holding + industry; read corporate announcements (capacity, M&A, mgmt changes, insider trades).
- **Quarterly:** results (filed within 45 days of Q-end, 60 days for Q4 — **a delay is a RED FLAG**, often fraud/governance, e.g. Ricoh India). Read P&L (YTD + quarter), segmental, B/S (in H1/FY), notes, **promoter shareholding & pledge** changes. Don't overreact to 1–2 soft quarters; *do* act if a permanent change appears.
- **Annual:** full annual report + refreshed credit rating (upgrade = +, downgrade = investigate).

Promoter **stake ↑** = positive (consider buying alongside); **stake ↓ consistently** or **new pledge** = investigate/concern. Track institutions only once they cross strategic 25%.

---

## 14. SELL DECISION RULES (Stage 11)

> **Default = NEVER SELL A GOOD STOCK.** A 100-bagger passes through 2×, 10×, 50× first — selling early forfeits the wealth.
> **Sell decisions must be DISSOCIATED FROM PRICE** (ignore current price, buy price, and unrealized gain/loss).
> Do **NOT** sell on: doubling, target %, trailing stop-loss, "sell to recover cost." Those force you out of winners.

**SELL only when one of these *fundamental* triggers fires:**
1. **Deteriorating operating performance for ≥2 consecutive years** — any of: declining sales YoY; declining OPM/NPM; declining efficiency (falling FAT, falling inventory turnover, rising receivable days); continuously rising debt to fund operations. (Require **2 consecutive years** — ignore 1–2 soft *quarters*; temporary dips are times to *buy*, not sell.) If the business advantage has genuinely eroded → sell regardless of profit/loss.
2. **Government starts capping pricing/profitability** of the company (regulated returns → suboptimal). (Gujarat State Petronet, IGL — PNGRB capped profitability.)
3. **Permanent adverse change in business dynamics** (impact not temporary). (Haldyn Glass — PNGRB cut gas supply, forced 20% capacity cut.)
4. **Portfolio has too many stocks to monitor** → sell the weakest to get back to a manageable count.
5. **Position has become a trivially small % of portfolio** (ran up, never added) and isn't worth the monitoring burden — either pray for a dip to add meaningfully, or sell.

Also exit immediately (overrides "never sell") if a **§3 fraud flag** or **§7 management integrity breach** surfaces post-purchase (e.g. self-dealing RPT, fabricated cash, delayed results signaling fraud). Don't anchor to your cost.

Accept that sold stocks may rise afterward — short-term price ≠ fundamentals ("voting machine short-term, weighing machine long-term").

---

## 15. WORKED-EXAMPLE LIBRARY (fast pattern-matching reference)

**GOLD STANDARD PASSES (what a buy looks like):**
- **Vinati Organics:** sales 34% CAGR (volume-led, beats peers), profit 44% CAGR, NPM 7%→12%, cPAT≈cCFO, D/E<1, ₹7.13 MCap per ₹1 retained; bought at P/E 7.7 → IRR 143% (P/E expansion = 81% of it). *The archetype.*
- **Mayur Uniquoters:** bought P/E 6.6 → IRR 136% (P/E expansion 104% of return); held through a year of flat price then +400%.
- **FDC, Container Corp, VST Tillers, Tide Water Oil:** SSGR >> growth, debt-free (self-funded growth).
- **Atul Auto (FCF% 48%), TTK Prestige (FCF% 42%), HUL (FCF% 86%):** high free-cash, debt-free, dividend from FCF.
- **Ambika Cotton, Manappuram:** shareholder-friendly management (modest/declined salary; honored commitments).
- **Oriental Carbon:** credit rating BBB→A improving, real fundamental improvement.

**INSTRUCTIVE REJECTS (what to avoid, and why):**
- **Tata Steel:** sales 28% CAGR but profit 0% (NPM 23%→2%, losses), FCF −₹20,508cr, debt ₹3,377cr→₹80,701cr, dividends debt-funded, ₹0.81 value per ₹1 retained → no moat + bad capital allocation. *Sales growth ≠ value.*
- **Amtek/Castex, Glenmark, Pratibha, Jaiprakash Power, LT Foods:** SSGR << growth → debt spirals (some to bankruptcy/asset sales). *Growth beyond means.*
- **Bhushan Steel (FCF% −300%), National Fertilizers (neg CFO):** cash guzzlers, debt-funded → fragile.
- **Brooks Laboratories:** perfect financials (sales +23%, profit +36%, debt-free) BUT promoter SEBI-fraud history → **REJECT on management alone.**
- **ESS DEE Aluminium:** promoter salary 2%→12% of PAT as profits fell → later debt ₹500cr, losses, stock ₹750→₹90.
- **Gujarat Automotive Gears, Rexnord:** related-party self-dealing (loans to promoter co; commission/warrants to promoter family) → value siphoned from minorities.
- **DCB Bank:** management U-turned a sound long-term plan after a 30% price drop (ESOP-protective) → short-termist.
- **SCI:** 2% sales CAGR, MCap fell → no moat, dead money.
- **Honda SIEL:** growth at the cost of margins + efficiency + cash → avoid.

**Quick numeric anchors to recall:**
- Good NPM ≥ 8% (Vinati 12%); thin/falling NPM (Tata Steel →2%) = bad.
- Good FCF/CFO ≥ ~40% (Atul 48, TTK 42, HUL 86); negative (Bhushan −300) = bad.
- Good promoter salary 2–4% of PAT (Ambika); bad ≥10% / rising-as-profit-falls (ESS DEE 12%).
- Good value-creation ≥ ₹1 per ₹1 retained (Vinati ₹7.13); bad < ₹1 (Tata Steel ₹0.81).
- Good D/E < 0.5 (≈0 ideal); danger = debt rising every year.
- Buy P/E < 10; avoid P/E > 20–25 (no expansion room, contraction risk).

---

## 16. FORMULA APPENDIX (compute these from 10-yr screener data)

```
EPS                = PAT / shares outstanding
P/E                = CMP / EPS
Earnings Yield EY  = EPS / CMP = 1 / P/E
PEG                = P/E / EPS-growth%
P/B                = CMP / (Book value per share)         [Book value = equity + retained earnings]
P/S                = CMP / (Sales per share)
Dividend Yield     = Dividend per share / CMP
EV                 = MCap + Total Debt − Cash & equivalents
EV/EBITDA          = EV / EBITDA

Sales CAGR         = (Sales_end / Sales_start)^(1/yrs) − 1
OPM                = Operating Profit / Sales              [Op profit excludes interest, dep, tax, non-op income]
NPM                = PAT / Sales
Interest coverage  = Operating Profit / Interest expense
D/E                = Total Debt / Shareholder funds
Current ratio      = Current Assets / Current Liabilities
Inventory turnover = Sales / avg Inventory
Receivable Days    = (avg Receivables / Sales) × 365
Fixed-Asset Turn   = Sales / Net Fixed Assets
NFAT               = Sales / avg Net Fixed Assets         [NFA = Gross FA − accumulated depreciation]
DPR                = Dividends / PAT
Dep (for SSGR)     = Depreciation / Net Fixed Assets      [as a %]

SSGR               = NFAT × NPM × (1 − DPR) − Dep         [use 3-yr averages of NFAT, NPM, DPR, Dep]
                   = [(1 − Dep) + NFAT × NPM × (1 − DPR)] − 1

FCF                = CFO − Capex
Capex              = Δ(Gross FA + CWIP) over the year
                   = Δ(Net FA + CWIP) + Depreciation for the year
FCF%               = FCF / CFO
Fraud-adjusted CF  = CFO − Capex − Cash paid for acquisitions

cPAT               = Σ PAT over 10 yrs       cCFO = Σ CFO over 10 yrs
Value per ₹ retained = Δ MCap (10y) / Retained profits (10y)     [Buffett $1 test, want ≥ 1]

Target P/E         = (1 / 10-yr G-Sec yield)
                     + SSGR premium (≈ +1 P/E per 5–10% SSGR-above-growth)
                     + FCF% premium (≈ +1 P/E per 5–10% FCF%)
                     + circle-of-competence premium (small)
                     + stable-business premium (+10–15 if MCap > ~₹10,000 cr & strong)
```

**Decision shortcut when time-constrained:** compute, in order — (1) 10-yr sales CAGR & NPM, (2) D/E & cPAT-vs-cCFO,
(3) FCF% & SSGR-vs-growth, (4) P/E vs target, (5) promoter salary%/RPT/pledge/SEBI-search.
If any of {cCFO<<cPAT, NPM<8%, debt spiraling, FCF negative, SSGR<<growth, P/E>>target, management integrity flag} → **REJECT**.
Only a stock clean on *all* of them earns a deeper read and a BUY.

---

## 17. CASE-STUDY EXAMPLE LIBRARY (my pattern-match reference — read this when analyzing any company)

> **How I use this:** when handed a company, I (a) run §1–§16, then (b) find the closest case below and copy its reasoning and verdict logic.
> These are 20 *real* worked analyses (Vijay Malik's Case Studies ebook). Each card gives the numbers, the verdict, and the transferable lesson.
> All "value created per ₹1 retained" = ΔMCap(10y)/retained-profits(10y) (Buffett $1 test; want ≥1, the higher the better).
> Verdicts were one-off snapshots at their dates — treat them as *reasoning templates*, not live calls.

### 17a. The recurring archetypes (match your company to one of these first)

| Archetype | Signature | Verdict default | Cases |
|-----------|-----------|-----------------|-------|
| **Clean compounder, cheap** | sales>15%, NPM>8%, cPAT≈cCFO, +FCF, SSGR>growth, debt-free, good mgmt, **P/E<~11** | **BUY** (rare) | (the goal; National Fittings *almost*, ex-management) |
| **Great business, too expensive** | all-green fundamentals but **P/E 25–80** | **PASS on price** (watch for a dip) | Amara Raja (40), Supreme (29), Symphony (63), Page (78) |
| **Strong biz, governance blemish** | great numbers + *some* RPT/board/salary issues | **Conditional — get comfortable with mgmt first** | National Fittings, Kaveri, Ratnamani |
| **Self-dealing management** | warrant abuse, backdoor control, related-party to family, governance non-compliance | **REJECT (veto)** | Rexnord, Virat Crane |
| **Growth beyond means (SSGR<<growth)** | high sales growth, debt spiraling, profits stuck | **REJECT** | KRBL, Sarla, Ujaas, Meghmani, Fiem |
| **Capital-intensive low-margin trap** | low NPM + low fixed-asset-turnover → debt | **REJECT** | Meghmani, Fiem, Sarla |
| **Value trap** | low P/E + high DY but MCap eroding / regulatory threat | **AVOID** | Noida Toll Bridge |
| **Structural model loser** | FX-wrong-way / parent-milked / no expansion | **AVOID / no catalyst** | Merck, Zenith (no growth), Hindustan Media (watch cash) |
| **Quality masked by accounting** | NPM inflated by forex/low-tax/non-op; high-cash+high-debt | **Forensic diligence before trusting** | Torrent Pharma |

### 17b. The 20 verdict cards

**1. National Fittings — *strong biz + board/RPT blemish* (P/E 9.9, ~MoS).**
Sales 25% CAGR; OPM 6%→20%, NPM loss→14%; tax 33–34%; NFAT 1.43→8.83; ITR 1→9; receivables 81→16d (90% exports on LC); cPAT ₹18cr≈cCFO ₹17cr; SSGR 25–30%; FCF ₹12cr/CFO ₹17cr; debt-free; div rising from FCF; value ₹4.36/₹1; salary reasonable (~₹2L/mo on ₹7.4cr PAT).
⚠ "Independent" director sits on all promoter private cos (Zauba); 3/4 directors promoter-aligned; RPT purchases from holding co Interfit (~₹2cr leakage); ₹2.7cr interest-free advances to related parties.
**Verdict:** financially a near-ideal cheap compounder; **conditional on getting comfortable with management.** *Lesson: a clean P&L doesn't clear the management gate — verify board independence via MCA/Zauba.*

**2. Torrent Pharma — *quality masked by accounting* (P/E 14, no MoS).**
Sales 20% CAGR; OPM 14–16%, NPM ~10% but volatile; tax 20–25% (SEZ/Sikkim/HP incentives); cPAT ₹3,096cr≈cCFO ₹3,325cr; FCF ₹1,017cr (9y); SSGR 25–30%.
⚠ ₹253cr forex gain = 27% of PBT (true NPM ~11.8% vs reported 16%); ITR 6→4, receivables 53→106d; ₹222cr standalone receivables >6mo from own US/Brazil/Romania subs not remitting; **high cash + high debt** (~₹900cr each, ~₹100cr/yr wasted interest); serial debt-funded acquisitions (Elder, Zyg) → debt ₹2,740cr; dividends paid *while* borrowing.
**Verdict:** good growth/FCF but **needs forensic diligence; avoid until cash/receivables/acquisition concerns resolve.** *Lesson: strip non-op income; high-cash-with-high-debt is a fraud-adjacent tell; chase the receivables to subsidiaries.*

**3. Rexnord Electronics — *self-dealing management* (P/E 20, no MoS). REJECT.**
Sales 20–30%; OPM cyclical 6–14%, NPM low 1.4–4.8% (weak pricing power); tax >30%; cPAT ₹9cr<cCFO ₹20cr (working-capital release); SSGR only 5–6% **<< growth 20–30%** (funded by WC release + debt ₹3→8cr + warrant equity); FCF only ₹1cr.
⚠ Warrants to promoters @₹13.40 vs market ₹23.34 (43% disc, ₹3.36cr gift); promoters took majority 46.47%→51.46% via warrant conversion (backdoor); sales-commission contract to son-in-law's firm Excelum (≤₹2cr/yr); N&R committee non-compliant (§178, auditor-flagged, ignored); company secretary resigned.
**Verdict:** **REJECT** — SSGR<<growth + serial governance abuse. *Lesson: warrant-at-discount + backdoor control + family RPT = veto.*

**4. Virat Crane — *self-dealing + negative FCF* (P/E 20.4). AVOID.**
Sales 18–20%; OPM cyclical 3–14%, NPM 1–9% (FY15 spike suspect); cPAT ₹17cr **>> cCFO ₹5cr** (stuck in inventory); SSGR 6–7% << growth; **FCF −₹5cr** (CFO ₹5cr < capex ₹10cr) → funded by equity dilution.
⚠ No company secretary (§203 non-compliance); corporate guarantees to non-subsidiary group cos (₹10cr+₹13.24cr); ₹8.4cr interest-free loans to group cos; deals with MD's personal firm (Crane Betel Nut); spelling mistakes in AR.
**Verdict:** **AVOID** — negative FCF + equity dilution + multiple RPT/governance flags. *Lesson: contingent guarantees for group cos and sloppy ARs are real signals.*

**5. Kaveri Seed — *strong biz + disclosure/stake blemishes* (P/E 14.2).**
Sales 40–45% CAGR; OPM 20–27%, NPM 16–26% (seed entry-barrier moat, farmers pay premium); debt-free; SSGR 50–70% >> growth; FCF ₹347cr/CFO ₹635cr; value ₹3.8/₹1.
⚠ Tax only 3–5% (incentive — model NPM at 30%); ITR 9.4→2.3 (working-capital heavy); cPAT ₹823cr>cCFO ₹635cr; **68% of receivables >6 months, writing off ₹4–4.5cr/yr**; promoter stake 63.64%→57.49%; RPT (land lease from promoters, sales to 70%-owned Aditya Agritech); unspent CSR; auditor omitted disputed tax; Monsanto royalty lawsuit + Maharashtra MRP cut.
**Verdict:** strong business; **watch tax-incentive dependence, receivables quality, stake cut, disclosure standards.** *Lesson: read receivables ageing; very-low-tax NPM is fragile.*

**6. Ratnamani Metals — *strong biz + one high-salary flag* (P/E 16.5).**
Sales 10–20%; OPM 18–20%, NPM 9–11% sustained; tax 32–35%; NFAT→3.87; debt cut ₹106cr→₹30cr (D/E 0.03); SSGR 18–20%; FCF ₹273cr/CFO ₹910cr; value ₹3.10/₹1; CRISIL: 35%+ market share in SS tubes, backward-integrated (moat).
⚠ cPAT ₹986cr>cCFO ₹910cr (working-capital intensive, per CRISIL); promoter salary ₹26.94cr ≈ ceiling ₹28.44cr on PAT ₹172cr (~15.7%).
**Verdict:** good business; **only weak spot is high promoter salary**; no price MoS at 16.5. *Lesson: credit reports reveal market share/capacity; salary near ceiling is a flag even in quality names.*

**7. Emami — *great FMCG business* (strong moat).**
Sales 20–25% CAGR; OPM 24–25% sustained; cPAT ₹2,158cr≈cCFO ₹2,304cr; NFAT 1.74→5.22; ITR 8.7→16.6; receivables 29→15d; ad-spend 15–17% of sales (brand moat); brand shares Navratna 49%→65%, Boroplus 74%→76%; **value ₹15.79/₹1** (exceptional).
⚠ NPM 12%→22% boosted by low tax (12–18%) + non-op income + falling interest — true operating quality a bit lower; flag incentive expiry.
**Verdict:** excellent business; buyable only if valuation gives MoS (usually rich). *Lesson: heavy sustained ad-spend + high market share = FMCG moat; adjust NPM for tax/non-op.*

**8. KRBL — *growth-beyond-means, negative FCF* (P/E 16). AVOID.**
Sales 15–20%; OPM 14–15% stable (India Gate brand premium); tax 17–33% (NPM 4–10% varies); NFAT flat; **ITR 1.3–2.0 (very low — buys whole-year paddy Oct–Dec, ages rice 12–18 months)**; cPAT ₹1,226cr **>> cCFO ₹640cr**; capex ₹940cr > CFO ₹640cr → **FCF −₹300cr**; debt ₹452cr→₹1,281cr; **dividends ₹133cr paid from borrowed money.**
**Verdict:** **AVOID** — structurally working-capital heavy, negative FCF, debt-funded dividends. *Lesson: brand premium doesn't fix a structurally cash-absorbing model.*

**9. Meghmani Organics — *low-margin capital-intensive trap* (P/E 9.9). AVOID.**
Sales 7–10%; OPM 14–16% stable but **NPM only 2–3% (interest ₹16cr→₹75cr eats it)**; NFAT 7.5→1.8, ITR 7.2→5.5 (deteriorating); debt ₹209cr→₹603cr; **PBT/NFA <9% (below bank FD)**.
**Verdict:** **AVOID despite low P/E** — value trap. *Lesson: the PBT/NFA-below-FD test; low NPM + low NFAT = debt; cheap ≠ buy.*

**10. Zenith Fibres — *clean but no growth catalyst* (P/E 7.2, cheap-justified).**
Sales 10–15%; OPM 8–13%/NPM 5–9% cyclical (low pricing power; PP losing to polyester); tax 34–36%; NFAT 4.48→11.77; **no capacity expansion in 10 yrs** (only ₹6cr maintenance capex); FCF ₹19cr; debt-free; SSGR 30–40%; professional mgmt (non-exec promoter; ex-RBI governor on board; staff raises > KMP raises); **value only ₹1.38/₹1**.
**Verdict:** low P/E is *justified* — clean and debt-free but no growth engine → limited upside. *Lesson: cheapness can be deserved when there's no expansion; value ~₹1.38 signals mediocrity.*

**11. Merck India — *FX-wrong-way + parent-milked* (P/E 29). AVOID.**
Sales 10–15% but **OPM collapsed 24–26%→7%, NPM 20%→5%** (imports inputs in USD, sells in INR; INR −60%); tax 33–35%; ITR 8.8→5.3 (obsolete-inventory write-offs); cPAT ₹642cr>>cCFO ₹318cr; SSGR 40–50% (high NFAT) but growth only 10–15%; **dividends ₹341cr > FCF ₹167cr** (funded by liquidating FDs; benefits parent Merck Group); value ₹1.97/₹1.
**Verdict:** **AVOID** — structural FX disadvantage + parent extraction + expensive. *Lesson: check import/export FX direction; MNC subs can be milked via dividends > FCF.*

**12. Noida Toll Bridge — *value trap* (P/E 5.6, DY ~12%). AVOID.**
Sales 8–10%; OPM 70–73% (toll); NPM 33–66% (tax 1–36%); receivables 4d (cash toll); cPAT ₹363cr<cCFO ₹661cr; FCF ₹419cr; repaid debt + ₹149cr dividends.
⚠ Competing bridges (Sarai Kale Khan, Kalindi Kunj) + proposed Barapullah Phase III; **MCap fell ₹189cr vs ₹214cr retained — wealth erosion.**
**Verdict:** **VALUE TRAP** — cheap + high DY but eroding business/no growth visibility; capital loss > dividend. *Lesson: don't buy DY while MCap erodes.*

**13. Amara Raja Batteries — *great business, too expensive* (P/E 40). PASS on price.**
Sales 25–30% CAGR; OPM 15–18%/NPM 9–10% sustained; tax 32–34%; NFAT 4.61→8.3; ITR 7.0→11.2; receivables 70→44d; cPAT ₹1,841cr≈cCFO ₹1,782cr; SSGR 40–45%; debt-free (D/E 0.04); FCF ₹389cr; **value ₹6.6/₹1**; rising dividends.
**Verdict:** textbook quality business but **P/E 40 = no MoS → PASS** (wait for a dip). *Lesson: the price gate is independent of quality; a wonderful business is still a "no" when overpriced.*

**14. Symphony — *great business, far too expensive* (P/E 63.5). PASS on price.**
Sales 30–40% CAGR; OPM 21–30% (high even in down years); SSGR 60–70%; debt-free; FCF ₹218cr; cPAT ₹361cr≈cCFO ₹313cr (gap is one year); **value ₹25.57/₹1** (asset-light air-cooler moat, outsourced manufacturing).
**Verdict:** exceptional business, **valuation absurd → PASS.** *Lesson: even a 25× value-creator must clear the price gate.*

**15. Hindustan Media Ventures — *good biz, watch capital allocation* (P/E 11.9, limited MoS).**
Sales 35–40% (post-2009 Hindi biz transfer); OPM 3–5%→18–20%, NPM→17–18%; cPAT ₹470cr≈cCFO ₹505cr; NFAT 2.2→4.69; ITR 19.9→40.2; receivables 47→21d; SSGR 40–45%; ₹587cr cash pile.
⚠ Raised ₹78cr short-term debt *despite* ₹587cr cash (**treasury arbitrage** — avoid in non-financials); DPR fell 11%→5% while cash ballooned; buying brands from parent HT Media for ₹62cr (was licensed for ₹1 lakh) → RPT cutting non-op income ~₹6cr/yr.
**Verdict:** good business at a fairish price; **hinges on cash deployment / parent RPT.** *Lesson: idle-cash-plus-fresh-debt and parent brand-buys are capital-allocation flags.*

**16. Ujaas Energy — *regulatory-dependent speculation* (P/E 30.2). AVOID.**
Sales spiked 7× (₹34cr→₹234cr→₹526cr) then **crashed 80% to ₹111cr** on solar-policy change; OPM 1–38%/NPM 1–11% wild; NFAT 38→1.4→6.1 erratic; **cPAT ₹65cr vs cCFO −₹43cr** (FY12–14); debt ₹2cr→₹120cr; India Ratings negative outlook.
**Verdict:** **AVOID** — "a proxy for speculation on regulatory actions." *Lesson: >30–35% growth is unstable; policy-dependent + wildly swinging ratios = unestablished model.*

**17. Page Industries — *great brand, too expensive + WC chink* (P/E 78.3). PASS on price.**
Sales 30–35% CAGR; OPM 20–21%/NPM 11–13% sustained; tax 31–34%; NFAT 5.3→7.9; ITR 4.1→7.4; SSGR 40–50%; **value ₹33.6/₹1** (Jockey/Speedo licence moat).
⚠ cPAT ₹734cr>cCFO ₹547cr (receivables 18→21d, debt ₹13cr→₹134cr).
**Verdict:** elite business but **P/E 78 = no MoS → PASS**; minor receivables chink to watch. *Lesson: brand quality never overrides the price gate.*

**18. Sarla Performance Fibers — *deteriorating capital-intensive* (P/E 13.4). AVOID.**
Sales ~15%; OPM 14–20%/NPM 8–12% fluctuating (low pricing power); **NFAT 4.7→1.8, ITR 5.2→4.0 (deteriorating)**; cPAT ₹146cr>cCFO ₹114cr; receivables ~90d; debt ₹43cr→₹203cr; SSGR 14–15%.
**Verdict:** **AVOID** — declining efficiency + rising debt + low bargaining power. *Lesson: deteriorating NFAT/ITR in a capital-intensive co = future debt.*

**19. Supreme Industries — *good biz, slightly expensive, watch the slope* (P/E 29). PASS/watch.**
Sales 16–19%; OPM 15–16%/NPM 7–9% stable; tax 33–34%; NFAT stable 3.7–4.0 (*declining recently*); ITR 7.7–9.0 (*declining recently*); receivables 20d; cPAT ₹1,410cr<cCFO ₹1,886cr; **SSGR 11–13% < growth 16–19%** (gap funded by modest debt ₹237→385cr); value ₹8.5/₹1; DPR 30–35%.
**Verdict:** good business, no MoS at 29; **watch falling NFAT/NPM (would drop SSGR and force debt).** *Key Q&A lessons embedded here: verify macro excuses vs peers; brand = consistently higher margins than peers; author's own rule = G-Sec/FD ~9–10% → max P/E ~10–11; ROE only good if from margins+turnover not leverage; invert via the checklist.*

**20. Fiem Industries — *low-margin low-turnover auto-ancillary* (P/E 16.35). CAUTION/AVOID.**
Sales 20–25%; OPM 9–13%/NPM 2–8% fluctuating (OEM pricing pressure); tax ~30%; **FAT low 2.1–2.4 + low NPM = capital-intensive**; PAT ₹146cr vs investing need ₹349cr → gap met by inventory release (ITR 12→15.8) + debt (₹23cr→₹139cr, recently reduced via efficiency).
**Verdict:** **CAUTION/AVOID** — once efficiency maxes, debt likely rises again. *Lesson: low NPM + low FAT is structurally capital-hungry; auto-ancillary/OEM suppliers face permanent margin pressure.*

### 17c. New decision rules distilled from the cases (add to the checklist mentally)

1. **Cheap ≠ buy.** Always separate "low P/E because undiscovered good business" (buy) from "low P/E because structurally weak/declining" (value trap). Use value-creation (≥₹1/₹1) + PBT/NFA-vs-FD + MCap trend to tell them apart.
2. **Great ≠ buy.** A wonderful business at P/E 29–78 is a **PASS on price**, not a buy. Keep it on a watchlist for a dip. (Amara Raja, Supreme, Symphony, Page.)
3. **Management blemish ≠ automatic veto, but integrity breach IS.** Grade it: self-dealing/fabrication/warrant-abuse/backdoor-control = veto (Rexnord, Virat Crane); one high salary or minor RPT in an otherwise strong, honest company = caution to price in (Ratnamani, National Fittings, Kaveri).
4. **Adjust reported NPM** for: non-operating income (forex/interest), tax incentives (recompute at ~30%), and one-offs — before believing the quality.
5. **Two cash tells:** cPAT>>cCFO (profits stuck — check ITR/receivables ageing) and **high-cash+high-debt** (treasury game or fake cash).
6. **Two structural-debt tells:** SSGR << sales growth, and low-NPM+low-fixed-asset-turnover. Both → the company *must* keep borrowing → eventual stress.
7. **Verify the story:** macro excuses → compare peers; "brand" → demand higher consistent margins than peers; "independent" directors → MCA/Zauba cross-check; credit-rating report → mine for market share/capacity/working-capital sensitivity.
8. **FX direction & regulatory dependence** can make an otherwise-fine business structurally un-investable (Merck, Ujaas, Noida Toll).

### 17d. The one-screen analysis dashboard (reconstruct this for every company — the author's template)

Pull 10 years from screener.in into this layout; it ties every gate together at a glance:

```
Row inputs (10 cols = 10 years) + a "10-yr total/CAGR" column:
  Sales | Operating Profit | OPM% | Other Income | PBT | Tax% | PAT | NPM%
  CFO | Capex[(NFA+CWIP)Δ+Dep] | → FCF (=ΣCFO−ΣCapex) | FCF% (=FCF/CFO)
  SSGR%  vs  Past sales growth (3/5/7/10-yr CAGR)
  NFAT (high=good) | Receivables days (low=good) | Inventory turnover (high=good)
  NFA | CWIP | Share Capital(↑=dilution) | Dividend(incl DDT) | DPR% | Retained Earnings
  Total Debt | Total Equity | D/E
  CFO | CFI | CFF | Net cash | Cash at year-end
  Σ Retained Earnings(10y) | Σ ΔMCap(10y) | Value created per ₹1 retained (=ΔMCap/RE)
```
Read it top-to-bottom against the §11 checklist. Reference value-creation numbers seen in the cases:
Symphony 25.6 · Page 33.6 · Emami 15.8 · Amara Raja 6.6 · National Fittings 4.4 · Kaveri 3.8 · Ratnamani 3.1 · Merck 2.0 · Zenith 1.4 · Noida Toll **negative**.
(≥~3 is good; ~1 is mediocre; <1 or negative = value destroyer → reject.)

---

## 18. COMPANY-ANALYSES VOL 1 — forensic deep-dive library (my second pattern-match reference)

> These 11 cases are *forensic* deep-dives (heavier on accounting/governance than §17). Use them when a company looks clean on the
> numbers but you suspect something — match it to a card, then run the **forensic red-flag catalog (§18c)** like a checklist.
> Recurring theme of the whole volume: **capital-intensive + low/volatile margin = debt trap** (the authors' touchstones are Amtek/Castex
> and Ahmednagar/Metalyst Forgings — debt rose ~33× chasing low-NFAT, low-profit growth). Avoid that shape.

### 18a. Quick archetype map (Vol 1)

| Archetype | Cases | Default verdict |
|-----------|-------|-----------------|
| **Debt-trap / liquidity crisis + governance breakdown** | Omkar Speciality | REJECT (veto) |
| **Quality business, commodity-cyclical, fairly/over-priced** | MRF (P/E 17), Divi's* (17–18) | MoS-in-business but watch input cycle / integrity; not cheap |
| **Great business + great management, far too expensive** | Caplin (54), Wonderla (56) | PASS on price |
| **Capital-intensive commodity, negative SSGR, debt + governance** | Nandan Denim (11) | AVOID despite low P/E |
| **Commodity, no pricing power, high-NFAT = low barriers** | Nile (7.2), Bhageria (12), Ishan (11) | low-P/E value traps; avoid/monitor |
| **Margin windfall from foreign-govt policy + governance** | AksharChem (10) | fragile; avoid |
| **Squeezed-both-ends auto-ancillary + governance** | Machino (43) | AVOID |
*Divi's: strong business but USFDA data-falsification + parallel competing promoter business = integrity overhang.

### 18b. The 11 deep-dive cards

**1. Omkar Speciality Chemicals — debt-trap + governance collapse. REJECT (veto).**
Sales 30–35% CAGR, OPM 19–20% (cost-plus spot pricing → pass-through but no customer lock-in); NPM 10%→7% (interest ₹8→20cr). **SSGR 10–15% << growth 25–30% → FCF −₹181cr** (capex ₹356cr vs CFO ₹175cr); debt ₹11→228cr. Funding desperation: IPO at **14% cost**, QIP/PE refused, warrants, NBFC loan-against-shares at **18–19%**, promoter stake-sale 58%→41%, heavy pledge. CRISIL **3-notch cut BBB+→BB+ (junk)** → switched to Brickwork (rating-shopping). Red flags: missed commitments ×3; opaque shareholding; volumetric 5,400 vs rated 2,315 TPA; physical inconsistency (product sales up, raw-material consumption down; freight down while sales up); demerger asset transfer at fair<book (₹63cr loss); promoter chasing a brokerage mid-crisis; delayed statutory dues. *Lesson: the textbook anatomy of capex-without-a-financing-plan → debt trap + every governance tell.*

**2. MRF — quality but commodity-cyclical (P/E 17). MoS-in-business, no price MoS.**
Use consolidated (standalone hid ₹400cr debt); normalize the 18-month FY2016 (×2/3). Sales ~15% CAGR (volume-backed); **OPM 8–21% tracks rubber/crude → no pricing power** (margin up only on cheap inputs; marketing → volume not pricing). SSGR 15–20% ≈ growth; FCF +₹1,897cr; value ₹3.89/₹1; upgraded to AAA; land+cash for expansion. Flags: in-house RTA; AR indebtedness table doesn't tally; ₹240cr RP purchases; Thiruvottiyur wage dispute; promoter stake low 27.5% but rising. *Lesson: don't mistake input-cost margin expansion for a moat; split the decade into sub-cycles (2007–11 capex>CFO→debt).*

**3. Wonderla Holidays — good business, capital-intensive, too expensive (P/E 56). PASS on price.**
Sales 20–25%; **OPM >40% (highest among peers — a real edge) but falling 51%→41%→~20%**; cash/advance collection (receivables ₹1cr) → cCFO ₹372cr > cPAT ₹263cr. **NFAT <1** (each new park ₹250–300cr for ~₹120cr/yr revenue) → must keep high OPM or fall into debt. Insulated local-monopoly business → problems are self-inflicted (mispriced Hyderabad/ Bangalore). Modeled the Chennai-park funding gap (declining OPM widens it). IPO cost 6.25%. *Lesson: NFAT<1 survives only on high margin + cash collection; model project financial-closure gaps.*

**4. Divi's Laboratories — strong business, integrity overhang (P/E 17–18).**
Sales 18–20%; **OPM 37–40% >> peers 20–25%** (NPM > peers' OPM — investigate, don't celebrate); SSGR 40–43%, FCF ₹2,754cr, value ₹4/₹1, near-debt-free. WC days > peers (cPAT ₹5,592cr > cCFO ₹4,711cr). **Red flags: promoters run a parallel competing pharma** ("Divi's Pharmaceuticals Pvt Ltd" — Zauba shows same promoters) under USFDA scrutiny while drawing ₹45cr/₹23cr salaries; **USFDA "data falsification" observations** = integrity question. *Lesson: abnormal margins + parallel promoter business + regulatory data-integrity = dig deep before trusting.*

**5. Caplin Point — great business + exemplary management, too expensive (P/E 54). PASS on price.**
Sales 25–30%; **OPM 4%→32%, NPM 2%→24%** (company-specific: direct-to-retail, product mix); near-debt-free; **negative working capital** (customer advances ₹57cr + supplier credit fund operations) → grows *above* SSGR 26–28% debt-free because cCFO ₹242cr > cPAT ₹149cr; receivables 69→18d; turned risky LatAm/Africa markets into advance-payment advantage. **Management = the gold standard:** founder takes **zero salary**, Harvard-MBA son paid nominal ₹1.5L/mo. Watch: 95% short-treatment-duration drugs (need constant marketing); undisclosed HK subsidiary. *Lesson: negative-WC + zero-salary founder = elite; price is the only thing wrong.*

**6. Nandan Denim — capital-intensive commodity, negative SSGR, governance (P/E 11). AVOID.**
Sales 18–20% (price+volume); OPM 13%→17% from *cheap cotton + backward integration, not pricing power* (only ~10% value-add, can't pass cotton hikes). **Negative SSGR −3–4% → debt ₹201→530cr** + equity dilution (warrants); plants at 84–85% (no operating leverage left). Flags: warrants issued *above* market (₹200 vs ₹100–160); auditor "debtors subject to confirmation"; CMLTD hidden; corporate guarantees + investment in related Vraj; **chairman's other co Nova Petrochemicals had a SEBI case** (bogus expansion announcement; quarterly profits summed to profit but audited annual = loss); group books-violation/bogus-degree FIRs; AR error. *Lesson: low P/E ≠ cheap when SSGR is negative and the promoter group has a fraud trail.*

**7. Nile Limited — commodity, single-customer, high-NFAT = low barriers (P/E 7.2). AVOID/monitor.**
Sales 16–20%; **OPM 4–9% (even losses) tracks lead price** despite LME "price benchmarking" — because the premium is %-only with no fixed-INR floor. **NFAT 10–16 = low capital intensity → commodity competition** (China makes 50% of lead). 80% revenue from one customer (Amara Raja); competitor Gravita set up 70km away. Low receivables partly via **bill discounting** (in contingent liabilities, not pure collection strength). Flags: salary at exact statutory ceiling; **interest-bearing deposits from related parties at 10–12% vs bank 8.85%** (reverse-RPT); failed Georgia JV write-off. *Lesson: benchmarking ≠ pricing power; high NFAT can mean a commoditized, low-barrier business.*

**8. Bhageria Industries — commodity dyes + diworsification + equity speculation (P/E 12). AVOID.**
Sales 20% but turbulent (declines FY10, FY16); OPM volatile 6–17% (losses FY08–09); NFAT >10 (to 62 — trading + low capital intensity); wildly swinging ITR (can't gauge demand). Flags: **company runs a ₹33cr stock-trading book** (35 stocks > ₹27cr operating assets, booking short-term gains); unrelated **solar** entry (₹170cr debt-funded vs ₹110cr net worth) on a **25-yr PPA at ₹4.41 vs market ₹2.44 → renegotiation risk**; merging promoter co Nipur Chemicals via all-share deal (compute what it's paying: P/E 18–30, P/B 4.5–5). *Lesson: a manufacturer speculating in equities + chasing above-market long contracts = capital-allocation red flags.*

**9. Ishan Dyes & Chemicals — small commodity chemical, data-quality issues (P/E 11). monitor.**
Sales 16% (turbulent); OPM volatile 4–17% (no pricing power); **high NFAT ~5–9 = low barriers**; SSGR 20% > growth 16%, FCF +₹23cr, reduced debt, first dividend. Flags: **CFO statement ignored working-capital changes; CFF omitted a ₹4cr debt inflow**; **₹3cr (75% of PAT) to undisclosed "Others"**; AR copy-paste; **low promoter stake 24.6% but ~28% held by "Patel" friends/family** (confirmed when a "public" holder gifted shares to a promoter). *Lesson: reconstruct missing data; cross-check the cash-flow statement; low reported stake can be benign.*

**10. AksharChem (India) — policy-driven margin windfall + governance (P/E 10). fragile; avoid.**
Vinyl Sulphone loss-making for years → suddenly profitable only because **China's environmental crackdown** removed competition (reverses if policy reverses); pigment proxy (Asahi Songwon) ~15–16% OPM. Merger added capital-intensive CPC Green → NFAT heading to ~2. Flags: junk/delisted quoted-share holdings; subsidiaries bought & sold in quick succession; **remuneration above statutory limit → clawback**; preferential shares to promoters at ₹18.50 vs ₹25.55 (possibly suppressed price); improper consolidation; **brother-vs-brother rivalry risk** (AksharChem entering Asahi's CPC Blue). *Lesson: a margin gift from a foreign government is not a moat; estimate normalized segment economics via a pure-play proxy.*

**11. Machino Plastics — squeezed-both-ends auto-ancillary + governance (P/E 43). AVOID.**
Sales 7–10%; OPM/NPM wild (losses FY12–14, OEM pricing pressure); **cCFO ₹153cr >> cPAT ₹23cr is a depreciation artifact (₹115cr), not strength**; receivables spiked ₹11→32cr in H1 → ₹21cr capex forced onto debt (₹34→66cr). **Squeezed from both ends by related-party shareholders:** customer Maruti/Suzuki block cost pass-through *to* it; supplier Machino Polymers (promoter) passes all cost rises *onto* it. Flags: BSE fine (no woman director); disputed ₹1.25cr investment in Caparo Maruti (investee denies it); **submits financial projections to exchanges**; remuneration above ceiling (auditor qualification). *Lesson: customer-as-shareholder isn't a positive; check RP contracts on BOTH supply and sale sides; decompose CFO.*

### 18c. Forensic red-flag catalog (run as a checklist on any suspicious company)

**Accounting / cash quality**
1. cCFO < cPAT over 10 yrs → profits stuck/unreal. But also: cCFO *artificially high* from rising payables or heavy depreciation — decompose.
2. Receivables ageing: % >6 months, write-offs, "subject to confirmation" by auditor, standalone>>consolidated (subs not remitting).
3. Physical input-consumption vs output-sales mismatch; cost lines that move the wrong way (freight down while sales up).
4. Cash-flow statement inconsistent with balance-sheet changes (CFO ignores WC; CFF omits a known debt draw).
5. Hidden debt: CMLTD inside "other current liabilities"; subsidiary debt missed by using standalone.
6. High cash alongside high/rising debt (treasury arbitrage or fictitious cash).
7. Tax charge in P&L not paid as cash tax; very low tax from incentives (normalize NPM to ~30%).
8. Non-operating income (forex/interest/one-offs) inflating NPM.

**Business quality**
9. OPM tracks raw-material price → commodity, no pricing power.
10. NFAT too high (>5) = low barriers/trading; NFAT <1 = capital guzzler. Want moderate-stable with pricing power.
11. Low NPM + low NFAT = capital-intensive debt trap (Amtek/Ahmednagar shape).
12. Margin windfall from a government policy (domestic or foreign) — fragile.
13. "Benchmarked"/cost-plus contracts without a fixed-INR floor still leave margin exposure.
14. Single-customer concentration; competitor near the key customer.
15. Above-market long-term contracts (PPA/LNG) — assume renegotiation.
16. Capacity near utilization ceiling → next growth needs fresh debt-funded capex; distrust headline (volumetric) capacity.
17. Value-added edge that competitors copy in months (no durable differentiation).

**Capital structure / growth funding**
18. SSGR << sales growth → debt/equity dependence (unless negative-WC and cCFO>cPAT).
19. Negative FCF over 10 yrs; dividends funded by debt.
20. Fundraising desperation: high issue cost %, NBFC loan-against-shares at high rates, repeated equity dilution, heavy promoter pledge.
21. Credit-rating *downgrade* (esp. to junk, multi-notch) or **rating-agency shopping** after a downgrade; rating withdrawn for "lack of information."

**Management / governance**
22. Self-dealing RPT: loans/deposits/purchases/leases/commissions with promoter entities; reverse-RPT (company pays related parties above market).
23. Squeezed both ends by related-party customer and supplier.
24. "Independent" directors who sit on promoters' private companies (MCA/Zauba); long-time-employee "independent" directors.
25. Promoter running a parallel/competing business or chasing unrelated ventures (esp. during stress).
26. Warrants below market (promoter gift / backdoor stake) or above market (parking); prefer preferential equity over warrants.
27. Demerger/asset transfer at fair<book value; serial subsidiary buy/sell; serial acquisitions.
28. Remuneration above statutory ceiling (qualification/clawback) or at the exact ceiling; pay unlinked to contribution.
29. Promoter group's other companies have SEBI/fraud/books-violation history; quarterly profits that sum to a profit but audited annual = loss.
30. Regulated-industry data-integrity findings (e.g. USFDA falsification) = integrity veto.
31. Manager repeatedly misses stated commitments; declares public financial projections/targets.
32. Non-core capital misallocation: stock-trading book, junk/delisted holdings, unrelated diworsification.
33. Statutory non-compliance (woman director, company secretary, N&R committee, in-house RTA) + AR sloppiness (arithmetic that doesn't tally, copy-paste, factual howlers).
34. Pledged promoter shares; opaque shareholding disclosure; falling promoter stake.

**Positives to credit (rare, high value)**
35. Founder zero/nominal salary; successors paid modestly/by contribution; negative working capital; honest "we got it wrong" disclosures; pure-play focus; on-time organic project execution; improving credit-rating trend.

### 18d. Verdict reminders reinforced by Vol 1
- **Low P/E is not cheap if the business is capital-intensive + commodity + negative-SSGR** (Nandan 11, Nile 7.2, Bhageria 12, Meghmani-style). Most Vol 1 "cheap" names are value traps.
- **Great business at P/E 40–56 is still a PASS** (Caplin 54, Wonderla 56, Machino 43, Amara Raja 40). Price gate is independent of quality.
- **Management/integrity is the veto** — Omkar and the Divi's overhang show even strong numbers don't survive governance failure.
- When a company "looks too good" (Divi's margins, Caplin/Omkar growth), the work is to find *why*, and whether it's durable, real, and shareholder-aligned.
