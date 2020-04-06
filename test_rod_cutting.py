from unittest import TestCase

from RodCutting import cut_rod_naive, cut_rod_dyna, cut_rod_recur


class TestCutRod(TestCase):
    def test_cut_rod_dyna(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        # prices = [1, 5]
        for rod_len in range(1, 15):
            self.assertEqual(cut_rod_naive(prices, rod_len), cut_rod_dyna(prices, rod_len))

    def test_cut_rod_recur(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        # prices = [1, 5]
        for rod_len in range(1, 15):
            self.assertEqual(cut_rod_naive(prices, rod_len), cut_rod_recur(prices, rod_len))
