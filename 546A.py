price, budget, count = list(map(int, input().split()))
total_amount = (price + (count * price)) * (count / 2)
if total_amount - budget < 0:
    print(0)
else:
    print(int(total_amount - budget))