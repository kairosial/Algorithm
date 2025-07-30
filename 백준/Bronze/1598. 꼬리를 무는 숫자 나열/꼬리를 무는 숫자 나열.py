a, b = map(int, input().split())

if a % 4 == 0:
    a_row_idx = 3
else:
    a_row_idx = (a % 4) - 1
a_col_idx = (a-1) // 4

if b % 4 == 0:
    b_row_idx = 3
else:
    b_row_idx = (b % 4) - 1
a_col_idx = (a-1) // 4
b_col_idx = (b-1) // 4

result = (abs(a_col_idx - b_col_idx) + abs(a_row_idx - b_row_idx))
print(result)