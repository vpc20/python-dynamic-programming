from random import randrange
from unittest import TestCase

from RandomData import random_int_array
from SubsetSum import is_subset_sum_naive, is_subset_sum_dyna, is_subset_sum_recur


class TestIsSubsetSum(TestCase):
    def test_is_subset_sum_dyna(self):
        for _ in range(1000):
            arr = random_int_array(20, 20)
            n = randrange(100)
            print(arr, n)
            print(is_subset_sum_naive(arr, n))
            self.assertEqual(is_subset_sum_naive(arr, n), is_subset_sum_dyna(arr, n))

    def test_is_subset_sum_recur(self):
        for _ in range(1000):
            arr = random_int_array(20, 20)
            n = randrange(100)
            print(arr, n)
            print(is_subset_sum_naive(arr, n))
            self.assertEqual(is_subset_sum_naive(arr, n), is_subset_sum_recur(arr, n))
