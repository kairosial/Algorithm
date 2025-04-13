score_list = [int(input()) for _ in range(5)]
for idx, score in enumerate(score_list):
    if score < 40:
        score_list[idx] = 40
print(int(sum(score_list) / 5))