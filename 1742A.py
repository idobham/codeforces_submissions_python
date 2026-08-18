total = int(input())
for i in range(total):
    numbers = list(map(int, input().split()))
    numbers.sort()
    print('YES' if numbers[0] + numbers[1] == numbers[2] else 'NO')
