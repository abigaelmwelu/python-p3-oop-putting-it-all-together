#!/usr/bin/env python3

class Shoe:
    pass
class Shoe:
   def __init__(self, brand, size):
      self.size= size 
      self.brand= brand
      
      import io
import sys
import unittest
from shoe import Shoe

class TestShoeMethods(unittest.TestCase):
    def test_requires_int_size(self):
        '''prints "size must be an integer" if size is not an integer.'''
        stan_smith = Shoe("Adidas", 9)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        stan_smith.size = "not an integer"
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "size must be an integer\n")

if __name__ == '__main__':
    unittest.main()


      

       