n = int(input())
input_str = input()
result = 0
for idx, s in enumerate(input_str):
    str2int = ord(s) - 96
    result += str2int * (31 ** idx)
print(result % 1234567891)