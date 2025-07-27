import sys
N, M = map(int, sys.stdin.readline().split())

unheard = {sys.stdin.readline().strip() for _ in range(N)}

result = []

for _ in range(M):
    name = sys.stdin.readline().strip()
    if name in unheard:
        result.append(name)

result.sort()

print(len(result))
for name in result:
    sys.stdout.write(f'{name}\n')