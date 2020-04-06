# Given a value N, if we want to make change for N cents, and we have infinite supply
# of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?
# The order of coins doesn’t matter.
#
# For example, for N = 4 and S = {1,2,3},
# there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
#
# For N = 10 and S = {2, 5, 3, 6},
# there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
# So the output should be 5.

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n


# def coin_change(coin_list, m, change):
#     # If n is 0 then there is 1
#     # solution (do not include any coin)
#     if change == 0:
#         return 1
#
#     # If n is less than 0 then no
#     # solution exists
#     if change < 0:
#         return 0
#
#     # If there are no coins and n
#     # is greater than 0, then no
#     # solution exist
#     if m <= 0 and change >= 1:
#         return 0
#
#     # count is sum of solutions (i)
#     # including S[m-1] (ii) excluding S[m-1]
#     return coin_change(coin_list, m - 1, change) + coin_change(coin_list, m, change - coin_list[m - 1])


# def coin_change(coin_list, list_size, change):
#     if change == 0:
#         return 1
#     elif change < 0:
#         return 0
#     elif list_size <= 0:
#         return 0
#     return coin_change(coin_list, list_size - 1, change) \
#         + coin_change(coin_list, list_size, change - coin_list[list_size - 1])


# def coin_change_recur(coin_list, change):
#     # print(coin_list, change)
#     if change == 0:
#         return 1
#     if change < 0:
#         return 0
#     if not coin_list:
#         return 0
#     return coin_change_recur(coin_list[:-1], change) + coin_change_recur(coin_list, change - coin_list[-1])


# def coin_change_recur(coin_list, change):
#     # print(coin_list, change)
#     if change == 0:
#         return 1
#     if change < 0:
#         return 0
#     if not coin_list:
#         return 0
#     # excluding coin[-1] + including coin[-1]
#     return coin_change_recur(coin_list[:-1], change) \
#         + coin_change_recur(coin_list, change - coin_list[-1])


def coin_change_recur(coin_list, change):
    # print(coin_list, change)
    if change == 0:
        return 1
    if change < 0:
        return 0
    if not coin_list:
        return 0
    # excluding coin[-1] + including coin[-1]
    if change >= coin_list[-1]:
        return coin_change_recur(coin_list[:-1], change) \
               + coin_change_recur(coin_list, change - coin_list[-1])
    else:
        return coin_change_recur(coin_list[:-1], change)

# def coin_change_dyna_recur(coin_list, change, results={}):
# print(coin_list, change)
# if change == 0:
#     return 1
# if change < 0:
#     return 0
# if not coin_list:
#     return 0
# results[change] = coin_change_recur(coin_list[1:], change) \
#     + coin_change_recur(coin_list, change - coin_list[0])
# return results[change]


if __name__ == '__main__':
    # print(coin_change_recur([1, 2, 3], 4))
    # print(coin_change_recur([2, 3, 5, 6], 10))
    # print(coin_change_recur([1, 2, 5], 12))
    # print(coin_change_recur([1, 5, 10, 25], 63))

    print(coin_change_recur([1, 2, 5], 5))
    #    0  1  2  3  4  5
    #   [1, 0, 0, 0, 0, 0]
    # 1 [1, 1, 1, 1, 1, 1]
    # 2 [1, 1, 2, 2, 3, 3]
    # 5 [1, 1, 2, 2, 3, 4]
