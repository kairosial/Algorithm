import sys

# 테스트 케이스의 개수 T를 입력받습니다.
T = int(sys.stdin.readline())

for _ in range(T):
    # 정수 a와 b를 입력받습니다.
    a, b = map(int, sys.stdin.readline().split())

    # pow(a, b, 10)은 (a^b) % 10, 즉 a^b의 마지막 자리 숫자를 계산합니다.
    last_digit = pow(a, b, 10)

    # 마지막 자리 숫자가 0이면 10번 컴퓨터가 처리한 것입니다.
    if last_digit == 0:
        print(10)
    # 그 외의 경우에는 해당 숫자와 동일한 번호의 컴퓨터가 처리합니다.
    else:
        print(last_digit)