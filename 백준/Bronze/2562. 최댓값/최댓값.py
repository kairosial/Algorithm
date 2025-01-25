num_list = []
for _ in range(9):
    num = int(input())
    num_list.append(num)

max_num = max(num_list)
max_num_idx = num_list.index(max_num) + 1

print(max_num)
print(max_num_idx)