import re

with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()


with open("input.txt", "r") as file:
    text = file.read().lower()

words = {}

for word in searched_words:
    pattern = rf"\b{word}\b"
    result = re.findall(pattern, text)
    words[word] = len(result)

sorted_words = sorted(words.items(), key=lambda x: -x[1])

with open("output.txt", "w") as file:
    for key, value in sorted_words:
        file.write(f"{key} - {value}\n")
