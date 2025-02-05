import sys
t = int(sys.stdin.readline().strip())

for _ in range(t):
    PS = sys.stdin.readline().strip()
    while True:
        idx = PS.find('()')
        if idx == -1:
            if len(PS) == 0:
                result = 'YES'
                break
            else:
                result = 'NO'
                break
        else:
            PS = PS[:idx] + PS[idx+2:]

    sys.stdout.write(str(result)+'\n')