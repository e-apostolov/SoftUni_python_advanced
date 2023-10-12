def sum_num(num1, num2):
    return f"{num1 + num2:.2f}"


def subtract(num1, num2):
    return f"{num1 - num2:.2f}"


def multiply(num1, num2):
    return f"{num1 * num2:.2f}"


def divide(num1, num2):
    try:
        return f"{num1 / num2:.2f}"
    except ZeroDivisionError:
        return "Cannot divide by zero"


def power(num1, num2):
    return f"{num1 ** num2:.2f}"
