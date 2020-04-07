from unittest import TestCase

from CoinChange.CoinChangeMinCoin.MinCoinChange import min_coin_change, min_coin_change_naive, min_coin_change_recur


class Test(TestCase):
    def test_min_coin_change(self):
        for change in range(50):
            self.assertEqual(min_coin_change_naive([50, 25, 10, 5, 1], change),
                             min_coin_change([50, 25, 10, 5, 1], change))

    def test_min_coin_change_recur(self):
        for change in range(50):
            self.assertEqual(min_coin_change_naive([50, 25, 10, 5, 1], change),
                             min_coin_change_recur([50, 25, 10, 5, 1], change))
