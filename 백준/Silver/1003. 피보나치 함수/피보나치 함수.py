import sys
T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    f0, f1 = 1, 0
    if N == 0:
        print(f0, f1)
    else:
        for i in range(1, N+1):
            f0, f1 = f1, f0+f1
        print(f0, f1)