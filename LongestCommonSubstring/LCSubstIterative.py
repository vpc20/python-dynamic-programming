def lcsubst_iter(s1, s2):
    s1 = ' ' + s1
    s2 = ' ' + s2
    dp_arr = [[0] * (len(s2)) for _ in range(len(s1))]
    maxlen = 0

    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if s1[i] == s2[j]:
                dp_arr[i][j] = dp_arr[i - 1][j - 1] + 1
                maxlen = max(maxlen, dp_arr[i][j])
    # print(dp_arr)
    # for e in dp_arr:
    #     print(e)
    # find all the strings
    str_arr = []
    for j in range(len(s2) - 1, -1, -1):
        for i in range(len(s1) - 1, -1, -1):
            if s1[i] == s2[j] and dp_arr[i][j] == maxlen:
                str_arr.append(get_lcsubst(s1, i, maxlen))
    return maxlen  # , str_arr


def get_lcsubst(s, i, strlen):
    lcsubst = s[i]
    for _ in range(strlen - 1):
        i -= 1
        lcsubst += s[i]
    return lcsubst[::-1]


if __name__ == '__main__':
    print(lcsubst_iter('xyzabcd', 'abcdxyz'))
    #       0   1   2   3   4   5   6   7
    #       ø   a   b   c   d   x   y   z
    #     ┌───┬───┬───┬───┬───┬───┬───┬───┐
    # 0 ø │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │
    #     ├───┼───┼───┼───┼───┼───┼───┼───┤
    # 1 x │ 0 │ 0 │ 0 │ 0 │ 0 │ 1 │ 0 │ 0 │
    #     ├───┼───┼───┼───┼───┼───┼───┼───┤
    # 2 y │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 2 │ 0 │
    #     ├───┼───┼───┼───┼───┼───┼───┼───┤
    # 3 z │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │ 3 │
    #     ├───┼───┼───┼───┼───┼───┼───┼───┤
    # 4 a │ 0 │ 1 │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │
    #     ├───┼───┼───┼───┼───┼───┼───┼───┤
    # 5 b │ 0 │ 0 │ 2 │ 0 │ 0 │ 0 │ 0 │ 0 │
    #     ├───┼───┼───┼───┼───┼───┼───┼───┤
    # 6 c │ 0 │ 0 │ 0 │ 3 │ 0 │ 0 │ 0 │ 0 │
    #     ├───┼───┼───┼───┼───┼───┼───┼───┤
    # 7 d │ 0 │ 0 │ 0 │ 0 │ 4 │ 0 │ 0 │ 0 │
    #     └───┴───┴───┴───┴───┴───┴───┴───┘

    # print(lcsubst_iter('wxyzabcd', 'abcdwxyz'))
    # print(lcsubst_iter('ab', 'ba'))
    # print(lcsubst_iter('asdabcdefghjk', 'kjhgfabcdedsa'))
    # print(lcsubst_iter('xyzabcdqwe', 'abcdxyzqwe'))

    # print(lcsubst_iter('longmatchingstringabcdefghijklmnop', 'longmatchingstringponmlkjihgfedcba'))

    #       a  b  c  d  x  y  z
    #   [0, 0, 0, 0, 0, 0, 0, 0]
    # x [0, 0, 0, 0, 0, 1, 0, 0]
    # y [0, 0, 0, 0, 0, 0, 2, 0]
    # z [0, 0, 0, 0, 0, 0, 0, 3]
    # a [0, 1, 0, 0, 0, 0, 0, 0]
    # b [0, 0, 2, 0, 0, 0, 0, 0]
    # c [0, 0, 0, 3, 0, 0, 0, 0]
    # d [0, 0, 0, 0, 4, 0, 0, 0]

    # print(get_lcsubst('xyzabcd', 6, 4))
