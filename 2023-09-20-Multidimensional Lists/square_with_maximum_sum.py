import sys

rows, columns = [int(x) for x in input().split(", ")]


matrix = [
    [int(j) for j in input().split(", ")]
    for i in range(rows)
]

max_sum = -sys.maxsize
max_sum_sub_matrix = []

for row_index in range(len(matrix) - 1):
    for column_index in range(len(matrix[row_index]) - 1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        below_element = matrix[row_index + 1][column_index]
        element_diagonal = matrix[row_index + 1][column_index + 1]
        sum_elements = current_element + next_element + below_element + element_diagonal
        if max_sum < sum_elements:
            max_sum = sum_elements
            max_sum_sub_matrix = [[current_element, next_element], [below_element, element_diagonal]]

[print(*row) for row in max_sum_sub_matrix]
print(max_sum)