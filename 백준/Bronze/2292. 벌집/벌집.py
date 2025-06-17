n = int(input())
i = 1
k = 1
result = []
while i < n:
    result.append(i)
    i = i + (6 * k)
    k += 1
print(len(result) + 1)