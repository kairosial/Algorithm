d = int(input())
cars = list(map(int, input().split()))

result = 0
for car in cars:
    if d == car:
        result += 1

print(result)