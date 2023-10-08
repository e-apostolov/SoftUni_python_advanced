import os
WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(WORKING_DIRECTORY, "my_dir", "evgeni.txt")

print(file_path)

email = input()

file = open("users.txt", "a")
file.write(email + "\n")
file.close()

print(email)

file_1 = open(file_path, "a")
file_1.write(email + "\n")
file_1.close()

