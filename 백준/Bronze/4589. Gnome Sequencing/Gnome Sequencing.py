n = int(input())
beards = [list(map(int, input().split())) for _ in range(n)]
print('Gnomes:')
for beard in beards:
    status = 'Unordered'
    a, b, c = beard[0], beard[1], beard[2]
    if a < b and b < c:
        status = 'Ordered'
    elif a > b and b > c:
        status = 'Ordered'
    print(status)