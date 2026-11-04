#!/usr/bin/env python3
"""Validate local navigation, citations, assets and bilingual page metadata."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.images, self.canon, self.langs = path, [], [], [], [], {}
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'a' and a.get('href'):
            self.links.append(a['href'])
        if tag == 'img':
            self.images.append(a)
        if tag in ('script', 'img') and a.get('src'):
            self.links.append(a['src'])
        if tag == 'link' and a.get('href'):
            self.links.append(a['href'])
            if a.get('rel') == 'canonical':
                self.canon.append(a['href'])
            if a.get('hreflang'):
                self.langs[a['hreflang']] = a['href']


def main():
    files = sorted(ROOT.glob('*.html')) + sorted((ROOT/'ja').glob('*.html'))
    docs = {p.resolve(): Document(p) for p in files}
    errors = []
    for path, d in docs.items():
        label = str(path.relative_to(ROOT))
        if len(d.ids) != len(set(d.ids)):
            errors.append(f'{label}: duplicate ids')
        if len(d.canon) != 1:
            errors.append(f'{label}: missing or duplicate canonical')
        if path.stem not in ('philosophy', 'scenario'):
            if set(d.langs) != {'en', 'ja', 'x-default'}:
                errors.append(f'{label}: language alternates missing')
            if '2026-11-04' not in path.read_text():
                errors.append(f'{label}: edition date missing')
        for a in d.images:
            if not a.get('alt', '').strip():
                errors.append(f'{label}: image without alt: {a.get("src")}')
        for href in d.links:
            u = urlsplit(href)
            if u.scheme or u.netloc:
                continue
            target = (ROOT/unquote(u.path).lstrip('/')) if u.path.startswith('/') else path.parent/unquote(u.path)
            if not u.path:
                target = path
            if target.is_dir():
                target /= 'index.html'
            target = target.resolve()
            if not target.exists():
                errors.append(f'{label}: missing local target {href}')
            elif u.fragment and target in docs and unquote(u.fragment) not in docs[target].ids:
                errors.append(f'{label}: broken fragment {href}')
        body = path.read_text()
        if re.search(r'\[\[[A-Z0-9]+\]\]|\{\{[a-z]+\}\}', body):
            errors.append(f'{label}: unresolved template')
        if any(x in body for x in ('/Users/', 'link_6a23', 'drive.google.com/drive/folders/')):
            errors.append(f'{label}: private collection detail leaked')
    for stem in ('index','science','progress','carboncopies','validation','future','action','history','resources'):
        en, ja = docs[ROOT/(stem+'.html')], docs[ROOT/'ja'/(stem+'.html')]
        if {x for x in en.ids if x.startswith('ref-')} != {x for x in ja.ids if x.startswith('ref-')}:
            errors.append(f'{stem}: EN/JA reference mismatch')
    refs = json.loads((ROOT/'assets/references.json').read_text())
    if len(refs) != len({r['id'] for r in refs}):
        errors.append('Duplicate bibliography identifiers')
    for r in refs:
        if not r.get('title') or not r.get('url'):
            errors.append(f'Incomplete citation: {r["id"]}')
        if not r.get('citation_eligible') or r.get('reading_status') != 'fulltext_reviewed':
            errors.append(f'Unavailable or unread citation: {r["id"]}')
        if r.get('fulltext_status') not in ('pdf', 'text') or not r.get('review_scope'):
            errors.append(f'Missing full-text review scope: {r["id"]}')
    published_ids = {r['id'] for r in refs}
    cited_ids = {x[4:] for d in docs.values() for x in d.ids if x.startswith('ref-')}
    if published_ids != cited_ids:
        errors.append(f'Catalogue and used citations differ: {published_ids ^ cited_ids}')
    sitemap = ET.parse(ROOT/'sitemap.xml')
    if len(sitemap.getroot()) != 18:
        errors.append('Expected 18 canonical sitemap pages')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(docs)} pages; local links/fragments/assets, alternative languages, reference parity, {len(refs)} citations, sitemap, and private-data checks.')


if __name__ == '__main__':
    main()
