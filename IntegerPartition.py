# Input description: An integer n.
# Problem description: Generate all integer partitions and its count
#
# Integer partitions are multisets of nonzero integers that add up exactly to
# n. For example, the seven distinct integer partitions of 5 are {5}, {4,1},
# {3,2}, {3,1,1}, {2,2,1}, {2,1,1,1}, and {1,1,1,1,1}.
from itertools import combinations_with_replacement


def int_partitions_naive(n):
    arr = [i for i in range(1, n + 1)]
    part_arr = []
    part_count = 0
    for r in range(1, len(arr) + 1):
        for comb in combinations_with_replacement(arr, r):
            if sum(comb) == n:
                part_arr.append(comb)
                part_count += 1
    return part_count  # , part_arr


def int_partitions_recur(n):
    def _int_partitions_recur(arr, j):
        if len(arr) == 0:
            if j == 0:
                return 1
            else:
                return 0
        if j == 0:
            return 1
        if j >= len(arr):
            return _int_partitions_recur(arr[:-1], j) + _int_partitions_recur(arr, j - len(arr))
        else:
            return _int_partitions_recur(arr[:-1], j)

    num_arr = [i for i in range(1, n + 1)]
    return _int_partitions_recur(num_arr, n)


def int_partitions_recur1(n):
    def _int_partitions_recur(arr, j):
        if len(arr) == 0:
            return []
        if j == 0:
            return [[]]
        if j >= len(arr):
            x = _int_partitions_recur(arr[:-1], j)
            for prev in _int_partitions_recur(arr, j - len(arr)):  # prev int arr list could have several lists
                x.append(prev + [arr[-1]])
            return x
        else:
            return _int_partitions_recur(arr[:-1], j)

    num_arr = [i for i in range(1, n + 1)]
    return _int_partitions_recur(num_arr, n)


# def int_partitions_iter(n):  # dynamic solution
#     dp_arr = [[1] + [0] * n for _ in range(n + 1)]
#     # part_arr = [[[[]]] + [[]] * n for _ in range(n + 1)]
#     part_arr = [[[[]]] + [[] for _ in range(n)] for _ in range(n + 1)]
#     for e in part_arr:
#         print(e)
#     int_list = [i for i in range(1, n + 1)]
#     # for e in part_arr:
#     #     print(e)
#     for i in int_list:
#         for j in range(1, n + 1):
#             if j >= i:
#                 dp_arr[i][j] = dp_arr[i - 1][j] + dp_arr[i][j - i]
#                 part_arr[i][j] = part_arr[i - 1][j]
#                 for prev in part_arr[i][j - i]:  # prev int arr list could have several lists
#                     part_arr[i][j].append(prev + [i])
#             else:
#                 dp_arr[i][j] = dp_arr[i - 1][j]
#                 part_arr[i][j] = part_arr[i - 1][j]
#     # for subarr in part_arr:
#     #     print(subarr)
#     # print(part_arr)
#     return dp_arr[-1][-1], part_arr[-1][-1]

def int_partitions_iter(n):  # dynamic solution
    dp_arr = [1] + [0] * n
    print(dp_arr)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j >= i:
                dp_arr[j] += dp_arr[j - i]
    return dp_arr[-1]


# def int_partitions_iter(n):  # dynamic solution
#     dp_arr = [1] + [0] * n
#     part_arr = [[[]]] + [[] for _ in range(n)]
#     int_list = [i for i in range(1, n + 1)]
#     # print(arr)
#     # print(part_arr)
#     # print('')
#     for i in int_list:
#         for j in range(1, n + 1):
#             if j >= i:
#                 dp_arr[j] += dp_arr[j - i]
#                 for prev in part_arr[j - i]:  # prev int arr list could have several lists
#                     part_arr[j].append(prev + [i])
#         # print(dp_arr)
#         # print(part_arr)
#         # print('')
#     for subarr in part_arr:
#         print(subarr)
#     return dp_arr[-1], part_arr[-1]


if __name__ == '__main__':
    # print(int_partitions_naive(4))
    print(int_partitions_iter(4))
    #      0      1       2               3                           4
    #   ┌──────┬───────┬───────────────┬───────────────────────────┬────────────────────────────────────────────────┐
    # 0 │ [[]] │ [[1]] │ [[1, 1], [2]] │ [[1, 1, 1], [1, 2], [3]]  │ [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]] │
    #   ├──────┼───────┼───────────────┼───────────────────────────┼────────────────────────────────────────────────┤
    # 1 │ [[]] │ [[1]] │ [[1, 1], [2]] │ [[1, 1, 1], [1, 2], [3]]  │ [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]] │
    #   ├──────┼───────┼───────────────┼───────────────────────────┼────────────────────────────────────────────────┤
    # 2 │ [[]] │ [[1]] │ [[1, 1], [2]] │ [[1, 1, 1], [1, 2], [3]]  │ [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]] │
    #   ├──────┼───────┼───────────────┼───────────────────────────┼────────────────────────────────────────────────┤
    # 3 │ [[]] │ [[1]] │ [[1, 1], [2]] │ [[1, 1, 1], [1, 2], [3]]  │ [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]] │
    #   ├──────┼───────┼───────────────┼───────────────────────────┼────────────────────────────────────────────────┤
    # 4 │ [[]] │ [[1]] │ [[1, 1], [2]] │ [[1, 1, 1], [1, 2], [3]]  │ [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]] │
    #   └──────┴───────┴───────────────┴───────────────────────────┴────────────────────────────────────────────────┘

    # for i in range(1, 21):
    #     print(int_partitions_iter(i))

    #    0  1  2  3
    #   [1, 0, 0, 0]
    # 1 [1, 1, 1, 1]
    # 2 [1, 1, 2, 2]
    # 3 [1, 1, 2, 3]

    #   0      1      2              3
    # ø [[[]], [   ], [           ], [                      ]]
    # 1 [[[]], [[1]], [[1, 1]     ], [[1, 1, 1]             ]]
    # 2 [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2]     ]]
    # 3 [[[]], [[1]], [[1, 1], [2]], [[1, 1, 1], [1, 2], [3]]]

    # ø is u'\xf8'

    # print(int_partitions_recur(1))
    print(int_partitions_recur(4))
    print(int_partitions_recur1(4))

    # for i in range(1,10):
    #     print(int_partitions_iter(i))
    #     print(int_partitions_recur(i))
