"""Regression checks for shared terms and safe per-page first-use explanations."""
import copy
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import build_site as build
from check_site import Document, glossary_errors, terminology_warnings


class TermAnnotationTests(unittest.TestCase):
    def test_first_use_is_shared_across_sections_but_reset_for_each_page(self):
        seen = set()
        first = build.annotate_terms('<p>EMとコネクトームを調べます。</p>', 'ja', seen)
        later = build.annotate_terms('<p>EMとコネクトームを比べます。</p>', 'ja', seen)
        next_page = build.annotate_terms('<p>EMを調べます。</p>', 'ja')
        self.assertIn('電子顕微鏡法（EM）', first)
        self.assertEqual(2, first.count('class="term-link"'))
        self.assertNotIn('term-link', later)
        self.assertIn('電子顕微鏡法（EM）', next_page)

    def test_headings_attributes_existing_links_and_source_titles_are_unchanged(self):
        protected = (
            '<h2>EM</h2><a href="https://example.org/EM" title="ASC">WBE</a>'
            '<code>EM</code><pre>ASC</pre><script>const EM="WBE";</script>'
            '<figure><figcaption>Electron microscopy</figcaption></figure>'
            '<ol class="refs"><li id="ref-EM">EM and WBE</li></ol>'
            '<li class="library-record" data-search="em">EM study</li>'
            '<section id="citation-rights"><p>WBE reference example</p></section>'
            '<span data-no-terms>ASC quotation</span>'
        )
        body = protected + '<p title="EM &amp; ASC">EM then WBE and ASC.</p>'
        result = build.annotate_terms(body, 'en')
        self.assertTrue(result.startswith(protected))
        self.assertIn('<p title="EM &amp; ASC">', result)
        self.assertIn('electron microscopy (EM)', result)
        self.assertIn('whole-brain emulation (WBE)', result)
        self.assertIn('aldehyde-stabilized cryopreservation (ASC)', result)

    def test_existing_explanations_are_not_repeated_even_across_inline_tags(self):
        cases = (
            ('ja', '<p>電子顕微鏡法（EM）とEMです。</p>', '電子顕微鏡法', 'EM'),
            ('ja', '<p><strong>電子顕微鏡法</strong>（EM）とEMです。</p>', '電子顕微鏡法', 'EM'),
            ('ja', '<p>正規化相関CCnormです。</p>', '正規化相関', 'CCnorm'),
            ('en', '<p>electron microscopy (EM), then EM.</p>', 'electron microscopy', 'EM'),
            ('en', '<p><em>electron microscopy</em> (EM), then EM.</p>', 'electron microscopy', 'EM'),
            ('ja', '<p>TOST（2つの片側検定）を使います。</p>', '2つの片側検定', 'TOST'),
        )
        for lang, source, name, abbreviation in cases:
            with self.subTest(source=source):
                result = build.annotate_terms(source, lang)
                # Definitions in title attributes may contain the name too.
                visible = build.re.sub(r'<[^>]+>', '', result)
                self.assertEqual(1, visible.count(name))
                self.assertEqual(source.count(abbreviation), visible.count(abbreviation))
                self.assertEqual(1, result.count('class="term-link"'))

    def test_token_boundaries_entities_and_longest_alias_are_preserved(self):
        source = '<!-- EM --><p>CEM SYSTEM EM_model EM2 &amp; WBE EM.</p>'
        result = build.annotate_terms(source, 'en')
        self.assertTrue(result.startswith('<!-- EM -->'))
        self.assertIn('CEM SYSTEM EM_model EM2 &amp;', result)
        self.assertEqual(2, result.count('class="term-link"'))
        full = build.annotate_terms('<p>whole-brain emulation is a goal.</p>', 'en')
        self.assertEqual(1, full.count('class="term-link"'))
        self.assertIn('data-term="wbe"', full)
        self.assertNotIn('data-term="emulation"', full)

    def test_method_abbreviations_and_measurement_symbols_have_precise_expansions(self):
        source = '<p>ExLSFM, CCmax, CCnorm, ECCI, SNR, r²_ER, fSBI, MAE, ΔF/F.</p>'
        result = build.annotate_terms(source, 'en')
        for full in ('expansion light-sheet fluorescence microscopy (ExLSFM)',
                     'estimate-centered credible interval (ECCI)',
                     'filter simulation-based inference (fSBI)',
                     'mean absolute error (MAE)',
                     'relative change in fluorescence (ΔF/F)'):
            self.assertIn(full, result)
        self.assertNotIn('flexible simulation-based inference', result)
        self.assertEqual(9, result.count('class="term-link"'))
        self.assertEqual([], terminology_warnings(result, 'en'))

    def test_builder_processes_lead_before_sections_and_keeps_metadata_plain(self):
        page = dict(title=dict(ja='EMの見出し', en='EM heading'),
                    lead=dict(ja='EMで測定します。', en='Measure with EM.'),
                    sections=[dict(id='detail', title=dict(ja='WBEの見出し', en='WBE heading'),
                                   body=dict(ja='<p>EMとWBEを比べます。</p>', en='<p>Compare EM and WBE.</p>'))])
        with tempfile.TemporaryDirectory() as folder, patch.object(build, 'ROOT', Path(folder)):
            for lang in ('ja', 'en'):
                build.build_page('example', page, lang)
                path = Path(folder) / ('ja' if lang == 'ja' else '') / 'example.html'
                rendered = path.read_text()
                self.assertEqual(1, rendered.count('data-term="em"'))
                self.assertEqual(1, rendered.count('data-term="wbe"'))
                self.assertIn(f'<h1>{page["title"][lang]}</h1>', rendered)
                self.assertIn(f'<h2>{page["sections"][0]["title"][lang]}</h2>', rendered)
                self.assertIn(f'<meta name="description" content="{page["lead"][lang]}">', rendered)
                self.assertLess(rendered.index('data-term="em"'), rendered.index('id="detail"'))


class GlossaryChecks(unittest.TestCase):
    def test_glossary_contains_every_shared_term_in_both_languages(self):
        with tempfile.TemporaryDirectory() as folder:
            documents = {}
            for lang in ('ja', 'en'):
                body = build.expand_body('{{glossary}}', lang)
                self.assertEqual(body, build.annotate_terms(body, lang))
                path = Path(folder) / f'{lang}.html'
                path.write_text(body)
                documents[lang] = Document(path)
                for term in build.TERMS:
                    self.assertIn(term['label'][lang], body)
                    self.assertIn(build.H(term['definition'][lang]), body)
                    self.assertTrue(set(term['refs']) <= set(build.REFS))
            self.assertEqual([], glossary_errors(documents))
            missing = copy.deepcopy(documents)
            missing['ja'].ids.remove('term-wbe')
            self.assertTrue(glossary_errors(missing))

    def test_checker_finds_legacy_forms_and_missing_explanations_only_in_prose(self):
        source = ('<head><title>感覚帰還 EM</title></head><main>'
                  '<h2>EM</h2><p>感覚帰還と濃芯小胞。WBEを評価します。</p>'
                  '<ol class="refs"><li>里程標 ASC</li></ol>'
                  '<li class="library-record">拡大顕微鏡 BMTK</li>'
                  '<section id="citation-rights"><p>被覆率 OSF</p></section></main>')
        warnings = terminology_warnings(source, 'ja')
        self.assertEqual(3, len(warnings))
        self.assertTrue(any('感覚帰還' in warning for warning in warnings))
        self.assertTrue(any('濃芯小胞' in warning for warning in warnings))
        self.assertTrue(any('WBE' in warning for warning in warnings))
        annotated = build.annotate_terms('<p>WBEとEMを評価します。</p>', 'ja')
        self.assertEqual([], terminology_warnings(annotated, 'ja'))

    def test_long_sentence_check_keeps_inline_text_and_exempts_citation_examples(self):
        source = '<p>' + '長い文を確認します' * 5 + '<strong>' + '同じ文を続けます' * 5 + '</strong>。</p>'
        self.assertTrue(any('長い文' in message for message in terminology_warnings(source, 'ja')))
        exempt = '<section id="citation-rights">' + source + '</section>'
        self.assertEqual([], terminology_warnings(exempt, 'ja'))


if __name__ == '__main__':
    unittest.main()
