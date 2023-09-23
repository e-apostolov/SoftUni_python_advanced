from collections import deque

materials_sq = deque(int(x) for x in input().split())
magic_sq = deque(int(x) for x in input().split())

presents_dict = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}

crafted_presents = {}

while materials_sq and magic_sq:
    if materials_sq[-1] * magic_sq[0] in presents_dict.values():


