from unittest import TestCase
from LongestIncreasingSubsequence.LISNaive import lis_naive
from LongestIncreasingSubsequence.LISIter import lis_iter
from LongestIncreasingSubsequence.LISRecur import lis_recur
from random_data import random_int_array_neg


class TestLis(TestCase):
    def test_lis_iter(self):
        self.assertEqual(lis_naive([1]), lis_iter([1]))
        self.assertEqual(lis_naive([1, 2]), lis_iter([1, 2]))
        self.assertEqual(lis_naive([1, 2, 3]), lis_iter([1, 2, 3]))
        self.assertEqual(lis_naive([1, 2, 3, 4]), lis_iter([1, 2, 3, 4]))
        self.assertEqual(lis_naive([2, 1]), lis_iter([2, 1]))
        self.assertEqual(lis_naive([3, 2, 1]), lis_iter([3, 2, 1]))
        self.assertEqual(lis_naive([4, 3, 2, 1]), lis_iter([4, 3, 2, 1]))
        self.assertEqual(lis_naive([4, 2, 1, 3]), lis_iter([4, 2, 1, 3]))
        self.assertEqual(lis_naive([2, 4, 1, 3]), lis_iter([2, 4, 1, 3]))

        for _ in range(1000):
            arr = random_int_array_neg(10, 1000)
            print('arr', arr)
            self.assertEqual(lis_naive(arr), lis_iter(arr))

    def test_lis_recur(self):
        self.assertEqual(lis_naive([1]), lis_recur([1]))
        self.assertEqual(lis_naive([1, 2]), lis_recur([1, 2]))
        self.assertEqual(lis_naive([1, 2, 3]), lis_recur([1, 2, 3]))
        self.assertEqual(lis_naive([1, 2, 3, 4]), lis_recur([1, 2, 3, 4]))
        self.assertEqual(lis_naive([2, 1]), lis_recur([2, 1]))
        self.assertEqual(lis_naive([3, 2, 1]), lis_recur([3, 2, 1]))
        self.assertEqual(lis_naive([4, 3, 2, 1]), lis_recur([4, 3, 2, 1]))
        self.assertEqual(lis_naive([4, 2, 1, 3]), lis_recur([4, 2, 1, 3]))
        self.assertEqual(lis_naive([2, 4, 1, 3]), lis_recur([2, 4, 1, 3]))

        for _ in range(1000):
            arr = random_int_array_neg(10, 1000)
            print('arr', arr)
            self.assertEqual(lis_naive(arr), lis_recur(arr))
