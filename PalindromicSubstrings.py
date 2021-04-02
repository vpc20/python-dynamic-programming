# Given a string, your task is to count how many palindromic substrings in this string.
# The substrings with different start indexes or end indexes are counted as different substrings even they consist
# of same characters.
#
# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


def count_substrings(s):
    n = len(s)
    dp = [1] * n
    for i in range(1, n):
        count = 0
        for j in range(i):
            if s[j:i + 1] == s[j:i + 1][::-1]:
                count += 1
        dp[i] += dp[i - 1] + count
    return dp[-1]


assert count_substrings('abc') == 3
assert count_substrings('aaa') == 6

# a b a b a
# 1 2 4 6 8
