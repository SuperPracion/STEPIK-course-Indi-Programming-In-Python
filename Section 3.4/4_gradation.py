age = int(input())

if age < 2:
    print('Младенец')
elif 2 <= age < 4:
    print('Малыш')
elif 4 <= age < 12:
    print('Ребенок')
elif 12 <= age < 19:
    print('Подросток')
elif 19 <= age < 65:
    print('Взрослый человек')
else:
    print('Пожилой человек')