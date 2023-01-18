def text_decor(func):
    def inner(*args, **kwargs):
        print('Hello')
        func(*args, **kwargs)
        print('Goodbye!')
    return inner

@text_decor
def simple_func():
    print('I just simple python func')

simple_func()

@text_decor
def multiply(num1, num2):
    print(num1 * num2)

multiply(3, 5)