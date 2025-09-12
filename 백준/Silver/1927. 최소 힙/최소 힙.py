import sys
import heapq

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
h = []

for value in arr:
    if value == 0:
        try:
            sys.stdout.write(f'{heapq.heappop(h)}\n')
        except:
            sys.stdout.write(f'0\n')
    else:
        heapq.heappush(h, value)