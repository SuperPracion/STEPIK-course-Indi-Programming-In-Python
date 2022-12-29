num1, num2, action = input(), input(), input()

try:
    print(eval(f'{num1} {action} {num2}'))
except:
    print('Неизвестно')