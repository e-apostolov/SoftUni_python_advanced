from collections import deque

monsters = deque([int(x) for x in input().split(",")])
soldiers = [int(x) for x in input().split(",")]

total_kills = 0

while monsters and soldiers:

    current_monster = monsters.popleft()
    current_soldier = soldiers.pop()

    if current_soldier >= current_monster:
        total_kills += 1
        current_soldier -= current_monster
        if not soldiers and current_soldier > 0:
            soldiers.append(current_soldier)
        elif soldiers:
            soldiers[-1] += current_soldier
    else:
        current_monster -= current_soldier
        monsters.append(current_monster)

if not monsters:
    print("All monsters have been killed!")
if not soldiers:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {total_kills}")