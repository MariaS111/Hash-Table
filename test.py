# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 20:51:43 2021

@author: Masha
"""

import unittest
import hashtable


class CalcTest(unittest.TestCase):
   
  def test1search(self):
    self.assertEqual(hashtable.search(471, {471:['sdf'], 325:['mnb', 'mnbtg']} ), ['sdf'])
  def test2search(self):
    self.assertEqual(hashtable.search(372, {334:['mwc'], 372:['oit', 'oits'], 325:['mnbtg']} ),  ['oit', 'oits'] )
  def test1hash(self):
    self.assertEqual(hashtable.hash_funct('ty' ), 518)
  def test2hash(self):
    self.assertEqual(hashtable.hash_funct('as'), 18)
  def test3hash(self):
    self.assertEqual(hashtable.hash_funct('grfe'), 173)  
  def test1check(self):
    self.assertEqual(hashtable.check('e-o' ), False)
  def test2check(self):
    self.assertEqual(hashtable.check('4567kjh'), False)
  def test3check(self):
    self.assertEqual(hashtable.check('kerjh'), True)
  def test4check(self):
    self.assertEqual(hashtable.check('h'), False)    


if __name__ == "__main__":
  unittest.main()