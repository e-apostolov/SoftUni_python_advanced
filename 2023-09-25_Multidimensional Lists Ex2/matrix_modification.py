def add_(some_row, some_column, some_value, some_matrix):
    if some_row in range(len(some_matrix)) and some_column in range(len(some_matrix[some_row])):
        matrix[some_row][some_column] += some_value
        return some_matrix
    else:
        print("Invalid coordinates")


def subtract_(some_row, some_column, some_value, some_matrix):
    if some_row in range(len(some_matrix)) and some_column in range(len(some_matrix[some_row])):
        matrix[some_row][some_column] -= some_value
        return some_matrix
    else:
        print("Invalid coordinates")


matrix = [[int(j) for j in input().split()]
          for i in range(int(input()))
          ]

while True:
    command = input()
    if command == "END":
        break

    command = command.split()
    row, column, value = [int(x) for x in command[1:]]
    if command[0] == "Add":
        add_(row, column, value, matrix)
    elif command[0] == "Subtract":
        subtract_(row, column, value, matrix)

[print(*row) for row in matrix]





