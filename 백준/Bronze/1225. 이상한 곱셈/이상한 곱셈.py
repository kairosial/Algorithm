a_str, b_str = input().split()
sum_a = sum([int(a) for a in a_str])
sum_b = sum([int(b) for b in b_str])
print(sum_a * sum_b)