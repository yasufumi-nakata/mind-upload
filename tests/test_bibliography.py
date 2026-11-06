"""Regression cases for bibliography exports, catalogue search and site citations."""
import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_site import bibtex_entry
import build_site as build
from check_site import Document, catalogue_errors, citation_identity_errors


class BibliographyTests(unittest.TestCase):
    def test_identifiers_remain_literal_and_titles_keep_their_case(self):
        entry = bibtex_entry('EXAMPLE', {
            'title': 'NEURON & OpenWorm: C. elegans, Drosophila and ZAPBench',
            'authors': ['Research Consortium'], 'type': 'journalArticle',
            'year': '2025', 'venue': 'Neural Models',
            'doi': '10.1007/0-306-48610-5_11',
            'url': 'https://example.org/a_b?part=1&name=C%20elegans',
        })
        self.assertIn('doi = {10.1007/0-306-48610-5_11}', entry)
        self.assertIn('url = {https://example.org/a_b?part=1&name=C%20elegans}', entry)
        self.assertIn(r'title = {{NEURON \& OpenWorm: C. elegans, Drosophila and ZAPBench}}', entry)
        self.assertIn('author = {{Research Consortium}}', entry)

    def test_web_resource_has_no_fictitious_publication_year_or_journal(self):
        entry = bibtex_entry('WEB', {
            'title': 'Research library', 'authors': ['Foundation'],
            'type': 'webpage', 'year': 'n.d.', 'venue': 'Web resource',
            'accessed': '2026-11-04',
        })
        self.assertTrue(entry.startswith('@misc{WEB,'))
        self.assertNotIn('  year =', entry)
        self.assertNotIn('  journal =', entry)
        self.assertIn('howpublished = {Web resource}', entry)
        self.assertIn('urldate = {2026-11-04}', entry)

    def test_report_has_distinct_institution_and_report_number(self):
        entry = bibtex_entry('ROADMAP', {
            'title': 'Whole Brain Emulation: A Roadmap', 'type': 'report',
            'institution': 'Future of Humanity Institute, University of Oxford',
            'report_number': '2008-3', 'year': '2008',
        })
        self.assertTrue(entry.startswith('@techreport{ROADMAP,'))
        self.assertIn('institution = {Future of Humanity Institute, University of Oxford}', entry)
        self.assertIn('number = {2008-3}', entry)
        self.assertNotIn('  journal =', entry)

    def test_preprint_is_not_exported_as_a_journal_article(self):
        entry = bibtex_entry('DRAFT', {
            'title': 'A draft CNS connectome', 'type': 'journalArticle',
            'publication_status': 'preprint', 'venue': 'bioRxiv',
            'year': '2026', 'note': 'First draft.',
            'bibtex_authors': ['Barnes, Christopher L.', 'Xu, C. Shan', '{The Consortium}'],
        })
        self.assertTrue(entry.startswith('@misc{DRAFT,'))
        self.assertNotIn('  journal =', entry)
        self.assertIn('howpublished = {bioRxiv preprint}', entry)
        self.assertIn('Preprint; not peer reviewed.', entry)
        self.assertIn('Barnes, Christopher L. and Xu, C. Shan and {The Consortium}', entry)


class CatalogueTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.folder = tempfile.TemporaryDirectory()
        cls.documents = {}
        for lang in ('ja', 'en'):
            path = Path(cls.folder.name) / f'library-{lang}.html'
            path.write_text(build.library(lang))
            cls.documents[lang] = Document(path)

    @classmethod
    def tearDownClass(cls):
        cls.folder.cleanup()

    @staticmethod
    def matching_ids(document, query, category=''):
        # These are the DOM attributes consumed by the existing browser filter.
        words = query.lower().split()
        return {
            row['attrs']['data-reference-id'] for row in document.library_records
            if (not category or row['attrs']['data-category'] == category)
            and all(word in row['attrs']['data-search'] for word in words)
        }

    def test_displayed_author_names_and_existing_queries_find_the_paper(self):
        queries = [
            ('Lappalainen JK', 'XMYSQXY8'),
            ('Lappalainen', 'XMYSQXY8'),
            (build.REFS['XMYSQXY8']['authors'][0], 'XMYSQXY8'),
            ('Shiu PK', 'V4GV7JAJ'),
            (build.REFS['V4GV7JAJ']['title'], 'V4GV7JAJ'),
            (build.REFS['V4GV7JAJ']['doi'], 'V4GV7JAJ'),
        ]
        for lang, document in self.documents.items():
            for query, ref_id in queries:
                with self.subTest(lang=lang, query=query):
                    self.assertIn(ref_id, self.matching_ids(document, query))
                    self.assertIn(ref_id, self.matching_ids(document, query, build.REFS[ref_id]['category']))
                    self.assertNotIn(ref_id, self.matching_ids(document, query, 'organizations'))

    def test_every_record_is_searchable_with_its_review_details(self):
        refs = list(build.REFS.values())
        web_ids = {'CCFAQ', 'CCRESEARCH', 'CCROADMAP', 'CCCHALLENGE', 'CCBRAINGENIX',
                   'CCFLY', 'CCLIBRARY', 'STROUT', 'EON', 'MALEDATA'}
        for lang, document in self.documents.items():
            with self.subTest(lang=lang):
                self.assertEqual(set(build.REFS), self.matching_ids(document, ''))
                self.assertTrue(web_ids <= self.matching_ids(document, '', 'organizations'))
                self.assertEqual([], catalogue_errors(document, refs, lang))
                for row in document.library_records:
                    ref = build.REFS[row['attrs']['data-reference-id']]
                    self.assertIn(build.publication_type(ref, lang), ''.join(row['text']))

    def test_organisation_and_page_queries_work_with_category_filter(self):
        for lang, document in self.documents.items():
            for query, ref_id in [('Eon Systems', 'EON'), ('BrainGenix', 'CCBRAINGENIX'),
                                  ('MaleCNS', 'MALEDATA'),
                                  ('Male CNS connectome: data download', 'MALEDATA')]:
                with self.subTest(lang=lang, query=query):
                    self.assertIn(ref_id, self.matching_ids(document, query, 'organizations'))
                    self.assertNotIn(ref_id, self.matching_ids(document, query, '構造・コネクトミクス'))

    def test_checker_rejects_catalogue_omissions_duplicates_and_search_regressions(self):
        refs = list(build.REFS.values())
        missing = copy.deepcopy(self.documents['en'])
        missing.library_records = [r for r in missing.library_records if r['attrs']['data-reference-id'] != 'EON']
        self.assertIn('catalogue coverage mismatch', '\n'.join(catalogue_errors(missing, refs, 'en')))
        duplicate = copy.deepcopy(self.documents['en'])
        duplicate.library_records.append(duplicate.library_records[0])
        self.assertIn('duplicate catalogue records', '\n'.join(catalogue_errors(duplicate, refs, 'en')))
        abbreviated = copy.deepcopy(self.documents['en'])
        row = next(r for r in abbreviated.library_records if r['attrs']['data-reference-id'] == 'XMYSQXY8')
        row['attrs']['data-search'] = row['attrs']['data-search'].replace('lappalainen jk', '')
        self.assertIn('catalogue search omits', '\n'.join(catalogue_errors(abbreviated, refs, 'en')))
        alias_missing = copy.deepcopy(self.documents['en'])
        row = next(r for r in alias_missing.library_records if r['attrs']['data-reference-id'] == 'MALEDATA')
        row['attrs']['data-search'] = row['attrs']['data-search'].replace('malecns', '')
        self.assertIn('catalogue search omits', '\n'.join(catalogue_errors(alias_missing, refs, 'en')))


class SiteCitationTests(unittest.TestCase):
    def test_citation_title_and_localized_dates_agree_across_outputs(self):
        page = {
            'title': {'ja': '引用方法', 'en': 'Citation'},
            'lead': {'ja': '引用例', 'en': 'Citation example'},
            'sections': [{'id': 'citation-rights', 'title': {'ja': '引用', 'en': 'Citation'},
                          'body': {lang: '<p><em>{{site_title}}</em>. {{edition_date}}</p>' for lang in ('ja', 'en')}}],
        }
        with tempfile.TemporaryDirectory() as folder, patch.object(build, 'ROOT', Path(folder)):
            resources = {}
            for lang in ('ja', 'en'):
                build.build_page('resources', page, lang)
                path = Path(folder) / ('ja' if lang == 'ja' else '') / 'resources.html'
                resources[lang] = Document(path)
                self.assertEqual(build.SITE_TITLE, resources[lang].json_ld[0]['isPartOf']['name'])
                self.assertEqual([build.SITE_TITLE], resources[lang].og_image_alts)
                self.assertNotIn(build.DATE, ''.join(resources[lang].citation_text))
                self.assertNotIn('{{', path.read_text())
            cff = build.citation_cff()
            self.assertEqual([], citation_identity_errors(cff, resources))
            wrong_cff = cff.replace(build.SITE_TITLE, 'Different citation title', 1)
            self.assertIn('CITATION.cff: title differs', '\n'.join(citation_identity_errors(wrong_cff, resources)))
            resources['ja'].citation_titles = ['Different visible title']
            resources['en'].citation_text = [build.DATE]
            errors = '\n'.join(citation_identity_errors(cff, resources))
            self.assertIn('ja: citation example title differs', errors)
            self.assertIn('en: citation example is missing the localized edition date', errors)


if __name__ == '__main__':
    unittest.main()
