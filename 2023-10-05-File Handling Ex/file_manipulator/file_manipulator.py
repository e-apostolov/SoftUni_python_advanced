import os

while True:
    line = input()
    if line == "End":
        break

    command, file_name, *args = line.split("-")
    if command == "Create":
        open(file_name, "w").close()
    elif command == "Add":
        with open(file_name, "a") as file:
            file.write(f"{args[0]}\n")
    elif command == "Replace":
        try:
            with open(file_name) as file:
                content = file.read()
        except FileNotFoundError:
            print("An error occurred")
        else:
            with open(file_name, 'w') as file:
                content = content.replace(args[0], args[1])
                file.write(content)
    elif command == "Delete":
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print("An error occurred")


# """2nd solution with functions:"""
#
# import os
#
#
# def create(some_file_name):
#     open(file_name, "w").close()
#
#
# def add(some_file_name, *args):
#     with open(file_name, "a") as file:
#         file.write(f'{args[0]}\n')
#
#
# def replace(some_file_name, *args):
#     try:
#         with open(file_name) as file:
#             content = file.read()
#     except FileNotFoundError:
#         print("An error occurred")
#     else:
#         with open(file_name, "w") as file:
#             content = content.replace(args[0], args[1])
#             file.write(content)
#
#
# def delete(some_file_name):
#     if os.path.exists(file_name):
#         os.remove(file_name)
#     else:
#         print("An error occurred")
#
#
# while True:
#     line = input()
#     if line == "End":
#         break
#
#     command, file_name, *args = line.split("-")
#     if command == "Create":
#         create(file_name)
#     elif command == "Add":
#         add(file_name, *args)
#     elif command == "Replace":
#         replace(file_name, *args)
#     elif command == "Delete":
#         delete(file_name)
