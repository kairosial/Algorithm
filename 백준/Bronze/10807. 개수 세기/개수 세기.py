n = int(input())
x = list(map(int, input().split()))
v = int(input())

count = 0
for i in x:
    if i == v:
        count += 1
print(count)