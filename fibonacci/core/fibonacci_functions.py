def create_sequence(n):
    sequence = [0, 1]
    for _ in range(n - 2):
        current = sequence[-1]
        previous = sequence[-2]
        next_number = current + previous
        sequence.append(next_number)
    return sequence


def locate_index(number, sequence):
    try:
        return f"The number - {number} is at index {sequence.index(number)}"
    except ValueError:
        return f"The number {number} is not in the sequence"

