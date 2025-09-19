import math
a, b, c, d = map(int, input().split())
x = abs((a+b) - (c+d))
y = abs((a+c) - (b+d))
z = abs((b+c) - (a+d))
if x <= y and x <= z:
    print(x)
elif y <= x and y <= z:
    print(y)
elif z <= x and z <= y:
    print(z)