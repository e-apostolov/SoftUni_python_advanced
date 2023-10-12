from math import log

input_number = int(input())

command = input()

if command == "natural":
    print(f"{log(input_number):.2f}")

else:
    print(f"{log(input_number, int(command)):.2f}")
