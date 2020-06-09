# You are given coins of different denominations and a total amount of money.Write a function to compute the number
# of combinations that make up that amount.You may assume that you have infinite number of each kind of coin.
#
# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5 = 5
# 5 = 2 + 2 + 1
# 5 = 2 + 1 + 1 + 1
# 5 = 1 + 1 + 1 + 1 + 1
#
# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
# Example 3:
# Input: amount = 10, coins = [10]
# Output: 1
#
# Note:
# You can assume that
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32 - bit integer


# def change(amount, coins):
#     nrows = len(coins) + 1
#     ncols = amount + 1
#     dp = [[1] + [0] * amount for _ in range(nrows)]
#
#     for i in range(1, nrows):
#         for j in range(1, ncols):
#             if j >= coins[i - 1]:
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
#             else:
#                 dp[i][j] = dp[i - 1][j]
#     for e in dp:
#         print(e)
#     return dp[-1][-1]

# simplified dp
def change(amount, coins):
    dp = [1] + [0] * amount
    print(dp)

    for i in range(1, len(coins) + 1):
        for j in range(1, amount + 1):
            if j >= coins[i - 1]:
                dp[j] += dp[j - coins[i - 1]]
        print(dp)
    return dp[-1]


# def change(amount, coins):
#     dp = [1] + [0] * amount
#     print(dp)
#
#     for coin in coins:
#         for j in range(1, amount + 1):
#             if j >= coin:
#                 dp[j] += dp[j - coin]
#         print(dp)
#     return dp[-1]


def change_recur(amount, coins):
    def changex(amt, acc_coins):
        nonlocal count
        if amt == 0:  # add 1 to count if accumulated coins already adds up to amount
            count += 1
            return
        for coin in coins:
            if coin > amt:
                break
            elif acc_coins and coin < acc_coins[-1]:
                continue  # remove duplicates, take coins in non-decreasing order
            else:
                changex(amt - coin, acc_coins + [coin])

    count = 0
    coins.sort()
    changex(amount, [])
    return count


# print(change(5, [1, 2, 5]))
# print(change_recur(5, [1, 2, 5]))

print(change(3, [1, 2, 3]))
print(change_recur(3, [1, 2, 3]))
