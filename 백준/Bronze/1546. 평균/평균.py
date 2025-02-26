N = int(input())
org_score_list = list(map(int, input().split()))
new_score_list = []
M = max(org_score_list)
for org_score in org_score_list:
    new_score_list.append(org_score / M * 100)
print(sum(new_score_list) / N)