matrix = [
    [int(j) for j in input().split()]
    for i in range(int(input()))
]

sum_diagonal = 0
secondary_diagonal = 0
for row_index in range(len(matrix)):
    sum_diagonal += matrix[row_index][row_index]
    secondary_diagonal += matrix[row_index][len(matrix) - row_index - 1]

print(sum_diagonal)
print(secondary_diagonal)