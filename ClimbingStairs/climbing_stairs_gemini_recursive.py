def climb_stairs_paths(n):
  """
  Finds all distinct ways to climb n stairs, where you can climb 1 or 2 steps at a time.

  Args:
    n: The number of stairs.

  Returns:
    A list of lists, where each inner list represents a distinct way to climb the stairs.
  """

  if n == 0:
    return [[]]  # Empty list represents reaching the top with no steps

  if n == 1:
    return [[1]]

  paths = []

  # If you take a 1-step from the previous stair
  for path in climb_stairs_paths(n - 1):
    paths.append(path + [1])

  # If you take a 2-step from the previous stair
  for path in climb_stairs_paths(n - 2):
    paths.append(path + [2])

  return paths

# Example usage
n = 4
all_paths = climb_stairs_paths(n)
print(f"All distinct ways to climb {n} stairs:")
for path in all_paths:
  print(path)