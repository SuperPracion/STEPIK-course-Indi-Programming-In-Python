import functools

print(functools.reduce(lambda a, b: a * b, map(int, list(input()))))