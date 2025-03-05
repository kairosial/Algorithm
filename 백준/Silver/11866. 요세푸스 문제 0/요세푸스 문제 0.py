N, K = map(int, input().split())

num_list = [i for i in range(1, N+1)]
result = []
idx = -1
while num_list:
    idx += K
    if idx >= len(num_list):
        idx = idx % len(num_list)
    p = num_list.pop(idx)
    result.append(p)
    idx -= 1

print('<' + ', '.join(map(str, result)) + '>')