def is_coordinates_valid(r1, c1, r2, c2, some_rows, some_columns):
    return 0 <= r1 < some_rows and 0 <= r2 < some_rows and 0 <= c1 < some_columns and 0 <= c2 < some_columns


rows, columns = [int(x) for x in input().split()]

matrix = [
    [int(j) for j in input().split()]
    for i in range(rows)
]

while True:
    command = input().split()
    if command[0] == "END":
        break

    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_coordinates_valid(row1, col1, row2, col2, rows, columns):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        [print(*r) for r in matrix]
    else:
        print("Invalid input!")

