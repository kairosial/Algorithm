n = int(input())
content = [input() for _ in range(n)]
for idx, c in enumerate(content):
    print(f"{idx+1}. {c}")