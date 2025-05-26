M = int(input())
ball = 1
for _ in range(M):
    x, y = map(int, input().split())
    if ball == x:
        ball = y
    elif ball == y:
        ball = x
print(ball)