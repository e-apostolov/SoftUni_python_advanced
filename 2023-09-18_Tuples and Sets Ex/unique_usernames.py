n = int(input())

usernames_set = set()

for _ in range(n):
    username = input()
    usernames_set.add(username)

print('\n'.join(usernames_set))
# print(*usernames_set, sep='\n')