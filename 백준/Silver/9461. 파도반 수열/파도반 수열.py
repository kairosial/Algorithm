import sys
T = int(input())

# P(n) = P(n-1) + P(n-5)라는 점화식으로 풀었지만
# P(n) = P(n-2) + P(n-3)라는 점화식도 가능함
def padovan(sequence, n):
    return sequence[n-1] + sequence[n-5]

dp = [0, 1, 1, 1, 2]
for i in range(5, 101):
    dp.append(padovan(dp, i))

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    sys.stdout.write(str(dp[N]) + '\n')