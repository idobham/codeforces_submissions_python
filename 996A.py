def least_bills(amount):
    total_bills = 0
    '''if amount % 100 == 0:
        total_bills = amount / 100
    else:
        remainder = amount % 100
        amount -= remainder
        total_bills += amount / 100
        ##print(total_bills, remainder, 100)
        if not remainder % 20 == 0:
            amount = remainder
            remainder = amount % 20
            amount -= remainder
            total_bills += amount / 20
            ##print(total_bills, remainder, 20)
            if not remainder % 10 == 0:
                amount = remainder
                remainder = amount % 10
                amount -= remainder
                total_bills += amount / 10
                ##print(total_bills, remainder, 10)
                if not remainder % 5 == 0:
                    amount = remainder
                    remainder = amount % 5
                    amount -= remainder
                    total_bills += amount / 5
                    ##print(total_bills, remainder, 5)
                    total_bills += remainder
                else:
                    total_bills += remainder / 5
            else:
                total_bills += remainder / 10
        else:
            total_bills += remainder / 20
            ## lets make it more python idiomatic
    '''
    remainder = 0
    total_bills += amount // 100
    remainder = amount % 100
    total_bills += remainder // 20
    remainder = remainder % 20
    total_bills += remainder // 10
    remainder = remainder % 10
    total_bills += remainder // 5
    remainder = remainder % 5
    total_bills += remainder
    return int(total_bills)

print(least_bills(int(input())))



