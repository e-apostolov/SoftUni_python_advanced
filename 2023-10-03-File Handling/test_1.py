import os
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, "text.txt")

file = open(file_path, "r")

file.close()
print(file.readlines(2))
