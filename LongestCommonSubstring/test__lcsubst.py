from unittest import TestCase

from LongestCommonSubstring.LCSSubstNaive import lcsubst_naive
from LongestCommonSubstring.LCSubstIterative import lcsubst_iter
from LongestCommonSubstring.LCSubstRecursive import lcsubst_recur
from RandomData import random_string


class TestLCSubstRecur(TestCase):
    def test__lcsubst_recur(self):
        for _ in range(1000):
            s1 = random_string(10)
            s2 = random_string(10)
            print(s1, s2)
            self.assertEqual(lcsubst_naive(s1, s2), lcsubst_recur(s1, s2))

    def test__lcsubst_iter(self):
        for _ in range(1000):
            s1 = random_string(10)
            s2 = random_string(10)
            print(s1, s2)
            self.assertEqual(lcsubst_naive(s1, s2), lcsubst_iter(s1, s2))
