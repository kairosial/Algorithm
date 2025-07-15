import sys
n = int(input())
score = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] * n

dp[0] = score[0]

if n >= 2:
    dp[1] = score[0] + score[1]
if n >= 3:
    dp[2] = max(score[0]+score[2], score[1]+score[2])

    for i in range(3, n):
        dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])

print(dp[-1])