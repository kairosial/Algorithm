n = int(input())
k = input()
odd = 0
even = 0
for s_str in k:
    s = int(s_str)
    if s % 2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    print(0)
elif odd > even:
    print(1)
else:
    print(-1)