def nums_sums(*args):
    negatives_sum = sum(x for x in args if x < 0)
    positive_sum = sum(x for x in args if x >= 0)
    return negatives_sum, positive_sum


input_sequence = [int(x) for x in input().split()]

sums_input_sequence = nums_sums(*input_sequence)
print(*sums_input_sequence, sep='\n')
if abs(sums_input_sequence[0]) > sums_input_sequence[1]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")