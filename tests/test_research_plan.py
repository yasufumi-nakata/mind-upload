import copy
import runpy
import unittest
from pathlib import Path

P = runpy.run_path(str(Path(__file__).resolve().parents[1] / 'content/research_plan.py'))

class ResearchPlanTests(unittest.TestCase):
    def test_initial_evidence_score_and_fixed_denominator(self):
        value = P['score']()
        self.assertEqual(value, dict(earned=10, total=100, percent=10, unknown=55, added=0))
        self.assertEqual(len(P['ITEMS']),14)
        self.assertEqual([sum(x['points'] for x in P['ITEMS'] if x['stage']==s['id']) for s in P['STAGES']], [20,25,25,30])
    def test_increment_is_shared_and_not_double_counted(self):
        value = P['score'](assume=['M1','M1','F-STRUCTURE'])
        self.assertEqual(value['percent'],15)
        self.assertEqual(value['added'],5)
        self.assertEqual(P['score'](assume=['M1','M2'])['percent'],20)
        self.assertEqual(P['score'](assume=['M1','M2','M3','M4'])['percent'],45)
        with self.assertRaises(ValueError): P['score'](assume=['unknown'])
        with self.assertRaises(ValueError): P['score'](items=P['ITEMS']+(P['ITEMS'][0],))
    def test_unknown_keeps_denominator_and_changes_only_with_evidence(self):
        items=copy.deepcopy(list(P['ITEMS']))
        items[4]['status']='not_assessed'
        self.assertEqual(P['score'](items)['percent'],10)
        self.assertEqual(P['score'](items)['unknown'],60)
        items[4]['status']='met'
        self.assertEqual(P['score'](items)['percent'],15)
        self.assertEqual(P['score'](items)['unknown'],55)
        items[0]['status']='not_met'
        self.assertEqual(P['score'](items)['percent'],12.5)
    def test_stage_requires_each_item_and_prior_stage(self):
        later=[x['id'] for x in P['ITEMS'] if x['stage'] in ('S3','S4')]
        self.assertGreater(P['score'](assume=later)['percent'],45)
        self.assertFalse(P['stage_complete']('S2', assume=later))
        self.assertFalse(P['stage_complete']('S2', assume=['M3','M4']))
        self.assertTrue(P['stage_complete']('S2', assume=['M1','M2','M3','M4']))
        all_ids=[x['id'] for x in P['ITEMS']]
        self.assertEqual(P['score'](assume=all_ids)['percent'],100)
        self.assertTrue(P['stage_complete']('S4', assume=all_ids))
        for missing in all_ids:
            if missing.startswith('F-'): continue
            remaining=[x for x in all_ids if x != missing]
            self.assertFalse(P['stage_complete']('S4', assume=remaining))
        self.assertFalse(P['stage_complete']('S4', items=P['ITEMS'][:-1], assume=all_ids))
    def test_ids_evidence_and_bilingual_numbers(self):
        tasks={i for ids in P['TASK_IDS'].values() for i in ids}
        self.assertEqual(tasks,{f'R{i:02}' for i in range(1,13)})
        for x in P['ITEMS']:
            self.assertTrue(set(x['tasks']) <= tasks)
            self.assertTrue(x['reviewed'])
            self.assertTrue(x['criterion'][0] and x['criterion'][1])
            if x['status']=='met':self.assertTrue(x['refs'])
        for lang in ('ja','en'):
            text=P['progress_summary'](lang)
            self.assertIn('10%', text); self.assertIn('15%',text);self.assertIn('20%',text)

if __name__=='__main__': unittest.main()
