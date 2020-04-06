def climb_iter(n):
    arr = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    return arr[-1]


print(climb_iter(1))
print(climb_iter(2))
print(climb_iter(3))
print(climb_iter(4))
print(climb_iter(5))
print(climb_iter(6))
