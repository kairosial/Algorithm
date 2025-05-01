from collections import deque

n = int(input())
queue = deque()
visited = set()

queue.append((n, 0))
visited.add(n)

while queue:
    current, count = queue.popleft()

    if current == 1:
        print(count)
        break

    if current % 3 == 0 and (current // 3) not in visited:
        queue.append((current // 3, count + 1))
        visited.add(current // 3)

    if current % 2 == 0 and (current // 2) not in visited:
        queue.append((current // 2, count + 1))
        visited.add(current // 2)

    if (current - 1) not in visited:
        queue.append((current - 1, count + 1))
        visited.add(current - 1)