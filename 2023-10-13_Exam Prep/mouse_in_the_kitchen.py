rows_count, column_count = [int(x) for x in input().split(",")]


def check_valid_move(some_row, some_column):
    if 0 <= some_row < rows_count and 0 <= some_column < column_count:
        return True
    return False


matrix = []
count_of_cheese = 0
eaten_cheese = 0
mouse_position = []

directions_dict = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(rows_count):
    matrix.append([x for x in input()])
    for column in range(column_count):
        if matrix[row][column] == "M":
            mouse_position = [row, column]
        elif matrix[row][column] == "C":
            count_of_cheese += 1


while True:
    direction = input()
    if direction == "danger":
        break

    current_row, current_column = mouse_position
    next_row, next_column = current_row + directions_dict[direction][0], current_column + directions_dict[direction][1]

    if not check_valid_move(next_row, next_column):
        print("No more cheese for tonight!")
        break

    if matrix[next_row][next_column] == "C":
        matrix[next_row][next_column] = "M"
        mouse_position = [next_row, next_column]
        matrix[current_row][current_column] = "*"

        eaten_cheese += 1

        if eaten_cheese == count_of_cheese:
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[next_row][next_column] == "T":
        matrix[next_row][next_column] = "M"
        matrix[current_row][current_column] = "*"
        print("Mouse is trapped!")
        break

    elif matrix[next_row][next_column] == "@":
        continue

    else:
        matrix[next_row][next_column] = "M"
        mouse_position = [next_row, next_column]
        matrix[current_row][current_column] = "*"

if direction == "danger" and count_of_cheese > eaten_cheese:
    print(f"Mouse will come back later!")

[print(*row, sep="") for row in matrix]

