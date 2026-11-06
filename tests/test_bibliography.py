"""Regression cases for identifiers and reference types in downloadable BibTeX."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from build_site import bibtex_entry


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


if __name__ == '__main__':
    unittest.main()
