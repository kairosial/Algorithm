N = int(input())
num_list = list(map(int, input().split()))
max_num = max(num_list)
prime_num_list = []

def is_prime_number(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    for i in range(3, int(x**0.5)+1, 2):
        if x % i == 0:
            return False
    return True

for n in num_list:
    if is_prime_number(n):
        prime_num_list.append(n)

print(len(prime_num_list))