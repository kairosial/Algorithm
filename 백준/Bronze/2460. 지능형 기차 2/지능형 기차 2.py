result = 0
current = 0
for _ in range(10):
    drop, board = map(int, input().split())
    current -= drop
    current += board
    if current > result:
        result = current
print(result)