from collections import defaultdict

n = int(input())
fruits = list(map(int, input().split()))

count = defaultdict(int)
left = 0
max_len = 0

for right in range(n):
    count[fruits[right]] += 1
    
    while len(count) > 2:  # 종류가 3개 이상이면
        count[fruits[left]] -= 1
        if count[fruits[left]] == 0:
            del count[fruits[left]]
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)