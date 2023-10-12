from fibonacci.core.fibonacci_functions import *


def play_fibonacci():
    sequence = []
    while True:
        command = input()
        if command == "Stop":
            break
        n = int(command.split()[-1])
        if command.startswith("Create"):
            sequence = create_sequence(n)
            print(*sequence)
        elif command.startswith("Locate"):
            print(locate_index(n, sequence))

