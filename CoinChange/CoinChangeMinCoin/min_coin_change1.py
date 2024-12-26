# Same as MinCoinChange but will also return the coins making up the minimum change
from itertools import combinations_with_replacement


def min_coin_change(coins, change):
    dp_arr = [0] + [change] * change
    coins_arr = [[] for _ in range(change + 1)]
    for amt in range(1, change + 1):
        for coin in coins:
            if amt >= coin:
                if 1 + dp_arr[amt - coin] < dp_arr[amt]:
                    dp_arr[amt] = 1 + dp_arr[amt - coin]
                    coins_arr[amt] = [coin] + coins_arr[amt - coin]
    return dp_arr[-1], coins_arr[-1]


def min_coin_change_naive(coins, change):
    if change == 0:
        return 0, []
    min_coins = change
    coins_arr = []
    for r in range(1, change + 1):
        for comb in combinations_with_replacement(coins, r):
            if sum(comb) == change:
                if len(comb) < min_coins:
                    min_coins = len(comb)
                    coins_arr = list(comb)
    return min_coins, coins_arr


print(min_coin_change([1, 2, 5], 11))
print(min_coin_change_naive([1, 2, 5], 11))
