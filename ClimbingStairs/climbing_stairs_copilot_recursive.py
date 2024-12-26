def climbStairsWays(n):
    def backtrack(steps, path):
        # If the number of steps is 0, we've found a valid way to climb the stairs
        if steps == 0:
            result.append(path[:])
            return
        # If the number of steps is negative, this is not a valid path
        if steps < 0:
            return

        # Try taking 1 step
        path.append(1)
        backtrack(steps - 1, path)
        path.pop()

        # Try taking 2 steps
        path.append(2)
        backtrack(steps - 2, path)
        path.pop()

    result = []
    backtrack(n, [])
    return result

# Example usage:
n1 = 2
n2 = 3
print(f"All ways to climb {n1} steps: {climbStairsWays(n1)}")
print(f"All ways to climb {n2} steps: {climbStairsWays(n2)}")