#!/usr/bin/env python3
"""
Run a screener.in query-language screen (authenticated, so any query works —
not just publicly-shared ones) and restrict the results to the constituents
of an NSE index (Nifty 50, Nifty Next 50, Nifty 500, ...).

Requires: requests, beautifulsoup4 (pip install beautifulsoup4 requests)
Credentials: read from SCREENER_USER / SCREENER_PASS env vars. Never pass
a password as a bare CLI arg (it would leak into shell history / ps output).

Example:
    export SCREENER_USER='you@example.com'
    export SCREENER_PASS='your-password'
    python3 screen_by_index.py --query "Dividend yield > 2" --index nifty50 --sort "Div Yld%"
"""
import argparse
import csv
import io
import os
import re
import sys
import tempfile

import requests
from bs4 import BeautifulSoup

SCREENER_BASE = "https://www.screener.in"

# Known niftyindices.com constituent-list filenames. If the index you want
# isn't here, pass --index-url directly — niftyindices.com/IndexConstituent/
# hosts a CSV for essentially every NSE index following the same naming
# pattern (ind_nifty<name>list.csv); check the site if a guess 404s.
KNOWN_INDEXES = {
    "nifty50": "ind_nifty50list.csv",
    "niftynext50": "ind_niftynext50list.csv",
    "nifty100": "ind_nifty100list.csv",
    "nifty200": "ind_nifty200list.csv",
    "nifty500": "ind_nifty500list.csv",
    "niftymidcap50": "ind_niftymidcap50list.csv",
    "niftymidcap150": "ind_niftymidcap150list.csv",
    "niftysmallcap50": "ind_niftysmallcap50list.csv",
    "niftysmallcap250": "ind_niftysmallcap250list.csv",
    "niftybank": "ind_niftybanklist.csv",
    "niftyit": "ind_niftyitlist.csv",
    "niftyfmcg": "ind_niftyfmcglist.csv",
    "niftypharma": "ind_niftypharmalist.csv",
    "niftyauto": "ind_niftyautolist.csv",
}


def login(session: requests.Session, user: str, password: str) -> None:
    r = session.get(f"{SCREENER_BASE}/login/")
    m = re.search(r'csrfmiddlewaretoken[^>]*value="([^"]*)"', r.text)
    if not m:
        raise RuntimeError("Could not find csrfmiddlewaretoken on login page — screener.in's login form may have changed.")
    csrf = m.group(1)

    r = session.post(
        f"{SCREENER_BASE}/login/",
        data={
            "csrfmiddlewaretoken": csrf,
            "username": user,
            "password": password,
            "next": "",
        },
        headers={
            "Referer": f"{SCREENER_BASE}/login/",
            "Origin": SCREENER_BASE,
        },
        allow_redirects=False,
    )
    if r.status_code != 302 or "/dash/" not in r.headers.get("Location", ""):
        if "errorlist" in r.text:
            raise RuntimeError("screener.in rejected the credentials (errorlist in response).")
        raise RuntimeError(f"Unexpected login response: status={r.status_code}, location={r.headers.get('Location')}")


def fetch_all_pages(session: requests.Session, query: str) -> list[str]:
    """Return raw HTML for every results page of the query."""
    pages = []
    r = session.get(f"{SCREENER_BASE}/screen/raw/", params={"query": query, "sort": "", "order": ""})
    r.raise_for_status()
    pages.append(r.text)

    m = re.search(r"Showing page \d+ of (\d+)", r.text)
    total_pages = int(m.group(1)) if m else 1

    for p in range(2, total_pages + 1):
        r = session.get(f"{SCREENER_BASE}/screen/raw/", params={"query": query, "sort": "", "order": "", "page": p})
        r.raise_for_status()
        pages.append(r.text)

    return pages


def parse_pages(pages: list[str]) -> tuple[list[str], list[dict]]:
    """Parse every results page. Returns (column_names, rows) where each row
    is a dict of {column_name: text_value} plus a 'ticker' key.

    Header names come from the table's own <th> row (not hardcoded) so this
    keeps working if screener changes/reorders default display columns.
    """
    headers: list[str] | None = None
    rows: list[dict] = []
    seen_tickers: set[str] = set()

    for html in pages:
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table")
        if table is None:
            continue
        for tr in table.find_all("tr"):
            th_cells = tr.find_all("th")
            if th_cells and headers is None:
                headers = [th.get_text(strip=True) for th in th_cells]
                continue
            if th_cells:
                continue  # repeated header row mid-table — skip

            td_cells = tr.find_all("td")
            if not td_cells:
                continue
            link = tr.find("a", href=True)
            if not link or "/company/" not in link["href"]:
                continue  # not a data row (e.g. a footer/pagination row)

            ticker = link["href"].strip("/").split("/")[-1]
            if ticker == "consolidated":
                ticker = link["href"].strip("/").split("/")[-2]
            if ticker in seen_tickers:
                continue
            seen_tickers.add(ticker)

            values = [td.get_text(strip=True) for td in td_cells]
            row = dict(zip(headers or [], values))
            row["ticker"] = ticker
            rows.append(row)

    return headers or [], rows


def fetch_index_symbols(index_key: str | None, index_url: str | None) -> dict[str, str]:
    """Returns {SYMBOL: Company Name} for the requested index."""
    if index_url is None:
        if index_key not in KNOWN_INDEXES:
            raise RuntimeError(
                f"Unknown index '{index_key}'. Known: {', '.join(sorted(KNOWN_INDEXES))}. "
                "For anything else, pass --index-url directly (niftyindices.com/IndexConstituent/ind_nifty<name>list.csv)."
            )
        index_url = f"https://niftyindices.com/IndexConstituent/{KNOWN_INDEXES[index_key]}"

    # A plain requests/curl call without a browser-like User-Agent can get
    # blocked or redirected by niftyindices.com — this UA is required, not optional.
    r = requests.get(index_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=30)
    r.raise_for_status()
    reader = csv.DictReader(io.StringIO(r.text))
    symbols = {}
    for row in reader:
        sym = (row.get("Symbol") or "").strip()
        name = (row.get("Company Name") or "").strip()
        if sym:
            symbols[sym] = name
    if not symbols:
        raise RuntimeError(f"Fetched {index_url} but found no Symbol column — the CSV format may have changed.")
    return symbols


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--query", required=True, help='screener.in query language string, e.g. "Dividend yield > 2"')
    ap.add_argument("--index", default="nifty50", help=f"one of {', '.join(sorted(KNOWN_INDEXES))} (default: nifty50)")
    ap.add_argument("--index-url", default=None, help="override: direct niftyindices.com CSV URL for an index not in the known list")
    ap.add_argument("--sort", default=None, help="column name to sort by (must match a header from the results table, e.g. 'Div Yld%%')")
    ap.add_argument("--desc", action="store_true", default=True, help="sort descending (default)")
    ap.add_argument("--asc", dest="desc", action="store_false", help="sort ascending instead")
    ap.add_argument("--format", choices=["markdown", "csv"], default="markdown")
    args = ap.parse_args()

    user = os.environ.get("SCREENER_USER")
    password = os.environ.get("SCREENER_PASS")
    if not user or not password:
        print("ERROR: set SCREENER_USER and SCREENER_PASS environment variables before running.", file=sys.stderr)
        sys.exit(1)

    session = requests.Session()
    try:
        login(session, user, password)
        pages = fetch_all_pages(session, args.query)
        headers, rows = parse_pages(pages)

        index_symbols = fetch_index_symbols(args.index if args.index_url is None else None, args.index_url)
        matches = [row for row in rows if row["ticker"] in index_symbols]

        sort_col = args.sort
        if sort_col and sort_col in headers:
            def keyfn(row):
                raw = row.get(sort_col, "")
                cleaned = re.sub(r"[^0-9.\-]", "", raw)
                try:
                    return float(cleaned)
                except ValueError:
                    return float("-inf")
            matches.sort(key=keyfn, reverse=args.desc)

        print(f"# Universe screened: {len(rows)} companies matched query: {args.query}", file=sys.stderr)
        print(f"# Index constituents: {len(index_symbols)} ({args.index or args.index_url})", file=sys.stderr)
        print(f"# Matches in index: {len(matches)}", file=sys.stderr)

        out_headers = ["ticker"] + headers
        if args.format == "csv":
            writer = csv.writer(sys.stdout)
            writer.writerow(out_headers)
            for row in matches:
                writer.writerow([row.get(h, "") for h in out_headers])
        else:
            print("| " + " | ".join(out_headers) + " |")
            print("|" + "---|" * len(out_headers))
            for row in matches:
                print("| " + " | ".join(row.get(h, "") for h in out_headers) + " |")

    finally:
        try:
            session.get(f"{SCREENER_BASE}/logout/", timeout=10)
        except requests.RequestException:
            pass
        session.close()


if __name__ == "__main__":
    main()
