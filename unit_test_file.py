# coding: utf-8

import unittest

from std1 import *

class unit_test(unittest.TestCase):
    def test_Sum(self):
        self.assertEqual(Sum(1, 2, 5),  8)

    def test_Multiplying(self):
        self.assertEqual(Multiply(1, 4, 5), 20)

    def test_fibb(self):
        self.assertEqual(fibonacci(5), 5)

if __name__ == '__main__':
    unittest.main()
