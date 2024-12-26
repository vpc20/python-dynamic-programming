# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none)
# deleted without changing the relative order of the remaining characters.(eg, "ace" is a subsequence of "abcde"
# while "aec" is not).A common subsequence of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence, return 0.
#
# Example 1:
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
# Example 2:
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
# Example 3:
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
# Constraints:
#
#     1 <= text1.length <= 1000
#     1 <= text2.length <= 1000
#     The input strings consist of lowercase English characters only.


def longest_common_subsequence(s1, s2):
    numrow = (len(s1) + 1)
    numcol = (len(s2) + 1)
    dp = [[0] * numcol for _ in range(numrow)]
    for i in range(1, numrow):
        for j in range(1, numcol):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


print(longest_common_subsequence('abcde', 'ace'))
# print(longest_common_subsequence('abc', 'abc'))
# print(longest_common_subsequence('abc', 'def'))
# print(longest_common_subsequence('bl', 'yby'))
# print(longest_common_subsequence("bsbininm", "jmjkbkjkv"))
