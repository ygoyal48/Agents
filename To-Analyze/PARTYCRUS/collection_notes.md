# Collection notes — Party Cruisers Ltd (PARTYCRUS)

- Run date: 2026-07-06
- screener_url: https://www.screener.in/company/PARTYCRUS/consolidated/
- consolidated_available: True
- collection_status: partial

## Counts
- Annual reports: found(fetched-target) 5, extracted-ok 5
- Credit ratings: found 0, extracted-ok 0
- Concalls (transcript/ppt PDFs): found 2, extracted-ok 2
- Material announcements downloaded-ok: 1

## Observations / gaps
- shareholding.csv holds top-level rows (Promoters/FIIs/DIIs/Public/#holders); promoter-PLEDGE % is a schedule sub-row that screener loads via an authenticated AJAX endpoint (/api/company/<id>/schedules/...) which returns 404 anonymously -> pledge NOT captured.
- peers.csv unavailable: /api/company/1274838/peers/ returns 404 without a logged-in session.
- export.xlsx: skipped-no-login (no screener credentials supplied; CSV tables carry the same numbers).
- IPO doc listed in annual-reports block (not fetched here unless SME): DRHP -> https://www.sebi.gov.in/filings/public-issues/feb-2021/party-cruisers-limited_49192.html
- annual reports: 5 FYs listed; fetching newest 5 (contract target=last 10 FYs).
- annual report 'Annual Report FY2023' arrived as .zip; extracted inner PDF.
- annual report 'Annual Report FY2022' arrived as .zip; extracted inner PDF.
- annual report 'Annual Report FY2021' arrived as .zip; extracted inner PDF.
- concall naming: Concall_<YYYY-MM>_<kind>.pdf using screener's publish-month label; contract's <FYqQ> quarter mapping is ambiguous from publish month alone.
- announcements index.csv: 5 rows from screener 'Recent' feed. NOTE: full 24-month feed lives on BSE (https://www.bseindia.com/.../corp-announcements/); only the screener-listed recent items were captured this run (BSE full-feed scrape not implemented).
- IPO: 1 RHP/DRHP-type link(s) found and fetched into docs/ipo/.
