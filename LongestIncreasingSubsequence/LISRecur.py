# def lis_recur(arr, maxlen=0):
#     print(arr, maxlen)
#     for i in range(1, len(arr)):
#         for j in range(i):
#             if arr[i] > arr[j]:
#                 length = lis_recur(arr[1:], maxlen + 1)
#                 if length > maxlen:
#                     maxlen = length
#     if len(arr) == 1:
#         return maxlen
#     return maxlen


# def lis_recur(arr, n, maximum=1):
#     if n == 1:
#         return 1
#     max_ending_here = 1
#     for i in range(1, n):
#         res = lis_recur(arr, i)
#         if arr[i - 1] < arr[n - 1] and res + 1 > max_ending_here:
#             max_ending_here = res + 1
#     maximum = max(maximum, max_ending_here)
#     return max_ending_here


# def lis_recur(arr, maximum=1):
#     n = len(arr)
#
#     def _lis_recur(arr, n):
#         if n == 1:
#             return 1
#         nonlocal maximum
#         max_ending_here = 1
#         # print('-----new for', n)
#         for i in range(1, n):
#             # print('for i', i)
#             res = _lis_recur(arr, i)
#             # print(i-1, n-1)
#             if arr[i - 1] < arr[n - 1] and res + 1 > max_ending_here:
#                 max_ending_here = res + 1
#         maximum = max(maximum, max_ending_here)
#         return max_ending_here
#
#     return _lis_recur(arr, n)


# def lis_recur(arr, maximum=1):
#     if len(arr) == 1:
#         return 1
#     max_subarr = 1
#     for i in range(len(arr)):
#         res = lis_recur(arr[1:])
#         if arr[i] < arr[-1] and res + 1 > max_subarr:
#             max_subarr = res + 1
#     maximum = max(maximum, max_subarr)
#     return maximum


def lis_recur(arr):
    def _lis_recur(arr):
        # print(f'_lis_recur({arr})')
        if len(arr) == 1:
            return 1
        nonlocal maximum
        max_subarr = 1
        for i in range(len(arr) - 1):
            res = _lis_recur(arr[:i + 1])
            if arr[i] < arr[-1] and res + 1 > max_subarr:
                max_subarr = res + 1
        maximum = max(maximum, max_subarr)
        return max_subarr

    maximum = 1
    _lis_recur(arr)
    return maximum


if __name__ == '__main__':
    # print(lis_iter([1, 10, 5, 20, 30, 6, 7, 8, 9, 2]))

    # print(lis_recur([1], 1))
    # print(lis_recur([1, 2], 2))
    # print(lis_recur([1, 2, 3], 3))

    # print(lis_recur([1]))
    # print(lis_recur([1, 2]))
    # print(lis_recur([1, 2, 3]))
    # print(lis_recur([1, 2, 3, 4]))

    # print(lis_recur([1, 3, 2]))

    # print(lis_recur([2, 1]))
    # print(lis_recur([3, 2, 1]))
    # print(lis_recur([4, 3, 2, 1]))
    #
    # print(lis_recur([4]))
    # print(lis_recur([4, 2]))
    # print(lis_recur([4, 2, 1]))
    print(lis_recur([4, 2, 1, 3]))
    # print(lis_recur([2, 4, 1, 3]))
    # print(lis_recur_iter([590, 309, 255, -866, 801, 392, -711, -883, 29, 186]))
    #
    # print(lis_recur([10]))
    # print(lis_recur([10, 5]))
    # print(lis_recur([10, 5, 1]))
    # print(lis_recur([10, 5, 1, 75]))
    # print(lis_recur([10, 5, 1, 75, 50]))
    # print(lis_recur([10, 5, 1, 75, 50, -10, 150]))
    # print(lis_recur([10, 5, 1, 75, 50, -10, 150, 200]))
    # print(lis_recur([620, -703, -788, 796, -865], 5))
