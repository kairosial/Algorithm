n = int(input())
progression = []
for _ in range(n):
    num = int(input())
    progression.append(num)

stack = []
result = []
i = 0

for t in progression:
    if stack and t == stack[-1]:
        p = stack.pop()
        result.append('-')
        if p == t:
            continue
    
    while i < t:
        i += 1
        stack.append(i)
        result.append('+')

    if stack[-1] == t:
        p = stack.pop()
        result.append('-')
    else:
        print('NO')
        exit()
print(*result, sep='\n')