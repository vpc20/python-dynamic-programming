# def coin_change_recur(coin_list, change):
#     min_coins = change
#     for coin in coin_list:
#         if change >= coin:
#             num_coins = 1 + coin_change_recur(coin_list, change - coin)
#             min_coins = min(min_coins, num_coins)
#     return min_coins

# def coin_change_recur(coin_list, change):
#     def _coin_change_recur(coin_list, change):
#         nonlocal change_ok
#         if change == 0:
#             change_ok = True
#             return 0
#         min_coins = change
#         for coin in coin_list:
#             if change >= coin:
#                 num_coins = 1 + _coin_change_recur(coin_list, change - coin)
#                 min_coins = min(min_coins, num_coins)
#         return min_coins
#
#     change_ok = False
#     minval = _coin_change_recur(coin_list, change)
#     return minval if change_ok else 0  # return 0 if not possible to make change


# def coin_change_recur(coin_list, change):  # memoized
#     def _coin_change_recur(coin_list, change):
#         nonlocal change_ok
#         if change == 0:
#             change_ok = True
#             return 0
#         if change in cache:
#             return cache[change]
#         min_coins = change
#         for coin in coin_list:
#             if change >= coin:
#                 num_coins = 1 + _coin_change_recur(coin_list, change - coin)
#                 min_coins = min(min_coins, num_coins)
#         cache[change] = min_coins
#         return min_coins
#
#     change_ok = False
#     cache = {}
#     minval = _coin_change_recur(coin_list, change)
#     return minval if change_ok else 0  # return 0 if not possible to make change


def coin_change_recur(coin_list, change):  # memoized, build coin_arr
    def _coin_change_recur(coin_list, change):
        nonlocal change_ok
        if change == 0:
            change_ok = True
            return 0
        if change in cache:
            return cache[change]
        min_coins = change
        for coin in coin_list:
            if change >= coin:
                num_coins = 1 + _coin_change_recur(coin_list, change - coin)
                # min_coins = min(min_coins, num_coins)
                if num_coins <= min_coins:
                    min_coins = num_coins
                    coin_arr[change] = coin_arr[change - coin] + [coin]
        cache[change] = min_coins
        return min_coins

    change_ok = False
    cache = {}
    coin_arr = [[] for _ in range(change + 1)]
    minval = _coin_change_recur(coin_list, change)
    # print(coin_arr)
    # return minval if change_ok else 0  # return 0 if not possible to make change
    return (minval, coin_arr[change]) if change_ok else (0, [])  # return 0 if not possible to make change


# def coin_change_recur(coin_list, change, min_coin_arr=[]):
#     min_coins = change
#     for coin in coin_list:
#         if change >= coin:
#             min_coin_arr.append(coin)
#             num_coins = 1 + coin_change_recur(coin_list, change - coin, min_coin_arr)
#             if num_coins < min_coins:
#                 min_coins = num_coins
#                 print(min_coin_arr)
#     return min_coins


# def coin_change_dyna_recur(coin_list, change, computed_min_coins={}):
#     if change in computed_min_coins:
#         return computed_min_coins[change]
#
#     min_coins = change
#     for coin in coin_list:
#         if change >= coin:
#             num_coins = 1 + coin_change_dyna_recur(coin_list, change - coin)
#             if num_coins < min_coins:
#                 min_coins = num_coins
#                 computed_min_coins[change] = min_coins
#     return min_coins


if __name__ == '__main__':
    # print(coin_change_dyna_recur([1, 5, 10, 25], 0))
    # print(coin_change_recur([1, 2, 5], 8))
    # print(coin_change_recur([1, 5, 10, 25, 50], 40))

    # print(coin_change_recur([1], 1))
    # print(coin_change_recur([1], 2))
    # print(coin_change_recur([1], 3))
    # print(coin_change_recur([1], 4))
    # print(coin_change_recur([1], 5))
    # print(coin_change_recur([1], 6))
    # print(coin_change_recur([1], 7))
    # print(coin_change_recur([1], 8))
    # print(coin_change_recur([1], 9))
    # print(coin_change_recur([1], 10))
    # print(coin_change_recur([1], 11))
    # print(coin_change_recur([1], 12))

    # print(coin_change_recur([5], 5))

    # print(coin_change_recur([1, 5, 10, 25, 50], 43))
    # print(coin_change_recur([5, 10, 25, 50], 43))  # not possible
    # print(coin_change_recur([1], 1))
    # print(coin_change_recur([1, 2, 5], 5))
    # print(coin_change_recur([1], 4))

    # print(coin_change_recur([1, 5, 10, 25], 63))
    # print(coin_change_dyna_recur([1, 2, 5], 8))
    # print(coin_change_dyna_recur([1, 5, 10, 25], 63))
    # print(coin_change_dyna_recur([1, 5, 10, 25, 21], 63))
    #
    # for i in range(30):
    #     print(coin_change_recur([1, 5, 10, 25], i))
    # print(coin_change_dyna_recur([1, 5, 10, 25], 1000))

    # print(coin_change_recur([1, 2, 5], 3))
    # print(coin_change_recur([50, 25, 10, 5, 1], 5))
    # print(coin_change_recur([50, 25, 10, 5, 1], 2))
    # print(coin_change_recur([1, 2, 4], 5))
    # print(coin_change_recur([2, 5], 3))
    print(coin_change_recur([50, 25, 10, 5, 1], 5))
    print(coin_change_recur([50, 25, 10, 5, 1], 1))
