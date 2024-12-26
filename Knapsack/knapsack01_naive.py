# The 0-1 knapsack problem is the following. A thief robbing a store finds n
# items. The ith item is worth vi dollars and weighs wi pounds, where vi and wi are
# integers. The thief wants to take as valuable a load as possible, but he can carry at
# most W pounds in his knapsack, for some integer W . Which items should he take?
# (We call this the 0-1 knapsack problem because for each item, the thief must either
# take it or leave it behind; he cannot take a fractional amount of an item or take an
# item more than once.)
from itertools import combinations


# weights in wts are unique
# def knapsack01_naive(wts, vals, wt_limit):
#     wt_val_dict = {wts[i]: vals[i] for i in range(len(wts))}
#     # print(wt_val_dict)
#     maxval = 0
#     maxcomb = ()
#     for r in range(1, len(wts) + 1):
#         for comb in combinations(wts, r):
#             if sum(comb) <= wt_limit:
#                 totval = sum([wt_val_dict[e] for e in comb])
#                 # print(comb, totval)
#                 if totval > maxval:
#                     maxval = totval
#                     maxcomb = comb
#     return maxval  # , maxcomb

# can have items with same weights in wts
def knapsack01_naive(wts, vals, wt_limit):
    wt_val_pairs = list(zip(wts, vals))
    # print(wt_val_pairs)
    maxval = 0
    maxcomb = ()
    for r in range(1, wt_limit + 1):
        for comb in combinations(wt_val_pairs, r):
            if sum([item[0] for item in comb]) <= wt_limit:
                # print(comb)
                totval = sum([item[1] for item in comb])
                if totval > maxval:
                    maxval = totval
                    maxcomb = comb
    return maxval   #, maxcomb


if __name__ == '__main__':
    # wts = [1, 2, 3]
    # vals = [60, 100, 120]
    # wt_limit = 5
    # print(knapsack01_naive(wts, vals, wt_limit))
    # all possible combinations
    # (1,) 60
    # (2,) 100
    # (3,) 120
    # (1, 2) 160
    # (1, 3) 180
    # (2, 3) 220

    # wts = [1]
    # vals = [50]
    # wts = [1, 2]
    # vals = [50, 110]
    # wts = [1, 2, 3]
    # vals = [50, 110, 160]
    # print(knapsack01_naive(wts, vals, 1))
    # print(knapsack01_naive(wts, vals, 2))
    # print(knapsack01_naive(wts, vals, 3))
    # print(knapsack01_naive(wts, vals, 4))
    # print(knapsack01_naive(wts, vals, 5))

    # wts = [1, 2, 3]
    # vals = [50, 110, 160]
    # wlimit = 5
    # print(knapsack01_naive(wts, vals, wlimit))

    wts = [1, 1, 2, 4, 12]
    vals = [1, 2, 2, 10, 4]
    wt_limit = 15
    print(knapsack01_naive(wts, vals, wt_limit))

    # wts = [2, 3, 5]
    # vals = [50, 100, 140]
    # wlimit = 17
    # print(knapsack01_naive(wts, vals, wlimit))
