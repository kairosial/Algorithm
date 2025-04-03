import sys

N = int(input())
# 모든 좌표 추가
points = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().strip().split())
    points.append((x, y))

# y좌표 기준으로 오름차순 정렬, y좌표가 같은 경우에는 x좌표 기준으로 오름차순 정렬
sorted_points = sorted(points, key=lambda point: (point[1], point[0]))

for x, y in sorted_points:
    sys.stdout.write(f'{x} {y}\n')