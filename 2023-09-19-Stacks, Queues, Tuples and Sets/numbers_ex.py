def add(some_sequence, some_numbers):
    some_sequence.update(some_numbers)
    return some_sequence


def remove(some_sequence, some_numbers):
    # for number in some_numbers:
    #     if number in some_sequence:
    #         some_sequence.remove(number)
    some_sequence.difference_update(some_numbers)
    return some_sequence


def check_subset(sequence_1, sequence_2):
    if sequence_1.issubset(sequence_2) or sequence_2.issubset(sequence_1):
        return True
    else:
        return False


input_set_1, input_set_2 = set(int(x) for x in input().split()), set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0] + ' ' + line[1]
    numbers = [int(x) for x in line[2:]]
    if command == "Add First":
        add(input_set_1, numbers)
    elif command == "Add Second":
        add(input_set_2, numbers)
    elif command == "Remove First":
        remove(input_set_1, numbers)
    elif command == "Remove Second":
        remove(input_set_2, numbers)
    elif command == "Check Subset":
        print(check_subset(input_set_1, input_set_2))

print(*sorted(input_set_1), sep=", ")
print(*sorted(input_set_2), sep=", ")