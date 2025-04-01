import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 알고리즘으로 실행 시 RecursionError 발생하므로 재귀 제한을 늘려주는 코드 추가 필요
sys.setrecursionlimit(10 ** 5)
def dfs(graph, node, visited):
    # 현재 노드를 방문 처리
    visited[node] = True
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for child in graph[node]:
        if not visited[child]:
            dfs(graph, child, visited)

def bfs(graph, start_node, visited):
    queue = deque([start_node])
    visited[start_node] = True
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True

result = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(graph, i, visited)
        result += 1

print(result)