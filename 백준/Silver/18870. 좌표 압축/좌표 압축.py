import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_set = set(num_list)
sorted_num_list = sorted(num_set)

num_dict = dict()
idx = 0
for i in sorted_num_list:
    num_dict[i] = idx
    idx += 1

result = []
for j in num_list:
    result.append(num_dict[j])
print(*result)