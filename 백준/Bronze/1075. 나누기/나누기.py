n = input()
f = int(input())
n = n[:-2]
n_int = ''
for i in range(10):
    for j in range(10):
        n_int = int(n + str(i) + str(j))
        if n_int % f == 0:
            break
    if n_int % f == 0:
        break
result = str(n_int)[-2:]
print(result)