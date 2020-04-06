from itertools import combinations

box_dict = {'green': [4, 12],
            'blue': [2, 2],
            'gray': [2, 1],
            'red': [1, 1],
            'yellow': [10, 4]}
max_box_combo = None
max_weight = 15
max_amt = 0
for box_count in range(1, len(box_dict) + 1):
    for box_combinations in combinations(box_dict, box_count):
        print('==============================================')
        print(box_combinations)
        sum_weight = 0
        sum_amt = 0
        for box in box_combinations:
            print(box_dict[box])
            sum_amt += box_dict[box][0]
            sum_weight += box_dict[box][1]
        print('sum_amt ', sum_amt)
        print('sum_weight', sum_weight)
        if sum_weight < max_weight and sum_amt > max_amt:
            max_box_combo = box_combinations
print(max_box_combo)
