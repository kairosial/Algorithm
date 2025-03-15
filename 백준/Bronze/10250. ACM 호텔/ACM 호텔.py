T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        h = H
        w = N // H
    else:
        h = N % H
        w = (N // H) + 1

    if len(str(w)) == 1:
        print(str(h) + '0' + str(w))
    else:
        print(str(h) + str(w))