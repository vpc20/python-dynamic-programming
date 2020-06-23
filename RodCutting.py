# The rod-cutting problem is the following. Given a rod of length n inches and a
# table of prices pi for i D 1; 2; : : : ; n, determine the maximum revenue rn
# obtainable by cutting up the rod and selling the pieces.
# Note that if the price pn for a rod # of length n is large enough, an
# optimal solution may require no cutting at all.

# Consider the case when n = 4. Figure 15.2 shows all the ways to cut up a rod
# of 4 inches in length, including the way with no cuts at all. We see that cutting a
# 4-inch rod into two 2-inch pieces produces revenue p2 + p2 = 5 + 5 = 10, which
# is optimal.
#
# length i   1 2 3 4 5  6  7  8  9  10
# price  pi  1 5 8 9 10 17 17 20 24 30

#            ┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
#  length i  │  1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │  9 │ 10 │
#            ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
#  price  pi │  1 │  5 │  8 │  9 │ 10 │ 17 │ 17 │ 20 │ 24 │ 30 │
#            └────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
import sys
from itertools import combinations_with_replacement


# def cut_rod_naive(prices, rod_len):
#     maxprc = 0
#     maxcomb = ()
#     lengths = [i for i in range(1, len(prices) + 1)]
#     for r in range(1, rod_len + 1):
#         for comb in combinations_with_replacement(lengths, r):
#             if sum(comb) == rod_len:
#                 total_price = sum([prices[i - 1] for i in comb])
#                 if total_price > maxprc:
#                     # print(comb, total_price)
#                     maxprc = total_price
#                     maxcomb = comb
#     return maxprc  # , maxcomb


def cut_rod_naive(prices, l):
    maxprc = 0
    lengths = [i for i in range(1, len(prices) + 1)]
    for r in range(1, l + 1):
        for comb in combinations_with_replacement(lengths, r):
            if sum(comb) == l:
                totprc = sum([prices[i - 1] for i in comb])
                maxprc = max(maxprc, totprc)
    return maxprc


# def cut_rod_recur(prices, rod_len):
#     if rod_len == 0:
#         return 0
#     max_price = -sys.maxsize
#     for i in range(1, rod_len + 1):
#         max_price = max(max_price, prices[i - 1] + cut_rod_recur(prices, rod_len - i))
#     return max_price


def cut_rod_recur(prices, rod_len):
    def cut_rod(prices, rod_len):
        nonlocal maxprc
        if not prices or rod_len == 0:
            return 0
        if rod_len >= len(prices):
            totprc = max(cut_rod(prices[:-1], rod_len),
                         prices[-1] + cut_rod(prices, rod_len - len(prices)))
        else:
            totprc = cut_rod(prices[:-1], rod_len)
        maxprc = max(maxprc, totprc)
        return totprc

    maxprc = -sys.maxsize
    cut_rod(prices, rod_len)
    return maxprc


# def cut_rod_recur_dyna(prices, rod_len):
#     def _cut_rod_recur_dyna(prices, rod_len):
#         if rod_len == 0:
#             return 0
#         if rod_len in dp_cache:
#             return dp_cache[rod_len]
#         max_price = -sys.maxsize
#         for i in range(1, rod_len + 1):
#             computed_price = prices[i - 1] + _cut_rod_recur_dyna(prices, rod_len - i)
#             max_price = max(max_price, computed_price)
#             dp_cache[rod_len] = computed_price
#         return max_price
#
#     dp_cache = {}
#     return _cut_rod_recur_dyna(prices, rod_len)


# def cut_rod_dyna(prices, rod_len): # cormen book solution
#     dp_arr = [0] * (rod_len + 1)
#     # print(dp_arr)
#     for i in range(1, rod_len + 1):
#         q = -sys.maxsize
#         for j in range(1, i + 1):
#             q = max(q, prices[j - 1] + dp_arr[i - j])
#         dp_arr[i] = q
#         # print(dp_arr)
#     return dp_arr[rod_len]


def cut_rod_dyna(prices, l):
    dp = [[0] * (l + 1) for _ in range(len(prices) + 1)]
    maxprc = -sys.maxsize
    for i in range(1, len(prices) + 1):
        for j in range(1, l + 1):
            if j >= i:
                dp[i][j] = max(dp[i - 1][j], prices[i - 1] + dp[i][j - i])
            else:
                dp[i][j] = dp[i - 1][j]
            maxprc = max(maxprc, dp[i][j])
    print(dp)
    return maxprc


# def cut_rod_dyna(prices, l):  # simplified version
#     dp = [0] * (l + 1)
#     maxprc = -sys.maxsize
#     for i in range(1, len(prices) + 1):
#         for j in range(1, l + 1):
#             if j >= i:
#                 dp[j] = max(dp[j], prices[i - 1] + dp[j - i])
#             maxprc = max(maxprc, dp[j])
#     return maxprc


if __name__ == '__main__':
    prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # assert cut_rod_naive(prices, 1) == cut_rod_recur(prices, 1)
    # assert cut_rod_naive(prices, 2) == cut_rod_recur(prices, 2)
    # assert cut_rod_naive(prices, 3) == cut_rod_recur(prices, 3)
    # assert cut_rod_naive(prices, 4) == cut_rod_recur(prices, 4)
    # assert cut_rod_naive(prices, 5) == cut_rod_recur(prices, 5)
    # assert cut_rod_naive(prices, 6) == cut_rod_recur(prices, 6)
    # assert cut_rod_naive(prices, 7) == cut_rod_recur(prices, 7)
    # assert cut_rod_naive(prices, 8) == cut_rod_recur(prices, 8)
    #
    # assert cut_rod_naive(prices, 1) == cut_rod_dyna(prices, 1)
    # assert cut_rod_naive(prices, 2) == cut_rod_dyna(prices, 2)
    # assert cut_rod_naive(prices, 3) == cut_rod_dyna(prices, 3)
    # assert cut_rod_naive(prices, 4) == cut_rod_dyna(prices, 4)
    # assert cut_rod_naive(prices, 5) == cut_rod_dyna(prices, 5)
    # assert cut_rod_naive(prices, 6) == cut_rod_dyna(prices, 6)
    # assert cut_rod_naive(prices, 7) == cut_rod_dyna(prices, 7)
    # assert cut_rod_naive(prices, 8) == cut_rod_dyna(prices, 8)

    print(cut_rod_dyna(prices, 4))

#      0   1   2   3    4
#    ┌───┬───┬───┬───┬────┐
#  0 │ 0 │ 0 │ 0 │ 0 │  0 │
#    ├───┼───┼───┼───┼────┤
#  1 │ 0 │ 1 │ 2 │ 3 │  4 │
#    ├───┼───┼───┼───┼────┤
#  2 │ 0 │ 1 │ 5 │ 6 │ 10 │
#    ├───┼───┼───┼───┼────┤
#  3 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    ├───┼───┼───┼───┼────┤
#  4 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    ├───┼───┼───┼───┼────┤
#  5 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    ├───┼───┼───┼───┼────┤
#  6 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    ├───┼───┼───┼───┼────┤
#  7 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    ├───┼───┼───┼───┼────┤
#  8 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    ├───┼───┼───┼───┼────┤
#  9 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    ├───┼───┼───┼───┼────┤
# 10 │ 0 │ 1 │ 5 │ 8 │ 10 │
#    └───┴───┴───┴───┴────┘


# prices_arr = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24,  # 0X's
#               30, 32, 35, 39, 43, 43, 45, 49, 50, 54,  # 1X's
#               57, 60, 65, 68, 70, 74, 80, 81, 84, 85,  # 2X's
#               87, 91, 95, 99, 101, 104, 107, 112, 115, 116,  # 3X's
#               119]  # 40th element
#
# print(cut_rod_dyna(prices_arr, 1))
