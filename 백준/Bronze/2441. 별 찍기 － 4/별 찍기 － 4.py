n = int(input())
for idx, i in enumerate(range(n, 0, -1)):
    if i == n:
        print('*' * i)
    else:
        print(' ' * idx + '*' * i)