# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and
# return its area.
#
# Example:
#
# Input:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
from math import sqrt


# def maximal_square(matrix):
#     dp = matrix.copy()
#     max_sq = 0
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if (i == 0 or j == 0) and dp[i][j] != 0:
#                 max_sq = 1
#             elif dp[i][j] != 0 and dp[i - 1][j - 1] != 0:
#                 prev_val = int(sqrt(dp[i - 1][j - 1]))
#                 if all([dp[i][j - (k + 1)] != 0 and dp[i - (k + 1)][j] != 0 for k in range(prev_val)]):
#                     dp[i][j] = (prev_val + 1) ** 2
#                     max_sq = max(max_sq, dp[i][j])
#     for e in dp:
#         print(e)
#     return max_sq


def maximal_square(matrix):
    dp = matrix.copy()
    # max_sq = 1 if 1 can be found in first row or first col of matrix
    max_sq = 1 if 1 in dp[0] or any([row[0] == 1 for row in dp]) else 0

    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if dp[i][j] != 0 and max_sq == 0:
                max_sq = 1
            if dp[i][j] != 0 and dp[i - 1][j - 1] != 0:
                prev_val = int(sqrt(dp[i - 1][j - 1]))
                all_ones = True
                for k in range(prev_val):
                    if dp[i][j - (k + 1)] == 0 or dp[i - (k + 1)][j] == 0:
                        all_ones = False
                        break
                if all_ones:
                    dp[i][j] = (prev_val + 1) ** 2
                    max_sq = max(max_sq, dp[i][j])
                else:
                    if k:
                        dp[i][j] = (k + 1) ** 2
                        max_sq = max(max_sq, dp[i][j])
    for e in dp:
        print(e)
    return max_sq


# 1 1
# 4 2
# 9 3


# matrix = [[0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 1],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0]]
# matrix = [[1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 1, 1, 1, 1]]
# matrix = [[1, 0, 1, 0, 0],
#           [1, 0, 1, 1, 1],
#           [1, 1, 1, 1, 1],
#           [1, 0, 0, 1, 0]]
matrix = [[0, 0, 0, 1],
          [1, 1, 0, 1],
          [1, 1, 1, 1],
          [0, 1, 1, 1],
          [0, 1, 1, 1]]
print(maximal_square(matrix))
