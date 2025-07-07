import sys
chrs = sys.stdin.read().splitlines()
num = 0
num_idx = -1
for idx, c in enumerate(chrs):
    try:
        num = int(c)
        num_idx = idx
    except:
        continue

num_list = [0, 0, 0]
num_list[num_idx] = num
for idx, n in enumerate(num_list):
    if n == 0:
        num_list[idx] = num + (idx - num_idx)

result = num_list[-1] + 1
if result % 3 == 0 and result % 5 == 0:
    result = 'FizzBuzz'
elif result % 3 == 0:
    result = 'Fizz'
elif result % 5 == 0:
    result = 'Buzz'
print(result)