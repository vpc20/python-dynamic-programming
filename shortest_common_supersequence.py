# Shortest Common Supersequence
#
# The shortest common supersequence (SCS) of T and P is the smallest sequence L such that both T and
# P are a subsequence of L.
#
# Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.
#
# Examples :
#
# Input:   str1 = "geek",  str2 = "eke"
# Output: "geeke"
#
# Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
# Output:  "AGXGTXAYB"
from itertools import permutations


def is_subsequence(sub, s):
    j = 0
    for i in range(len(s)):
        if sub[j] == s[i]:
            j += 1
            if j == len(sub):
                return True
    return False


# def is_subsequence2(sub, s):
#     start = 0
#     for i in range(len(sub)):
#         for j in range(start, len(s)):
#             if sub[i] == s[j]:
#                 start = j + 1
#                 break
#         else:
#             return False
#     return True

def scs_naive(s1, s2):
    sarr = []

    # s12 = s1 + s2
    # for r in range(min(len(s1), len(s2)), len(s12) + 1):
    #     sarr += [''.join(comb) for comb in combinations(s12, r)]
    # s21 = s2 + s1
    # for r in range(min(len(s1), len(s2)), len(s21) + 1):

    #     sarr += [''.join(comb) for comb in combinations(s21, r)]

    s = s1 + s2
    for r in range(min(len(s1), len(s2)), len(s) + 1):
        sarr += [''.join(comb) for comb in permutations(s, r)]
    # print(len(sarr))
    for e in sarr:
        if is_subsequence(s1, e) and is_subsequence(s2, e):
            print(e)
            return len(e)


def scs_recur(s1, s2):
    if not s1 and not s2:
        return 0
    if s1 and not s2:
        return len(s1)
    if s2 and not s1:
        return len(s2)

    if s1[-1] == s2[-1]:
        return 1 + scs_recur(s1[:-1], s2[:-1])
    else:
        return 1 + min(scs_recur(s1[:-1], s2), scs_recur(s1, s2[:-1]))


if __name__ == '__main__':
    # print(scs('a', 'a'))

    # abc def
    # abcdef
    # defabc

    # abc ''    abc
    # ab c    abc acb  cab
    # ab cd   abcd acbd cabd acdb cdab
    # abc d   abcd  abdc adbc dabc
    # a  cde  acde  cade cdae cdea
    # abc de  abcde

    # print(scs_recur('geek', 'eke'))
    # print(scs_naive('geek', 'eke'))
    print(scs_naive('ecb', 'cee'))
    print(is_subsequence('ca', 'abc'))

