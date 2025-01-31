def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

n = int(input())
print(factorial_recursive(n))