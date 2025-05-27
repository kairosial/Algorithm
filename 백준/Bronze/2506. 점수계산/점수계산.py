n = int(input())
marks = list(map(int, input().split()))
stack = 0
score = 0
for m in marks:
    if m == 1:
        score += stack + 1
        stack += 1
    else:
        stack = 0
print(score)