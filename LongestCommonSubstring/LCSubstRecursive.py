# def lcsubst_recur(s1, s2, count=0):
#     if not s1 or not s2:
#         return count
#     if s1[0] == s2[0]:
#         count = lcsubst_recur(s1[1:], s2[1:], count + 1)
#     return max(count, max(lcsubst_recur(s1[1:], s2), lcsubst_recur(s1, s2[1:])))


def lcsubst_recur(s1, s2, count=0):
    if not s1 or not s2:
        return count
    if s1[-1] == s2[-1]:
        count = lcsubst_recur(s1[:-1], s2[:-1], count + 1)
    return max(count, max(lcsubst_recur(s1[:-1], s2), lcsubst_recur(s1, s2[:-1])))


# def lcsubst_recur(s1, s2):  # incorrect
#     def _lcsubst_recur(s1, s2):
#         nonlocal maxlen
#         if not s1 or not s2:
#             return 0
#         if s1[-1] == s2[-1]:
#             strlen = 1 + _lcsubst_recur(s1[:-1], s2[:-1])
#             maxlen = max(maxlen, strlen)
#             return strlen
#         return max(_lcsubst_recur(s1[:-1], s2), _lcsubst_recur(s1, s2[:-1]))
#
#     maxlen = 0
#     _lcsubst_recur(s1, s2)
#     return maxlen


if __name__ == '__main__':
    # print(lcsubst_recur('ab', 'ab'))
    # print(lcsubst_recur('abcd', 'xzzxcv'))
    # print(lcsubst_recur('tc', 'uc'))
    # print(lcsubst_recur('tcab', 'ucxz'))

    # print(lcsubst_recur('', ''))
    # print(lcsubst_recur('c', ''))
    # print(lcsubst_recur('', 'c'))
    # print(lcsubst_recur('c', 'x'))
    # print(lcsubst_recur('c', 'xc'))
    # print(lcsubst_recur('cx', 'xc'))
    # print(lcsubst_recur('cxv', 'xc'))
    print(lcsubst_recur('cxv', 'cv'))
    print(lcsubst_recur('cx', 'c'))
    print(lcsubst_recur('cx', 'cv'))
    print(lcsubst_recur('cxv', 'c'))

    # print(lcsubst_recur('tcaakv', 'uczvbl'))
    # print(lcsubst_recur('tcaak', 'uczvbl'))
    # print(lcsubst_recur('tcaakv', 'uczvb'))

    # print(lcsubst_recur('cv', 'cv'))

    # print(lcsubst_recur('tcaak', 'uczvb'))
    # print(lcsubst_recur('tcaa', 'uczvb'))
    # print(lcsubst_recur('tcaak', 'uczv'))
    #
    # print(lcsubst_recur('tcaa', 'uczv'))
    # print(lcsubst_recur('tca', 'uczv'))
    # print(lcsubst_recur('tcaa', 'ucz'))
    #
    # print(lcsubst_recur('tca', 'ucz'))
    # print(lcsubst_recur('tc', 'ucz'))
    # print(lcsubst_recur('tca', 'uc'))
    #
    # print(lcsubst_recur('tc', 'uc'))
    # print(lcsubst_recur('t', 'uc'))
    # print(lcsubst_recur('tc', 'u'))
    #
    # print(lcsubst_recur('t', 'c'))

    # print(lcsubst_recur('xyzabcd', 'abcdxyz'))
    # print(lcsubst_recur('aczt', 'bnnznd'))
    # print(lcsubst_recur('wxyzabcd', 'abcdwxyz'))
    # print(lcsubst_recur('xyzabcdqwe', 'abcdxyzqwe'))
    # print(lcsubst_recur('asdabcdefghjk', 'kjhgfabcdedsa'))
    # print(lcsubst_recur('longmatchingstringabcdefghijklmnop', 'longmatchingstringponmlkjihgfedcba'))

    # s1 = 'vwxyz'
    # s2 = 'abcde'
    # for i in range(len(s1)):
    #     str1 = s1[:i] + s2 + s1[i:]
    #     for j in range(len(s2)):
    #         str2 = s1[:j] + s2 + s1[j:]
    #         if lcsubst_recur1(str1, str2) != lcsubst_recur2(str1, str2):
    #             print(str1, str2)
    #             print(lcsubst_recur1(str1, str2))
    #             print(lcsubst_recur2(str1, str2))

    # print(lcsubst_recur2('ab', 'ab'))

    #       a  b  c  d  x  y  z
    #   [0, 0, 0, 0, 0, 0, 0, 0]
    # x [0, 0, 0, 0, 0, 1, 0, 0]
    # y [0, 0, 0, 0, 0, 0, 2, 0]
    # z [0, 0, 0, 0, 0, 0, 0, 3]
    # a [0, 1, 0, 0, 0, 0, 0, 0]
    # b [0, 0, 2, 0, 0, 0, 0, 0]
    # c [0, 0, 0, 3, 0, 0, 0, 0]
    # d [0, 0, 0, 0, 4, 0, 0, 0]
