import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(1, m+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 알고리즘으로 실행 시 RecursionError 발생하므로 BFS 알고리즘 활용
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