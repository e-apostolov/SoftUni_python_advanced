number_of_presents = int(input())
n = int(input())

santa_position = []
matrix = []
count_of_nice_kids = 0
count_of_nice_kids_wp = 0

possible_moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),

    'up_left': (-1, -1),
    'up_right': (-1, 1),
    'down_left': (1, -1),
    'down_right': (1, 1)
}

for row in range(n):
    matrix.append(input().split())
    for column in range(n):
        if matrix[row][column] == "V":
            count_of_nice_kids += 1
        elif matrix[row][column] == "S":
            santa_position = [row, column]
            matrix[row][column] = "-"

while number_of_presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    row = santa_position[0] + possible_moves[command][0]
    column = santa_position[1] + possible_moves[command][1]
    if 0 <= row < n and 0 <= column < n:
        santa_position = [row, column]
        if matrix[row][column] == "X":
            matrix[row][column] = '-'
            continue
        elif matrix[row][column] == "V":
            number_of_presents -= 1
            count_of_nice_kids_wp += 1
            matrix[row][column] = '-'
        elif matrix[row][column] == "C":
            for key, value in possible_moves.items():
                r = row + value[0]
                c = column + value[1]
                if number_of_presents > 0:
                    if matrix[r][c] == "V":
                        number_of_presents -= 1
                        count_of_nice_kids_wp += 1
                        matrix[r][c] = "-"
                    elif matrix[r][c] == "X":
                        number_of_presents -= 1
                        matrix[r][c] = "-"


matrix[santa_position[0]][santa_position[1]] = "S"
if number_of_presents == 0 and count_of_nice_kids - count_of_nice_kids_wp > 0:
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if count_of_nice_kids - count_of_nice_kids_wp == 0:
    print(f"Good job, Santa! {count_of_nice_kids_wp} happy nice kid/s.")
else:
    print(f"No presents for {count_of_nice_kids - count_of_nice_kids_wp} nice kid/s.")
