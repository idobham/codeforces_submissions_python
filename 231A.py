count = int(input())
total_errors = 0
for i in range(count):
    team_errors = list(map(int, input().split(' ')))
    ##if sum(team_errors[0],team_errors[-1])
    if sum(team_errors) >= 2:
        total_errors += 1

print(total_errors)