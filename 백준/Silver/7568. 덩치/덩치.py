n = int(input())
body_list = [list(map(int, input().split())) for _ in range(n)]
rank_list = []
for idx, body in enumerate(body_list):
    weight, height = body[0], body[1]
    body_self_excluded = body_list.copy()
    del body_self_excluded[idx]
    rank = 1
    for w, h in body_self_excluded:
        if w > weight and h > height:
            rank += 1
    rank_list.append(rank)
print(*rank_list)