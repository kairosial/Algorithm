n, b = list(map(str, input().split()))
b = int(b)

result = 0
n_lst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i, num in enumerate(n):
    digit = n_lst.index(num)
    result += digit * (b ** (abs(i-len(n)+1)))

print(result)