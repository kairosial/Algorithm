n, m = map(int, input().split())
n_str = str(n)
nn_str = n_str * n
max_len = len(nn_str)
if max_len > m:
    print(nn_str[:m])
else:
    print(nn_str)