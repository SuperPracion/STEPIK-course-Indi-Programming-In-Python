def calculate(x:float, y:float, operation:str='a') -> None:
    def addition(x, y):
        return x + y

    def subtraction(x, y):
        return x - y

    def division(x, y):
        if 0 in (x, y):
            return 'На ноль делить нельзя!'
        return x / y

    def multiplication(x, y):
        return x * y

    match operation:
        case 'a':
            print(addition(x, y))
        case 's':
            print(subtraction(x, y))
        case 'd':
            print(division(x, y))
        case 'm':
            print(multiplication(x, y))
        case _:
            print('Ошибка. Данной операции не существует')
