def is_valid(row, column, some_n):
    return 0 <= row < some_n and 0 <= column < some_n


n = int(input())
commands= input().split()

matrix = []
current_row, current_column = 0, 0
coal = 0
is_game_over = False

for row_index in range(n):
    matrix.append(input().split())
    for column_index in range(n):
        if matrix[row_index][column_index] == 's':
            current_row, current_column = row_index, column_index
        elif matrix[row_index][column_index] == "c":
            coal += 1

for command in commands:
    if command == "up":
        if is_valid(current_row -1, current_column, n):
            current_row -= 1
    elif command == "down":
        if is_valid(current_row + 1, current_column, n):
            current_row += 1
    elif command == "left":
        if is_valid(current_row, current_column - 1, n):
            current_column -= 1
    elif command == "right":
        if is_valid(current_row, current_column + 1, n):
            current_column += 1

    if matrix[current_row][current_column] == "e":
        print(f"Game over! ({current_row}, {current_column})")
        is_game_over = True
        break
    if matrix[current_row][current_column] == "c":
        coal -= 1
        matrix[current_row][current_column] = "*"
        if coal == 0:
            print(f"You collected all coal! ({current_row}, {current_column})")
            is_game_over = True
            break

if not is_game_over:
    print(f"{coal} pieces of coal left. ({current_row}, {current_column})")