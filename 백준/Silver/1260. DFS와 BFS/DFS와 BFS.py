from collections import deque

n, m, v = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n+1)]
for a, b in edge:
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(g) for g in graph]

DFS_visited = [False] * (n+1)
DFS_result = []
def DFS(graph, v, visited, result):
    result.append(v)
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited, result)
    return result

BFS_visited = [False] * (n+1)
BFS_result = []
def BFS(graph, start, visited, result):
    result.append(start)
    visited[start] = True
    que = deque([start])
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True
                result.append(i)
    return result

print(*DFS(graph, v, DFS_visited, DFS_result))
print(*BFS(graph, v, BFS_visited, BFS_result))