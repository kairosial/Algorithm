N, m, M, T, R = map(int, input().split())
X = m
exercise = 0
result = 0

while exercise < N:
    if X + T <= M: # 운동
        X += T
        exercise += 1
        result += 1
        continue
    elif X + T > M and exercise == 0:
        result = -1
        break
    else: # 휴식
        if X - R < m:
            X = m
        else:
            X -= R
        result += 1

print(result)