# def climb_recur(n, climb={0: 1, 1: 1}):
#     if n in climb:
#         return climb[n]
#     climb[n] = climb_recur(n - 1) + climb_recur(n - 2)
#     return climb[n]

from functools import lru_cache


@lru_cache(maxsize=1000)
def climb_recur(n):
    if n in [0, 1]:
        return n
    climb = climb_recur(n - 1) + climb_recur(n - 2)
    return climb


print(climb_recur(1))
print(climb_recur(2))
print(climb_recur(3))
print(climb_recur(4))
print(climb_recur(5))
print(climb_recur(6))
print(climb_recur(7))
print(climb_recur(50))
