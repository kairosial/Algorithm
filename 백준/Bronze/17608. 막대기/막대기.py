import sys
n = int(input())
stack = [int(sys.stdin.readline().strip()) for _ in range(n)]

max_h = 0
result = 0

for h in stack[::-1]:
    if h > max_h:
        result += 1
        max_h = h

print(result)