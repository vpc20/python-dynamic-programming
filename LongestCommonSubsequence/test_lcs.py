from unittest import TestCase

from LongestCommonSubsequence.LCSIterative import lcs_iter
from LongestCommonSubsequence.LCSNaive import is_subsequence, subsequence
from LongestCommonSubsequence.LCSNaive import lcs_naive
from LongestCommonSubsequence.LCSRecursive import lcs_recur
from RandomData import random_string


class TestLcs(TestCase):
    def test_is_subsequence(self):
        for _ in range(1000):
            s1 = random_string(10)
            print(s1)
            for sub in subsequence(s1):
                self.assertEqual(True, is_subsequence(sub, s1))

    def test_lcs_iterative(self):
        for _ in range(1000):
            s1 = random_string(10)
            s2 = random_string(10)
            # print(s1, s2)
            # print(lcs_comb(s1, s2))
            # print(lcs_iter(s1, s2))
            self.assertEqual(lcs_naive(s1, s2), lcs_iter(s1, s2))

    def test_lcs_recursive(self):
        for _ in range(1000):
            s1 = random_string(10)
            s2 = random_string(10)
            # print(s1, s2)
            # print(lcs_naive(s1, s2))
            # print(lcs_recur(s1, s2))
            self.assertEqual(lcs_naive(s1, s2), lcs_recur(s1, s2))
