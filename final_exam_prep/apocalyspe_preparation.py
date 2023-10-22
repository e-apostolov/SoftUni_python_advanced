from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]


healing_items_dict = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    result = current_textile + current_medicament

    if result == 30:
        healing_items_dict["Patch"] += 1
    elif result == 40:
        healing_items_dict["Bandage"] += 1
    elif result == 100:
        healing_items_dict["MedKit"] += 1
    elif result > 100:
        healing_items_dict["MedKit"] += 1
        if medicaments:
            element_to_update = medicaments.pop()
            element_to_update += (result - 100)
            medicaments.append(element_to_update)
        else:
            medicaments.append(result - 100)
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and medicaments:
    print("Textiles are empty.")
if not medicaments and textiles:
    print("Medicaments are empty.")
if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")

if healing_items_dict:
    for item, value in sorted(healing_items_dict.items(), key=lambda x: (-x[1], x[0])):
        if value > 0:
            print(f"{item} - {value}")

if medicaments:
    medicaments = reversed(medicaments)
    print(f"Medicaments left: {', '.join(str(x) for x in medicaments)}")

if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")


