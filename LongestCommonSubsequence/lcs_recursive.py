# A Naive recursive Python implementation of LCS problem


# def lcs(s1, s2, m, n):
#     if m == 0 or n == 0:
#         return 0
#     elif s1[m - 1] == s2[n - 1]:
#         return 1 + lcs(s1, s2, m - 1, n - 1)
#     else:
#         return max(lcs(s1, s2, m, n - 1), lcs(s1, s2, m - 1, n))


# compare last char
# remove last char in recursive function calls
from functools import lru_cache


@lru_cache(maxsize=1000)
def lcs_recur(s1, s2):
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + lcs_recur(s1[:-1], s2[:-1])
    return max(lcs_recur(s1, s2[:-1]), lcs_recur(s1[:-1], s2))


# compare first char
# pass string tail in recursive function calls
# def lcs_recur(s1, s2):
#     if not s1 or not s2:
#         return 0
#     if s1[0] == s2[0]:
#         return 1 + lcs_recur(s1[1:], s2[1:])
#     return max(lcs_recur(s1[1:], s2), lcs_recur(s1, s2[1:]))


# compare first char
# pass string tail in recursive function calls
# def lcs(s1, s2, results={}):
#     if not s1 or not s2:
#         return 0
#     if (s1, s2) in results:
#         return results[(s1, s2)]
#     if s1[0] == s2[0]:
#         count = 1 + lcs(s1[1:], s2[1:])
#         results[(s1, s2)] = count
#         return count
#     return max(lcs(s1[1:], s2), lcs(s1, s2[1:]))


# compare first char******incorrect
# pass string tail in recursive function calls
# output string instead of string length
# def lcs_str(s1, s2):
#     if not s1 or not s2:
#         return ''
#     if s1[0] == s2[0]:
#         return s1[0] + lcs_str(s1[1:], s2[1:])
#     if len(s1) > len(s2):
#         return lcs_str(s1[1:], s2)
#     else:
#         return lcs_str(s1, s2[1:])


# s1 = "AGGTAB"
# s2 = "GXTXAYB"
# print("Length of LCS is ", lcs(s1, s2, len(s1), len(s2)))

if __name__ == '__main__':
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print(lcs_recur(str1, str2))
    # str1 = "fdak"
    # str2 = "pvsklkn"
    # print(lcs_recur(str1, str2))
    # print(lcs_recur('cxv', 'cv'))
