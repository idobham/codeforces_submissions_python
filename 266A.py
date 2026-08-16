total_stones = int(input())
color_string = input()
neighbor_count = 0
for i in range(total_stones - 1):
    if color_string[i] == color_string[i + 1]:
        neighbor_count += 1
print(neighbor_count)