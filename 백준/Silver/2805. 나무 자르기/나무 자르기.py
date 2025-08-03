import sys
n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for t in trees:
        if t > mid:
            total += t - mid
    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)