import sys


def max_subarr_sum_naive(arr):
    if not arr:
        return 0
    maxsum = -sys.maxsize
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) + 1):
            maxsum = max(maxsum, sum(arr[i:j]))
    return maxsum


# dynamic simplified
def max_subarr_sum(arr):
    """ Maximum sub-array function computes for the largest sum of sub-array

    :param arr: input array
    :return: maximum sum of sub-array
    """
    if not arr:
        return 0
    subarr_sum = 0
    maxsum = -sys.maxsize
    for num in arr:
        subarr_sum = max(subarr_sum + num, num)
        maxsum = max(maxsum, subarr_sum)
    return maxsum


# def max_subarr_sum(arr):
#     """ Maximum sub-array function computes for the largest sum of sub-array
#
#     :param arr: input array
#     :return: maximum sum of sub-array
#     """
#     if not arr:
#         return 0
#     subarr_sum = 0
#     maxi = 0
#     maxsum = -sys.maxsize
#     for i, num in enumerate(arr):
#         subarr_sum = max(subarr_sum + num, num)
#         if subarr_sum > maxsum:
#             maxsum = subarr_sum
#             maxi = i
#
#     subarr_sum = 0
#     for i in range(maxi, -1, -1):
#         subarr_sum += arr[i]
#         if subarr_sum == maxsum:
#             break
#
#     return maxsum, i, arr[i:maxi + 1]


def max_subarr_sum_dyna(arr):
    if not arr:
        return 0
    dp_arr = [0] * len(arr)
    print(dp_arr)
    maxsum = -sys.maxsize
    for i in range(len(arr)):
        dp_arr[i] = max(arr[i], arr[i] + dp_arr[i - 1])
        maxsum = max(maxsum, dp_arr[i])
        print(dp_arr)
    return maxsum


# def max_subarr_sum_dyna(arr):
#     dp_arr = [arr[0]] + [0] * (len(arr) - 1)
#     for i in range(1, len(arr)):
#         dp_arr[i] = max(arr[i], arr[i] + dp_arr[i - 1])
#     return max(dp_arr)


# def max_subarr_sum_recur(arr, subarr_sum=0, maxsum=-sys.maxsize):
#     # print(arr, subarr_sum, maxsum)
#     if not arr:
#         return 0
#     subarr_sum = max(subarr_sum + arr[0], arr[0])
#     maxsum = max(maxsum, subarr_sum)
#     if len(arr) == 1:
#         return maxsum
#     return max_subarr_sum_recur(arr[1:], subarr_sum, maxsum)


# def max_subarr_sum_recur(arr):
#     def _max_subarr_sum_recur(arr):
#         nonlocal subarr_sum
#         nonlocal maxsum
#         if not arr:
#             return 0
#         subarr_sum = max(subarr_sum + arr[0], arr[0])
#         maxsum = max(maxsum, subarr_sum)
#         return _max_subarr_sum_recur(arr[1:])
#
#     if not arr:
#         return 0
#     subarr_sum = 0
#     maxsum = -sys.maxsize
#     _max_subarr_sum_recur(arr)
#     return maxsum


def max_subarr_sum_recur(arr):  # dyna equivalent
    def _max_subarr_sum_recur(arr):
        nonlocal maxsum
        if not arr:
            return 0
        subarr_sum = max(_max_subarr_sum_recur(arr[1:]) + arr[0], arr[0])
        maxsum = max(maxsum, subarr_sum)
        return subarr_sum

    if not arr:
        return 0
    maxsum = -sys.maxsize
    _max_subarr_sum_recur(arr)
    return maxsum


# return subarray indexes
# def max_subarray(arr):
#     maxsum, start_idx, end_idx, subarr_sum = -maxsize, 0, 0, 0
#     for j, num in enumerate(arr):
#         subarr_sum = subarr_sum + num
#         if num > subarr_sum:
#             subarr_sum = num
#         if subarr_sum > maxsum:
#             maxsum, end_idx = subarr_sum, j
#     subarr_sum = 0
#     for start_idx in range(end_idx, -1, -1):
#         subarr_sum += arr[start_idx]
#         if subarr_sum == maxsum:
#             break
#     return maxsum, start_idx, end_idx


if __name__ == '__main__':
    # print(max_subarr_sum_naive([]))
    # print(max_subarr_sum([]))
    # print(max_subarr_sum_dyna([]))
    # print(max_subarr_sum_recur([]))
    #
    # print(max_subarr_sum_naive([1]))
    # print(max_subarr_sum([1]))
    # print(max_subarr_sum_dyna([1]))
    # print(max_subarr_sum_recur([1]))
    #
    # print(max_subarr_sum_naive([1, 2]))
    # print(max_subarr_sum([1, 2]))
    # print(max_subarr_sum_dyna([1, 2]))
    # print(max_subarr_sum_recur([1, 2]))
    #
    # print(max_subarr_sum_naive([-1, 2]))
    # print(max_subarr_sum([-1, 2]))
    # print(max_subarr_sum_dyna([-1, 2]))
    # print(max_subarr_sum_recur([-1, 2]))
    #
    # print(max_subarr_sum_naive([1, -2]))
    # print(max_subarr_sum([1, -2]))
    # print(max_subarr_sum_dyna([1, -2]))
    # print(max_subarr_sum_recur([1, -2]))
    #
    # print(max_subarr_sum_naive([-1, -2]))
    # print(max_subarr_sum([-1, -2]))
    # print(max_subarr_sum_dyna([-1, -2]))
    # print(max_subarr_sum_recur([-1, -2]))

    # print(max_subarr_sum_naive([5, -1, 6, -3, 4, 2, -2]))
    # print(max_subarr_sum([5, -1, 6, -3, 4, 2, -2]))
    # print(max_subarr_sum_dyna([5, -1, 6, -3, 4, 2, -2]))
    # print(max_subarr_sum_recur([5]))
    # print(max_subarr_sum_recur([5, -1]))
    # print(max_subarr_sum_recur([5, -1, 6]))
    # print(max_subarr_sum_recur([5, -1, 6]))
    # print(max_subarr_sum_recur([-1, -2, -3]))
    # print(max_subarr_sum_recur([1, 2, 3, -1, -2, -3]))
    # print(max_subarr_sum_recur([-3, 1]))
    # print(max_subarr_sum_recur([-1, -2, -3, 1, 2, 3]))
    # print(max_subarr_sum_recur([1, 2, 3, -1, -2, -3]))

    print(max_subarr_sum_naive([5, -1, 6, -3, 4, 2, -2]))
    print(max_subarr_sum([5, -1, 6, -3, 4, 2, -2]))
    print(max_subarr_sum_dyna([5, -1, 6, -3, 4, 2, -2]))
    print(max_subarr_sum_recur([5, -1, 6, -3, 4, 2, -2]))

    #      0   1    2   3    4    5    6   7
    #    ┌───┬───┬────┬───┬────┬────┬────┬───┐
    # ø  │ 0 │ 0 │  0 │ 0 │  0 │  0 │  0 │ 0 │
    #    ├───┼───┼────┼───┼────┼────┼────┼───┤
    # 5  │ 5 │ 0 │  0 │ 0 │  0 │  0 │  0 │ 0 │
    #    ├───┼───┼────┼───┼────┼────┼────┼───┤
    # -1 │ 5 │ 4 │  0 │ 0 │  0 │  0 │  0 │ 0 │
    #    ├───┼───┼────┼───┼────┼────┼────┼───┤
    # 6  │ 5 │ 4 │ 10 │ 0 │  0 │  0 │  0 │ 0 │
    #    ├───┼───┼────┼───┼────┼────┼────┼───┤
    # -3 │ 5 │ 4 │ 10 │ 7 │  0 │  0 │  0 │ 0 │
    #    ├───┼───┼────┼───┼────┼────┼────┼───┤
    # 4  │ 5 │ 4 │ 10 │ 7 │ 11 │  0 │  0 │ 0 │
    #    ├───┼───┼────┼───┼────┼────┼────┼───┤
    # 2  │ 5 │ 4 │ 10 │ 7 │ 11 │ 13 │  0 │ 0 │
    #    ├───┼───┼────┼───┼────┼────┼────┼───┤
    # -2 │ 5 │ 4 │ 10 │ 7 │ 11 │ 13 │ 11 │ 0 │
    #    └───┴───┴────┴───┴────┴────┴────┴───┘
