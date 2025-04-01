import sys
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# # DFS 알고리즘으로 실행 시 RecursionError 발생하므로 재귀 제한을 늘려주는 코드 추가 필요
# sys.setrecursionlimit(10 ** 5)
# def DFS(graph, node, visited):
#     # 현재 노드를 방문 처리
#     visited[node] = True
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for child in graph[node]:
#         if not visited[child]:
#             DFS(graph, child, visited)

def BFS(graph, start_node, visited):
    queue = deque([start_node])
    # 현재 노드를 방문 처리
    visited[start_node] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 가장 처음 원소를 추출
        node = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for child in graph[node]:
            if not visited[child]:
                queue.append(child)
                visited[child] = True

result = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        BFS(graph, i, visited)
        result += 1

print(result)