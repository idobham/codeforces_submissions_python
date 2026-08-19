initial_health, enemies = map(int, input().split())
duel_won = True
duels = []
for _ in range(enemies):
    enemy_health, bonus = map(int, input().split())
    duels.append([enemy_health, bonus])
duels.sort()

for duel in duels:
    if initial_health <= duel[0]:
        duel_won = False
        break
    else:
        initial_health += duel[1]

print('YES' if duel_won else 'NO')
