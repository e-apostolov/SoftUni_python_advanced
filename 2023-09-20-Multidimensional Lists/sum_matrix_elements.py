data = input().split(", ")
rows = int(data[0])
columns = int(data[1])

matrix = []
sum_elements = 0

for _ in range(rows):
    elements = [int(x) for x in input().split(", ")]
    sum_elements += sum(elements)
    matrix.append(elements)

print(sum_elements)
print(matrix)

