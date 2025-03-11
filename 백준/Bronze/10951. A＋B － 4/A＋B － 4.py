import sys
cases = sys.stdin.readlines()
for case in cases:
    A, B = map(int, case.strip().split())
    print(A + B)