# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique
# combinations in candidates where the candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of times.
#
# Note:
#
#     All numbers (including target) will be positive integers.
#     The solution set must not contain duplicate combinations.
#
# Example 1:
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#
# Example 2:
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]

# *** returns number of ways to make combination
# def combination_sum(candidatesr, target):
#     nrows = len(candidatesr) + 1
#     ncols = target + 1
#     dp = [[1] + [0] * target for _ in range(nrows)]
#
#     for i in range(1, nrows):
#         for j in range(1, ncols):
#             if j >= candidatesr[i - 1]:
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - candidatesr[i - 1]]
#             else:
#                 dp[i][j] = dp[i - 1][j]
#     for e in dp:
#         print(e)
#     return dp[-1][-1]


# *** returns number of ways to make combination - simplified dp
# def combination_sum(candidates, target):
#     nrows = len(candidates) + 1
#     ncols = target + 1
#     dp = [1] + [0] * target
#     print(dp)
#
#     for i in range(1, nrows):
#         for j in range(1, ncols):
#             if j >= candidates[i - 1]:
#                 dp[j] += dp[j - candidates[i - 1]]
#         print(dp)
#     return dp[-1]


# *** returns the array  of combinations
def combination_sum(candidates, target):
    nrows = len(candidates) + 1
    ncols = target + 1
    dp = [[[]]] + [[] for _ in range(target)]
    # print(dp)

    for i in range(1, nrows):
        for j in range(1, ncols):
            if j >= candidates[i - 1]:
                for e in dp[j - candidates[i - 1]]:
                    dp[j].append(e + [candidates[i - 1]])
        # print(dp)
    return dp[-1]


def combinationSum(candidates, target):
    candidates, result = sorted(candidates), []

    def dfs(target, stack):
        # found a valid combination
        if target == 0:
            return result.append(stack)

        # for every candidate
        for candidate in candidates:
            if candidate > target:
                break  # anything else would be negative (see sort)
            elif stack and candidate < stack[-1]:
                continue  # don't allow dupes, take coins in non-decreasing order
            else:
                dfs(target - candidate, stack + [candidate])

    dfs(target, [])
    return result


# print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
print(combinationSum([2, 3, 5], 8))
