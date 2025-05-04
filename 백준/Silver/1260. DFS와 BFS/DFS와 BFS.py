from collections import deque

n, m, v = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# 인접 리스트 생성
graph = [[] for _ in range(n+1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)
# 정점 번호가 작은 것부터 방문해야하므로 graph의 각 요소를 오름차순 정렬
for g in graph:
    g.sort()
# 또는 다음과 같이 정렬
# graph = [sorted(g) for g in graph]



# DFS - 재귀 방식
DFS_visited = [False] * (n+1)
DFS_result = []
def DFS(v):
    DFS_visited[v] = True
    DFS_result.append(v)
    for i in graph[v]:
        if not DFS_visited[i]:
            DFS(i)



# BFS - 큐 기반
BFS_visited = [False] * (n+1)
BFS_result = []
def BFS(start):
    que = deque([start])
    BFS_visited[start] = True
    BFS_result.append(start)
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not BFS_visited[i]:
                que.append(i)
                BFS_visited[i] = True
                BFS_result.append(i)



DFS(v)
print(*DFS_result)
BFS(v)
print(*BFS_result)