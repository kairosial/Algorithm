N, L, W, H = map(int, input().split())

# 이분 탐색의 좌우 범위 설정
low = 0.0
high = max(L, W, H)

# 정답 후보
answer = 0.0

# 반복 (정밀도 조건)
for _ in range(100):
    mid = (low + high) / 2

    count = int(L // mid) * int(W // mid) * int(H // mid)

    if count >= N:
        answer = mid
        low = mid
    else:
        high = mid

print(f'{answer:.10f}')