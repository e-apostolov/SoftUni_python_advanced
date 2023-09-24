rows, columns = [int(x) for x in input().split()]

matrix = [
    [int(j) for j in input().split()]
    for i in range(rows)
]

max_sum = float('-inf')
max_row = 0
max_column = 0

for row_index in range(rows - 2):
    for column_index in range(columns - 2):
        current_sum = 0
        for r in range(row_index, row_index + 3):
            for c in range(column_index, column_index + 3):
                current_sum += matrix[r][c]
        if current_sum > max_sum:
            max_sum = current_sum
            max_row = row_index
            max_column = column_index

print(f"Sum = {max_sum}")
max_submatrix = [matrix[i][max_column:max_column+3] for i in range(max_row, max_row + 3)]
[print(*row) for row in max_submatrix]


