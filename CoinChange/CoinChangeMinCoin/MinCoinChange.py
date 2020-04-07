# Given a set of coins, find the minimum number of coins needed to produce the change amount

import sys
from itertools import combinations_with_replacement


def min_coin_change(coins, change):
    dp_arr = [0] + [change] * change
    for amt in range(1, change + 1):
        for coin in coins:
            if amt >= coin:
                dp_arr[amt] = min(dp_arr[amt], 1 + dp_arr[amt - coin])
    return dp_arr[-1]


def min_coin_change_recur(coins, change):
    if change <= 0:
        return 0
    minval = change
    for coin in coins:
        if change >= coin:
            minval = min(minval, 1 + min_coin_change_recur(coins, change - coin))
    return minval


def min_coin_change_naive(coins, change):
    if change == 0:
        return 0
    min_coins = change
    for r in range(1, change + 1):
        for comb in combinations_with_replacement(coins, r):
            if sum(comb) == change:
                min_coins = min(min_coins, len(comb))
    return min_coins


if __name__ == '__main__':
    print(min_coin_change([1, 2, 5], 11))
    print(min_coin_change_recur([1, 2, 5], 11))
    print(min_coin_change_naive([1, 2, 5], 11))
    # print(min_coin_change_naive([50, 25, 10, 5, 1], 19))

# coins = [1, 2, 5]
# for i in range(12):
#     print(min_coin_change(coins, i),min_coin_change_recur(coins, i),min_coin_change_naive(coins, i))


# min_coin_change([1, 2, 5], 11)
#      0   1    2    3    4    5    6    7    8    9   10   11
#    ┌───┬───┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
#  1 │ 0 │ 1 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  2 │ 0 │ 1 │  1 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  3 │ 0 │ 1 │  1 │  2 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  4 │ 0 │ 1 │  1 │  2 │  2 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  5 │ 0 │ 1 │  1 │  2 │  2 │  1 │ 11 │ 11 │ 11 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  6 │ 0 │ 1 │  1 │  2 │  2 │  1 │  2 │ 11 │ 11 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  7 │ 0 │ 1 │  1 │  2 │  2 │  1 │  2 │  2 │ 11 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  8 │ 0 │ 1 │  1 │  2 │  2 │  1 │  2 │  2 │  3 │ 11 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  9 │ 0 │ 1 │  1 │  2 │  2 │  1 │  2 │  2 │  3 │  3 │ 11 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
# 10 │ 0 │ 1 │  1 │  2 │  2 │  1 │  2 │  2 │  3 │  3 │  2 │ 11 │
#    ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
# 11 │ 0 │ 1 │  1 │  2 │  2 │  1 │  2 │  2 │  3 │  3 │  2 │  3 │
#    └───┴───┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
