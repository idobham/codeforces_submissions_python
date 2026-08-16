numbers = list(map(int, input().split('+')))
numbers.sort()
string_numbers = ''
for i in range(len(numbers)):
        string_numbers += str(numbers[i]) + '+'
string_numbers = string_numbers[:-1]
print(string_numbers)


