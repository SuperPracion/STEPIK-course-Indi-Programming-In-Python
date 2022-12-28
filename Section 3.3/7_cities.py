first_city = input().lower().replace('ь', '')
second_city = input().lower()

print('Good' if first_city[-1] == second_city[0] else 'Bad')