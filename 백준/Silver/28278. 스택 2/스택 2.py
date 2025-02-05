import sys
n = int(sys.stdin.readline().strip())
stack = []

for _ in range(n):
    command = sys.stdin.readline().strip()
    if command.startswith('1'):
        num = int(list(command.split())[1])
        stack.append(num)
        continue
    elif command == '2':
        if len(stack) == 0:
            result = -1
        else:
            result = stack.pop()
    elif command == '3':
        result = len(stack)
    elif command == '4':
        if len(stack) == 0:
            result = 1
        else:
            result = 0
    elif command == '5':
        if len(stack) == 0:
            result = -1
        else:
            result = stack[-1]

    sys.stdout.write(str(result)+'\n')