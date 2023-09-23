expression = input()

stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        last_par = stack.pop()
        closing_par = i + 1
        print(expression[last_par:closing_par])