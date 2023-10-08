import os


extension_dict = {}

directory = "../"


def get_files(folder, level):
    if level < 0:
        return
    for element in os.listdir(folder):
        file = os.path.join(folder, element)
        if os.path.isfile(file):
            extension = file.split(".")[-1]
            if extension not in extension_dict:
                extension_dict[extension] = []
            extension_dict[extension].append(element)
        else:
            get_files(file, level-1)


get_files(directory, 1)

# """Solution 2 without recursion"""
# for element in os.listdir(directory):
#     file = os.path.join(directory, element)
#     if os.path.isfile(file):
#         extension = file.split(".")[-1]
#         if extension not in extension_dict:
#             extension_dict[extension] = []
#         extension_dict[extension].append(element)
#     else:
#         for el in os.listdir(file):
#             f = os.path.join(file, el)
#             if os.path.isfile(f):
#                 ext = el.split(".")[-1]
#                 if ext not in extension_dict:
#                     extension_dict[ext] = []
#                 extension_dict[ext].append(el)

with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for ext, file_names in sorted(extension_dict.items()):
        output_file.write(f".{ext}\n")
        for file_name in sorted(file_names):
            output_file.write(f"- - - {file_name}\n")