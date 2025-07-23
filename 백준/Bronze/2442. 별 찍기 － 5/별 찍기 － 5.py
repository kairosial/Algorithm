n = int(input())
for a, b in enumerate(range(n, 0, -1)):
    blank = b-1
    star = (a+1)*2 - 1
    print(' '*blank  + '*'*star)