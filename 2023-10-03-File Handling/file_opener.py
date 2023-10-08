try:
    file = open("text.txt", "r")
    file.close()
    print("Found")
except FileNotFoundError:
    print("File not found")

