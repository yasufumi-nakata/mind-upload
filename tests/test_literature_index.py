"""Public bibliography indices cannot promote discovery candidates into evidence."""
import copy
import json
from pathlib import Path
import runpy
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / 'content/literature_index.py'))
normalize_doi = MODULE['normalize_doi']
validate_references = MODULE['validate_references']
make_index = MODULE['make_index']
REFS = json.loads((ROOT / 'content/references.json').read_text())
PAGES = runpy.run_path(str(ROOT / 'content/site_content.py'))['PAGES']
DATE = runpy.run_path(str(ROOT / 'content/edition.py'))['DATE']


class LiteratureIndexTests(unittest.TestCase):
    def test_doi_aliases_are_normalized(self):
        for value in ['10.1234/ABC_1', ' https://doi.org/10.1234/ABC_1 ',
                      'http://dx.doi.org/10.1234/ABC_1', 'DOI: 10.1234/ABC%5F1']:
            self.assertEqual('10.1234/abc_1', normalize_doi(value))
        self.assertEqual('', normalize_doi(None))

    def test_duplicate_doi_is_rejected(self):
        refs = copy.deepcopy(REFS)
        key = next(key for key, ref in refs.items() if ref.get('doi'))
        refs['DUPLICATE'] = dict(refs[key], id='DUPLICATE', doi='https://doi.org/' + refs[key]['doi'].upper())
        self.assertIn('duplicate DOI', '\n'.join(validate_references(refs)))
        with self.assertRaises(ValueError):
            make_index(refs, PAGES, DATE)

    def test_id_and_each_review_language_are_required(self):
        refs = copy.deepcopy(REFS)
        key = next(iter(refs))
        refs[key]['id'] = 'WRONG'
        del refs[key]['review_scope']['ja']
        errors = '\n'.join(validate_references(refs))
        self.assertIn('ID mismatch', errors)
        self.assertIn('missing ja review scope', errors)

    def test_unreviewed_candidates_cannot_enter_the_public_index(self):
        for field, value in [('citation_eligible', False), ('reading_status', 'unread')]:
            refs = copy.deepcopy(REFS)
            refs[next(iter(refs))][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                make_index(refs, PAGES, DATE)

    def test_index_covers_every_adopted_source_and_counts(self):
        index = make_index(REFS, PAGES, DATE)
        self.assertEqual([], validate_references(REFS))
        self.assertEqual(set(REFS), {record['id'] for record in index['records']})
        self.assertEqual(len(REFS), index['counts']['total'])
        self.assertEqual(len(REFS), index['counts']['literature'] + index['counts']['official_or_historical_web'])
        self.assertEqual(len(REFS), sum(index['counts']['by_category'].values()))

    def test_mentions_are_real_bilingual_page_sections(self):
        for record in make_index(REFS, PAGES, DATE)['records']:
            self.assertEqual({'ja', 'en'}, {mention['lang'] for mention in record['mentions']})
            for mention in record['mentions']:
                path, anchor = mention['url'].split('#')
                page = Path(path).stem
                section = next(section for section in PAGES[page]['sections'] if section['id'] == anchor)
                self.assertIn('[[' + record['id'] + ']]', section['body'][mention['lang']])
                self.assertEqual(mention['lang'] == 'ja', path.startswith('/ja/'))

    def test_index_output_matches_the_source(self):
        self.assertEqual(make_index(REFS, PAGES, DATE), json.loads((ROOT / 'data/literature-index.json').read_text()))


if __name__ == '__main__':
    unittest.main()
