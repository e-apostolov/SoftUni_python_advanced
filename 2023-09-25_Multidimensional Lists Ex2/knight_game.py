n = int(input())

matrix = []
knights = []
possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

for rows in range(n):
    matrix.append([x for x in input()])
    for columns in range(n):
        if matrix[rows][columns] == "K":
            knights.append([rows, columns])

removed_knights = 0

while True:
    max_hits = 0
    current_max_knight = [0, 0]
    for k_row, k_column in knights:
        current_hits = 0
        for move in possible_moves:
            new_row = k_row + move[0]
            new_column = k_column + move[1]
            if 0 <= new_row < n and 0 <= new_column < n:
                if matrix[new_row][new_column] == "K":
                    current_hits += 1
        if current_hits > max_hits:
            max_hits = current_hits
            current_max_knight = [k_row, k_column]

    if max_hits == 0:
        break
    else:
        knights.remove(current_max_knight)
        matrix[current_max_knight[0]][current_max_knight[1]] = '0'
        removed_knights += 1

print(removed_knights)









