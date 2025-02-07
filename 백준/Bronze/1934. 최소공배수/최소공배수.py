import sys
T = int(input())

def GCD(A, B):
    if A % B == 0:
        return B
    return GCD(B, A % B)

for _ in range(T):
    A, B = map(int, sys.stdin.readline().strip().split())
    gcd = GCD(A, B)
    A, B = A // gcd, B // gcd
    lcm = gcd * A * B
    sys.stdout.write(str(lcm) + '\n')