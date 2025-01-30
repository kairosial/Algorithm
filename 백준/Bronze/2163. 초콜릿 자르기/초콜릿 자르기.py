n, m = map(int, input().split())
result = 0
if n > m:
    result = (m-1) + (n-1) * m
else:
    result = (n-1) + (m-1) * n
print(result)