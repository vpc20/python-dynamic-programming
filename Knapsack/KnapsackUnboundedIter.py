def knapsack_unbounded_iter(wts, vals, wt_limit):
    # dp_arr = [[0 for _ in range(wt_limit + 1)] for _ in range(len(wts) + 1)]
    dp_arr = [[0] * (wt_limit + 1) for _ in range(len(wts) + 1)]
    # wt_arr = [[[] for _ in range(wlimit + 1)] for _ in range(len(wts) + 1)]
    wt_arr = [[[]] * (wt_limit + 1) for _ in range(len(wts) + 1)]
    # for e in dp_arr:
    #     print(e)
    for i in range(1, len(wts) + 1):
        for j in range(1, wt_limit + 1):
            if j >= wts[i - 1]:
                # dp_arr[i][j] = max(vals[i - 1] + dp_arr[i][j - wts[i - 1]],
                #                    dp_arr[i - 1][j])
                new_val = vals[i - 1] + dp_arr[i][j - wts[i - 1]]
                if new_val > dp_arr[i - 1][j]:
                    dp_arr[i][j] = new_val
                    wt_arr[i][j] = [wts[i - 1]] + wt_arr[i][j - wts[i - 1]]
                else:
                    dp_arr[i][j] = dp_arr[i - 1][j]
                    wt_arr[i][j] = wt_arr[i - 1][j]
            else:
                dp_arr[i][j] = dp_arr[i - 1][j]
                wt_arr[i][j] = wt_arr[i - 1][j]
    # for e in dp_arr:
    #     print(e)
    return dp_arr[-1][-1]  # , wt_arr[-1][-1]


if __name__ == '__main__':
    # wts = [1, 2, 3]
    # vals = [50, 110, 160]
    # wlimit = 5
    # print(knapsack_unbounded_iter(wts, vals, wlimit))

    wts = [1, 1, 2, 4, 12]
    vals = [1, 2, 2, 10, 4]
    wlimit = 15
    print(knapsack_unbounded_iter(wts, vals, wlimit))

    # wts = [2, 3, 5]
    # vals = [50, 100, 140]
    # wlimit = 17
    # print(knapsack_unbounded_iter(wts, vals, wlimit))
