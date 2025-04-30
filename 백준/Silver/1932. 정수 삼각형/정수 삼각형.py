import sys
n = int(sys.stdin.readline().strip())
triangle = []
for _ in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    triangle.append(temp)

for i in range(n-2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])