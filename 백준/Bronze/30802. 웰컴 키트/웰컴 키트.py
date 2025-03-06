N = int(input())
size_list = list(map(int, input().split()))
T, P = map(int, input().split())

result_T = 0
for size in size_list:
    if size % T == 0:
        quotient_T = (size // T)
    else:
        quotient_T = (size // T) + 1
    result_T += quotient_T
print(result_T)
print(N // P, N % P)