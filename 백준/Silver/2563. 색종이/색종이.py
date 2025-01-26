matrix = [ [0 for _ in range(100)] for _ in range(100) ]

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    y = abs(y - 99)
    for row in range(y, y-10, -1):
        for col in range(x, x+10):
            matrix[row][col] = 1

count = sum(row.count(1) for row in matrix)
print(count)