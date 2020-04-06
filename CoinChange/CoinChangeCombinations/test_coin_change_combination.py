from unittest import TestCase
from CoinChange.CoinChangeCombinations.CoinChangeCombinations import coin_change_combination
from CoinChange.CoinChangeCombinations.CoinChangeRecursive import coin_change_recur
from CoinChange.CoinChangeCombinations.CoinChangeDynamic import coin_change_dyna_iter


class TestCoinChangeCombinations(TestCase):
    def test_coin_change_recur(self):
        for change in range(41):
            self.assertEqual(coin_change_combination([1, 5, 10, 25, 50], change),
                             coin_change_recur([1, 5, 10, 25, 50], change))

    def test_coin_change_dyna_iter(self):
        for change in range(101):
            self.assertEqual(coin_change_recur([1, 5, 10, 25, 50], change),
                             coin_change_dyna_iter([1, 5, 10, 25, 50], change))
