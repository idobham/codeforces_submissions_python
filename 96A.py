players = input()
temp = 0
dangerous_situation = False
for i in range(len(players) - 1):
    if players[i] == players[i + 1]:
        temp += 1
    else:
        temp = 0
    ##print(temp)
    if temp >= 6:
        dangerous_situation = True
        break
print("YES" if dangerous_situation else "NO")
