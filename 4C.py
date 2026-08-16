users = {}

for i in range(int(input())):
    temp = input()
    if temp not in users:
        print('OK')
        users[temp] = 1
    else:
        users[temp] = users[temp] + 1
        print(temp , users[temp] - 1, sep='')