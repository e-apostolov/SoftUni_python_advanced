n = int(input())

odd_numbers = set()
even_numbers = set()


for row in range(1, n + 1):
    sum_ascii = sum([ord(x) for x in input()])
    result = int(sum_ascii/row)
    if result % 2 == 0:
        even_numbers.add(result)
    else:
        odd_numbers.add(result)

if sum(odd_numbers) == sum(even_numbers):
    union = odd_numbers.union(even_numbers)
    print(*union, sep=", ")
elif sum(odd_numbers) > sum(even_numbers):
    difference = odd_numbers.difference(even_numbers)
    print(*difference, sep=", ")
elif sum(odd_numbers) < sum(even_numbers):
    sym_diff = odd_numbers.symmetric_difference(even_numbers)
    print(*sym_diff, sep=", ")




