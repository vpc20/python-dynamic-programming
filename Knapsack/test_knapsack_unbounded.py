import random
from unittest import TestCase

from Knapsack.KnapsackUnboundedIter import knapsack_unbounded_iter
from Knapsack.KnapsackUnboundedNaive import knapsack_unbounded_naive
from Knapsack.KnapsackUnboundedRecursive import knapsack_unbounded_recur
from random_data import random_int_array


class TestKnapsackUnbounded(TestCase):
    def test_knapsack_unbounded_iter(self):
        wts = [1, 2, 3]
        vals = [50, 110, 160]
        for wt_limit in range(1, 10):
            self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                             knapsack_unbounded_iter(wts, vals, wt_limit))

        wts = [1, 1, 2, 4, 12]
        vals = [1, 2, 2, 10, 4]
        for wt_limit in range(1, 20):
            self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                             knapsack_unbounded_iter(wts, vals, wt_limit))

        wts = [2, 3, 5]
        vals = [50, 100, 140]
        for wt_limit in range(1, 20):
            self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                             knapsack_unbounded_iter(wts, vals, wt_limit))

        for _ in range(100):
            # wts = list(set(random_int_array(10, 15)))
            wts = random_int_array(10, 15)
            if wts:
                vals = [random.randrange(1, 15) for _ in range(len(wts))]
                for wt_limit in range(1, max(wts)):
                    print(wts, vals, wt_limit)
                    print(knapsack_unbounded_iter(wts, vals, wt_limit))
                    self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                                     knapsack_unbounded_iter(wts, vals, wt_limit))


    def test_knapsack_unbounded_recur(self):
        wts = [1, 2, 3]
        vals = [50, 110, 160]
        for wt_limit in range(1, 10):
            self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                             knapsack_unbounded_recur(wts, vals, wt_limit))

        wts = [1, 1, 2, 4, 12]
        vals = [1, 2, 2, 10, 4]
        for wt_limit in range(1, 20):
            self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                             knapsack_unbounded_recur(wts, vals, wt_limit))

        wts = [2, 3, 5]
        vals = [50, 100, 140]
        for wt_limit in range(1, 20):
            self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                             knapsack_unbounded_recur(wts, vals, wt_limit))

        for _ in range(100):
            # wts = list(set(random_int_array(10, 15)))
            wts = random_int_array(10, 15)
            if wts:
                vals = [random.randrange(1, 15) for _ in range(len(wts))]
                for wt_limit in range(1, max(wts)):
                    print(wts, vals, wt_limit)
                    print(knapsack_unbounded_recur(wts, vals, wt_limit))
                    self.assertEqual(knapsack_unbounded_naive(wts, vals, wt_limit),
                                     knapsack_unbounded_recur(wts, vals, wt_limit))
