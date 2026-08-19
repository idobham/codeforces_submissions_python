guest_and_host = {}
word_pile = {}
guest = input()
host = input()
word = input()
for g in guest:
    if g not in guest_and_host:
        guest_and_host[g] = 1
    else:
        guest_and_host[g] += 1
for h in host:
    if h not in guest_and_host:
        guest_and_host[h] = 1
    else:
        guest_and_host[h] += 1
for w in word:
    if w not in word_pile:
        word_pile[w] = 1
    else:
        word_pile[w] += 1
is_possible = True
for g in guest_and_host:
    if g not in word_pile or word_pile[g] != guest_and_host[g]:
        is_possible = False
        break
for h in word_pile:
    if h not in guest_and_host:
        is_possible = False
        break

##print(guest_and_host)
##print(word_pile)
print('YES' if is_possible else 'NO')
