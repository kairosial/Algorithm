import sys

dp = [0, 1]
for i in range(2, 302):
    dp.append(dp[i-1]+i)

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    result = 0
    for k in range(1, n+1):
        result += k * dp[k+1]
    sys.stdout.write(f'{result}\n')