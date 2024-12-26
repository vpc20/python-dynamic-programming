def knapsack_unbounded_recur(wts, vals, wt_limit):
    if not wts or wt_limit == 0:
        return 0
    if wt_limit >= wts[-1]:
        return max(vals[-1] + knapsack_unbounded_recur(wts, vals, wt_limit - wts[-1]),
                   knapsack_unbounded_recur(wts[:-1], vals[:-1], wt_limit), )
    else:
        return knapsack_unbounded_recur(wts[:-1], vals[:-1], wt_limit)


if __name__ == '__main__':
    # wts = [1, 2, 3]
    # vals = [50, 110, 160]
    # wlimit = 5
    # print(knapsack_unbounded_iter(wts, vals, wlimit))

    wts = [1, 1, 2, 4, 12]
    vals = [1, 2, 2, 10, 4]
    wlimit = 15
    print(knapsack_unbounded_recur(wts, vals, wlimit))

    # wts = [2, 3, 5]
    # vals = [50, 100, 140]
    # wlimit = 17
    # print(knapsack_unbounded_recur(wts, vals, wlimit))
