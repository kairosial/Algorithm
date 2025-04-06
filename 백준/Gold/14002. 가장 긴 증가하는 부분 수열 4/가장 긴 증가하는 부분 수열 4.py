N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N  # 각 인덱스를 끝으로 하는 LIS의 길이 (최소는 자기 자신이므로 1)
prev = [-1] * N  # 각 인덱스의 이전 요소 위치를 기록 (LIS 추적용)

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i] and dp[j]+1 > dp[i]:  # 증가 수열이고, 더 긴 수열이 가능하다면
            dp[i] = dp[j]+1  # dp 갱신
            prev[i] = j  # 

# LIS 최대 길이와 마지막 원소 인덱스 찾기
max_len = max(dp)  # LIS의 길이
idx = dp.index(max_len)  # LIS 수열의 마지막 값(가장 큰 값)의 arr 내 인덱스

# 역추적
lis = []
while idx != -1:
    lis.append(arr[idx])  # 해당 인덱스 값을 결과 리스트에 넣고
    idx = prev[idx]  # 이전 인덱스로 이동

lis.reverse()  # 역순이므로 뒤집기

print(max_len)
print(*lis)