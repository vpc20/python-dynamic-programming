# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right
# which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.
#
# Example:
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

# def min_path_sum(arr):
#     # dp_arr = [[0] * (len(arr[0])) for _ in range(len(arr))]
#     dp_arr = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]
#
#     dp_arr[0][0] = arr[0][0]
#     for j in range(1, len(arr[0])): # init dp_arr first row
#         dp_arr[0][j] = arr[0][j] + dp_arr[0][j - 1]
#     for i in range(1, len(arr)): # init dp_arr first col
#         dp_arr[i][0] = arr[i][0] + dp_arr[i - 1][0]
#
#     for i in range(1, len(arr)):
#         for j in range(1, len(arr[0])):
#             dp_arr[i][j] = min(arr[i][j] + dp_arr[i][j - 1], arr[i][j] + dp_arr[i - 1][j])
#     for e in dp_arr:
#         print(e)
#     return dp_arr[-1][-1]


def min_path_sum(grid):
    dp = grid.copy()
    numrows = len(grid)
    numcols = len(grid[0])

    for j in range(1, numcols):  # init dp first row
        dp[0][j] += dp[0][j - 1]
    for i in range(1, numrows):  # init dp first col
        dp[i][0] += dp[i - 1][0]

    for i in range(1, numrows):
        for j in range(1, numcols):
            dp[i][j] = min(dp[i][j] + dp[i][j - 1], dp[i][j] + dp[i - 1][j])
    for e in dp:
        print(e)
    return dp[-1][-1]


# def min_path_sum(arr, i, j):
#     if i == 0 or j == 0:
#         return arr[0][0]
#     return min(min_path_sum(arr, i - 1, j), min_path_sum(arr, i, j - 1))


arr = [[1, 3, 1],
       [1, 5, 1],
       [4, 2, 1]]
print(min_path_sum(arr))
