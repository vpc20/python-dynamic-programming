def climbStairsWays(n):
    # Initialize the list to store the ways to climb each step
    dp = [[] for _ in range(n + 1)]

    # Base cases
    dp[0] = [[]]  # One way to stay at the ground
    if n >= 1:
        dp[1] = [[1]]  # One way to reach the first step

    # Fill the dp array for each step from 2 to n
    for i in range(2, n + 1):
        # Ways to reach the current step by taking 1 step from (i-1)
        for way in dp[i - 1]:
            dp[i].append(way + [1])

        # Ways to reach the current step by taking 2 steps from (i-2)
        for way in dp[i - 2]:
            dp[i].append(way + [2])
    print(dp)
    return dp[n]


# Example usage:
n1 = 2
n2 = 3
print(f"All ways to climb {n1} steps: {climbStairsWays(n1)}")
print(f"All ways to climb {n2} steps: {climbStairsWays(n2)}")