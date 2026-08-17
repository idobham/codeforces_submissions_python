for _ in range(int(input())):
    numbers_dict = {}
    input()
    numbers =  list(map(int, input().split()))
    for i, number in enumerate(numbers):
        if number - (i + 1) in numbers_dict:
            numbers_dict[number - (i + 1)] += 1
        else:
            numbers_dict[number - (i + 1)] = 1
    final = 0
    biggest = max(numbers_dict.values())
    possibilities = [0]
    for i in range(biggest):
        possibilities.append(possibilities[i] + (i + 1))
    for value in numbers_dict.values():
        if value - 1 > 0:
            final += possibilities[value - 1]
    print(final)