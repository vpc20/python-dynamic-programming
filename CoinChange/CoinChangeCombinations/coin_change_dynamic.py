# def coin_change_dyna_iter(coin_list, change):
#     arr = [[1] + [0] * change for _ in range(len(coin_list) + 1)]
#     for i in range(1, len(coin_list) + 1):
#         for j in range(1, change + 1):
#             if j >= coin_list[i-1]:
#                 arr[i][j] = arr[i - 1][j] + arr[i][j - coin_list[i-1]]
#             else:
#                 arr[i][j] = arr[i - 1][j]
#     for e in arr:
#         print(e)
#     return arr[-1][-1]


# def coin_change_dyna_iter(coin_list, change):
#     arr = [1] + [0] * change
#     # print(arr)
#     for coin in coin_list:
#         for chg in range(1, change + 1):
#             if chg >= coin:
#                 arr[chg] += arr[chg - coin]
#         # print(arr)
#     return arr[-1]


def coin_change_dyna_iter(coins, change):
    dp_arr = [1] + [0] * change
    coin_arr = [[[]]] + [[] for _ in range(change)]
    print(dp_arr)
    # print(coin_arr)
    # print('')
    for coin in coins:
        for chg in range(1, change + 1):
            if chg >= coin:
                dp_arr[chg] += dp_arr[chg - coin]
                for prev in coin_arr[chg - coin]:  # prev coin arr list could have several lists
                    coin_arr[chg].append(prev + [coin])
                # print(dp_arr)
                # print(coin_arr)
                # print('')
        print(dp_arr)
    # print(coin_arr)
    # for e in coin_arr:
    #     print(e)
    return dp_arr[-1] #, coin_arr[-1]


if __name__ == '__main__':
    # print(coin_change_dyna_iter([1, 2, 3], 4))
    # print(coin_change_dyna_iter([2, 5, 3, 6], 10))
    # print(coin_change_dyna_iter([1, 2, 5], 12))
    # print(coin_change_dyna_iter([1, 5, 10, 25], 63))

    # print(coin_change_dyna_iter([1, 2, 5], 5))
    #    0  1  2  3  4  5
    #   [1, 0, 0, 0, 0, 0]
    # 1 [1, 1, 1, 1, 1, 1]
    # 2 [1, 1, 2, 2, 3, 3]
    # 5 [1, 1, 2, 2, 3, 4]

    print(coin_change_dyna_iter([1, 2, 5], 5))
    #     0   1   2   3   4   5
    #   ┌───┬───┬───┬───┬───┬───┐
    # 0 │ 1 │ 0 │ 0 │ 0 │ 0 │ 0 │
    #   ├───┼───┼───┼───┼───┼───┤
    # 1 │ 1 │ 1 │ 1 │ 1 │ 1 │ 1 │
    #   ├───┼───┼───┼───┼───┼───┤
    # 2 │ 1 │ 1 │ 2 │ 2 │ 3 │ 3 │
    #   ├───┼───┼───┼───┼───┼───┤
    # 5 │ 1 │ 1 │ 2 │ 2 │ 3 │ 4 │
    #   └───┴───┴───┴───┴───┴───┘
