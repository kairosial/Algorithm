from collections import deque
while True:
    que = deque(map(int, input().split()))
    if que[0] == 0 and len(que) == 1:
        break
    age = que.popleft()
    result = 1
    while que:
        splitting_factor = que.popleft()
        pruning = que.popleft()
        result = result * splitting_factor - pruning
    print(result)