from collections import deque

daily_portions = [int(x) for x in input().split(", ")]
stamina = deque([int(x) for x in input().split(", ")])

peaks = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])
climbed_peaks = []

peaks_dict = {
    "Vihren": 80,
    "Kutelo": 90,
    "Banski Suhodol": 100,
    "Polezhan": 60,
    "Kamenitza": 70
}
days = 0
peak_index = 0

for day in range(7):

    current_portion = daily_portions.pop()
    current_stamina = stamina.popleft()
    result = current_portion + current_stamina

    if peaks:
        if result >= peaks_dict[peaks[peak_index]]:
            climbed_peaks.append(peaks.popleft())
    else:
        break

    days += 1

if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if climbed_peaks:
    print("Conquered peaks:")
    print(*climbed_peaks, sep="\n")








