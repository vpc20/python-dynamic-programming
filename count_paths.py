# Dynamic Programming – Count all paths from top left to bottom right of a mXn matrix
# Objective: Given two dimensional matrix, write an algorithm to count all possible
# paths from top left corner to bottom-right corner. You are allowed to move only
# in two directions, move right OR move down.


def count_path(m, n):
    if m == 0 and n == 0:
        return 0
    if m == 0 or n == 0:
        return 1
    return count_path(m - 1, n) + count_path(m, n - 1)


def count_path_iter(m, n):
    dp_arr = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp_arr[i][0] = 1
    for j in range(1, n + 1):
        dp_arr[0][j] = 1
    # path_arr = [[[]] * (n + 1) for _ in range(m + 1)] # incorrect
    path_arr = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        path_arr[i][0] = ['d' * i]
    for j in range(1, n + 1):
        path_arr[0][j] = ['r' * j]
    # for item in path_arr:
    #     print(item)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp_arr[i][j] = dp_arr[i - 1][j] + dp_arr[i][j - 1]
            path_arr[i][j] = [s + 'r' for s in path_arr[i][j - 1]] + \
                             [s + 'd' for s in path_arr[i - 1][j]]
    # print(path_arr)
    # for item in path_arr:
    #     print(item)
    return dp_arr[-1][-1], path_arr[-1][-1]


print(count_path(0, 0))
print(count_path(0, 1))
print(count_path(0, 2))
print(count_path(0, 3))
print(count_path(1, 0))
print(count_path(2, 0))
print(count_path(3, 0))
print(count_path(1, 1))
print(count_path(1, 2))
print(count_path(2, 1))
print(count_path(1, 3))
print(count_path(3, 1))
print(count_path(2, 2))
print(count_path(3, 3))
# print(count_path_iter(2, 2))
# print(count_path(1, 2))
print(count_path_iter(2, 1))
