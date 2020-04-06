def lcs_iter(s1, s2):
    dp_arr = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    lcs_arr = [[' '] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
                lcs_arr[i][j] = '↖'
            else:
                if dp_arr[i - 1][j] > dp_arr[i][j - 1]:
                    dp_arr[i][j] = dp_arr[i - 1][j]
                    lcs_arr[i][j] = '↑'
                else:
                    dp_arr[i][j] = dp_arr[i][j - 1]
                    lcs_arr[i][j] = '←'
    # for e in dp_arr:
    #     print(e)
    # print(dp_arr)
    # for e in lcs_arr:
    #     print(e)
    # print(lcs_arr)
    # return dp_arr[i][j]
    # ********* find string
    maxlen = dp_arr[i][j]
    lcs_str = ''
    while lcs_arr[i][j] != ' ':
        if lcs_arr[i][j] == '↖':  # diagonal - up-left
            lcs_str += s1[i - 1]
            i -= 1
            j -= 1
        elif lcs_arr[i][j] == '↑':  # go up
            i -= 1
        elif lcs_arr[i][j] == '←':  # go left
            j -= 1
    print(lcs_str[::-1])
    # return maxlen
    return lcs_str[::-1]

    # str_arr = []
    # for i in range(len(s1), 0, -1):
    #     for j in range(len(s2), 0, -1):
    #         if dp_arr[i][j] == maxlen and s1[i - 1] == s2[j - 1]:
    #             str_arr.append(get_lcs(dp_arr, s1, s2, i, j, maxlen))
    # return maxlen, str_arr


# def lcs_iter(s1, s2):
#     dp_arr = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
#
#     for i in range(1, len(s1) + 1):
#         for j in range(1, len(s2) + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
#             else:
#                 dp_arr[i][j] = max(dp_arr[i][j - 1], dp_arr[i - 1][j])
#     # for e in dp_arr:
#     #     print(e)
#
#     return dp_arr[i][j]


# def lcs_iter(s1, s2):
#     dp_arr = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
#
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 dp_arr[i + 1][j + 1] = dp_arr[i][j] + 1
#             else:
#                 dp_arr[i + 1][j + 1] = max(dp_arr[i][j + 1], dp_arr[i + 1][j])
#     # for e in dp_arr:
#     #     print(e)
#     return dp_arr[-1][-1]


# def lcs_iter(s1, s2):
#     s1 = ' ' + s1
#     s2 = ' ' + s2
#     dp_arr = [[0] * (len(s2)) for _ in range(len(s1))]
#
#     for i in range(1, len(s1)):
#         for j in range(1, len(s2)):
#             if s1[i] == s2[j]:
#                 dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
#             else:
#                 dp_arr[i][j] = max(dp_arr[i][j - 1], dp_arr[i - 1][j])
#     for e in dp_arr:
#         print(e)
#     return dp_arr[i][j]


# def lcs_iter(s1, s2):
#     s1 = ' ' + s1
#     s2 = ' ' + s2
#     dp_arr = [[0] * (len(s2)) for _ in range(len(s1))]
#
#     for i in range(1, len(s1)):
#         for j in range(1, len(s2)):
#             if s1[i] == s2[j]:
#                 dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
#             else:
#                 dp_arr[i][j] = max(dp_arr[i][j - 1], dp_arr[i - 1][j])
#     # for e in dp_arr:
#     #     print(e)
#     return dp_arr[i][j]


# def lcs_iter(s1, s2):
#     s1 = ' ' + s1
#     s2 = ' ' + s2
#     dp_arr = [[0] * (len(s2)) for _ in range(len(s1))]
#
#     for i in range(1, len(s1)):
#         for j in range(1, len(s2)):
#             if s1[i] == s2[j]:
#                 dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
#             else:
#                 dp_arr[i][j] = max(dp_arr[i][j - 1], dp_arr[i - 1][j])
#     for e in dp_arr:
#         print(e)
#     lcs = dp_arr[i][j]
#     # *****find the string one match only
#     lcs_str = ''
#     str_idx = lcs
#     for i in range(len(s2) - 1, -1, -1):
#         for j in range(len(s1) - 1, -1, -1):
#             if s1[i] == s2[j] and dp_arr[i][j] == str_idx:
#                 lcs_str += s1[i]
#                 str_idx -= 1
#             if str_idx == 0:
#                 break
#         if str_idx == 0:
#             break
#     return lcs, lcs_str[::-1]


# def lcs_iter(s1, s2):
#     dp_arr = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
#
#     for i in range(1, len(s1) + 1):
#         for j in range(1, len(s2) + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
#             else:
#                 dp_arr[i][j] = max(dp_arr[i - 1][j], dp_arr[i][j - 1])
#     # for e in dp_arr:
#     #     print(e)
#     return dp_arr[-1][-1]

# def lcs(s1, s2):
#     dp_arr = [0] * (len(s2) + 1)
#
#     for i in range(1, len(s1) + 1):
#         for j in range(1, len(s2) + 1):
#             if s1[i - 1] == s2[j - 1]:
#                 dp_arr[j] = dp_arr[j - 1] + 1
#             else:
#                 dp_arr[j] = max(dp_arr[j], dp_arr[j - 1])
#     print(dp_arr)
#     return dp_arr[len(s2)]


# incorrect
# def lcs_iter(s1, s2):
#     dp_arr = [0] * (len(s2) + 1)
#
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i] == s2[j]:
#                 dp_arr[j + 1] = dp_arr[j + 1] + 1
#             else:
#                 dp_arr[j + 1] = max(dp_arr[j + 1], dp_arr[j])
#         print(dp_arr)
#     return dp_arr[-1]


# def lcs_iter(s1, s2):
#     s1 = ' ' + s1
#     s2 = ' ' + s2
#     dp_arr = [[0] * (len(s2)) for _ in range(len(s1))]
#     str_arr = []
#
#     for i in range(1, len(s1)):
#         for j in range(1, len(s2)):
#             if s1[i] == s2[j]:
#                 dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
#                 if dp_arr[i][j] > len(str_arr):
#                     str_arr.append(s1[i])
#                 else:
#                     str_arr[dp_arr[i][j] - 1] += s1[i]
#             else:
#                 dp_arr[i][j] = max(dp_arr[i][j - 1], dp_arr[i - 1][j])
#     for e in dp_arr:
#         print(e)
#     print('')
#     print(str_arr)
#     # for e in str_arr:
#     #     print(e)
#     new_str_arr = [''] * len(str_arr[0])
#     for strng in str_arr:
#         for j in range(len(strng)):
#             new_str_arr[j] += strng[j]
#     print(new_str_arr)
#     return dp_arr[i][j], new_str_arr


# def get_lcs(dp_arr, s1, s2, i, j, slen):
#     lcs = s1[i - 1]
#     slen -= 1
#     while slen > 0:
#         i -= 1
#         j -= 1
#         for row in range(i, -1, -1):
#             for col in range(j, -1, -1):
#                 if dp_arr[i][j] == slen and s1[i - 1] == s2[j - 1]:
#                     lcs += s1[i - 1]
#                     slen -= 1
#                     # break
#             # if slen == 0:
#             #     break
#     return lcs[::-1]


def get_lcs(dp_arr, s1, s2, row, col, slen):
    lcs = s1[row - 1]
    slen -= 1
    for i in range(row, -1, -1):
        for j in range(col, -1, -1):
            if dp_arr[i][j] == slen and s1[i - 1] == s2[j - 1]:
                lcs += s1[i - 1]
                slen -= 1
                if slen == 0:
                    return lcs[::-1]
                i -= 1
                j -= 1


if __name__ == '__main__':
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print(lcs_iter(str1, str2))

    #       G  X  T  X  A  Y  B
    #   [0, 0, 0, 0, 0, 0, 0, 0]
    # A [0, 0, 0, 0, 0, 1, 1, 1]
    # G [0, 1, 1, 1, 1, 1, 1, 1]
    # G [0, 1, 1, 1, 1, 1, 1, 1]
    # T [0, 1, 1, 2, 2, 2, 2, 2]
    # A [0, 1, 1, 2, 2, 3, 3, 3]
    # B [0, 1, 1, 2, 2, 3, 3, 4]

    #     ø   G   X   T   X   A   Y   B
    #   ┌───┬───┬───┬───┬───┬───┬───┬───┐
    # ø │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │
    #   ├───┼───┼───┼───┼───┼───┼───┼───┤
    # A │ 0 │ 0 │ 0 │ 0 │ 0 │ 1 │ 1 │ 1 │
    #   ├───┼───┼───┼───┼───┼───┼───┼───┤
    # G │ 0 │ 1 │ 1 │ 1 │ 1 │ 1 │ 1 │ 1 │
    #   ├───┼───┼───┼───┼───┼───┼───┼───┤
    # G │ 0 │ 1 │ 1 │ 1 │ 1 │ 1 │ 1 │ 1 │
    #   ├───┼───┼───┼───┼───┼───┼───┼───┤
    # T │ 0 │ 1 │ 1 │ 2 │ 2 │ 2 │ 2 │ 2 │
    #   ├───┼───┼───┼───┼───┼───┼───┼───┤
    # A │ 0 │ 1 │ 1 │ 2 │ 2 │ 3 │ 3 │ 3 │
    #   ├───┼───┼───┼───┼───┼───┼───┼───┤
    # B │ 0 │ 1 │ 1 │ 2 │ 2 │ 3 │ 3 │ 4 │
    #   └───┴───┴───┴───┴───┴───┴───┴───┘

    # str1 = "abcxyz"
    # str2 = "xyzabc"
    # print(lcs_iter(str1, str2))
    #       x  y  z  a  b  c
    #   [0, 0, 0, 0, 0, 0, 0]
    # a [0, 0, 0, 0, 1, 1, 1]
    # b [0, 0, 0, 0, 1, 2, 2]
    # c [0, 0, 0, 0, 1, 2, 3]
    # x [0, 1, 1, 1, 1, 2, 3]
    # y [0, 1, 2, 2, 2, 2, 3]
    # z [0, 1, 2, 3, 3, 3, 3]

    # str1 = "abxcyz"
    # str2 = "xyzabc"
    # print(lcs_iter(str1, str2))
    #       x  y  z  a  b  c
    #   [0, 0, 0, 0, 0, 0, 0]
    # a [0, 0, 0, 0, 1, 1, 1]
    # b [0, 0, 0, 0, 1, 2, 2]
    # x [0, 1, 1, 1, 1, 2, 2]
    # c [0, 1, 1, 1, 1, 2, 3]
    # y [0, 1, 2, 2, 2, 2, 3]
    # z [0, 1, 2, 3, 3, 3, 3]

    # str1 = "axbycz"
    # str2 = "xyzabc"
    # print(lcs_iter(str1, str2))
    #       x  y  z  a  b  c
    #   [0, 0, 0, 0, 0, 0, 0]
    # a [0, 0, 0, 0, 1, 1, 1]
    # x [0, 1, 1, 1, 1, 1, 1]
    # b [0, 1, 1, 1, 1, 2, 2]
    # y [0, 1, 2, 2, 2, 2, 2]
    # c [0, 1, 2, 2, 2, 2, 3]
    # z [0, 1, 2, 3, 3, 3, 3]

    # str1 = "axbycz"
    # str2 = "xaybzc"
    # print(lcs_iter(str1, str2))
    #       x  a  y  b  z  c
    #   [0, 0, 0, 0, 0, 0, 0]
    # a [0, 0, 1, 1, 1, 1, 1]
    # x [0, 1, 1, 1, 1, 1, 1]
    # b [0, 1, 1, 1, 2, 2, 2]
    # y [0, 1, 1, 2, 2, 2, 2]
    # c [0, 1, 1, 2, 2, 2, 3]
    # z [0, 1, 1, 2, 2, 3, 3]

# dp_arr = [[0, 0, 0, 0, 0, 0, 0],
#           [0, 0, 1, 1, 1, 1, 1],
#           [0, 1, 1, 1, 1, 1, 1],
#           [0, 1, 1, 1, 2, 2, 2],
#           [0, 1, 1, 2, 2, 2, 2],
#           [0, 1, 1, 2, 2, 2, 3],
#           [0, 1, 1, 2, 2, 3, 3]]
# print(get_lcs(dp_arr, 'axbycz', 'xaybzc', 6, 5, 3))
# print(get_lcs(dp_arr, 'axbycz', 'xaybzc', 5, 6, 3))

# str1 = "zxcvqkfkkwgjejrgtyasd"
# str2 = "qsdwexcvxcvriooptytzz"
# print(lcs_iter(str1, str2))
