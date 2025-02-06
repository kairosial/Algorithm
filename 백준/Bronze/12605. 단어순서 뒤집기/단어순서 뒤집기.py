n = int(input())
for case_num in range(1, n+1):
    list_str = input().split()
    stack = [i for i in list_str[::-1]]
    print(f'Case #{case_num}:', *stack)