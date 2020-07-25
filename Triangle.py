# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the
# row below.
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the
# triangle.
#
# 0 -> 0, 1
# 0 -> 0, 1   1 -> 1, 2
# 0 -> 0, 1   1 -> 1, 2  2 -> 2, 3


# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# [
#   [2],
#   [3,4],
#   [6,5,7],
#   [4,1,8,3]
# ]

def minimum_total(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:
                triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])
    return min(triangle[-1])


# import sys
# from collections import defaultdict, deque
#
#
# class Node:
#     def __init__(self, val):
#         self.val = val
#
#     def __repr__(self):
#         return f'Node({self.val})'
#
#
# def minimum_total(triangle):
#     def dfs(u, acc):
#         nonlocal minval
#         for v in g[u]:
#             if v not in visited:
#                 if v in list(g):
#                     dfs(v, acc + v.val)
#                 else:
#                     print(acc + v.val)
#                     minval = min(minval, acc + v.val)
#                 visited.add(v)
#
#     root = Node(triangle[0][0])
#     queue = deque([root])
#     g = defaultdict(list)
#     for i in range(len(triangle) - 1):
#         for j in range(len(triangle[i])):
#             node = queue.popleft()
#
#             lnode = Node(triangle[i + 1][j])
#             g[node].append(lnode)
#             queue.append(lnode)
#             rnode = Node(triangle[i + 1][j + 1])
#             g[node].append(rnode)
#
#             if j == len(triangle[i]) - 1:
#                 queue.append(rnode)
#
#     for k in g:
#         print(k, g[k])
#
#     minval = sys.maxsize
#     visited = set()
#     dfs(root, root.val)
#     return minval


# print(minimum_total([[2],
#                      [3, 4],
#                      [6, 5, 7]]))
# print(minimum_total([[1],
#                      [1, 1],
#                      [1, 1, 1],
#                      [1, 1, 1, 1]]))

print(minimum_total([[2],
                     [3, 4],
                     [6, 5, 7],
                     [4, 1, 8, 3]]))

# print(minimum_total([[1],
#                      [2, 3]]))

# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]

# [
#         [2],
#      [3,    4],
#    [6, 5, 5,  7],
#   [4,1, 1, 8, 8,3]
# ]
