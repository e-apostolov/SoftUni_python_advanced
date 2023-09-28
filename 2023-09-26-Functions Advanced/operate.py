# def operate(sign, *args):
#     def add():
#         return sum(args)
#
#     def subtract():
#         result = args[0]
#         for el in args[1:]:
#             result -= el
#         return result
#
#     def multiply():
#         result = 1
#         for el in args:
#             result *= el
#         return result
#
#     def divide():
#         result = args[0]
#         for el in args[1:]:
#             result /= el
#         return result
#
#     if sign == "+":
#         return add()
#     elif sign == "-":
#         return subtract()
#     elif sign == "*":
#         return multiply()
#     elif sign == "/":
#         return divide()

def operate(sign, *args):
    result = args[0]
    for number in args[1:]:
        if sign == "+":
            result += number
        elif sign == "-":
            result -= number
        elif sign == "*":
            result *= number
        elif sign == "/":
            result /= number
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

