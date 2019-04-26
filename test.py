#! /usr/bin/env python

import unittest

class MyTests(unittest.TestCase):
  def test_that_it_passes(self):
    self.assertEqual(0, 0)

  @unittest.skip("not finished yet")
  def test_that_it_skips(self): 
    raise Exception("Does not happen")

  def test_that_it_fails(self):
    self.assertEqual(1, 0)

if __name__ == '__main__':
  from pycotap import TAPTestRunner
  suite = unittest.TestLoader().loadTestsFromTestCase(MyTests)
  result = TAPTestRunner().run(suite)
  if not result.wasSuccessful ():
    exit (1)
