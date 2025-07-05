isbn = input()
isbn_list = [_ for _ in isbn]
isbn_sum = 0
s_weight = 0
for idx, i in enumerate(isbn_list):
    if i != '*':
        n = int(i)
        if idx % 2 == 0:
            weight = 1
        else:
            weight = 3
        isbn_sum += weight * n
    else:
        if idx % 2 == 0:
            s_weight = 1
        else:
            s_weight = 3

result = 0
for j in range(10):
    if (isbn_sum + (s_weight * j)) % 10 == 0:
        result = j

print(result)