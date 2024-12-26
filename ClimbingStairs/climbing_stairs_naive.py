from itertools import product


def climb_naive(n):
    # print('\nn = ', steps)
    result = 0
    for i in range(1, n + 1):
        for prod in product([1, 2], repeat=i):
            if sum(prod) == n:
                result += 1
    return result


print(climb_naive(1))
print(climb_naive(2))
print(climb_naive(3))
print(climb_naive(4))
print(climb_naive(5))
print(climb_naive(6))
