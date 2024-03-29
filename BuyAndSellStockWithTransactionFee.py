# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and
# a non-negative integer fee representing a transaction fee.
#
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
#
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
# Note:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.


def max_profit(prices, fee):
    n = len(prices)
    dp = [0] * n
    # dp[0] = -prices[0]
    for i in range(1, n):
        for j in range(i):
            diff = prices[i] - prices[j]
            if diff > fee:
                dp[i] = max(dp[i - 1], diff - fee)
            else:
                dp[i] = dp[i - 1]
    print(dp)
    return dp[-1]


# def max_profit(prices, fee):
#     n = len(prices)
#     dp = [0] * n
#     # dp[0] = -prices[0]
#     for i in range(1, n):
#         diff = prices[i] - prices[i - 1]
#         if diff > fee:
#             for j in range(i):
#                 dp[i] = max(dp[i-1], dp[j] + diff)
#         else:
#             dp[i] = dp[i - 1]
#     print(dp)
#     return dp[-1]


print(max_profit([1, 3, 2, 8, 4, 9], 2))
#  [1,  3,  2,  8,  4,  9]
#  [0,  0,  0,  5,  5,  8]
