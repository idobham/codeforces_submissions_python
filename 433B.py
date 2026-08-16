final_price = total_stones = count = type = first = last = 0
stone_prices = []
total_stones = int(input())

##for i in range(total_stones):
##    stone_prices.append(int(input()))
stone_prices = list(map(int, input().split()))
count = int(input())

sorted_stone_prices = sorted(stone_prices)

for i in range(count):
    stone_type, first, last = map(int, input().split())
    if stone_type == 1:
        final_price = sum(stone_prices[first - 1 :last])
    else:
        final_price = sum(sorted_stone_prices[first - 1:last])
    print(final_price)


