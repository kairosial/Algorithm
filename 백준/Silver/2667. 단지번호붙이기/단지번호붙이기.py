import sys
from collections import deque

N = int(input())

maps = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
que = deque()
group = []

# maps 입력
for i in range(N):
    maps[i] = list(map(int, sys.stdin.readline().strip()))

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def BFS():
    while que:
        y, x = que.popleft()
        
        # 사방으로 돌면서 확인
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if 0 <= nx < N and 0 <= ny < N:  # map의 범위를 벗어나지 않고
                if visited[ny][nx] == 0 and maps[ny][nx] == 1:
                    visited[ny][nx] = 1
                    que.append((ny, nx))
                    group[-1] += 1  # 단지에 속한 집의 개수 추가

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and maps[i][j] == 1:
            visited[i][j] = 1  # 방문 처리
            que.append((i, j))  # 큐에 노드 좌표 추가
            group.append(1)  # 새로운 단지 추가
            BFS()

# 문제 조건: 오름차순 정렬
group.sort()

# 문제 조건대로 단지의 수와 집의 개수를 오름차순으로 출력
print(len(group))
for house in group:
    print(house)