from unittest import TestCase
from CoinChange.CoinChangeMinCoin.CoinChangeRecursive import coin_change_recur
from CoinChange.CoinChangeMinCoin.CoinChangeIterative import coin_change_iter
from CoinChange.CoinChangeMinCoin.CoinChangeGreedyIteractive import coin_change_greedy_iter
from CoinChange.CoinChangeMinCoin.CoinChangeGreedyRecursive import coin_change_greedy_recur
from CoinChange.CoinChangeMinCoin.CoinChangeNaive import coin_change_naive


class TestCoinChangeMincoin(TestCase):
    def test_coin_change_recursive(self):
        for change in range(100):
            self.assertEqual(coin_change_naive([50, 25, 10, 5, 1], change),
                             coin_change_recur([50, 25, 10, 5, 1], change))
        for change in range(100):
            self.assertEqual(coin_change_naive([50, 25, 10, 5], change),
                             coin_change_recur([50, 25, 10, 5], change))

    def test_coin_change_iterative(self):
        for change in range(100):
            self.assertEqual(coin_change_iter([50, 25, 10, 5, 1], change),
                             coin_change_recur([50, 25, 10, 5, 1], change))
        for change in range(100):
            self.assertEqual(coin_change_iter([50, 25, 10, 5], change),
                             coin_change_recur([50, 25, 10, 5], change))

    def test_coin_change_greedy(self):
        for change in range(101):
            self.assertEqual(coin_change_greedy_iter([50, 25, 10, 5, 1], change),
                             coin_change_greedy_recur([50, 25, 10, 5, 1], change))

        for change in range(101):
            # print(coin_change_greedy_iter([50, 25, 10, 5], change))
            self.assertEqual(coin_change_greedy_iter([50, 25, 10, 5], change),
                             coin_change_greedy_recur([50, 25, 10, 5], change))
