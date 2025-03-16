remainder = []
for _ in range(10):
    n = int(input())
    remainder.append(n % 42)
result = set(remainder)
print(len(result))