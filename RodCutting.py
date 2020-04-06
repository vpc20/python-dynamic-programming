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


def cut_rod_naive(prices, rod_len):
    max_price = 0
    max_comb = ()
    for r in range(1, rod_len + 1):
        for comb in combinations_with_replacement([i for i in range(1, len(prices) + 1)], r):
            if sum(comb) == rod_len:
                total_price = 0
                for i in comb:
                    total_price += prices[i - 1]
                if total_price > max_price:
                    # print(comb, total_price)
                    max_price = total_price
                    max_comb = comb
    return max_price  # , max_comb


# def cut_rod_recur(prices, rod_len):
#     if rod_len == 0:
#         return 0
#     max_price = -sys.maxsize
#     for i in range(1, rod_len + 1):
#         max_price = max(max_price, prices[i - 1] + cut_rod_recur(prices, rod_len - i))
#     return max_price


def cut_rod_recur(prices, rod_len):
    def _cut_rod_recur(prices, rod_len):
        nonlocal max_price
        if not prices or rod_len == 0:
            return 0
        if rod_len >= len(prices):
            tot_price = max(_cut_rod_recur(prices[:-1], rod_len),
                            prices[-1] + _cut_rod_recur(prices, rod_len - len(prices)))
        else:
            tot_price = _cut_rod_recur(prices[:-1], rod_len)
        max_price = max(max_price, tot_price)
        return tot_price

    max_price = -sys.maxsize
    _cut_rod_recur(prices, rod_len)
    return max_price


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


# def cut_rod_recur(prices, rod_len): #incorrect
#     # max_price = 0
#     max_set = []
#
#     def _cut_rod_recur(prices, rod_len):
#         # print(prices, rod_len)
#         if rod_len == 0:
#             return 0
#         max_price = -sys.maxsize
#         for i in range(1, rod_len + 1):
#             comp_price = prices[i - 1] + _cut_rod_recur(prices, rod_len - i)
#             if comp_price > max_price:
#                 max_price = comp_price
#                 max_set.append(i)
#         return max_price
#
#     return _cut_rod_recur(prices, rod_len), max_set

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


def cut_rod_dyna(prices, rod_len):
    dp_arr = [[0] * (rod_len + 1) for _ in range(len(prices) + 1)]
    max_price = -sys.maxsize
    for i in range(1, len(prices) + 1):
        for j in range(1, rod_len + 1):
            if j >= i:
                dp_arr[i][j] = max(dp_arr[i - 1][j], prices[i - 1] + dp_arr[i][j - i])
            else:
                dp_arr[i][j] = dp_arr[i - 1][j]
            max_price = max(max_price, dp_arr[i][j])
    return max_price


# def cut_rod_dyna(prices, rod_len):  # simplified version
#     dp_arr = [0] * (rod_len + 1)
#     # print(dp_arr)
#     max_price = -sys.maxsize
#     for i in range(1, len(prices) + 1):
#         for j in range(1, rod_len + 1):
#             if j >= i:
#                 dp_arr[j] = max(dp_arr[j], prices[i - 1] + dp_arr[j - i])
#             max_price = max(max_price, dp_arr[j])
#         # print(dp_arr)
#     return max_price


if __name__ == '__main__':
    # prices_arr = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # for i in range(1, 11):
    #     print(cut_rod_naive(prices_arr, i))
    #     print(cut_rod_recur(prices_arr, i))
    #     print(cut_rod_recur_dyna(prices_arr, i))
    #     print(cut_rod_dyna(prices_arr, i))

    # print(cut_rod_naive(prices_arr, 20))
    # print(cut_rod_recur(prices_arr, 4))

    prices_arr = [1, 5, 8]

    # print(cut_rod_naive(prices_arr, 1))
    # print(cut_rod_naive(prices_arr, 2))
    # print(cut_rod_naive(prices_arr, 3))
    # print(cut_rod_naive(prices_arr, 4))
    # print(cut_rod_naive(prices_arr, 5))
    # print(cut_rod_naive(prices_arr, 6))
    # print(cut_rod_naive(prices_arr, 7))
    # print(cut_rod_naive(prices_arr, 8))

    # print(cut_rod_dyna(prices_arr, 8))

    print(cut_rod_recur(prices_arr, 1))
    print(cut_rod_recur(prices_arr, 2))
    print(cut_rod_recur(prices_arr, 3))
    print(cut_rod_recur(prices_arr, 4))
    print(cut_rod_recur(prices_arr, 5))
    print(cut_rod_recur(prices_arr, 6))
    print(cut_rod_recur(prices_arr, 7))
    print(cut_rod_recur(prices_arr, 8))

    #      0    1    2    3    4
    #   ┌────┬────┬────┬────┬────┐
    # ø │  0 │  0 │  0 │  0 │  0 │
    #   ├────┼────┼────┼────┼────┤
    # 1 │  0 │  1 │  0 │  0 │  0 │
    #   ├────┼────┼────┼────┼────┤
    # 2 │  0 │  1 │  5 │  0 │  0 │
    #   ├────┼────┼────┼────┼────┤
    # 3 │  0 │  1 │  5 │  8 │  0 │
    #   ├────┼────┼────┼────┼────┤
    # 4 │  0 │  1 │  5 │  8 │ 10 │
    #   └────┴────┴────┴────┴────┘

    prices_arr = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24,  # 0X's
                  30, 32, 35, 39, 43, 43, 45, 49, 50, 54,  # 1X's
                  57, 60, 65, 68, 70, 74, 80, 81, 84, 85,  # 2X's
                  87, 91, 95, 99, 101, 104, 107, 112, 115, 116,  # 3X's
                  119]  # 40th element

    print(cut_rod_dyna(prices_arr, 1))
