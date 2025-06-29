m, n = map(int, input().split())
matrix = [list(input()) for _ in range(m)]
result = float('inf')
for x in range(m-8+1):
    for y in range(n-8+1):
        sub_matrix = [row[y:y+8] for row in matrix[x:x+8]]
        repaint_w_start = 0
        repaint_b_start = 0
        for r in range(8):
            for c in range(8):
                current_color = sub_matrix[r][c]
                if (r + c) % 2 == 0:
                    if current_color != 'W':
                        repaint_w_start += 1
                    if current_color != 'B':
                        repaint_b_start += 1
                else:
                    if current_color != 'B':
                        repaint_w_start += 1
                    if current_color != 'W':
                        repaint_b_start += 1
        min_sub_matrix = min(repaint_w_start, repaint_b_start)
        result = min(result, min_sub_matrix)
print(result)