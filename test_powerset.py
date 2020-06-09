from unittest import TestCase

from PowerSet import powerset_naive, powerset_iter, powerset_recur
from RandomData import random_int_array


class TestPowerset(TestCase):
    def test_powerset_iter(self):
        for _ in range(1000):
            arr = random_int_array(15, 1000)
            print(arr)
            self.assertEqual(sorted(powerset_naive(arr)), sorted(powerset_iter(arr)))

    def test_powerset_recur(self):
        for _ in range(1000):
            arr = random_int_array(15, 1000)
            print(arr)
            self.assertEqual(sorted(powerset_naive(arr)), sorted(list(powerset_recur(arr))))
