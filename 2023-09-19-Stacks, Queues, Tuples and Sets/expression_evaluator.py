from collections import deque

input_string = input().split()
numbers = deque()

for char in input_string:
    if char not in "+-*/":
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            if char == "+":
                numbers.appendleft(first_number + second_number)
            elif char == "-":
                numbers.appendleft(first_number - second_number)
            elif char == "*":
                numbers.appendleft(first_number * second_number)
            elif char == "/":
                numbers.appendleft(first_number // second_number)

print(*numbers)
