from functools import reduce


def multiply(*args):
    return reduce(lambda x, y: x * y, args, 1)

print(multiply(1, 2, 3))