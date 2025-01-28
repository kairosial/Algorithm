import sys
import math
n = int(sys.stdin.readline())
num = n
result = ''

def is_prime_number(x): # 효율적인 소수 판별
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    return True

while True:
    if is_prime_number(num): # 소수 판별
        num_str = str(num) # 팰린드롬수 판별
        if num_str == num_str[::-1]:
            result = num_str
            break
        else:
            num += 1
    else:
        num += 1

sys.stdout.write(result)