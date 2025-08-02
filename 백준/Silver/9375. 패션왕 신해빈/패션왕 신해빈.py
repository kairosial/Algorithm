import sys
t = int(input())
for _ in range(t):
    clothes = {}
    n = int(sys.stdin.readline())
    for i in range(n):
        cloth, type_ = sys.stdin.readline().strip().split()
        if type_ in clothes:
            clothes[type_].append(cloth)
        else:
            clothes[type_] = [cloth]
    
    result = 1
    for type_ in clothes:
        result *= len(clothes[type_]) + 1
    print(result - 1)