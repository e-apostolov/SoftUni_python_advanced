from collections import deque

quantity_of_water = int(input())
water_line = deque()

while True:
    command = input()
    if command == "Start":
        break
    water_line.append(command)

while True:
    command = input()
    if command == "End":
        break
    data = command.split()
    if len(data) == 1:
        liters_to_give = int(data[0])
        person_name = water_line.popleft()
        if quantity_of_water >= liters_to_give:
            quantity_of_water -= liters_to_give
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    else:
        liters_to_add = int(data[1])
        quantity_of_water += liters_to_add

print(f"{quantity_of_water} liters left")

