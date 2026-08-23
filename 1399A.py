for _ in range(int(input())):
    input()
    numbers = list(map(int, input().split()))
    numbers.sort()
    is_true = True
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] >= 2:
            is_true = False
            break
    print('YES' if is_true else 'NO')