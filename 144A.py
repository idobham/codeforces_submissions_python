size = int(input())
heights = list(map(int, input().split()))
#print(heights)
min_height = min(heights)
max_height = max(heights)
should_be_first = should_be_last = 0
for i, height in enumerate(heights):
    if height == max_height:
        should_be_first = i
        break

for i, height in enumerate(reversed(heights)):
    if height == min_height:
        should_be_last = i
        break
result = 0
if size - (should_be_first + should_be_last) <= 0:
    result -= 1
result += should_be_first + should_be_last

if size == 2 and result != 0:
    result = 1

print(result)