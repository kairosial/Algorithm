import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

result = 0
visited = [False] * (n+1)
for node in range(1, n+1):
    if not visited[node]:
        bfs(graph, node, visited)
        result += 1

print(result)