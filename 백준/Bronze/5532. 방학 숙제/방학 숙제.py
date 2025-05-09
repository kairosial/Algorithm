vacation = [int(input()) for _ in range(5)]
l = vacation[0]
a = vacation[1]
b = vacation[2]
c = vacation[3]
d = vacation[4]

if a % c != 0:
    kor = (a // c) + 1
else:
    kor = (a // c)

if b % d != 0:
    math = (b // d) + 1
else:
    math = (b // d)

result = l - max(kor, math)
print(result)