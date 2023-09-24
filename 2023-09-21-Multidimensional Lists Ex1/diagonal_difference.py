matrix = [
    [int(j) for j in input().split()]
    for i in range(int(input()))
]

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][-i - 1]for i in range(len(matrix))]

primary_diagonal_sum = sum(primary_diagonal)
secondary_diagonal_sum = sum(secondary_diagonal)

print(abs(primary_diagonal_sum - secondary_diagonal_sum))