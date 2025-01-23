n, m = map(int, input().split())
basket_list = [i+1 for i in range(n)]

for _ in range(m):
    start, end = map(int, input().split())
    basket_list = basket_list[0:start-1] + list(reversed(basket_list[start-1:end])) + basket_list[end:n+1]

print(*basket_list)