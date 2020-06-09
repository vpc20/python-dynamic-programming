# The thief has found himself a new place for his thievery again. There is only one entrance to this area,
# called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief
# realized that "all houses in this place forms a binary tree". It will automatically contact the police if two
# directly-linked houses were broken into on the same night.
#
# Determine the maximum amount of money the thief can rob tonight without alerting the police.
#
# Example 1:
#
# Input: [3,2,3,null,3,null,1]
#
#      3
#     / \
#    2   3
#     \   \
#      3   1
#
# Output: 7
# Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
#
# Example 2:
#
# Input: [3,4,5,1,3,null,1]
#
#      3
#     / \
#    4   5
#   / \   \
#  1   3   1
#
# Output: 9
# Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
from collections import deque

from BinaryTrees import TreeNode, print_preorder


# incorrect
# def rob(root):
#     def dfs(node, lvlsw):
#         nonlocal maxval1, maxval2
#         if lvlsw:
#             maxval1 += node.val
#         else:
#             maxval2 += node.val
#         if node.left:
#             dfs(node.left, not lvlsw)
#         if node.right:
#             dfs(node.right, not lvlsw)
#
#     if root is None:
#         return 0
#     maxval1 = maxval2 = 0
#     dfs(root, True)
#     return max(maxval1, maxval2)

def rob(root):
    if root is None:
        return 0

    q = deque([root])
    lvl_sums = []
    while q:  # level order traversal
        lvl_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            lvl_sum += node.val  # accumulate sum per level
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        lvl_sums.append(lvl_sum)
    # dp, get max sum with no adjacent elements of lvl_sums
    if len(lvl_sums) == 1:
        return lvl_sums[0]
    n = len(lvl_sums)
    dp = [0] * n
    dp[0] = lvl_sums[0]
    dp[1] = max(lvl_sums[0], lvl_sums[1])
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + lvl_sums[i])
    return dp[-1]


# arr = [3, 2, 3, None, 3, None, 1]
# arr = [3, 4, 5, 1, 3, None, 1]
# arr = [4, 1, None, 2, None, None, None, 3]
# arr = [1]
arr = [3, 1, None, 2, None, None, None, None, 4]
nodes = [TreeNode(v) if v else None for v in arr]
root = nodes[0]
for i, node in enumerate(nodes):
    left_idx = i * 2 + 1
    if left_idx < len(arr) and arr[i] is not None:
        node.left = nodes[left_idx]
    right_idx = i * 2 + 2
    if right_idx < len(arr) and arr[i] is not None:
        node.right = nodes[right_idx]

print_preorder(root)
print(rob(root))
