from collections import deque

programmer_throughput = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

duck_type_dict = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while programmer_throughput and number_of_tasks:
    current_programmer = programmer_throughput.popleft()
    current_number = number_of_tasks.pop()
    result = current_programmer * current_number

    if 0 <= result <= 60:
        duck_type_dict["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        duck_type_dict["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        duck_type_dict["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        duck_type_dict["Small Yellow Rubber Ducky"] += 1
    else:
        number_of_tasks.append(current_number - 2)
        programmer_throughput.append(current_programmer)

print(f"Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, quantity in duck_type_dict.items():
    print(f"{duck}: {quantity}")

