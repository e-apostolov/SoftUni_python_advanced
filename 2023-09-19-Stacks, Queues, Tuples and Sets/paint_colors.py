from collections import deque


input_string = deque(input().split())

main_colors = ["red", "blue", "yellow"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["blue", "yellow"]}

collected_colors = []

while input_string:
    first_substring = input_string.popleft()
    last_substring = input_string.pop() if input_string else ""
    if (first_substring + last_substring) in main_colors or (first_substring + last_substring) in secondary_colors:
        collected_colors.append(first_substring + last_substring)
    elif (last_substring + first_substring) in main_colors or (last_substring + first_substring) in secondary_colors:
        collected_colors.append(last_substring + first_substring)
    else:
        if len(first_substring) > 1:
            input_string.insert(len(input_string) // 2, first_substring[:-1])
        if len(last_substring) > 1:
            input_string.insert(len(input_string) // 2, last_substring[:-1])


for color in collected_colors:
    if color in secondary_colors:
        for element in secondary_colors[color]:
            if element not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)

