import os

WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

file = os.path.join(WORKING_DIRECTORY, "new_file")

with open(file, "w") as file:
    print(file.closed)
    file.write("hello")

print(file.closed)

