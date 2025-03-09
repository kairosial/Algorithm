import sys

def custom_round(n):
    return int(n + 0.5) if n >= 0 else int(n - 0.5)

n = int(input())
if n == 0:
    print(0)
else:
    level_list = sorted([int(sys.stdin.readline().strip()) for _ in range(n)])
    exc = custom_round(len(level_list) * 0.15)
    if exc == 0:
        new_level_list = level_list
    else:
        new_level_list = level_list[exc:-exc]
    print(custom_round(sum(new_level_list) / len(new_level_list)))