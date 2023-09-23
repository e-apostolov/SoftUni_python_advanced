from collections import deque

sq_chocolate = deque([int(x) for x in input().split(",")])
sq_cups = deque(int(x) for x in input().split(","))

chocolate_milkshakes = 0

while sq_chocolate and sq_cups and chocolate_milkshakes < 5:

    if sq_chocolate[-1] <= 0 and sq_cups[0] <= 0:
        sq_chocolate.pop()
        sq_cups.popleft()
        continue
    if sq_chocolate[-1] <= 0:
        sq_chocolate.pop()
        continue
    if sq_cups[0] <= 0:
        sq_cups.popleft()
        continue
    if sq_chocolate[-1] == sq_cups[0]:
        chocolate_milkshakes += 1
        sq_chocolate.pop()
        sq_cups.popleft()
    else:
        sq_chocolate[-1] -= 5
        if sq_chocolate[-1] < 0:
            sq_chocolate.pop()
        sq_cups.rotate(-1)

if chocolate_milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")


print(f"Chocolate: {', '.join(str(x) for x in sq_chocolate) if sq_chocolate else 'empty'}")
print(f"Milk: {', '.join(str(x) for x in sq_cups) if sq_cups else 'empty'}")
