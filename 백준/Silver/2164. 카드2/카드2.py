from collections import deque
N = int(input())
card_list = [i for i in range(1, N+1)]
card_queue = deque(card_list)
while card_queue:
    result = card_queue.popleft()
    card_queue.rotate(-1)
print(result)