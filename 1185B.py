def compress(text):
    result = []
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result.append((text[i - 1], count))
            count = 1
    result.append((text[-1], count))
    return result

def is_polycrap(first, second):
    if len(first) != len(second):
        return False
    for i in range(len(first)):
        if first[i][0] != second[i][0]:
            return False
        else:
            if(first[i][1] > second[i][1]):
                return False
    return True

for _ in range(int(input())):
    print('YES' if is_polycrap(first = compress(input()), second = compress(input())) else 'NO')
