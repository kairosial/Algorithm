N, X = map(int, input().split())
num_list = list(map(int, input().split()))
result = []
for i in num_list:
    if i < X:
        result.append(i)
print(*result)