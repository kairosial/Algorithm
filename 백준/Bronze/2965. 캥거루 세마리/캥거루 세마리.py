a, b, c = map(int, input().split())
result = 0
while (b - a > 1) or (c - b > 1):
    front = b - a
    back = c - b
    if front > back:
        c = b
        b = c - 1
    else:
        a = b
        b = a + 1
    result += 1
print(result)