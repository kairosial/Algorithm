n, k = map(int, input().split())

def sieve_of_eratosthenes(n, k):
    list_num = [i for i in range(2, n+1)]
    list_num_temp = list_num.copy()
    count = 0
    while True:
        for num in list_num:
            min_val = min(list_num)
            if num % min_val == 0:
                list_num_temp.remove(num)
                count += 1
            if count == k:
                return num
        list_num = list_num_temp.copy()

print(sieve_of_eratosthenes(n,k))