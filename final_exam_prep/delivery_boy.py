field_row, field_column = (int(x) for x in input().split())


matrix = []
starting_position = []
current_position = []
is_pizza_collected = False

directions_dict = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

for row in range(field_row):
    matrix.append([x for x in input()])
    for column in range(field_column):
        if matrix[row][column] == "B":
            starting_position = [row, column]
            current_position = [row, column]

while True:
    direction = input()

    next_row = current_position[0] + directions_dict[direction][0]
    next_column = current_position[1] + directions_dict[direction][1]

    if not (0 <= next_row < field_row and 0 <= next_column < field_column):
        print("The delivery is late. Order is canceled.")
        matrix[starting_position[0]][starting_position[1]] = " "
        break

    if matrix[next_row][next_column] == "*":
        continue

    if matrix[next_row][next_column] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        is_pizza_collected = True
        matrix[next_row][next_column] = "R"
        current_position = [next_row, next_column]
        continue

    if matrix[next_row][next_column] == "A" and is_pizza_collected:
        print("Pizza is delivered on time! Next order...")
        matrix[next_row][next_column] = "P"
        matrix[starting_position[0]][starting_position[1]] = "B"
        break

    matrix[next_row][next_column] = "."
    current_position = [next_row, next_column]


for row in matrix:
    print("".join(row))





