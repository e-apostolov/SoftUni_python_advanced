from collections import deque

input_expression = deque(input())
opening_parentheses = "([{"
closing_parentheses = ")]}"

counter = 0

while input_expression and counter < len(input_expression) / 2:
    if input_expression[0] not in (opening_parentheses):
        break
    index = opening_parentheses.index(input_expression[0])
    if input_expression[1] == closing_parentheses[index]:
        input_expression.popleft()
        input_expression.popleft()
        input_expression.rotate(counter)
        counter = 0
    else:
        input_expression.rotate(-1)
        counter += 1

if input_expression:
    print("NO")
else:
    print("YES")