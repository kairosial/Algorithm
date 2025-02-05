import sys
n = int(sys.stdin.readline().strip())
stack = []

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith('push'):
        num = int(list(command.split())[1])
        stack.append(num)
        continue
    elif command == 'pop':
        if len(stack) == 0:
            result = -1
        else:
            result = stack.pop()
    elif command == 'size':
        result = len(stack)
    elif command == 'empty':
        if len(stack) == 0:
            result = 1
        else:
            result = 0
    elif command == 'top':
        if len(stack) == 0:
            result = -1
        else:
            result = stack[-1]

    sys.stdout.write(str(result)+'\n')