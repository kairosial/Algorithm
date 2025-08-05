import sys

a, b = sys.stdin.readline().split()

num_a = int(a, 2)
num_b = int(b, 2)

sum_result = num_a + num_b

binary_sum = bin(sum_result)[2:]

print(binary_sum)