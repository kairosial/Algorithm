import sys
n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
sum_num_list = list()
tmp = 0
for s in num_list:
    sum_num_list.append(s + tmp)
    tmp = sum_num_list[-1]
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    i_, j_ = i - 1, j - 1
    if i_ == 0:
        sys.stdout.write(f'{sum_num_list[j_]}\n')
    elif i_ == j_:
        sys.stdout.write(f'{num_list[i_]}\n')
    else:
        sys.stdout.write(f'{sum_num_list[j_] - sum_num_list[i_-1]}\n')