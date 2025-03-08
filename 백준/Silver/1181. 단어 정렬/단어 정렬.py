import sys
N = int(sys.stdin.readline().strip())
word_list = []
for _ in range(N):
    word = sys.stdin.readline().strip()
    word_list.append(word)
word_set = set(word_list)
result = sorted(word_set, key=lambda x: (len(x), x))
print(*result, sep='\n')