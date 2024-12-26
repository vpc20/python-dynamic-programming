from itertools import combinations


def is_subset_sum_naive(arr, n):
    if n == 0:
        return True
    for i in range(1, len(arr) + 1):
        for comb in combinations(arr, i):
            # print(comb)
            if sum(comb) == n:
                # print(comb)
                return True
    return False


# def is_subset_sum_recur(arr, n):
#     if n == 0:
#         return True
#     if not arr and n != 0:
#         return False
#     if arr[0] > n:
#         return is_subset_sum_recur(arr[1:], n)
#     else:
#         return is_subset_sum_recur(arr[1:], n) or is_subset_sum_recur(arr[1:], n - arr[0])


def is_subset_sum_recur(arr, n):
    if n == 0:
        return True
    if not arr and n != 0:
        return False
    if arr[-1] > n:
        return is_subset_sum_recur(arr[:-1], n)
    else:
        return is_subset_sum_recur(arr[:-1], n) or is_subset_sum_recur(arr[:-1], n - arr[-1])


def is_subset_sum_dyna(arr, n):
    dp_arr = [[False] * (n + 1) for _ in range(len(arr) + 1)]
    num_arr = [[[] for _ in range(n + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        dp_arr[i][0] = True
    # for e in dp_arr:
    #     print(e)
    # for e in num_arr:
    #     print(e)
    for i in range(1, len(arr) + 1):
        for j in range(1, n + 1):
            if arr[i - 1] > j:
                dp_arr[i][j] = dp_arr[i - 1][j]
                num_arr[i][j] = num_arr[i - 1][j]
            else:
                dp_arr[i][j] = dp_arr[i - 1][j] or dp_arr[i - 1][j - arr[i - 1]]
                if dp_arr[i][j]:
                    num_arr[i][j] += num_arr[i - 1][j - arr[i - 1]]
                    num_arr[i][j].append(arr[i - 1])
    # for e in dp_arr:
    #     print(e)
    # for e in num_arr:
    #     print(e)
    # print(dp_arr)
    # print(num_arr)
    # print([subarr[n] for subarr in num_arr if subarr[n]])
    return dp_arr[-1][-1]


if __name__ == '__main__':
    # print(is_subset_sum([3, 34, 4, 12, 5, 2], 9))

    #       0      1      2      3      4      5      6      7      8      9
    #    [True, False, False, False, False, False, False, False, False, False]
    #  3 [True, False, False, True,  False, False, False, False, False, False]
    # 34 [True, False, False, True,  False, False, False, False, False, False]
    #  4 [True, False, False, True,  True,  False, False, True,  False, False]
    # 12 [True, False, False, True,  True,  False, False, True,  False, False]
    #  5 [True, False, False, True,  True,  True,  False, True,  True,  True]
    #  2 [True, False, True,  True,  True,  True,  True,  True,  True,  True]

    # print(is_subset_sum_naive([2, 3, 5, 7], 9))
    # print(is_subset_sum_dyna([2, 3, 5, 7], 9))
    # print(is_subset_sum_recur([2, 3, 5, 7], 9))

    #    0     1      2      3      4      5      6      7      8      9
    #   [True, False, False, False, False, False, False, False, False, False]
    # 2 [True, False, True,  False, False, False, False, False, False, False]
    # 3 [True, False, True,  True,  False, True,  False, False, False, False]
    # 5 [True, False, True,  True,  False, True,  False, True,  True,  False]
    # 7 [True, False, True,  True,  False, True,  False, True,  True,  True]

    # print(is_subset_sum_naive([8, 3, -8, 10], 0))
    # print(is_subset_sum_naive([7, 4], 0))
    # print(is_subset_sum([7, 4], 0))
    # print(is_subset_sum_dyna([15, 15, 13, 9], 82))

    # print(is_subset_sum_dyna([2, 4, 6], 6))
    #       0       1       2       3       4       5       6
    #   ┌───────┬───────┬───────┬───────┬───────┬───────┬───────┐
    # ø │  True │ False │ False │ False │ False │ False │ False │
    #   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┤
    # 2 │  True │ False │  True │ False │ False │ False │ False │
    #   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┤
    # 4 │  True │ False │  True │ False │  True │ False │  True │
    #   ├───────┼───────┼───────┼───────┼───────┼───────┼───────┤
    # 6 │  True │ False │  True │ False │  True │ False │  True │
    #   └───────┴───────┴───────┴───────┴───────┴───────┴───────┘

    #        0        1        2        3        4        5        6
    #   ┌────────┬────────┬────────┬────────┬────────┬────────┬────────┐
    # ø │     [] │     [] │     [] │     [] │     [] │     [] │     [] │
    #   ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
    # 2 │     [] │     [] │    [2] │     [] │     [] │     [] │     [] │
    #   ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
    # 4 │     [] │     [] │     [] │     [] │    [4] │     [] │ [2, 4] │
    #   ├────────┼────────┼────────┼────────┼────────┼────────┼────────┤
    # 6 │     [] │     [] │     [] │     [] │     [] │     [] │    [6] │
    #   └────────┴────────┴────────┴────────┴────────┴────────┴────────┘

    # print(is_subset_sum_dyna([3, 34, 4, 12, 5, 2], 9))

    print(is_subset_sum_dyna([1, 2, 3, 4, 5], 5))
    #       0      1       2       3       4       5
    #   ┌──────┬───────┬───────┬───────┬───────┬───────┐
    # 0 │ True │ False │ False │ False │ False │ False │
    #   ├──────┼───────┼───────┼───────┼───────┼───────┤
    # 1 │ True │ True  │ False │ False │ False │ False │
    #   ├──────┼───────┼───────┼───────┼───────┼───────┤
    # 2 │ True │ True  │ True  │ True  │ False │ False │
    #   ├──────┼───────┼───────┼───────┼───────┼───────┤
    # 3 │ True │ True  │ True  │ True  │ True  │ True  │
    #   ├──────┼───────┼───────┼───────┼───────┼───────┤
    # 4 │ True │ True  │ True  │ True  │ True  │ True  │
    #   ├──────┼───────┼───────┼───────┼───────┼───────┤
    # 5 │ True │ True  │ True  │ True  │ True  │ True  │
    #   └──────┴───────┴───────┴───────┴───────┴───────┘

    #      0    1     2       3        4        5
    #   ┌────┬─────┬─────┬────────┬────────┬────────┐
    # 0 │ [] │ []  │ []  │ []     │ []     │ []     │
    #   ├────┼─────┼─────┼────────┼────────┼────────┤
    # 1 │ [] │ [1] │ []  │ []     │ []     │ []     │
    #   ├────┼─────┼─────┼────────┼────────┼────────┤
    # 2 │ [] │ [1] │ [2] │ [1, 2] │ []     │ []     │
    #   ├────┼─────┼─────┼────────┼────────┼────────┤
    # 3 │ [] │ [1] │ [2] │ [3]    │ [1, 3] │ [2, 3] │
    #   ├────┼─────┼─────┼────────┼────────┼────────┤
    # 4 │ [] │ [1] │ [2] │ [3]    │ [4]    │ [1, 4] │
    #   ├────┼─────┼─────┼────────┼────────┼────────┤
    # 5 │ [] │ [1] │ [2] │ [3]    │ [4]    │ [5]    │
    #   └────┴─────┴─────┴────────┴────────┴────────┘

    print(is_subset_sum_naive([1, 2, 3, 4, 5], 5))




