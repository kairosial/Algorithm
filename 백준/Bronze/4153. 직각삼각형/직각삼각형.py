import sys
while True:
    num_list = list(map(int, sys.stdin.readline().strip().split()))
    c = max(num_list)
    num_list.remove(c)
    a = num_list[0]
    b = num_list[1]
    if a == 0 and b == 0 and c == 0:
        break
    
    if (a ** 2) + (b ** 2) == (c ** 2):
        sys.stdout.write('right\n')
    else:
        sys.stdout.write('wrong\n')