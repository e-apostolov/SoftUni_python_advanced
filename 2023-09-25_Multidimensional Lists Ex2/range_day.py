matrix = []
my_position = []
count_targets = 0

for row in range(5):
    matrix.append(input().split())
    for column in range(5):
        if matrix[row][column] == "A":
            my_position = [row, column]
        elif matrix[row][column] == "x":
            count_targets += 1

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

targets_shot = []

n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == "shoot":
        r = my_position[0] + directions[command[1]][0]
        c = my_position[1] + directions[command[1]][1]
        while 0 <= r < 5 and 0 <= c < 5:
            if matrix[r][c] == "x":
                matrix[r][c] = "."
                count_targets -= 1
                targets_shot.append([r, c])
                break
            r += directions[command[1]][0]
            c += directions[command[1]][1]
        if count_targets == 0:
            print(f"Training completed! All {len(targets_shot)} targets hit.")
            break
    elif command[0] == "move":
        steps = int(command[2])
        direction = command[1]
        if direction == "up":
            r = my_position[0] - steps
            c = my_position[1]
        elif direction == "down":
            r = my_position[0] + steps
            c = my_position[1]
        elif direction == "left":
            r = my_position[0]
            c = my_position[1] - steps
        elif direction == "right":
            r = my_position[0]
            c = my_position[1] + steps

        if 0 <= r < 5 and 0 <= c < 5 and matrix[r][c] == ".":
            matrix[r][c] = "A"
            matrix[my_position[0]][my_position[1]] = '.'
            my_position = [r, c]

if count_targets > 0:
    print(f"Training not completed! {count_targets} targets left.")
[print(row) for row in targets_shot]
