n = int(input())
origin_n = str(n)
result = 0

if len(origin_n) == 1:
    origin_n = '0' + origin_n

tmp_n = origin_n

while True:
    l_n = tmp_n[0]
    r_n = tmp_n[1]
    sum_n = str(int(l_n) + int(r_n))
    new_n = tmp_n[-1] + sum_n[-1]
    result += 1
    if origin_n == new_n:
        print(result)
        break
    else:
        tmp_n = new_n