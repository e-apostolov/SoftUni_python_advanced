n = int(input())

final_set = set()

for _ in range(n):
    current_set = set(input().split())
    final_set = final_set.union(current_set)

print(*final_set, sep='\n')
