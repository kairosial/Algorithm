from collections import deque
N, K = map(int, input().split())
num_q = deque([_ for _ in range(1, N+1)])
result = []
while num_q:
    num_q.rotate(-K+1)
    result.append(num_q.popleft())
print(f"<{', '.join(map(str, result))}>")