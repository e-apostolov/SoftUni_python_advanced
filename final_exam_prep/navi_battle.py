n = int(input())

field_matrix = []
submarine_position = []
mine_hits = 0
cruisers_destroyed = 0

moves_dict = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}


for row in range(n):
    field_matrix.append([x for x in input()])
    for column in range(n):
        if field_matrix[row][column] == "S":
            submarine_position = [row, column]


while True:

    command = input()

    next_row = submarine_position[0] + moves_dict[command][0]
    next_column = submarine_position[1] + moves_dict[command][1]

    if field_matrix[next_row][next_column] == "*":
        field_matrix[next_row][next_column] = "-"
        mine_hits += 1
        if mine_hits == 3:
            field_matrix[submarine_position[0]][submarine_position[1]] = "-"
            submarine_position = [next_row, next_column]
            field_matrix[next_row][next_column] = "S"
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{submarine_position[0]}, {submarine_position[1]}]!")
            break

    if field_matrix[next_row][next_column] == "C":
        field_matrix[next_row][next_column] = "-"
        cruisers_destroyed += 1
        if cruisers_destroyed == 3:
            if cruisers_destroyed == 3:
                field_matrix[submarine_position[0]][submarine_position[1]] = "-"
                field_matrix[next_row][next_column] = "S"
                print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
                break

    field_matrix[submarine_position[0]][submarine_position[1]] = "-"
    submarine_position = [next_row, next_column]
    field_matrix[next_row][next_column] = "S"


[print(*row, sep="") for row in field_matrix]
