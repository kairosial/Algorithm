N = int(input())
calls = list(map(int, input().split()))

Y = 0
M = 0

for c in calls:
    y = 10 + ((c // 30) * 10)
    Y += y
    m = 15 + ((c // 60) * 15)
    M += m

if M < Y:
    print(f'M {M}')
elif Y < M:
    print(f'Y {Y}')
elif Y == M:
    print(f'Y M {Y}')