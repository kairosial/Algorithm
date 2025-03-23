from collections import deque
N = int(input())
card_list = [i for i in range(1, N+1)]
card_queue = deque(card_list)
result = []
while card_queue:
    result.append(card_queue.popleft())
    card_queue.rotate(-1)
print(*result)