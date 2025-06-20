n = int(input())
result = -1

if n >= 5:
    quotient_max = n // 5
    for quotient in range(quotient_max, -1, -1):
        if quotient > 0:
            tmp = n - (5 * quotient)
        else:
            tmp = n
        if tmp % 3 == 0:
            result = quotient + (tmp // 3)
            break
    print(result)
elif n == 4:
    print(-1)
elif n == 3:
    print(1)