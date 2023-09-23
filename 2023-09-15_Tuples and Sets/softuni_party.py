n = int(input())

reservations = set()

for _ in range(n):
    res_number = input()
    reservations.add(res_number)

while True:
    guest = input()
    if guest == "END":
        break
    reservations.remove(guest)

print(len(reservations))
for num in sorted(reservations):
    print(num)