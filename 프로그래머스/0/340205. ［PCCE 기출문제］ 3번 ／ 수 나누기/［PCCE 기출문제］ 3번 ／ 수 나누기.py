number = int(input())

answer = 0

for _ in range(len(str(number)) // 2):
    answer += number % 100
    number //= 100

print(answer)