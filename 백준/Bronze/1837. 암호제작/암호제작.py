P, K = map(int, input().split())

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

limit = min(K, int(P ** 0.5) + 1)
primes = sieve(limit)

r = 0
for prime in primes:
    if P % prime == 0:
        p = prime
        q = P // p
        r = q if p > q else p
        break

if r and r < K:
    print("BAD", r)
else:
    print("GOOD")