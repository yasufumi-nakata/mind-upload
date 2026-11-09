#!/usr/bin/env python3
"""Validate local navigation, citations, assets and bilingual page metadata."""
import json
import re
import runpy
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EDITION = runpy.run_path(str(ROOT / 'content/edition.py'))
DATE = EDITION['DATE']
SITE_TITLE = EDITION['SITE_TITLE']
TERMINOLOGY = runpy.run_path(str(ROOT / 'content/terms.py'))
TERMS = TERMINOLOGY['TERMS']


class Document(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path, self.ids, self.links, self.images, self.canon, self.langs = path, [], [], [], [], {}
        self.library_records, self.library_categories = [], []
        self.library_count, self.citation_text, self.citation_titles = [], [], []
        self.json_ld, self.og_image_alts = [], []
        self._record = self._json_parts = self._citation_title = None
        self._record_scope = self._library_count = self._library_category = False
        self._sections = []
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            self.ids.append(a['id'])
        if tag == 'section':
            self._sections.append(a.get('id'))
        if tag == 'em' and 'citation-rights' in self._sections:
            self._citation_title = []
        if tag == 'script' and a.get('type') == 'application/ld+json':
            self._json_parts = []
        if tag == 'meta' and a.get('property') == 'og:image:alt':
            self.og_image_alts.append(a.get('content'))
        if tag == 'li' and 'library-record' in a.get('class', '').split():
            self._record = {'attrs': a, 'text': [], 'scope': [], 'dates': [], 'links': []}
            self.library_records.append(self._record)
        if self._record is not None:
            if tag == 'p' and 'review-scope' in a.get('class', '').split():
                self._record_scope = True
            if tag == 'time':
                self._record['dates'].append(a.get('datetime'))
            if tag == 'a' and a.get('href'):
                self._record['links'].append(a['href'])
        if tag == 'p' and a.get('id') == 'library-count':
            self._library_count = True
        if tag == 'select' and a.get('id') == 'library-category':
            self._library_category = True
        if tag == 'option' and self._library_category:
            self.library_categories.append(a.get('value', ''))
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


    def handle_data(self, data):
        if self._record is not None:
            self._record['text'].append(data)
            if self._record_scope:
                self._record['scope'].append(data)
        if self._library_count:
            self.library_count.append(data)
        if 'citation-rights' in self._sections:
            self.citation_text.append(data)
        if self._citation_title is not None:
            self._citation_title.append(data)
        if self._json_parts is not None:
            self._json_parts.append(data)

    def handle_endtag(self, tag):
        if tag == 'li':
            self._record = None
        if tag == 'p':
            self._record_scope = self._library_count = False
        if tag == 'select':
            self._library_category = False
        if tag == 'em' and self._citation_title is not None:
            self.citation_titles.append(''.join(self._citation_title))
            self._citation_title = None
        if tag == 'section' and self._sections:
            self._sections.pop()
        if tag == 'script' and self._json_parts is not None:
            try:
                self.json_ld.append(json.loads(''.join(self._json_parts)))
            except json.JSONDecodeError:
                self.json_ld.append(None)
            self._json_parts = None


def catalogue_errors(document, refs, lang):
    """Check the searchable records against the complete public bibliography."""
    errors = []
    records = document.library_records
    ids = [r['attrs'].get('data-reference-id', '') for r in records]
    expected = {ref['id']: ref for ref in refs}
    if len(ids) != len(set(ids)):
        errors.append(f'{lang}: duplicate catalogue records')
    if set(ids) != set(expected):
        errors.append(f'{lang}: catalogue coverage mismatch: missing={sorted(set(expected) - set(ids))}; extra={sorted(set(ids) - set(expected))}')
    if ''.join(document.library_count).split()[:1] != [str(len(refs))]:
        errors.append(f'{lang}: initial catalogue count differs from the bibliography')
    if set(document.library_categories) != {''} | {r.get('category', '') for r in refs}:
        errors.append(f'{lang}: catalogue category options differ from the bibliography')
    for record in records:
        ref_id = record['attrs'].get('data-reference-id', '')
        if ref_id not in expected:
            continue
        ref = expected[ref_id]
        search = record['attrs'].get('data-search', '')
        fields = [ref['title'], *ref.get('authors', []), *ref.get('author_display', []), *ref.get('search_aliases', []), ref.get('doi') or '']
        if any(field.lower() not in search for field in fields if field):
            errors.append(f'{lang}: catalogue search omits title, author, alias or DOI: {ref_id}')
        if record['attrs'].get('data-category') != ref.get('category', ''):
            errors.append(f'{lang}: incorrect catalogue category: {ref_id}')
        accessed = ref.get('accessed')
        if not accessed or record['dates'] != [accessed] or accessed not in ''.join(record['text']):
            errors.append(f'{lang}: missing or incorrect catalogue review date: {ref_id}')
        scope = ref.get('review_scope', {}).get(lang)
        if not scope or ''.join(record['scope']) != scope:
            errors.append(f'{lang}: missing or incorrect catalogue review scope: {ref_id}')
        if ref.get('url') not in record['links']:
            errors.append(f'{lang}: catalogue source link missing: {ref_id}')
    return errors


def citation_identity_errors(cff_text, resources):
    """Check the generated CFF scalar fields and the visible citation examples."""
    errors = []
    for key, expected in (('title', SITE_TITLE), ('version', DATE), ('date-released', DATE)):
        # The generator emits JSON-quoted YAML scalars, at the root and under
        # preferred-citation. This checks that output contract, not arbitrary YAML.
        matches = re.findall(r'^\s*' + key + r': (".*")$', cff_text, re.MULTILINE)
        try:
            values = [json.loads(value) for value in matches]
        except json.JSONDecodeError:
            values = []
        if values != [expected, expected]:
            errors.append(f'CITATION.cff: {key} differs from the site edition metadata')
    for lang, document in resources.items():
        if document.citation_titles != [SITE_TITLE]:
            errors.append(f'{lang}: citation example title differs from CITATION.cff')
        if EDITION['DATE_JA' if lang == 'ja' else 'DATE_EN'] not in ''.join(document.citation_text):
            errors.append(f'{lang}: citation example is missing the localized edition date')
    return errors


class ProseText(HTMLParser):
    """Read editorial prose without auditing paper titles or citation examples."""
    EXCLUDED = {'head', 'header', 'footer', 'nav', 'script', 'style', 'code',
                'pre', 'svg', 'math', 'figure', 'button', 'label', 'select', 'textarea'}
    HEADINGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'summary', 'thead', 'th'}
    BLOCKS = {'p', 'li', 'div', 'section', 'tr', 'td', 'th', 'dt', 'dd', *HEADINGS}
    VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
            'meta', 'param', 'source', 'track', 'wbr'}

    def __init__(self, body):
        super().__init__(convert_charrefs=True)
        self.stack, self.prose, self.editorial = [], [], []
        self.feed(body)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        excluded = (bool(self.stack and self.stack[-1][1]) or tag in self.EXCLUDED or
                    'data-no-terms' in a or 'data-term-glossary' in a or
                    a.get('id') in {'references', 'citation-rights'} or
                    bool({'library-record', 'refs'} & set(a.get('class', '').split())))
        heading = bool(self.stack and self.stack[-1][2]) or tag in self.HEADINGS
        if tag in self.BLOCKS or tag == 'br':
            self.prose.append('\n')
            self.editorial.append('\n')
        if tag not in self.VOID:
            self.stack.append((tag, excluded, heading))

    def handle_endtag(self, tag):
        if tag in self.BLOCKS:
            self.prose.append('\n')
            self.editorial.append('\n')
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        excluded = bool(self.stack and self.stack[-1][1])
        heading = bool(self.stack and self.stack[-1][2])
        if not excluded:
            self.editorial.append(data)
            if not heading:
                self.prose.append(data)


def terminology_warnings(body, lang):
    """Nonblocking editorial checks; ambiguous terms need contextual review."""
    parsed = ProseText(body)
    prose, editorial = ''.join(parsed.prose), ''.join(parsed.editorial)
    warnings = []
    if lang == 'ja':
        for old, preferred in TERMINOLOGY['DISCOURAGED'].items():
            if old in editorial:
                warnings.append(f'表記の確認: {old} → {preferred}')
        # Inline links/strong tags do not split a sentence; block boundaries do.
        for sentence in re.split(r'[。！？\n]', prose):
            compact = re.sub(r'\s+|\[\d+\]', '', sentence)
            if len(compact) > 80 and re.search(r'[ぁ-んァ-ヶ一-龯]', compact):
                warnings.append(f'長い文（{len(compact)}字）: {compact[:55]}…')
    for term in TERMS:
        if not term['abbreviations']:
            continue
        pattern = r'(?<![A-Za-z0-9_])(?:' + '|'.join(map(re.escape, term['abbreviations'])) + r')(?![A-Za-z0-9_])'
        first = re.search(pattern, prose)
        if not first:
            continue
        prefix = prose[:first.start()].casefold()
        following = re.match(r'\s*[（(]([^）)]{1,160})[）)]', prose[first.end():])
        following_text = following[1].casefold() if following else ''
        names = (*term['aliases'][lang], term['expansion'][lang])
        if not any(name.casefold() in prefix or name.casefold() in following_text for name in names):
            warnings.append(f'略語の初出説明を確認: {first[0]}')
    return warnings


def glossary_errors(documents):
    """Both languages must expose every central term with the same stable ID."""
    expected = {'term-' + term['id'] for term in TERMS}
    errors = []
    if len(expected) != len(TERMS):
        errors.append('Duplicate terminology identifiers')
    for lang, document in documents.items():
        actual = {key for key in document.ids if key.startswith('term-')}
        if actual != expected:
            errors.append(f'{lang}: glossary coverage differs from central terms: {actual ^ expected}')
    for term in TERMS:
        if any(not term[field].get(lang) for field in ('label', 'definition', 'aliases') for lang in ('ja', 'en')):
            errors.append(f'Incomplete bilingual term: {term["id"]}')
    return errors


def main():
    files = sorted(ROOT.glob('*.html')) + sorted((ROOT/'ja').glob('*.html'))
    docs = {p.resolve(): Document(p) for p in files}
    errors, warnings = [], []
    for path, d in docs.items():
        label = str(path.relative_to(ROOT))
        if len(d.ids) != len(set(d.ids)):
            errors.append(f'{label}: duplicate ids')
        if len(d.canon) != 1:
            errors.append(f'{label}: missing or duplicate canonical')
        if path.stem not in ('philosophy', 'scenario'):
            if set(d.langs) != {'en', 'ja', 'x-default'}:
                errors.append(f'{label}: language alternates missing')
            if DATE not in path.read_text():
                errors.append(f'{label}: edition date missing')
            if len(d.json_ld) != 1 or not isinstance(d.json_ld[0], dict) or d.json_ld[0].get('isPartOf', {}).get('name') != SITE_TITLE:
                errors.append(f'{label}: JSON-LD site title differs from citation metadata')
            elif path.stem == 'index' and d.json_ld[0].get('name') != SITE_TITLE:
                errors.append(f'{label}: JSON-LD WebSite name differs from citation metadata')
            if d.og_image_alts != [SITE_TITLE]:
                errors.append(f'{label}: OG image title differs from citation metadata')
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
        if path.stem not in ('philosophy', 'scenario'):
            warnings.extend(f'{label}: {warning}' for warning in terminology_warnings(body, 'ja' if path.parent.name == 'ja' else 'en'))
        if re.search(r'\[\[[A-Z0-9_]+\]\]|\{\{[a-z_]+\}\}', body):
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
    index_tools = runpy.run_path(str(ROOT/'content/literature_index.py'))
    page_sources = runpy.run_path(str(ROOT/'content/site_content.py'))['PAGES']
    source_refs = json.loads((ROOT/'content/references.json').read_text())
    errors.extend(index_tools['validate_references'](source_refs))
    index_path = ROOT/'data/literature-index.json'
    try:
        index_data = json.loads(index_path.read_text())
        if index_data != index_tools['make_index'](source_refs, page_sources, DATE):
            errors.append('Literature index differs from adopted sources or citation locations')
        for record in index_data.get('records', []):
            for mention in record['mentions']:
                path, anchor = mention['url'].split('#', 1)
                document = docs.get(ROOT/path.lstrip('/'))
                if not document or anchor not in document.ids:
                    errors.append(f"Literature index has an invalid citation location: {record['id']}")
    except (OSError, ValueError, KeyError) as exc:
        errors.append(f'Invalid literature index: {exc}')
    sources = json.loads((ROOT/'content/references.json').read_text())
    if {r['id']: r for r in refs} != sources:
        errors.append('Public JSON bibliography differs from the source records')
    bib_ids = re.findall(r'^@\w+\{([^,\n]+),', (ROOT/'assets/references.bib').read_text(), re.MULTILINE)
    if len(bib_ids) != len(set(bib_ids)) or set(bib_ids) != published_ids:
        errors.append('BibTeX coverage differs from the public JSON bibliography')
    resources = {'en': docs[ROOT/'resources.html'], 'ja': docs[ROOT/'ja/resources.html']}
    errors.extend(glossary_errors({'en': docs[ROOT/'science.html'], 'ja': docs[ROOT/'ja/science.html']}))
    if not {key for term in TERMS for key in term['refs']} <= published_ids:
        errors.append('Terminology cites an unavailable source')
    for lang, document in resources.items():
        errors.extend(catalogue_errors(document, refs, lang))
    errors.extend(citation_identity_errors((ROOT/'CITATION.cff').read_text(), resources))
    if (ROOT/'README.md').read_text().splitlines()[0] != '# ' + SITE_TITLE:
        errors.append('README title differs from the site citation metadata')
    cited_ids = {x[4:] for d in docs.values() for x in d.ids if x.startswith('ref-')}
    if published_ids != cited_ids:
        errors.append(f'Bibliography and used citations differ: {published_ids ^ cited_ids}')
    sitemap = ET.parse(ROOT/'sitemap.xml')
    if len(sitemap.getroot()) != 18:
        errors.append('Expected 18 canonical sitemap pages')
    if any(node.text != DATE for node in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod')):
        errors.append('Sitemap dates do not match the edition')
    if errors:
        raise SystemExit('\n'.join(errors))
    if warnings:
        print('読みやすさ・表記の注意（非blocking）:\n' + '\n'.join(warnings))
    print(f'PASS: {len(docs)} pages; local links/fragments/assets, alternative languages, reference parity, {len(refs)} catalogue and download records, citation identity, {len(TERMS)} bilingual terms, sitemap, and private-data checks. Editorial notices: {len(warnings)}.')


if __name__ == '__main__':
    main()
