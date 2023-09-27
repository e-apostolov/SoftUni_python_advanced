n = int(input())

matrix = []
bunny_position = []

for rows in range(n):
    matrix.append(input().split())
    for columns in range(n):
        if matrix[rows][columns] == "B":
            bunny_position = [rows, columns]

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_eggs = float('-inf')
max_direction = ''
max_eggs_submatrix = []

for direction, move in possible_moves.items():
    current_eggs = 0
    current_max_submatrix = []
    row = bunny_position[0] + move[0]
    column = bunny_position[1] + move[1]

    while 0 <= row < n and 0 <= column < n:
        if matrix[row][column] == "X":
            break
        current_eggs += int(matrix[row][column])
        current_max_submatrix.append([row, column])
        row += move[0]
        column += move[1]

    if current_eggs > max_eggs and current_max_submatrix:
        max_eggs = current_eggs
        max_direction = direction
        max_eggs_submatrix = current_max_submatrix

print(max_direction)
print(*max_eggs_submatrix, sep="\n")
print(max_eggs)

