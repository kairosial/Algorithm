def sieve_of_eratosthenes(m, n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i : n+1 : i] = [False] * len(sieve[i*i : n+1 : i])
    prime_num_list = [i for i in range(m, n+1) if sieve[i]]
    return prime_num_list

m, n = map(int, input().split())
result = sieve_of_eratosthenes(m, n)
for i in result:
    print(i)