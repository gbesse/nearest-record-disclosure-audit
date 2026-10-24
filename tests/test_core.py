import unittest
from nearest_record_disclosure_audit import run
class Tests(unittest.TestCase):
 def data(self):return {'fields':{'x':{'kind':'numeric','minimum':0,'maximum':10},'c':{'kind':'category'}},'source':[{'id':'s','x':2,'c':'a'}],'holdout':[{'id':'h','x':8,'c':'b'}],'synthetic':[{'id':'g','x':2,'c':'a'}]}
 def test_exact_source_copy_and_known_gower_distance(self):
  r=run(self.data())['records'][0];self.assertEqual(r['nearest_source']['distance'],0);self.assertAlmostEqual(r['nearest_holdout']['distance'],.8);self.assertTrue(r['closer_to_source'])
 def test_missing_fields_do_not_become_zero_distance(self):
  d=self.data();d['synthetic']=[{'id':'g'}];r=run(d)['records'][0];self.assertIsNone(r['nearest_source']);self.assertIsNone(r['closer_to_source'])
 def test_declared_ranges_not_refitted_on_synthetic(self):
  d=self.data();d['synthetic'][0]['x']=11
  with self.assertRaises(ValueError):run(d)
 def test_source_holdout_identity_overlap_rejected(self):
  d=self.data();d['holdout'][0]['id']='s'
  with self.assertRaises(ValueError):run(d)
