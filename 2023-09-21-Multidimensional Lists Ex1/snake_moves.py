from collections import deque

rows, columns = [int(x) for x in input().split()]
input_string = deque(input())

matrix = []

for row_index in range(rows):
    matrix.append([''] * columns)
    for column_index in range(columns):
        if row_index % 2 == 0:
            matrix[row_index][column_index] = input_string[0]
        else:
            matrix[row_index][-1 - column_index] = input_string[0]
        input_string.rotate(-1)

[print(*row, sep='') for row in matrix]



