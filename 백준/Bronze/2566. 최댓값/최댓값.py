matrix = []
for _ in range(9):
    num_list = list(map(int, input().split()))
    matrix.append(num_list)

max_num = max(map(max, matrix)) # 2차원 이상 리스트에서는 단순 max 함수가 제대로 적용되지 않으므로 map 함수를 잘 활용해보자

def find_idx(matrix, max_num):
    for idx_i, i in enumerate(matrix):
        for idx_j, j in enumerate(i):
            if j == max_num:
                return idx_i+1, idx_j+1

a, b = find_idx(matrix, max_num)

print(max_num)
print(a, b)