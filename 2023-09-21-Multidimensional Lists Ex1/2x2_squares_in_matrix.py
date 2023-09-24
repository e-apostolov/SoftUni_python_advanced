rows, columns = [int(x) for x in input().split()]

matrix = [
    [j for j in input().split()]
    for i in range(rows)
]

squares = 0

for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        below_element = matrix[row_index + 1][column_index]
        diagonal_element = matrix[row_index + 1][column_index + 1]
        if current_element == next_element == below_element == diagonal_element:
            squares += 1

print(squares)
