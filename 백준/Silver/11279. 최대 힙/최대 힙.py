import sys
import heapq
n = int(sys.stdin.readline())
h = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if h:
            sys.stdout.write(f'{-heapq.heappop(h)}\n')
        else:
            sys.stdout.write(f'0\n')
    else:
        heapq.heappush(h, -x)