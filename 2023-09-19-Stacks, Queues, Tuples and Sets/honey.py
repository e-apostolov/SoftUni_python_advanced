from collections import deque

bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
operators = deque(input().split())

operators_dict = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

total_honey = 0

while bees and nectar:
    if nectar[-1] >= bees[0]:
        total_honey += abs(operators_dict[operators[0]](bees[0], nectar[-1]))
        bees.popleft()
        nectar.pop()
        operators.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")




