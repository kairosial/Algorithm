for _ in range(3):
    n = int(input())
    num_list = [int(input()) for _ in range(n)]
    if sum(num_list) == 0:
        print('0')
    elif sum(num_list) > 0:
        print('+')
    elif sum(num_list) < 0:
        print('-')