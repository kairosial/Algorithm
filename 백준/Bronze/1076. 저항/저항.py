res_color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
result = ''
for i in range(3):
    color = input()
    if i == 2:
        value = res_color.index(color)
        result = int(result)
        result *= 10 ** value
    else:
        result += str(res_color.index(color))
print(result)