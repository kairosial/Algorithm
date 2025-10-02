import sys

def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)

while True:
    n_str = sys.stdin.readline().strip()
    if n_str == '0':
        break
    result = 0
    for idx, i in enumerate(n_str[::-1]):
        result += int(i) * factorial(idx+1)
    sys.stdout.write(f'{str(result)}\n')