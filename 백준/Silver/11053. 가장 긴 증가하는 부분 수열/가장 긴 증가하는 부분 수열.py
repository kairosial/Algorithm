n = int(input())
arr = list(map(int, input().split()))

# dp 배열을 1로 초기화 (각 수열 원소 자체만으로도 길이가 1인 증가부분수열)
dp = [1] * n

# dp 배열에 각 원소별로 증가부분수열의 길이를 업데이트하는 전략
# 각 원소에 대해 앞쪽 원소들을 확인하여 dp 값을 갱신
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))