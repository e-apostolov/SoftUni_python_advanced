n = int(input())

matrix = []
alice_position = []

for rows in range(n):
    matrix.append(input().split())
    for columns in range(n):
        if matrix[rows][columns] == "A":
            matrix[rows][columns] = "*"
            alice_position = [rows, columns]

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

collected_tea_bags = 0

while collected_tea_bags < 10:
    command = input()
    move = possible_moves[command]
    row = alice_position[0] + move[0]
    column = alice_position[1] + move[1]

    if row < 0 or row >= n or column < 0 or column >= n:
        break
    if matrix[row][column] == "R":
        matrix[row][column] = "*"
        break

    if matrix[row][column] not in "*.":
        collected_tea_bags += int(matrix[row][column])
    matrix[row][column] = "*"
    alice_position = [row, column]


if collected_tea_bags == 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]



