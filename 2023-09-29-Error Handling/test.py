a = [int(x) for x in input().split()]

index = int(input())

try:
    print(a[index])
except IndexError:
    print("Invalid index")
except ValueError:
    print("Invalid index input type")
finally:
    print(f"{a}")

