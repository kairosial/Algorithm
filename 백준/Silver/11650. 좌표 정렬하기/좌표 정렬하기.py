import sys
n = int(sys.stdin.readline())

points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
points.sort(key=lambda x: (x[0], x[1]))

for x, y in points:
    sys.stdout.write(f'{str(x)} {str(y)}\n')