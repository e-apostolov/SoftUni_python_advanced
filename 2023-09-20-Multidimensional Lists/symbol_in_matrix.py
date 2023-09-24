matrix = [
    [j for j in input()]
    for i in range(int(input()))
]

element_to_find = input()

is_found = False

for row_index in range(len(matrix)):
    if is_found:
        break
    for column_index in range(len(matrix[row_index])):
        current_element = matrix[row_index][column_index]
        if current_element == element_to_find:
            print((row_index, column_index))
            is_found = True
            break

if not is_found:
    print(f"{element_to_find} does not occur in the matrix")