birthdays = {}

for _ in range(int(input())):
    name, day, month = input().split()
    birthdays[month] = birthdays.get(month, dict()) | {name: day}

for _ in range(int(input())):
    print(*sorted(birthdays.get(input(), ['Нет данных'])))