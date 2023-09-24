matrix = [
    [int(j) for j in input().split(", ")]
    for i in range(int(input()))
]

primary_diagonal = [matrix[i][i] for i in range(len(matrix))]
secondary_diagonal = [matrix[i][-i - 1]for i in range(len(matrix))]

# for row_index in range(len(matrix)):
#     for column_index in range(len(matrix[row_index])):
#         primary_diagonal.append(matrix[row_index][row_index])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
