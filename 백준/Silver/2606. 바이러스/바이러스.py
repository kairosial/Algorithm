from collections import deque

n = int(input())
e = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        q = queue.popleft()
        for child in graph[q]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True

visited = [False] * (n+1)
BFS(graph, 1, visited)
print(sum(visited) - 1)