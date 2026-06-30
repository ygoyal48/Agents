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

**Verdict:** management is a **hard veto.** If integrity is in any doubt (fraud history, self-dealing RPT, warrant abuse, debt-funded dividends to self) → **REJECT**, even with flawless financials/valuation. "Investment in a great business is futile if management isn't shareholder-friendly." Never trust awards/ratings as proof of integrity.

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
