import sys
T = int(input())

def padovan(seq, n):
    return seq[n-1] + seq[n-5]

p_seq = [0, 1, 1, 1, 2]
for i in range(5, 101):
    p_seq.append(padovan(p_seq, i))

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    sys.stdout.write(str(p_seq[N]) + '\n')