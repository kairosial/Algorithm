import sys
T = int(input())

fib_01_list = [(1,0)]
for i in range(1, 41):
    fib_01_list.append((fib_01_list[i-1][1], fib_01_list[i-1][0]+fib_01_list[i-1][1]))

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    sys.stdout.write(str(fib_01_list[N][0]) + ' ' + str(fib_01_list[N][1]) + '\n')