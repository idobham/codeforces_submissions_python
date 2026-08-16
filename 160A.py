coin_count = int(input())
coins = list(map(int, input().split()))

total_amount = sum(coins)
sorted_coins = sorted(coins, reverse=True)
current_amount = 0
coins_count = 0
for i in sorted_coins:
    current_amount += i
    coins_count += 1
    if current_amount > int(total_amount / 2):
        #print(current_amount, total_amount)
        print(coins_count)
        break
