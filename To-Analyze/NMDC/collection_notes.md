# Collection notes — NMDC Ltd (NMDC)

- Run date: 2026-07-06
- screener_url: https://www.screener.in/company/NMDC/consolidated/
- consolidated_available: True
- collection_status: partial

## Counts
- Annual reports: found(fetched-target) 10, extracted-ok 10
- Credit ratings: found 6, extracted-ok 6
- Concalls (transcript/ppt PDFs): found 56, extracted-ok 49
- Material announcements downloaded-ok: 0

## Observations / gaps
- shareholding.csv holds top-level rows (Promoters/FIIs/DIIs/Public/#holders); promoter-PLEDGE % is a schedule sub-row that screener loads via an authenticated AJAX endpoint (/api/company/<id>/schedules/...) which returns 404 anonymously -> pledge NOT captured.
- peers.csv unavailable: /api/company/2287/peers/ returns 404 without a logged-in session.
- export.xlsx: skipped-no-login (no screener credentials supplied; CSV tables carry the same numbers).
- IPO doc listed in annual-reports block (not fetched here unless SME): DRHP -> https://www.sebi.gov.in/filings/public-issues/mar-2010/nmdc-limited_2399.html
- annual reports: 15 FYs listed; fetching newest 10 (contract target=last 10 FYs).
- concalls: 6 audio/video 'REC' links (YouTube / nmdc.co.in media) skipped (not text documents).
- concall naming: Concall_<YYYY-MM>_<kind>.pdf using screener's publish-month label; contract's <FYqQ> quarter mapping is ambiguous from publish month alone.
- announcements index.csv: 5 rows from screener 'Recent' feed. NOTE: full 24-month feed lives on BSE (https://www.bseindia.com/.../corp-announcements/); only the screener-listed recent items were captured this run (BSE full-feed scrape not implemented).
