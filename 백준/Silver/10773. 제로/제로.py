import sys
k = int(sys.stdin.readline().strip())
stack = []
result = 0
for _ in range(k):
    num = int(sys.stdin.readline().strip())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
result = sum(stack)
sys.stdout.write(str(result)+'\n')