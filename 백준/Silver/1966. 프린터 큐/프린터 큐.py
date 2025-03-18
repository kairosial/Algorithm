import sys
from collections import deque
T = int(sys.stdin.readline().strip())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    importance_list = list(map(int, sys.stdin.readline().strip().split()))
    queue = deque()
    for idx, i in enumerate(importance_list):
        queue.append((i, idx))
    result = 0
    while True:
        if queue[0][0] == max(queue)[0] and queue[0][1] == M:
            queue.popleft()
            result += 1
            break
        elif queue[0][0] == max(queue)[0]:
            queue.popleft()
            result += 1
        else:
            queue.rotate(-1)
    sys.stdout.write(str(result) + '\n')