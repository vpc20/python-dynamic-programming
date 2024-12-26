from itertools import combinations


def lis_naive(arr):
    max_len = 1
    for r in range(1, len(arr) + 1):
        for comb in combinations(arr, r):
            if is_increasing(comb):
                if len(comb) > max_len:
                    max_len = len(comb)
                    print(comb)
    return max_len


def is_increasing(arr):
    if len(arr) == 1:
        return True
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] <= prev:
            return False
        else:
            prev = arr[i]
    return True


if __name__ == '__main__':
    # print(lis_naive([1, 10, 5, 20, 30, 6, 7, 8, 9, 2]))
    # print(lis_naive([1]))
    # print(lis_naive([1, 2]))
    # print(lis_naive([1, 2, 3]))
    # print(lis_naive([1, 2, 3, 4]))

    # print(lis_naive([2, 1]))
    # print(lis_naive([3, 2, 1]))
    # print(lis_naive([4, 3, 2, 1]))

    # print(lis_naive([4, 2, 1, 3]))
    # print(lis_naive([2, 4, 1, 3]))
    # print(lis_naive([590, 309, 255, -866, 801, 392, -711, -883, 29, 186]))
    print(lis_naive([10, 5, 1, 75, 50, -10, 150, 200]))


    # print(is_increasing([1]))
    # print(is_increasing([1, 2]))
    # print(is_increasing([1, 2, 3]))
    # print(is_increasing([2, 1]))
    # print(is_increasing([3, 2, 1]))
    # print(is_increasing([1, 3, 2]))
