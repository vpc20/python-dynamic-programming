from itertools import combinations


def is_subsequence(sub, s):
    j = 0
    for i in range(len(s)):
        if sub[j] == s[i]:
            j += 1
            if j == len(sub):
                return True
    return False

# def isSubSequence(str1, str2, m, n):
#     j = 0  # Index of str1
#     i = 0  # Index of str2
#
#     while j < m and i < n:
#         if str1[j] == str2[i]:
#             j = j + 1
#         i = i + 1
#
#     return j == m


def subsequence(s):
    subseq = []
    for i in range(1, len(s) + 1):
        for comb in combinations(s, i):
            subseq.append(''.join(comb))
    return subseq


def lcs_naive(s1, s2):
    maxlen = 0
    for str1 in subsequence(s1):
        for str2 in subsequence(s2):
            if str1 == str2:
                maxlen = max(maxlen, len(str1))
    return maxlen


if __name__ == '__main__':
    str1 = "goort"
    str2 = "geoeksfakgoortadfghr"
    # m = len(str1)
    # n = len(str2)
    print(is_subsequence(str1, str2))
    print(subsequence('geoeksfakgoort'))

    strn1 = "AGGTAB"
    strn2 = "GXTXAYB"
    # strn1 = "abcdqowie"
    # strn2 = "apodpodbx"
    print(lcs_naive(strn1, strn2))
