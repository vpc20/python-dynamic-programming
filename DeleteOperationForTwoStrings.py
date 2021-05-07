# Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2
# the same.
#
# In one step, you can delete exactly one character in either string.
#
# Example 1:
# Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
#
# Example 2:
# Input: word1 = "leetcode", word2 = "etco"
# Output: 4
#
# Constraints:
# 1 <= word1.length, word2.length <= 500
# word1 and word2 consist of only lowercase English letters.
from itertools import combinations, product


def min_distance_naive(word1, word2):
    w1 = []
    for r in range(1, len(word1) + 1):
        for comb in combinations(word1, r):
            w1.append(comb)
    w2 = []
    for r in range(1, len(word1) + 1):
        for comb in combinations(word2, r):
            w2.append(comb)
    # print(w1)
    # print(w2)

    maxlen = 0
    p = [prod for prod in product(w1, w2) if prod[0] == prod[1]]
    # print(p)
    for s1, s2 in p:
        totlen = len(s1) + len(s2)
        maxlen = max(maxlen, totlen)

    initial_len = len(word1) + len(word2)
    return initial_len - maxlen


def min_distance(word1, word2):
    m = len(word1) + 1
    n = len(word2) + 1

    dp = [[0] * n for _ in range(m)]
    for i in range(1, m):
        dp[i][0] = i
    for j in range(1, n):
        dp[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1)
    # for e in dp:
    #     print(e)
    # print('')
    return dp[-1][-1]


assert min_distance_naive("sea", "eat") == 2
assert min_distance_naive("leetcode", "etco") == 4
assert min_distance_naive("x", "y") == 2

assert min_distance("sea", "eat") == 2
assert min_distance("leetcode", "etco") == 4
assert min_distance("x", "y") == 2
