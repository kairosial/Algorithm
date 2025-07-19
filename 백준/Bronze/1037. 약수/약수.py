# 입력 받기
n = int(input())  # 진짜 약수의 개수
divisors = list(map(int, input().split()))  # 진짜 약수들

# 정렬
divisors.sort()

# N은 가장 작은 진짜 약수 * 가장 큰 진짜 약수
N = divisors[0] * divisors[-1]

print(N)