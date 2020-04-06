def lis_iter(arr):
    dp_arr = [1] * len(arr)
    print(dp_arr)
    # num_arr = [[arr[0]]] + [[] for _ in range(len(arr) - 1)]
    num_arr = [[e] for e in arr]
    # print(num_arr)
    max_len = 1
    max_i = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and dp_arr[j] + 1 > dp_arr[i]:
                dp_arr[i] = dp_arr[j] + 1
                if dp_arr[i] >= max_len:
                    max_len = dp_arr[i]
                    max_i = i
                    num_arr[i] = num_arr[j] + [arr[i]]
        print(dp_arr)
    # print(num_arr)
    if num_arr:
        print(num_arr[max_i])
    return max_len


if __name__ == '__main__':
    # print(lis_iter([1, 10, 5, 20, 30, 6, 7, 8, 9, 2]))

    # print(lis([1]))
    # print(lis([1, 2]))
    # print(lis([1, 2, 3]))
    # print(lis([1, 2, 3, 4]))

    # print(lis([2, 1]))
    # print(lis([3, 2, 1]))
    # print(lis([4, 3, 2, 1]))

    # print(lis([4, 2, 1, 3]))
    # print(lis([2, 4, 1, 3]))
    # print(lis_iter([590, 309, 255, -866, 801, 392, -711, -883, 29, 186]))

    # print(lis_iter([10]))
    # print(lis_iter([10, 5]))
    # print(lis_iter([10, 5, 1]))
    # print(lis_iter([10, 5, 1, 75]))
    # print(lis_iter([10, 5, 1, 75, 50]))
    # print(lis_iter([10, 5, 1, 75, 50, -10, 150]))
    print(lis_iter([10, 5, 1, 75, 50, -10, 150, 200]))
    #  0  1  2  3  4  5  6  7
    # ------------------------
    # [1, 1, 1, 1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1, 1, 1, 1]
    # [1, 1, 1, 2, 1, 1, 1, 1]
    # [1, 1, 1, 2, 2, 1, 1, 1]
    # [1, 1, 1, 2, 2, 1, 1, 1]
    # [1, 1, 1, 2, 2, 1, 3, 1]
    # [1, 1, 1, 2, 2, 1, 3, 4]
