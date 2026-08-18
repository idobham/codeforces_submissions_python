numbers = []
for i in range(int(input())):
    numbers.append(input())
#print(len('7'))
for number in numbers:
    zero_count = 0
    for i in range(len(number)):
        if number[i] == '0':
            zero_count += 1

    print(len(number) - zero_count)
    for i in range(len(number)):
        if number[i] != '0':
            num = number[i]
            num += '0' * (len(number) - i - 1)
            print(num)

