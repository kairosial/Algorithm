import sys
n = int(sys.stdin.readline())

for i in range(n):
    # 앞쪽 공백 계산: (n-1), (n-2), ..., 0개
    num_spaces = n - 1 - i
    # 별 개수 계산: 1, 3, 5, ..., (2*n-1)개
    num_stars = 2 * i + 1
    
    # 공백과 별을 조합하여 출력
    print(' ' * num_spaces + '*' * num_stars)

for i in range(n - 2, -1, -1):
    # 앞쪽 공백 계산: 1, 2, ..., (n-1)개
    num_spaces = n - 1 - i
    # 별 개수 계산: (2*n-3), ..., 3, 1개
    num_stars = 2 * i + 1

    # 공백과 별을 조합하여 출력
    print(' ' * num_spaces + '*' * num_stars)