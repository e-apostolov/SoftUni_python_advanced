from collections import deque

customer_list = deque()

while True:
    command = input()
    if command == "End":
        break
    elif command == "Paid":
        while customer_list:
            print(customer_list.popleft())
    else:
        customer_list.append(command)

print(f"{len(customer_list)} people remaining.")
