from itertools import combinations


def powerset_naive(arr):
    powerset = [[]]
    for i in range(1, len(arr) + 1):
        for comb in combinations(arr, i):
            powerset.append(list(comb))
    return powerset


# def powerset_iter(arr):
#     dp_arr = [[[]]] + [[] for _ in range(len(arr))]
#     print(dp_arr)
#     for i in range(1, len(arr) + 1):
#         for prev in dp_arr[i - 1]:
#             dp_arr[i].append(prev)
#             x = prev.copy()
#             x.append(arr[i - 1])
#             dp_arr[i].append(x)
#         print(dp_arr)
#     return dp_arr[-1]


# def powerset_iter(arr):
#     pset = [[]]
#     # print(pset)
#     for i in range(len(arr)):
#         for e in pset.copy():
#             e_copy = e.copy()
#             e_copy.append(arr[i])
#             pset.append(e_copy)
#         # print(pset)
#     return pset

def powerset(arr):
    pset = [[]]
    for n in arr:
        for e in pset.copy():
            pset.append(e + [n])
        print(pset)
    return pset


def power_set(nums):
    result = [[]]

    for num in nums:
        new_subsets = [subset + [num] for subset in result]
        result.extend(new_subsets)

    return result


# class Solution:
#
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         # You start with a list that contains one empty list (null subset)
#         power_set = [[]]
#         for num in nums:
#             power_set += [subset + [num] for subset in power_set]
#
#         return power_set

# def powerset_recur(arr):
#     if not arr:
#         yield []
#     elif len(arr) == 1:
#         yield []
#         yield [arr[-1]]
#     else:
#         for p in powerset_recur(arr[:-1]):
#             yield p
#             yield p + [arr[-1]] if p else [arr[-1]]


def powerset_recur(arr):  # dyna equivalent
    if not arr:
        yield []
    else:
        for p in powerset_recur(arr[:-1]):
            yield p
            yield p + [arr[-1]]


# def powerset_recur(arr):
#     if not arr:
#         yield []
#     else:
#         for p in powerset_recur(arr[:-1]):
#             yield p
#         for p in powerset_recur(arr[:-1]):
#             yield p + [arr[-1]]


if __name__ == '__main__':
    # print(powerset_naive([1, 2]))
    # print(list(powerset_recur([1, 2])))
    # print(powerset_naive([745, 993, 599]))
    # print(powerset_iter([745, 993, 599]))
    # print(list(powerset_recur([])))

    #  0     1          2
    # [[[]], []       , []                    ]
    # [[[]], [[], [1]], []                    ]
    # [[[]], [[], [1]], [[], [2], [1], [1, 2]]]
    print(list(powerset_recur([5, 6])))
    # print(list(powerset_recur([5, 6])))

##    print(powerset([]))
##    print(powerset([1]))
##    print(powerset([1, 2]))
    print(powerset([1, 2, 3]))
##    print(powerset([1, 2, 2]))
