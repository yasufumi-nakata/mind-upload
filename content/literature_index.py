"""Derived, public bibliography index. Never ingest a private discovery queue."""
import re
from collections import Counter
from urllib.parse import unquote


def normalize_doi(value):
    value = unquote((value or '').strip()).lower()
    return re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)', '', value)


def validate_references(refs):
    errors, seen = [], {}
    for key, ref in refs.items():
        if ref.get('id') != key:
            errors.append(f'{key}: ID mismatch')
        if not ref.get('citation_eligible') or ref.get('reading_status') != 'fulltext_reviewed':
            errors.append(f'{key}: not reviewed for publication')
        for lang in ('ja', 'en'):
            if not ref.get('review_scope', {}).get(lang):
                errors.append(f'{key}: missing {lang} review scope')
        doi = normalize_doi(ref.get('doi', ''))
        if doi:
            if doi in seen:
                errors.append(f'{key}: duplicate DOI with {seen[doi]}: {doi}')
            seen[doi] = key
    return errors


def make_index(refs, pages, edition):
    """Index actual page/section citations, not inferred task equivalence."""
    errors = validate_references(refs)
    if errors:
        raise ValueError('\n'.join(errors))
    records = []
    for key, ref in refs.items():
        mentions = []
        for page_id, page in pages.items():
            for section in page['sections']:
                for lang in ('ja', 'en'):
                    if f'[[{key}]]' in section['body'][lang]:
                        prefix = '/ja/' if lang == 'ja' else '/'
                        filename = 'index.html' if page_id == 'index' else page_id + '.html'
                        mentions.append({'lang': lang, 'url': prefix + filename + '#' + section['id']})
        records.append({'id': key, 'title': ref['title'], 'authors': ref.get('authors', []),
                        'year': ref.get('year', ''), 'accessed': ref.get('accessed', ''), 'doi': normalize_doi(ref.get('doi', '')),
                        'url': ref['url'], 'category': ref['category'],
                        'publication_status': ref.get('publication_status', ''),
                        'review_scope': ref['review_scope'], 'mentions': mentions})
    web_count = sum(ref.get('category') == 'organizations' for ref in refs.values())
    return {'edition': edition, 'scope': 'Reviewed public sources only; discovery candidates are excluded.',
            'counts': {'total': len(refs), 'literature': len(refs) - web_count,
                       'official_or_historical_web': web_count,
                       'by_category': dict(sorted(Counter(r['category'] for r in refs.values()).items()))},
            'records': records}
