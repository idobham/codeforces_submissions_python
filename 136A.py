total_friends = int(input())
gift_swap = list(map(int, input().split()))
for i in range(total_friends):
    print(gift_swap.index(i + 1) + 1)
