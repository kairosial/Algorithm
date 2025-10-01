import sys
n = int(sys.stdin.readline())
results = []
init_list = [1, 2, 3, 4, 5, 6]
for _ in range(n):
    dices_dict = {key: 0 for key in init_list}
    dices_list = map(int, sys.stdin.readline().split())
    for i in dices_list:
        dices_dict[i] += 1
    max_list = list(dices_dict.values())
    max_dice_count = max(max_list)
    result = 0
    if max_dice_count == 4:
        found_keys = [key for key, value in dices_dict.items() if value == max_dice_count]
        result = 50000 + (found_keys[0] * 5000)
        results.append(result)
    elif max_dice_count == 3:
        found_keys = [key for key, value in dices_dict.items() if value == max_dice_count]
        result = 10000 + (found_keys[0] * 1000)
        results.append(result)
    elif max_dice_count == 2:
        found_keys = [key for key, value in dices_dict.items() if value == max_dice_count]
        if len(found_keys) == 2:
            result = 2000 + (found_keys[0] * 500) + (found_keys[1] * 500)
            results.append(result)
        else:
            result = 1000 + (found_keys[0] * 100)
            results.append(result)
    else:
        found_keys = [key for key, value in dices_dict.items() if value == max_dice_count]
        result = max(found_keys) * 100
        results.append(result)
print(max(results))