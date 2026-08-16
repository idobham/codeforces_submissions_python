total_and_score = list(map(int, input().split(' ')))
total_numbers = total_and_score[0]
required_participants = total_and_score[1]
participants_score = list(map(int, input().split(' ')))

required_score = participants_score[required_participants - 1]
passed_participants = 0
for i in range(total_numbers):
    if participants_score[i] >= required_score and participants_score[i] > 0:
        passed_participants += 1

print(passed_participants)
