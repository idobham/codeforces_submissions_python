input()
flowers_list = list(map(int, input().split()))
flowers = {}
for flower in flowers_list:
    if flower in flowers:
        flowers[flower] += 1
    else:
        flowers[flower] = 1
most = max(flowers.keys())
least = min(flowers.keys())
if most == least:
    possibility = int((flowers[most] * (flowers[most] - 1)) / 2)
else:
    possibility = flowers[most] * flowers[least]
print(most - least, possibility)

