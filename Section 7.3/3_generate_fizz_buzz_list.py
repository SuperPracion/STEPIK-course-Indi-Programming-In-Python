def generate_fizz_buzz_list(num):
    res = []
    for i in range(1, num + 1):
        if i % 15 == 0:
            res += 'FizzBuzz'
        elif i % 5 == 0:
            res += 'Buzz'
        elif i % 3 == 0:
            res += 'Fizz'
        else:
            res += i

    return res