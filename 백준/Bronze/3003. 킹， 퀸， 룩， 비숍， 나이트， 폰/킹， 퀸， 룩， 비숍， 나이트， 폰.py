k, q, r, b, n ,p = map(int, input().split())
white_lst = [k, q, r, b, n , p]
normal_lst = [1, 1, 2, 2, 2, 8]
result = []

for i, j in zip(white_lst, normal_lst):
    if i != j:
        result.append(j-i)
    else:
        result.append(0)

print(*result)