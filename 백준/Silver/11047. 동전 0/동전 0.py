N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

result = 0
K_tmp = K
for coin in coins:
    if K_tmp // coin > 0:
        result += K_tmp // coin
        K_tmp = K_tmp % coin
print(result)