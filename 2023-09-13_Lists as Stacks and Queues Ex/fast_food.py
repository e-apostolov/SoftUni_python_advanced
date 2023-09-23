from collections import deque


food_quantity = int(input())
food_orders = deque([int(x) for x in input().split()])

print(max(food_orders))

while food_orders and food_orders[0] <= food_quantity:
    food_quantity -= food_orders[0]
    food_orders.popleft()

if food_orders:
    print("Orders left:", end="")
    while food_orders:
        print(f" {food_orders.popleft()}", end="")
else:
    print("Orders complete")