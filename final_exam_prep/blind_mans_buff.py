number_of_rows, number_of_columns = (int(x) for x in input().split())


field = []
number_of_moves = 0
touched_opponents = 0
player_position = []

directions_dict = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(number_of_rows):
    field.append([x for x in input().split()])
    for column in range(number_of_columns):
        if field[row][column] == "B":
            player_position = [row, column]

while True:
    if touched_opponents == 3:
        break

    command = input()
    if command == "Finish":
        break

    next_move_row = player_position[0] + directions_dict[command][0]
    next_move_column = player_position[1] + directions_dict[command][1]

    if not (0 <= next_move_row < number_of_rows and 0 <= next_move_column < number_of_columns):
        continue

    if field[next_move_row][next_move_column] == "O":
        continue

    elif field[next_move_row][next_move_column] == "P":
        field[next_move_row][next_move_column] = "-"
        touched_opponents += 1

    field[player_position[0]][player_position[1]] = "-"
    player_position = [next_move_row, next_move_column]
    number_of_moves += 1

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {number_of_moves}")
