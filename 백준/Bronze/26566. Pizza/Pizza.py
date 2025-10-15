import math
n = int(input())
for _ in range(n):
    a1, p1 = map(int, input().split())
    r1, p2 = map(int, input().split())
    a_per_dollar = a1 / p1
    b_per_dollar = math.pi * (r1 ** 2) / p2
    if a_per_dollar > b_per_dollar:
        print('Slice of pizza')
    else:
        print('Whole pizza')