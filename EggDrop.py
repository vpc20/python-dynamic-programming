# Minimum egg drops with n eggs and k floors
import sys
from functools import lru_cache


def egg_drop_iter(n, k):
    if n == 0:
        return 0
    dp_arr = [[0, 1] + [k] * (k - 1) for _ in range(n + 1)]

    # For one egg and j floors.
    for j in range(k + 1):
        dp_arr[1][j] = j

    # print(dp_arr)
    # for e in dp_arr:
    #     print(e)
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            for h in range(1, j + 1):
                num_drops = 1 + max(dp_arr[i - 1][h - 1], dp_arr[i][j - h])
                if num_drops < dp_arr[i][j]:
                    dp_arr[i][j] = num_drops

    print(dp_arr)
    # for e in dp_arr:
    #     print(e)
    return dp_arr[n][k]


# Recursive Solution
# You have n eggs and k consecutive floors yet to be tested,
# and afterward you drop the egg at floor h in this sequence of k consecutive floors.
# If the eggs break:
# The problem reduces to n−1 eggs and h−1 remaining floors.
# If it doesn't break:
# The problem reduces to n eggs and k - h remaining floors.
@lru_cache(maxsize=1000)
def egg_drop_recur(n, k):
    if n == 0 or k == 0:
        return 0
    if k == 1:
        return 1
    if n == 1:
        return k

    min_drops = sys.maxsize
    for h in range(1, k + 1):
        num_drops = 1 + max(egg_drop_recur(n - 1, h - 1),
                            egg_drop_recur(n, k - h))
        if num_drops < min_drops:
            min_drops = num_drops

    return min_drops


if __name__ == '__main__':
    n = 2
    k = 10
    print(egg_drop_iter(n, k))
    # print(egg_drop_recur(n, k))

    #     0   1    2    3    4    5    6    7    8    9   10
    #   ┌───┬───┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
    # 0 │ 0 │ 1 │ 10 │ 10 │ 10 │ 10 │ 10 │ 10 │ 10 │ 10 │ 10 │
    #   ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
    # 1 │ 0 │ 1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │  9 │ 10 │
    #   ├───┼───┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
    # 2 │ 0 │ 1 │  2 │  2 │  3 │  3 │  3 │  4 │  4 │  4 │  4 │
    #   └───┴───┴────┴────┴────┴────┴────┴────┴────┴────┴────┘

    # for n in range(25):
    #     for k in range(25):
    #         if egg_drop_iter(n, k) != egg_drop_recur(n, k):
    #             print(egg_drop_iter(n, k), egg_drop_recur(n, k))
    #             print('error', n, k)
    #             break
    #         # print(n,k,egg_drop_iter(n, k))
    # print('Egg drop program completed')




