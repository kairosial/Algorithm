board = []
for _ in range(8):
    row = list(input())
    board.append(row)

result = 0
for i, row in enumerate(board):
    for j, space in enumerate(row):
        if (i + j) % 2 == 0 and space == 'F':
            result += 1
print(result)