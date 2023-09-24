rows, columns = [int(x) for x in input().split(", ")]


matrix = [
    [int(j) for j in input().split()]
    for i in range(rows)
]

for column_index in range(columns):
    current_total = 0
    for row_index in range(rows):
        current_total += matrix[row_index][column_index]
    print(current_total)
