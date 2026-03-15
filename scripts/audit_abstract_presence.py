#!/usr/bin/env python3
"""Audit papers listed as "without abstracts" in mind_uploading_papers.md.

The script checks three layers:
1. Publisher / DOI landing page HTML
2. Crossref metadata
3. OpenAlex metadata

It writes a CSV and a Markdown summary under automation/.
"""

from __future__ import annotations

import csv
import datetime as dt
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "mind_uploading_papers.md"
OUTPUT_DIR = ROOT / "automation"
TODAY = dt.date.today().isoformat()
CSV_PATH = OUTPUT_DIR / f"abstract_presence_audit_{TODAY}.csv"
MD_PATH = OUTPUT_DIR / f"abstract_presence_audit_{TODAY}.md"
USER_AGENT = (
    "mind-upload-abstract-audit/1.0 "
    "(https://github.com/yasufumi-nakata/mind-upload)"
)

ABSTRACT_HEADINGS = {
    "abstract",
    "summary",
    "resumo",
    "résumé",
    "resume",
    "zusammenfassung",
    "摘要",
    "要旨",
}
META_PATTERNS = {
    "citation_abstract": re.compile(
        r'<meta[^>]+name=["\']citation_abstract["\'][^>]+content=["\'](.*?)["\']',
        re.I | re.S,
    ),
    "dc_description": re.compile(
        r'<meta[^>]+name=["\']dc\.description["\'][^>]+content=["\'](.*?)["\']',
        re.I | re.S,
    ),
    "og_description": re.compile(
        r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\'](.*?)["\']',
        re.I | re.S,
    ),
    "twitter_description": re.compile(
        r'<meta[^>]+name=["\']twitter:description["\'][^>]+content=["\'](.*?)["\']',
        re.I | re.S,
    ),
    "description": re.compile(
        r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
        re.I | re.S,
    ),
}
SECTION_PATTERNS = {
    "section_abstract": re.compile(
        r'<section[^>]+data-title=["\'](?:Abstract|Summary|Resumo|Résumé|'
        r'Zusammenfassung|摘要|要旨)["\'][^>]*>(.*?)</section>',
        re.I | re.S,
    ),
    "abs_content": re.compile(r'id=["\']Abs\d+-content["\'][^>]*>(.*?)</div>', re.I | re.S),
    "class_abstract": re.compile(
        r'<(?:section|div|article|p)[^>]+class=["\'][^"\']*abstract[^"\']*["\'][^>]*>'
        r"(.*?)</(?:section|div|article|p)>",
        re.I | re.S,
    ),
}
GENERIC_REJECT_PATTERNS = [
    re.compile(r"we use cookies", re.I),
    re.compile(r"access through your institution", re.I),
    re.compile(r"buy now", re.I),
    re.compile(r"rights and permissions", re.I),
    re.compile(r"this browser is no longer supported", re.I),
]


@dataclass
class Paper:
    index: int
    title: str
    date: str
    year: str
    doi: str
    scopus_url: str


def normalize_space(text: str) -> str:
    return " ".join(text.split()).strip()


def strip_tags(raw: str) -> str:
    text = re.sub(r"<script\b.*?</script>", " ", raw, flags=re.I | re.S)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    return normalize_space(html.unescape(text))


def norm_title(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html.unescape(text))
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text).lower()
    return normalize_space(text)


def similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()


def fetch_text(url: str) -> tuple[str, str, int]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        final_url = response.geturl()
        status = getattr(response, "status", 200)
        charset = response.headers.get_content_charset() or "utf-8"
        body = response.read().decode(charset, errors="replace")
    return final_url, body, status


def canonicalize_url(url: str) -> str:
    if not url:
        return ""
    split = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit((split.scheme, split.netloc, split.path, "", ""))


def fetch_json(url: str) -> dict | list | None:
    try:
        _, body, _ = fetch_text(url)
        return json.loads(body)
    except Exception:
        return None


def word_count(text: str) -> int:
    return len(text.split())


def is_generic(text: str) -> bool:
    lowered = text.lower()
    return any(pattern.search(lowered) for pattern in GENERIC_REJECT_PATTERNS)


def is_keywords_only(text: str) -> bool:
    lowered = text.lower()
    if lowered.startswith("keywords:") or lowered.startswith("keywords "):
        return True
    if word_count(text) < 18 and lowered.count(",") >= 4:
        return True
    return False


def clean_candidate(text: str) -> str:
    text = strip_tags(text)
    text = text.replace("\u00a0", " ")
    return normalize_space(text)


def best_html_evidence(html_text: str) -> tuple[str, str]:
    candidates: list[tuple[str, str]] = []
    for label, pattern in SECTION_PATTERNS.items():
        for match in pattern.finditer(html_text):
            cleaned = clean_candidate(match.group(1))
            if word_count(cleaned) >= 18 and not is_generic(cleaned):
                candidates.append((label, cleaned))
                break
    for label, pattern in META_PATTERNS.items():
        match = pattern.search(html_text)
        if match:
            cleaned = clean_candidate(match.group(1))
            if word_count(cleaned) >= 18 and not is_generic(cleaned):
                candidates.append((label, cleaned))
    candidates.sort(key=lambda item: (item[0].startswith("section"), word_count(item[1])), reverse=True)
    return candidates[0] if candidates else ("", "")


def crossref_by_doi(doi: str) -> dict | None:
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi, safe='')}"
    payload = fetch_json(url)
    if not payload or not isinstance(payload, dict):
        return None
    return payload.get("message")


def openalex_by_doi(doi: str) -> dict | None:
    encoded = urllib.parse.quote(f"https://doi.org/{doi}", safe="")
    payload = fetch_json(f"https://api.openalex.org/works/{encoded}")
    if not payload or not isinstance(payload, dict):
        return None
    return payload


def search_crossref(title: str) -> dict | None:
    query = urllib.parse.quote(title)
    payload = fetch_json(f"https://api.crossref.org/works?query.title={query}&rows=5")
    if not payload or not isinstance(payload, dict):
        return None
    items = payload.get("message", {}).get("items", [])
    best = None
    best_score = -1.0
    for item in items:
        candidate_title = (item.get("title") or [""])[0]
        score = similarity(title, candidate_title)
        if score > best_score:
            best = item
            best_score = score
    if best is not None:
        best["_title_score"] = best_score
    return best


def search_openalex(title: str) -> dict | None:
    query = urllib.parse.quote(title)
    payload = fetch_json(f"https://api.openalex.org/works?search={query}&per-page=5")
    if not payload or not isinstance(payload, dict):
        return None
    results = payload.get("results", [])
    best = None
    best_score = -1.0
    for item in results:
        candidate_title = item.get("display_name", "")
        score = similarity(title, candidate_title)
        if score > best_score:
            best = item
            best_score = score
    if best is not None:
        best["_title_score"] = best_score
    return best


def reconstruct_openalex_abstract(item: dict | None) -> str:
    if not item:
        return ""
    abstract_index = item.get("abstract_inverted_index") or {}
    if not abstract_index:
        return ""
    max_pos = max(max(positions) for positions in abstract_index.values())
    words = [""] * (max_pos + 1)
    for token, positions in abstract_index.items():
        for position in positions:
            words[position] = token
    return normalize_space(" ".join(words))


def crossref_abstract_text(item: dict | None) -> str:
    if not item:
        return ""
    abstract = item.get("abstract", "")
    return clean_candidate(abstract)


def parse_cards() -> list[Paper]:
    text = SOURCE_FILE.read_text(encoding="utf-8")
    start = text.index('<h2 id="without-abstracts"')
    section = text[start:]
    cards = section.split('<div class="paper-card">')[1:]
    papers: list[Paper] = []
    for index, card in enumerate(cards, start=1):
        title_match = re.search(r"<h3>(.*?)</h3>", card, re.S)
        date_match = re.search(r"</svg>\s*([0-9]{4}-[0-9]{2}-[0-9]{2})</div>", card)
        doi_match = re.search(
            r'DOI:\s*(?:<a href="https://doi.org/([^"]+)"[^>]*>[^<]+</a>|N/A)',
            card,
            re.I,
        )
        scopus_match = re.search(
            r'<a href="([^"]+)"\s*target="_blank" class="btn-action">View Full Access',
            card,
            re.I,
        )
        title = normalize_space(strip_tags(title_match.group(1) if title_match else ""))
        date = date_match.group(1) if date_match else ""
        doi = doi_match.group(1) if doi_match and doi_match.group(1) else ""
        scopus_url = scopus_match.group(1) if scopus_match else ""
        papers.append(Paper(index=index, title=title, date=date, year=date[:4], doi=doi, scopus_url=scopus_url))
    return papers


def classify(paper: Paper) -> dict[str, str]:
    row = {
        "index": str(paper.index),
        "title": paper.title,
        "listed_date": paper.date,
        "listed_doi": paper.doi or "",
        "resolved_doi": "",
        "publisher_url": "",
        "crossref_type": "",
        "openalex_type": "",
        "crossref_title_score": "",
        "openalex_title_score": "",
        "html_evidence_kind": "",
        "html_evidence_excerpt": "",
        "crossref_abstract_excerpt": "",
        "openalex_abstract_excerpt": "",
        "final_status": "",
        "confidence": "",
        "notes": "",
    }

    resolved_doi = paper.doi
    crossref_item = crossref_by_doi(resolved_doi) if resolved_doi else None
    openalex_item = openalex_by_doi(resolved_doi) if resolved_doi else None

    if not resolved_doi:
        crossref_guess = search_crossref(paper.title)
        if crossref_guess and crossref_guess.get("_title_score", 0.0) >= 0.86:
            resolved_doi = crossref_guess.get("DOI", "")
            crossref_item = crossref_guess
            row["notes"] = "DOI was recovered from Crossref title search."
        openalex_guess = search_openalex(paper.title)
        if openalex_guess:
            row["openalex_title_score"] = f"{openalex_guess.get('_title_score', 0.0):.2f}"
        if not crossref_item and openalex_guess and openalex_guess.get("_title_score", 0.0) >= 0.90:
            doi_url = openalex_guess.get("doi") or ""
            if doi_url.startswith("https://doi.org/"):
                resolved_doi = doi_url.removeprefix("https://doi.org/")
                openalex_item = openalex_guess
                row["notes"] = (row["notes"] + " " if row["notes"] else "") + "DOI was recovered from OpenAlex title search."
    elif crossref_item is None:
        crossref_guess = search_crossref(paper.title)
        if crossref_guess and crossref_guess.get("_title_score", 0.0) >= 0.86:
            crossref_item = crossref_guess

    if not openalex_item and resolved_doi:
        openalex_item = openalex_by_doi(resolved_doi)
    if not openalex_item:
        guess = search_openalex(paper.title)
        if guess and guess.get("_title_score", 0.0) >= 0.90:
            openalex_item = guess
            if not row["openalex_title_score"]:
                row["openalex_title_score"] = f"{guess.get('_title_score', 0.0):.2f}"
    if crossref_item and not row["crossref_title_score"]:
        score = crossref_item.get("_title_score")
        if score is not None:
            row["crossref_title_score"] = f"{score:.2f}"

    row["resolved_doi"] = resolved_doi or ""
    if crossref_item:
        row["crossref_type"] = crossref_item.get("type", "")
    if openalex_item:
        row["openalex_type"] = openalex_item.get("type", "")

    html_kind = ""
    html_excerpt = ""
    publisher_url = ""
    if resolved_doi:
        try:
            publisher_url, html_text, _ = fetch_text(f"https://doi.org/{resolved_doi}")
            html_kind, html_excerpt = best_html_evidence(html_text)
            row["publisher_url"] = canonicalize_url(publisher_url)
        except Exception as exc:
            row["notes"] = (row["notes"] + " " if row["notes"] else "") + f"Publisher fetch failed: {exc.__class__.__name__}."

    crossref_excerpt = crossref_abstract_text(crossref_item)
    openalex_excerpt = reconstruct_openalex_abstract(openalex_item)
    if is_keywords_only(openalex_excerpt):
        openalex_excerpt = ""

    row["html_evidence_kind"] = html_kind
    row["html_evidence_excerpt"] = html_excerpt[:320]
    row["crossref_abstract_excerpt"] = crossref_excerpt[:320]
    row["openalex_abstract_excerpt"] = openalex_excerpt[:320]

    explicit_html = html_kind in {"section_abstract", "abs_content", "class_abstract", "citation_abstract"}
    metadata_html = html_kind in {"dc_description", "og_description", "twitter_description", "description"}
    has_crossref_abstract = bool(crossref_excerpt) and not is_keywords_only(crossref_excerpt)
    has_openalex_abstract = bool(openalex_excerpt)

    if explicit_html or has_crossref_abstract:
        row["final_status"] = "abstract_present"
        row["confidence"] = "high"
    elif metadata_html or has_openalex_abstract:
        row["final_status"] = "abstract_like_metadata_present"
        row["confidence"] = "medium"
    else:
        row["final_status"] = "no_abstract_found"
        row["confidence"] = "medium" if resolved_doi else "low"

    if not resolved_doi:
        row["confidence"] = "low"
        if row["final_status"] == "no_abstract_found":
            row["notes"] = (row["notes"] + " " if row["notes"] else "") + "No DOI could be resolved automatically."

    return row


def write_csv(rows: Iterable[dict[str, str]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    rows = list(rows)
    if not rows:
        return
    with CSV_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(rows: list[dict[str, str]]) -> None:
    total = len(rows)
    present = [row for row in rows if row["final_status"] == "abstract_present"]
    metadata_only = [row for row in rows if row["final_status"] == "abstract_like_metadata_present"]
    absent = [row for row in rows if row["final_status"] == "no_abstract_found"]

    lines = [
        f"# Abstract Presence Audit ({TODAY})",
        "",
        f"- 対象: `mind_uploading_papers.md` の「2. アブストラクトなし」にある `{total}` 件",
        "- 判定層: DOI / 出版社ページ HTML, Crossref, OpenAlex",
        f"- abstract が確認できた: `{len(present)}` 件",
        f"- メタデータ上の要旨相当あり: `{len(metadata_only)}` 件",
        f"- 現時点で確認できず: `{len(absent)}` 件",
        f"- 詳細 CSV: `{CSV_PATH.relative_to(ROOT)}`",
        "",
        "## abstract が確認できた",
        "",
    ]
    if present:
        for row in present:
            source = row["publisher_url"] or (f"https://doi.org/{row['resolved_doi']}" if row["resolved_doi"] else row["title"])
            lines.append(f"- {row['index']}. {row['title']} [{row['html_evidence_kind'] or 'crossref'}] {source}")
    else:
        lines.append("- 該当なし")

    lines.extend(
        [
            "",
            "## メタデータ上の要旨相当あり",
            "",
        ]
    )
    if metadata_only:
        for row in metadata_only:
            source = row["publisher_url"] or (f"https://doi.org/{row['resolved_doi']}" if row["resolved_doi"] else row["title"])
            lines.append(f"- {row['index']}. {row['title']} [{row['html_evidence_kind'] or 'openalex'}] {source}")
    else:
        lines.append("- 該当なし")

    lines.extend(
        [
            "",
            "## 現時点で確認できず",
            "",
        ]
    )
    if absent:
        for row in absent:
            note = f" ({row['notes']})" if row["notes"] else ""
            lines.append(f"- {row['index']}. {row['title']}{note}")
    else:
        lines.append("- 該当なし")

    MD_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    papers = parse_cards()
    rows: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        future_map = {executor.submit(classify, paper): paper for paper in papers}
        for future in as_completed(future_map):
            paper = future_map[future]
            try:
                rows.append(future.result())
            except Exception as exc:
                rows.append(
                    {
                        "index": str(paper.index),
                        "title": paper.title,
                        "listed_date": paper.date,
                        "listed_doi": paper.doi or "",
                        "resolved_doi": "",
                        "publisher_url": "",
                        "crossref_type": "",
                        "openalex_type": "",
                        "crossref_title_score": "",
                        "openalex_title_score": "",
                        "html_evidence_kind": "",
                        "html_evidence_excerpt": "",
                        "crossref_abstract_excerpt": "",
                        "openalex_abstract_excerpt": "",
                        "final_status": "error",
                        "confidence": "low",
                        "notes": f"{exc.__class__.__name__}: {exc}",
                    }
                )
            time.sleep(0.05)

    rows.sort(key=lambda row: int(row["index"]))
    write_csv(rows)
    write_markdown(rows)

    total = len(rows)
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["final_status"]] = counts.get(row["final_status"], 0) + 1
    print(f"Wrote {CSV_PATH.relative_to(ROOT)} and {MD_PATH.relative_to(ROOT)}")
    print(f"Total: {total}")
    for key in sorted(counts):
        print(f"{key}: {counts[key]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
