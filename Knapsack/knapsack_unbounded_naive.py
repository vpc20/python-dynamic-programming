from itertools import combinations_with_replacement


# weights in wts are unique
# def knapsack_unbounded_naive(wts, vals, wt_limit):
#     wt_val_dict = {wts[i]: vals[i] for i in range(len(wts))}
#     # print(wt_val_dict)
#     maxval = 0
#     maxcomb = ()
#     for r in range(1, wt_limit + 1):
#         for comb in combinations_with_replacement(wts, r):
#             if sum(comb) <= wt_limit:
#                 totval = sum([wt_val_dict[e] for e in comb])
#                 # print(comb, totval)
#                 if totval > maxval:
#                     maxval = totval
#                     maxcomb = comb
#     return maxval  # , maxcomb


# can have items with same weights in wts
def knapsack_unbounded_naive(wts, vals, wt_limit):
    wt_val_pairs = list(zip(wts, vals))
    # print(wt_val_pairs)
    maxval = 0
    maxcomb = ()
    for r in range(1, wt_limit + 1):
        for comb in combinations_with_replacement(wt_val_pairs, r):
            if sum([item[0] for item in comb]) <= wt_limit:
                # print(comb)
                totval = sum([item[1] for item in comb])
                if totval > maxval:
                    maxval = totval
                    maxcomb = comb
    return maxval   #, maxcomb


if __name__ == '__main__':
    # wts = [1, 2, 3]
    # vals = [50, 110, 160]
    # wt_limit = 5
    # print(knapsack_unbounded_naive(wts, vals, wt_limit))

    # all possible combinations
    # (1,) 50
    # (2,) 110
    # (3,) 160
    # (1, 1) 100
    # (1, 2) 160
    # (1, 3) 210
    # (2, 2) 220
    # (2, 3) 270
    # (1, 1, 1) 150
    # (1, 1, 2) 210
    # (1, 1, 3) 260
    # (1, 2, 2) 270
    # (1, 1, 1, 1) 200
    # (1, 1, 1, 2) 260
    # (1, 1, 1, 1, 1) 250

    # wts = [1, 1, 2, 4, 12]
    # vals = [1, 2, 2, 10, 4]
    # wt_limit = 15
    # print(knapsack_unbounded_naive(wts, vals, wt_limit))

    # wts = [7, 8, 5, 5, 5]
    # vals = [9, 12, 4, 13, 4]
    # wt_limit = 5
    # print(knapsack_unbounded_naive(wts, vals, wt_limit))

    # wts = [1, 2, 3]
    # vals = [50, 110, 160]
    # wlimit = 5
    # print(knapsack_unbounded_naive(wts, vals, wlimit))

    wts = [1, 1, 2, 4, 12]
    vals = [1, 2, 2, 10, 4]
    wlimit = 15
    print(knapsack_unbounded_naive(wts, vals, wlimit))

    # wts = [2, 3, 5]
    # vals = [50, 100, 140]
    # wlimit = 17
    # print(knapsack_unbounded_naive(wts, vals, wlimit))
