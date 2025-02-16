A, B = map(int, input().split())

def GCD(a, b):
    if a % b == 0:
        return b
    return GCD(b, a % b)

def LCM(a, b, gcd):
    a_r = a // gcd
    b_r = b // gcd
    return gcd * a_r * b_r

gcd = GCD(A, B)
lcm = LCM(A, B, gcd)

print(gcd)
print(lcm)