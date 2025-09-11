names = [input() for _ in range(5)]
result = []
for idx, name in enumerate(names):
    if 'FBI' in name:
        result.append(idx+1)
if not result:
    print('HE GOT AWAY!')
else:
    print(*result)