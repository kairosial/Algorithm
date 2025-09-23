string = input()
alphabet = [0 for _ in range(123)]
for s in string:
    asc = ord(s)
    alphabet[asc] += 1
print(*alphabet[97:123])