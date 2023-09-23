letters = tuple(input())

occurrence = {}

for letter in letters:
    occurrence[letter] = letters.count(letter)

for key, value in sorted(occurrence.items()):
    print(f"{key}: {value} time/s")