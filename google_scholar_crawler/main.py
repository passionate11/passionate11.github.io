"""Fetch Google Scholar stats via scrape.do and emit gs_data.json.

The previous implementation used `scholarly` with free proxies, which failed
often enough that the workflow was disabled. scrape.do fetches the profile
page from a clean IP; we parse the HTML ourselves.

Output schema is kept compatible with the old `scholarly` output so that
_includes/fetch_google_scholar_stats.html keeps working:
  - citedby: int
  - publications: {author_pub_id: {num_citations: int, ...}}
"""

import html
import json
import os
import re
import sys
import urllib.parse
from datetime import datetime, timezone

import requests

SCHOLAR_ID = os.environ["GOOGLE_SCHOLAR_ID"]
SCRAPEDO_TOKEN = os.environ["SCRAPEDO_TOKEN"]

PROFILE_URL = (
    "https://scholar.google.com/citations"
    f"?user={SCHOLAR_ID}&hl=en&cstart=0&pagesize=100"
)


def fetch_profile_html():
    endpoint = "https://api.scrape.do/"
    params = {"url": PROFILE_URL, "token": SCRAPEDO_TOKEN}
    resp = requests.get(endpoint, params=params, timeout=120)
    resp.raise_for_status()
    return resp.text


def parse_stats(page):
    """Return (citedby, citedby5y, hindex, hindex5y, i10index, i10index5y)."""
    values = re.findall(r'<td class="gsc_rsb_std">(\d+)</td>', page)
    if len(values) < 6:
        raise ValueError(
            f"expected 6 values in the stats table, found {len(values)}; "
            "Google Scholar markup may have changed"
        )
    return [int(v) for v in values[:6]]


def strip_tags(fragment):
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).strip()


def parse_publications(page):
    """Return {author_pub_id: publication dict} mirroring scholarly's shape."""
    rows = re.findall(r'<tr class="gsc_a_tr">(.*?)</tr>', page, re.S)
    if not rows:
        raise ValueError("no publication rows found; markup may have changed")

    publications = {}
    for row in rows:
        # `citation_for_view` is the stable id; the `data-cid` attribute is
        # only emitted on some rows.
        cid = re.search(r'citation_for_view=([^"&]+)', row)
        title = re.search(r'class="gsc_a_at"[^>]*>([^<]*)</a>', row)
        cites = re.search(r'class="gsc_a_ac[^"]*"[^>]*>(\d*)</a>', row)
        year = re.search(r'class="gsc_a_h[^"]*"[^>]*>(\d*)</span>', row)
        authors_pub = re.findall(r'class="gs_gray">(.*?)</div>', row, re.S)
        if not cid:
            continue

        pub_id = html.unescape(cid.group(1))
        publications[pub_id] = {
            "author_pub_id": pub_id,
            "num_citations": int(cites.group(1)) if cites and cites.group(1) else 0,
            "bib": {
                "title": html.unescape(title.group(1)) if title else "",
                "pub_year": year.group(1) if year and year.group(1) else "",
                "author": strip_tags(authors_pub[0]) if authors_pub else "",
                "citation": strip_tags(authors_pub[1]) if len(authors_pub) > 1 else "",
            },
            "citedby_url": (
                f"https://scholar.google.com/citations?view_op=view_citation"
                f"&hl=en&user={SCHOLAR_ID}&citation_for_view={pub_id}"
            ),
        }
    return publications


def parse_name(page):
    match = re.search(r'<div id="gsc_prf_in"[^>]*>([^<]*)</div>', page)
    return html.unescape(match.group(1)).strip() if match else ""


def main():
    page = fetch_profile_html()

    if "gsc_rsb_std" not in page:
        # Usually a CAPTCHA page or an error body returned with HTTP 200.
        raise ValueError(
            "response does not look like a Scholar profile page "
            f"(got {len(page)} bytes)"
        )

    citedby, citedby5y, hindex, hindex5y, i10index, i10index5y = parse_stats(page)
    publications = parse_publications(page)

    # Sanity check: the per-paper counts should add up to the headline number.
    # A mismatch means we parsed a partial page, so fail rather than publish
    # a number that is quietly too low.
    summed = sum(p["num_citations"] for p in publications.values())
    if summed != citedby:
        print(
            f"WARNING: per-paper citations sum to {summed} but the profile "
            f"reports {citedby}. This is expected only if you have more than "
            "100 publications.",
            file=sys.stderr,
        )

    if citedby <= 0:
        raise ValueError("parsed a citation count of 0; refusing to publish")

    author = {
        "scholar_id": SCHOLAR_ID,
        "name": parse_name(page),
        "citedby": citedby,
        "citedby5y": citedby5y,
        "hindex": hindex,
        "hindex5y": hindex5y,
        "i10index": i10index,
        "i10index5y": i10index5y,
        "publications": publications,
        "updated": str(datetime.now(timezone.utc)),
    }

    print(
        f"{author['name']}: {citedby} citations, h-index {hindex}, "
        f"{len(publications)} publications"
    )

    os.makedirs("results", exist_ok=True)
    with open("results/gs_data.json", "w") as outfile:
        json.dump(author, outfile, ensure_ascii=False)

    shieldio_data = {
        "schemaVersion": 1,
        "label": "citations",
        "message": str(citedby),
    }
    with open("results/gs_data_shieldsio.json", "w") as outfile:
        json.dump(shieldio_data, outfile, ensure_ascii=False)


if __name__ == "__main__":
    main()
