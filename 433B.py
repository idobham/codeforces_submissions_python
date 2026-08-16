final_price = total_stones = count = type = first = last = 0
stone_prices = []
total_stones = int(input())

stone_prices = list(map(int, input().split()))
count = int(input())

prefix_sum = [0]
for i in stone_prices:
    prefix_sum.append(prefix_sum[-1] + i)

sorted_stone_prices = sorted(stone_prices)
prefix_sum_sort = [0]
for i in sorted_stone_prices:
    prefix_sum_sort.append(prefix_sum_sort[-1] + i)

##print("prefix sum sort: " , prefix_sum_sort)
##print("prefix_sum: " , prefix_sum)



for i in range(count):
    stone_type, first, last = map(int, input().split())
    ##print("stone type: " + str(stone_type))
    ##print("first: " + str(first))
    ##print("last: " + str(last))
    if stone_type == 1:
        final_price = prefix_sum[last] - prefix_sum[first - 1]
        ##sub_stone_prices = stone_prices[first - 1 : last]
        ##final_price = sum(stone_prices[first - 1 :last])
    else:
        final_price = prefix_sum_sort[last] - prefix_sum_sort[first - 1]
        #final_price = sum(sorted_stone_prices[first - 1:last])
    print(final_price)



