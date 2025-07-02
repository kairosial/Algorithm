n = int(input())
time_ = list(map(int, input().split()))
time_.sort()
result = 0
for i in range(n):
    tmp = sum(time_[:i+1])
    result += tmp
print(result)