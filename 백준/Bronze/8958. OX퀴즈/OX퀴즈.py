import sys
n = int(input())
for _ in range(n):
    ox_str = sys.stdin.readline().strip()
    result = 0
    temp = 0       # X가 나오기 전까지 더해놓는 숫자
    add_num = 1    # O가 두 번 이상 나올 때 +1씩 증가시킬 숫자
    for c in ox_str:
        if c == 'O':
            if temp == 0:
                temp += add_num
            else:
                add_num += 1
                temp += add_num
        else:
            result += temp
            temp = 0
            add_num = 1
    if temp != 0:
        result += temp
    sys.stdout.write(str(result) + '\n')