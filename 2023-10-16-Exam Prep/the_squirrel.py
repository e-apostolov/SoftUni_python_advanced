n = int(input())
directions = input().split(", ")
field_matrix = []
hazelnuts = 0
squirrel_position = []
is_game_over = False

move_mapper = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(n):
    field_matrix.append([x for x in input()])
    for column in range(n):
        if field_matrix[row][column] == "s":
            squirrel_position = [row, column]

for direction in directions:
    field_matrix[squirrel_position[0]][squirrel_position[1]] = "*"

    next_direction_row = squirrel_position[0] + move_mapper[direction][0]
    next_direction_column = squirrel_position[1] + move_mapper[direction][1]

    if not (0 <= next_direction_row < n and 0 <= next_direction_column < n):
        print("The squirrel is out of the field.")
        is_game_over = True
        break

    else:
        squirrel_position = [next_direction_row, next_direction_column]

    if field_matrix[next_direction_row][next_direction_column] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        is_game_over = True
        break

    if field_matrix[next_direction_row][next_direction_column] == "h":
        hazelnuts += 1
        if hazelnuts == 3:
            print("Good job! You have collected all hazelnuts!")
            break

if hazelnuts < 3 and not is_game_over:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts}")



