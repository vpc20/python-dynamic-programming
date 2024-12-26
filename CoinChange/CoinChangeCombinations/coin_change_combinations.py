from itertools import combinations_with_replacement


def coin_change_combination(coin_list, change):
    if change == 0:
        return 1
    change_count = 0
    for i in range(1, int(change / min(coin_list)) + 1):
        for comb in combinations_with_replacement(coin_list, i):
            if sum(comb) == change:
                change_count += 1
    return change_count


if __name__ == '__main__':
    # print(coin_change_combination([1, 2, 3], 4))
    # print(coin_change_combination([2, 5, 3, 6], 10))
    # print(coin_change_combination([1, 2, 5], 12))
    # print(coin_change_combination([1, 5, 10, 25], 63))
    print(coin_change_combination([1, 2, 3, 4, 5], 5))
