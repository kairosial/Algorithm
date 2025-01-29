t = int(input())
for _ in range(t):
    result = []
    list_num = list(map(int, input().split()))
    list_even = [i for i in list_num if i % 2 == 0]
    result.append(sum(list_even))
    result.append(min(list_even))
    print(*result)