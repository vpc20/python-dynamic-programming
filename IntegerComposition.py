from itertools import product


def int_compositions_naive(n):
    arr = [i for i in range(1, n + 1)]
    comp_arr = []
    comp_count = 0
    for r in range(1, len(arr) + 1):
        for prod in product(arr, repeat=r):
            if sum(prod) == n:
                comp_arr.append(prod)
                comp_count += 1
    return comp_count, comp_arr


# def int_compositions_recur(n):
#     def _int_compositions_recur(arr, i):
#         if len(arr) == 0:
#             if i > 0:
#                 return 0
#             else:
#                 return 1
#         if i == 0:
#             return 1
#         for j in range(1, i + 1):
#             if j >= i:
#                 return _int_compositions_recur(arr[:-1], j) + _int_compositions_recur(arr, j - i)
#             else:
#                 return _int_compositions_recur(arr[:-1], j)
#     num_arr = [i for i in range(1, n + 1)]
#     return _int_compositions_recur(num_arr, n)
# return _int_compositions_recur([1], 2)


def int_compositions_iter(n):  # dynamic solution
    dp_arr = [[1] + [0] * n for _ in range(n + 1)]
    # part_arr = [[[[]]] + [[]] * n for _ in range(n + 1)]
    comp_arr = [[[[]]] + [[] for _ in range(n)] for _ in range(n + 1)]
    int_list = [i for i in range(1, n + 1)]
    # for e in comp_arr:
    #     print(e)
    # print('')
    for i in int_list:
        for j in range(1, n + 1):
            if j >= i:
                comp_arr[i][j] += comp_arr[i - 1][j]
                for prev in comp_arr[i][j - i]:  # prev int arr list could have several lists
                    # if all elements of prev is same as the integer, just append the integer to prev
                    if len(set(prev)) == 1 and list(set(prev))[0] == int_list[i - 1]:
                        prev_copy = prev.copy()
                        prev_copy.append(int_list[i - 1])
                        comp_arr[i][j] += [prev_copy]
                    else:
                        new_list = []
                        for k in range(len(prev), -1, -1):  # insert char in all positions
                            new_list.append(prev[:k] + [int_list[i - 1]] + prev[k:])
                        comp_arr[i][j] += new_list
            else:
                comp_arr[i][j] = comp_arr[i - 1][j]
        dp_arr[i][j] = len(comp_arr[i][j])
    for subarr in comp_arr:
        print(subarr)
    # print(comp_arr)
    return dp_arr[-1][-1], comp_arr[-1][-1]


# def int_compositions_iter(n):  # dynamic solution
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
    # print(int_compositions_naive(4))
    print(int_compositions_iter(4))
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
    #     print(int_compositions_iter(i))

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

    # print(int_compositions_recur(1))
    # print(int_compositions_naive(4))

    for i in range(1, 10):
        print(int_compositions_iter(i))
