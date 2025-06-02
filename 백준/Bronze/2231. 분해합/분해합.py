n = int(input())
scope_min = len(str(n)) * 9

def is_generator(candidate, target):
    return (candidate + sum(int(d) for d in str(candidate))) == target

candidate_list = []
for i in range(max(1, n - scope_min), n):
    if is_generator(i, n):
        candidate_list.append(i)

if candidate_list:
    print(min(candidate_list))
else:
    print(0)