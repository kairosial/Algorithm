import sys
import math
m, n = map(int, (sys.stdin.readline().split()))
result = []

def is_prime_number(x):
    if x < 2:
        return None
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return None
    return x

for _ in range(m, n+1):
    result.append(is_prime_number(_))

for num in result:
    if num != None:
        sys.stdout.write(str(num)+'\n')