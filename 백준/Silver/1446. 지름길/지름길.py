n, d = map(int, input().split())
cases = [list(map(int, input().split())) for _ in range(n)]
filtered_cases = []
for case in cases:
    start, end, shortcut = case
    if shortcut > (end - start):
        continue
    if end > d:
        continue
    filtered_cases.append(case)

INF = int(1e9)
dist = [INF] * (d+1)
dist[0] = 0

# 미리 지름길들을 start 기준으로 묶기 (ex: {0: [(50, 10), (50, 20)], 50: [(100, 10)]})
shortcut_dict = {}
for start, end, shortcut in filtered_cases:
    if start not in shortcut_dict:
        shortcut_dict[start] = []
    shortcut_dict[start].append((end, shortcut))

for i in range(d + 1):
    # 1. 기본 도로 이동
    if i + 1 <= d:
        dist[i + 1] = min(dist[i + 1], dist[i] + 1)

    # 2. 지름길 적용 (시작 위치가 i일 때만)
    if i in shortcut_dict:
        for end, shortcut in shortcut_dict[i]:
            if end <= d:
                dist[end] = min(dist[end], dist[i] + shortcut)

print(dist[d])