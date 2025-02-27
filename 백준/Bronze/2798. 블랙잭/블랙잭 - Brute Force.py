N, M = map(int, input().split())
num_list = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            s = num_list[i] + num_list[j] + num_list[k]
            if s <= M and s > result:
                result = s

print(result)