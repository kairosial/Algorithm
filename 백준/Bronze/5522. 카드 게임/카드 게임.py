import sys
sum = 0
for _ in range(5):
    score = int(sys.stdin.readline())
    sum += score
sys.stdout.write(str(sum))