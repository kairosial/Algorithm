results = []
current = 0
for _ in range(4):
    off, on = map(int, input().split())
    current -= off
    current += on
    results.append(current)
print(max(results))