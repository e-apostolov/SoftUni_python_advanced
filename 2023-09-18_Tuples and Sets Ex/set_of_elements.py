n, m = (int(x) for x in input().split())


set_one = set()
set_two = set()

for _ in range(n):
    set_one.add(input())

for _ in range(m):
    set_two.add(input())

final_set = set_one & set_two
# final_set = set_one.intersection(set_two)
print('\n'.join(final_set))

