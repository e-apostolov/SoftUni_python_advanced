matrix = [
    [int(j) for j in input().split(", ")]
    for i in range(int(input()))
]

flattened = [num for sublist in matrix for num in sublist]

print(flattened)