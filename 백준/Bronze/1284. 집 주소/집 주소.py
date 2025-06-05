while True:
    n = int(input())
    if n == 0:
        break
    num_str = [str(i) for i in str(n)]
    num_width = 2
    for s in num_str:
        if s == '1':
            num_width += 2
        elif s == '0':
            num_width += 4
        else:
            num_width += 3
    num_width += len(num_str) - 1
    print(num_width)