import sys
input = sys.stdin.readlines()
N = int(input[0].strip())
card_list = list(map(int, input[1].strip().split()))
M = int(input[2].strip())
target_list = list(map(int, input[3].strip().split()))

count_dict = {}
for num in card_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

result = [count_dict.get(num, 0) for num in target_list]

print(*result)