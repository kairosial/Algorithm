serial_number = list(map(int, input().split()))
serial_number_sq = [(x ** 2) for x in serial_number]
serial_number_sum = sum(serial_number_sq)
print(serial_number_sum % 10)