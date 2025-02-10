import sys
T = int(input())
for _ in range(T):
    R, S = sys.stdin.readline().strip().split()
    R = int(R)
    result = ''
    for s in S:
        result += s * R
    sys.stdout.write(result + '\n')