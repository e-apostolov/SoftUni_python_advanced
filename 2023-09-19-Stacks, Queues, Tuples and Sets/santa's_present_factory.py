from collections import deque

materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())

presents_dict = {
    "Doll": [150, 0],
    "Wooden train": [250, 0],
    "Teddy bear": [300, 0],
    "Bicycle": [400, 0]
}

while materials and magic:
    toy_crafted = False
    current_total_magic = materials[-1] * magic[0]
    if current_total_magic < 0:
        materials.append(materials.pop() + magic.popleft())
    elif materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.popleft()
    for points in presents_dict.values():
        if points[0] == current_total_magic:
            points[1] += 1
            materials.pop()
            magic.popleft()
            toy_crafted = True
            break
    if current_total_magic > 0 and not toy_crafted:
        materials[-1] += 15
        magic.popleft()

if presents_dict["Doll"][1] > 0 and presents_dict["Wooden train"][1] > 0 or\
        presents_dict["Teddy bear"][1] > 0 and presents_dict["Bicycle"][1] > 0:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(presents_dict.items()):
    if value[1] > 0:
        print(f"{key}: {value[1]}")




