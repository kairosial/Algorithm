n = int(input())

count_r = 0
def fib_r(n):
    global count_r
    if n == 1 or n == 2:
        count_r += 1
        return 1
    else:
        return (fib_r(n-1) + fib_r(n-2))

count_d = 0
def fib_d(n):
    global count_d
    f = [1] * (n+1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count_d += 1
    return f[n]

print(fib_d(n), count_d)