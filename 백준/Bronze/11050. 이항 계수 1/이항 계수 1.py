N, K = map(int, input().split())

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

result = int(factorial_recursive(N) / (factorial_recursive(N-K) * factorial_recursive(K)))
print(result)