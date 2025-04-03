import sys

N = int(input())
points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    points.append((x, y))

sorted_points = sorted(points, key=lambda point: (point[1], point[0]))

for x, y in sorted_points:
    sys.stdout.write(f'{x} {y}\n')