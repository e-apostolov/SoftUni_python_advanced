input_numbers = [x for x in input().split()]
output_numbers = []

while input_numbers:
    output_numbers.append(input_numbers.pop())

print(" ".join(output_numbers))
