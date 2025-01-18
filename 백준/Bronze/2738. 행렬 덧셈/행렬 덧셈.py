n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))
sum = []

for i in range(n):
    for j in range(m):
        sum.append(a[i][j] + b[i][j])

for k in range(0, len(sum), 3):
    print(*sum[k:k+3])