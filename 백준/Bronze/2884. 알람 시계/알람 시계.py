H, M = map(int, input().split())
m = M - 45
if m < 0:
    m += 60
    h = H - 1
    if h < 0:
        h += 24
else:
    h = H
print(h, m)