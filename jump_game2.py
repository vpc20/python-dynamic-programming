# Given an array of non - negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position. Your goal is to reach the
# last index in the minimum number of jumps. You can assume that you can always reach the last index.
#
# Example 1:
# Input: nums = [2, 3, 1, 1, 4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then
# 3 steps to the last index.
#
# Example 2:
# Input: nums = [2, 3, 0, 1, 4]
# Output: 2
#
# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 105
from collections import defaultdict, deque


# dp solution
def jump(nums):
    dp = [0] * len(nums)

    for i in range(1, len(nums)):
        mindpj = 9999
        for j in range(i):
            if nums[j] + j >= i:
                mindpj = min(mindpj, dp[j])
        dp[i] = mindpj + 1
    print(dp)
    return dp[-1]


# using graph
def jump1(nums):
    if len(nums) == 1:
        return 0

    n = len(nums)
    g = defaultdict(list)  # graph
    for i in range(n):  # nodes
        g[i] = []

    for i in range(n):  # edges
        for j in range(i + 1, min(i + nums[i] + 1, n)):
            g[i].append(j)
    print(g)
    # bfs shortest path -  start = 0,  end = n
    pathlen = 0
    q = deque([0])
    while q:
        pathlen += 1
        for _ in range(len(q)):
            u = q.popleft()
            for v in g[u]:
                if v == n - 1:
                    return pathlen
                if v not in q:
                    q.append(v)
    return pathlen


# class Solution:
#     def jump(self, n: List[int]) -> int:
#         currEnd = currFarthest = jump = 0
#         l = len(n)
#         for i in range(l - 1):
#             currFarthest = max(currFarthest, i + n[i])
#             if i == currEnd:
#                 jump += 1
#                 currEnd = currFarthest
#
#         return jump


print(jump([2, 3, 1, 1, 4]))
# dp        0  1  1  2  2

print(jump([2, 3, 0, 1, 4]))
# dp        0  1  1  2  2


print(jump1([2, 3, 1, 1, 4]))
print(jump1([4, 3, 1, 1, 4]))
print(jump1([1]))
