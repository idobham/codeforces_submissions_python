home = {}
guest = {}

for _ in range(int(input())):
    numbers = input().split()
    if numbers[0] in home:
        home[numbers[0]] += 1
    else:
        home[numbers[0]] = 1
    if numbers[1] in guest:
        guest[numbers[1]] += 1
    else:
        guest[numbers[1]] = 1
total = 0
for number in home:
    if number in guest:
        total += (home[number] * guest[number])
print(total)
