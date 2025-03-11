import sys
cases = sys.stdin.readlines()
for case in cases:
    A, B = map(int, case.strip().split())
    print(A + B)

# input()
# 사용자에게 입력을 받을 때 일반적으로 많이 사용되는 함수

# sys.stdin.readline()
# 입력 데이터의 양이 많을 경우, input() 함수 대신 sys.stdin.readline()을 사용하면 입력 속도를 향상시킬 수 있음
# 개행문자(\n)까지 함께 입력받으므로, 이를 제거하기 위해 strip() 메서드를 함께 사용함

# sys.stdin.read()
# 전체 입력을 한 번에 읽어들임
# 일반적으로 파일 전체를 문자열로 읽을 때 사용됨

# sys.stdin.readlines()
# 입력된 모든 줄을 읽어들여 각 줄을 요소로 갖는 리스트를 반환
# 이 문제에서는 종료 조건이 의도적으로 마련되지 않은 문제이므로 readlines를 사용함