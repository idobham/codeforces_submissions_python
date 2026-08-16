starting_number = count = 0
count = int(input())
temp = None
for i in range(count):
    temp = input()
    if '+' in temp:
        starting_number += 1
    elif '-' in temp:
        starting_number -= 1

print(starting_number)