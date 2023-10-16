def accommodate_new_pets(capacity: int, weight:float , *args):
    result = ""
    pets_dict = {}

    for pet_type, pet_weight in args:
        if capacity <= 0:
            result += "You did not manage to accommodate all pets!\n"
            break
        if pet_weight > weight:
            continue
        if pet_type not in pets_dict:
            pets_dict[pet_type] = 0
        pets_dict[pet_type] += 1
        capacity -= 1
    else:
        result += f"All pets are accommodated! Available capacity: {capacity}.\n"

    result += "Accommodated pets:\n"
    for pet, number in sorted(pets_dict.items(), key=lambda x: x[0]):
        result += f"{pet}: {number}\n"
    return result


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

