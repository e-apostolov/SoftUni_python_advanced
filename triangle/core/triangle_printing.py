def print_upper_part(n):
    for row in range(1, n + 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()


def print_lower_part(n):
    for row in range(n - 1, - 1, - 1):
        for number in range(1, row + 1):
            print(number, end=" ")
        print()


def print_triangle(n):
    print_upper_part(n)
    print_lower_part(n)