n = int(input())
result = -1
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b:
        if result == -1:
            result = b
        else:
            result = min(result, b)
print(result)