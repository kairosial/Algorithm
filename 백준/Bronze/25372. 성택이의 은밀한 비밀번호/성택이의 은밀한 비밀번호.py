n = int(input())
for _ in range(n):
    input_str = input()
    if 6 <= len(input_str) <= 9:
        print('yes')
    else:
        print('no')