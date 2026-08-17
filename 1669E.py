for i in range(int(input())):
    string_list = {}

    exactly_one = 0
    for j in range(int(input())):
        string = input()
        if string not in string_list:
            string_list[string] = 1
        else:
            string_list[string] += 1

    keys = list(string_list.keys())
    ##print(string_list)
    ##print(keys)
    for j in range(len(keys) - 1):
        for k in range(j + 1, len(keys)):
            if keys[j][0] == keys[k][0] and keys[j][1] != keys[k][1]:
                exactly_one += int(string_list[keys[j]]) * int(string_list[keys[k]])
            if keys[j][1] == keys[k][1] and keys[j][0] != keys[k][0]:
                exactly_one += int(string_list[keys[j]]) * int(string_list[keys[k]])

    print(exactly_one)

