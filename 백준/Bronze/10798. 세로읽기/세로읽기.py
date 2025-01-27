import sys

matrix = []
for _ in range(5):
    string = list(sys.stdin.readline().strip())
    matrix.append(string)

result = ''
for col_idx in range(max((map(len, matrix)))):
    for row_idx in range(len(matrix)):
        try:
            result += matrix[row_idx][col_idx]
        except:
            pass

sys.stdout.write(result)