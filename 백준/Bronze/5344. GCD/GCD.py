import sys
n = int(sys.stdin.readline().strip())

# 유클리드 호제법
# 두 수  a와 b(a > b)의 최대공약수는 b와, a를 b로 나눈 나머지의 최대공약수와 같다.
# GCD(a,b) = GCD(b, a mod b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for _ in range(n):
    GCD = 1
    a, b = map(int, sys.stdin.readline().strip().split())
    big, small = max(a, b), min(a, b)
    GCD = gcd(big, small)
    sys.stdout.write(str(GCD)+'\n')