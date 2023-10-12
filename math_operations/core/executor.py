from math_operations.core.operations import sum_num, subtract, divide, multiply, power

sign_mapper = {
    "+": sum_num,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "^": power
}


def execute_string(string):
    num1, sign, num2 = string.split()
    num1, num2 = float(num1), float(num2)
    return sign_mapper[sign](num1, num2)
