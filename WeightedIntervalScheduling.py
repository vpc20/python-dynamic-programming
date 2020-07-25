import sys
from functools import lru_cache
from itertools import combinations


def compatible_intervals(intvs):
    for i in range(len(intvs) - 1):
        for j in range(i + 1, len(intvs)):
            # stj  < sti < ftj
            # stj  < fti < ftj
            if intvs[j][0] < intvs[i][0] < intvs[j][1] or \
                    intvs[j][0] < intvs[i][1] < intvs[j][1]:
                return False
    return True


def weighted_interval_sched_naive(intvs):
    maxval = -sys.maxsize
    for r in range(1, len(intvs) + 1):
        for comb in combinations(intvs, r):
            if compatible_intervals(comb):
                sumval = sum([val for _, _, val in comb])
                maxval = max(maxval, sumval)
                # print(maxval, comb)
    return maxval


def weighted_interval_sched(intvs):
    @lru_cache(maxsize=1000)
    def interval_sched(j):
        if j == -1:
            return 0
        return max(intvs[j][2] + interval_sched(p[j]), interval_sched(j - 1))

    # intervals = (start_time, finishing_time, value)
    n = len(intvs)
    intvs.sort(key=lambda e: e[1])  # sort by finishing time
    p = [-1]  # indices of last compatible interval, -1 means no compatible interval
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if intvs[i][0] >= intvs[j][1]:
                p.append(j)
                break
        else:
            p.append(-1)
    return interval_sched(n - 1)


# def weighted_interval_sched_iter(intrvls):  # dynamic
#     # intervals = (start_time, finishing_time, value)
#     intrvls.sort(key=lambda e: e[1])  # sort by finishing time
#     p = [-1]  # indices of last compatible interval, -1 means no compatible interval
#     for i in range(1, len(intrvls)):
#         for j in range(i - 1, -1, -1):
#             if intrvls[i][0] >= intrvls[j][1]:
#                 p.append(j)
#                 break
#         else:
#             p.append(-1)
#
#     dp_arr = [0] * (len(intrvls) + 1)
#     for i in range(1, len(intrvls) + 1):
#         if p[i - 1] != -1:
#             dp_arr[i] = max(intrvls[i - 1][2] + dp_arr[p[i - 1] + 1], dp_arr[i - 1])
#         else:
#             dp_arr[i] = max(intrvls[i - 1][2], dp_arr[i - 1])
#
#     return dp_arr[-1]

def weighted_interval_sched_iter(intvs):  # dynamic
    # intervals = (start_time, finishing_time, value)
    intvs.append((0, 0, 0))
    intvs.sort(key=lambda e: e[1])  # sort by finishing time
    p = [0, 0]  # indices of last compatible interval, 0 means no compatible interval
    for i in range(2, len(intvs)):
        for j in range(i - 1, -1, -1):
            if intvs[i][0] >= intvs[j][1]:
                p.append(j)
                break
        else:
            p.append(0)
    print(p)

    dp_arr = [0] * len(intvs)
    intv_arr = [[] for _ in range(len(intvs))]
    for i in range(1, len(intvs)):
        # dp_arr[i] = max(intvs[i][2] + dp_arr[p[i]], dp_arr[i - 1])
        if intvs[i][2] + dp_arr[p[i]] > dp_arr[i - 1]:
            dp_arr[i] = intvs[i][2] + dp_arr[p[i]]
            intv_arr[i] = intv_arr[p[i]].copy()
            intv_arr[i].append(intvs[i])
        else:
            dp_arr[i] = dp_arr[i - 1]
            intv_arr[i] = intv_arr[i - 1].copy()

    return dp_arr[-1], intv_arr[-1]


if __name__ == '__main__':
    # intervals = [(0, 5, 8),
    #              (0, 10, 6)]
    intervals = [(0, 4, 2),
                 (1, 6, 4),
                 (5, 7, 4),
                 (3, 10, 7),
                 (8, 11, 2),
                 (9, 12, 1)]
    #    0  1  2  3  4  5  6  7  8  9  10  11  12
    # 0                                             <== dummy
    # 1  |-----------|
    # 2     |--------------|
    # 3                 |-----|
    # 4           |---------------------|
    # 5                          |----------|
    # 6                             |-----------|

    print(weighted_interval_sched_naive(intervals))
    print(weighted_interval_sched(intervals))
    print(weighted_interval_sched_iter(intervals))
