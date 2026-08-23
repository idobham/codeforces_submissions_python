for _ in range(int(input())):
    input()
    numbers = list(map(int, input().split()))
    numbers_dict = dict()
    for number in numbers:
        if number not in numbers_dict:
            numbers_dict[number] = 1
        else:
            numbers_dict[number] += 1

    for key, value in numbers_dict.items():
        if value == 1:
            spy = key
            break
    print(numbers.index(spy) + 1)