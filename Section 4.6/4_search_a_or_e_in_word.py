word = input()

while word:
    if word[0] in ('a', 'e'):
        print('Ага! Нашлась')
        break
    else:
        print(f'Текущая буква: {word[0]}')

    word = word[1:]
else:
    print('Распечатали все буквы')