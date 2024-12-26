def climb_iter(n):
    arr = [1, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
    print(arr)
    return arr[-1]


def climb_iter2(n):
    arr1 = [[]]
    arr2 = [[1]]
    if n == 0:
        return arr1
    elif n == 1:
        return arr2

    for _ in range(2, n + 1):
        new_arr = []
        for e in arr2:
            new_arr.append(e + [1])
        for e in arr1:
            new_arr.append(e + [2])
        arr1, arr2 = arr2, new_arr
    return new_arr


# print(climb_iter(0))
# print(climb_iter(1))
# print(climb_iter(2))
# print(climb_iter(3))
# print(climb_iter(4))

print(climb_iter2(1))
print(climb_iter2(2))
print(climb_iter2(3))
print(climb_iter2(4))
print(climb_iter2(5))
