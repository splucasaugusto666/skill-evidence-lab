import unittest
from evaluate import digest, evaluate


class PairedEvaluationTest(unittest.TestCase):
    def setUp(self):
        self.plan = {'schema_version': 1, 'data_origin': 'synthetic', 'model': 'fixture',
                     'scorer': 'fixture-v1', 'config_sha256': '0'*64,
                     'conditions': {'A': '1'*64, 'C': '2'*64},
                     'tasks': {'t1': '3'*64, 't2': '4'*64}, 'repetitions': 1}

    def row(self, task, condition, success):
        return {'plan_sha256': digest(self.plan), 'task': task, 'repeat': 1,
                'condition': condition, 'status': 'completed' if success is not None else 'error',
                'success': success, 'output_sha256': '5'*64 if success is not None else None}

    def test_complete_pairs(self):
        rows = [self.row('t1','A',False), self.row('t1','C',True),
                self.row('t2','A',True), self.row('t2','C',False)]
        c = evaluate(self.plan,rows)['comparisons']['C-A']
        self.assertEqual((c['wins'],c['losses'],c['complete_pair_delta']), (1,1,0))
        self.assertEqual(c['all_planned_delta_bounds'], [0,0])
        self.assertEqual(evaluate(self.plan,rows),evaluate(self.plan,list(reversed(rows))))

    def test_missing_bounds(self):
        c = evaluate(self.plan,[self.row('t1','A',False), self.row('t1','C',True),
                                self.row('t2','A',True)])['comparisons']['C-A']
        self.assertEqual(c['complete_pair_delta'], 1)
        self.assertEqual(c['all_planned_delta_bounds'], [0,0.5])
        self.assertEqual(c['incomplete_pairs'], 1)

    def test_empty(self):
        c = evaluate(self.plan,[])['comparisons']['C-A']
        self.assertIsNone(c['complete_pair_delta'])
        self.assertEqual(c['all_planned_delta_bounds'],[-1,1])

    def test_errors(self):
        report = evaluate(self.plan,[self.row('t1','A',None)])
        self.assertEqual(report['error_records'],1)
        self.assertEqual(report['comparisons']['C-A']['complete_pairs'],0)

    def test_duplicate(self):
        r = self.row('t1','A',True)
        with self.assertRaisesRegex(ValueError,'duplicate'):
            evaluate(self.plan,[r,r])

    def test_mismatched_plan(self):
        r = self.row('t1','A',True)
        self.plan['model'] = 'different'
        with self.assertRaisesRegex(ValueError,'plan hash'):
            evaluate(self.plan,[r])

    def test_reject_numeric_success(self):
        r = self.row('t1','A',1)
        with self.assertRaisesRegex(ValueError,'completed'):
            evaluate(self.plan,[r])

    def test_reject_unknown_task(self):
        with self.assertRaisesRegex(ValueError,'unknown task'):
            evaluate(self.plan,[self.row('other','A',True)])

    def test_four_conditions(self):
        self.plan['conditions'].update(B='6'*64,D='7'*64)
        self.assertEqual(set(evaluate(self.plan,[])['comparisons']),{'C-A','C-B','D-C'})

    def test_grid_limit(self):
        self.plan['repetitions'] = 101
        with self.assertRaisesRegex(ValueError,'grid limit'):
            evaluate(self.plan,[])
