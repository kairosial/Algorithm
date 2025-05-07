n = int(input())
case_list = [int(input()) for _ in range(n)]
case_max = max(case_list)

dp = [0 for _ in range(case_max+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

if case_max >= 4:
    for i in range(4, case_max+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

result = [dp[c] for c in case_list]
for r in result:
    print(r)