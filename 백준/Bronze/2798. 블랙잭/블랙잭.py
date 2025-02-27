from itertools import combinations
N, M = map(int, input().split())
num_list = list(map(int, input().split()))

result = 0
for combo in combinations(num_list, 3):
    if sum(combo) <= M and sum(combo) > result:
        result = sum(combo)

print(result)