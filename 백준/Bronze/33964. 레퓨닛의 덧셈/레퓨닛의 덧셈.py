x, y = map(int, input().split())
x_str = ''
y_str = ''
for _ in range(x):
    x_str += '1'
for _ in range(y):
    y_str += '1'

x_int = int(x_str)
y_int = int(y_str)

print(x_int + y_int)