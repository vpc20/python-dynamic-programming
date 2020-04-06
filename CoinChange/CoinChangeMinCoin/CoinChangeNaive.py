from itertools import combinations_with_replacement


# def coin_change_naive(coin_list, change):
#     min_coins = int(change / min(coin_list))
#     for i in range(1, min_coins):
#         for comb in combinations_with_replacement(coin_list, i):
#             if sum(comb) == change:
#                 print(comb)
#                 if len(comb) < min_coins:
#                     min_coins = len(comb)
#     return min_coins


def coin_change_naive(coin_list, change):
    if change == 0:
        return 0, []
    for i in range(1, int(change / min(coin_list)) + 1):
        for comb in combinations_with_replacement(coin_list, i):
            if sum(comb) == change:
                return i, list(comb)
    return 0, []  # coin change not possible


if __name__ == '__main__':
    # print(coin_change_naive([25, 10, 5, 1], 27))
    print(coin_change_naive([25, 10, 5], 0))
    print(coin_change_naive([50, 25, 10, 5, 1], 1))
    print(coin_change_naive([1, 2, 5], 5))
    print(coin_change_naive([50, 25, 10, 5], 36))  # not possible
