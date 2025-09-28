scores = []
for _ in range(5):
    score = list(map(int, input().split()))
    scores.append(score)

max_score = 0
max_idx = 0
for idx, score in enumerate(scores):
    score_sum = sum(score)
    if max(max_score, score_sum) > max_score:
        max_idx = idx + 1
        max_score = max(max_score, score_sum)

print(max_idx, max_score)