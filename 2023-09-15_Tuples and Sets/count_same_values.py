nums = tuple(float(x) for x in input().split())

occurrence = {}

for num in nums:
    if num not in occurrence:
        occurrence[num] = nums.count(num)
        print(f"{num} - {nums.count(num)} times")
