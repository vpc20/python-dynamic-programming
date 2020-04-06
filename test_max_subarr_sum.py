from unittest import TestCase
from MaximumSubarraySum import max_subarr_sum_naive, max_subarr_sum,max_subarr_sum_dyna,max_subarr_sum_recur
from random_data import random_int_array_neg


class TestMaxSubarrSum(TestCase):
    def test_max_subarr_sum(self):
        for _ in range(1000):
            arr = random_int_array_neg(20, 100)
            print(arr)
            self.assertEqual(max_subarr_sum_naive(arr), max_subarr_sum(arr))

    def test_max_subarr_sum_dyna(self):
        for _ in range(1000):
            arr = random_int_array_neg(20, 100)
            print(arr)
            self.assertEqual(max_subarr_sum_naive(arr), max_subarr_sum_dyna(arr))

    def test_max_subarr_sum_recur(self):
        for _ in range(1000):
            arr = random_int_array_neg(20, 100)
            print(arr)
            self.assertEqual(max_subarr_sum_naive(arr), max_subarr_sum_recur(arr))
