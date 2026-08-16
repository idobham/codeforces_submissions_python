lengths = list(map(int, input().split(' ')))
dominos = 0
x = lengths[0]
y = lengths[1]
dominos = (x * y) / 2
print(int(dominos))