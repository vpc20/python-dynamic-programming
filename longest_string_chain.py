# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to
# make it equal to word2. For example, "abc" is a predecessor of "abac".
#
# A word chain is a sequence of words[word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor
# of word_2, word_2 is a predecessor of word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the given list of words.
#
# Example 1:
# Input: words = ["a", "b", "ba", "bca", "bda", "bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a", "ba", "bda", "bdca".
#
# Example 2:
# Input: words = ["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]
# Output: 5
#
# Constraints:
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
#
# Hint  # 1
# Instead of adding a character, try deleting a character to form a chain in reverse.
#
# Hint  # 2
# For each word in order of length, for each word2 which is word with one character removed,
# length[word2] = max(length[word2], length[word] + 1).


# def longest_str_chain(words):
#     words.sort(key=lambda e: len(e))
#     print(words)
#     dp = [0] * len(words)
#     for i, word in enumerate(words):
#         dp[i] = 1
#         for j, prevword in enumerate(words[:i]):
#             if len(word) == len(prevword) + 1:
#                 for k in range(len(word)):
#                     if word[:k] + word[k + 1:] == prevword:
#                         dp[i] = max(dp[i], dp[j] + 1)
#                         break
#     print(dp)
#     return max(dp)

def longest_str_chain(words):
    words.sort(key=len)
    print(words)
    dp = {w: 1 for w in words}
    for w in words:
        for k in range(len(w)):
            wk = w[:k] + w[k + 1:]  # remove 1 char
            if wk in dp:
                dp[w] = max(dp[w], dp[wk] + 1)
    print(dp)
    return max(count for _, count in dp.items())


# def longest_str_chain(words):
#     words.sort(key=lambda e: len(e))
#     print(words)
#     dp = [0] * len(words)
#     for i in range(len(words)):
#         dp[i] = 1
#         for j in range(i):
#             if len(words[i]) == len(words[j]) + 1:
#                 for k in range(len(words[i])):
#                     if words[i][:k] + words[i][k + 1:] == words[j]:
#                         dp[i] = max(dp[i], dp[j] + 1)
#                         break
#     print(dp)
#     return max(dp)


# def longest_str_chain(words):
#     words.sort(key=lambda e: len(e))
#     print(words)
#     dp = [0] * len(words)
#     dp[0] = 1
#     previ = 0
#     curri = 0
#     for i in range(1, len(words)):
#         dp[i] = 1
#         for j in range(previ, i):
#             if len(words[i]) == len(words[j]) + 1:
#                 for k in range(len(words[i])):
#                     if words[i][:k] + words[i][k + 1:] == words[j]:
#                         dp[i] = max(dp[i], dp[j] + 1)
#                         break
#         if len(words[i]) != len(words[i - 1]):
#             previ = curri
#             curri = i
#     print(dp)
#     return max(dp)


# def longest_str_chain(words): # incorrect
#     words.sort(key=lambda e: len(e))
#     print(words)
#
#     dp = [0] * len(words)
#     dp[0] = 1
#     print(dp)
#     prevlen = len(words[0])
#     previ = 0
#
#     for i in range(1, len(words)):
#         if len(words[i]) == prevlen:
#             dp[i] = 1
#
#         for j in range(previ, i):
#             if len(words[i]) == len(words[j]):
#                 continue
#             else:
#                 if len(words[i].translate(words[i].maketrans('', '', words[j]))) == 1: # incorrect
#                     dp[i] = dp[j] + 1
#
#         if len(words[i]) != prevlen:
#             prevlen = len(words[i])
#             previ = i
#
#     print(dp)
#     return dp[-1]


assert longest_str_chain(["a", "ab", "abc", "abcd", "abcde"]) == 5
assert longest_str_chain(["a", "b", "ba", "bca", "bda", "bdca"]) == 4
assert longest_str_chain(["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"]) == 5
assert longest_str_chain(["a", "b", "ab", "bac"]) == 2
assert longest_str_chain(["a", "ab", "ac", "bd", "abc", "abd", "abdd"]) == 4
assert longest_str_chain(["bdca", "bda", "ca", "dca", "a"]) == 4
