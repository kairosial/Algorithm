import sys
from collections import Counter

input = sys.stdin.readline
n = int(input())
num_list = [int(input()) for _ in range(n)]

mean = int(round((sum(num_list) / len(num_list)), 0))
median = sorted(num_list)[int(len(num_list)/2)]

count = Counter(num_list)
most_common = count.most_common()
max_freq = most_common[0][1]
modes = [num for num, freq in most_common if freq == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

range = max(num_list) - min(num_list)

print(mean)
print(median)
print(mode)
print(range)