rows, columns = [int(x) for x in input().split()]

start_ord = ord('a')

for row_index in range(rows):
    for column_index in range(columns):
        print(f"{chr(start_ord + row_index)}{chr(start_ord + row_index + column_index)}{chr(start_ord + row_index)}", end=' ')
    print()

