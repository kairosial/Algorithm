import sys
n = int(sys.stdin.readline())

def fibonacci(n):
    if n <= 1:
        return 1
    return n * fibonacci(n-1)
fib_n = str(fibonacci(n))

count = 0
for i in fib_n[::-1]:
    if i != '0':
        break
    count += 1
print(count)