import sys
from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    command = sys.stdin.readline().strip()
    if command[:4] == 'push':
        queue.append(int(command[5:]))
    elif command == 'pop':
        if len(queue):
            sys.stdout.write(str(queue.popleft()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')
    elif command == 'size':
        sys.stdout.write(str(len(queue)) + '\n')
    elif command == 'empty':
        if len(queue):
            sys.stdout.write(str(0) + '\n')
        else:
            sys.stdout.write(str(1) + '\n')
    elif command == 'front':
        if len(queue):
            sys.stdout.write(str(queue[0]) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')
    elif command == 'back':
        if len(queue):
            sys.stdout.write(str(queue[-1]) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')